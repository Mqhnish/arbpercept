"""Maker-taker on today's market, from our own recordings (Bybit 10 ms book + trades, Binance ticks).

    .venv/bin/python analysis/maker_taker_live.py 2026-10-19 2026-10-20

Same simulator and accounting as analysis/maker_taker.py: both quoting rules, positions
tracked and capped at $50k, and whatever is left at the end of each recorded stretch closed
with taker orders. Funding: Bybit's rates only (Binance's October file is not published yet
and its API refuses this region), so the Binance side of any carried position pays nothing.
The clocks are our receive time for books and the matching-engine time for Bybit trades.
Hours of data only: a first look, not a result.
"""

from __future__ import annotations

import argparse
import itertools

import numpy as np
import pandas as pd

from arbdata.config import load_config
from arbdata.funding import load_funding
from arbdata.normalize import normalize_binance_live, normalize_bybit_live, normalize_bybit_live_trades
from arbtrade.inventory import account_day
from arbtrade.makertaker import Params, offset_reference, simulate
from arbtrade.replay import Leg

FEES = {"top tier (0 / 1.7)": (0.0, 1.7), "mid tier (1 / 3)": (1.0, 3.0)}
MARGINS = [1.0, 3.0]
LAT = {"co-located (5 ms)": 5.0, "from here (50 ms)": 50.0}
RULES = {"vs zero": False, "vs trailing offset": True}
CAP_USD = 50_000.0


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("dates", nargs="+")
    args = ap.parse_args()
    cfg = load_config()
    rows = []
    for asset in ("BTC", "ETH"):
        pair = f"{asset}-USDT"
        fund_by = load_funding(cfg, "bybit", f"{asset}USDT")
        for d in args.dates:
            bn, _ = normalize_binance_live(cfg.raw_path(cfg.streams[f"binance_live/binance/{pair}/perp"], d, ""))
            by_dir = cfg.raw_path(cfg.streams[f"bybit_live/bybit/{pair}/perp"], d, "")
            by, _ = normalize_bybit_live(by_dir)
            tr = normalize_bybit_live_trades(by_dir)
            if bn.empty or by.empty or tr.empty:
                continue
            lo = int(max(bn.avail_ts.min(), by.avail_ts.min()))
            hi = int(min(bn.avail_ts.max(), by.avail_ts.max()))
            by = by[by.avail_ts >= lo]
            legs = (Leg.from_l1(bn, sampled=False), Leg.from_l1(by, sampled=False))
            ref = offset_reference(by, bn)
            price = float(((by.bid_px + by.ask_px) / 2).mean())
            for (fname, (mk, tk)), m, (lname, lat), (rname, use_ref) in itertools.product(
                    FEES.items(), MARGINS, LAT.items(), RULES.items()):
                p = Params(maker_fee_bps=mk, taker_fee_bps=tk, min_margin_bps=m, lat_bybit_ms=8.0, lat_binance_ms=lat)
                parts = []
                for side, sign in (("bid", -1.0), ("ask", 1.0)):
                    r = simulate(by, tr, bn, side, p, ref if use_ref else None)
                    if not r.empty:
                        f = r[r.filled > 0]
                        parts.append(pd.DataFrame({"t": f.t_fill, "dq_a": sign * f.filled, "pnl": f.pnl}))
                fills = pd.concat(parts, ignore_index=True) if parts else pd.DataFrame(columns=["t", "dq_a", "pnl"])
                acc = account_day(fills.t.to_numpy(), fills.dq_a.to_numpy(), fills.pnl.to_numpy(), *legs,
                                  None, fund_by, lo, hi + 1, CAP_USD / price, tk, tk)
                rows.append({"asset": asset, "date": d, "hours": (hi - lo) / 3.6e9, "fees": fname, "margin": m,
                             "latency": lname, "rule": rname, "fills": len(fills), "kept": acc["trades"],
                             "one_way": float(max((fills.dq_a > 0).mean(), (fills.dq_a < 0).mean())) if len(fills) else np.nan,
                             "old": acc["raw"], "realised": acc["realised"]})
    df = pd.DataFrame(rows)
    hrs = df.drop_duplicates(["asset", "date"]).groupby("asset").hours.sum()
    g = df.groupby(["asset", "fees", "latency", "rule", "margin"], sort=False).agg(
        fills=("fills", "sum"), kept=("kept", "sum"), old=("old", "sum"), realised=("realised", "sum")).reset_index()
    for c in ("fills", "old", "realised"):
        g[c] = g[c] / g.asset.map(hrs)
    lines = [f"# Maker-taker on today's market ({', '.join(args.dates)}), first look", "",
             ", ".join(f"{a}: {h:.1f} h" for a, h in hrs.items()) + " of overlapping recordings. Bybit latency 8 ms, $10k clips. "
             f"Per hour. Realised: positions capped at ${CAP_USD:,.0f}, Bybit funding, the remainder closed with taker orders "
             "at the end of each recorded stretch.", "",
             "| Asset | Fees (maker / taker bps) | Binance latency | Quoting rule | Margin (bps) | Fills per hour | Old accounting | Realised, capped |",
             "|---|---|---|---|---|---|---|---|"]
    for _, r in g.iterrows():
        lines.append(f"| {r.asset} | {r.fees} | {r.latency} | {r.rule} | {r.margin:g} | {r.fills:,.1f} | "
                     f"${r.old:,.2f} | ${r.realised:,.2f} |")
    out = cfg.reports_dir / "maker_taker" / "live_first_look.md"
    out.write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
