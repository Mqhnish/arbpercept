"""Sweep the maker-taker prototype over January 2024 (Bybit maker leg, Binance taker hedge),
with the positions it leaves on the two venues accounted for.

    .venv/bin/python analysis/maker_taker.py

Two quoting rules: the margin measured against zero (the original prototype), and against
the trailing 5-minute median offset between the venues (Binance mid minus Bybit mid).
Every configuration is scored three ways (see arbtrade/inventory.py):
  old accounting   each fill credited with the whole gap, positions assumed free to close
  realised         positions tracked through the day, funding paid or received at each
                   funding time, the remainder closed with taker orders at the day's end
  realised, capped as realised, and a fill that would push the position past $50k is not taken
  marked           as capped, but what is left at the day's end is valued at the two mids
                   instead of closed (an upper bound: closing costs nothing)

All January days are development data. To avoid reporting a tuned result as if it were out
of sample, the margin is chosen on the first 20 days (by capped realised P&L) and reported on
the last 11; the whole grid is written out as well.
"""

from __future__ import annotations

import itertools
import json

import numpy as np
import pandas as pd

from arbdata import pipeline as P
from arbdata.config import load_config
from arbdata.funding import load_funding
from arbtrade.inventory import CLOSE_WINDOW_S, account_day
from arbtrade.makertaker import Params, offset_reference, simulate
from arbtrade.replay import Leg
from arbtrade.stats import boot_ci

FEES = {"top tier (maker 0, taker 1.7)": (0.0, 1.7), "mid tier (1, 3)": (1.0, 3.0), "base tier (2, 5)": (2.0, 5.0)}
MARGINS = [0.5, 1.0, 2.0, 3.0, 5.0]
BINANCE_LAT = {"co-located (5 ms)": 5.0, "from here (50 ms)": 50.0}
RULES = {"vs zero": False, "vs trailing offset": True}
CAP_USD = 50_000.0
DAY_US = 86_400_000_000


def score_day(by, tr, bn, ref, legs, funding, day_start, mk, tk, margin, lat, use_ref, lat_bybit=8.0) -> list[dict]:
    p = Params(maker_fee_bps=mk, taker_fee_bps=tk, min_margin_bps=margin, lat_bybit_ms=lat_bybit, lat_binance_ms=lat)
    parts = []
    for side, sign in (("bid", -1.0), ("ask", 1.0)):  # bid: long Bybit, short Binance (venue a)
        r = simulate(by, tr, bn, side, p, ref if use_ref else None)
        if not r.empty:
            f = r[r.filled > 0]
            parts.append(pd.DataFrame({"t": f.t_fill, "dq_a": sign * f.filled, "pnl": f.pnl, "notional": f.filled * f.price}))
    fills = pd.concat(parts, ignore_index=True) if parts else pd.DataFrame(columns=["t", "dq_a", "pnl", "notional"])
    price = float(((by.bid_px + by.ask_px) / 2).mean())  # only to express the peak position in USD
    out = []
    for cap_name, cap in (("no cap", None), ("$50k cap", CAP_USD)):
        acc = account_day(fills.t.to_numpy(), fills.dq_a.to_numpy(), fills.pnl.to_numpy(), legs["a"], legs["b"],
                          funding["binance"], funding["bybit"], day_start, day_start + DAY_US, fee_a_bps=tk, fee_b_bps=tk,
                          cap_usd=cap, close_window_s=CLOSE_WINDOW_S)
        out.append({"cap": cap_name, "fills": acc["trades"], "skipped_by_cap": acc["skipped_by_cap"],
                    "one_way_share": float(max((fills.dq_a > 0).mean(), (fills.dq_a < 0).mean())) if len(fills) else np.nan,
                    "old_accounting": acc["raw"], "trade_pnl": acc["trade_pnl"], "funding": acc["funding"],
                    "flatten": acc["flatten"], "realised": acc["realised"], "marked": acc["marked"],
                    "peak_position_usd": acc["peak_position"] * price,
                    "filled_notional": float(fills.notional[acc["keep"]].sum()) if len(fills) else 0.0})
    return out


