import numpy as np
import pandas as pd

from arbtrade.inventory import account_day
from arbtrade.replay import Leg

DAY = 86_400_000_000


def flat_leg(bid, ask):
    t = np.array([0], dtype=np.int64)
    return Leg(t, np.array([bid]), np.array([ask]), np.array([10.0]), np.array([10.0]), False)


def test_offsetting_trades_need_no_flattening():
    a, b = flat_leg(99.9, 100.1), flat_leg(100.9, 101.1)
    r = account_day(np.array([10, 20]), np.array([1.0, -1.0]), np.array([5.0, 3.0]), a, b, None, None,
                    0, DAY, cap_base=5.0, fee_a_bps=0.0, fee_b_bps=0.0)
    assert r["end_position"] == 0 and r["flatten"] == 0 and r["realised"] == 8.0


def test_cap_skips_trades_that_grow_the_position_but_not_ones_that_shrink_it():
    a, b = flat_leg(99.9, 100.1), flat_leg(100.9, 101.1)
    r = account_day(np.array([1, 2, 3, 4]), np.array([1.0, 1.0, 1.0, -1.0]), np.ones(4), a, b, None, None,
                    0, DAY, cap_base=2.0, fee_a_bps=0.0, fee_b_bps=0.0)
    assert r["keep"].tolist() == [True, True, False, True]
    assert r["end_position"] == 1.0 and r["peak_position"] == 2.0


def test_leftover_position_is_closed_across_both_spreads_and_fees():
    # long 1 on a, short 1 on b: sell a at its bid 99.9, buy b back at its ask 101.1
    a, b = flat_leg(99.9, 100.1), flat_leg(100.9, 101.1)
    r = account_day(np.array([10]), np.array([1.0]), np.array([1.0]), a, b, None, None,
                    0, DAY, cap_base=5.0, fee_a_bps=10.0, fee_b_bps=10.0)
    fees = (99.9 + 101.1) * 10 / 1e4
    assert np.isclose(r["flatten"], 99.9 - 101.1 - fees)
    assert np.isclose(r["mark"], 100.0 - 101.0)          # marked at the mids, no costs
    assert np.isclose(r["realised"], 1.0 + 99.9 - 101.1 - fees)


def test_longs_pay_and_shorts_receive_funding():
    a, b = flat_leg(99.9, 100.1), flat_leg(99.9, 100.1)
    fund_a = pd.DataFrame({"ts": [8 * 3_600_000_000], "rate": [0.001]})
    fund_b = pd.DataFrame({"ts": [8 * 3_600_000_000], "rate": [0.0003]})
    r = account_day(np.array([10]), np.array([2.0]), np.zeros(1), a, b, fund_a, fund_b,
                    0, DAY, cap_base=5.0, fee_a_bps=0.0, fee_b_bps=0.0)
    # long 2 on a pays 2*100*0.001; short 2 on b receives 2*100*0.0003
    assert np.isclose(r["funding"], -0.2 + 0.06)


def test_trade_after_the_funding_time_does_not_pay_it():
    a, b = flat_leg(99.9, 100.1), flat_leg(99.9, 100.1)
    fund = pd.DataFrame({"ts": [100], "rate": [0.01]})
    r = account_day(np.array([200]), np.array([1.0]), np.zeros(1), a, b, fund, None,
                    0, DAY, cap_base=5.0, fee_a_bps=0.0, fee_b_bps=0.0)
    assert r["funding"] == 0.0
