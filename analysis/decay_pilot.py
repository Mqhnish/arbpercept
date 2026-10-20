"""Pilot decay models: can we predict whether an opportunity survives a latency budget?

For each pair, hurdle and latency budget tau, every model predicts P(lifetime > tau)
from features known at the birth. Development data only, walk-forward folds built from
the pair's own dates, fixed hyperparameters (nothing tuned), holdout never opened.

Labels respect sampling resolution: an episode is "alive at tau" only if its lifetime
lower bound clears tau and "dead" only if its upper bound is below tau. Episodes whose
interval straddles tau are undecidable from this data and are excluded (share reported).

Run:  .venv/bin/python analysis/decay_pilot.py [--pairs bybit_btc_basis ...]
"""

from __future__ import annotations

import argparse
import json
import time

import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.impute import SimpleImputer
from sklearn.inspection import permutation_importance
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import brier_score_loss, log_loss, roc_auc_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from arbdata.config import load_config
from arbdata.dataset import load_episodes
from arbdata.splits import walk_forward_folds

TAUS_MS = [250, 500, 1000, 2000]
HURDLES = ["gross>1bps", "gross>2bps", "gross>5bps"]
MIN_CLASS = 30  # a fold needs this many of each class in train and validation to be scored
SEED = 0


def labels_at(ep: pd.DataFrame, tau: float) -> pd.Series:
    """1 = surely alive at tau, 0 = surely dead, NaN = interval straddles tau."""
    alive = ep.lower_ms >= tau
    dead = ep.upper_ms < tau
    return pd.Series(np.where(alive, 1.0, np.where(dead, 0.0, np.nan)), index=ep.index)


def feature_columns(df: pd.DataFrame) -> list[str]:
    """Every causal feature with data: the same set the trading system's slow model uses."""
    from arbtrade.policies import slow_features
    return slow_features(df)


def models(features: list[str]) -> dict:
    return {
        "gap size only (logistic)": (["edge_birth_bps"], make_pipeline(
            SimpleImputer(strategy="median"), StandardScaler(), LogisticRegression(max_iter=1000))),
        "all features (logistic)": (features, make_pipeline(
            SimpleImputer(strategy="median"), StandardScaler(), LogisticRegression(max_iter=2000, C=1.0))),
        "all features (gradient boosting)": (features, HistGradientBoostingClassifier(
            max_iter=300, learning_rate=0.05, max_leaf_nodes=31, min_samples_leaf=100,
            l2_regularization=1.0, early_stopping=False, random_state=SEED)),
    }


def ece(y: np.ndarray, p: np.ndarray, bins: int = 10) -> float:
    """Expected calibration error over equal-count bins."""
    order = np.argsort(p)
    err = 0.0
    for chunk in np.array_split(order, bins):
        if len(chunk):
            err += len(chunk) * abs(y[chunk].mean() - p[chunk].mean())
    return err / len(y)


