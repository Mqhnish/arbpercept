"""End to end: arbtrade.evaluate.run on synthetic days (no data files needed).

load_config and load_day are replaced by small stand-ins, so this checks the walk-forward
loop itself: offset-aware re-checks, per-venue latency and fees, the gap-size baseline,
validation days without triggers counted as $0, and the trade dump the inventory check reads.
"""

import json
from types import SimpleNamespace

import numpy as np
import pandas as pd

import arbtrade.evaluate as ev
from arbtrade.policies import FAST_FEATURES
from arbtrade.replay import Leg

PAIR = "synthetic_cross"
DATES = [f"2024-01-{d:02d}" for d in range(1, 15)]
QUIET, BROKEN = "2024-01-13", "2024-01-05"   # a day without triggers, and one that fails quality
DAY_US = 86_400_000_000


def _day(date: str, seed: int):
    rng = np.random.default_rng(seed)
    start = int(pd.Timestamp(date, tz="UTC").value // 1000)
    n = 20_000
    t = start + np.sort(rng.integers(0, DAY_US, n)).astype(np.int64)
    walk = 40_000 * np.exp(np.cumsum(rng.normal(0, 2e-5, n)))
    mk = lambda mid: Leg(t, mid - 0.05, mid + 0.05, np.full(n, 1.0), np.full(n, 1.0), False)
    jitter = rng.normal(0, 3e-4, n)  # each venue wobbles around the common price: gaps open and close
    a, b = mk(walk * (1 - 3e-4 + jitter)), mk(walk * (1 - rng.normal(0, 3e-4, n)))
    k = np.sort(rng.choice(np.arange(100, n - 100), 300, replace=False))
    eps = pd.DataFrame({"birth_ts": t[k], "date": date,
                        "direction": np.where(rng.random(300) < 0.5, "sell_a_buy_b", "sell_b_buy_a")})
    for f in FAST_FEATURES:
        eps[f] = rng.normal(0, 1, 300)
    eps["edge_birth_bps"] = eps["edge_rel_bps"] = 2.5 + rng.exponential(1.0, 300)
    eps["f_kalman_z"] = rng.normal(0, 1, 300)
    legs = {"a": a, "b": b, "offset": (t, np.full(n, -3.0))}
    return eps, legs


def _setup(monkeypatch, tmp_path):
    (tmp_path / "episodes" / PAIR).mkdir(parents=True)
    for d in DATES:
        (tmp_path / "episodes" / PAIR / f"{d}.parquet").touch()
    (tmp_path / "splits.json").write_text(json.dumps({"development": DATES,
                                                      "params": {"embargo_days": 1, "n_folds": 2}}))
    cfg = SimpleNamespace(splits_path=tmp_path / "splits.json", data_root=tmp_path,
                          pairs={PAIR: SimpleNamespace(type="cross")})
    monkeypatch.setattr(ev, "load_config", lambda: cfg)
    seen = []

    def fake_load_day(cfg, pair, date, trigger, offset_window_s=None):
        seen.append(offset_window_s)
        if date == BROKEN:
            return None
        if date == QUIET:
            return pd.DataFrame(), None
        eps, legs = _day(date, DATES.index(date))
        if offset_window_s is None:  # like the real load_day: the offset only travels with an offset-aware run
            legs.pop("offset")
        return eps, legs
    monkeypatch.setattr(ev, "load_day", fake_load_day)
    return seen


def test_run_end_to_end_offset_aware_with_venue_latency_and_fees(monkeypatch, tmp_path):
    seen = _setup(monkeypatch, tmp_path)
    out = tmp_path / "out"
    agg = ev.run(PAIR, [1.0], out, slow_wait_ms=0.01, dump_trades=True, offset_aware=True,
                 leg_latency_ms=(50.0, 8.0), venue_fees=(1.7, 3.0))
    assert set(seen) == {ev.OFFSET_WINDOW_S}                       # births labelled against the offset
    assert set(agg.strategy) == set(ev.STRATEGIES) | {"hindsight ceiling"}
    assert set(agg.tau_ms) == {50.0}
    folds = pd.read_csv(out / "pnl_vs_latency_folds.csv")
    assert (folds.fee_a_bps == 1.7).all() and (folds.fee_b_bps == 3.0).all()
    assert (folds.lat_a_ms == 50.0).all() and (folds.lat_b_ms == 8.0).all()
    meta = json.loads((out / "meta.json").read_text())
    assert meta["offset_aware"] and meta["latencies_ms"] == {"50.0": [50.0, 8.0]}
    val = sorted({d for days in meta["val_days"]["2.35"].values() for d in days})
    assert QUIET in val and BROKEN not in val                      # a quiet day is scored, a broken one is not
    by_day = pd.read_csv(out / "pnl_by_day.csv")
    quiet = by_day[by_day.date == QUIET]
    assert len(quiet) and (quiet.pnl_usd == 0).all() and (quiet.trades == 0).all()
    # every strategy is scored on exactly its fold's validation days, once each
    for (mode, fold, strat), g in by_day.groupby(["mode", "fold", "strategy"]):
        assert sorted(g.date) == sorted(meta["val_days"]["2.35"][str(fold)])
    tr = pd.read_parquet(out / "trades.parquet")
    assert {"fee_a_bps", "fee_b_bps", "dq_a", "t", "pnl"} <= set(tr.columns) and len(tr)
    # naive trades every trigger; the gated policies trade a subset
    naive = agg[(agg.strategy == "naive fast path")].trades.sum()
    assert (agg[agg.strategy.isin(["gap size only", "fast path + decay prior"])].trades <= naive).all()


def test_run_raw_mode_keeps_pnl_rel_equal_to_pnl(monkeypatch, tmp_path):
    _setup(monkeypatch, tmp_path)
    monkeypatch.setattr(ev, "TAUS_MS", [10])
    out = tmp_path / "raw"
    agg = ev.run(PAIR, [1.0], out, slow_wait_ms=0.01)
    assert np.allclose(agg.pnl_usd, agg.pnl_rel_usd)
