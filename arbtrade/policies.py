"""Decision policies: which fast-path triggers to trade, and whether to wait for the slow model.

q(tau | x) = P(both legs still fill in full after tau), learned from replayed outcomes on
training days. Expected value of acting with total delay tau, in bps of notional:
    EV(tau) = q * (edge - fees) + (1 - q) * L(tau)
where L(tau) is the average outcome when the trade does not fully fill (zero for no fill,
negative for leg-risk unwinds), estimated on training days. The fast path uses one average;
the slow path predicts L per trigger (MissCost). This is the abstract's
S = e*q - (1-q)*pi*l - c with pi*l folded into one measured term.
"""

from __future__ import annotations

import time

import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression

FAST_FEATURES = ["edge_birth_bps", "f_a_spread_bps", "f_b_spread_bps", "f_a_age_ms", "f_b_age_ms", "f_rv_1s_bps"]
GAP_ONLY_FEATURES = ["edge_birth_bps"]  # the gap-size-only baseline every model must beat


def slow_features(df: pd.DataFrame) -> list[str]:
    cols = [c for c in df.columns if c.startswith("f_")] + ["edge_birth_bps"]
    return [c for c in cols if df[c].notna().any()]


class FastPrior:
    """A six-feature logistic model evaluated as one dot product: microseconds per decision.
    With features=GAP_ONLY_FEATURES it is the gap-size-only baseline."""

    def __init__(self, features: list[str] | None = None):
        self.features = list(features or FAST_FEATURES)

    def fit(self, X: pd.DataFrame, y: np.ndarray) -> "FastPrior":
        X = X[self.features]
        self.median = X.median().to_numpy()
        Z = np.where(np.isnan(X.to_numpy()), self.median, X.to_numpy())
        self.mu, self.sd = Z.mean(0), Z.std(0) + 1e-9
        y = np.asarray(y).astype(int)
        if y.min() == y.max():  # one outcome only: predict it with certainty (logit +-10)
            self.w, self.b = np.zeros(len(self.features)), 10.0 if y[0] else -10.0
            return self
        lr = LogisticRegression(max_iter=2000).fit((Z - self.mu) / self.sd, y)
        self.w, self.b = lr.coef_[0], lr.intercept_[0]
        return self

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        Z = X[self.features].to_numpy()
        Z = np.where(np.isnan(Z), self.median, Z)
        return 1 / (1 + np.exp(-(((Z - self.mu) / self.sd) @ self.w + self.b)))


class SlowModel:
    """Gradient boosting on every causal feature: better, but milliseconds per decision."""

    def fit(self, X: pd.DataFrame, y: np.ndarray) -> "SlowModel":
        self.cols = slow_features(X)
        y = np.asarray(y).astype(int)
        if y.min() == y.max():
            from sklearn.dummy import DummyClassifier
            self.model = DummyClassifier(strategy="constant", constant=y[0]).fit(X[self.cols], y)
            self.model.predict_proba = lambda Z, c=float(y[0]): np.column_stack([np.full(len(Z), 1 - c), np.full(len(Z), c)])
            return self
        self.model = HistGradientBoostingClassifier(max_iter=200, learning_rate=0.05, max_leaf_nodes=31,
                                                    min_samples_leaf=100, l2_regularization=1.0,
                                                    early_stopping=False, random_state=0).fit(X[self.cols], y)
        from .compiled import CompiledTrees
        self.compiled = CompiledTrees(self.model)  # identical outputs, microseconds per trigger
        return self

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        return self.model.predict_proba(X[self.cols])[:, 1]


class MissCost:
    """What a trade costs when it does not fully fill, predicted per trigger (bps of its notional).

    A miss is either no fill at all, which costs nothing, or one leg (or part of one) filled and
    unwound across the spread. Which of the two is likely, and how far the price runs before the
    unwind, depends on the trigger, so one average over all misses overcharges the harmless ones.
    Boosted trees of the same number and size as SlowModel, fitted on training-day misses only.
    """

    def fit(self, X: pd.DataFrame, pnl_bps: np.ndarray) -> "MissCost":
        from sklearn.ensemble import HistGradientBoostingRegressor
        self.cols = slow_features(X)
        self.model = HistGradientBoostingRegressor(max_iter=200, learning_rate=0.05, max_leaf_nodes=31,
                                                   min_samples_leaf=100, l2_regularization=1.0,
                                                   early_stopping=False, random_state=0)
        self.model.fit(X[self.cols], np.asarray(pnl_bps, float))
        from .compiled import CompiledTrees
        self.compiled = CompiledTrees(self.model)  # raw_one(x) gives the same number as predict
        return self

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        return self.model.predict(X[self.cols])


