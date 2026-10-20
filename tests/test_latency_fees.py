"""Per-venue latency and fees in the taker replay, and the fold split that keeps choices off validation days."""

import numpy as np
import pandas as pd

from arbtrade.replay import Leg, execute


def leg(t, bid, ask, size=10.0):
    t = np.asarray(t, dtype=np.int64)
    return Leg(t, np.asarray(bid, float), np.asarray(ask, float), np.full(len(t), size), np.full(len(t), size), False)


def test_each_leg_arrives_after_its_own_venue_latency():
    # The buy venue's ask rises at 20 ms. A 5 ms leg gets there first; a 50 ms leg misses.
    a = leg([0], [101.0], [101.1])
    b = leg([0, 20_000], [99.9, 100.9], [100.0, 101.0])
    fast = execute(a, b, np.array([0]), 50_000, 0, 0, 1_000.0, "optimistic", delay_buy_us=5_000).iloc[0]
    slow = execute(a, b, np.array([0]), 5_000, 0, 0, 1_000.0, "optimistic", delay_buy_us=50_000).iloc[0]
    assert fast.both_filled and not slow.both_filled
    assert slow.one_leg  # sold on a, missed on b


def test_one_sided_fill_is_closed_once_both_legs_are_in_plus_that_venues_latency():
    # Sell leg (5 ms) fills, buy leg (50 ms) misses. The buy-back on the sell venue arrives at 50 + 5 = 55 ms.
    a = leg([0, 54_000, 56_000], [101.0] * 3, [101.1, 101.2, 101.6])
    b = leg([0, 20_000], [99.9, 100.9], [100.0, 101.0])
    r = execute(a, b, np.array([0]), 5_000, 0, 0, 1_000.0, "optimistic", delay_buy_us=50_000).iloc[0]
    assert np.isclose(r.unwind, -r.qty * (101.2 - 101.0))  # the ask in force at 55 ms


def test_equal_latency_matches_the_single_delay():
    a = leg([0, 5_000], [101.0, 101.0], [101.1, 101.1])
    b = leg([0, 5_000], [99.9, 100.9], [100.0, 101.0])
    one = execute(a, b, np.array([0]), 10_000, 1.0, 1.0, 1_000.0, "optimistic")
    two = execute(a, b, np.array([0]), 10_000, 1.0, 1.0, 1_000.0, "optimistic", delay_buy_us=10_000)
    pd.testing.assert_frame_equal(one, two)


def test_venue_fees_are_charged_per_leg():
    from arbtrade.evaluate import replay_day
    a = leg([0], [101.0], [101.1])
    b = leg([0], [99.9], [100.0])
    eps = pd.DataFrame({"birth_ts": [0], "direction": ["sell_a_buy_b"]})
    r = replay_day(eps, {"a": a, "b": b}, 0, 1.0, "optimistic", fee_b_bps=3.0).iloc[0]
    assert np.isclose(r.fees, r.qty * (101.0 * 1.0 + 100.0 * 3.0) / 1e4)


def test_replay_day_gives_each_leg_its_latency():
    from arbtrade.evaluate import replay_day
    a = leg([0], [101.0], [101.1])
    b = leg([0, 20_000], [99.9, 100.9], [100.0, 101.0])
    eps = pd.DataFrame({"birth_ts": [0], "direction": ["sell_a_buy_b"]})
    assert replay_day(eps, {"a": a, "b": b}, 50, 0.0, "optimistic", delay_b_ms=5).full_fill.iloc[0]
    assert not replay_day(eps, {"a": a, "b": b}, 5, 0.0, "optimistic", delay_b_ms=50).full_fill.iloc[0]


def test_fold_days_keep_choices_off_validation_days():
    from arbtrade.evaluate import fold_days
    train = [f"2024-01-{d:02d}" for d in range(1, 11)]
    val = ["2024-01-12", "2024-01-13", "2024-01-14"]
    fit, cal, va = fold_days({"train": train, "val": val}, set(train) | set(val), set(train) | set(val))
    assert fit == train[:7] and cal == train[7:] and va == val
    assert max(fit) < min(cal) and max(cal) < min(va)          # fit, then calibrate, then score
    assert not (set(fit) | set(cal)) & set(va)
    # a validation day without triggers is still scored (as $0); a training day without them is not used
    fit, cal, va = fold_days({"train": train, "val": val}, set(train) - {"2024-01-03"}, set(val))
    assert "2024-01-03" not in fit + cal and va == val
    assert fold_days({"train": train[:2], "val": val}, set(train), set(val)) is None
