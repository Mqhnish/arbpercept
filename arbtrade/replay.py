"""Replay a two-leg arbitrage against recorded quotes, with injected latency.

At a decision time t the trader sees each leg's latest quote (as-of t) and sends two
immediate-or-cancel limit orders: sell at the observed bid on one venue, buy at the
observed ask on the other. They reach the exchanges at t + delay. Each leg fills only if
the book at arrival still crosses its limit, up to the displayed size, at the arrival price.

If exactly one leg fills, the position is unhedged and is closed by crossing the spread on
that venue. The closing order is sent once both legs have arrived and reaches that venue one
of its own latencies later. That is the leg risk in S = e*q - (1-q)*pi*l - c.

Each leg can have its own latency (delay_buy_us), since the two venues are not equally far away.

A sampled leg (Bybit's 100 ms archive) is only known at its snapshots, so between them the
true book is unknown. Two simulation assumptions show how much that matters:
  optimistic    the last snapshot at or before arrival is still valid at arrival
  conservative  the order fills only if the snapshots on both sides of arrival allow it,
                at the worse of their prices and the smaller of their sizes
Neither is a guaranteed bound: the book can move away and come back between two snapshots,
and "conservative" cannot see that. Treat the gap between the two as a sensitivity, not as
an interval that must contain the truth.
For a tick-level leg (every change recorded) both modes are the same answer.

Two optional effects, both off by default (old results reproduce exactly):
  feed delay        the trader sees each venue's book late, by that venue's feed delay. At
                    decision time t it sees the quotes published at or before t - feed delay.
                    This is separate from the order latency (delay_us, delay_buy_us).
  liquidity reuse   (deplete=True) a fill uses up the displayed size it took. The size stays
                    used up while that side's price holds, so a later order at that price only
                    gets what is left. When the price changes, the full displayed size is back.
Remaining limits: only level 1 exists. Orders are still sized from the displayed size, so an
order can ask for more than is left; the leg that gets less leaves an unhedged remainder, closed
like any one-sided fill. The closing order is neither size-limited nor counted against the
displayed size.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

MODES = ("optimistic", "conservative")


@dataclass
class Leg:
    t: np.ndarray
    bid: np.ndarray
    ask: np.ndarray
    bid_sz: np.ndarray
    ask_sz: np.ndarray
    sampled: bool
    # Smallest size shown while each row's price held (tick sources fold size-only updates).
    # The conservative bound fills against these; None means the sizes are exact per row.
    bid_sz_min: np.ndarray | None = None
    ask_sz_min: np.ndarray | None = None

    @classmethod
    def from_l1(cls, df: pd.DataFrame, sampled: bool) -> "Leg":
        d = df.drop_duplicates("avail_ts", keep="last").sort_values("avail_ts")
        mins = (d.bid_sz_min.to_numpy(float), d.ask_sz_min.to_numpy(float)) if "bid_sz_min" in d else (None, None)
        return cls(d.avail_ts.to_numpy(np.int64), d.bid_px.to_numpy(float), d.ask_px.to_numpy(float),
                   d.bid_sz.to_numpy(float), d.ask_sz.to_numpy(float), sampled, *mins)

    def quote(self, t: np.ndarray, mode: str = "optimistic") -> tuple[np.ndarray, ...]:
        """bid, ask, bid_sz, ask_sz in force at times t (NaN before the first update)."""
        i = np.searchsorted(self.t, t, side="right") - 1
        ok = i >= 0
        i = np.maximum(i, 0)
        bid, ask, bsz, asz = self.bid[i], self.ask[i], self.bid_sz[i], self.ask_sz[i]
        if mode == "conservative" and self.bid_sz_min is not None:
            # size may have been pulled while the price held: assume only the run's minimum
            bsz, asz = np.minimum(bsz, self.bid_sz_min[i]), np.minimum(asz, self.ask_sz_min[i])
        if mode == "conservative" and self.sampled:
            j = np.minimum(i + 1, len(self.t) - 1)
            between = (self.t[i] != t) & (j != i)  # arrival falls strictly between two snapshots
            bid = np.where(between, np.minimum(bid, self.bid[j]), bid)
            ask = np.where(between, np.maximum(ask, self.ask[j]), ask)
            bsz = np.where(between, np.minimum(bsz, self.bid_sz[j]), bsz)
            asz = np.where(between, np.minimum(asz, self.ask_sz[j]), asz)
        nan = np.where(ok, 1.0, np.nan)
        return bid * nan, ask * nan, bsz * nan, asz * nan


def updated_at(leg: Leg, t: np.ndarray) -> np.ndarray:
    """Whether the leg has an update at exactly each time t."""
    t = np.asarray(t, dtype=np.int64)
    if not len(leg.t):
        return np.zeros(t.shape, bool)
    i = np.minimum(np.searchsorted(leg.t, t, side="left"), len(leg.t) - 1)
    return leg.t[i] == t


def seen_after_us(sell: Leg, buy: Leg, t_birth: np.ndarray, feed_sell_us: int, feed_buy_us: int) -> np.ndarray:
    """How long after a birth (µs) the trader first sees it, given each venue's feed delay.

    A birth happens at one venue's update. The trader sees it once that update arrives, which
    is that venue's feed delay later. When both venues (or neither) updated at that instant,
    it is the slower feed's delay.
    """
    hit_s, hit_b = updated_at(sell, t_birth), updated_at(buy, t_birth)
    slower = max(feed_sell_us, feed_buy_us)
    return np.where(hit_s & ~hit_b, feed_sell_us, np.where(hit_b & ~hit_s, feed_buy_us, slower)).astype(np.int64)


def price_runs(px: np.ndarray) -> np.ndarray:
    """Run number of each update on one side of a book. It goes up whenever the price changes."""
    if not len(px):
        return np.zeros(0, np.int64)
    return np.concatenate(([0], np.cumsum(px[1:] != px[:-1])))


def fill_depleting(t_side: np.ndarray, px_side: np.ndarray, t_arr: np.ndarray, want: np.ndarray,
                   size: np.ndarray) -> np.ndarray:
    """Fills on one side of one venue when each fill uses up the displayed size it took.

    t_side, px_side: that side's update times and prices. want: what each order would take
    (0 if its price no longer crosses). size: the displayed size at its arrival (t_arr).
    Orders are matched in arrival order. While the side's price holds, a later order gets the
    displayed size minus what earlier orders took. A price change makes the full size available again.
    """
    want, size = np.nan_to_num(np.asarray(want, float)), np.nan_to_num(np.asarray(size, float))
    fill = np.minimum(want, size)
    i = np.searchsorted(t_side, t_arr, side="right") - 1
    run = np.where(i >= 0, price_runs(px_side)[np.maximum(i, 0)], -1)
    order = np.lexsort((np.arange(len(run)), t_arr, run))  # by price run, then arrival, then input order
    r = run[order]
    starts = np.flatnonzero(np.r_[True, r[1:] != r[:-1]]) if len(r) else np.zeros(0, int)
    for a, b in zip(starts, np.r_[starts[1:], len(r)]):
        if b - a < 2 or r[a] < 0:
            continue  # alone in its price run, or before the first quote: nothing is shared
        used = 0.0
        for k in order[a:b]:
            fill[k] = min(want[k], max(size[k] - used, 0.0))
            used += fill[k]
    return fill


def execute(sell: Leg, buy: Leg, t_dec: np.ndarray, delay_us: np.ndarray | int, fee_sell_bps: float,
            fee_buy_bps: float, notional_cap: float, mode: str, delay_buy_us: np.ndarray | int | None = None,
            feed_sell_us: int = 0, feed_buy_us: int = 0, deplete: bool = False) -> pd.DataFrame:
    """Outcome of selling on `sell` and buying on `buy` for decisions at t_dec (µs).

    delay_us is the sell venue's latency; delay_buy_us the buy venue's (default: the same).
    feed_sell_us and feed_buy_us are the venues' feed delays. The orders are priced and sized
    from the quotes published at or before t_dec minus that venue's feed delay.
    deplete: each fill uses up the displayed size it took (fill_depleting), shared by all the
    decisions in this call.
    Returns per decision: filled legs, hedged quantity, gross/fee/unwind P&L in quote currency,
    and pnl_bps relative to the intended notional.
    """
    t_dec = np.asarray(t_dec, dtype=np.int64)
    d_sell = np.broadcast_to(np.asarray(delay_us, dtype=np.int64), t_dec.shape)
    d_buy = d_sell if delay_buy_us is None else np.broadcast_to(np.asarray(delay_buy_us, dtype=np.int64), t_dec.shape)
    # What the trader saw: each venue's latest quote that had reached it (no bounds needed: this is observed).
    s_bid0, _, s_bsz0, _ = sell.quote(t_dec - feed_sell_us, "optimistic")
    _, b_ask0, _, b_asz0 = buy.quote(t_dec - feed_buy_us, "optimistic")
    mid0 = (s_bid0 + b_ask0) / 2
    qty = np.minimum(notional_cap / mid0, np.minimum(s_bsz0, b_asz0))

    t_arr_s, t_arr_b = t_dec + d_sell, t_dec + d_buy
    s_bid, _, s_bsz, _ = sell.quote(t_arr_s, mode)
    _, b_ask, _, b_asz = buy.quote(t_arr_b, mode)
    if deplete:
        sell_q = fill_depleting(sell.t, sell.bid, t_arr_s, np.where(s_bid >= s_bid0, qty, 0.0), s_bsz)
        buy_q = fill_depleting(buy.t, buy.ask, t_arr_b, np.where(b_ask <= b_ask0, qty, 0.0), b_asz)
    else:
        sell_q = np.where(s_bid >= s_bid0, np.minimum(qty, s_bsz), 0.0)
        buy_q = np.where(b_ask <= b_ask0, np.minimum(qty, b_asz), 0.0)
    sell_q, buy_q = np.nan_to_num(sell_q), np.nan_to_num(buy_q)
    hedged = np.minimum(sell_q, buy_q)
    gross = hedged * (np.nan_to_num(s_bid) - np.nan_to_num(b_ask))
    fees = (fee_sell_bps * sell_q * np.nan_to_num(s_bid) + fee_buy_bps * buy_q * np.nan_to_num(b_ask)) / 1e4

    # Unhedged remainder: once both legs have arrived, close it on the venue where it was filled,
    # arriving one of that venue's latencies later.
    both_in = np.maximum(t_arr_s, t_arr_b)
    short = sell_q - hedged  # sold more than bought: buy it back on the sell venue
    long = buy_q - hedged    # bought more than sold: sell it on the buy venue
    _, s_ask_u, _, _ = sell.quote(both_in + d_sell, mode)
    b_bid_u, _, _, _ = buy.quote(both_in + d_buy, mode)
    s_fill, b_fill = np.nan_to_num(s_bid), np.nan_to_num(b_ask)
    s_ask_u = np.where(np.isnan(s_ask_u), s_fill, s_ask_u)
    b_bid_u = np.where(np.isnan(b_bid_u), b_fill, b_bid_u)
    unwind = short * (s_fill - s_ask_u) + long * (b_bid_u - b_fill)
    unwind_fees = (fee_sell_bps * short * s_ask_u + fee_buy_bps * long * b_bid_u) / 1e4
    pnl = gross - fees + unwind - unwind_fees
    notional = qty * mid0
    both = (sell_q > 0) & (buy_q > 0)
    one = (sell_q > 0) ^ (buy_q > 0)
    return pd.DataFrame({
        "both_filled": both, "one_leg": one, "full_fill": both & (hedged >= qty - 1e-12),
        "qty": qty, "hedged": hedged, "notional": notional,
        "gross": gross, "fees": fees + unwind_fees, "unwind": unwind, "pnl": pnl,
        "pnl_bps": np.where(notional > 0, pnl / notional * 1e4, 0.0),
        "mid_dec": mid0,
        # The gap the trader saw when deciding: a re-check before sending can skip a vanished gap.
        "edge_dec_bps": (s_bid0 - b_ask0) / mid0 * 1e4,
    })
