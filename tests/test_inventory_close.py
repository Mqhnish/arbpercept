"""The position cap at each trade's price, and the day-end close that never takes more than the books show."""

import numpy as np

from arbtrade.inventory import account_day
from arbtrade.replay import Leg

DAY = 86_400_000_000
T_CLOSE = DAY - 60_000_000


def moving_leg(t, mid, size=10.0, half=0.1):
    t = np.asarray(t, dtype=np.int64)
    mid = np.asarray(mid, float)
    n = len(t)
    return Leg(t, mid - half, mid + half, np.full(n, size), np.full(n, size), False)


def test_usd_cap_uses_the_price_at_each_trade():
    # $250 cap. At 100 that is 2.5 units; after the price halves to 50 it is 5 units.
    a = moving_leg([0, 1_000], [100.0, 50.0])
    b = moving_leg([0, 1_000], [100.0, 50.0])
    t = np.array([10, 20, 30, 2_000, 2_010])
    r = account_day(t, np.ones(5), np.zeros(5), a, b, None, None, 0, DAY, cap_usd=250.0)
    assert r["keep"].tolist() == [True, True, False, True, True]  # 3 units at 100 is $300; at 50, 4 units is $200


def test_closing_window_takes_no_new_trades_and_never_more_than_the_books_show():
    # Long 3 on a. Both books show 1 unit and change twice inside the last minute: 3 states, 1 unit each.
    a = moving_leg([0, T_CLOSE + 1, T_CLOSE + 2], [100.0] * 3, size=1.0)
    b = moving_leg([0, T_CLOSE + 1, T_CLOSE + 2], [101.0] * 3, size=1.0)
    r = account_day(np.array([10, T_CLOSE + 5]), np.array([3.0, 1.0]), np.array([0.0, 7.0]), a, b, None, None,
                    0, DAY, close_window_s=60.0)
    assert r["keep"].tolist() == [True, False] and r["skipped_closing"] == 1 and r["skipped_by_cap"] == 0
    assert np.isclose(r["close_unfilled"], 0.0)
    assert np.isclose(r["flatten"], 3 * (99.9 - 101.1))   # sold a at its bid, bought b back at its ask


def test_a_level_we_took_from_is_not_used_again_until_it_changes():
    a = moving_leg([0], [100.0], size=1.0)                 # a never updates: 1 unit, once
    b = moving_leg([0, T_CLOSE + 1, T_CLOSE + 2], [101.0] * 3, size=5.0)
    r = account_day(np.array([10]), np.array([3.0]), np.zeros(1), a, b, None, None, 0, DAY, close_window_s=60.0)
    assert np.isclose(r["close_unfilled"], 2.0)            # 2 units left: closed at the last quotes and flagged
    assert np.isclose(r["flatten"], 3 * (99.9 - 101.1))


def test_short_positions_are_bought_back_on_a_and_sold_on_b():
    a = moving_leg([0, T_CLOSE + 1], [100.0, 100.0], size=5.0)
    b = moving_leg([0, T_CLOSE + 1], [101.0, 101.0], size=5.0)
    r = account_day(np.array([10]), np.array([-2.0]), np.zeros(1), a, b, None, None, 0, DAY, close_window_s=60.0)
    assert np.isclose(r["flatten"], 2 * (100.9 - 100.1)) and r["close_unfilled"] == 0.0


def test_no_closing_window_is_the_old_close():
    a, b = moving_leg([0], [100.0]), moving_leg([0], [101.0])
    r = account_day(np.array([10]), np.array([1.0]), np.array([1.0]), a, b, None, None, 0, DAY,
                    cap_base=5.0, fee_a_bps=10.0, fee_b_bps=10.0)
    assert r["close_unfilled"] == 0.0 and r["skipped_closing"] == 0
    assert np.isclose(r["flatten"], 99.9 - 101.1 - (99.9 + 101.1) * 10 / 1e4)
