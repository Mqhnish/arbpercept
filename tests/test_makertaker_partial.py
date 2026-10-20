import numpy as np
import pandas as pd

from arbtrade.makertaker import Params, simulate


def book(t, bid, ask, bsz=1.0, asz=1.0):
    n = len(t)
    return pd.DataFrame({"avail_ts": np.asarray(t, np.int64), "bid_px": np.full(n, bid) if np.isscalar(bid) else bid,
                         "ask_px": np.full(n, ask) if np.isscalar(ask) else ask,
                         "bid_sz": np.full(n, bsz), "ask_sz": np.full(n, asz)})


def test_each_partial_fill_is_hedged_from_its_own_print():
    # Two prints at our price fill us half each, 100 ms apart. Binance's bid drops between the two hedges.
    bybit = book([0, 300_000], 100.0, 100.1, bsz=0.0)                    # nobody ahead of us
    binance = book([0, 150_000], np.array([100.06, 100.02]), np.array([100.07, 100.03]))
    trades = pd.DataFrame({"ts": np.array([20_000, 120_000], np.int64), "price": [100.0, 100.0],
                           "size": [0.05, 0.05], "side": np.array([-1, -1], np.int8), "rpi": False})
    p = Params(maker_fee_bps=0, taker_fee_bps=0, min_margin_bps=1, lat_bybit_ms=8, lat_binance_ms=50, notional=10.0)
    r = simulate(bybit, trades, binance, "bid", p).iloc[0]
    assert np.isclose(r.filled, 0.1) and r.t_fill == 20_000
    # first half hedged at 78 ms (bid 100.06), second at 178 ms (bid 100.02)
    assert np.isclose(r.pnl, 0.05 * 0.06 + 0.05 * 0.02)
    assert np.isclose(r.hedge_px, 100.04)


def test_partial_fill_then_sweep_fills_the_rest_at_the_sweep():
    bybit = book([0, 300_000], 100.0, 100.1, bsz=0.0)
    binance = book([0, 150_000], np.array([100.06, 100.02]), np.array([100.07, 100.03]))
    trades = pd.DataFrame({"ts": np.array([20_000, 120_000], np.int64), "price": [100.0, 99.9],
                           "size": [0.03, 5.0], "side": np.array([-1, -1], np.int8), "rpi": False})
    p = Params(maker_fee_bps=0, taker_fee_bps=1.0, min_margin_bps=1, lat_bybit_ms=8, lat_binance_ms=50, notional=10.0)
    r = simulate(bybit, trades, binance, "bid", p).iloc[0]
    assert np.isclose(r.filled, 0.1)
    gross = 0.03 * 0.06 + 0.07 * 0.02
    fees = (0.03 * 100.06 + 0.07 * 100.02) * 1.0 / 1e4      # taker fee on what each hedge actually paid
    assert np.isclose(r.pnl, gross - fees)
