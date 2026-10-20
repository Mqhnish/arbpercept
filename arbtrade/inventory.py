"""Inventory, funding and end-of-day flattening for cross-venue trades.

The replays credit each hedged trade with the whole gap it crossed. That is profit only if
the opposite positions the trade leaves on the two venues can later be closed for free.
They can't when one venue sits persistently above the other: in January 2024 Binance's BTC
perpetual traded 0.5-3 bps below Bybit's, so trades ran mostly one way, built up a long
position on one venue and a short on the other, and closing it means paying that same offset
back. Here the position is tracked through each day:

  cap       a trade that would push the net position beyond the cap is skipped (the order
            would not have been sent); trades that shrink the position are always allowed.
            A cap in USD is converted at the price when each trade happens (no look-ahead)
  funding   at each funding time a long pays, and a short receives, the venue's rate on
            the position's notional
  flatten   what is left at the end of the day is closed with taker orders on both venues
            (realised), or valued at the two mids (mark, no costs). With close_window_s = 0
            it closes at the last quotes, whatever their size. With close_window_s > 0 no new
            trade is taken in the day's last close_window_s seconds, and the position is
            worked down at each quote update in that window, never taking more than both
            books show (a level we took from is used up until that venue's quote changes).
            Anything still open at the end is closed at the last quotes and reported as
            close_unfilled (base units), since its true cost is unknown

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


CLOSE_WINDOW_S = 60.0  # what the analysis scripts use: stop trading and work the close over the last minute


def _work_close(pos: float, leg_a: Leg, leg_b: Leg, t_from: int, t_to: int, fee_a_bps: float,
                fee_b_bps: float) -> tuple[float, float, float]:
    """Close pos (base units on venue a; venue b holds -pos) with taker orders at each quote update in
    [t_from, t_to), each clip limited to what both books show. Returns (cash, fees, still open)."""
    remaining = abs(pos)
    if remaining == 0 or t_to <= t_from:
        return 0.0, 0.0, remaining
    sell_a = pos > 0  # long on a: sell a at its bid, buy b back at its ask
    times = np.unique(np.concatenate([[t_from], leg_a.t[(leg_a.t >= t_from) & (leg_a.t < t_to)],
                                      leg_b.t[(leg_b.t >= t_from) & (leg_b.t < t_to)]]))
    ia = np.searchsorted(leg_a.t, times, side="right") - 1
    ib = np.searchsorted(leg_b.t, times, side="right") - 1
    cash = fees = 0.0
    used = {"a": (-1, 0.0), "b": (-1, 0.0)}  # (quote index, size already taken from it)
    for i_a, i_b in zip(ia, ib):
        if remaining <= 1e-12:
            break
        if i_a < 0 or i_b < 0:
            continue
        pa, sa = (leg_a.bid[i_a], leg_a.bid_sz[i_a]) if sell_a else (leg_a.ask[i_a], leg_a.ask_sz[i_a])
        pb, sb = (leg_b.ask[i_b], leg_b.ask_sz[i_b]) if sell_a else (leg_b.bid[i_b], leg_b.bid_sz[i_b])
        sa -= used["a"][1] if used["a"][0] == i_a else 0.0
        sb -= used["b"][1] if used["b"][0] == i_b else 0.0
        q = min(remaining, sa, sb)
        if not np.isfinite(q) or q <= 0 or np.isnan(pa) or np.isnan(pb):
            continue
        cash += q * (pa - pb) if sell_a else q * (pb - pa)
        fees += q * (pa * fee_a_bps + pb * fee_b_bps) / 1e4
        remaining -= q
        used["a"] = (i_a, (used["a"][1] if used["a"][0] == i_a else 0.0) + q)
        used["b"] = (i_b, (used["b"][1] if used["b"][0] == i_b else 0.0) + q)
    return cash, fees, remaining


def account_day(t: np.ndarray, dq_a: np.ndarray, pnl: np.ndarray, leg_a: Leg, leg_b: Leg,
                funding_a: pd.DataFrame | None, funding_b: pd.DataFrame | None, day_start: int, day_end: int,
                cap_base: float = np.inf, fee_a_bps: float = 0.0, fee_b_bps: float = 0.0,
                cap_usd: float | None = None, close_window_s: float = 0.0) -> dict:
    """One day of trades (times in µs, already in the replay's own P&L terms) -> inventory-aware P&L.

    The cap is cap_base (base units), or cap_usd converted at venue a's mid when each trade happens."""
    t = np.asarray(t, dtype=np.int64)
    dq_a, pnl = np.asarray(dq_a, float), np.asarray(pnl, float)
    if cap_usd is not None:
        px = _mid(leg_a, t) if len(t) else np.zeros(0)
        cap = np.where(np.isfinite(px) & (px > 0), cap_usd / np.where(px > 0, px, 1.0), np.inf)
    else:
        cap = np.full(len(t), cap_base)
    t_close = day_end - int(close_window_s * 1e6)
    keep = np.zeros(len(t), bool)
    path_t, path_pos = [day_start], [0.0]
    pos, peak = 0.0, 0.0
    for i in np.argsort(t, kind="stable"):
        if close_window_s > 0 and t[i] >= t_close:
            continue  # closing window: no new trades
        new = pos + dq_a[i]
        if abs(new) <= cap[i] * (1 + 1e-9) or abs(new) < abs(pos):
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

    t_last = np.array([day_end - 1], dtype=np.int64)
    bid_a, ask_a, _, _ = (x[0] for x in leg_a.quote(t_last))
    bid_b, ask_b, _, _ = (x[0] for x in leg_b.quote(t_last))
    mark = pos * ((bid_a + ask_a) / 2 - (bid_b + ask_b) / 2) if pos != 0 else 0.0
    worked_cash, worked_fees, left = 0.0, 0.0, abs(pos)
    if close_window_s > 0:
        worked_cash, worked_fees, left = _work_close(pos, leg_a, leg_b, t_close, day_end, fee_a_bps, fee_b_bps)
    rest = np.sign(pos) * left  # what is still open: closed at the last quotes, whatever their size
    px_a, px_b = (bid_a, ask_b) if rest > 0 else (ask_a, bid_b)  # sell longs at the bid, buy back shorts at the ask
    flatten_cash = worked_cash + (rest * (px_a - px_b) if rest != 0 else 0.0)
    flatten_fees = worked_fees + (abs(rest) * (px_a * fee_a_bps + px_b * fee_b_bps) / 1e4 if rest != 0 else 0.0)
    trade_pnl = float(pnl[keep].sum())
    closing = (t >= t_close) if close_window_s > 0 else np.zeros(len(t), bool)
    return {"keep": keep, "trades": int(keep.sum()), "skipped_by_cap": int((~keep & ~closing).sum()),
            "skipped_closing": int(closing.sum()), "trade_pnl": trade_pnl, "funding": funding, "flatten": float(flatten_cash - flatten_fees),
            "close_unfilled": float(left) if close_window_s > 0 else 0.0,
            "mark": float(mark), "end_position": float(pos), "peak_position": float(peak),
            "realised": trade_pnl + funding + float(flatten_cash - flatten_fees),
            "marked": trade_pnl + funding + float(mark),
            "raw": float(pnl.sum())}
