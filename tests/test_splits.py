import datetime as dt
import json

import pytest

from arbdata.splits import CROSS_UNLOCK_ENV, UNLOCK_ENV, cross_window, dates_for, make_splits, save_frozen


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


CROSS = {"embargo_start": "2026-01-10", "holdout_start": "2026-01-11", "holdout_end": "2026-01-20"}


def test_cross_venue_holdout_never_joins_development(monkeypatch):
    s = make_splits(_dates(90), 0.2, 7, 1, 3, cross=CROSS)
    assert s["cross_window"] == CROSS
    assert s["cross_embargo"] == ["2026-01-10"] and s["cross_holdout"] == _dates(10, "2026-01-11")
    assert not set(s["development"]) & set(s["cross_holdout"] + s["cross_embargo"])
    assert not {d for f in s["folds"] for d in f["train"] + f["val"]} & set(s["cross_holdout"])
    monkeypatch.delenv(CROSS_UNLOCK_ENV, raising=False)
    monkeypatch.setenv(UNLOCK_ENV, "1")  # opening the main holdout does not open this one
    with pytest.raises(PermissionError):
        dates_for(s, "cross_holdout")
    monkeypatch.setenv(CROSS_UNLOCK_ENV, "1")
    assert dates_for(s, "cross_holdout") == s["cross_holdout"]


def test_cross_dates_downloaded_later_go_to_the_cross_holdout(tmp_path):
    # Splits frozen before the window had data; its dates arrive later and are older than the main holdout.
    path = tmp_path / "splits.json"
    first = save_frozen(make_splits(_dates(40, "2026-02-01"), 0.2, 7, 1, 3, cross=CROSS), path)
    later = save_frozen(make_splits(_dates(31, "2026-01-01") + _dates(40, "2026-02-01"), 0.2, 7, 1, 3, cross=CROSS), path)
    assert later["window"] == first["window"] and later["holdout"] == first["holdout"]
    assert later["cross_holdout"] == _dates(10, "2026-01-11")
    assert set(_dates(9, "2026-01-01")) <= set(later["development"])
    assert not set(later["development"]) & set(_dates(11, "2026-01-10"))


def test_the_committed_cross_window_is_the_frozen_one():
    w = cross_window()
    assert w == {"embargo_start": "2024-02-01", "holdout_start": "2024-02-02", "holdout_end": "2024-03-31"}
