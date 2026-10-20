"""Convergence trades for statistical-arbitrage pairs (spot vs perpetual, ETH vs BTC).

Unlike a cross-venue arbitrage, buying cheap and selling rich does not lock in profit:
it pays only if the dislocation closes while the position is held.

Entry: at decision time t the trader sees a dislocation and sends two IOC orders priced at
the quotes seen then (sell the rich leg at its bid, buy the cheap leg at its ask). They
arrive at t + delay and fill only if the book still allows it, up to displayed size.
Partial or one-sided fills are hedged down to the smaller leg and the excess is unwound.

Exit: at the first observed moment after arrival when the mid-based dislocation is back
at its reference (the trailing basis, or the Kalman fair value for ratio pairs), or after
hold_s, both legs are closed by crossing the spread, arriving one delay later.

P&L includes both spreads paid on entry and exit and taker fees on all four fills. Leg
notionals follow the hedge ratio (1 for spot vs perpetual, the filter's beta for ratio pairs).
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from .replay import Leg


def next_true_index(cond: np.ndarray) -> np.ndarray:
    """nxt[i] = smallest j >= i with cond[j], or len(cond) if none."""
    n = len(cond)
    idx = np.where(cond, np.arange(n), n)
    return np.minimum.accumulate(idx[::-1])[::-1]


def exit_signal_times(t: np.ndarray, closed: np.ndarray, t_arr: np.ndarray, hold_us: int) -> np.ndarray:
    """First event time after arrival where the dislocation is closed, capped at arrival + hold."""
    nxt = next_true_index(closed)
    i0 = np.searchsorted(t, t_arr, side="right")
    j = np.where(i0 < len(t), nxt[np.minimum(i0, len(t) - 1)], len(t))
    t_close = np.where(j < len(t), t[np.minimum(j, len(t) - 1)], np.iinfo(np.int64).max)
    return np.minimum(t_close, t_arr + hold_us)


def execute_convergence(sell: Leg, buy: Leg, t_dec: np.ndarray, delay_us: int, fee_bps: float,
                        notional_sell: np.ndarray, notional_buy: np.ndarray, t_exit_signal_fn,
                        mode: str) -> pd.DataFrame:
    t_dec = np.asarray(t_dec, dtype=np.int64)
    s_bid0, _, s_bsz0, _ = sell.quote(t_dec, "optimistic")
    _, b_ask0, _, b_asz0 = buy.quote(t_dec, "optimistic")
    q_s = notional_sell / s_bid0
    q_b = notional_buy / b_ask0
    cap = np.minimum(1.0, np.minimum(s_bsz0 / q_s, b_asz0 / q_b))  # thinner side limits both legs
    q_s, q_b = q_s * cap, q_b * cap

    t_arr = t_dec + delay_us
    s_bid, _, s_bsz, _ = sell.quote(t_arr, mode)
    _, b_ask, _, b_asz = buy.quote(t_arr, mode)
    f_s = np.where(s_bid >= s_bid0, np.minimum(1.0, s_bsz / q_s), 0.0)
    f_b = np.where(b_ask <= b_ask0, np.minimum(1.0, b_asz / q_b), 0.0)
    f_s, f_b = np.nan_to_num(f_s), np.nan_to_num(f_b)
    h = np.minimum(f_s, f_b)  # hedged fraction carried into the hold

    fee = fee_bps / 1e4
    s_fill, b_fill = np.nan_to_num(s_bid), np.nan_to_num(b_ask)
    entry_fees = fee * (f_s * q_s * s_fill + f_b * q_b * b_fill)

    # Excess on one leg is unwound one delay after arrival.
    t_unw = t_arr + delay_us
    _, s_ask_u, _, _ = sell.quote(t_unw, mode)
    b_bid_u, _, _, _ = buy.quote(t_unw, mode)
    s_ask_u = np.where(np.isnan(s_ask_u), s_fill, s_ask_u)
    b_bid_u = np.where(np.isnan(b_bid_u), b_fill, b_bid_u)
    ex_s, ex_b = (f_s - h) * q_s, (f_b - h) * q_b
    unwind = ex_s * (s_fill - s_ask_u) + ex_b * (b_bid_u - b_fill) - fee * (ex_s * s_ask_u + ex_b * b_bid_u)

    # Hold the hedged part until the dislocation closes (or the time limit), then cross out.
    t_sig = t_exit_signal_fn(t_arr)
    t_out = t_sig + delay_us
    _, s_ask_x, _, _ = sell.quote(t_out, mode)   # buy back the leg we sold
    b_bid_x, _, _, _ = buy.quote(t_out, mode)    # sell the leg we bought
    s_ask_x = np.where(np.isnan(s_ask_x), s_fill, s_ask_x)
    b_bid_x = np.where(np.isnan(b_bid_x), b_fill, b_bid_x)
    hs, hb = h * q_s, h * q_b
    held = hs * (s_fill - s_ask_x) + hb * (b_bid_x - b_fill) - fee * (hs * s_ask_x + hb * b_bid_x)

    pnl = held + unwind - entry_fees
    notional = q_s * s_bid0  # sell-leg notional as the reference size
    full = (f_s >= 1 - 1e-9) & (f_b >= 1 - 1e-9)
    return pd.DataFrame({
        "both_filled": (f_s > 0) & (f_b > 0), "one_leg": (f_s > 0) ^ (f_b > 0), "full_fill": full,
        "notional": notional, "hold_ms": np.where(h > 0, (t_sig - t_arr) / 1000, 0.0),
        "held": held, "unwind": unwind, "fees": entry_fees, "pnl": pnl,
        "pnl_bps": np.where(notional > 0, pnl / notional * 1e4, 0.0),
    })
