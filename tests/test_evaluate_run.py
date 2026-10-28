"""End to end: arbtrade.evaluate.run on synthetic days (no data files needed).

load_config and load_day are replaced by small stand-ins, so this checks the walk-forward
loop itself: offset-aware re-checks, per-venue latency and fees, the gap-size baseline,
validation days without triggers counted as $0, and the trade dump the inventory check reads.
"""

import json
from types import SimpleNamespace

import numpy as np
import pandas as pd
import pytest

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
    seen, feeds = [], []

    def fake_load_day(cfg, pair, date, trigger, offset_window_s=None, feed_delay_ms=None):
        seen.append(offset_window_s)
        feeds.append(feed_delay_ms)
        if date == BROKEN:
            return None
        if date == QUIET:
            return pd.DataFrame(), None
        eps, legs = _day(date, DATES.index(date))
        if offset_window_s is None:  # like the real load_day: the offset only travels with an offset-aware run
            legs.pop("offset")
        return eps, legs
    monkeypatch.setattr(ev, "load_day", fake_load_day)
    return seen, feeds


def test_run_end_to_end_offset_aware_with_venue_latency_and_fees(monkeypatch, tmp_path):
    seen, feeds = _setup(monkeypatch, tmp_path)
    out = tmp_path / "out"
    agg = ev.run(PAIR, [1.0], out, slow_wait_ms=0.01, dump_trades=True, offset_aware=True,
                 leg_latency_ms=(50.0, 8.0), venue_fees=(1.7, 3.0))
    assert set(seen) == {ev.OFFSET_WINDOW_S}                       # births labelled against the offset
    assert set(feeds) == {None}                                    # no feed delay: births from the raw books
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


def test_run_zero_feed_delay_and_no_depletion_match_the_default(monkeypatch, tmp_path):
    _setup(monkeypatch, tmp_path)
    monkeypatch.setattr(ev, "TAUS_MS", [10])
    kw = dict(slow_wait_ms=0.01, dump_trades=True, offset_aware=True, venue_fees=(1.7, 3.0))
    ev.run(PAIR, [1.0], tmp_path / "default", **kw)
    ev.run(PAIR, [1.0], tmp_path / "zero", feed_delay_ms=(0.0, 0.0), deplete_liquidity=False, **kw)
    for f in ("pnl_vs_latency_folds.csv", "pnl_by_day.csv", "pnl_vs_latency.csv"):
        assert (tmp_path / "default" / f).read_bytes() == (tmp_path / "zero" / f).read_bytes()
    pd.testing.assert_frame_equal(pd.read_parquet(tmp_path / "default" / "trades.parquet"),
                                  pd.read_parquet(tmp_path / "zero" / "trades.parquet"))
    meta = json.loads((tmp_path / "default" / "meta.json").read_text())
    assert meta["feed_delay_ms"] == [0.0, 0.0] and meta["deplete_liquidity"] is False


def test_run_with_feed_delay_trades_only_gaps_the_trader_can_see(monkeypatch, tmp_path):
    _, feeds = _setup(monkeypatch, tmp_path)
    monkeypatch.setattr(ev, "TAUS_MS", [10])
    out = tmp_path / "feed"
    ev.run(PAIR, [1.0], out, slow_wait_ms=0.01, feed_delay_ms=(2.0, 30.0))
    meta = json.loads((out / "meta.json").read_text())
    assert meta["feed_delay_ms"] == [2.0, 30.0] and meta["births_from_delayed_view"]
    assert set(feeds) == {(2.0, 30.0)}                             # births built from the delayed books
    folds = pd.read_csv(out / "pnl_vs_latency_folds.csv")
    naive = folds[folds.strategy == "naive fast path"]
    assert len(naive) and (naive.trades < naive.triggers).all()
    for _, row in naive.iterrows():
        seen = 0
        for d in meta["val_days"]["1.0"][str(row.fold)]:
            got = ev.load_day(None, PAIR, d, 2.0)
            if got[1] is not None:
                r = ev.replay_day(got[0], got[1], 10, 1.0, row["mode"], feed_delay_ms=(2.0, 30.0))
                seen += int((r.edge_dec_bps > 2.0).sum())  # the delayed books still show a gap above the trigger
        assert row.trades == seen


SWAP = "2024-01-11"  # first validation day of the last fold (training: 1-9 Jan)


