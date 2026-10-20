"""Market-data (feed) delay and liquidity reuse in the taker replay. Both are off by default."""

import numpy as np
import pandas as pd
import pytest

from arbtrade.evaluate import replay_day
from arbtrade.replay import Leg, execute, fill_depleting, price_runs, seen_after_us, updated_at


def leg(t, bid, ask, size=10.0):
    t = np.asarray(t, dtype=np.int64)
    sz = np.broadcast_to(np.asarray(size, float), t.shape).copy()
    return Leg(t, np.asarray(bid, float), np.asarray(ask, float), sz, sz.copy(), False)


def births(*rows):
    return pd.DataFrame(rows, columns=["birth_ts", "direction"])


# --- feed delay -------------------------------------------------------------------------------

def test_updated_at_and_seen_after_us():
    a, b = leg([0, 10_000], [1, 1], [2, 2]), leg([0, 20_000], [1, 1], [2, 2])
    t = np.array([10_000, 20_000, 0, 15_000])
    assert updated_at(a, t).tolist() == [True, False, True, False]
    assert updated_at(leg([], [], []), t).tolist() == [False] * 4
    # a's update: a's feed delay; b's update: b's; both or neither: the slower feed
    assert seen_after_us(a, b, t, 3_000, 7_000).tolist() == [3_000, 7_000, 7_000, 7_000]


def test_feed_delay_prices_from_older_quotes():
    # The sell venue's bid rises at 4 ms. Deciding at 5 ms with a 2 ms feed delay, the trader still sees 101.0.
    a = leg([0, 4_000], [101.0, 101.5], [101.1, 101.6])
    b = leg([0], [99.9], [100.0])
    fresh = execute(a, b, np.array([5_000]), 0, 0, 0, 1_000.0, "optimistic").iloc[0]
    late = execute(a, b, np.array([5_000]), 0, 0, 0, 1_000.0, "optimistic", feed_sell_us=2_000).iloc[0]
    assert np.isclose(fresh.edge_dec_bps, 1.5 / 100.75 * 1e4)
    assert np.isclose(late.edge_dec_bps, 1.0 / 100.5 * 1e4)


def test_trader_sees_a_birth_once_the_update_that_opened_it_arrives():
    # b's ask drops at 10 ms and opens the gap; a's bid falls at 13 ms and closes it.
    a = leg([0, 13_000], [101.0, 100.0], [101.1, 100.1])
    b = leg([0, 10_000], [100.9, 99.9], [101.2, 100.0])
    eps = births((10_000, "sell_a_buy_b"))
    legs = {"a": a, "b": b}
    now = replay_day(eps, legs, 0, 0.0, "optimistic").iloc[0]
    assert now.full_fill and now.seen_after_us == 0
    # b's feed is 5 ms late: the gap is seen at 15 ms, when a's bid (no feed delay) has already fallen.
    late_b = replay_day(eps, legs, 0, 0.0, "optimistic", feed_delay_ms=(0, 5)).iloc[0]
    assert late_b.seen_after_us == 5_000 and late_b.edge_dec_bps <= 0
    # Only a's feed is late: b's update is seen at once, and a's view (as of 5 ms) still shows 101.0.
    late_a = replay_day(eps, legs, 0, 0.0, "optimistic", feed_delay_ms=(5, 0)).iloc[0]
    assert late_a.seen_after_us == 0 and late_a.full_fill


def test_feed_delay_is_not_order_latency():
    # Both legs updated at the birth, so it is seen one (equal) feed delay later. The entry legs then
    # arrive as if the order latency were longer, but closing a one-sided fill takes one order latency.
    a = leg([0, 14_000, 18_000], [101.0] * 3, [101.1, 101.2, 101.6])
    b = leg([0, 7_000], [99.9, 100.9], [100.0, 101.0])   # the buy leg's gap is gone at 7 ms
    eps = births((0, "sell_a_buy_b"))
    feed = replay_day(eps, {"a": a, "b": b}, 5, 0.0, "optimistic", feed_delay_ms=(5, 5)).iloc[0]
    slow = replay_day(eps, {"a": a, "b": b}, 10, 0.0, "optimistic").iloc[0]
    assert feed.one_leg and slow.one_leg               # sold on a at 10 ms in both, missed on b
    assert np.isclose(feed.unwind, -feed.qty * (101.2 - 101.0))  # bought back at 10 + 5 ms
    assert np.isclose(slow.unwind, -slow.qty * (101.6 - 101.0))  # bought back at 10 + 10 ms


