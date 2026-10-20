import numpy as np
import pandas as pd

from arbtrade.evaluate import offset_at


def test_gap_is_measured_against_the_usual_offset_in_each_direction():
    # venue a sits 2 bps above venue b for ten minutes
    t = np.arange(0, 600_000_000, 1_000_000, dtype=np.int64)
    b_mid = np.full(len(t), 100.0)
    a_mid = b_mid * (1 + 2e-4)
    al = pd.DataFrame({"t": t, "a_mid": a_mid, "b_mid": b_mid})
    eps = pd.DataFrame({"birth_ts": [400_000_000, 400_000_000], "direction": ["sell_a_buy_b", "sell_b_buy_a"]})
    off = offset_at(al, eps)
    assert np.allclose(off, [2.0, -2.0], atol=1e-3)   # selling the rich venue: 2 bps of the gap is just the offset


def test_offset_uses_only_past_data():
    t = np.array([0, 1_000_000, 2_000_000], dtype=np.int64)
    al = pd.DataFrame({"t": t, "a_mid": [100.0, 100.0, 101.0], "b_mid": [100.0, 100.0, 100.0]})
    eps = pd.DataFrame({"birth_ts": [2_000_000], "direction": ["sell_a_buy_b"]})
    assert np.isclose(offset_at(al, eps)[0], 0.0)    # the jump at the birth itself is not part of the reference
