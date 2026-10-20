"""The live paper trader measured against the venues' usual offset, as the offline evaluation is."""

import math

import numpy as np
import pandas as pd

from arbtrade.live import PaperEngine, prior_matches

DAY0 = 0


def engine(window_s=300.0, **kw):
    return PaperEngine(("x", "y"), trigger_bps=2.0, fee_bps=0.0, latency_ms={"x": 1, "y": 1}, notional=1_000.0,
                       offset_window_s=window_s, **kw)


def settle_offset(e, n=50, x_mid=100.05, y_mid=100.0, step=1_000_000):
    """x sits ~5 bps above y for n seconds: alternating price changes so both books stay fresh."""
    for k in range(n):
        dx = 0.0001 * (k % 2)  # a tiny change so every update is a price change
        e.on_quote("x", k * step, x_mid - 0.005 + dx, x_mid + 0.005 + dx, 10, 10)
        e.on_quote("y", k * step + 500_000, y_mid - 0.005 + dx, y_mid + 0.005 + dx, 10, 10)
    return n * step


def test_a_persistent_offset_does_not_trigger():
    e = engine()
    settle_offset(e)
    assert e.triggers == 0                         # selling x / buying y earns the ~4 bps (net of spreads) offset all the time
    raw = engine(window_s=None)
    settle_offset(raw)
    assert raw.triggers == 1                       # measured against zero it fires (once, and stays open)


def test_a_gap_beyond_the_usual_offset_triggers():
    e = engine()
    t = settle_offset(e)
    e.on_quote("x", t, 100.085, 100.095, 10, 10)   # x jumps a further ~4 bps
    assert e.triggers == 1
    d = e.decisions[-1]
    assert d["direction"].startswith("sell x") and d["edge_bps"] > 7 and 2 < d["edge_rel_bps"] < 3.5


def test_nothing_triggers_before_the_first_offset_sample():
    e = engine()
    e.on_quote("x", 0, 100.1, 100.2, 10, 10)
    e.on_quote("y", 1, 99.9, 100.0, 10, 10)        # a 10 bps raw gap, but no usual level yet
    assert e.triggers == 0


def test_offset_reference_uses_only_earlier_samples_and_drops_old_ones():
    e = engine(window_s=10)
    e.on_quote("x", 0, 100.0, 100.0, 10, 10)
    e.on_quote("y", 1, 100.0, 100.0, 10, 10)        # first sample: 0 bps
    assert math.isclose(e.offset_ref(2), 0.0, abs_tol=1e-9)
    e.on_quote("x", 5_000_000, 100.1, 100.1, 10, 10)  # decided against the 0 bps sample, then sampled at ~10 bps
    assert math.isclose(e.offset_ref(5_000_001), 5.0, rel_tol=1e-3)      # median of 0 and ~10
    assert math.isclose(e.offset_ref(10_000_002), 10.0, rel_tol=1e-3)    # the 0 bps samples are older than 10 s


def test_stale_moments_are_not_sampled():
    e = engine(stale_ms=100)
    e.on_quote("x", 0, 100.0, 100.0, 10, 10)
    e.on_quote("y", 1, 100.0, 100.0, 10, 10)
    e.on_quote("x", 1_000_000, 101.0, 101.0, 10, 10)   # y has been silent for 1 s: this sample is skipped
    assert len(e.off_samples) == 1


def test_live_offset_matches_the_offline_reference():
    """Same quotes, same rule: the engine's reference equals cross_offset_bps over the price-change events."""
    from arbdata.episodes import cross_offset_bps
    rng = np.random.default_rng(0)
    e = engine(window_s=30)
    t, seen = 0, set()
    rows, refs = [], []
    books = {"x": (100.03, 100.04), "y": (100.0, 100.01)}
    for k in range(400):
        t += int(rng.integers(50_000, 400_000))
        v = "x" if rng.random() < 0.5 else "y"
        bid = round(books[v][0] + rng.normal(0, 0.01), 4)
        if bid == books[v][0]:
            bid += 0.0001  # offline rows are price changes only (size-only updates are folded away)
        books[v] = (bid, bid + 0.01)
        refs.append(e.offset_ref(t))
        e.on_quote(v, t, *books[v], 10, 10)
        seen.add(v)
        # the engine only knows a venue's book once that venue has quoted
        rows.append({"t": t, "a_mid": sum(books["x"]) / 2, "b_mid": sum(books["y"]) / 2, "valid": len(seen) == 2})
    al = pd.DataFrame(rows)
    offline = cross_offset_bps(al, 30)
    assert np.isfinite(offline).sum() > 300
    assert np.allclose(np.asarray(refs), offline, equal_nan=True, atol=1e-9)


def test_calibrated_prior_and_matching_check():
    prior = {"features": ["edge_birth_bps"], "median": np.array([0.0]), "mu": np.array([0.0]), "sd": np.array([1.0]),
             "w": np.array([0.0]), "b": 0.0, "cal_x": [0.0, 1.0], "cal_y": [0.0, 0.2], "offset_window_s": 300.0}
    e = engine(prior=prior, loss_bps=0.0)
    # the raw model says 50%; calibration maps it to 10%: EV = 0.1 * (6 - 2)
    assert math.isclose(e._prior_ev({"edge_birth_bps": 6.0}), 0.4, rel_tol=1e-9)
    assert prior_matches(prior, 300.0) and not prior_matches(prior, None)
    assert prior_matches({"b": 0.0}, None) and not prior_matches({"b": 0.0}, 300.0)  # an old raw-gap prior
