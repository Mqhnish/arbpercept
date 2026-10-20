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


# ---- births labelled against the usual offset (arbdata.episodes) -------------------------

def _cross_al(n=600, step_us=1_000_000, a_offset_bps=-3.0, spikes=()):
    """Venue a sits a_offset_bps from venue b (b mid 100). spikes: (index, leg, move in bps) one-event jumps."""
    t = np.arange(n, dtype=np.int64) * step_us
    b_mid = np.full(n, 100.0)
    a_mid = b_mid * (1 + a_offset_bps * 1e-4)
    for i, leg, bps in spikes:
        (a_mid if leg == "a" else b_mid)[i] *= 1 + bps * 1e-4
    half = 1e-4  # 0.01 bps half-spread
    return pd.DataFrame({"t": t, "valid": True, "a_mid": a_mid, "b_mid": b_mid,
                         "a_bid_px": a_mid - half, "a_ask_px": a_mid + half,
                         "b_bid_px": b_mid - half, "b_ask_px": b_mid + half})


def _births(al, direction, cross_ref):
    from arbdata.episodes import edges, label_runs
    e = edges(al, "cross", None, cross_ref=cross_ref)[direction]
    return label_runs(al.t.to_numpy(), e, al.valid.to_numpy(), 2.0, 0, 1)


def test_relative_spike_inside_a_raw_episode_becomes_a_birth():
    from arbdata.episodes import cross_offset_bps
    # Selling b and buying a earns the 3 bps offset all day: the raw gap never closes, so it never "opens".
    al = _cross_al(spikes=[(400, "b", 3.0)])
    assert _births(al, "sell_b_buy_a", None).empty
    rel = _births(al, "sell_b_buy_a", cross_offset_bps(al, 300))
    assert rel.birth_ts.tolist() == [400_000_000]
    assert np.isclose(rel.edge_birth_bps.iloc[0], 3.0, atol=0.05)


def test_gap_against_the_offset_is_found_without_beating_it_twice():
    from arbdata.episodes import cross_offset_bps
    # a rises 4 bps: relative to the usual -3 bps that is a 4 bps gap, but the raw gap is only ~1 bp.
    al = _cross_al(spikes=[(500, "a", 4.0)])
    assert _births(al, "sell_a_buy_b", None).empty
    rel = _births(al, "sell_a_buy_b", cross_offset_bps(al, 300))
    assert rel.birth_ts.tolist() == [500_000_000]


def test_offset_reference_skips_moments_when_a_leg_is_down():
    from arbdata.episodes import cross_offset_bps
    al = _cross_al(n=100, spikes=[(i, "a", 50.0) for i in range(20, 90)])
    assert cross_offset_bps(al, 300)[95] > 40          # most of the window is junk: it would drag the median
    al.loc[20:89, "valid"] = False                     # but it all happened while a feed was down
    assert np.isclose(cross_offset_bps(al, 300)[95], -3.0, atol=1e-3)


def test_label_pair_day_reports_the_offset_it_subtracted():
    from arbdata.config import PairSpec
    from arbdata.episodes import label_pair_day
    al = _cross_al(spikes=[(400, "b", 3.0)])
    for c in ("a", "b"):
        al[f"{c}_bid_sz"] = al[f"{c}_ask_sz"] = 1.0
        al[f"{c}_bid_depth5"] = al[f"{c}_ask_depth5"] = 5.0
        al[f"{c}_age_ms"] = al[f"{c}_lag_ms"] = 0.0
        al[f"{c}_is_update"], al[f"{c}_credit"] = True, 1
    feat = {"vol_windows_s": [1], "rate_windows_s": [1], "recent_births_window_s": 30, "trade_windows_s": []}
    ep = label_pair_day(al, PairSpec("x", "cross", "a", "b"), "1970-01-01", {"h": 2.0}, 1,
                        {"basis_ref_window_s": 60, "warmup_s": 300, "max_feed_lag_ms": 250}, feat,
                        cross_offset_window_s=300)
    row = ep[ep.direction == "sell_b_buy_a"].iloc[0]
    assert np.isclose(row.edge_offset_bps, 3.0, atol=1e-3)   # selling the rich venue: 3 bps of the raw gap is offset
    assert np.isclose(row.edge_birth_bps + row.edge_offset_bps, 6.0, atol=0.05)


# ---- the replay against the usual offset (arbtrade.evaluate) -------------------------------

def test_offset_at_times_uses_the_reference_in_force():
    from arbtrade.evaluate import offset_at_times
    off = (np.array([10, 20], dtype=np.int64), np.array([np.nan, -3.0]))
    assert np.allclose(offset_at_times(off, np.array([5, 15, 25]), -1.0), [0.0, 0.0, 3.0])


def test_recheck_and_pnl_are_measured_against_the_offset():
    from arbtrade.evaluate import replay_day
    from arbtrade.replay import Leg
    al = _cross_al(n=10)
    mk = lambda c: Leg(al.t.to_numpy(), al[f"{c}_bid_px"].to_numpy(), al[f"{c}_ask_px"].to_numpy(),
                       np.full(10, 1.0), np.full(10, 1.0), False)
    legs = {"a": mk("a"), "b": mk("b"), "offset": (al.t.to_numpy(), np.full(10, -3.0))}
    eps = pd.DataFrame({"birth_ts": [5_000_000], "direction": ["sell_b_buy_a"]})
    r = replay_day(eps, legs, 0, 0.0, "optimistic").iloc[0]
    raw = replay_day(eps, {"a": legs["a"], "b": legs["b"]}, 0, 0.0, "optimistic").iloc[0]
    # The raw gap (~3 bps) clears a 2 bps trigger, the relative gap (~0) does not: the slow path's re-check skips it.
    assert raw.edge_dec_bps > 2.0 and r.edge_dec_bps < 2.0
    assert np.isclose(r.edge_dec_bps, raw.edge_dec_bps - 3.0)
    assert np.isclose(r.pnl, raw.pnl)                                   # the fill itself is unchanged
    assert np.isclose(r.pnl_rel, r.pnl - r.hedged * r.mid_dec * 3e-4)   # but 3 bps of it is the offset
    assert r.pnl_rel < 0.01 * r.pnl