def _setup_shared_quotes(monkeypatch, tmp_path):
    """Like _setup, but every birth has a twin 1 µs later (same gap, other f_ features), and books show
    only 0.3 units, so a twin that follows a fill finds just 0.05 of its 0.25 units left.

    f_a_spread_bps is +3 on the earlier twin and -3 on the later one, except on the last fold's
    validation days (from SWAP), where the signs swap. Models fitted on earlier days learn that +3
    fills, so on those days they send the later twin and skip the earlier one."""
    _setup(monkeypatch, tmp_path)
    plain = ev.load_day

    def twins(cfg, pair, date, trigger, offset_window_s=None):
        got = plain(cfg, pair, date, trigger, offset_window_s)
        if got is None or got[1] is None:
            return got
        eps, legs = got
        rng = np.random.default_rng(len(eps) + DATES.index(date))
        twin = eps.copy()
        twin["birth_ts"] = twin.birth_ts + 1
        for f in [c for c in twin.columns if c.startswith("f_")]:
            twin[f] = rng.normal(0, 1, len(twin))
        first = -3.0 if date >= SWAP else 3.0
        eps["f_a_spread_bps"], twin["f_a_spread_bps"] = first, -first
        eps = pd.concat([eps, twin]).sort_values("birth_ts", kind="stable").reset_index(drop=True)
        thin = lambda g: Leg(g.t, g.bid, g.ask, np.full(len(g.t), 0.3), np.full(len(g.t), 0.3), g.sampled)
        return eps, {**legs, "a": thin(legs["a"]), "b": thin(legs["b"])}
    monkeypatch.setattr(ev, "load_day", twins)


def test_run_with_depletion_scores_each_strategy_on_its_own_trades(monkeypatch, tmp_path):
    _setup_shared_quotes(monkeypatch, tmp_path)
    monkeypatch.setattr(ev, "TAUS_MS", [10])
    agg_reuse = ev.run(PAIR, [1.0], tmp_path / "reuse", slow_wait_ms=0.01)
    agg = ev.run(PAIR, [1.0], tmp_path / "used", slow_wait_ms=0.01, dump_trades=True, deplete_liquidity=True)
    assert json.loads((tmp_path / "used" / "meta.json").read_text())["deplete_liquidity"] is True
    naive = lambda a: a[a.strategy == "naive fast path"].set_index("mode").full_fill_rate
    assert (naive(agg) < naive(agg_reuse)).all()          # twins now find the displayed size used up
    folds = pd.read_csv(tmp_path / "used" / "pnl_vs_latency_folds.csv")
    late = folds[(folds.fold == 1) & (folds.strategy == "fast path + decay prior")]
    # it sends only the later twins there, and they fill in full: the earlier twins it skipped used nothing
    assert (late.trades == late.triggers / 2).all() and (late.full_fill_rate > 0.9).all()

    # Each strategy's trades replay, on their own, to exactly the P&L it was scored with.
    trades = pd.read_parquet(tmp_path / "used" / "trades.parquet")
    lost_to_others = 0
    for (mode, date), g in trades.groupby(["mode", "date"]):
        eps, legs = ev.load_day(None, PAIR, date, 2.0)
        row_of = {t: i for i, t in enumerate(eps.birth_ts)}
        sent_all = ev.replay_day(eps, legs, 10, 1.0, mode, delay_b_ms=10, deplete=True)
        sent_all_slow = ev.replay_day(eps, legs, 10, 1.0, mode, 0.01, deplete=True)
        for (fold, strategy), s in g.groupby(["fold", "strategy"]):
            fast = s.t.to_numpy() - 10_000
            is_fast = np.array([t in row_of for t in fast])
            idx = np.array([row_of[t] if f else row_of[t - 10] for t, f in zip(fast, is_fast)])
            order = np.argsort(idx)
            sub = eps.iloc[idx[order]]
            r = ev.replay_day(sub, legs, 10, 1.0, mode, np.where(is_fast[order], 0.0, 0.01), deplete=True)
            assert np.allclose(r.pnl.to_numpy(), s.pnl.to_numpy()[order])
            world = np.where(is_fast[order], sent_all.pnl.to_numpy()[idx[order]], sent_all_slow.pnl.to_numpy()[idx[order]])
            lost_to_others += int((~np.isclose(world, r.pnl.to_numpy())).sum())
    assert lost_to_others > 100  # replaying every trigger would have charged strategies for others' fills


def test_run_refuses_feed_delay_and_depletion_on_convergence_pairs(monkeypatch, tmp_path):
    _setup(monkeypatch, tmp_path)
    ev.load_config().pairs[PAIR].type = "basis"
    with pytest.raises(ValueError):
        ev.run(PAIR, [1.0], tmp_path / "x", feed_delay_ms=(5.0, 5.0))
    with pytest.raises(ValueError):
        ev.run(PAIR, [1.0], tmp_path / "x", deplete_liquidity=True)
