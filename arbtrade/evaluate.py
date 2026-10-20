"""Walk-forward evaluation: P&L against latency for four decision policies.

    .venv/bin/python -m arbtrade.evaluate [--pair btc_perp_binance_bybit] [--fees 1.0 0.0 2.5]

--offset-aware (cross pairs): measure each gap against the venues' usual offset (trailing
5-minute median of mid a minus mid b) instead of zero, both to fire and in the expected value.
A persistent offset between venues is not arbitrage: trades that only harvest it build a
one-way position that must be closed against the same offset (arbtrade/inventory.py).

Development days only. Folds come from the pair's own dates (training strictly before
validation, one embargo day). Within each fold, models are fitted on the first 70% of
training days and the cascade's margins are chosen on the last 30%. Validation days are
scored once per fold and never used for any choice. Every trigger is replayed under the
optimistic and conservative fill bounds (see replay.py).
"""

from __future__ import annotations

import argparse
import json
import time
import warnings

import numpy as np
import pandas as pd

from arbdata import pipeline as P
from arbdata.align import align
from arbdata.config import load_config
from arbdata.episodes import label_pair_day
from arbdata.splits import walk_forward_folds

from .policies import (FAST_FEATURES, Calibrator, FastPrior, SlowModel, choose_margins, expected_value_gain,
                       fit_gain, miss_loss_bps)
from .convergence import exit_signal_times, execute_convergence
from .replay import MODES, Leg, execute

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
STRATEGIES = ["naive fast path", "fast path + decay prior", "slow model always", "latency-aware cascade"]


def load_day(cfg, pair_name: str, date: str, trigger_bps: float):
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
    eps = label_pair_day(al, spec, date, {"trigger": trigger_bps}, cfg.resolution_ms(spec), cfg.episodes,
                         cfg.features, leg_resolution_ms=tuple(res), trades=tuple(trades))
    if eps.empty:
        return None
    eps = eps[~eps.stale_birth].reset_index(drop=True)
    if spec.type == "cross":
        eps["edge_rel_bps"] = eps.edge_birth_bps - offset_at(al, eps)
    legs = {k: Leg.from_l1(v, sampled=r > 1) for (k, v), r in zip(l1.items(), res)}
    if spec.type in CONV_DIRECTIONS:
        legs["ctx"] = convergence_context(cfg, spec, al)
    return eps, legs


def offset_at(al: pd.DataFrame, eps: pd.DataFrame, window_s: float = OFFSET_WINDOW_S) -> np.ndarray:
    """Usual level of each birth's edge direction: the trailing (strictly past) median of mid a minus
    mid b in bps, signed + for selling a and buying b, - for the reverse."""
    from arbdata.features import trailing_reference
    t = al.t.to_numpy()
    mid = ((al.a_mid + al.b_mid) / 2).to_numpy()
    ref = trailing_reference(t, ((al.a_mid - al.b_mid).to_numpy() / mid) * 1e4, window_s)
    i = np.maximum(np.searchsorted(t, eps.birth_ts.to_numpy(), side="right") - 1, 0)
    sign = np.where(eps.direction.to_numpy() == "sell_a_buy_b", 1.0, -1.0)
    return sign * np.nan_to_num(ref[i])


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
               decide_after_ms: float = 0.0) -> pd.DataFrame:
    """decide_after_ms > 0: the order is priced from quotes seen that long after the trigger
    (a slow path that re-reads the book once its model has finished)."""
    ctx = legs.get("ctx")
    if ctx is not None:
        return replay_convergence(eps, legs, ctx, delay_ms, fee_bps, mode, decide_after_ms)
    parts = []
    for direction, (sell, buy) in DIRECTIONS.items():
        m = (eps.direction == direction).to_numpy()
        if m.any():
            t_dec = eps.birth_ts.to_numpy()[m] + int(round(decide_after_ms * 1000))
            r = execute(legs[sell], legs[buy], t_dec, int(round(delay_ms * 1000)),
                        fee_bps, fee_bps, NOTIONAL, mode)
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


