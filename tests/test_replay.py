import numpy as np
import pandas as pd

from arbtrade.replay import Leg, execute


def leg(t, bid, ask, size=10.0, sampled=False):
    t = np.asarray(t, dtype=np.int64)
    return Leg(t, np.asarray(bid, float), np.asarray(ask, float), np.full(len(t), size), np.full(len(t), size), sampled)


def test_zero_latency_locks_in_the_edge():
    a = leg([0], [101.0], [101.1])           # sell here at 101.0
    b = leg([0], [99.9], [100.0])            # buy here at 100.0
    r = execute(a, b, np.array([0]), 0, 0.0, 0.0, 1_000.0, "optimistic").iloc[0]
    assert r.both_filled and r.full_fill
    assert np.isclose(r.pnl, r.qty * 1.0)    # one unit of price per unit of size
    assert np.isclose(r.pnl_bps, 1.0 / 100.5 * 1e4, rtol=1e-6)


def test_gap_gone_on_one_leg_creates_leg_risk():
    a = leg([0, 5_000], [101.0, 101.0], [101.1, 101.1])   # sell leg unchanged
    b = leg([0, 5_000], [99.9, 100.9], [100.0, 101.0])    # buy leg ask moved up by 1.0 at 5 ms
    r = execute(a, b, np.array([0]), 10_000, 0.0, 0.0, 1_000.0, "optimistic").iloc[0]
    assert r.one_leg and not r.both_filled
    # sold at 101.0, bought back on the sell venue at its ask 101.1 one latency later
    assert np.isclose(r.pnl, -r.qty * 0.1)


def test_fees_are_charged_on_every_fill():
    a = leg([0], [101.0], [101.1])
    b = leg([0], [99.9], [100.0])
    r = execute(a, b, np.array([0]), 0, 5.0, 5.0, 1_000.0, "optimistic").iloc[0]
    expected_fees = r.qty * (101.0 + 100.0) * 5 / 1e4
    assert np.isclose(r.fees, expected_fees)
    assert np.isclose(r.pnl, r.qty * 1.0 - expected_fees)


def test_conservative_bound_needs_both_snapshots():
    # Sampled buy leg: snapshot at 0 still crosses, the next one at 100 ms does not.
    a = leg([0], [101.0], [101.1])
    b = leg([0, 100_000], [99.9, 100.9], [100.0, 101.0], sampled=True)
    opt = execute(a, b, np.array([0]), 50_000, 0, 0, 1_000.0, "optimistic").iloc[0]
    con = execute(a, b, np.array([0]), 50_000, 0, 0, 1_000.0, "conservative").iloc[0]
    assert opt.both_filled and not con.both_filled
    assert con.pnl <= opt.pnl


def test_size_cap_and_displayed_size():
    a = leg([0], [101.0], [101.1], size=0.5)
    b = leg([0], [99.9], [100.0], size=10.0)
    r = execute(a, b, np.array([0]), 0, 0, 0, 1_000_000.0, "optimistic").iloc[0]
    assert np.isclose(r.qty, 0.5)  # limited by the thinner side at decision time


def test_fast_path_fires_once_when_a_gap_opens():
    from arbtrade.fastpath import stream_triggers
    venue = np.array([0, 1, 0, 0, 1], np.int8)
    bid = np.array([100.0, 99.0, 100.2, 100.3, 99.0])
    ask = np.array([100.1, 100.0, 100.3, 100.4, 100.1])
    # after event 2: sell venue 0 at 100.2, buy venue 1 at 100.0 -> ~2 bps gap opens; stays open at 3; closes at 4
    idx, d = stream_triggers(venue, bid, ask, 1.0)
    assert idx.tolist() == [2] and d.tolist() == [1]


def test_slow_path_reprices_from_quotes_seen_after_inference():
    from arbtrade.evaluate import replay_day
    # Venue a's bid drops 9 ms after the trigger; a slow path deciding at +9 ms must see the new price.
    a = leg([0, 9_000], [101.0, 100.05], [101.1, 100.15])
    b = leg([0], [99.9], [100.0])
    eps = pd.DataFrame({"birth_ts": [0], "direction": ["sell_a_buy_b"]})
    now = replay_day(eps, {"a": a, "b": b}, 0, 0.0, "optimistic")
    slow = replay_day(eps, {"a": a, "b": b}, 0, 0.0, "optimistic", decide_after_ms=9)
    assert np.isclose(now.edge_dec_bps.iloc[0], 1.0 / 100.5 * 1e4, rtol=1e-6)
    assert slow.edge_dec_bps.iloc[0] < 10       # the gap has mostly gone by the time the slow model is done
    assert slow.pnl.iloc[0] < now.pnl.iloc[0]


def test_conservative_fill_uses_the_smallest_size_shown_while_the_price_held():
    # Sell leg showed 10 when the gap opened, but size was pulled to 0.1 before the price changed.
    a = Leg(np.array([0], np.int64), np.array([101.0]), np.array([101.1]), np.array([10.0]), np.array([10.0]), False,
            np.array([0.1]), np.array([10.0]))
    b = leg([0], [99.9], [100.0])
    opt = execute(a, b, np.array([0]), 1_000, 0.0, 0.0, 1_000.0, "optimistic").iloc[0]
    con = execute(a, b, np.array([0]), 1_000, 0.0, 0.0, 1_000.0, "conservative").iloc[0]
    assert np.isclose(opt.hedged, opt.qty) and np.isclose(con.hedged, 0.1)
