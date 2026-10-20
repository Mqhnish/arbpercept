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
true book is unknown. Two bounds bracket the truth:
  optimistic    the last snapshot at or before arrival is still valid at arrival
  conservative  the order fills only if the snapshots on both sides of arrival allow it,
                at the worse of their prices and the smaller of their sizes
For a tick-level leg (every change recorded) both modes are the same, exact, answer.
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

    @classmethod
    def from_l1(cls, df: pd.DataFrame, sampled: bool) -> "Leg":
        d = df.drop_duplicates("avail_ts", keep="last").sort_values("avail_ts")
        return cls(d.avail_ts.to_numpy(np.int64), d.bid_px.to_numpy(float), d.ask_px.to_numpy(float),
                   d.bid_sz.to_numpy(float), d.ask_sz.to_numpy(float), sampled)

    def quote(self, t: np.ndarray, mode: str = "optimistic") -> tuple[np.ndarray, ...]:
        """bid, ask, bid_sz, ask_sz in force at times t (NaN before the first update)."""
        i = np.searchsorted(self.t, t, side="right") - 1
        ok = i >= 0
        i = np.maximum(i, 0)
        bid, ask, bsz, asz = self.bid[i], self.ask[i], self.bid_sz[i], self.ask_sz[i]
        if mode == "conservative" and self.sampled:
            j = np.minimum(i + 1, len(self.t) - 1)
            between = (self.t[i] != t) & (j != i)  # arrival falls strictly between two snapshots
            bid = np.where(between, np.minimum(bid, self.bid[j]), bid)
            ask = np.where(between, np.maximum(ask, self.ask[j]), ask)
            bsz = np.where(between, np.minimum(bsz, self.bid_sz[j]), bsz)
            asz = np.where(between, np.minimum(asz, self.ask_sz[j]), asz)
        nan = np.where(ok, 1.0, np.nan)
        return bid * nan, ask * nan, bsz * nan, asz * nan


def execute(sell: Leg, buy: Leg, t_dec: np.ndarray, delay_us: np.ndarray | int, fee_sell_bps: float,
            fee_buy_bps: float, notional_cap: float, mode: str, delay_buy_us: np.ndarray | int | None = None) -> pd.DataFrame:
    """Outcome of selling on `sell` and buying on `buy` for decisions at t_dec (µs).

    delay_us is the sell venue's latency; delay_buy_us the buy venue's (default: the same).
    Returns per decision: filled legs, hedged quantity, gross/fee/unwind P&L in quote currency,
    and pnl_bps relative to the intended notional.
    """
    t_dec = np.asarray(t_dec, dtype=np.int64)
    d_sell = np.broadcast_to(np.asarray(delay_us, dtype=np.int64), t_dec.shape)
    d_buy = d_sell if delay_buy_us is None else np.broadcast_to(np.asarray(delay_buy_us, dtype=np.int64), t_dec.shape)
    # What the trader saw: the latest quotes at decision time (no bounds needed: this is observed).
    s_bid0, _, s_bsz0, _ = sell.quote(t_dec, "optimistic")
    _, b_ask0, _, b_asz0 = buy.quote(t_dec, "optimistic")
    mid0 = (s_bid0 + b_ask0) / 2
    qty = np.minimum(notional_cap / mid0, np.minimum(s_bsz0, b_asz0))

    t_arr_s, t_arr_b = t_dec + d_sell, t_dec + d_buy
    s_bid, _, s_bsz, _ = sell.quote(t_arr_s, mode)
    _, b_ask, _, b_asz = buy.quote(t_arr_b, mode)
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
