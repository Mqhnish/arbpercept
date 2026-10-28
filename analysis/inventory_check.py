"""Re-score the taker strategies' trades with the positions they leave on the two venues.

    .venv/bin/python analysis/inventory_check.py [--tag _v3] [--baseline-tag _v4_offset]

Reads trades.parquet written by `python -m arbtrade.evaluate --dump-trades`. For each
strategy, latency and fill bound, every validation day is replayed through
arbtrade/inventory.py: positions tracked, funding paid or received at each funding time,
no new trades in the day's last --close-window-s seconds while the position is worked down
without taking more than the books show (0 = close at the last quotes, as before), and
optionally a cap on the position ($50k = five $10k clips, converted at the price of each trade).

Validation days without a trade count as $0 days (the day list comes from meta.json).
The closing is reported in two parts: what was really traded within the displayed size, and
what was booked for the rest at the last quotes (an assumption). The capped result is also
shown with an extra 5, 10 and 25 bps charged on that rest, to show how much it leans on it.
Day-bootstrap 95% intervals, with paired differences against the naive and gap-size-only
baselines, and against an earlier run when --baseline-tag is given.
"""

from __future__ import annotations

import argparse
import json

import numpy as np
import pandas as pd

from arbdata import pipeline as P
from arbdata.config import load_config
from arbdata.funding import load_funding
from arbtrade.inventory import CLOSE_WINDOW_S, RESIDUAL_COST_BPS, account_day, with_residual_cost
from arbtrade.replay import Leg
from arbtrade.stats import boot_ci, paired_diff

CAP_USD = 50_000.0
DAY_US = 86_400_000_000
NAMES = {"naive fast path": "Naive", "gap size only": "Gap size only", "fast path + decay prior": "Prior only",
         "slow model always": "Slow always", "latency-aware cascade": "Cascade"}
# Paired comparisons reported for every setting: (strategy, against)
PAIRS = [("latency-aware cascade", "naive fast path"), ("latency-aware cascade", "slow model always"),
         ("fast path + decay prior", "gap size only"), ("latency-aware cascade", "gap size only")]


def validation_days(d, tr: pd.DataFrame, fee: float) -> list[str]:
    """Every validation day of the run at this fee, including days without a single trade."""
    meta_path = d / "meta.json"
    if meta_path.exists():
        per_fold = json.loads(meta_path.read_text()).get("val_days", {}).get(str(float(fee)))
        if per_fold:
            return sorted({day for days in per_fold.values() for day in days})
    return sorted(tr[tr.fee_bps_per_leg == fee].date.unique())  # older runs: days with at least one trade


