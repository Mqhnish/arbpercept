"""The gap-size-only baseline, the exported calibration map, the leg-risk term net of the offset,
and the fill-probability quality scores."""

import numpy as np
import pandas as pd

from arbtrade.policies import FAST_FEATURES, GAP_ONLY_FEATURES, Calibrator, FastPrior, miss_loss_bps, q_quality


def test_gap_size_baseline_uses_only_the_gap():
    rng = np.random.default_rng(4)
    X = pd.DataFrame(rng.normal(0, 1, (2000, len(FAST_FEATURES))), columns=FAST_FEATURES)
    y = (X.f_rv_1s_bps > 0).to_numpy()                   # depends on something the gap model cannot see
    gap = FastPrior(GAP_ONLY_FEATURES).fit(X, y)
    assert gap.features == ["edge_birth_bps"] and len(gap.w) == 1
    X2 = X.copy()
    X2["f_rv_1s_bps"] = 0.0                              # changing other columns changes nothing
    assert np.allclose(gap.predict(X), gap.predict(X2))
    assert FastPrior().features == FAST_FEATURES          # the default is still the six-feature prior


def test_calibrator_exports_the_same_map():
    rng = np.random.default_rng(5)
    p = rng.uniform(0, 1, 5000)
    c = Calibrator().fit(p, rng.random(5000) < p ** 2)
    x, yv = c.to_arrays()
    probe = np.linspace(-0.1, 1.1, 101)
    assert np.allclose(np.interp(probe, x, yv), c.transform(probe))
    assert Calibrator().fit(p, np.zeros(5000, bool)).to_arrays() is None


def test_miss_loss_can_use_pnl_net_of_the_offset():
    out = pd.DataFrame({"full_fill": [True, False], "pnl_bps": [9.0, 1.0], "pnl_rel_bps": [6.0, -2.0]})
    assert miss_loss_bps(out) == 1.0
    assert miss_loss_bps(out, "pnl_rel_bps") == -2.0


def test_q_quality_scores_ranking_and_calibration():
    y = np.array([0, 0, 1, 1])
    perfect = q_quality(y, np.array([0.0, 0.0, 1.0, 1.0]))
    assert perfect["auc"] == 1.0 and perfect["brier"] == 0.0 and perfect["brier_skill"] == 1.0
    base = q_quality(y, np.full(4, 0.5))                 # always the fill rate: no skill, no ranking
    assert base["auc"] == 0.5 and base["brier_skill"] == 0.0 and base["fill_rate"] == 0.5 and base["n"] == 4
    overconfident = q_quality(y, np.array([0.4, 0.6, 0.9, 1.0]) ** 0.1)   # ranks perfectly, says too much
    assert overconfident["auc"] == 1.0 and overconfident["brier_skill"] < 0
    one_class = q_quality(np.ones(3), np.full(3, 0.9))   # no ranking to score with one outcome only
    assert np.isnan(one_class["auc"]) and np.isnan(one_class["brier_skill"])
    assert q_quality(np.array([]), np.array([]))["n"] == 0
