"""Features must not change when the future is deleted.

Synthetic raw feeds (with size-only updates, so run folding is exercised) are pushed
through the same normalize -> align -> label path as real data. For a sample of births
the RAW feeds are cut at the birth instant and everything is rebuilt. Every feature
(and the birth edge) must be identical: if any value moved, it was using information
from after the moment a trader would act.
"""

import numpy as np
import pandas as pd

from arbdata.align import align, delayed_view
from arbdata.config import PairSpec
from arbdata.episodes import label_pair_day
from arbdata.normalize import RawFeed, _RunCollapser
from arbdata.quality import down_windows

DATE = "2026-01-05"
DAY0 = int(pd.Timestamp(DATE, tz="UTC").value // 1000)
EP_CFG = {"basis_ref_window_s": 60, "warmup_s": 60, "max_feed_lag_ms": 250}
FEAT_CFG = {"vol_windows_s": [1, 10], "rate_windows_s": [1], "recent_births_window_s": 30,
            "trade_windows_s": [1, 10], "trade_publish_margin_ms": 50, "stale_partner_fraction": 0.5}
HURDLES = {"gross>0bps": 0.0, "gross>1bps": 1.0}
MAX_GAP_MS = 1000


def _latent(rng, seconds=400):
    """One efficient price on a 1 ms grid that every venue tracks with its own noise."""
    return 50_000.0 * np.exp(np.cumsum(rng.normal(0, 3e-6, seconds * 1000)))


def _raw_leg(rng, latent, step_us, n, jitter, offset_bps=0.0, tick=0.5):
    t = DAY0 + np.cumsum(rng.integers(step_us - jitter, step_us + jitter + 1, n)).astype(np.int64)
    ms = np.minimum((t - DAY0) // 1000, len(latent) - 1)
    mid = latent[ms] * (1 + offset_bps * 1e-4) * (1 + rng.normal(0, 1.5e-4, n))
    half = np.round(mid * rng.uniform(0.25e-4, 1e-4, n) / tick) * tick + tick
    mid = np.round(mid / tick) * tick
    # As in real feeds, most raw updates change only sizes: hold the quote between price updates.
    last_price_row = np.maximum.accumulate(np.where(rng.random(n) < 0.3, np.arange(n), 0))
    mid, half = mid[last_price_row], half[last_price_row]
    # A short outage, so feed-health handling is exercised too.
    keep = ~((t > DAY0 + 200_000_000) & (t < DAY0 + 203_000_000))
    return pd.DataFrame({"t": t, "exch": t - rng.integers(1_000, 20_000, n), "bid": mid - half,
                         "ask": mid + half, "bsz": rng.uniform(0.1, 5, n), "asz": rng.uniform(0.1, 5, n)})[keep]


def _trades(rng, raw):
    """Trades near each raw quote, stamped a little before or after it."""
    n = len(raw) // 2
    pick = np.sort(rng.choice(len(raw), n, replace=False))
    q = raw.iloc[pick]
    side = rng.choice([-1, 1], n).astype(np.int8)
    return pd.DataFrame({"ts": q.t.to_numpy() + rng.integers(-5_000, 5_000, n), "price": np.where(side > 0, q.ask, q.bid),
                         "size": rng.uniform(0.001, 1, n), "side": side, "rpi": np.zeros(n, dtype=bool)}).sort_values("ts")


def _normalize(raw):
    col, feed = _RunCollapser(), RawFeed()
    feed.observe(raw.t.to_numpy())
    col.add(raw.t.to_numpy(), raw.exch.to_numpy(), raw.bid.to_numpy(), raw.bsz.to_numpy(),
            raw.ask.to_numpy(), raw.asz.to_numpy())
    down = down_windows(feed.silences_frame(), feed.last_ts, DAY0, MAX_GAP_MS)
    return col.frame(), down


def _episodes(raw_a, raw_b, pair_type, tr_a, tr_b, offset_window_s=None, feed_ms=(0.0, 0.0)):
    (a, da), (b, db) = _normalize(raw_a), _normalize(raw_b)
    a, da, tr_a = delayed_view(a, da, tr_a, feed_ms[0])
    b, db, tr_b = delayed_view(b, db, tr_b, feed_ms[1])
    pair = PairSpec(name="synthetic", type=pair_type, a="x", b="y")
    return label_pair_day(align(a, b, da, db), pair, DATE, HURDLES, 100, EP_CFG, FEAT_CFG,
                          leg_resolution_ms=(1, 100), trades=(tr_a, tr_b), cross_offset_window_s=offset_window_s)


def _check(pair_type, seed, offset_window_s=None):
    rng = np.random.default_rng(seed)
    latent = _latent(rng)
    raw_a = _raw_leg(rng, latent, 30_000, 12_000, 20_000)       # irregular, ~30 ms
    raw_b = _raw_leg(rng, latent, 100_000, 3_600, 2_000, 3.0)   # sampled, ~100 ms, small premium
    tr_a, tr_b = _trades(rng, raw_a), _trades(rng, raw_b)
    full = _episodes(raw_a, raw_b, pair_type, tr_a, tr_b, offset_window_s)
    assert len(full) > 20, "synthetic data should produce episodes"
    assert full.f_a_trades_per_s_1s.gt(0).any() and full.stale_partner.any() and (~full.stale_partner).any()
    fcols = [c for c in full.columns if c.startswith("f_")] + ["edge_birth_bps", "stale_birth", "stale_partner"]
    if offset_window_s:
        fcols.append("edge_offset_bps")  # the venues' usual offset must come from the past only
    for _, ep in full.sample(25, random_state=seed).iterrows():
        cut = ep.birth_ts
        part = _episodes(raw_a[raw_a.t <= cut], raw_b[raw_b.t <= cut], pair_type,
                         tr_a[tr_a.ts <= cut], tr_b[tr_b.ts <= cut], offset_window_s)
        match = part[(part.birth_ts == cut) & (part.direction == ep.direction) & (part.hurdle_name == ep.hurdle_name)]
        assert len(match) == 1, "a birth must still exist when everything after it is removed"
        got = match.iloc[0][fcols].astype(float).to_numpy()
        want = ep[fcols].astype(float).to_numpy()
        assert np.allclose(got, want, equal_nan=True), {c: (w, g) for c, w, g in zip(fcols, want, got) if not np.isclose(w, g, equal_nan=True)}


def test_cross_features_are_causal():
    _check("cross", 1)


def test_basis_features_are_causal():
    _check("basis", 2)


def test_ratio_features_are_causal():
    _check("ratio", 3)


def test_cross_features_against_the_usual_offset_are_causal():
    # births labelled on the gap minus the trailing offset (arbtrade.evaluate --offset-aware)
    _check("cross", 4, offset_window_s=60)


def test_with_a_feed_delay_unseen_messages_cannot_change_a_birth():
    # Births built from the books as the trader receives them (arbtrade.evaluate --feed-delay-ms).
    # At a birth the trader has seen each venue only up to its feed delay earlier. Deleting every
    # message it has not received yet must leave the birth and all its features unchanged.
    rng = np.random.default_rng(5)
    latent = _latent(rng)
    raw_a = _raw_leg(rng, latent, 30_000, 12_000, 20_000)
    raw_b = _raw_leg(rng, latent, 100_000, 3_600, 2_000, 3.0)
    tr_a, tr_b = _trades(rng, raw_a), _trades(rng, raw_b)
    feed = (2.0, 45.0)
    full = _episodes(raw_a, raw_b, "cross", tr_a, tr_b, 60, feed)
    assert len(full) > 20
    fcols = [c for c in full.columns if c.startswith("f_")] + ["edge_birth_bps", "edge_offset_bps", "stale_birth"]
    for _, ep in full.sample(25, random_state=5).iterrows():
        ca, cb = ep.birth_ts - int(feed[0] * 1000), ep.birth_ts - int(feed[1] * 1000)
        part = _episodes(raw_a[raw_a.t <= ca], raw_b[raw_b.t <= cb], "cross",
                         tr_a[tr_a.ts <= ca], tr_b[tr_b.ts <= cb], 60, feed)
        match = part[(part.birth_ts == ep.birth_ts) & (part.direction == ep.direction) & (part.hurdle_name == ep.hurdle_name)]
        assert len(match) == 1, "a birth must still exist when every unseen message is removed"
        got, want = match.iloc[0][fcols].astype(float).to_numpy(), ep[fcols].astype(float).to_numpy()
        assert np.allclose(got, want, equal_nan=True), {c: (w, g) for c, w, g in zip(fcols, want, got) if not np.isclose(w, g, equal_nan=True)}


def test_without_the_delayed_view_unseen_messages_do_change_births():
    # The check above has teeth: births built from the raw books (the old way) use messages the
    # trader has not received yet, so cutting those messages changes some of them.
    rng = np.random.default_rng(5)
    latent = _latent(rng)
    raw_a = _raw_leg(rng, latent, 30_000, 12_000, 20_000)
    raw_b = _raw_leg(rng, latent, 100_000, 3_600, 2_000, 3.0)
    tr_a, tr_b = _trades(rng, raw_a), _trades(rng, raw_b)
    full = _episodes(raw_a, raw_b, "cross", tr_a, tr_b, 60)
    changed = 0
    for _, ep in full.sample(25, random_state=5).iterrows():
        ca, cb = ep.birth_ts - 2_000, ep.birth_ts - 45_000
        part = _episodes(raw_a[raw_a.t <= ca], raw_b[raw_b.t <= cb], "cross",
                         tr_a[tr_a.ts <= ca], tr_b[tr_b.ts <= cb], 60)
        match = part[(part.birth_ts == ep.birth_ts) & (part.direction == ep.direction) & (part.hurdle_name == ep.hurdle_name)]
        changed += len(match) == 0 or not np.isclose(match.iloc[0].edge_birth_bps, ep.edge_birth_bps)
    assert changed > 0
