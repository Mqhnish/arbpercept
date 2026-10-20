"""Inventory, funding and end-of-day flattening for cross-venue trades.

The replays credit each hedged trade with the whole gap it crossed. That is profit only if
the opposite positions the trade leaves on the two venues can later be closed for free.
They can't when one venue sits persistently above the other: in January 2024 Binance's BTC
perpetual traded 0.5-3 bps below Bybit's, so trades ran mostly one way, built up a long
position on one venue and a short on the other, and closing it means paying that same offset
back. Here the position is tracked through each day:

  cap       a trade that would push the net position beyond the cap is skipped (the order
            would not have been sent); trades that shrink the position are always allowed
  funding   at each funding time a long pays, and a short receives, the venue's rate on
            the position's notional
  flatten   what is left at the end of the day is closed with taker orders on both venues
            at the last quotes (realised), or valued at the two mids (mark, no costs)

Each day starts flat, so days stay independent for the day-bootstrap intervals.
Venue a and venue b are the pair's two legs; dq_a is the change of the position on venue a
(base units), and the position on venue b is always its negative.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from .replay import Leg


def _mid(leg: Leg, t: np.ndarray) -> np.ndarray:
    bid, ask, _, _ = leg.quote(np.asarray(t, dtype=np.int64))
    return (bid + ask) / 2


def account_day(t: np.ndarray, dq_a: np.ndarray, pnl: np.ndarray, leg_a: Leg, leg_b: Leg,
                funding_a: pd.DataFrame | None, funding_b: pd.DataFrame | None, day_start: int, day_end: int,
                cap_base: float, fee_a_bps: float, fee_b_bps: float) -> dict:
    """One day of trades (times in µs, already in the replay's own P&L terms) -> inventory-aware P&L."""
    t = np.asarray(t, dtype=np.int64)
    dq_a, pnl = np.asarray(dq_a, float), np.asarray(pnl, float)
    keep = np.zeros(len(t), bool)
    path_t, path_pos = [day_start], [0.0]
    pos, peak = 0.0, 0.0
    for i in np.argsort(t, kind="stable"):
        new = pos + dq_a[i]
        if abs(new) <= cap_base * (1 + 1e-9) or abs(new) < abs(pos):
            keep[i], pos = True, new
            path_t.append(int(t[i]))
            path_pos.append(pos)
            peak = max(peak, abs(pos))
    path_t, path_pos = np.asarray(path_t, np.int64), np.asarray(path_pos)

    def held(ts: np.ndarray) -> np.ndarray:  # position in force at each instant (trades strictly before it)
        return path_pos[np.searchsorted(path_t, ts, side="left") - 1]

    funding = 0.0
    for leg, fund, sign in ((leg_a, funding_a, 1.0), (leg_b, funding_b, -1.0)):
        if fund is None or fund.empty:
            continue
        f = fund[(fund.ts > day_start) & (fund.ts < day_end)]
        if f.empty:
            continue
        ts = f.ts.to_numpy(np.int64)
        funding += float(np.nansum(-sign * held(ts) * _mid(leg, ts) * f.rate.to_numpy()))

    t_close = np.array([day_end - 1], dtype=np.int64)
    bid_a, ask_a, _, _ = (x[0] for x in leg_a.quote(t_close))
    bid_b, ask_b, _, _ = (x[0] for x in leg_b.quote(t_close))
    px_a, px_b = (bid_a, ask_b) if pos > 0 else (ask_a, bid_b)  # sell longs at the bid, buy back shorts at the ask
    flatten_cash = pos * (px_a - px_b) if pos != 0 else 0.0
    flatten_fees = abs(pos) * (px_a * fee_a_bps + px_b * fee_b_bps) / 1e4 if pos != 0 else 0.0
    mark = pos * ((bid_a + ask_a) / 2 - (bid_b + ask_b) / 2) if pos != 0 else 0.0
    trade_pnl = float(pnl[keep].sum())
    return {"keep": keep, "trades": int(keep.sum()), "skipped_by_cap": int((~keep).sum()),
            "trade_pnl": trade_pnl, "funding": funding, "flatten": float(flatten_cash - flatten_fees),
            "mark": float(mark), "end_position": float(pos), "peak_position": float(peak),
            "realised": trade_pnl + funding + float(flatten_cash - flatten_fees),
            "marked": trade_pnl + funding + float(mark),
            "raw": float(pnl.sum())}
