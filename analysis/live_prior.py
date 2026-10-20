"""Retrain the decay prior on the current market, from our own Binance + Bybit recordings.

    .venv/bin/python analysis/live_prior.py 2026-10-19 2026-10-20 [--trigger 1.0]

The paper engine replays the recordings with each venue's measured latency (Binance ~50 ms,
Bybit ~8 ms from this machine), trades every trigger and records the features it saw and
whether both legs filled. Split strictly by time: the prior is fitted on the first 70% of
triggers and tested on the last 30%. Reported per fee level: P&L of trading every trigger
against trading only when the prior's expected value is positive. The prior refitted on
all triggers is saved for the live demo (data/reports/live/prior_live_<asset>.json).
"""

from __future__ import annotations

import argparse
import json

import pandas as pd
from sklearn.metrics import roc_auc_score

from arbdata.config import load_config
from arbtrade.live import PaperEngine, replay_events
from arbtrade.policies import FAST_FEATURES, FastPrior

LAT = {"binance": 50.0, "bybit": 8.0}
FEES = [0.0, 0.5, 1.0, 2.5]


def collect(cfg, dates, asset, trigger):
    eng = PaperEngine(("binance", "bybit"), trigger, 0.0, LAT)
    for t, v, bid, ask, bsz, asz in replay_events(cfg, dates, asset):
        eng.on_quote(v, int(t), bid, ask, bsz, asz)
    rows = []
    for tr in eng.trades:
        if not tr.settled:
            continue
        notional = sum(o.filled * o.price for o in tr.orders + tr.unwind if o.filled > 0)
        rows.append({"t": tr.t, **tr.features, "full": all(o.filled >= o.qty - 1e-12 for o in tr.orders),
                     "gross": tr.pnl, "traded_notional": notional,
                     "intended": tr.orders[0].qty * tr.orders[0].limit})
    return pd.DataFrame(rows).sort_values("t").reset_index(drop=True)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("dates", nargs="+")
    ap.add_argument("--trigger", type=float, default=1.0)
    args = ap.parse_args()
    cfg = load_config()
    out_dir = cfg.reports_dir / "live"
    out_dir.mkdir(parents=True, exist_ok=True)
    lines = [f"# Decay prior on the current market ({', '.join(args.dates)})", "",
             f"Trigger {args.trigger} bps, latencies Binance {LAT['binance']:.0f} ms / Bybit {LAT['bybit']:.0f} ms, "
             "$10k per trade, train on the first 70% of triggers in time, test on the last 30%.", ""]
    for asset in ("BTC", "ETH"):
        df = collect(cfg, args.dates, asset, args.trigger)
        if len(df) < 50 or df.full.all() or not df.full.any():
            lines.append(f"## {asset}: only {len(df)} triggers, not enough to train")
            continue
        cut = int(len(df) * 0.7)
        tr, te = df.iloc[:cut], df.iloc[cut:]
        hours = (df.t.iloc[-1] - df.t.iloc[0]) / 3.6e9
        prior = FastPrior().fit(tr, tr.full.to_numpy())
        q_te = prior.predict(te)
        auc = roc_auc_score(te.full, q_te) if 0 < te.full.sum() < len(te) else float("nan")
        gap_auc = roc_auc_score(te.full, te.edge_birth_bps) if 0 < te.full.sum() < len(te) else float("nan")
        lines += [f"## {asset}", "",
                  f"{len(df):,} triggers over {hours:.1f} h; {df.full.mean():.0%} filled on both legs. "
                  f"Test AUC {auc:.2f} (gap size alone {gap_auc:.2f}).", "",
                  "| Fee per leg (bps) | Trade every trigger | Prior-gated | Trades taken by the prior |", "|---|---|---|---|"]
        for fee in FEES:
            net_tr = tr.gross - fee / 1e4 * tr.traded_notional
            net_te = te.gross - fee / 1e4 * te.traded_notional
            miss = net_tr[~tr.full] / tr.intended[~tr.full] * 1e4
            loss = float(miss.mean()) if len(miss) else 0.0
            ev = q_te * (te.edge_birth_bps - 2 * fee) + (1 - q_te) * loss
            take = ev > 0
            lines.append(f"| {fee:g} | ${net_te.sum():,.0f} | ${net_te[take].sum():,.0f} | {int(take.sum())} of {len(te)} |")
        full_prior = FastPrior().fit(df, df.full.to_numpy())
        net_all = df.gross - 1.0 / 1e4 * df.traded_notional
        miss_all = net_all[~df.full] / df.intended[~df.full] * 1e4
        (out_dir / f"prior_live_{asset}.json").write_text(json.dumps({
            "median": full_prior.median.tolist(), "mu": full_prior.mu.tolist(), "sd": full_prior.sd.tolist(),
            "w": full_prior.w.tolist(), "b": float(full_prior.b), "loss_bps": float(miss_all.mean()),
            "trained_on": f"live {asset} perpetual Binance vs Bybit, {len(df):,} triggers, {', '.join(args.dates)}",
            "features": FAST_FEATURES, "latency_ms": LAT, "fee_bps": 1.0, "full_fill_rate": float(df.full.mean())}, indent=1))
        lines.append("")
    (out_dir / "live_prior.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