def evaluate(df: pd.DataFrame, folds: list[dict], tau: float) -> list[dict]:
    y_all = labels_at(df, tau)
    rows = []
    feats = feature_columns(df)
    for k, fold in enumerate(folds):
        tr = df[df.date.isin(fold["train"]) & y_all.notna()]
        va = df[df.date.isin(fold["val"]) & y_all.notna()]
        ytr, yva = y_all[tr.index].to_numpy(), y_all[va.index].to_numpy()
        if min(ytr.sum(), len(ytr) - ytr.sum(), yva.sum(), len(yva) - yva.sum()) < MIN_CLASS:
            continue
        base = ytr.mean()
        b_base = brier_score_loss(yva, np.full(len(yva), base))
        rows.append({"fold": k, "model": "survival rate only (Kaplan-Meier style)", "n_train": len(ytr),
                     "n_val": len(yva), "val_alive_share": yva.mean(), "auc": 0.5, "brier": b_base,
                     "bss": 0.0, "log_loss": log_loss(yva, np.full(len(yva), base)), "ece": abs(yva.mean() - base),
                     "auc_fresh": 0.5})
        fresh = ~va.stale_partner.to_numpy()
        # Calibrated boosting: fit on the first 70% of training days, isotonic map on the rest.
        tr_days = sorted(tr.date.unique())
        cut = max(1, int(len(tr_days) * 0.7))
        fit_m, cal_m = tr.date.isin(tr_days[:cut]).to_numpy(), tr.date.isin(tr_days[cut:]).to_numpy()
        if cal_m.any() and 0 < ytr[cal_m].sum() < cal_m.sum() and 0 < ytr[fit_m].sum() < fit_m.sum():
            from sklearn.isotonic import IsotonicRegression
            gb = models(feats)["all features (gradient boosting)"][1].fit(tr[feats][fit_m], ytr[fit_m])
            iso = IsotonicRegression(y_min=0, y_max=1, out_of_bounds="clip").fit(gb.predict_proba(tr[feats][cal_m])[:, 1], ytr[cal_m])
            p = np.clip(iso.predict(gb.predict_proba(va[feats])[:, 1]), 1e-6, 1 - 1e-6)
            yf = yva[fresh]
            rows.append({
                "fold": k, "model": "all features (gradient boosting, calibrated)", "n_train": len(ytr), "n_val": len(yva),
                "val_alive_share": yva.mean(), "auc": roc_auc_score(yva, p), "brier": brier_score_loss(yva, p),
                "bss": 1 - brier_score_loss(yva, p) / b_base, "log_loss": log_loss(yva, p), "ece": ece(yva, p),
                "auc_fresh": roc_auc_score(yf, p[fresh]) if 0 < yf.sum() < len(yf) else np.nan,
            })
        for name, (cols, model) in models(feats).items():
            model.fit(tr[cols], ytr)
            p = np.clip(model.predict_proba(va[cols])[:, 1], 1e-6, 1 - 1e-6)
            yf = yva[fresh]
            rows.append({
                "fold": k, "model": name, "n_train": len(ytr), "n_val": len(yva), "val_alive_share": yva.mean(),
                "auc": roc_auc_score(yva, p), "brier": brier_score_loss(yva, p),
                "bss": 1 - brier_score_loss(yva, p) / b_base, "log_loss": log_loss(yva, p), "ece": ece(yva, p),
                "auc_fresh": roc_auc_score(yf, p[fresh]) if 0 < yf.sum() < len(yf) else np.nan,
            })
    return rows


def regime_auc(df: pd.DataFrame, folds: list[dict], tau: float, rv: dict[str, float]) -> list[dict]:
    """Out-of-fold predictions of the boosted model, scored separately on calm, normal and
    volatile validation days (terciles of daily realised volatility)."""
    y_all = labels_at(df, tau)
    feats = feature_columns(df)
    parts = []
    for fold in folds:
        tr = df[df.date.isin(fold["train"]) & y_all.notna()]
        va = df[df.date.isin(fold["val"]) & y_all.notna()]
        ytr = y_all[tr.index].to_numpy()
        if min(ytr.sum(), len(ytr) - ytr.sum()) < MIN_CLASS or va.empty:
            continue
        model = models(feats)["all features (gradient boosting)"][1].fit(tr[feats], ytr)
        parts.append(pd.DataFrame({"date": va.date.to_numpy(), "y": y_all[va.index].to_numpy(),
                                   "p": model.predict_proba(va[feats])[:, 1]}))
    if not parts:
        return []
    oof = pd.concat(parts)
    days = sorted(oof.date.unique())
    vols = pd.Series({d: rv.get(d, np.nan) for d in days}).dropna()
    if len(vols) < 6:
        return []
    bucket = pd.qcut(vols, 3, labels=["calm", "normal", "volatile"])
    oof["regime"] = oof.date.map(bucket)
    out = []
    for name, g in oof.groupby("regime", observed=True):
        if 0 < g.y.sum() < len(g):
            out.append({"regime": str(name), "days": int(g.date.nunique()), "n": int(len(g)),
                        "rv_bps_range": [float(vols[bucket == name].min()), float(vols[bucket == name].max())],
                        "auc": float(roc_auc_score(g.y, g.p)), "alive_share": float(g.y.mean())})
    return out


