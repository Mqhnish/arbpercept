import numpy as np

from arbtrade.convergence import execute_convergence, exit_signal_times, next_true_index
from arbtrade.replay import Leg


def leg(t, bid, ask, size=100.0):
    t = np.asarray(t, dtype=np.int64)
    return Leg(t, np.asarray(bid, float), np.asarray(ask, float), np.full(len(t), size), np.full(len(t), size), False)


def test_next_true_index():
    assert next_true_index(np.array([False, True, False, False, True])).tolist() == [1, 1, 4, 4, 4]
    assert next_true_index(np.array([False, False])).tolist() == [2, 2]


def test_exit_signal_respects_hold_limit():
    t = np.array([0, 10, 20, 30], dtype=np.int64)
    closed = np.array([False, False, True, False])
    assert exit_signal_times(t, closed, np.array([5]), 1_000).tolist() == [20]
    assert exit_signal_times(t, closed, np.array([5]), 8).tolist() == [13]       # hold limit first
    assert exit_signal_times(t, np.zeros(4, bool), np.array([5]), 100).tolist() == [105]


def test_convergence_profit_when_the_gap_closes():
    # b is 10 units rich at t=0 and back to fair at t=1 s; a does not move.
    b = leg([0, 1_000_000], [110.0, 100.0], [110.1, 100.1])
    a = leg([0, 1_000_000], [99.9, 99.9], [100.0, 100.0])
    t_ev = np.array([0, 1_000_000], dtype=np.int64)
    closed = np.array([False, True])
    fn = lambda t_arr: exit_signal_times(t_ev, closed, t_arr, 60_000_000)
    r = execute_convergence(b, a, np.array([0]), 0, 0.0, np.array([1100.0]), np.array([1000.0]), fn, "optimistic").iloc[0]
    # sold 10 b at 110, bought back at 100.1 (+99); bought 10 a at 100, sold at 99.9 (-1)
    assert r.full_fill and np.isclose(r.pnl, 10 * (110.0 - 100.1) + 10 * (99.9 - 100.0))
    assert np.isclose(r.hold_ms, 1000)


def test_convergence_pays_four_fees():
    b = leg([0, 1_000_000], [110.0, 100.0], [110.1, 100.1])
    a = leg([0, 1_000_000], [99.9, 99.9], [100.0, 100.0])
    t_ev = np.array([0, 1_000_000], dtype=np.int64)
    fn = lambda t_arr: exit_signal_times(t_ev, np.array([False, True]), t_arr, 60_000_000)
    free = execute_convergence(b, a, np.array([0]), 0, 0.0, np.array([1100.0]), np.array([1000.0]), fn, "optimistic").iloc[0]
    paid = execute_convergence(b, a, np.array([0]), 0, 10.0, np.array([1100.0]), np.array([1000.0]), fn, "optimistic").iloc[0]
    notionals = 10 * 110.0 + 10 * 100.0 + 10 * 100.1 + 10 * 99.9
    assert np.isclose(free.pnl - paid.pnl, notionals * 10 / 1e4)