def main() -> None:
    cfg = load_config()
    bn_s, by_s = cfg.streams["binance_bt/binance/BTC-USDT/perp"], cfg.streams["bybit_ob/bybit/BTC-USDT/perp"]
    funding = {"binance": load_funding(cfg, "binance", "BTCUSDT"), "bybit": load_funding(cfg, "bybit", "BTCUSDT")}
    dates = sorted(p.stem for p in (cfg.data_root / "trades" / by_s.key).glob("2024-01-*.parquet"))
    rows = []
    for d in dates:
        qa = json.loads((cfg.reports_dir / "quality" / bn_s.key / f"{d}.json").read_text())
        qb = json.loads((cfg.reports_dir / "quality" / by_s.key / f"{d}.json").read_text())
        if not (qa["passes"] and qb["passes"]):
            continue
        bn = pd.read_parquet(cfg.l1_path(bn_s, d))
        by = pd.read_parquet(cfg.l1_path(by_s, d))
        tr = pd.read_parquet(cfg.trades_path(by_s, d))
        legs = {"a": Leg.from_l1(bn, sampled=False), "b": Leg.from_l1(by, sampled=True)}
        ref = offset_reference(by, bn)
        day_start = P.day_start_us(d)
        for (fname, (mk, tk)), m, (lname, lat), (rname, use_ref) in itertools.product(
                FEES.items(), MARGINS, BINANCE_LAT.items(), RULES.items()):
            for r in score_day(by, tr, bn, ref, legs, funding, day_start, mk, tk, m, lat, use_ref,
                               cfg.latency_ms.get("bybit", 8.0)):
                rows.append({"date": d, "fees": fname, "margin_bps": m, "latency": lname, "rule": rname, **r})
        print(d, "done", flush=True)
    df = pd.DataFrame(rows)
    out = cfg.reports_dir / "maker_taker"
    out.mkdir(parents=True, exist_ok=True)
    df.to_csv(out / "by_day.csv", index=False)

    days = sorted(df.date.unique())
    sel_days, rep_days = days[:20], days[20:]
    lines = ["# Maker-taker prototype, January 2024 (Bybit maker, Binance taker hedge), with inventory", "",
             f"{len(days)} days. Margin chosen on the first {len(sel_days)} days by capped realised P&L; "
             f"everything below is the last {len(rep_days)} days.",
             f"Bybit latency {cfg.latency_ms.get('bybit', 8.0):g} ms; one order per quoting spell; queue cancellations "
             "ignored (pessimistic); each partial fill hedged on its own.",
             "Old accounting: each fill credited with the whole gap. Realised: positions tracked, funding paid or "
             f"received, no new fills in the day's last {CLOSE_WINDOW_S:g} s while the position is closed with taker orders, "
             "never taking more than both books show. Capped: no fill that would take the "
             f"position past ${CAP_USD:,.0f} at the price of that fill.", "",
             "| Fees (bps) | Binance latency | Quoting rule | Margin | Fills per day | Fills going one way | Old accounting | "
             "Realised, no cap | Realised, capped | 95% interval (capped) | Marked, capped |",
             "|---|---|---|---|---|---|---|---|---|---|---|"]
    for (fname, lname, rname), g in df.groupby(["fees", "latency", "rule"], sort=False):
        capped = g[g.cap == "$50k cap"]
        m = float(capped[capped.date.isin(sel_days)].groupby("margin_bps").realised.mean().idxmax())
        rep = g[(g.margin_bps == m) & g.date.isin(rep_days)]
        c, u = rep[rep.cap == "$50k cap"], rep[rep.cap == "no cap"]
        lo, hi = boot_ci(c.realised.to_numpy())
        lines.append(f"| {fname} | {lname} | {rname} | {m:g} | {u.fills.mean():,.0f} | {u.one_way_share.mean():.0%} | "
                     f"${u.old_accounting.mean():,.0f} | ${u.realised.mean():,.0f} | ${c.realised.mean():,.0f} | "
                     f"[{lo:,.0f}, {hi:,.0f}] | ${c.marked.mean():,.0f} |")
    lines += ["", "Per-day components (trade P&L, funding, closing cost, peak position) for every configuration: `by_day.csv`."]
    (out / "summary.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
