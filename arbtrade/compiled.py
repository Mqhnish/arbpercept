"""Compile a fitted HistGradientBoostingClassifier into a Numba tree walker.

sklearn's predict_proba spends milliseconds per call on input checks and Python overhead,
which on a single trigger is the whole cost of the slow path. The model itself is just a
few hundred small trees: walking them for one row takes microseconds. This module copies
each tree's split table into flat arrays and evaluates them in compiled code, giving the
same probabilities as sklearn (checked in tests/test_compiled.py).

Traversal rule (numerical features, as sklearn uses them): a missing value follows the
node's learned missing direction; otherwise go left if x <= threshold.
"""

from __future__ import annotations

import numpy as np

try:
    from numba import njit
except ImportError:  # pragma: no cover
    def njit(*args, **kwargs):
        return (lambda f: f) if not args or not callable(args[0]) else args[0]


@njit(cache=True)
def _raw_one(x, feat, thr, mleft, left, right, leaf, val, starts, base):
    s = base
    for k in range(len(starts)):
        o = starts[k]
        i = o
        while not leaf[i]:
            v = x[feat[i]]
            go_left = mleft[i] if np.isnan(v) else v <= thr[i]
            i = o + (left[i] if go_left else right[i])
        s += val[i]
    return s


@njit(cache=True)
def _raw_many(X, feat, thr, mleft, left, right, leaf, val, starts, base):
    out = np.empty(X.shape[0])
    for r in range(X.shape[0]):
        out[r] = _raw_one(X[r], feat, thr, mleft, left, right, leaf, val, starts, base)
    return out


class CompiledTrees:
    def __init__(self, model):
        if getattr(model, "n_trees_per_iteration_", 1) != 1:
            raise ValueError("binary classifiers only")
        trees = [preds[0] for preds in model._predictors]
        if any(t.nodes["is_categorical"].any() for t in trees):
            raise ValueError("categorical splits are not supported")
        sizes = [len(t.nodes) for t in trees]
        self.starts = np.concatenate(([0], np.cumsum(sizes)[:-1])).astype(np.int64)
        nodes = np.concatenate([t.nodes for t in trees])
        self.feat = nodes["feature_idx"].astype(np.int64)
        self.thr = nodes["num_threshold"].astype(np.float64)
        self.mleft = nodes["missing_go_to_left"].astype(np.bool_)
        self.left = nodes["left"].astype(np.int64)
        self.right = nodes["right"].astype(np.int64)
        self.leaf = nodes["is_leaf"].astype(np.bool_)
        self.val = nodes["value"].astype(np.float64)
        self.base = float(np.asarray(model._baseline_prediction).ravel()[0])
        self.n_trees = len(trees)
        self.predict_one(np.zeros(model.n_features_in_))  # compile now, not on the first live trigger

    def _args(self):
        return (self.feat, self.thr, self.mleft, self.left, self.right, self.leaf, self.val, self.starts, self.base)

    def predict_one(self, x: np.ndarray) -> float:
        return 1.0 / (1.0 + np.exp(-_raw_one(np.asarray(x, dtype=np.float64), *self._args())))

    def predict(self, X: np.ndarray) -> np.ndarray:
        return 1.0 / (1.0 + np.exp(-_raw_many(np.ascontiguousarray(X, dtype=np.float64), *self._args())))
