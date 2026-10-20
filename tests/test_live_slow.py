"""The live paper trader running a compiled slow model on the incremental slow-path features."""

import numpy as np
import pytest
from sklearn.ensemble import HistGradientBoostingClassifier

from arbtrade.compiled import CompiledTrees
from arbtrade.live import SLOW_FEATURE_DEFAULTS, PaperEngine
from arbtrade.slowpath import SlowFeatures

FEATURES = ["edge_birth_bps", "f_a_spread_bps", "f_kalman_z", "f_rv_10s_bps", "f_b_rate_1s", "f_ou_halflife_s"]


def bundle(fill_share=0.95, **kw):
    rng = np.random.default_rng(0)
    X = rng.normal(0, 1, (2_000, len(FEATURES)))
    y = (rng.random(len(X)) < fill_share).astype(int)
    model = HistGradientBoostingClassifier(max_iter=20, random_state=0).fit(X, y)
    return {"model": CompiledTrees(model), "sk": model, "features": FEATURES, "loss_bps": -1.0, **kw}


def engine(slow):
    return PaperEngine(("x", "y"), trigger_bps=2.0, fee_bps=0.0, latency_ms={"x": 5, "y": 1}, notional=1_000.0,
                       slow=slow)


def open_gap(e):
    e.on_quote("x", 0, 100.0, 100.1, 10, 10)
    e.on_quote("y", 1, 99.9, 100.0, 10, 10)
    e.on_quote("y", 2, 99.9, 100.0, 11, 10)       # size-only: counted for the rates, not a row
    e.on_quote("x", 3, 100.1, 100.2, 10, 10)      # sell x at 100.1, buy y at 100.0: a 10 bps gap opens


def test_slow_policy_scores_the_features_of_the_trigger_update():
    s = bundle()
    e = engine(s)
    open_gap(e)
    dec = {d["policy"]: d for d in e.decisions}
    assert set(dec) == {"naive", "slow"} and dec["slow"]["action"] == "ENTER"
    # what the engine scored is a tracker's state after the same quotes
    sf = SlowFeatures(SLOW_FEATURE_DEFAULTS)
    for leg, t, bid, ask, bsz, asz in [(0, 0, 100.0, 100.1, 10, 10), (1, 1, 99.9, 100.0, 10, 10),
                                       (1, 2, 99.9, 100.0, 11, 10), (0, 3, 100.1, 100.2, 10, 10)]:
        sf.update(leg, t, bid, ask, bsz, asz)
    want = sf.features()
    assert want["f_b_rate_1s"] == 1.0             # y's size-only update waits for y's next price change
    tr = next(tr for tr in e.trades if tr.policy == "slow")
    assert np.allclose([tr.features[f] for f in FEATURES[1:]], [want[f] for f in FEATURES[1:]],
                       rtol=0, atol=0, equal_nan=True)
    assert tr.features["edge_birth_bps"] == tr.edge_bps  # no offset here: the relative gap is the raw gap
    # and the compiled model gives sklearn's probability for that vector
    v = np.array([tr.features[f] for f in FEATURES])
    assert np.isclose(s["model"].predict_one(v), s["sk"].predict_proba(v[None])[0, 1], rtol=1e-9)
    assert e.summary()["slow"]["decision_us_median"] > 0


def test_slow_policy_skips_when_calibrated_expected_value_is_negative():
    e = engine(bundle(cal_x=[0.0, 1.0], cal_y=[0.0, 0.0]))   # calibration says nothing ever fills
    open_gap(e)
    dec = next(d for d in e.decisions if d["policy"] == "slow")
    assert dec["action"] == "SKIP_EV" and dec["reason"] == "slow model expected value -1.00 bps"
    assert not [tr for tr in e.trades if tr.policy == "slow"]


def test_a_slow_model_needing_offline_only_features_is_refused():
    s = bundle()
    s["features"] = FEATURES + ["f_a_lag_ms", "f_b_trades_per_s_1s"]
    with pytest.raises(ValueError, match="f_a_lag_ms"):
        engine(s)


def test_without_a_slow_model_the_engine_keeps_no_slow_state():
    e = engine(None)
    open_gap(e)
    assert e.sf is None and {d["policy"] for d in e.decisions} == {"naive"}
