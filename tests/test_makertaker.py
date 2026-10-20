import numpy as np
import pandas as pd

from arbtrade.makertaker import Params, simulate


def book(t, bid, ask, bsz=1.0, asz=1.0):
    n = len(t)
    return pd.DataFrame({"avail_ts": np.asarray(t, np.int64), "bid_px": np.full(n, bid) if np.isscalar(bid) else bid,
                         "ask_px": np.full(n, ask) if np.isscalar(ask) else ask,
                         "bid_sz": np.full(n, bsz), "ask_sz": np.full(n, asz)})


def test_queue_then_fill_then_hedge():
    bybit = book([0, 100_000, 200_000], 100.0, 100.1, bsz=1.0)          # 1 unit ahead of us at 100.0
    binance = book([0], 100.06, 100.07)                                  # Binance bid 6 bps above
    trades = pd.DataFrame({"ts": np.array([20_000, 30_000, 40_000], np.int64), "price": [100.0, 100.0, 100.0],
                           "size": [0.6, 0.6, 0.6], "side": np.array([-1, -1, -1], np.int8), "rpi": False})
    p = Params(maker_fee_bps=0, taker_fee_bps=0, min_margin_bps=1, lat_bybit_ms=8, lat_binance_ms=50, notional=10.0)
    r = simulate(bybit, trades, binance, "bid", p).iloc[0]
    assert np.isclose(r.queue_ahead, 1.0)
    assert np.isclose(r.filled, 0.1)                     # qty is 0.1 (notional 10 at 100); queue cleared at 30 ms
    assert r.t_fill == 30_000
    assert np.isclose(r.hedge_px, 100.06) and np.isclose(r.pnl, 0.1 * 0.06)


def test_no_trades_no_fill_and_fees_only_on_fills():
    bybit = book([0, 100_000], 100.0, 100.1)
    binance = book([0], 100.06, 100.07)
    trades = pd.DataFrame({"ts": np.array([], np.int64), "price": [], "size": [], "side": np.array([], np.int8), "rpi": []})
    r = simulate(bybit, trades, binance, "bid", Params(min_margin_bps=1, notional=10.0)).iloc[0]
    assert r.filled == 0 and r.pnl == 0


def test_sweep_through_our_price_fills_everything():
    bybit = book([0, 100_000], 100.0, 100.1, bsz=50.0)                   # long queue
    binance = book([0], 100.06, 100.07)
    trades = pd.DataFrame({"ts": np.array([20_000], np.int64), "price": [99.9], "size": [80.0],
                           "side": np.array([-1], np.int8), "rpi": False})
    p = Params(maker_fee_bps=0, taker_fee_bps=0, min_margin_bps=1, notional=10.0)
    r = simulate(bybit, trades, binance, "bid", p).iloc[0]
    assert np.isclose(r.filled, 0.1) and r.t_fill == 20_000


def test_no_quoting_against_a_stale_binance_quote():
    # Binance last updated at t=0 showing a rich bid; Bybit updates 2 s later: the gap is not trusted.
    by = pd.DataFrame({"avail_ts": [2_000_000, 2_100_000], "bid_px": [100.0, 100.0], "ask_px": [100.1, 100.1],
                       "bid_sz": [1.0, 1.0], "ask_sz": [1.0, 1.0]})
    bn = pd.DataFrame({"avail_ts": [0], "bid_px": [100.5], "ask_px": [100.6], "bid_sz": [5.0], "ask_sz": [5.0]})
    tr = pd.DataFrame({"ts": [2_050_000], "price": [99.9], "size": [10.0], "side": [-1], "rpi": [False]})
    assert simulate(by, tr, bn, "bid", Params(min_margin_bps=0.5, stale_ms=1_000)).empty
    assert not simulate(by, tr, bn, "bid", Params(min_margin_bps=0.5, stale_ms=5_000)).empty
