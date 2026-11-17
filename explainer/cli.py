"""Explain a sample of logged decisions and write a report.

    python -m explainer.cli explainer/sample/decisions_btc_2026-10-19.jsonl --per-action 3
    python -m explainer.cli <decisions.jsonl> --backend claude-cli     # your Claude login, no API key
    python -m explainer.cli <decisions.jsonl> --backend ollama         # a free local model
    LLM_API_KEY=... python -m explainer.cli <decisions.jsonl> --backend openai-compat \\
        --base-url https://api.groq.com/openai/v1 --model <model name>   # Groq, Gemini, OpenRouter, ...
    ANTHROPIC_API_KEY=... python -m explainer.cli <decisions.jsonl> --backend claude-api

The default backend is the deterministic template, which is also what a model's answer is replaced by if it
fails the number check.
"""

from __future__ import annotations

import argparse
import collections
import json
import os
import random
from pathlib import Path

from .explain import DEFAULT_MODEL, ClaudeAPIWriter, ClaudeCLIWriter, OllamaWriter, OpenAICompatWriter, explain
from .facts import ACTIONS, build_facts
from .page import card_data, render


def load(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def sample(recs: list[dict], per_action: int, policy: str | None, seed: int = 0) -> list[dict]:
    """per_action decisions of each kind, spread over the day, so every reason shows up."""
    rng = random.Random(seed)
    by_action: dict[str, list[dict]] = collections.defaultdict(list)
    for r in recs:
        if policy and r["policy"] != policy:
            continue
        by_action[r["action"]].append(r)
    out = []
    for a in ACTIONS:
        rows = by_action.get(a, [])
        out += sorted(rng.sample(rows, min(per_action, len(rows))), key=lambda r: r["t"])
    return out


def day_summary(recs: list[dict]) -> str:
    c: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    for r in recs:
        c[r["policy"]][r["action"]] += 1
    lines = []
    for p, cnt in sorted(c.items()):
        total = sum(cnt.values())
        parts = ", ".join(f"{a} {n}" for a, n in cnt.most_common())
        lines.append(f"{p}: {total} decisions ({parts})")
    return "\n".join(lines)


def summary_stats(recs: list[dict]) -> dict:
    by = collections.Counter((r["policy"], r["action"]) for r in recs)
    policies = {r["policy"] for r in recs}
    return {"total": max(sum(n for (p, _), n in by.items() if p == pol) for pol in policies),
            "sent": by[("naive", "ENTER")], "prior_sent": by[("prior", "ENTER")]}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("decisions", type=Path)
    ap.add_argument("--per-action", type=int, default=3)
    ap.add_argument("--policy", default=None, help="only this policy (naive, prior, slow)")
    ap.add_argument("--fee", type=float, default=1.0, help="the --fee the paper trader ran with (bps per leg)")
    ap.add_argument("--backend", choices=["template", "claude-cli", "claude-api", "ollama", "openai-compat"], default="template")
    ap.add_argument("--model", default=None, help="model name for the chosen backend")
    ap.add_argument("--base-url", default=None, help="for openai-compat: the service's API base URL")
    ap.add_argument("--key-env", default="LLM_API_KEY", help="for openai-compat: the environment variable holding the key")
    ap.add_argument("--out", type=Path, default=Path("explainer/report.html"))
    ap.add_argument("--render", type=Path, default=None,
                    help="re-render the page from a report.json written by an earlier run (no writer is called)")
    args = ap.parse_args()

    if args.render:
        data = json.loads(args.render.read_text())
        args.out.write_text(render(data["cards"], data["summary"]))
        print(f"re-rendered {len(data['cards'])} cards to {args.out}")
        return
    writer = None
    if args.backend == "claude-cli":
        writer = ClaudeCLIWriter(args.model)
    elif args.backend == "claude-api":
        import anthropic
        writer = ClaudeAPIWriter(anthropic.Anthropic(), args.model or DEFAULT_MODEL)
    elif args.backend == "openai-compat":
        if not (args.base_url and args.model):
            ap.error("--backend openai-compat needs --base-url and --model")
        writer = OpenAICompatWriter(args.base_url, args.model, args.key_env)
    elif args.backend == "ollama":
        writer = OllamaWriter(args.model or "llama3.2")
    recs = load(args.decisions)
    chosen = sample(recs, args.per_action, args.policy)
    cards, stats = [], collections.Counter()
    for r in chosen:
        f = build_facts(r, args.fee)
        e = explain(f, writer)
        stats[e.source] += 1
        cards.append(card_data(f, e))
        print(f"[{f['action']:<14}] {e.text}")
    summary = summary_stats(recs)
    args.out.with_suffix(".json").write_text(json.dumps({"cards": cards, "summary": summary}, indent=1))
    args.out.write_text(render(cards, summary))
    print(f"\n{len(chosen)} explained ({dict(stats)}); report written to {args.out}")


if __name__ == "__main__":
    main()
