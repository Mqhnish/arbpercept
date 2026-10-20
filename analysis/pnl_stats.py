"""Uncertainty and regime breakdown for the P&L-vs-latency results.

    .venv/bin/python analysis/pnl_stats.py [--pair btc_perp_binance_bybit] [--tag _byday] [--fee 1.0]

Days are the resampling unit (trades within a day are not independent), 10,000 bootstrap
draws, percentile 95% intervals. Regimes are terciles of the validation days' realised
volatility on the pair's second leg.

For an --offset-aware run the P&L is pnl_rel (each trade net of the venues' usual offset).
That is a quick view: the reported result is analysis/inventory_check.py, which tracks
positions, funding and the day-end close.
"""

from __future__ import annotations

import argparse
import json

import numpy as np
import pandas as pd

from arbdata.config import load_config
from arbtrade.stats import boot_ci

SHOW_TAUS = [0, 1, 10, 50, 100]
NAMES = {"naive fast path": "Naive", "gap size only": "Gap size only", "fast path + decay prior": "Prior only",
         "slow model always": "Slow always", "latency-aware cascade": "Cascade"}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pair", default="btc_perp_binance_bybit")
    ap.add_argument("--tag", default="_byday")
    ap.add_argument("--fee", type=float, default=1.0, help="fee per leg (bps) to report, when the run has several")
    args = ap.parse_args()
    cfg = load_config()
    d = cfg.reports_dir / "pnl" / f"{args.pair}{args.tag}"
    days = pd.read_csv(d / "pnl_by_day.csv")
    days = days[days.strategy.isin(NAMES) & (days.fee_bps_per_leg == args.fee)]
    if days.empty:
        raise SystemExit(f"no rows at {args.fee} bps per leg in {d}")
    leg = cfg.pairs[args.pair].b
    rv = {q.stem: json.loads(q.read_text())["daily_rv_bps"] for q in (cfg.reports_dir / "quality" / leg).glob("*.json")}
    meta = json.loads((d / "meta.json").read_text()) if (d / "meta.json").exists() else {}
    value = "pnl_rel_usd" if meta.get("offset_aware") and "pnl_rel_usd" in days else "pnl_usd"
    names = {s: n for s, n in NAMES.items() if s in set(days.strategy)}  # older runs have no gap-size baseline

    lines = [f"# P&L uncertainty and regimes: {args.pair}", "",
             f"Mean net P&L per validation day (USD) with day-bootstrap 95% intervals. Fees {args.fee:g} bps per leg, $10k per trade. "
             + ("P&L net of the venues' usual offset (pnl_rel), positions not tracked: see inventory.md for the reported result."
                if value == "pnl_rel_usd" else ""), ""]
    for mode in ("optimistic", "conservative"):
        lines += [f"## {mode.capitalize()} fill bound", "",
                  "| Latency | Days | " + " | ".join(names.values()) + " | Cascade − Naive | Cascade − Slow always |",
                  "|---|---|" + "---|" * (len(names) + 2)]
        for tau in SHOW_TAUS:
            w = days[(days["mode"] == mode) & (days.tau_ms == tau)].pivot_table(index="date", columns="strategy", values=value)
            if w.empty or "latency-aware cascade" not in w:
                continue
            cells = []
            for s in names:
                x = w[s].to_numpy()
                lo, hi = boot_ci(x)
                cells.append(f"{x.mean():,.0f} [{lo:,.0f}, {hi:,.0f}]")
            for other in ("naive fast path", "slow model always"):
                dx = (w["latency-aware cascade"] - w[other]).to_numpy()
                lo, hi = boot_ci(dx)
                cells.append(f"{dx.mean():+,.0f} [{lo:+,.0f}, {hi:+,.0f}]")
            lines.append(f"| {tau} ms | {len(w)} | " + " | ".join(cells) + " |")
        lines.append("")

    # Regimes, at 10 ms
    w = days[days.tau_ms == 10].copy()
    w["rv"] = w.date.map(rv)
    dvals = w.drop_duplicates("date").set_index("date").rv.dropna()
    if len(dvals) >= 6:
        bucket = pd.qcut(dvals, 3, labels=["calm", "normal", "volatile"])
        w["regime"] = w.date.map(bucket)
        lines += ["## By volatility regime at 10 ms latency", "",
                  "| Fill bound | Regime | Days | " + " | ".join(names.values()) + " |", "|---|---|---|" + "---|" * len(names)]
        for (mode, reg), g in w.groupby(["mode", "regime"], observed=True):
            m = g.groupby("strategy")[value].mean()
            lines.append(f"| {mode} | {reg} | {g.date.nunique()} | " +
                         " | ".join(f"{m.get(s, np.nan):,.0f}" for s in names) + " |")
    out = d / ("stats.md" if args.fee == 1.0 else f"stats_fee{args.fee:g}.md")
    out.write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
