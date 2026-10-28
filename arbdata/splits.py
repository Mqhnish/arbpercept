"""Time-ordered splits with embargoes and a frozen, guarded holdout.

Why not a random split: episodes on the same day share a market regime, so a random
split puts near-copies of test rows in training and inflates every score. Splits here
are by calendar date, applied identically to every source, so a day seen at 100 ms
resolution in one dataset can never sit in training while its tick-level twin is tested.

The holdout is frozen as a calendar window the first time splits are made. Data added
later is assigned by date: older dates join development, dates inside the window join
the holdout, and dates after it are set aside. The window itself never moves.

A second, cross-venue window is frozen the same way. The main holdout holds Bybit archive
days only, so the Binance vs Bybit strategies could never be scored on it. February and
March 2024 (Binance's best-price archive ends on 30 March 2024) are set aside for them,
with one embargo day, before any of that data was downloaded. Those dates never join
development, and reading them needs the same unlock as the main holdout.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import math
import os
from pathlib import Path

import numpy as np

UNLOCK_ENV = "ARBDATA_UNLOCK_HOLDOUT"
CROSS_VENUE_WINDOW = {"embargo_start": "2024-02-01", "holdout_start": "2024-02-02", "holdout_end": "2024-03-31"}


def _sha(window: dict) -> str:
    return hashlib.sha256(json.dumps(window, sort_keys=True).encode()).hexdigest()[:16]


def _minus_days(date: str, days: int) -> str:
    return (dt.date.fromisoformat(date) - dt.timedelta(days=days)).isoformat()


def walk_forward_folds(dates: list[str], embargo_days: int, n_folds: int) -> list[dict]:
    """Folds over one pair's own development dates, so every fold has data for that pair."""
    return _folds(sorted(set(dates)), embargo_days, n_folds)


def _folds(development: list[str], embargo_days: int, n_folds: int) -> list[dict]:
    """Expanding-window walk-forward: validation blocks in time order, training strictly before."""
    folds = []
    chunks = [list(c) for c in np.array_split(np.array(development, dtype=object), n_folds + 1) if len(c)]
    for k in range(1, len(chunks)):
        val = chunks[k]
        cutoff = _minus_days(val[0], embargo_days)
        train = [d for d in development if d < cutoff]
        if train:
            folds.append({"train": train, "val": val})
    return folds


def _assign(dates: list[str], window: dict, embargo_days: int, n_folds: int, cross: dict | None = None) -> dict:
    dates = sorted(set(dates))
    in_cross = (lambda d: cross["embargo_start"] <= d <= cross["holdout_end"]) if cross else (lambda d: False)
    development = [d for d in dates if d < window["embargo_start"] and not in_cross(d)]
    return {
        "development": development,
        "embargo": [d for d in dates if window["embargo_start"] <= d < window["holdout_start"]
                    or (cross and cross["embargo_start"] <= d < cross["holdout_start"])],
        "holdout": [d for d in dates if window["holdout_start"] <= d <= window["holdout_end"]],
        "holdout_cross": [d for d in dates if cross and cross["holdout_start"] <= d <= cross["holdout_end"]],
        "arrived_after_freeze": [d for d in dates if d > window["holdout_end"]],
        "folds": _folds(development, embargo_days, n_folds),
    }


def make_splits(dates: list[str], holdout_fraction: float, min_holdout_days: int,
                embargo_days: int, n_folds: int) -> dict:
    dates = sorted(set(dates))
    n_hold = max(min_holdout_days, math.ceil(holdout_fraction * len(dates)))
    if n_hold >= len(dates):
        raise ValueError(f"only {len(dates)} dates: not enough for a {n_hold}-date holdout plus development data")
    holdout_start = dates[-n_hold]
    window = {"embargo_start": _minus_days(holdout_start, embargo_days),
              "holdout_start": holdout_start, "holdout_end": dates[-1]}
    params = {"holdout_fraction": holdout_fraction, "min_holdout_days": min_holdout_days,
              "embargo_days": embargo_days, "n_folds": n_folds}
    return {
        "created_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "params": params,
        "window": window,
        "holdout_sha": _sha(window),
        "cross_window": CROSS_VENUE_WINDOW,
        "cross_holdout_sha": _sha(CROSS_VENUE_WINDOW),
        **_assign(dates, window, embargo_days, n_folds, CROSS_VENUE_WINDOW),
    }


def _all_dates(s: dict) -> set[str]:
    return (set(s["development"]) | set(s["embargo"]) | set(s["holdout"]) | set(s.get("holdout_cross", []))
            | set(s.get("arrived_after_freeze", [])))


def save_frozen(proposed: dict, path: Path, force: bool = False) -> dict:
    """Write splits once. An existing holdout window is never moved unless force=True. A splits
    file made before the cross-venue window existed gets it once, the first time it is saved."""
    if path.exists() and not force:
        existing = json.loads(path.read_text())
        p = existing["params"]
        if "cross_window" not in existing:
            existing["cross_window"] = CROSS_VENUE_WINDOW
            existing["cross_holdout_sha"] = _sha(CROSS_VENUE_WINDOW)
        existing.update(_assign(sorted(_all_dates(existing) | _all_dates(proposed)), existing["window"],
                                p["embargo_days"], p["n_folds"], existing["cross_window"]))
        path.write_text(json.dumps(existing, indent=1))
        return existing
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(proposed, indent=1))
    return proposed


def dates_for(splits: dict, split: str, fold: int | None = None) -> list[str]:
    if split in ("holdout", "holdout_cross"):
        if os.environ.get(UNLOCK_ENV) != "1":
            raise PermissionError(
                f"The {split} set is locked. Evaluate on it once, at the very end, by setting "
                f"{UNLOCK_ENV}=1. Never tune thresholds, features or models after looking."
            )
        return splits.get(split, [])
    if split == "development":
        return splits["development"]
    if split in ("train", "val"):
        if fold is None:
            raise ValueError("train/val need a fold number")
        return splits["folds"][fold][split]
    raise ValueError(f"unknown split {split}")
