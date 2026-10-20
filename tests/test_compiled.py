import time

import numpy as np
from sklearn.ensemble import HistGradientBoostingClassifier

from arbtrade.compiled import CompiledTrees


def test_compiled_trees_match_sklearn_including_missing_values():
    rng = np.random.default_rng(0)
    X = rng.normal(size=(5000, 12))
    X[rng.random(X.shape) < 0.1] = np.nan
    y = ((np.nan_to_num(X[:, 0]) + 0.5 * np.nan_to_num(X[:, 3]) - np.isnan(X[:, 5])) > 0).astype(int)
    m = HistGradientBoostingClassifier(max_iter=150, max_leaf_nodes=31, random_state=0).fit(X, y)
    c = CompiledTrees(m)
    Xt = rng.normal(size=(2000, 12))
    Xt[rng.random(Xt.shape) < 0.1] = np.nan
    assert np.allclose(c.predict(Xt), m.predict_proba(Xt)[:, 1], atol=1e-9)
    assert np.isclose(c.predict_one(Xt[7]), m.predict_proba(Xt[[7]])[0, 1], atol=1e-9)


def test_compiled_single_row_is_fast():
    rng = np.random.default_rng(1)
    X = rng.normal(size=(3000, 40))
    y = (X[:, 0] > 0).astype(int)
    c = CompiledTrees(HistGradientBoostingClassifier(max_iter=200, random_state=0).fit(X, y))
    row = X[0]
    t0 = time.perf_counter()
    for _ in range(2000):
        c.predict_one(row)
    per_call_us = (time.perf_counter() - t0) / 2000 * 1e6
    assert per_call_us < 200  # far below sklearn's milliseconds per call
