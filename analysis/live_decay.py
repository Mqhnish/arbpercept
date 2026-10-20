"""First decay models trained on our own 10 ms / tick-level recordings (preliminary).

    .venv/bin/python analysis/live_decay.py 2026-10-19 2026-10-20

The recordings resolve lifetimes to ~10 ms, so survival at 50 and 100 ms can be labelled,
which the 100 ms archive cannot do. With only hours of data, the split is by hour: train on
the first hours, skip one hour (embargo), test on the last. Same models and metrics as
analysis/decay_pilot.py. These dates are after the frozen holdout window, so nothing here
touches it.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
import decay_pilot as D  # noqa: E402
from arbdata import pipeline as P  # noqa: E402
from arbdata.align import align  # noqa: E402
from arbdata.config import load_config  # noqa: E402
from arbdata.episodes import label_pair_day  # noqa: E402
from arbdata.normalize import NORMALIZERS  # noqa: E402
from arbdata.quality import clean, down_windows  # noqa: E402

PAIRS = ["live_btc_basis", "live_eth_basis", "live_btc_perp_binance_bybit", "live_eth_perp_binance_bybit"]
TAUS = [50, 100, 250, 500]


def pair_episodes(cfg, pair_name, date):
    pair = cfg.pairs[pair_name]
    legs, downs, res = [], [], []
    for key in (pair.a, pair.b):
        s = cfg.streams[key]
        path = cfg.raw_path(s, date, "")
        if not path.exists():
            return pd.DataFrame()
        df, feed = NORMALIZERS[s.source](path)
        df, _ = clean(df, cfg.quality["spike_bps"])
        if df.empty:
            return pd.DataFrame()
        legs.append(df)
        downs.append(down_windows(feed.silences_frame(), feed.last_ts, P.day_start_us(date), cfg.source_cfg(key)["max_gap_ms"]))
        res.append(cfg.source_cfg(key)["resolution_ms"])
    lo = max(int(l.avail_ts.min()) for l in legs)
    legs = [l[l.avail_ts >= lo] for l in legs]
    al = align(legs[0], legs[1], downs[0], downs[1])
    feats = {**cfg.features, "trade_windows_s": []}
    ep = label_pair_day(al, pair, date, {"gross>1bps": 1.0, "gross>2bps": 2.0}, max(res), cfg.episodes, feats,
                        leg_resolution_ms=tuple(res))
    if ep.empty:
        return ep
    return ep[(ep.birth_ts >= lo + int(cfg.episodes["warmup_s"] * 1e6)) & ~ep.stale_birth]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("dates", nargs="+")
    args = ap.parse_args()
    cfg = load_config()
    lines = ["# Decay models on our 10 ms recordings (preliminary)", "",
             "Hour-based split: train on the first hours, one-hour embargo, test on the last hours. "
             "AUC of P(still open after tau) on the test hours.", "",
             "| Pair | Births above 1 bps | Hours (train / test) | tau (ms) | Open after tau (test) | Boosted AUC | Logistic AUC | Gap size alone |",
             "|---|---|---|---|---|---|---|---|"]
    for pair in PAIRS:
        ep = pd.concat([pair_episodes(cfg, pair, d) for d in args.dates], ignore_index=True)
        ep = ep[ep.hurdle_name == "gross>1bps"].reset_index(drop=True)
        if len(ep) < 300:
            lines.append(f"| {pair} | {len(ep)} | not enough data | | | | | |")
            continue
        hour = ((ep.birth_ts - ep.birth_ts.min()) // 3_600_000_000).astype(int)
        ep["date"] = hour.map(lambda h: f"h{h:03d}")
        hours = sorted(ep.date.unique())
        n_test = max(1, round(len(hours) * 0.3))
        fold = {"train": hours[: len(hours) - n_test - 1], "val": hours[len(hours) - n_test:]}
        if not fold["train"]:
            lines.append(f"| {pair} | {len(ep)} | too few hours | | | | | |")
            continue
        for tau in TAUS:
            rows = pd.DataFrame(D.evaluate(ep, [fold], tau))
            if rows.empty:
                continue
            g = rows.set_index("model")
            lines.append(f"| {pair} | {len(ep):,} | {len(fold['train'])} / {len(fold['val'])} | {tau} | "
                         f"{g.val_alive_share.iloc[0]:.0%} | {g.loc['all features (gradient boosting)', 'auc']:.2f} | "
                         f"{g.loc['all features (logistic)', 'auc']:.2f} | {g.loc['gap size only (logistic)', 'auc']:.2f} |")
        print(pair, "done", flush=True)
    out = cfg.reports_dir / "live" / "live_decay.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
