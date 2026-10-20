"""How much does Bybit's 100 ms archive distort opportunity lifetimes? Compare it with our own
10 ms live recording of the same hours.

    .venv/bin/python analysis/resolution_check.py 2026-10-19            # needs both sources for that date
    .venv/bin/python analysis/resolution_check.py 2026-10-20 --live-only # just sanity-check a live day

Both views are restricted to the hours the recorder covered. For each archive birth the
script looks for a live birth in the same direction within one archive step (100 ms):
  confirmed share     the archive opportunity also existed in 10 ms data
  live lifetime       how long confirmed ones really lasted
Split by the archive's own flags (sub_resolution, stale_partner), this measures directly how
many of the archive's short-lived episodes are real.
"""

from __future__ import annotations

import argparse
import json

import numpy as np
import pandas as pd

from arbdata import pipeline as P
from arbdata.align import align
from arbdata.config import load_config
from arbdata.episodes import label_pair_day
from arbdata.normalize import normalize_bybit_live
from arbdata.quality import clean, down_windows

HURDLES = {"gross>1bps": 1.0, "gross>2bps": 2.0, "gross>5bps": 5.0}


def live_legs(cfg, pair_name, date):
    spec = cfg.pairs[pair_name]
    legs, downs = [], []
    for key in (spec.a, spec.b):
        day_dir = cfg.raw_path(cfg.streams[key], date, "")
        df, feed = normalize_bybit_live(day_dir)
        df, _ = clean(df, cfg.quality["spike_bps"])
        legs.append(df)
        downs.append(down_windows(feed.silences_frame(), feed.last_ts, P.day_start_us(date), cfg.source_cfg(key)["max_gap_ms"]))
    return spec, legs, downs


def archive_legs(cfg, pair_name, date):
    spec = cfg.pairs[pair_name]
    legs, downs = [], []
    for key in (spec.a, spec.b):
        rep = P.normalize_day(cfg, key, date)
        if rep is None:
            raise SystemExit(f"no archive data for {key} on {date}: download it first")
        legs.append(pd.read_parquet(cfg.l1_path(cfg.streams[key], date)))
        downs.append(P.leg_down_windows(cfg, key, date, rep))
    return spec, legs, downs


def episodes(cfg, spec, legs, downs, date, res, lo, hi):
    legs = [l[(l.avail_ts >= lo) & (l.avail_ts <= hi)] for l in legs]
    al = align(legs[0], legs[1], downs[0], downs[1])
    feats = {**cfg.features, "trade_windows_s": []}
    ep = label_pair_day(al, spec, date, HURDLES, res, cfg.episodes, feats, leg_resolution_ms=(res, res))
    return ep[ep.birth_ts >= lo + int(cfg.episodes["warmup_s"] * 1e6)]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("date")
    ap.add_argument("--asset", default="BTC")
    ap.add_argument("--live-only", action="store_true")
    args = ap.parse_args()
    cfg = load_config()
    live_pair, arch_pair = f"live_{args.asset.lower()}_basis", f"bybit_{args.asset.lower()}_basis"

    spec_l, legs_l, downs_l = live_legs(cfg, live_pair, args.date)
    lo = max(int(l.avail_ts.min()) for l in legs_l)
    hi = min(int(l.avail_ts.max()) for l in legs_l)
    hours = (hi - lo) / 3.6e9
    live = episodes(cfg, spec_l, legs_l, downs_l, args.date, 10, lo, hi)
    step = np.median(np.diff(legs_l[1].avail_ts.to_numpy())) / 1000
    lines = [f"# Resolution check, {args.asset} spot vs perpetual, {args.date}", "",
             f"Live recording covers {hours:.1f} h (median perpetual update step {step:.0f} ms).", ""]
    summary = {"date": args.date, "hours": hours}
    if args.live_only:
        for h, g in live.groupby("hurdle_name"):
            lines.append(f"- {h}: {len(g):,} live births, {len(g) / hours:,.0f} per hour, "
                         f"median life {g.obs_ms.median():,.0f} ms, alive at 100 ms {(g.lower_ms >= 100).mean():.0%}")
    else:
        spec_a, legs_a, downs_a = archive_legs(cfg, arch_pair, args.date)
        arch = episodes(cfg, spec_a, legs_a, downs_a, args.date, 100, lo, hi)
        lines += ["| Hurdle | Archive births/h | Live births/h | Archive births confirmed live | "
                  "…of sub-resolution ones | …of stale-partner ones | Live life of confirmed sub-res births, median (ms) |",
                  "|---|---|---|---|---|---|---|"]
        for h in HURDLES:
            a, l = arch[arch.hurdle_name == h], live[live.hurdle_name == h]
            confirmed = np.zeros(len(a), bool)
            life = np.full(len(a), np.nan)
            for d in a.direction.unique():
                am, lm = (a.direction == d).to_numpy(), l[l.direction == d].sort_values("birth_ts")
                lt = lm.birth_ts.to_numpy()
                if not len(lt):
                    continue
                at = a.birth_ts.to_numpy()[am]
                j = np.clip(np.searchsorted(lt, at), 1, len(lt) - 1)
                near = np.where(np.abs(lt[j] - at) < np.abs(lt[j - 1] - at), j, j - 1)
                ok = np.abs(lt[near] - at) <= 100_000
                confirmed[np.flatnonzero(am)] = ok
                life[np.flatnonzero(am)] = np.where(ok, lm.obs_ms.to_numpy()[near], np.nan)
            sub, stale = a.sub_resolution.to_numpy(), a.stale_partner.to_numpy()
            med = np.nanmedian(life[sub & confirmed]) if (sub & confirmed).any() else float("nan")
            lines.append(f"| {h} | {len(a) / hours:,.0f} | {len(l) / hours:,.0f} | {confirmed.mean():.0%} | "
                         f"{confirmed[sub].mean() if sub.any() else float('nan'):.0%} | "
                         f"{confirmed[stale].mean() if stale.any() else float('nan'):.0%} | {med:,.0f} |")
            summary[h] = {"archive_per_h": len(a) / hours, "live_per_h": len(l) / hours,
                          "confirmed": float(confirmed.mean()),
                          "confirmed_sub_resolution": float(confirmed[sub].mean()) if sub.any() else None,
                          "confirmed_stale_partner": float(confirmed[stale].mean()) if stale.any() else None}
    out = cfg.reports_dir / f"resolution_check_{args.asset}_{args.date}.md"
    out.write_text("\n".join(lines) + "\n")
    (out.with_suffix(".json")).write_text(json.dumps(summary, indent=1))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
