"""Day-bootstrap intervals shared by the analysis scripts.

Days are the resampling unit, since trades within a day are not independent. Intervals are
percentile 95% intervals over 10,000 draws. A comparison between two strategies resamples the
same days for both (paired), which is much tighter than comparing two separate intervals.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def boot_ci(x: np.ndarray, reps: int = 10_000, seed: int = 0) -> tuple[float, float]:
    """95% interval of the mean of x (one value per day)."""
    x = np.asarray(x, float)
    if len(x) == 0:
        return float("nan"), float("nan")
    rng = np.random.default_rng(seed)
    means = x[rng.integers(0, len(x), (reps, len(x)))].mean(1)
    return float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))


def paired_diff(a: pd.Series, b: pd.Series, days: list | None = None, reps: int = 10_000,
                seed: int = 0) -> tuple[float, float, float]:
    """Mean of a - b per day with its 95% interval. a and b are indexed by day; a day missing from
    either side counts as $0 there (no trade that day). days fixes the set of days compared."""
    idx = pd.Index(days) if days is not None else a.index.union(b.index)
    d = (a.reindex(idx, fill_value=0.0) - b.reindex(idx, fill_value=0.0)).to_numpy(float)
    lo, hi = boot_ci(d, reps, seed)
    return float(d.mean()) if len(d) else float("nan"), lo, hi