def test_usual_offset_is_read_from_the_books_the_trader_has_seen():
    a, b = leg([0], [101.0], [101.1]), leg([0], [99.9], [100.0])
    off = (np.array([0, 3_000], np.int64), np.array([0.0, -2.0]))  # the offset moves at 3 ms
    eps = births((0, "sell_a_buy_b"))
    plain = replay_day(eps, {"a": a, "b": b}, 0, 0.0, "optimistic", feed_delay_ms=(5, 5)).iloc[0]
    with_off = replay_day(eps, {"a": a, "b": b, "offset": off}, 0, 0.0, "optimistic", feed_delay_ms=(5, 5)).iloc[0]
    # Decided at 5 ms, but the books seen are as of 0 ms, when the offset was still 0.
    assert np.isclose(with_off.edge_dec_bps, plain.edge_dec_bps)
    later = replay_day(eps, {"a": a, "b": b, "offset": off}, 0, 0.0, "optimistic", decide_after_ms=5).iloc[0]
    assert not np.isclose(later.edge_dec_bps, plain.edge_dec_bps)


def busy_day():
    """400 updates on a tick leg a and 200 on a sampled leg b, sizes that vary, and 60 births."""
    k = np.arange(400)
    t = (k * 2_500 + (k * 37) % 1_000).astype(np.int64)
    mid = 100 + 0.05 * np.sin(k * 0.37) + 0.0004 * k
    jig = 0.02 * np.sin(k * 1.91)
    size = 0.01 + 0.19 * ((k * 7919) % 101) / 100
    a = Leg(t, mid + jig - 0.01, mid + jig + 0.01, size, size[::-1].copy(), False)
    j = k[::2]
    b = Leg(t[j] + 400, mid[j] - 0.01, mid[j] + 0.01, size[j][::-1].copy(), size[j], True)
    idx = (k[:60] * 6) + 3
    eps = pd.DataFrame({"birth_ts": t[idx], "direction": np.where(k[:60] % 3 == 0, "sell_b_buy_a", "sell_a_buy_b")})
    return eps, {"a": a, "b": b}


# Totals from the replay as it was before feed delay and liquidity reuse existed (main at 70d51c5).
BEFORE = {"optimistic": (-0.14776810035484234, 0.4268, 5, 40),
          "conservative": (-0.14729106170215742, 0.34030000000000005, 3, 40)}


def test_zero_feed_delay_and_no_depletion_match_the_old_replay():
    eps, legs = busy_day()
    for mode, (pnl, hedged, full, one_leg) in BEFORE.items():
        base = replay_day(eps, legs, 3, 1.0, mode, 2.0, 7, 2.0)
        assert np.isclose(base.pnl.sum(), pnl, rtol=1e-12, atol=0)
        assert np.isclose(base.hedged.sum(), hedged, rtol=1e-12, atol=0)
        assert base.full_fill.sum() == full and base.one_leg.sum() == one_leg
        zero = replay_day(eps, legs, 3, 1.0, mode, 2.0, 7, 2.0, feed_delay_ms=(0, 0), deplete=False)
        pd.testing.assert_frame_equal(base, zero)
        assert (base.seen_after_us == 0).all()


def test_replay_day_takes_one_decision_delay_per_birth():
    a = leg([0, 9_000], [101.0, 100.05], [101.1, 100.15])
    b = leg([0], [99.9], [100.0])
    eps = births((0, "sell_a_buy_b"), (1_000, "sell_a_buy_b"))
    both = replay_day(eps, {"a": a, "b": b}, 0, 0.0, "optimistic", decide_after_ms=np.array([0.0, 9.0]))
    first = replay_day(eps.iloc[[0]], {"a": a, "b": b}, 0, 0.0, "optimistic")
    second = replay_day(eps.iloc[[1]], {"a": a, "b": b}, 0, 0.0, "optimistic", decide_after_ms=9.0)
    pd.testing.assert_frame_equal(both, pd.concat([first, second]))


