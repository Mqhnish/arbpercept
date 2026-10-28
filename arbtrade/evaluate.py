"""Walk-forward evaluation: P&L against latency for the decision policies.

    .venv/bin/python -m arbtrade.evaluate [--pair btc_perp_binance_bybit] [--fees 1.0 0.0 2.5]

--offset-aware (cross pairs): measure each gap against the venues' usual offset (trailing
5-minute median of mid a minus mid b) instead of zero. Births are labelled on that relative
gap, the slow path re-checks the relative gap, and the cascade's margins are chosen on P&L
net of the offset (pnl_rel). A persistent offset between venues is not arbitrage: trades that
only harvest it build a one-way position that must be closed against the same offset
(arbtrade/inventory.py).

--leg-latency-ms A B: one latency per venue (leg a, leg b) instead of the equal-latency sweep.
--venue-fees A B: one taker fee per venue (bps) instead of the same fee on both legs.
--feed-delay-ms A B: one market-data delay per venue (cross pairs). The trader sees each book
that late, so it reacts later and prices from older quotes. A trigger is traded only if the
delayed books still show a gap above the trigger. The order latency is separate.
--deplete-liquidity (cross pairs): a fill uses up the displayed size it took, until that side's
price changes. Each strategy is scored on a replay of only the triggers it sends.
Both are off by default, and then results are the same as before they existed.

Development days only. Folds come from the pair's own dates (training strictly before
validation, one embargo day). Within each fold, models are fitted on the first 70% of
training days, and calibration and the cascade's margins are chosen on the last 30%
(fold_days). Validation days are scored once per fold and never used for any choice.
Validation days with no trigger count as $0 days. Every trigger is replayed under the
optimistic and conservative fill bounds (see replay.py).
"""

from __future__ import annotations

import argparse
import atexit
import json
import shutil
import tempfile
import time
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

from arbdata import pipeline as P
from arbdata.align import align
from arbdata.config import load_config
from arbdata.episodes import CROSS_SIGN, cross_offset_bps, label_pair_day
from arbdata.splits import walk_forward_folds

from .policies import (GAP_ONLY_FEATURES, Calibrator, FastPrior, SlowModel, choose_margins, expected_value_gain,
                       fit_gain, miss_loss_bps)
from .convergence import exit_signal_times, execute_convergence
from .replay import MODES, Leg, execute, seen_after_us

TAUS_MS = [0, 1, 2, 5, 10, 20, 50, 100, 200]
NOTIONAL = 10_000.0
DIRECTIONS = {"sell_a_buy_b": ("a", "b"), "sell_b_buy_a": ("b", "a")}
HOLD_S = 60  # convergence trades: maximum holding time before closing out
OFFSET_WINDOW_S = 300.0  # --offset-aware: trailing window for the venues' usual offset
# Convergence pairs: (sell leg, buy leg, +1 if the trade bets on b being rich) per direction.
CONV_DIRECTIONS = {
    "basis": {"sell_perp_buy_spot": ("b", "a", 1), "buy_perp_sell_spot": ("a", "b", -1)},
    "ratio": {"sell_b_buy_a": ("b", "a", 1), "buy_b_sell_a": ("a", "b", -1)},
}
STRATEGIES = ["naive fast path", "gap size only", "fast path + decay prior", "slow model always", "latency-aware cascade"]


def load_day(cfg, pair_name: str, date: str, trigger_bps: float, offset_window_s: float | None = None):
    """Births and replay legs for one pair-day.

    None: the day is missing or fails quality. (empty frame, None): the day is fine but has no
    births, so it counts as a $0 day. offset_window_s (cross pairs): label births on the gap
    measured against the venues' trailing offset, and keep the offset for the replay's re-check.
    """
    spec = cfg.pairs[pair_name]
    l1, downs, trades, res = {}, {}, [], []
    for leg, key in (("a", spec.a), ("b", spec.b)):
        rep_path = P.quality_path(cfg, key, date)
        if not rep_path.exists():
            return None
        rep = json.loads(rep_path.read_text())
        if not rep["passes"]:
            return None
        l1[leg] = pd.read_parquet(cfg.l1_path(cfg.streams[key], date))
        downs[leg] = P.leg_down_windows(cfg, key, date, rep)
        trades.append(P.load_trades(cfg, key, date))
        res.append(cfg.source_cfg(key)["resolution_ms"])
    al = align(l1["a"], l1["b"], downs["a"], downs["b"])
    use_offset = spec.type == "cross" and offset_window_s is not None
    eps = label_pair_day(al, spec, date, {"trigger": trigger_bps}, cfg.resolution_ms(spec), cfg.episodes,
                         cfg.features, leg_resolution_ms=tuple(res), trades=tuple(trades),
                         cross_offset_window_s=offset_window_s if use_offset else None)
    if eps.empty:
        return pd.DataFrame(), None
    eps = eps[~eps.stale_birth].reset_index(drop=True)
    if eps.empty:
        return pd.DataFrame(), None
    legs = {k: Leg.from_l1(v, sampled=r > 1) for (k, v), r in zip(l1.items(), res)}
    if use_offset:
        eps["edge_rel_bps"] = eps.edge_birth_bps  # births are already labelled on the relative gap
        legs["offset"] = (al.t.to_numpy(), cross_offset_bps(al, offset_window_s))
    elif spec.type == "cross":
        eps["edge_rel_bps"] = eps.edge_birth_bps - offset_at(al, eps)
    if spec.type in CONV_DIRECTIONS:
        legs["ctx"] = convergence_context(cfg, spec, al)
    return eps, legs


