"""Re-score the taker strategies' trades with the positions they leave on the two venues.

    .venv/bin/python analysis/inventory_check.py [--tag _v3]

Reads trades.parquet written by `python -m arbtrade.evaluate --dump-trades`. For each
strategy, latency and fill bound, every validation day is replayed through
arbtrade/inventory.py: positions tracked, funding paid or received at each funding time,
the remainder closed with taker orders at the day's end, and optionally a cap on the
position ($50k = five $10k clips). Day-bootstrap 95% intervals, as in pnl_stats.py.
"""

from __future__ import annotations

import argparse

import numpy as np
import pandas as pd

from arbdata import pipeline as P
from arbdata.config import load_config
from arbdata.funding import load_funding
from arbtrade.inventory import account_day
from arbtrade.replay import Leg

CAP_USD = 50_000.0
DAY_US = 86_400_000_000
NAMES = {"naive fast path": "Naive", "fast path + decay prior": "Prior only",
         "slow model always": "Slow always", "latency-aware cascade": "Cascade"}


def boot(x: np.ndarray, reps: int = 10_000) -> tuple[float, float]:
    rng = np.random.default_rng(0)
    m = x[rng.integers(0, len(x), (reps, len(x)))].mean(1)
    return float(np.percentile(m, 2.5)), float(np.percentile(m, 97.5))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pair", default="btc_perp_binance_bybit")
    ap.add_argument("--tag", default="_v3")
    args = ap.parse_args()
    cfg = load_config()
    d = cfg.reports_dir / "pnl" / f"{args.pair}{args.tag}"
    tr = pd.read_parquet(d / "trades.parquet")
    spec = cfg.pairs[args.pair]
    sa, sb = cfg.streams[spec.a], cfg.streams[spec.b]
    fund = {k: load_funding(cfg, s.venue, s.symbol) for k, s in (("a", sa), ("b", sb))}
    res_a, res_b = cfg.source_cfg(spec.a)["resolution_ms"], cfg.source_cfg(spec.b)["resolution_ms"]

    rows = []
    for date, g_day in tr.groupby("date"):
        la = pd.read_parquet(cfg.l1_path(sa, date))
        lb = pd.read_parquet(cfg.l1_path(sb, date))
        legs = (Leg.from_l1(la, sampled=res_a > 1), Leg.from_l1(lb, sampled=res_b > 1))
        price = float(((la.bid_px + la.ask_px) / 2).mean())
        start = P.day_start_us(date)
        for (fee, mode, tau, strat), g in g_day.groupby(["fee_bps_per_leg", "mode", "tau_ms", "strategy"]):
            for cap_name, cap in (("no cap", np.inf), ("$50k cap", CAP_USD)):
                acc = account_day(g.t.to_numpy(), g.dq_a.to_numpy(), g.pnl.to_numpy(), *legs, fund["a"], fund["b"],
                                  start, start + DAY_US, cap / price, fee, fee)
                rows.append({"date": date, "fee": fee, "mode": mode, "tau_ms": tau, "strategy": strat, "cap": cap_name,
                             "trades": len(g), "one_way_share": max((g.dq_a > 0).mean(), (g.dq_a < 0).mean()),
                             "old": acc["raw"], "funding": acc["funding"], "flatten": acc["flatten"],
                             "realised": acc["realised"], "kept": acc["trades"]})
        print(date, "done", flush=True)
    df = pd.DataFrame(rows)
    df.to_csv(d / "inventory_by_day.csv", index=False)

    # Days with no trade for a strategy still count as $0 days.
    all_days = sorted(tr.date.unique())
    lines = [f"# Taker strategies with inventory accounted: {args.pair}", "",
             "Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. "
             "Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, "
             f"the remainder closed with taker orders at the day's end. Capped: no trade that takes the position past ${CAP_USD:,.0f}.", ""]
    for fee in sorted(df.fee.unique()):
        lines += [f"## Fees {fee:g} bps per leg", "",
                  "| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |",
                  "|---|---|---|---|---|---|---|"]
        for mode in ("optimistic", "conservative"):
            for tau in sorted(df.tau_ms.unique()):
                for strat, short in NAMES.items():
                    g = df[(df.fee == fee) & (df["mode"] == mode) & (df.tau_ms == tau) & (df.strategy == strat)]
                    if g.empty:
                        continue
                    cells = []
                    for col, cap in (("old", "no cap"), ("realised", "no cap"), ("realised", "$50k cap")):
                        x = g[g.cap == cap].set_index("date")[col].reindex(all_days, fill_value=0.0).to_numpy()
                        lo, hi = boot(x)
                        cells.append(f"{x.mean():,.0f} [{lo:,.0f}, {hi:,.0f}]")
                    share = np.average(g[g.cap == "no cap"].one_way_share, weights=g[g.cap == "no cap"].trades)
                    lines.append(f"| {mode} | {tau} ms | {short} | {share:.0%} | " + " | ".join(cells) + " |")
        lines.append("")
    (d / "inventory.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