class Calibrator:
    """Isotonic map from predicted to observed fill rates, fitted on calibration days.

    The expected-value rule multiplies these probabilities by gains and losses, so a model
    that ranks well but says 70% when the truth is 40% makes wrong trade decisions.
    """

    def fit(self, p: np.ndarray, y: np.ndarray) -> "Calibrator":
        from sklearn.isotonic import IsotonicRegression
        y = np.asarray(y).astype(float)
        self.iso = None
        if 0 < y.sum() < len(y):
            self.iso = IsotonicRegression(y_min=0.0, y_max=1.0, out_of_bounds="clip").fit(p, y)
        return self

    def transform(self, p: np.ndarray) -> np.ndarray:
        return p if self.iso is None else self.iso.predict(p)

    def to_arrays(self) -> tuple[list[float], list[float]] | None:
        """The fitted map as (x, y) points: np.interp(p, x, y) gives the same answer as transform."""
        if self.iso is None:
            return None
        return self.iso.X_thresholds_.tolist(), self.iso.y_thresholds_.tolist()


def q_quality(y: np.ndarray, p: np.ndarray) -> dict:
    """How well predicted fill probabilities p match outcomes y: AUC (ranking), Brier score, and
    Brier skill against always predicting y's own fill rate (0 = no better, 1 = perfect)."""
    from sklearn.metrics import roc_auc_score
    y, p = np.asarray(y).astype(float), np.asarray(p, float)
    if not len(y):
        return {"n": 0, "fill_rate": np.nan, "auc": np.nan, "brier": np.nan, "brier_skill": np.nan}
    base = float(y.mean())
    brier, ref = float(np.mean((p - y) ** 2)), base * (1 - base)
    return {"n": int(len(y)), "fill_rate": base, "auc": float(roc_auc_score(y, p)) if 0 < base < 1 else np.nan,
            "brier": brier, "brier_skill": 1 - brier / ref if ref > 0 else np.nan}


def single_decision_latency_ms(model, X: pd.DataFrame, repeats: int = 300) -> float:
    """Median wall time to score one trigger, as a live system would."""
    rows = [X.iloc[[i % len(X)]] for i in range(repeats)]
    times = []
    for r in rows:
        t0 = time.perf_counter()
        model.predict(r)
        times.append(time.perf_counter() - t0)
    return float(np.median(times) * 1e3)


def expected_value_bps(q: np.ndarray, edge_bps: np.ndarray, fee_bps_total: float, loss_bps: float) -> np.ndarray:
    return q * (edge_bps - fee_bps_total) + (1 - q) * loss_bps


def expected_value_gain(q: np.ndarray, edge_bps: np.ndarray, gain: tuple[float, float], loss_bps: float) -> np.ndarray:
    """EV with the payoff of a full fill given as a line in the edge: a + b * edge (bps)."""
    a, b = gain
    return q * (a + b * edge_bps) + (1 - q) * loss_bps


def fit_gain(edge_bps: np.ndarray, outcomes: pd.DataFrame, min_n: int = 30) -> tuple[float, float]:
    """Least-squares line of realised P&L (bps) on the birth edge, over fully filled trades.

    Used where a fill does not lock in the edge (convergence trades), so the payoff has to
    be learned. Falls back to the mean outcome when there are too few fills.
    """
    m = outcomes.full_fill.to_numpy()
    y = outcomes.pnl_bps.to_numpy()[m]
    x = np.asarray(edge_bps)[m]
    if m.sum() < min_n:
        return (float(y.mean()) if len(y) else 0.0, 0.0)
    b, a = np.polyfit(x, y, 1)
    return float(a), float(b)


def miss_loss_bps(outcomes: pd.DataFrame, col: str = "pnl_bps") -> float:
    """Average P&L (bps) of trades that did not fully fill: the leg-risk term.
    col="pnl_rel_bps" scores them net of the venues' usual offset (see evaluate.replay_day)."""
    miss = outcomes[~outcomes.full_fill]
    return float(miss[col].mean()) if len(miss) else 0.0


def choose_margins(ev_fast: np.ndarray, pnl_now: np.ndarray, pnl_slow_if_taken: np.ndarray,
                   slow_trade: np.ndarray) -> tuple[float, float]:
    """Pick the cascade's (skip below, act above) margins on calibration days by realised P&L.

    pnl_now: outcome if acted on immediately; pnl_slow_if_taken: outcome if the slow model is
    consulted (zero where it declines, per slow_trade). Grid over quantiles of ev_fast.
    """
    qs = np.unique(np.quantile(ev_fast, np.linspace(0, 1, 21)))
    best, best_pnl = (qs[0], qs[-1]), -np.inf
    for lo in qs:
        for hi in qs[qs >= lo]:
            act = ev_fast > hi
            ask = (ev_fast >= lo) & ~act
            pnl = pnl_now[act].sum() + np.where(slow_trade, pnl_slow_if_taken, 0.0)[ask].sum()
            if pnl > best_pnl:
                best, best_pnl = (float(lo), float(hi)), pnl
    return best