def test_convergence_pairs_refuse_the_new_options():
    a, b = leg([0], [101.0], [101.1]), leg([0], [99.9], [100.0])
    eps = births((0, "sell_perp_buy_spot"))
    with pytest.raises(ValueError):
        replay_day(eps, {"a": a, "b": b, "ctx": {}}, 0, 0.0, "optimistic", feed_delay_ms=(5, 5))
    with pytest.raises(ValueError):
        replay_day(eps, {"a": a, "b": b, "ctx": {}}, 0, 0.0, "optimistic", deplete=True)


# --- liquidity reuse --------------------------------------------------------------------------

def test_price_runs():
    assert price_runs(np.array([1.0, 1.0, 2.0, 2.0, 1.0])).tolist() == [0, 0, 1, 1, 2]
    assert price_runs(np.array([])).tolist() == []


def test_fill_depleting_matches_in_arrival_order():
    t_side, px = np.array([0, 100], np.int64), np.array([5.0, 5.0])   # one price run, sizes from the caller
    t_arr = np.array([30, 10, 20, 40], np.int64)
    want = np.array([0.6, 0.6, 0.0, 0.6])     # the order at 20 does not cross: it takes nothing
    size = np.array([1.0, 1.0, 1.0, 1.0])
    # arrival order: 10 takes 0.6, 20 takes 0, 30 gets the 0.4 left, 40 gets nothing
    assert np.allclose(fill_depleting(t_side, px, t_arr, want, size), [0.4, 0.6, 0.0, 0.0])
    # NaN size (before the first quote) fills nothing and uses up nothing
    assert np.allclose(fill_depleting(t_side, px, np.array([-5, 10]), np.array([1.0, 0.5]),
                                      np.array([np.nan, 1.0])), [0.0, 0.5])


def test_second_trigger_in_the_same_book_gets_what_is_left():
    a = leg([0], [101.0], [101.1], size=1.0)
    b = leg([0], [99.9], [100.0], size=1.0)
    t = np.array([0, 1_000])                      # both decisions see, and hit, the same quotes
    cap = 0.6 * 100.5                             # 0.6 units each
    reuse = execute(a, b, t, 0, 0, 0, cap, "optimistic")
    used = execute(a, b, t, 0, 0, 0, cap, "optimistic", deplete=True)
    assert np.allclose(reuse.hedged, [0.6, 0.6])
    assert np.allclose(used.hedged, [0.6, 0.4])
    assert used.full_fill.tolist() == [True, False]
    assert np.isclose(used.pnl.iloc[1], 0.4 * 1.0)


def test_used_size_comes_back_when_the_price_changes():
    a = leg([0, 500], [101.0, 101.1], [101.2, 101.2], size=1.0)   # the bid moves up at 0.5 ms
    b = leg([0], [99.9], [100.0], size=2.0)
    used = execute(a, b, np.array([0, 1_000]), 0, 0, 0, 0.6 * 100.5, "optimistic", deplete=True)
    # a fresh bid level, so the second order (about 0.6 units) fills in full again
    assert used.full_fill.all() and np.allclose(used.hedged, used.qty) and used.qty.iloc[1] > 0.5


def test_used_size_stays_used_through_a_size_only_update():
    a = leg([0, 500], [101.0, 101.0], [101.1, 101.1], size=[1.0, 1.2])  # more size joins at 101.0
    b = leg([0], [99.9], [100.0], size=10.0)
    used = execute(a, b, np.array([0, 1_000, 2_000]), 0, 0, 0, 0.6 * 100.5, "optimistic", deplete=True)
    # 1.2 shown minus the 0.6 already taken leaves 0.6 for the second; nothing for the third
    assert np.allclose(used.hedged, [0.6, 0.6, 0.0])


def test_depletion_changes_nothing_when_no_quotes_are_shared():
    a = leg([0, 5_000, 10_000], [101.0, 101.2, 101.4], [101.1, 101.3, 101.5], size=0.5)
    b = leg([0, 5_000, 10_000], [99.9, 99.8, 99.7], [100.0, 99.9, 99.8], size=0.5)
    t = np.array([0, 5_000, 10_000])              # each decision meets a new quote on both venues
    for mode in ("optimistic", "conservative"):
        pd.testing.assert_frame_equal(execute(a, b, t, 1_000, 1, 1, 1e6, mode),
                                      execute(a, b, t, 1_000, 1, 1, 1e6, mode, deplete=True))
