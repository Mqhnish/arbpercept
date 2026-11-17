"""Measure writer attempts, independently of whether the fallback template passes.

Run from the repository root, for example:
    .venv/bin/python -m explainer.evaluate explainer/sample/decisions_btc_2026-10-19.jsonl \
        --count 50 --seed 0 --backend ollama --model llama3.2

Use --backend openai-compat --base-url <url> --model <name> with a key already
in LLM_API_KEY, or --backend claude-cli with your own Claude login. The default
is a template baseline, not a model evaluation. No API key is saved or printed.
The command prints JSON to stdout and does not replace the demo report.

Sampling is uniform without replacement after the optional policy filter, capped
at the available count. Rates are fractions of sampled decisions, not attempts.
Mean tries counts writer calls, including errors and empty responses. Failure
reasons count failed attempts: one attempt can have several reasons. Actions
absent from the sample have null rates/means; template baselines have a null
first-try pass rate. A verifier pass measures these checks, not reasoning quality.
"""

from __future__ import annotations

import argparse
import collections
import json
import random
from pathlib import Path

from .cli import load
from .explain import ClaudeCLIWriter, OllamaWriter, OpenAICompatWriter, explain
from .facts import ACTIONS, build_facts
from .verify import check


class _ObservedWriter:
    """Record attempts while leaving the production retry/fallback loop in charge."""

    def __init__(self, writer):
        self.writer = writer
        self.name = writer.name
        self.attempts = 0
        self.first_pass = False
        self.reasons = collections.Counter()
        self.passed = False

    def __call__(self, facts, feedback=None):
        self.attempts += 1
        try:
            text = self.writer(facts, feedback)
        except Exception as exc:
            # Service error messages can contain private URLs or credentials.
            self.reasons[f"writer_error: {type(exc).__name__}"] += 1
            raise
        if text is None:
            self.reasons["empty_response"] += 1
            return text
        result = check(text, facts)
        self.passed = result["ok"]
        if self.attempts == 1:
            self.first_pass = self.passed
        if result["unsupported_numbers"]:
            self.reasons["unsupported_numbers"] += 1
        if result["wrong_action"]:
            self.reasons["wrong_action"] += 1
        for problem in result["style"]:
            self.reasons[f"style: {problem}"] += 1
        return text


def _summarize(rows: list[dict], has_writer: bool) -> dict:
    n = len(rows)
    first = sum(row["first_pass"] for row in rows)
    reasons = collections.Counter()
    for row in rows:
        reasons.update(row["reasons"])
    return {"decisions": n, "first_try_passes": first,
            "first_try_pass_rate": first / n if n and has_writer else None,
            "mean_tries": sum(row["tries"] for row in rows) / n if n else None,
            "template_fallbacks": sum(row["fallback"] for row in rows),
            "failure_reasons": dict(sorted(reasons.items()))}


def evaluate(records: list[dict], writer=None, *, count: int = 50, seed: int = 0,
             policy: str | None = None, fee_bps_per_leg: float = 1.0) -> dict:
    """Evaluate any callable writer accepted by explain(), using its normal retry limit.

    Input records are decision-log dictionaries, not facts. Every sampled record
    is evaluated once, even if identical records occur in the input log.
    """
    if count <= 0:
        raise ValueError("count must be positive")
    eligible = [r for r in records if policy is None or r["policy"] == policy]
    if not eligible:
        raise ValueError("no decisions match the requested sample")
    chosen = random.Random(seed).sample(eligible, min(count, len(eligible)))
    rows = []
    for record in chosen:
        facts = build_facts(record, fee_bps_per_leg)
        observed = _ObservedWriter(writer) if writer is not None else None
        explain(facts, observed)
        rows.append({"action": facts["action"],
                     "first_pass": observed.first_pass if observed else False,
                     "tries": observed.attempts if observed else 0,
                     "fallback": not observed.passed if observed else False,
                     "reasons": observed.reasons if observed else {}})
    actions = list(dict.fromkeys([*ACTIONS, *(row["action"] for row in rows)]))
    return {"writer": writer.name if writer is not None else "template", "requested": count,
            "available": len(eligible), "sampled": len(chosen), "seed": seed, "policy": policy,
            "fee_bps_per_leg": fee_bps_per_leg,
            "overall": _summarize(rows, writer is not None),
            "by_action": {action: _summarize([r for r in rows if r["action"] == action], writer is not None)
                          for action in actions}}


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("decisions", type=Path)
    parser.add_argument("--count", type=int, default=50, help="total decisions to sample (default: 50)")
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--policy", default=None)
    parser.add_argument("--fee", type=float, default=1.0, help="paper trader fee in bps per leg")
    parser.add_argument("--backend", choices=["template", "claude-cli", "ollama", "openai-compat"],
                        default="template")
    parser.add_argument("--model", default=None)
    parser.add_argument("--base-url", default=None, help="OpenAI-compatible service API base URL")
    parser.add_argument("--key-env", default="LLM_API_KEY")
    args = parser.parse_args(argv)
    writer = None
    if args.backend == "claude-cli":
        writer = ClaudeCLIWriter(args.model)
    elif args.backend == "ollama":
        writer = OllamaWriter(args.model or "llama3.2")
    elif args.backend == "openai-compat":
        if not (args.base_url and args.model):
            parser.error("--backend openai-compat needs --base-url and --model")
        writer = OpenAICompatWriter(args.base_url, args.model, args.key_env)
    try:
        result = evaluate(load(args.decisions), writer, count=args.count, seed=args.seed,
                          policy=args.policy, fee_bps_per_leg=args.fee)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
