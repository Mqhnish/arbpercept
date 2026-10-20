"""Maker-taker cross-venue arbitrage: rest an order on Bybit, hedge on Binance when it fills.

Taker fees on both legs exceed most gaps, so this pays one leg's fee as a maker (low or
zero at top tiers) and crosses the spread only on the hedge.

Bid side (the ask side is the mirror image):
  quote   whenever, as observed, Binance's bid sits far enough above Bybit's best bid to pay
          maker + taker fees plus a minimum margin, rest a buy at Bybit's best bid. The order
          reaches Bybit one Bybit latency after the decision.
  queue   it joins the back of the queue: the displayed size at that price when it arrives
          is ahead of it. Real Bybit trades at that price (seller-initiated) consume the queue
          first; a trade below our price means the whole level was taken. Cancellations by
          others ahead of us are ignored, which delays our fills (pessimistic).
  cancel  when the condition stops holding, a cancel is sent; it takes effect one Bybit
          latency later, and fills can still happen until then.
  hedge   we learn of a fill one Bybit latency after it and sell on Binance with a taker order
          arriving one Binance latency after that, at Binance's bid then (tick-level, exact).
          A partial fill is hedged on its own: each print that fills part of our order gets
          its own hedge, timed from that print.
P&L per fill = qty x (hedge price - our bid) - maker fee - taker fee. The gap between the
Binance bid at decision time and at hedge time is adverse selection: resting orders tend to
fill exactly when the market moves against them.
One order per quoting spell, at the price seen when the spell began (no requotes in this version).

Reference level. Measured against zero, the margin above counts any persistent offset
between the venues as profit. In January 2024 Binance sat 0.5-3 bps below Bybit, so nearly
every fill went the same way and built up a position that must be closed against that same
offset (see inventory.py). Passing ref_bps (the trailing median of Binance mid minus Bybit
mid, offset_reference below) measures the margin against the venues' usual offset instead.
That was expected to balance the two directions, but in January 2024 it did not: 74-94% of
fills still went one way (data/reports/maker_taker/summary.md). Why is still open; until it
is understood, judge this rule only by its inventory-accounted P&L.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass
class Params:
    maker_fee_bps: float = 0.0
    taker_fee_bps: float = 1.7
    min_margin_bps: float = 0.5
    lat_bybit_ms: float = 8.0
    lat_binance_ms: float = 50.0
    notional: float = 10_000.0
    stale_ms: float = 1_000.0  # no quoting while Binance's last quote is older than this (a dead feed)


def _asof(t_ref: np.ndarray, vals: np.ndarray, t: np.ndarray) -> np.ndarray:
    i = np.searchsorted(t_ref, t, side="right") - 1
    return np.where(i >= 0, vals[np.maximum(i, 0)], np.nan)


def binance_age_us(bybit: pd.DataFrame, binance: pd.DataFrame) -> np.ndarray:
    """At each Bybit update, how long ago Binance last updated (µs); inf before its first update."""
    by_t, bn_t = bybit.avail_ts.to_numpy(), binance.avail_ts.to_numpy()
    i = np.searchsorted(bn_t, by_t, side="right") - 1
    return np.where(i >= 0, by_t - bn_t[np.maximum(i, 0)], np.inf)


def offset_reference(bybit: pd.DataFrame, binance: pd.DataFrame, window_s: float = 300.0, stale_ms: float = 1_000.0) -> np.ndarray:
    """Trailing median (strictly past window_s) of Binance mid minus Bybit mid in bps, on Bybit's update clock.
    Moments when Binance's quote is stale are left out, so a dead feed cannot drag the reference."""
    from arbdata.features import trailing_reference
    by_t = bybit.avail_ts.to_numpy()
    by_mid = ((bybit.bid_px + bybit.ask_px) / 2).to_numpy()
    bn_mid = _asof(binance.avail_ts.to_numpy(), ((binance.bid_px + binance.ask_px) / 2).to_numpy(), by_t)
    off = (bn_mid - by_mid) / by_mid * 1e4
    off[binance_age_us(bybit, binance) > stale_ms * 1000] = np.nan
    return trailing_reference(by_t, off, window_s)


