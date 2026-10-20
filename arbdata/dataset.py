"""The one way modelling code should read episodes: split-aware and holdout-guarded.

    from arbdata.dataset import load_episodes
    train = load_episodes(split="train", fold=0, hurdle="gross>2bps")
    val   = load_episodes(split="val",   fold=0, hurdle="gross>2bps")

Fit scalers, thresholds and hyperparameters on train, choose among them on val, and
open the holdout once at the very end.
"""

from __future__ import annotations

import json

import pandas as pd

from .config import Config, load_config
from .splits import dates_for


def load_episodes(split: str, fold: int | None = None, pairs: list[str] | None = None,
                  hurdle: str | None = None, drop_stale: bool = True,
                  drop_sub_resolution: bool = False, drop_stale_partner: bool = False,
                  cfg: Config | None = None) -> pd.DataFrame:
    """drop_sub_resolution=False keeps episodes shorter than the sampling step. Fit them with
    interval censoring on [lower_ms, upper_ms]; dropping them biases lifetimes upward.
    drop_stale_partner=True keeps only births where every sampled leg's quote was fresh:
    the cleanest labels, for a sensitivity check against the full set."""
    cfg = cfg or load_config()
    if not cfg.splits_path.exists():
        raise FileNotFoundError("no splits.json yet: run `arbdata splits` first")
    splits = json.loads(cfg.splits_path.read_text())
    wanted = set(dates_for(splits, split, fold))
    frames = []
    for pair in pairs or sorted(cfg.pairs):
        for path in sorted((cfg.data_root / "episodes" / pair).glob("*.parquet")):
            if path.stem in wanted:
                frames.append(pd.read_parquet(path))
    if not frames:
        return pd.DataFrame()
    df = pd.concat(frames, ignore_index=True)
    if hurdle is not None:
        df = df[df.hurdle_name == hurdle]
    if drop_stale:
        df = df[~df.stale_birth]
    if drop_sub_resolution:
        df = df[~df.sub_resolution]
    if drop_stale_partner:
        df = df[~df.stale_partner]
    return df.reset_index(drop=True)
