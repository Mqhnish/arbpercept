import numpy as np

from arbdata.episodes import label_runs, recent_births


def _t(n):
    return np.arange(n, dtype=np.int64) * 100_000  # one event every 100 ms


def test_birth_death_and_interval_bounds():
    edge = np.array([0, 3, 3, 0, 0, 4, 0], dtype=float)
    valid = np.ones(7, dtype=bool)
    ep = label_runs(_t(7), edge, valid, hurdle=1.0, warmup_end=0, resolution_ms=100)
    assert ep.birth_ts.tolist() == [100_000, 500_000]
    assert ep.died.tolist() == [True, True]
    assert ep.obs_ms.tolist() == [200.0, 100.0]
    assert ep.lower_ms.tolist() == [100.0, 0.0]
    assert ep.upper_ms.tolist() == [300.0, 200.0]
    assert ep.n_events.tolist() == [2, 1]


def test_censoring_and_unknown_births():
    edge = np.array([5, 5, 0, 5, 5, 5, 0, 5, 5], dtype=float)
    valid = np.array([1, 1, 1, 1, 1, 0, 1, 1, 1], dtype=bool)
    ep = label_runs(_t(9), edge, valid, hurdle=1.0, warmup_end=0, resolution_ms=100)
    # run at 0 is dropped (birth before data starts is unknown)
    # run at 3 is cut by invalid data at 5 -> censored, lower bound only
    # run at 7 runs to the end of the day -> censored
    assert ep.birth_ts.tolist() == [300_000, 700_000]
    assert ep.died.tolist() == [False, False]
    assert ep.end_reason.tolist() == ["data_gap", "end_of_day"]
    assert np.isinf(ep.upper_ms).all()
    assert ep.lower_ms.tolist() == [100.0, 100.0]


def test_nan_edge_is_unknown_not_zero():
    edge = np.array([np.nan, 5, 5, 0], dtype=float)
    ep = label_runs(_t(4), edge, np.ones(4, dtype=bool), hurdle=1.0, warmup_end=0, resolution_ms=1)
    assert ep.empty  # the run starts right after an unknown edge, so its birth is unknown


def test_warmup_and_peak():
    edge = np.array([0, 2, 0, 0, 2, 6, 3, 0], dtype=float)
    ep = label_runs(_t(8), edge, np.ones(8, dtype=bool), hurdle=1.0, warmup_end=300_000, resolution_ms=1)
    assert ep.birth_ts.tolist() == [400_000]
    assert ep.edge_peak_bps.tolist() == [6.0]
    assert ep.t_to_peak_ms.tolist() == [100.0]


def test_recent_births_counts_strictly_past():
    ts = np.array([0, 10, 20, 20, 100], dtype=np.int64)
    assert recent_births(ts, 15).tolist() == [0, 1, 1, 1, 0]


def test_ratio_pair_tracks_fair_value_and_flags_a_mispricing():
    import pandas as pd
    from arbdata.episodes import edges, ratio_fair
    rng = np.random.default_rng(4)
    n = 20_000
    t = np.arange(n, dtype=np.int64) * 100_000
    a_mid = 60_000 * np.exp(np.cumsum(rng.normal(0, 2e-5, n)))
    b_mid = np.exp(0.3 + 0.8 * np.log(a_mid))            # b moves 0.8x a in log terms
    b_mid[15_000:15_010] *= 1 + 6e-4                     # b briefly 6 bps rich
    half = 0.05e-4
    al = pd.DataFrame({"a_bid_px": a_mid * (1 - half), "a_ask_px": a_mid * (1 + half), "a_mid": a_mid,
                       "b_bid_px": b_mid * (1 - half), "b_ask_px": b_mid * (1 + half), "b_mid": b_mid})
    cfg = {"ratio_q_alpha_bps_per_sqrt_s": 0.5, "ratio_q_beta_per_sqrt_s": 1e-3, "ratio_r_bps": 2.0}
    alpha, beta = ratio_fair(t, al, np.ones(n, bool), cfg)
    fair = alpha + beta * np.log(a_mid)
    assert np.abs((np.log(b_mid) - fair)[10_000:14_990]).max() * 1e4 < 1.0   # tracks within 1 bp
    e = edges(al, "ratio", None, (alpha, beta))["sell_b_buy_a"]
    assert e[15_000] > 4.5 and e[14_990] < 0.5                               # the 6 bps rich spell stands out