def simulate(bybit: pd.DataFrame, trades: pd.DataFrame, binance: pd.DataFrame, side: str, p: Params,
             ref_bps: np.ndarray | None = None) -> pd.DataFrame:
    """One day, one side ("bid": buy on Bybit, sell on Binance; "ask": the mirror). One row per quoting spell.
    ref_bps (per Bybit row): measure the margin against this offset level instead of zero."""
    by_t = bybit.avail_ts.to_numpy()
    bn_t = binance.avail_ts.to_numpy()
    sgn = 1 if side == "bid" else -1
    my_px = (bybit.bid_px if side == "bid" else bybit.ask_px).to_numpy()
    my_sz = (bybit.bid_sz if side == "bid" else bybit.ask_sz).to_numpy()
    hedge_col = "bid_px" if side == "bid" else "ask_px"
    bn_hedge = binance[hedge_col].to_numpy()
    hedge_obs = _asof(bn_t, bn_hedge, by_t)  # Binance hedge price as seen at each Bybit update
    mid = (bybit.bid_px.to_numpy() + bybit.ask_px.to_numpy()) / 2
    margin = sgn * (hedge_obs - my_px) / mid * 1e4 - p.maker_fee_bps - p.taker_fee_bps
    if ref_bps is not None:
        margin = margin - sgn * ref_bps
    quoting = (np.nan_to_num(margin, nan=-np.inf) >= p.min_margin_bps) & (binance_age_us(bybit, binance) <= p.stale_ms * 1000)

    # Quoting spells: maximal runs of the condition on Bybit's update clock.
    d = np.diff(np.concatenate(([0], quoting.astype(np.int8), [0])))
    starts, ends = np.flatnonzero(d == 1), np.flatnonzero(d == -1)  # ends = first index where it stops
    if len(starts) == 0:
        return pd.DataFrame()
    lb, ln = int(p.lat_bybit_ms * 1000), int(p.lat_binance_ms * 1000)
    t_dec = by_t[starts]
    t_arr = t_dec + lb
    t_stop = np.where(ends < len(by_t), by_t[np.minimum(ends, len(by_t) - 1)], by_t[-1]) + lb  # cancel takes effect
    price = my_px[starts]
    qty = p.notional / price
    queue0 = _asof(by_t, my_sz, t_arr)                         # size ahead of us when we arrive
    level_at_arr = _asof(by_t, my_px, t_arr)
    # If the level has already moved away from our price by arrival, we are not at the touch:
    # better than touch -> we are the new best (queue 0); worse -> we rest behind (keep queue0).
    better = sgn * (price - level_at_arr) > 0
    queue0 = np.where(better, 0.0, queue0)

    # Trades that can hit us: seller-initiated for a bid, buyer-initiated for an ask.
    tt = trades[(trades.side == -sgn) & ~trades.rpi]
    tr_t, tr_px, tr_sz = tt.ts.to_numpy(), tt.price.to_numpy(), tt["size"].to_numpy()
    filled = np.zeros(len(starts))
    t_fill = np.full(len(starts), -1, dtype=np.int64)
    hedge_px = np.full(len(starts), np.nan)  # quantity-weighted over the partial hedges
    gross = np.zeros(len(starts))
    hedge_notional = np.zeros(len(starts))
    for k in range(len(starts)):
        lo, hi = np.searchsorted(tr_t, t_arr[k], "left"), np.searchsorted(tr_t, t_stop[k], "right")
        if lo >= hi:
            continue
        px, sz, ts = tr_px[lo:hi], tr_sz[lo:hi], tr_t[lo:hi]
        at = sgn * (px - price[k]) == 0        # prints at our price consume the queue ahead of us
        through = sgn * (price[k] - px) > 0     # prints through our price: the level was swept
        cum = np.clip(np.cumsum(np.where(at, sz, 0.0)) - queue0[k], 0.0, qty[k])  # our filled size after each print
        cum = np.where(np.cumsum(through) > 0, qty[k], cum)                        # a sweep fills whatever is left
        inc = np.diff(np.concatenate(([0.0], cum)))
        j = np.flatnonzero(inc > 0)
        if not len(j):
            continue
        h_px = _asof(bn_t, bn_hedge, ts[j] + lb + ln)   # each part hedged one Bybit + one Binance latency after its print
        filled[k], t_fill[k] = float(cum[-1]), int(ts[j[0]])
        gross[k] = float(np.sum(inc[j] * sgn * (h_px - price[k])))
        hedge_notional[k] = float(np.sum(inc[j] * np.nan_to_num(h_px)))
        hedge_px[k] = hedge_notional[k] / filled[k]
    hedge_t = np.where(t_fill >= 0, t_fill + lb + ln, 0)  # the first hedge
    fees = filled * price * p.maker_fee_bps / 1e4 + hedge_notional * p.taker_fee_bps / 1e4
    pnl = gross - fees
    adverse = np.where(filled > 0, sgn * (hedge_px - hedge_obs[starts]) / price * 1e4, np.nan)
    return pd.DataFrame({
        "t_dec": t_dec, "price": price, "margin_bps": margin[starts], "queue_ahead": queue0, "qty": qty,
        "filled": filled, "t_fill": t_fill, "hedge_px": hedge_px, "pnl": pnl,
        "pnl_bps": np.divide(pnl * 1e4, filled * price, out=np.zeros(len(pnl)), where=filled > 0), "adverse_bps": adverse,
        "hedge_t": hedge_t,
        "spell_ms": (t_stop - t_arr) / 1000,
    })