def offset_at(al: pd.DataFrame, eps: pd.DataFrame, window_s: float = OFFSET_WINDOW_S) -> np.ndarray:
    """Usual level of each birth's edge direction: the trailing (strictly past) median of mid a minus
    mid b in bps, signed + for selling a and buying b, - for the reverse."""
    t = al.t.to_numpy()
    ref = cross_offset_bps(al, window_s)
    i = np.maximum(np.searchsorted(t, eps.birth_ts.to_numpy(), side="right") - 1, 0)
    sign = np.where(eps.direction.to_numpy() == "sell_a_buy_b", 1.0, -1.0)
    return sign * np.nan_to_num(ref[i])


def offset_at_times(offset: tuple[np.ndarray, np.ndarray], t: np.ndarray, sign: float) -> np.ndarray:
    """The usual offset (bps) in force at times t, for one direction (sign from CROSS_SIGN).
    offset = (event times, cross_offset_bps at those events); 0 before the first reference."""
    t_o, ref = offset
    i = np.searchsorted(t_o, np.asarray(t, dtype=np.int64), side="right") - 1
    return sign * np.where(i >= 0, np.nan_to_num(ref[np.maximum(i, 0)]), 0.0)


def convergence_context(cfg, spec, al: pd.DataFrame) -> dict:
    """Event-clock series the convergence replay needs, all causal (past data only)."""
    from arbdata.episodes import edges, ratio_fair
    from arbdata.features import trailing_reference
    t = al.t.to_numpy()
    valid = al.valid.to_numpy()
    if spec.type == "basis":
        basis = ((al.b_mid - al.a_mid) / al.a_mid * 1e4).to_numpy()
        ref = trailing_reference(t, basis, cfg.episodes["basis_ref_window_s"])
        dev = basis - ref
        ex = edges(al, "basis", ref)
        beta = np.ones(len(t))
    else:
        alpha, beta = ratio_fair(t, al, valid, cfg.features)
        dev = (np.log(al.b_mid.to_numpy()) - (alpha + beta * np.log(al.a_mid.to_numpy()))) * 1e4
        ex = edges(al, "ratio", None, (alpha, beta))
    closed = {d: (np.nan_to_num(sign * dev, nan=np.inf) <= 0) for d, (_, _, sign) in CONV_DIRECTIONS[spec.type].items()}
    return {"type": spec.type, "t": t, "beta": beta, "edges": ex, "closed": closed}