def measure_latencies(fast: FastPrior, slow: SlowModel, X: pd.DataFrame, repeats: int = 300) -> tuple[float, float]:
    """Median single-trigger inference time in ms, on plain arrays as a live system would use.
    The slow model is timed in its compiled form (arbtrade/compiled.py)."""
    Xf = X[FAST_FEATURES].to_numpy()
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


def run(pair: str, fees: list[float], out_dir, slow_wait_ms: float | None = None, dump_trades: bool = False,
        offset_aware: bool = False) -> pd.DataFrame:
    cfg = load_config()
    splits = json.loads(cfg.splits_path.read_text())
    dev_dates = sorted(set(splits["development"]) & {p.stem for p in (cfg.data_root / "episodes" / pair).glob("*.parquet")})
    folds = walk_forward_folds(dev_dates, splits["params"]["embargo_days"], splits["params"]["n_folds"])
    print(f"{pair}: {len(dev_dates)} development days, {len(folds)} folds", flush=True)
    rows, day_rows, trade_rows, meta = [], [], [], {"pair": pair, "folds": [{"train": [f["train"][0], f["train"][-1]], "val": [f["val"][0], f["val"][-1]]} for f in folds]}

    for fee in fees:
        convergence = cfg.pairs[pair].type in CONV_DIRECTIONS
        trigger = (4 if convergence else 2) * fee  # gross edge must cover every fill's fee
        days = {}
        offset_aware = offset_aware and not convergence
        ecol = "edge_rel_bps" if offset_aware else "edge_birth_bps"
        for d in dev_dates:
            got = load_day(cfg, pair, d, trigger)
            if got is not None:
                if offset_aware:  # fire only when the gap beats fees relative to the usual offset
                    e, legs = got
                    got = (e[e.edge_rel_bps > trigger].reset_index(drop=True), legs)
                if len(got[0]):
                    days[d] = got
        print(f"  fee {fee} bps/leg: {sum(len(e) for e, _ in days.values()):,} triggers over {len(days)} days", flush=True)

        # Measure the slow path's real inference latency once (it sets how long the slow path waits).
        first = folds[0]["train"]
        X0 = pd.concat([days[d][0] for d in first if d in days], ignore_index=True)
        # Labels at 10 ms: at 0 ms every optimistic trigger fills, which leaves nothing to learn.
        y0 = pd.concat([replay_day(days[d][0], days[d][1], 10, fee, "optimistic") for d in first if d in days]).full_fill.to_numpy()
        fast_ms, slow_ms = measure_latencies(FastPrior().fit(X0, y0), SlowModel().fit(X0, y0), X0)
        delta = float(np.ceil(slow_ms * 100) / 100) if slow_wait_ms is None else float(slow_wait_ms)  # measured, rounded up to 10 µs
        meta.setdefault("latency_ms", {})[str(fee)] = {"fast_prior": fast_ms, "slow_model": slow_ms, "slow_wait_used": delta}
        print(f"  measured inference: fast prior {fast_ms * 1000:.1f} µs, compiled slow model {slow_ms * 1000:.1f} µs -> slow path waits {delta} ms", flush=True)

        for mode in MODES:
            out = {d: {t: replay_day(e, legs, t, fee, mode) for t in TAUS_MS} for d, (e, legs) in days.items()}
            # Slow path: decides delta ms after the trigger, re-reads the book, trades only if the gap
            # still covers fees, priced at the quotes seen then.
            out_slow = {d: {t: replay_day(e, legs, t, fee, mode, decide_after_ms=delta) for t in TAUS_MS}
                        for d, (e, legs) in days.items()}
            for k, fold in enumerate(folds):
                tr = [d for d in fold["train"] if d in days]
                va = [d for d in fold["val"] if d in days]
                if len(tr) < 3 or not va:
                    continue
                cut = max(1, int(len(tr) * 0.7))
                fit_d, cal_d = tr[:cut], tr[cut:] or tr[-1:]
                cat = lambda ds: pd.concat([days[d][0] for d in ds], ignore_index=True)
                res = lambda ds, t: pd.concat([out[d][t] for d in ds], ignore_index=True)

                def res_slow(ds, t):
                    r = pd.concat([out_slow[d][t] for d in ds], ignore_index=True)
                    still = r.edge_dec_bps.to_numpy() > trigger  # gap vanished during inference: skip
                    for c in ("pnl", "pnl_bps"):
                        r[c] = np.where(still, r[c], 0.0)
                    r["full_fill"] = r.full_fill & still
                    r["still_open"] = still
                    return r
                Xfit, Xcal, Xval = cat(fit_d), cat(cal_d), cat(va)
                for tau in TAUS_MS:
                    fit_now, fit_slow = res(fit_d, tau), res_slow(fit_d, tau)
                    yf, yfd = fit_now.full_fill.to_numpy(), fit_slow.full_fill.to_numpy()
                    if yf.all() or not yf.any() or yfd.all() or not yfd.any():
                        continue
                    fast, slow = FastPrior().fit(Xfit, yf), SlowModel().fit(Xfit, yfd)
                    L_now = miss_loss_bps(fit_now)
                    L_slow = miss_loss_bps(fit_slow[fit_slow.still_open])
                    if convergence:  # payoff of a fill is learned: it depends on the later reversion
                        e_fit = Xfit.edge_birth_bps.to_numpy()
                        g_now = fit_gain(e_fit, fit_now)
                        open_ = fit_slow.still_open.to_numpy()
                        g_slow = fit_gain(e_fit[open_], fit_slow[open_])
                    else:  # cross-venue: a full fill locks in the edge minus fees
                        g_now = g_slow = (-trigger, 1.0)

                    cal_slow = res_slow(cal_d, tau)
                    cal_f = Calibrator().fit(fast.predict(Xcal), res(cal_d, tau).full_fill.to_numpy())
                    cal_s = Calibrator().fit(slow.predict(Xcal), cal_slow.full_fill.to_numpy())
                    q_fast = lambda X: cal_f.transform(fast.predict(X))
                    q_slow = lambda X: cal_s.transform(slow.predict(X))
                    ev_cal_f = expected_value_gain(q_fast(Xcal), Xcal[ecol].to_numpy(), g_now, L_now)
                    ev_cal_s = expected_value_gain(q_slow(Xcal), Xcal[ecol].to_numpy(), g_slow, L_slow)
                    lo, hi = choose_margins(ev_cal_f, res(cal_d, tau).pnl.to_numpy(), cal_slow.pnl.to_numpy(),
                                            (ev_cal_s > 0) & cal_slow.still_open.to_numpy())

                    edge = Xval[ecol].to_numpy()
                    ev_f = expected_value_gain(q_fast(Xval), edge, g_now, L_now)
                    now, later = res(va, tau), res_slow(va, tau)
                    ev_s = np.where(later.still_open, expected_value_gain(q_slow(Xval), edge, g_slow, L_slow), -np.inf)
                    act = ev_f > hi
                    ask = (ev_f >= lo) & ~act
                    choices = {
                        "naive fast path": (np.ones(len(now), bool), now),
                        "fast path + decay prior": (ev_f > 0, now),
                        "slow model always": (ev_s > 0, later),
                        "latency-aware cascade": None,
                    }
                    for name, ch in choices.items():
                        if ch is None:
                            pnl = np.where(act, now.pnl, 0.0) + np.where(ask & (ev_s > 0), later.pnl, 0.0)
                            traded = act | (ask & (ev_s > 0))
                            full = np.where(act, now.full_fill, later.full_fill)
                            slow_share = float((ask).mean())
                            hedged = np.where(act, now.hedged, later.hedged)
                            waited = np.where(act, 0.0, delta)
                        else:
                            take, o = ch
                            pnl = np.where(take, o.pnl, 0.0)
                            traded = take
                            full = o.full_fill.to_numpy()
                            slow_share = 1.0 if name == "slow model always" else 0.0
                            hedged = o.hedged.to_numpy()
                            waited = np.full(len(o), delta if o is later else 0.0)
                        if dump_trades and tau in DUMP_TAUS_MS and not convergence:
                            # Position change on leg a: selling there (sell_a_buy_b) leaves a short on a.
                            sign = np.where(Xval.direction.to_numpy() == "sell_a_buy_b", -1.0, 1.0)
                            fill_t = Xval.birth_ts.to_numpy() + np.round((waited + tau) * 1000).astype(np.int64)
                            tk = np.asarray(traded, bool)
                            trade_rows.append(pd.DataFrame({
                                "fee_bps_per_leg": fee, "mode": mode, "fold": k, "tau_ms": tau, "strategy": name,
                                "date": Xval.date.to_numpy()[tk], "t": fill_t[tk], "dq_a": (sign * hedged)[tk],
                                "pnl": np.asarray(pnl, float)[tk]}))
                        rows.append({"fee_bps_per_leg": fee, "mode": mode, "fold": k, "tau_ms": tau, "strategy": name,
                                     "val_days": len(va), "triggers": len(now), "trades": int(traded.sum()),
                                     "pnl_usd": float(np.sum(pnl)), "full_fill_rate": float(full[traded].mean()) if traded.any() else np.nan,
                                     "slow_share": slow_share, "margins": [lo, hi]})
                        per_day = pd.DataFrame({"date": Xval.date.to_numpy(), "pnl": np.asarray(pnl, float),
                                                "trades": np.asarray(traded, int)}).groupby("date").sum()
                        for day, r in per_day.iterrows():
                            day_rows.append({"fee_bps_per_leg": fee, "mode": mode, "fold": k, "tau_ms": tau,
                                             "strategy": name, "date": day, "pnl_usd": float(r.pnl), "trades": int(r.trades)})
                    # Ceiling for reference: trade exactly the triggers that turned out profitable at tau.
                    rows.append({"fee_bps_per_leg": fee, "mode": mode, "fold": k, "tau_ms": tau, "strategy": "hindsight ceiling",
                                 "val_days": len(va), "triggers": len(now), "trades": int((now.pnl > 0).sum()),
                                 "pnl_usd": float(now.pnl.clip(lower=0).sum()), "full_fill_rate": np.nan,
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
                  pnl_usd=("pnl_usd", "sum"), full_fill_rate=("full_fill_rate", "mean"), slow_share=("slow_share", "mean"))
             .reset_index())
    agg["pnl_per_day_usd"] = agg.pnl_usd / agg.val_days
    agg.to_csv(out_dir / "pnl_vs_latency.csv", index=False)
    return agg


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pair", default="btc_perp_binance_bybit")
    ap.add_argument("--fees", nargs="*", type=float, default=[1.0, 0.0, 2.5])
    ap.add_argument("--slow-wait-ms", type=float, default=None,
                    help="override the measured slow-model latency (e.g. 1.0 for a compiled model)")
    ap.add_argument("--tag", default="", help="suffix for the output folder")
    ap.add_argument("--offset-aware", action="store_true",
                    help="cross pairs: measure gaps against the venues' trailing offset, not zero")
    ap.add_argument("--dump-trades", action="store_true",
                    help="write every trade at 1, 10 and 50 ms to trades.parquet (for analysis/inventory_check.py)")
    args = ap.parse_args()
    cfg = load_config()
    agg = run(args.pair, args.fees, cfg.reports_dir / "pnl" / f"{args.pair}{args.tag}", args.slow_wait_ms,
              args.dump_trades, args.offset_aware)
    show = agg[agg.fee_bps_per_leg == args.fees[0]].pivot_table(index=["mode", "tau_ms"], columns="strategy", values="pnl_per_day_usd")
    print(show.round(1).to_string())


if __name__ == "__main__":
    main()
