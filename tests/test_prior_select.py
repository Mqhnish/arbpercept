"""Picking the saved decay prior that fits a run: the same asset and the same gap definition."""

import json
import os
import time

from arbtrade.live import find_prior, prior_file, prior_is_for

BASE = {"features": ["edge_birth_bps"], "median": [0.0], "mu": [0.0], "sd": [1.0], "w": [1.0], "b": 0.0,
        "loss_bps": -1.0}


def _save(folder, name, **kw):
    p = folder / name
    p.write_text(json.dumps({**BASE, **kw}))
    return p


def test_prior_is_for_reads_the_asset_field_or_older_trained_on_text():
    assert prior_is_for({"asset": "eth"}, "ETH") and not prior_is_for({"asset": "BTC"}, "ETH")
    assert prior_is_for({"trained_on": "btc_perp_binance_bybit, 336,478 triggers"}, "BTC")
    assert prior_is_for({"trained_on": "live ETH perpetual Binance vs Bybit, 3,166 triggers"}, "ETH")
    assert not prior_is_for({"trained_on": "live ETH perpetual"}, "BTC")
    assert not prior_is_for({"trained_on": "arb_perp_binance_bybit"}, "AR")


def test_prior_file_names_the_gap_definition():
    assert prior_file("btc", 300.0) == "prior_BTC_offset300s.json"
    assert prior_file("ETH", None) == "prior_ETH_raw.json"


def test_find_prior_picks_the_matching_asset_and_gaps(tmp_path):
    raw = _save(tmp_path, "prior.json", trained_on="btc_perp_binance_bybit, 10 triggers")
    _save(tmp_path, "prior_live_ETH.json", trained_on="live ETH perpetual, 5 triggers")
    path, note = find_prior(tmp_path, "BTC", None)
    assert path == raw and "prior.json" in note
    off = _save(tmp_path, prior_file("BTC", 300.0), asset="BTC", offset_window_s=300.0, trained_on="btc")
    path, _ = find_prior(tmp_path, "BTC", 300.0)
    assert path == off
    path, _ = find_prior(tmp_path, "ETH", None)
    assert path.name == "prior_live_ETH.json"


def test_find_prior_newest_first_and_says_why_nothing_fits(tmp_path):
    old = _save(tmp_path, "prior_a.json", asset="BTC", offset_window_s=300.0)
    new = _save(tmp_path, "prior_b.json", asset="BTC", offset_window_s=300.0)
    t = time.time()
    os.utime(old, (t - 100, t - 100))
    os.utime(new, (t, t))
    assert find_prior(tmp_path, "BTC", 300.0)[0] == new
    path, note = find_prior(tmp_path, "BTC", 60.0)
    assert path is None and "300 s offset" in note and "--train-prior --asset BTC --offset-window-s 60" in note
    path, note = find_prior(tmp_path, "SOL", 300.0)
    assert path is None and "No saved SOL prior" in note
    assert find_prior(tmp_path / "missing", "BTC", None)[0] is None