def replay_day(eps: pd.DataFrame, legs: dict, delay_ms: float, fee_bps: float, mode: str,
               decide_after_ms: float | np.ndarray = 0.0, delay_b_ms: float | None = None, fee_b_bps: float | None = None,
               feed_delay_ms: tuple[float, float] = (0.0, 0.0), deplete: bool = False) -> pd.DataFrame:
    """Replay every birth. delay_ms and fee_bps are leg a's, and leg b's too unless delay_b_ms or
    fee_b_bps is given.

    decide_after_ms > 0: the order is priced from quotes seen that long after the trigger
    (a slow path that re-reads the book once its model has finished). One value, or one per birth.

    feed_delay_ms (leg a, leg b): each venue's market-data delay. The trader sees a birth once
    the update that opened it reaches it (replay.seen_after_us), and from then on sees each book
    that venue's feed delay late. The order latencies are separate (delay_ms, delay_b_ms).
    deplete: fills use up the displayed size they took, shared by all the births given (replay.py).

    With an offset in legs (load_day with offset_window_s), edge_dec_bps is the gap seen at
    decision time measured against the usual offset, and pnl_rel credits each hedged unit with
    that relative gap only: pnl_rel = pnl - hedged * mid * offset. The offset part is paid back
    when the position is closed, so pnl_rel is what a trade really earns. Without an offset,
    pnl_rel equals pnl.
    """
    lat = {"a": delay_ms, "b": delay_ms if delay_b_ms is None else delay_b_ms}
    fee = {"a": fee_bps, "b": fee_bps if fee_b_bps is None else fee_b_bps}
    feed = {"a": feed_delay_ms[0], "b": feed_delay_ms[1]}
    ctx = legs.get("ctx")
    if ctx is not None:
        if any(feed.values()) or deplete or np.ndim(decide_after_ms):
            raise ValueError("feed delay, liquidity reuse and per-birth decision times apply to cross-venue pairs only")
        r = replay_convergence(eps, legs, ctx, max(lat.values()), (fee["a"] + fee["b"]) / 2, mode, decide_after_ms)
        r["pnl_rel"], r["pnl_rel_bps"] = r.pnl, r.pnl_bps
        return r
    us = lambda ms: int(round(ms * 1000))
    after = (us(decide_after_ms) if np.ndim(decide_after_ms) == 0
             else np.round(np.asarray(decide_after_ms, float) * 1000).astype(np.int64))
    off = legs.get("offset")
    parts = []
    for direction, (sell, buy) in DIRECTIONS.items():
        m = (eps.direction == direction).to_numpy()
        if m.any():
            t_birth = eps.birth_ts.to_numpy()[m]
            seen = (seen_after_us(legs[sell], legs[buy], t_birth, us(feed[sell]), us(feed[buy]))
                    if any(feed.values()) else np.zeros(len(t_birth), np.int64))
            t_dec = t_birth + seen + (after if np.ndim(after) == 0 else after[m])
            r = execute(legs[sell], legs[buy], t_dec, us(lat[sell]), fee[sell], fee[buy], NOTIONAL, mode,
                        delay_buy_us=us(lat[buy]), feed_sell_us=us(feed[sell]), feed_buy_us=us(feed[buy]),
                        deplete=deplete)
            # The usual offset as of the books the trader has seen (both venues' views reach that far).
            t_view = t_dec - us(max(feed.values()))
            o = np.zeros(len(t_dec)) if off is None else offset_at_times(off, t_view, CROSS_SIGN[direction])
            r["edge_dec_bps"] = r.edge_dec_bps - o
            r["pnl_rel"] = r.pnl - np.where(r.hedged > 0, r.hedged * r.mid_dec * o / 1e4, 0.0)
            r["pnl_rel_bps"] = np.where(r.notional > 0, r.pnl_rel / r.notional * 1e4, 0.0)
            r["seen_after_us"] = seen  # how long after the birth the trader saw it (0 without a feed delay)
            r.index = eps.index[m]
            parts.append(r)
    return pd.concat(parts).loc[eps.index]


def replay_convergence(eps, legs, ctx, delay_ms, fee_bps, mode, decide_after_ms=0.0) -> pd.DataFrame:
    parts = []
    t_ev = ctx["t"]
    for direction, (sell, buy, _) in CONV_DIRECTIONS[ctx["type"]].items():
        m = (eps.direction == direction).to_numpy()
        if not m.any():
            continue
        t_dec = eps.birth_ts.to_numpy()[m] + int(round(decide_after_ms * 1000))
        i = np.maximum(np.searchsorted(t_ev, t_dec, side="right") - 1, 0)
        beta = ctx["beta"][i]
        n_b, n_a = np.full(len(t_dec), NOTIONAL), beta * NOTIONAL
        ns, nb = (n_b, n_a) if sell == "b" else (n_a, n_b)
        closed = ctx["closed"][direction]
        fn = lambda t_arr, c=closed: exit_signal_times(t_ev, c, t_arr, HOLD_S * 1_000_000)
        r = execute_convergence(legs[sell], legs[buy], t_dec, int(round(delay_ms * 1000)), fee_bps, ns, nb, fn, mode)
        r["edge_dec_bps"] = ctx["edges"][direction][i]
        r.index = eps.index[m]
        parts.append(r)
    return pd.concat(parts).loc[eps.index]