def fmt(m: float, lo: float, hi: float, signed: bool = False) -> str:
    s = "+," if signed else ","
    return f"{m:{s}.0f} [{lo:{s}.0f}, {hi:{s}.0f}]"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pair", default="btc_perp_binance_bybit")
    ap.add_argument("--tag", default="_v3")
    ap.add_argument("--baseline-tag", default=None, help="an earlier run to compare against, day by day")
    ap.add_argument("--close-window-s", type=float, default=CLOSE_WINDOW_S,
                    help="stop trading and work the close over the day's last seconds; 0 = close at the last quotes")
    args = ap.parse_args()
    cfg = load_config()
    d = cfg.reports_dir / "pnl" / f"{args.pair}{args.tag}"
    tr = pd.read_parquet(d / "trades.parquet")
    if "fee_a_bps" not in tr:  # older dumps: the same fee on both legs
        tr["fee_a_bps"] = tr["fee_b_bps"] = tr.fee_bps_per_leg
    spec = cfg.pairs[args.pair]
    sa, sb = cfg.streams[spec.a], cfg.streams[spec.b]
    fund = {k: load_funding(cfg, s.venue, s.symbol) for k, s in (("a", sa), ("b", sb))}
    res_a, res_b = cfg.source_cfg(spec.a)["resolution_ms"], cfg.source_cfg(spec.b)["resolution_ms"]

    rows = []
    for date, g_day in tr.groupby("date"):
        la = pd.read_parquet(cfg.l1_path(sa, date))
        lb = pd.read_parquet(cfg.l1_path(sb, date))
        legs = (Leg.from_l1(la, sampled=res_a > 1), Leg.from_l1(lb, sampled=res_b > 1))
        start = P.day_start_us(date)
        for (fee, fa, fb, mode, tau, strat), g in g_day.groupby(
                ["fee_bps_per_leg", "fee_a_bps", "fee_b_bps", "mode", "tau_ms", "strategy"]):
            for cap_name, cap in (("no cap", None), ("$50k cap", CAP_USD)):
                acc = account_day(g.t.to_numpy(), g.dq_a.to_numpy(), g.pnl.to_numpy(), *legs, fund["a"], fund["b"],
                                  start, start + DAY_US, fee_a_bps=fa, fee_b_bps=fb, cap_usd=cap,
                                  close_window_s=args.close_window_s)
                rows.append({"date": date, "fee": fee, "mode": mode, "tau_ms": tau, "strategy": strat, "cap": cap_name,
                             "trades": len(g), "one_way_share": max((g.dq_a > 0).mean(), (g.dq_a < 0).mean()),
                             "old": acc["raw"], "funding": acc["funding"], "flatten": acc["flatten"],
                             "close_unfilled": acc["close_unfilled"], "close_executed": acc["close_executed"],
                             "close_assumed": acc["close_assumed"], "residual_usd": acc["residual_usd"],
                             "realised": acc["realised"], "kept": acc["trades"]})
        print(date, "done", flush=True)
    df = pd.DataFrame(rows)
    df.to_csv(d / "inventory_by_day.csv", index=False)
    base = None
    if args.baseline_tag:
        base = pd.read_csv(cfg.reports_dir / "pnl" / f"{args.pair}{args.baseline_tag}" / "inventory_by_day.csv")

    close = (f"no new trades in the day's last {args.close_window_s:g} s while the position is worked down, never "
             "taking more than both books show" if args.close_window_s > 0 else "the remainder closed at the last quotes")
    lines = [f"# Taker strategies with inventory accounted: {args.pair}", "",
             "Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. "
             "Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, "
             f"{close}. Capped: no trade that takes the position past ${CAP_USD:,.0f} at the price of that trade. "
             "Validation days without a trade count as $0. Optimistic and conservative are two simulation assumptions "
             "about the sampled Bybit book between snapshots, not guaranteed bounds on the truth.", ""]
    for fee in sorted(df.fee.unique()):
        all_days = validation_days(d, tr, fee)
        realised = lambda g, cap="$50k cap": g[g.cap == cap].set_index("date")["realised"]
        lines += [f"## Fees {fee:g} bps per leg (average of the two venues)", "", f"{len(all_days)} validation days.", "",
                  "| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |",
                  "|---|---|---|---|---|---|---|"]
        diff_lines = ["", "Paired differences, realised and capped (same days resampled for both):", "",
                      "| Fill bound | Latency | Comparison | Difference per day |", "|---|---|---|---|"]
        stress = " | ".join(f"+{c:g} bps" for c in RESIDUAL_COST_BPS)
        close_lines = ["", "Closing, capped. Executed: really traded within the displayed size. Assumed: the rest, "
                       "booked at the last quotes whatever their size. The last columns charge an extra cost on that rest.", "",
                       f"| Fill bound | Latency | Strategy | Days with a rest | Rest, mean USD | Executed | Assumed | {stress} |",
                       "|---|---|---|---|---|---|---|" + "---|" * len(RESIDUAL_COST_BPS)]
        base_lines = ["", f"Against the earlier run `{args.baseline_tag}`, realised and capped:", "",
                      "| Fill bound | Latency | Strategy | This run − earlier run |", "|---|---|---|---|"]
        for mode in ("optimistic", "conservative"):
            for tau in sorted(df.tau_ms.unique()):
                here = df[(df.fee == fee) & (df["mode"] == mode) & (df.tau_ms == tau)]
                for strat, short in NAMES.items():
                    g = here[here.strategy == strat]
                    if g.empty:
                        continue
                    cells = []
                    for col, cap in (("old", "no cap"), ("realised", "no cap"), ("realised", "$50k cap")):
                        x = g[g.cap == cap].set_index("date")[col].reindex(all_days, fill_value=0.0).to_numpy()
                        cells.append(fmt(x.mean(), *boot_ci(x)))
                    share = np.average(g[g.cap == "no cap"].one_way_share, weights=g[g.cap == "no cap"].trades)
                    lines.append(f"| {mode} | {tau} ms | {short} | {share:.0%} | " + " | ".join(cells) + " |")
                    c = g[g.cap == "$50k cap"].set_index("date").reindex(all_days, fill_value=0.0)
                    stressed = [with_residual_cost(c.realised, c.residual_usd, k).to_numpy() for k in RESIDUAL_COST_BPS]
                    close_lines.append(f"| {mode} | {tau} ms | {short} | {int((c.residual_usd > 0).sum())} of {len(c)} | "
                                       f"{c.residual_usd.mean():,.0f} | {c.close_executed.mean():+,.0f} | {c.close_assumed.mean():+,.0f} | "
                                       + " | ".join(fmt(x.mean(), *boot_ci(x)) for x in stressed) + " |")
                    if base is not None:
                        b = base[(base.fee == fee) & (base["mode"] == mode) & (base.tau_ms == tau) & (base.strategy == strat)]
                        if not b.empty:
                            days = sorted(set(all_days) | set(b.date))
                            base_lines.append(f"| {mode} | {tau} ms | {short} | {fmt(*paired_diff(realised(g), realised(b), days), signed=True)} |")
                for s, o in PAIRS:
                    gs, go = here[here.strategy == s], here[here.strategy == o]
                    if gs.empty or go.empty:
                        continue
                    diff_lines.append(f"| {mode} | {tau} ms | {NAMES[s]} − {NAMES[o]} | "
                                      f"{fmt(*paired_diff(realised(gs), realised(go), all_days), signed=True)} |")
        lines += diff_lines + close_lines + (base_lines if base is not None else []) + [""]
    (d / "inventory.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
