import datetime as dt
import json

import pytest

from arbdata.splits import UNLOCK_ENV, dates_for, make_splits, save_frozen


def _dates(n, start="2026-01-01"):
    d0 = dt.date.fromisoformat(start)
    return [(d0 + dt.timedelta(days=i)).isoformat() for i in range(n)]


def test_holdout_is_most_recent_and_embargoed():
    s = make_splits(_dates(60), 0.2, 7, 1, 4)
    assert s["holdout"] == _dates(60)[-12:]
    assert s["embargo"] == [_dates(60)[-13]]
    assert max(s["development"]) < min(s["embargo"]) < min(s["holdout"])
    for f in s["folds"]:
        assert max(f["train"]) < min(f["val"])
        gap = dt.date.fromisoformat(min(f["val"])) - dt.date.fromisoformat(max(f["train"]))
        assert gap.days >= 2  # one embargo day between them
        assert not set(f["train"]) & set(s["holdout"])
        assert not set(f["val"]) & set(s["holdout"])


def test_holdout_is_locked(monkeypatch):
    s = make_splits(_dates(30), 0.2, 7, 1, 3)
    monkeypatch.delenv(UNLOCK_ENV, raising=False)
    with pytest.raises(PermissionError):
        dates_for(s, "holdout")
    monkeypatch.setenv(UNLOCK_ENV, "1")
    assert dates_for(s, "holdout") == s["holdout"]


def test_frozen_holdout_does_not_move(tmp_path):
    path = tmp_path / "splits.json"
    first = save_frozen(make_splits(_dates(30), 0.2, 7, 1, 3), path)
    later = save_frozen(make_splits(_dates(40), 0.2, 7, 1, 3), path)
    assert later["holdout"] == first["holdout"]
    assert later["arrived_after_freeze"] == _dates(40)[30:]
    assert json.loads(path.read_text())["holdout_sha"] == first["holdout_sha"]


def test_too_few_dates():
    with pytest.raises(ValueError):
        make_splits(_dates(5), 0.2, 7, 1, 3)


def test_older_data_added_later_joins_development(tmp_path):
    path = tmp_path / "splits.json"
    first = save_frozen(make_splits(_dates(30, "2026-03-01"), 0.2, 7, 1, 3), path)
    older = _dates(20, "2026-01-01")
    later = save_frozen(make_splits(older + _dates(30, "2026-03-01"), 0.2, 7, 1, 3), path)
    assert later["window"] == first["window"] and later["holdout"] == first["holdout"]
    assert set(older) <= set(later["development"])
    assert later["arrived_after_freeze"] == []
    assert later["folds"][0]["train"][0] == "2026-01-01"


def test_cross_venue_window_is_locked_and_kept_out_of_development(tmp_path, monkeypatch):
    from arbdata.splits import CROSS_VENUE_WINDOW
    dates = ["2024-01-30", "2024-01-31", "2024-02-01", "2024-02-02", "2024-03-15", "2024-03-31", "2024-04-01",
             "2026-09-01", "2026-09-02", "2026-09-03", "2026-09-04", "2026-09-05", "2026-09-06", "2026-09-07",
             "2026-09-08", "2026-09-09", "2026-09-10"]
    s = save_frozen(make_splits(dates, 0.2, 7, 1, 3), tmp_path / "splits.json")
    assert s["cross_window"] == CROSS_VENUE_WINDOW
    assert s["holdout_cross"] == ["2024-02-02", "2024-03-15", "2024-03-31"]
    assert "2024-02-01" in s["embargo"]
    assert not set(s["holdout_cross"]) & set(s["development"]) and "2024-01-31" in s["development"]
    assert "2024-04-01" in s["development"]
    monkeypatch.delenv(UNLOCK_ENV, raising=False)
    with pytest.raises(PermissionError):
        dates_for(s, "holdout_cross")
    monkeypatch.setenv(UNLOCK_ENV, "1")
    assert dates_for(s, "holdout_cross") == s["holdout_cross"]


def test_an_older_splits_file_gets_the_cross_window_once(tmp_path):
    import json
    path = tmp_path / "splits.json"
    old = make_splits(_dates(30), 0.2, 7, 1, 3)
    for k in ("cross_window", "cross_holdout_sha", "holdout_cross"):
        old.pop(k)
    path.write_text(json.dumps(old))
    s = save_frozen(make_splits(_dates(30) + ["2024-02-10"], 0.2, 7, 1, 3), path)
    assert s["holdout_cross"] == ["2024-02-10"] and "2024-02-10" not in s["development"]