def fold_days(fold: dict, have_train: set, have_val: set) -> tuple[list, list, list] | None:
    """Split one fold. Models are fitted on the first 70% of its training days; calibration and
    the cascade's margins use the last 30%; scoring uses its validation days. All training days
    come before every validation day (walk_forward_folds). None when there are too few days."""
    tr = [d for d in fold["train"] if d in have_train]
    va = [d for d in fold["val"] if d in have_val]
    if len(tr) < 3 or not va:
        return None
    cut = max(1, int(len(tr) * 0.7))
    return tr[:cut], tr[cut:], va


def measure_latencies(fast: FastPrior, slow: SlowModel, X: pd.DataFrame, repeats: int = 300) -> tuple[float, float]:
    """Median single-trigger inference time in ms, on plain arrays as a live system would use.
    The slow model is timed in its compiled form (arbtrade/compiled.py). Feature computation is
    not included: here the slow features are computed offline. Live, arbtrade/slowpath.py computes
    them one update at a time, and `python -m arbtrade.slowpath` times that."""
    Xf = X[fast.features].to_numpy()
    Xs = X[slow.cols].to_numpy()
    tf, ts = [], []
    warnings.filterwarnings("ignore", message="X does not have valid feature names")
    for i in range(repeats):
        row_f, row_s = Xf[i % len(Xf)], Xs[[i % len(Xs)]]
        t0 = time.perf_counter()
        z = np.where(np.isnan(row_f), fast.median, row_f)
        _ = 1 / (1 + np.exp(-(((z - fast.mu) / fast.sd) @ fast.w + fast.b)))
        tf.append(time.perf_counter() - t0)
        t0 = time.perf_counter()
        slow.compiled.predict_one(row_s[0])
        ts.append(time.perf_counter() - t0)
    return float(np.median(tf) * 1e3), float(np.median(ts) * 1e3)


DUMP_TAUS_MS = [1, 10, 50]  # latencies whose individual trades are written out (--dump-trades)


def spill_legs(legs: dict, folder: Path) -> dict:
    """Write one day's price arrays to disk and map them back read-only.

    A month of BTC prices takes about 1.5 GB in memory, so holding every development day at
    once does not fit on a laptop. Mapped arrays behave exactly like the originals in the
    replay, but the operating system loads them only while a replay reads them. Replays never
    modify them. A convergence pair's context stays in memory (small, and its own structure)."""
    folder.mkdir(parents=True, exist_ok=True)

    def mapped(name: str, a: np.ndarray) -> np.ndarray:
        path = folder / f"{name}.npy"
        np.save(path, np.ascontiguousarray(a))
        return np.load(path, mmap_mode="r")

    out = {}
    for k, v in legs.items():
        if isinstance(v, Leg):
            mins = [None if getattr(v, f) is None else mapped(f"{k}_{f}", getattr(v, f)) for f in ("bid_sz_min", "ask_sz_min")]
            out[k] = Leg(*(mapped(f"{k}_{f}", getattr(v, f)) for f in ("t", "bid", "ask", "bid_sz", "ask_sz")), v.sampled, *mins)
        elif k == "offset":
            out[k] = tuple(mapped(f"offset_{i}", a) for i, a in enumerate(v))
        else:
            out[k] = v
    return out


