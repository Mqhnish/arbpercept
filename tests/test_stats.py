import json

import numpy as np
import pandas as pd

from arbtrade.stats import boot_ci, paired_diff


def test_interval_brackets_the_mean():
    x = np.random.default_rng(0).normal(5, 1, 200)
    lo, hi = boot_ci(x)
    assert lo < x.mean() < hi and hi - lo < 0.5


def test_paired_difference_counts_missing_days_as_zero():
    a = pd.Series({"d1": 10.0, "d2": 10.0})
    b = pd.Series({"d1": 4.0, "d3": 2.0})
    m, lo, hi = paired_diff(a, b)
    assert np.isclose(m, ((10 - 4) + (10 - 0) + (0 - 2)) / 3)
    m4, _, _ = paired_diff(a, b, days=["d1", "d2", "d3", "d4"])   # a fixed day list adds a $0 - $0 day
    assert np.isclose(m4, 14 / 4)


def test_paired_interval_is_tighter_than_separate_ones():
    rng = np.random.default_rng(1)
    day = rng.normal(0, 10, 50)                                   # shared day-to-day swings
    a = pd.Series(day + 1.0 + rng.normal(0, 0.5, 50))
    b = pd.Series(day + rng.normal(0, 0.5, 50))
    m, lo, hi = paired_diff(a, b)
    assert lo > 0                                                 # a beats b on the same days
    la, ha = boot_ci(a.to_numpy())
    lb, hb = boot_ci(b.to_numpy())
    assert la < hb                                                # while the separate intervals overlap


def test_validation_days_include_days_without_trades(tmp_path):
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "analysis"))
    from inventory_check import validation_days
    (tmp_path / "meta.json").write_text(json.dumps({"val_days": {"1.0": {"0": ["d1", "d2"], "1": ["d3"]}}}))
    tr = pd.DataFrame({"fee_bps_per_leg": [1.0], "date": ["d1"]})
    assert validation_days(tmp_path, tr, 1.0) == ["d1", "d2", "d3"]
    assert validation_days(tmp_path, tr, 2.5) == []                # no meta for this fee: days with trades only
