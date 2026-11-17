"""Explain a sample of logged decisions and write a report.

    python -m explainer.cli explainer/sample/decisions_btc_2026-10-19.jsonl --per-action 3
    ANTHROPIC_API_KEY=... python -m explainer.cli <decisions.jsonl> --claude

Without --claude (or without a key) the explanations come from the deterministic template, which is also
what Claude's answer is replaced by if it fails the number check.
"""

from __future__ import annotations

import argparse
import collections
import html
import json
import os
import random
from pathlib import Path

from .explain import DEFAULT_MODEL, explain
from .facts import ACTIONS, build_facts


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


PAGE = """<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Why did it trade?</title>
<style>
:root{{--bg:#fafaf7;--ink:#1c1c1a;--mut:#6b6b64;--card:#fff;--line:#e4e3dc;--ok:#1f7a4d;--skip:#8a5a00;--bad:#a12626}}
@media (prefers-color-scheme:dark){{:root{{--bg:#151513;--ink:#ecebe5;--mut:#9a9990;--card:#1e1e1b;--line:#33332e;--ok:#5bc48b;--skip:#e0a84a;--bad:#e06c6c}}}}
body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 ui-sans-serif,system-ui,sans-serif}}
main{{max-width:760px;margin:0 auto;padding:32px 16px 64px}}
h1{{font-size:26px;margin:0 0 4px}} .sub{{color:var(--mut);margin:0 0 24px}}
pre{{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:12px;overflow:auto;font-size:13px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px;margin:12px 0}}
.top{{display:flex;gap:8px;align-items:center;flex-wrap:wrap;font-size:13px;color:var(--mut)}}
.tag{{font-weight:600;padding:1px 8px;border-radius:99px;border:1px solid currentColor}}
.ENTER{{color:var(--ok)}} .SKIP_EV,.SKIP_THIN,.SKIP_STALE,.SKIP_INVENTORY{{color:var(--skip)}}
.card p{{margin:8px 0 6px}} details{{color:var(--mut);font-size:13px}}
.v{{font-size:12px;color:var(--ok)}} .v.no{{color:var(--bad)}}
</style>
<main>
<h1>Why did it trade?</h1>
<p class="sub">Decisions from the paper trader's log, each explained in plain English. Every number in an explanation is
checked against the log; the log line is under each one.</p>
<pre>{summary}</pre>
{cards}
</main>
"""


def card(f: dict, e) -> str:
    badge = ('<span class="v">numbers checked against the log</span>' if e.verified
             else '<span class="v no">not verified</span>')
    return (f'<div class="card"><div class="top"><span class="tag {f["action"]}">{f["action"]}</span>'
            f'<span>{html.escape(f["time_utc"])} UTC</span><span>{html.escape(f["policy"])}</span>'
            f'<span>{html.escape(e.source)}</span>{badge}</div>'
            f'<p>{html.escape(e.text)}</p>'
            f'<details><summary>The log line</summary><code>{html.escape(f["reason_text"])}</code> '
            f'(gap {f["gap_bps"]} bps, vs usual offset {f["gap_vs_usual_offset_bps"]} bps)</details></div>')


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("decisions", type=Path)
    ap.add_argument("--per-action", type=int, default=3)
    ap.add_argument("--policy", default=None, help="only this policy (naive, prior, slow)")
    ap.add_argument("--fee", type=float, default=1.0, help="the --fee the paper trader ran with (bps per leg)")
    ap.add_argument("--claude", action="store_true", help="ask Claude (needs ANTHROPIC_API_KEY or an ant login)")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--out", type=Path, default=Path("explainer/report.html"))
    args = ap.parse_args()

    client = None
    if args.claude:
        import anthropic
        client = anthropic.Anthropic()
    recs = load(args.decisions)
    chosen = sample(recs, args.per_action, args.policy)
    cards, stats = [], collections.Counter()
    for r in chosen:
        f = build_facts(r, args.fee)
        e = explain(f, client, args.model)
        stats[e.source] += 1
        cards.append(card(f, e))
        print(f"[{f['action']:<14}] {e.text}")
    args.out.write_text(PAGE.format(summary=html.escape(day_summary(recs)), cards="\n".join(cards)))
    print(f"\n{len(chosen)} explained ({dict(stats)}); report written to {args.out}")


if __name__ == "__main__":
    main()
