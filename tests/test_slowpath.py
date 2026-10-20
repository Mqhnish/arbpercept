"""The live slow-path features, one update at a time, against the offline vectorised code.

Synthetic raw feeds (with size-only updates and outages) go through the offline path
(normalize -> align -> features) and, quote by quote, through SlowFeatures. At every price
change the two must give the same value for every feature.
"""

import math

import numpy as np
import pandas as pd
import pytest

from arbdata.align import align
from arbdata.config import PairSpec
from arbdata.episodes import kalman_context, label_pair_day
from arbdata.features import features_at, rolling_context, trailing_reference
from arbdata.kalman import local_level, ou_halflife_s
from arbdata.normalize import RawFeed, _RunCollapser
from arbdata.quality import down_windows
from arbtrade.slowpath import (LocalLevel, OUHalfLife, SlowFeatures, TrailingMedian, WindowSum, benchmark,
                               synthetic_quotes)

DATE = "2026-01-10"  # a Saturday, so f_weekend is 1; the hour features move minute by minute
DAY0 = int(pd.Timestamp(DATE, tz="UTC").value // 1000)
MAX_GAP_MS = 1000
FEAT = {"vol_windows_s": [1, 10, 60], "rate_windows_s": [1, 10], "kalman_q_bps_per_sqrt_s": 0.2,
        "kalman_r_bps": 0.5, "ou_window_s": 60, "recent_births_window_s": 30}
EP_CFG = {"basis_ref_window_s": 60, "warmup_s": 60, "max_feed_lag_ms": 250}


def _raw_leg(rng, latent, step_us, offset_bps, outages, tick=0.5):
    n = len(latent) * 1000 // step_us
    t = DAY0 + np.cumsum(rng.integers(step_us // 2, step_us * 3 // 2, n)).astype(np.int64)
    t = t[t < DAY0 + len(latent) * 1000]
    n = len(t)
    mid = latent[(t - DAY0) // 1000] * (1 + offset_bps * 1e-4) * (1 + rng.normal(0, 1e-4, n))
    half = np.round(mid * rng.uniform(0.25e-4, 1e-4, n) / tick) * tick + tick
    mid = np.round(mid / tick) * tick
    hold = np.maximum.accumulate(np.where(rng.random(n) < 0.3, np.arange(n), 0))  # 70% of updates change sizes only
    mid, half = mid[hold], half[hold]
    keep = np.ones(n, dtype=bool)
    for lo, hi in outages:
        keep &= ~((t > DAY0 + lo * 1_000_000) & (t < DAY0 + hi * 1_000_000))
    return pd.DataFrame({"t": t, "exch": t - 5_000, "bid": mid - half, "ask": mid + half,
                         "bsz": rng.uniform(0.1, 5, n), "asz": rng.uniform(0.1, 5, n)})[keep]


def _normalize(raw):
    col, feed = _RunCollapser(), RawFeed()
    feed.observe(raw.t.to_numpy())
    col.add(raw.t.to_numpy(), raw.exch.to_numpy(), raw.bid.to_numpy(), raw.bsz.to_numpy(),
            raw.ask.to_numpy(), raw.asz.to_numpy())
    return col.frame(), down_windows(feed.silences_frame(), feed.last_ts, DAY0, MAX_GAP_MS)


@pytest.fixture(scope="module")
def stream():
    rng = np.random.default_rng(7)
    latent = 50_000.0 * np.exp(np.cumsum(rng.normal(0, 3e-6, 420 * 1000)))
    raw_a = _raw_leg(rng, latent, 30_000, 0.0, [(200, 203), (300, 306)])   # both down at 200 s, a alone at 300 s
    raw_b = _raw_leg(rng, latent, 100_000, 3.0, [(200, 203), (350, 356)])  # and b alone at 350 s
    raw_b = raw_b[~raw_b.t.isin(raw_a.t)]  # no shared timestamps: offline would make them one row
    (a, da), (b, db) = _normalize(raw_a), _normalize(raw_b)
    al = align(a, b, da, db)
    ev = pd.concat([raw_a.assign(leg=0), raw_b.assign(leg=1)]).sort_values("t", kind="stable")
    sf = SlowFeatures(FEAT, EP_CFG["basis_ref_window_s"], MAX_GAP_MS)
    ts, rows = [], []
    for t, leg, bid, ask, bsz, asz in ev[["t", "leg", "bid", "ask", "bsz", "asz"]].itertuples(index=False):
        if sf.update(int(leg), int(t), bid, ask, bsz, asz):
            ts.append(int(t))
            rows.append(sf.features())
    return al, sf, np.array(ts), pd.DataFrame(rows), len(ev)


def test_slow_features_match_the_offline_code_at_every_row(stream):
    al, sf, ts, live, n_raw = stream
    assert n_raw > 2 * len(al)                     # most raw updates were size-only and were not rows
    assert np.array_equal(ts, al.t.to_numpy())     # the same rows, in the same order
    valid = al.valid.to_numpy()
    assert (~valid).sum() > 50 and valid.sum() > 4_000
    ctx = rolling_context(al, FEAT["vol_windows_s"], FEAT["rate_windows_s"])
    ctx.update(kalman_context(al, valid, FEAT))
    basis = ((al.b_mid - al.a_mid) / al.a_mid * 1e4).to_numpy()
    off = features_at(al, ctx, basis - trailing_reference(al.t.to_numpy(), basis, EP_CFG["basis_ref_window_s"]),
                      np.arange(len(al)))
    assert np.isfinite(live.f_ou_halflife_s).sum() > 1_000 and live.f_weekend.max() == 1
    for c in sf.names():
        want, got = off[c].to_numpy(dtype=float), live[c].to_numpy(dtype=float)
        bad = ~np.isclose(got, want, rtol=1e-9, atol=1e-9, equal_nan=True)
        assert not bad.any(), (c, int(bad.sum()), got[bad][:3], want[bad][:3])


def test_slow_features_match_label_pair_day_at_births(stream):
    """The training data itself: at every labelled birth the live features equal the stored ones."""
    al, sf, ts, live, _ = stream
    pair = PairSpec(name="synthetic", type="cross", a="x", b="y")
    ep = label_pair_day(al, pair, DATE, {"gross>0bps": 0.0}, 100, EP_CFG, FEAT, leg_resolution_ms=(1, 100))
    assert len(ep) > 100
    assert set(sf.names()) <= set(ep.columns)
    at = live.set_index(ts).loc[ep.birth_ts.to_numpy()]
    for c in sf.names():
        assert np.allclose(at[c].to_numpy(dtype=float), ep[c].to_numpy(dtype=float), rtol=1e-9, atol=1e-9,
                           equal_nan=True), c


def test_local_level_matches_the_vectorised_filter():
    rng = np.random.default_rng(1)
    t = np.cumsum(rng.integers(1_000, 500_000, 3_000)).astype(np.int64)
    y = np.cumsum(rng.normal(0, 1e-5, len(t))) + rng.normal(0, 5e-5, len(t))
    y[:20] = np.nan                    # nothing to start from yet
    y[1_000:1_100] = np.nan            # a stretch of invalid rows: time moves on, the level does not
    m, p = local_level(t, y, 4e-10, 2.5e-9)
    kf = LocalLevel(4e-10, 2.5e-9)
    got = np.array([kf.step(int(ti), yi) for ti, yi in zip(t, y)])
    assert np.isnan(got[20, 0]) and np.isfinite(got[21, 0])
    assert np.allclose(got[:, 0], m, rtol=1e-12, atol=0, equal_nan=True)
    assert np.allclose(got[:, 1], p, rtol=1e-12, atol=0, equal_nan=True)


def test_ou_half_life_matches_the_vectorised_version():
    rng = np.random.default_rng(2)
    n = 6_000
    t = np.cumsum(rng.integers(10_000, 300_000, n)).astype(np.int64) + 1_700_000_000_000_000
    t[4_000:] += 90_000_000            # 90 s without rows: the grid carries the last value forward
    x = np.zeros(n)
    for i in range(1, n):
        x[i] = 0.97 * x[i - 1] + rng.normal(0, 1e-5)
    x[:5] = np.nan
    x[2_500:2_600] = np.nan            # missing values break the pairs that touch them
    want = ou_halflife_s(t, x, 60)
    ou = OUHalfLife(60)
    got = np.array([ou.step(int(ti), xi) for ti, xi in zip(t, x)])
    assert np.isfinite(want).sum() > 4_000
    assert np.allclose(got, want, rtol=1e-9, atol=0, equal_nan=True)


def test_window_sum_matches_the_pandas_rolling_sum():
    rng = np.random.default_rng(3)
    t = np.cumsum(rng.integers(1_000, 400_000, 5_000)).astype(np.int64)
    t[3_000:] += 5_000_000             # a silence longer than the window: the sum restarts
    v = rng.exponential(1e-10, len(t)) * (rng.random(len(t)) < 0.6)
    v[1_000:1_200] = 0.0               # a quiet stretch must read exactly zero
    want = pd.Series(v, index=pd.to_datetime(t, unit="us")).rolling("1000ms").sum().to_numpy()
    ws = WindowSum(1.0)
    got = []
    for ti, vi in zip(t, v):
        ws.add(int(ti), vi)
        got.append(ws.value())
    got = np.array(got)
    assert np.allclose(got, want, rtol=1e-12, atol=0)
    assert (got[want == 0] == 0).all() and (want == 0).sum() > 50


def test_trailing_median_uses_only_earlier_values():
    rng = np.random.default_rng(4)
    t = np.cumsum(rng.integers(1_000, 300_000, 3_000)).astype(np.int64)
    x = rng.normal(0, 1, len(t))
    want = trailing_reference(t, x, 10)
    tm = TrailingMedian(10)
    got = []
    for ti, xi in zip(t, x):
        got.append(tm.ref(int(ti)))
        tm.push(int(ti), xi)
        assert np.array_equal(tm.ref(int(ti)), got[-1], equal_nan=True)  # a row's own value never counts for itself
    assert np.isnan(got[0])
    assert np.allclose(got, want, rtol=0, atol=1e-12, equal_nan=True)


def test_rates_credit_size_only_updates_at_the_next_price_change():
    sf = SlowFeatures({"vol_windows_s": [1], "rate_windows_s": [1]})
    assert sf.update(0, 0, 100.0, 100.1, 1, 1)
    assert not sf.update(0, 100_000, 100.0, 100.1, 2, 1)       # size-only: counted, not a row
    assert not sf.update(0, 200_000, 100.0, 100.1, 3, 1)
    assert sf.features()["f_a_rate_1s"] == 1.0                 # still only the first price change
    assert sf.update(0, 300_000, 100.1, 100.2, 1, 1)
    assert sf.features()["f_a_rate_1s"] == 4.0                 # 1 + 2 size-only + this change
    assert sf.update(0, 1_300_000, 100.0, 100.1, 1, 1)        # the window (0.3 s, 1.3 s] has lost the first two
    f = sf.features()
    assert f["f_a_rate_1s"] == 1.0 and math.isnan(f["f_b_age_ms"]) and math.isnan(f["f_kalman_z"])


def test_benchmark_reports_the_cost_per_update():
    events = synthetic_quotes(seconds=30)
    assert len({t for t, *_ in events}) == len(events)         # no two updates share a timestamp
    res = benchmark(events, FEAT, n_triggers=50)
    assert res["quotes"] == len(events) and res["features"] == len(SlowFeatures(FEAT).names())
    assert 0 < res["price_changes"] < len(events) and res["engine_triggers"] >= 0
    for k in ("update_us", "update_price_change_us", "features_us", "inference_us", "trigger_us",
              "engine_us_per_quote", "engine_with_slow_us_per_quote"):
        assert 0 < res[k] < 10_000, k
