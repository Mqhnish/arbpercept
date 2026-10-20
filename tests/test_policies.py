import numpy as np
import pandas as pd

from arbtrade.policies import FAST_FEATURES, FastPrior, choose_margins, expected_value_bps, miss_loss_bps


def test_expected_value_formula():
    ev = expected_value_bps(np.array([1.0, 0.0, 0.5]), np.array([5.0, 5.0, 5.0]), 2.0, -3.0)
    assert np.allclose(ev, [3.0, -3.0, 0.0])


def test_miss_loss_averages_incomplete_fills_only():
    out = pd.DataFrame({"full_fill": [True, False, False], "pnl_bps": [9.0, -2.0, 0.0]})
    assert miss_loss_bps(out) == -1.0


def test_cascade_margins_pick_the_profitable_split():
    rng = np.random.default_rng(0)
    ev = rng.normal(0, 1, 2000)
    pnl_now = np.where(ev > 1, 1.0, -1.0)            # acting now pays only for the top
    pnl_slow = np.where(ev > 0, 0.5, -1.0)           # the slow model helps in the middle
    lo, hi = choose_margins(ev, pnl_now, pnl_slow, slow_trade=ev > 0)
    assert hi >= 0.9 and lo <= 0.1


def test_fast_prior_learns_a_simple_rule():
    rng = np.random.default_rng(1)
    X = pd.DataFrame(rng.normal(0, 1, (3000, len(FAST_FEATURES))), columns=FAST_FEATURES)
    y = (X.edge_birth_bps + 0.1 * rng.normal(0, 1, len(X)) > 0).astype(int).to_numpy()
    p = FastPrior().fit(X, y).predict(X)
    assert ((p > 0.5) == y).mean() > 0.9


def test_models_survive_a_single_outcome_class():
    from arbtrade.policies import SlowModel
    X = pd.DataFrame(np.random.default_rng(2).normal(0, 1, (50, len(FAST_FEATURES))), columns=FAST_FEATURES)
    y = np.ones(50, dtype=bool)
    assert (FastPrior().fit(X, y).predict(X) > 0.99).all()
    assert (SlowModel().fit(X, y).predict(X) == 1.0).all()


def test_calibrator_fixes_overconfident_probabilities():
    from arbtrade.policies import Calibrator
    rng = np.random.default_rng(3)
    p_raw = rng.uniform(0, 1, 20_000)
    y = rng.random(20_000) < 0.5 * p_raw          # true rate is half of what the model says
    c = Calibrator().fit(p_raw[:10_000], y[:10_000])
    q = c.transform(p_raw[10_000:])
    yt = y[10_000:]
    hi = p_raw[10_000:] > 0.8
    assert abs(yt[hi].mean() - q[hi].mean()) < 0.05   # calibrated (isotonic steps, ~2,000 samples in the bin)
    assert abs(yt[hi].mean() - p_raw[10_000:][hi].mean()) > 0.3  # raw was far off
