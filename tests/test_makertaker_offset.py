"""The maker-taker offset reference must use only the past, and skip moments when Binance's quote is stale."""

import numpy as np
import pandas as pd

from arbtrade.makertaker import offset_reference


def quotes(t, mid):
    t = np.asarray(t, np.int64)
    mid = np.asarray(mid, float)
    return pd.DataFrame({"avail_ts": t, "bid_px": mid - 0.005, "ask_px": mid + 0.005,
                         "bid_sz": 1.0, "ask_sz": 1.0})


def test_reference_excludes_the_current_update_and_the_future():
    by = quotes([0, 1_000_000, 2_000_000, 3_000_000], [100.0] * 4)
    bn = quotes([0, 2_000_000], [100.0, 100.1])                   # Binance jumps 10 bps at 2 s
    ref = offset_reference(by, bn, window_s=60)
    assert np.isnan(ref[0]) and np.allclose(ref[1:3], 0.0)       # the jump at 2 s is not in its own reference
    assert np.isclose(ref[3], 0.0)                                # median of 0, 0, 10
    cut = offset_reference(by.iloc[:3], bn[bn.avail_ts <= 2_000_000], window_s=60)
    assert np.allclose(cut, ref[:3], equal_nan=True)              # deleting the future changes nothing


def test_stale_binance_moments_are_left_out():
    by = quotes(np.arange(6) * 1_000_000, [100.0, 100.0, 100.1, 100.1, 100.1, 100.1])
    bn = quotes([0], [100.1])                                     # Binance never updates again
    # Only Bybit rows at 0 s and 1 s see a Binance quote younger than 1.5 s (offset 10 bps). Counting the
    # stale rows (offset 0 once Bybit has moved) would drag the median to 0.
    ref = offset_reference(by, bn, window_s=60, stale_ms=1_500)
    assert np.isnan(ref[0]) and np.allclose(ref[1:], 10.0, atol=0.01)
    assert np.isclose(offset_reference(by, bn, window_s=60, stale_ms=10_000)[5], 0.0, atol=0.01)
