"""Cross-venue decay at full resolution, from our own Binance + Bybit recordings.

    .venv/bin/python analysis/live_cross_check.py 2026-10-19 [--asset BTC]

Both legs are stamped by the same receive clock, so this is what an observer at this machine
saw: Binance changes at every tick, Bybit level 1 at about 10 ms. Reports births per hour,
the share still open after 10/50/100/200/500 ms, and each venue's feed latency to us.
Uses only the hours the recorder covered; the first five minutes after it starts are warm-up.
"""

from __future__ import annotations

import argparse

from arbdata import pipeline as P
from arbdata.align import align
from arbdata.config import load_config
from arbdata.episodes import label_pair_day
from arbdata.normalize import NORMALIZERS
from arbdata.quality import clean, down_windows

HURDLES = {"gross>1bps": 1.0, "gross>2bps": 2.0, "gross>5bps": 5.0, "gross>10bps": 10.0}
AT_MS = [10, 50, 100, 200, 500]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("date")
    ap.add_argument("--asset", default="BTC")
    args = ap.parse_args()
    cfg = load_config()
    pair = cfg.pairs[f"live_{args.asset.lower()}_perp_binance_bybit"]
    legs, downs, lags = [], [], {}
    for key in (pair.a, pair.b):
        stream = cfg.streams[key]
        df, feed = NORMALIZERS[stream.source](cfg.raw_path(stream, args.date, ""))
        df, _ = clean(df, cfg.quality["spike_bps"])
        legs.append(df)
        downs.append(down_windows(feed.silences_frame(), feed.last_ts, P.day_start_us(args.date),
                                  cfg.source_cfg(key)["max_gap_ms"]))
        lag = (df.avail_ts - df.exch_ts) / 1000
        lags[stream.venue] = (float(lag.median()), float(lag.quantile(0.99)), len(df))
    lo = max(int(l.avail_ts.min()) for l in legs)
    hi = min(int(l.avail_ts.max()) for l in legs)
    legs = [l[(l.avail_ts >= lo) & (l.avail_ts <= hi)] for l in legs]
    al = align(legs[0], legs[1], downs[0], downs[1])
    feats = {**cfg.features, "trade_windows_s": []}
    ep = label_pair_day(al, pair, args.date, HURDLES, 1, cfg.episodes, feats, leg_resolution_ms=(1, 10))
    ep = ep[ep.birth_ts >= lo + int(cfg.episodes["warmup_s"] * 1e6)]
    hours = (hi - lo - cfg.episodes["warmup_s"] * 1e6) / 3.6e9
    lines = [f"# Live cross-venue decay, {args.asset} perpetual, Binance vs Bybit, {args.date}", "",
             f"{hours:.2f} h after warm-up, one receive clock.", "",
             "| Venue | Quote changes | Feed latency to us, median / p99 (ms) |", "|---|---|---|"]
    lines += [f"| {v} | {n:,} | {m:.0f} / {p:.0f} |" for v, (m, p, n) in lags.items()]
    lines += ["", "| Hurdle | Births per hour | " + " | ".join(f"Open after {t} ms" for t in AT_MS) + " | Median life (ms) |",
              "|---|---|" + "---|" * len(AT_MS) + "---|"]
    for h in HURDLES:
        g = ep[(ep.hurdle_name == h) & ~ep.stale_birth]
        if g.empty:
            lines.append(f"| {h} | 0 |" + " - |" * len(AT_MS) + " - |")
            continue
        cells = [f"{(g.lower_ms >= t).mean():.0%}" for t in AT_MS]
        lines.append(f"| {h} | {len(g) / hours:,.0f} | " + " | ".join(cells) + f" | {g.obs_ms.median():,.0f} |")
    out = cfg.reports_dir / f"live_cross_{args.asset}_{args.date}.md"
    out.write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