def run(pair: str, fees: list[float], out_dir, slow_wait_ms: float | None = None, dump_trades: bool = False,
        offset_aware: bool = False, leg_latency_ms: tuple[float, float] | None = None,
        venue_fees: tuple[float, float] | None = None, feed_delay_ms: tuple[float, float] | None = None,
        deplete_liquidity: bool = False) -> pd.DataFrame:
    """feed_delay_ms (leg a, leg b): each venue's market-data delay. A trigger is then traded only
    if the books the trader has seen still show a gap above the trigger, the same re-check the
    slow path makes. deplete_liquidity: fills use up the displayed size they took. Models are
    fitted and calibrated on replays that send every trigger. Each strategy is scored on a replay
    of only the triggers it sends, so it never loses size to trades it did not make."""
    cfg = load_config()
    convergence = cfg.pairs[pair].type in CONV_DIRECTIONS
    feed = tuple(float(f) for f in feed_delay_ms) if feed_delay_ms else (0.0, 0.0)
    gate_fast = any(feed)  # without a feed delay the trader sees every birth as it happens
    if convergence and (gate_fast or deplete_liquidity):
        raise ValueError("--feed-delay-ms and --deplete-liquidity apply to cross-venue pairs only")
    splits = json.loads(cfg.splits_path.read_text())
    dev_dates = sorted(set(splits["development"]) & {p.stem for p in (cfg.data_root / "episodes" / pair).glob("*.parquet")})
    folds = walk_forward_folds(dev_dates, splits["params"]["embargo_days"], splits["params"]["n_folds"])
    print(f"{pair}: {len(dev_dates)} development days, {len(folds)} folds", flush=True)
    offset_aware = offset_aware and not convergence
    ecol = "edge_rel_bps" if offset_aware else "edge_birth_bps"
    pcol = "pnl_rel" if offset_aware else "pnl"  # the P&L that calibration choices maximise
    # Latency settings: (label, leg a ms, leg b ms). The label is the slower leg's latency.
    lat_sets = [(max(leg_latency_ms), *leg_latency_ms)] if leg_latency_ms else [(t, t, t) for t in TAUS_MS]
    lat_of = {s[0]: (s[1], s[2]) for s in lat_sets}
    taus = list(lat_of)
    dump_taus = set(taus) if leg_latency_ms else set(DUMP_TAUS_MS)
    fee_sets = [tuple(venue_fees)] if venue_fees else [(f, f) for f in fees]
    rows, day_rows, trade_rows = [], [], []
    meta = {"pair": pair, "offset_aware": offset_aware, "offset_window_s": OFFSET_WINDOW_S if offset_aware else None,
            "latencies_ms": {str(t): list(lat_of[t]) for t in taus},
            "feed_delay_ms": list(feed), "deplete_liquidity": deplete_liquidity,
            "folds": [{"train": [f["train"][0], f["train"][-1]], "val": [f["val"][0], f["val"][-1]]} for f in folds]}

    for fee_a, fee_b in fee_sets:
        fee = (fee_a + fee_b) / 2  # label: average fee per leg
        trigger = (2 if convergence else 1) * (fee_a + fee_b)  # gross edge must cover every fill's fee
        rp = lambda e, legs, tau, mode, after=0.0: replay_day(e, legs, lat_of[tau][0], fee_a, mode, after,
                                                               lat_of[tau][1], fee_b, feed, deplete_liquidity)
        days, quiet = {}, set()
        spill = Path(tempfile.mkdtemp(prefix="eval_prices_", dir=cfg.data_root))
        atexit.register(shutil.rmtree, spill, True)
        for d in dev_dates:
            got = load_day(cfg, pair, d, trigger, OFFSET_WINDOW_S if offset_aware else None)
            if got is None:
                continue
            if len(got[0]):
                days[d] = (got[0], spill_legs(got[1], spill / d))
            else:
                quiet.add(d)  # a valid day without a single trigger: a $0 day, not a missing one
        print(f"  fees {fee_a}/{fee_b} bps: {sum(len(e) for e, _ in days.values()):,} triggers over {len(days)} days "
              f"({len(quiet)} days without triggers)", flush=True)

        # Measure the slow path's real inference latency once (it sets how long the slow path waits).
        first = folds[0]["train"]
        X0 = pd.concat([days[d][0] for d in first if d in days], ignore_index=True)
        # Labels at 10 ms: at 0 ms every optimistic trigger fills, which leaves nothing to learn.
        y0 = pd.concat([replay_day(days[d][0], days[d][1], 10, fee_a, "optimistic", fee_b_bps=fee_b)
                        for d in first if d in days]).full_fill.to_numpy()
        fast_ms, slow_ms = measure_latencies(FastPrior().fit(X0, y0), SlowModel().fit(X0, y0), X0)
        delta = float(np.ceil(slow_ms * 100) / 100) if slow_wait_ms is None else float(slow_wait_ms)  # measured, rounded up to 10 µs
        meta.setdefault("latency_ms", {})[str(fee)] = {"fast_prior": fast_ms, "slow_model": slow_ms, "slow_wait_used": delta}
        print(f"  measured inference: fast prior {fast_ms * 1000:.1f} µs, compiled slow model {slow_ms * 1000:.1f} µs -> slow path waits {delta} ms", flush=True)

        for mode in MODES:
            out = {d: {t: rp(e, legs, t, mode) for t in taus} for d, (e, legs) in days.items()}
            # Slow path: decides delta ms after the trigger, re-reads the book, trades only if the gap
            # still covers fees (relative to the usual offset when offset-aware), priced at the quotes seen then.
            out_slow = {d: {t: rp(e, legs, t, mode, delta) for t in taus} for d, (e, legs) in days.items()}
            for k, fold in enumerate(folds):
                split = fold_days(fold, set(days), set(days) | quiet)
                if split is None:
                    continue
                fit_d, cal_d, va_all = split
                va = [d for d in va_all if d in days]
                if not va:
                    continue
                zero_days = [d for d in va_all if d not in days]
                meta.setdefault("val_days", {}).setdefault(str(fee), {})[str(k)] = va_all
                cat = lambda ds: pd.concat([days[d][0] for d in ds], ignore_index=True)

                def gated(r):
                    # Trade only a gap the trader still sees above the trigger: the slow path's view after
                    # inference, and with a feed delay the fast path's delayed view too. Otherwise skip.
                    still = r.edge_dec_bps.to_numpy() > trigger
                    for c in ("pnl", "pnl_bps", "pnl_rel", "pnl_rel_bps"):
                        r[c] = np.where(still, r[c], 0.0)
                    r["full_fill"] = r.full_fill & still
                    r["still_open"] = still
                    return r

                def res(ds, t):
                    r = pd.concat([out[d][t] for d in ds], ignore_index=True)
                    return gated(r) if gate_fast else r.assign(still_open=True)
                res_slow = lambda ds, t: gated(pd.concat([out_slow[d][t] for d in ds], ignore_index=True))
                Xfit, Xcal, Xval = cat(fit_d), cat(cal_d), cat(va)
                for tau in taus:
                    fit_now, fit_slow = res(fit_d, tau), res_slow(fit_d, tau)
                    yf, yfd = fit_now.full_fill.to_numpy(), fit_slow.full_fill.to_numpy()
                    if yf.all() or not yf.any() or yfd.all() or not yfd.any():
                        continue
                    fast, slow = FastPrior().fit(Xfit, yf), SlowModel().fit(Xfit, yfd)
                    gap = FastPrior(GAP_ONLY_FEATURES).fit(Xfit, yf)
                    L_now = miss_loss_bps(fit_now[fit_now.still_open], pcol + "_bps")
                    L_slow = miss_loss_bps(fit_slow[fit_slow.still_open], pcol + "_bps")
                    if convergence:  # payoff of a fill is learned: it depends on the later reversion
                        e_fit = Xfit.edge_birth_bps.to_numpy()
                        g_now = fit_gain(e_fit, fit_now)
                        open_ = fit_slow.still_open.to_numpy()
                        g_slow = fit_gain(e_fit[open_], fit_slow[open_])
                    else:  # cross-venue: a full fill locks in the edge minus fees
                        g_now = g_slow = (-trigger, 1.0)

                    cal_now, cal_slow = res(cal_d, tau), res_slow(cal_d, tau)
                    cal_f = Calibrator().fit(fast.predict(Xcal), cal_now.full_fill.to_numpy())
                    cal_g = Calibrator().fit(gap.predict(Xcal), cal_now.full_fill.to_numpy())
                    cal_s = Calibrator().fit(slow.predict(Xcal), cal_slow.full_fill.to_numpy())
                    q_fast = lambda X: cal_f.transform(fast.predict(X))
                    q_slow = lambda X: cal_s.transform(slow.predict(X))
                    ev_cal_f = expected_value_gain(q_fast(Xcal), Xcal[ecol].to_numpy(), g_now, L_now)
                    ev_cal_s = expected_value_gain(q_slow(Xcal), Xcal[ecol].to_numpy(), g_slow, L_slow)
                    lo, hi = choose_margins(ev_cal_f, cal_now[pcol].to_numpy(), cal_slow[pcol].to_numpy(),
                                            (ev_cal_s > 0) & cal_slow.still_open.to_numpy() & cal_now.still_open.to_numpy())

                    edge = Xval[ecol].to_numpy()
                    now, later = res(va, tau), res_slow(va, tau)
                    seen = now.still_open.to_numpy()  # all True without a feed delay
                    ev_f = np.where(seen, expected_value_gain(q_fast(Xval), edge, g_now, L_now), -np.inf)
                    ev_g = np.where(seen, expected_value_gain(cal_g.transform(gap.predict(Xval)), edge, g_now, L_now), -np.inf)
                    ev_s = np.where(later.still_open.to_numpy() & seen,
                                    expected_value_gain(q_slow(Xval), edge, g_slow, L_slow), -np.inf)
                    act = ev_f > hi
                    ask = (ev_f >= lo) & ~act
                    cols = ["pnl", "pnl_rel", "full_fill", "hedged"]

                    def outcome(take, slow_ch):
                        """Each trigger's outcome under a strategy that trades `take`, deciding the `slow_ch`
                        ones after the slow model. Rows it does not take are never used."""
                        if deplete_liquidity:  # replay only what it sends: it shares size only with its own fills
                            o, pos = {c: now[c].to_numpy().copy() for c in cols}, 0
                            for d in va:
                                e, legs = days[d]
                                tk = take[pos:pos + len(e)]
                                if tk.any():
                                    r = rp(e[tk], legs, tau, mode, np.where(slow_ch[pos:pos + len(e)][tk], delta, 0.0))
                                    for c in cols:
                                        o[c][pos + np.flatnonzero(tk)] = r[c].to_numpy()
                                pos += len(e)
                            return pd.DataFrame(o)
                        if not slow_ch.any():
                            return now
                        if slow_ch.all():
                            return later
                        return pd.DataFrame({c: np.where(slow_ch, later[c], now[c]) for c in cols})

                    never, always = np.zeros(len(now), bool), np.ones(len(now), bool)
                    choices = {  # strategy: (triggers it trades, which of them wait for the slow model)
                        "naive fast path": (seen, never),
                        "gap size only": (ev_g > 0, never),
                        "fast path + decay prior": (ev_f > 0, never),
                        "slow model always": (ev_s > 0, always),
                        "latency-aware cascade": (act | (ask & (ev_s > 0)), ~act),
                    }
                    for name, (take, slow_ch) in choices.items():
                        o = outcome(take, slow_ch)
                        pnl = np.where(take, o.pnl, 0.0)
                        pnl_rel = np.where(take, o.pnl_rel, 0.0)
                        traded = take
                        full = o.full_fill.to_numpy()
                        hedged = o.hedged.to_numpy()
                        waited = np.where(slow_ch, delta, 0.0)
                        slow_share = float(ask.mean()) if name == "latency-aware cascade" else float(name == "slow model always")
                        if dump_trades and tau in dump_taus and not convergence:
                            # Position change on leg a: selling there (sell_a_buy_b) leaves a short on a.
                            sign = np.where(Xval.direction.to_numpy() == "sell_a_buy_b", -1.0, 1.0)
                            fill_t = (Xval.birth_ts.to_numpy() + np.round((waited + tau) * 1000).astype(np.int64)
                                      + now.seen_after_us.to_numpy())
                            tk = np.asarray(traded, bool)
                            trade_rows.append(pd.DataFrame({
                                "fee_bps_per_leg": fee, "fee_a_bps": fee_a, "fee_b_bps": fee_b, "mode": mode, "fold": k,
                                "tau_ms": tau, "strategy": name, "date": Xval.date.to_numpy()[tk], "t": fill_t[tk],
                                "dq_a": (sign * hedged)[tk], "pnl": np.asarray(pnl, float)[tk]}))
                        rows.append({"fee_bps_per_leg": fee, "fee_a_bps": fee_a, "fee_b_bps": fee_b, "mode": mode,
                                     "fold": k, "tau_ms": tau, "lat_a_ms": lat_of[tau][0], "lat_b_ms": lat_of[tau][1],
                                     "strategy": name, "val_days": len(va_all), "triggers": len(now),
                                     "trades": int(traded.sum()), "pnl_usd": float(np.sum(pnl)),
                                     "pnl_rel_usd": float(np.sum(pnl_rel)),
                                     "full_fill_rate": float(full[traded].mean()) if traded.any() else np.nan,
                                     "slow_share": slow_share, "margins": [lo, hi]})
                        per_day = pd.DataFrame({"date": Xval.date.to_numpy(), "pnl": np.asarray(pnl, float),
                                                "pnl_rel": np.asarray(pnl_rel, float),
                                                "trades": np.asarray(traded, int)}).groupby("date").sum()
                        for day, r in per_day.iterrows():
                            day_rows.append({"fee_bps_per_leg": fee, "mode": mode, "fold": k, "tau_ms": tau,
                                             "strategy": name, "date": day, "pnl_usd": float(r.pnl),
                                             "pnl_rel_usd": float(r.pnl_rel), "trades": int(r.trades)})
                        for day in zero_days:
                            day_rows.append({"fee_bps_per_leg": fee, "mode": mode, "fold": k, "tau_ms": tau,
                                             "strategy": name, "date": day, "pnl_usd": 0.0, "pnl_rel_usd": 0.0,
                                             "trades": 0})
                    # Ceiling for reference: trade exactly the triggers that turned out profitable at tau.
                    best = now[pcol].clip(lower=0)
                    if deplete_liquidity:  # replay only the winners, so they do not lose size to the others
                        win = (now[pcol] > 0).to_numpy()
                        best = pd.Series(np.where(win, outcome(win, never)[pcol], 0.0)).clip(lower=0)
                    rows.append({"fee_bps_per_leg": fee, "fee_a_bps": fee_a, "fee_b_bps": fee_b, "mode": mode, "fold": k,
                                 "tau_ms": tau, "lat_a_ms": lat_of[tau][0], "lat_b_ms": lat_of[tau][1],
                                 "strategy": "hindsight ceiling", "val_days": len(va_all), "triggers": len(now),
                                 "trades": int((now[pcol] > 0).sum()), "pnl_usd": float(best.sum()),
                                 "pnl_rel_usd": float(best.sum()), "full_fill_rate": np.nan,
                                 "slow_share": 0.0, "margins": None})
                print(f"    {mode} fold {k}: done", flush=True)

    df = pd.DataFrame(rows)
    out_dir.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_dir / "pnl_vs_latency_folds.csv", index=False)
    pd.DataFrame(day_rows).to_csv(out_dir / "pnl_by_day.csv", index=False)
    (out_dir / "meta.json").write_text(json.dumps(meta, indent=1))
    if trade_rows:
        pd.concat(trade_rows, ignore_index=True).to_parquet(out_dir / "trades.parquet", index=False)
    agg = (df.groupby(["fee_bps_per_leg", "mode", "tau_ms", "strategy"])
             .agg(val_days=("val_days", "sum"), triggers=("triggers", "sum"), trades=("trades", "sum"),
                  pnl_usd=("pnl_usd", "sum"), pnl_rel_usd=("pnl_rel_usd", "sum"),
                  full_fill_rate=("full_fill_rate", "mean"), slow_share=("slow_share", "mean"))
             .reset_index())
    agg["pnl_per_day_usd"] = agg.pnl_usd / agg.val_days
    agg["pnl_rel_per_day_usd"] = agg.pnl_rel_usd / agg.val_days
    agg.to_csv(out_dir / "pnl_vs_latency.csv", index=False)
    return agg


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pair", default="btc_perp_binance_bybit")
    ap.add_argument("--fees", nargs="*", type=float, default=[1.0, 0.0, 2.5])
    ap.add_argument("--venue-fees", nargs=2, type=float, default=None, metavar=("A", "B"),
                    help="taker fee per venue (bps) for leg a and leg b; replaces --fees")
    ap.add_argument("--leg-latency-ms", nargs=2, type=float, default=None, metavar=("A", "B"),
                    help="order latency per venue (ms) for leg a and leg b; replaces the equal-latency sweep")
    ap.add_argument("--feed-delay-ms", nargs=2, type=float, default=None, metavar=("A", "B"),
                    help="market-data delay per venue (ms) for leg a and leg b: the trader sees each book this late")
    ap.add_argument("--deplete-liquidity", action="store_true",
                    help="a fill uses up the displayed size it took until that side's price changes")
    ap.add_argument("--slow-wait-ms", type=float, default=None,
                    help="override the measured slow-model latency (e.g. 1.0 for a compiled model)")
    ap.add_argument("--tag", default="", help="suffix for the output folder")
    ap.add_argument("--offset-aware", action="store_true",
                    help="cross pairs: measure gaps against the venues' trailing offset, not zero")
    ap.add_argument("--dump-trades", action="store_true",
                    help="write every trade at 1, 10 and 50 ms (or at --leg-latency-ms) to trades.parquet "
                         "(for analysis/inventory_check.py)")
    args = ap.parse_args()
    cfg = load_config()
    agg = run(args.pair, args.fees, cfg.reports_dir / "pnl" / f"{args.pair}{args.tag}", args.slow_wait_ms,
              args.dump_trades, args.offset_aware, args.leg_latency_ms, args.venue_fees, args.feed_delay_ms,
              args.deplete_liquidity)
    first_fee = sum(args.venue_fees) / 2 if args.venue_fees else args.fees[0]
    col = "pnl_rel_per_day_usd" if args.offset_aware else "pnl_per_day_usd"
    show = agg[agg.fee_bps_per_leg == first_fee].pivot_table(index=["mode", "tau_ms"], columns="strategy", values=col)
    print(show.round(1).to_string())


if __name__ == "__main__":
    main()