def importance(df: pd.DataFrame, folds: list[dict], tau: float, top: int = 10) -> list[tuple[str, float]]:
    """Permutation importance of the boosted model on the last fold's validation days."""
    y_all = labels_at(df, tau)
    fold = folds[-1]
    tr = df[df.date.isin(fold["train"]) & y_all.notna()]
    va = df[df.date.isin(fold["val"]) & y_all.notna()]
    feats = feature_columns(df)
    model = models(feats)["all features (gradient boosting)"][1].fit(tr[feats], y_all[tr.index])
    va = va.sample(min(len(va), 20_000), random_state=SEED)
    r = permutation_importance(model, va[feats], y_all[va.index], scoring="roc_auc", n_repeats=5, random_state=SEED)
    order = np.argsort(-r.importances_mean)[:top]
    return [(feats[i], float(r.importances_mean[i])) for i in order]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pairs", nargs="*", default=None)
    ap.add_argument("--taus", nargs="*", type=int, default=TAUS_MS)
    ap.add_argument("--hurdles", nargs="*", default=HURDLES)
    ap.add_argument("--tag", default="", help="suffix for the output files")
    args = ap.parse_args()
    cfg = load_config()
    splits = json.loads(cfg.splits_path.read_text())
    out_dir = cfg.reports_dir / "decay"
    out_dir.mkdir(parents=True, exist_ok=True)

    pairs = args.pairs or [p for p in cfg.pairs if (cfg.data_root / "episodes" / p).exists()]
    all_rows, summary = [], {}
    for pair in pairs:
        dev = load_episodes(split="development", pairs=[pair], cfg=cfg)  # stale births dropped by default
        if dev.empty:
            continue
        folds = walk_forward_folds(sorted(dev.date.unique()), splits["params"]["embargo_days"], splits["params"]["n_folds"])
        if not folds:
            print(f"{pair}: too few development days for walk-forward folds")
            continue
        for births in ("all", "clean"):
            # clean = births where every sampled leg's quote was fresh: the labels the archive can be trusted on
            base = dev if births == "all" else dev[~dev.stale_partner]
            for hurdle in args.hurdles:
                df = base[base.hurdle_name == hurdle].reset_index(drop=True)
                if len(df) < 500:
                    continue
                for tau in args.taus:
                    t0 = time.time()
                    undecidable = labels_at(df, tau).isna().mean()
                    rows = evaluate(df, folds, tau)
                    for r in rows:
                        r.update({"pair": pair, "births": births, "hurdle": hurdle, "tau_ms": tau,
                                  "undecidable_share": undecidable})
                    all_rows += rows
                    print(f"{pair} [{births}] {hurdle} tau={tau}ms: {len(df):,} episodes, {undecidable:.0%} undecidable, "
                          f"{len({r['fold'] for r in rows})} scored folds ({time.time() - t0:.0f}s)", flush=True)
        perp_leg = cfg.pairs[pair].b
        qdir = cfg.reports_dir / "quality" / perp_leg
        rv = {q.stem: json.loads(q.read_text())["daily_rv_bps"] for q in qdir.glob("*.json")}
        fresh1 = dev[(dev.hurdle_name == "gross>1bps") & ~dev.stale_partner].reset_index(drop=True)
        if len(fresh1) >= 500:
            summary[f"{pair}|fresh gross>1bps|500|by regime"] = regime_auc(fresh1, folds, 500, rv)
        key = f"{pair}|gross>2bps|500"
        d2 = dev[dev.hurdle_name == "gross>2bps"].reset_index(drop=True)
        if len(d2) >= 500:
            summary[key] = importance(d2, folds, 500)
        summary[f"{pair}|folds"] = [{"train_days": len(f["train"]), "val": [f["val"][0], f["val"][-1]]} for f in folds]

    res = pd.DataFrame(all_rows)
    res.to_csv(out_dir / f"fold_results{args.tag}.csv", index=False)
    (out_dir / f"importance{args.tag}.json").write_text(json.dumps(summary, indent=1))
    agg = (res.groupby(["pair", "births", "hurdle", "tau_ms", "model"])
           .agg(folds=("fold", "nunique"), n_val=("n_val", "sum"), alive=("val_alive_share", "mean"),
                undecidable=("undecidable_share", "first"), auc=("auc", "mean"), auc_sd=("auc", "std"),
                bss=("bss", "mean"), bss_sd=("bss", "std"), ece=("ece", "mean"), auc_fresh=("auc_fresh", "mean"))
           .reset_index())
    agg.to_csv(out_dir / f"summary{args.tag}.csv", index=False)
    print(agg.round(3).to_string())


if __name__ == "__main__":
    main()
