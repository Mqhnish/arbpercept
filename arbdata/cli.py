"""Command line: arbdata {download,normalize,episodes,splits,report,build}."""

from __future__ import annotations

import argparse
import json
import sys

import numpy as np

from . import pipeline
from .config import load_config
from .download import candidate_urls, date_range, download, download_trades

REGIME_STREAM = "bybit_ob/bybit/BTC-USDT/perp"


def _streams(cfg, sources, filters):
    out = []
    for s in cfg.streams.values():
        if sources and s.source not in sources:
            continue
        if filters and not any(f in s.key for f in filters):
            continue
        out.append(s)
    return out


def cmd_download(cfg, args):
    streams = _streams(cfg, args.source, args.filter)
    dates = date_range(args.start, args.end)
    if args.dry_run:
        for d in dates:
            for s in streams:
                print(d, s.key, " | ".join(candidate_urls(s, d)))
        return
    if args.trades:
        download_trades(cfg, streams, dates)
    else:
        download(cfg, streams, dates)


def cmd_normalize(cfg, args):
    for d in date_range(args.start, args.end):
        for s in _streams(cfg, args.source, args.filter):
            rep = pipeline.normalize_day(cfg, s.key, d, force=args.force)
            if rep:
                flag = "ok " if rep["passes"] else "LOW"
                print(f"{d} {s.key}: {flag} rows={rep['rows']:,} coverage={rep['coverage']:.3f} "
                      f"resyncs={rep['resyncs']} dropped={rep['dropped']}", flush=True)


def cmd_episodes(cfg, args):
    pairs = args.pair or sorted(cfg.pairs)
    for d in date_range(args.start, args.end):
        for p in pairs:
            s = pipeline.episodes_day(cfg, p, d, force=args.force)
            if s["status"] == "no_data":
                continue
            print(f"{d} {p}: {s['status']} episodes={s.get('episodes', 0):,} {s.get('detail', '')}".rstrip(), flush=True)


def cmd_splits(cfg, args):
    try:
        s = pipeline.build_splits(cfg, force=args.force)
    except ValueError as exc:
        print(f"splits not created: {exc}")
        return
    print(f"development={len(s['development'])} embargo={len(s['embargo'])} holdout={len(s['holdout'])} "
          f"folds={len(s['folds'])} after_freeze={len(s.get('arrived_after_freeze', []))}")


def _load_reports(cfg, kind):
    root = cfg.reports_dir / kind
    return [json.loads(p.read_text()) for p in sorted(root.glob("**/*.json"))] if root.exists() else []


def _trade_cells(r):
    t = r.get("trades")
    if not t or "in_band_share" not in t:
        return "no trade record | - | -"
    return f"{t['in_band_share']:.1%} | {t['longest_anomaly_run_min']} | {t['best_shift_ms']}"


def _development_summary(cfg, dev_dates):
    """Pooled lifetimes over development dates only, per pair and hurdle."""
    import pandas as pd
    cols = ["pair", "date", "hurdle_name", "obs_ms", "died", "sub_resolution", "stale_birth", "stale_partner"]
    frames = [pd.read_parquet(p, columns=cols)
              for p in sorted((cfg.data_root / "episodes").glob("*/*.parquet")) if p.stem in set(dev_dates)]
    if not frames:
        return []
    df = pd.concat(frames, ignore_index=True)
    df = df[~df.stale_birth]
    out = ["", "## Development data, pooled", "",
           "Holdout days are excluded. Stale births are dropped. Lifetimes are shown only for episodes "
           "longer than the pair's sampling step; shorter ones are known only to within it.", "",
           "Fresh partner = every sampled leg's quote was less than half a step old at the birth: the cleanest labels.", "",
           "| Pair | Hurdle | Days | Episodes per day | Shorter than resolution | Resolved life median / p90 (ms) "
           "| Fresh-partner births per day | Fresh: shorter than resolution | Fresh: resolved life median (ms) |",
           "|---|---|---|---|---|---|---|---|---|"]

    def life(x):
        res = x.obs_ms[~x.sub_resolution]
        return res, (f"{res.median():,.0f} / {res.quantile(0.9):,.0f}" if len(res) else "none resolved")

    for (pair, h), g in df.groupby(["pair", "hurdle_name"]):
        days = g.date.nunique()
        fresh = g[~g.stale_partner]
        fres, _ = life(fresh)
        fmed = f"{fres.median():,.0f}" if len(fres) else "none resolved"
        fsub = f"{fresh.sub_resolution.mean():.0%}" if len(fresh) else "-"
        out.append(f"| {pair} | {h} | {days} | {len(g) / days:,.0f} | {g.sub_resolution.mean():.0%} | {life(g)[1]} "
                   f"| {len(fresh) / days:,.1f} | {fsub} | {fmed} |")
    return out


def cmd_report(cfg, args):
    lines = ["# Dataset report", ""]
    q = _load_reports(cfg, "quality")
    lines += ["## Stream quality", "",
              "Trade check: Bybit's independent trade record against the reconstructed book. In band = share of trades "
              "printing between the bracketing snapshots' quotes; sweeps beyond the band are normal on volatile days. "
              "A day fails on persistence (5+ consecutive minutes where most trades miss the book) or a clock offset over 20 ms.", "",
              "| Date | Stream | Rows | Coverage | Longest raw silence (s) | Resyncs | Feed lag p50/p99 (ms) | Spread p50 (bps) | Daily RV (bps) | Trades in band | Longest anomaly (min) | Clock offset (ms) | Passes |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in sorted(q, key=lambda r: (r["date"], r["stream"])):
        lines.append(f"| {r['date']} | {r['stream']} | {r['rows']:,} | {r['coverage']:.3f} | {r['max_raw_silence_s']:.1f} | "
                     f"{r['resyncs']} | {r['feed_lag_ms_median']:.1f} / {r['feed_lag_ms_p99']:.1f} | "
                     f"{r['spread_bps_median']:.2f} | {r['daily_rv_bps']:.0f} | {_trade_cells(r)} | {'yes' if r['passes'] else 'NO'} |")

    e = _load_reports(cfg, "episodes")
    splits = json.loads(cfg.splits_path.read_text()) if cfg.splits_path.exists() else None
    # Label statistics of holdout days are never printed: looking at them is peeking at the test set.
    hidden = set(splits["holdout"]) if splits else set()
    if splits:
        lines += _development_summary(cfg, splits["development"])
    lines += ["", "## Episodes by day", "",
              "| Date | Pair | Status | Valid share | Hurdle | Episodes | Observed deaths | Shorter than resolution | Median life, resolved only (ms) | Stale births | Stale partner |",
              "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in sorted(e, key=lambda r: (r["date"], r["pair"])):
        if r["date"] in hidden:
            lines.append(f"| {r['date']} | {r['pair']} | holdout: label statistics hidden | | | | | | | | |")
            continue
        if r["status"] != "ok":
            lines.append(f"| {r['date']} | {r['pair']} | {r['status']}: {r.get('detail', '')} | | | | | | | | |")
            continue
        by_h: dict[str, list] = {}
        for k, v in r["by_hurdle"].items():
            by_h.setdefault(k.split("|")[0], []).append(v)
        for h, vs in sorted(by_h.items()):
            n = sum(v["n"] for v in vs)
            died = sum(v["n"] * v["died_share"] for v in vs) / n
            stale = sum(v["n"] * v["stale_share"] for v in vs) / n
            sub = sum(v["n"] * v["sub_resolution_share"] for v in vs) / n
            resolved = [v["resolved_median_obs_ms"] for v in vs if v["resolved_median_obs_ms"] == v["resolved_median_obs_ms"]]
            med = f"{np.median(resolved):,.0f}" if resolved else "none resolved"
            partner = sum(v["n"] * v.get("stale_partner_share", float("nan")) for v in vs) / n
            lines.append(f"| {r['date']} | {r['pair']} | ok | {r['valid_share']:.3f} | {h} | {n:,} | "
                         f"{died:.1%} | {sub:.0%} | {med} | {stale:.1%} | {partner:.0%} |")

    if splits:
        s = splits
        rv = {r["date"]: r["daily_rv_bps"] for r in q if r["stream"] == REGIME_STREAM}
        lines += ["", "## Splits", "",
                  f"Holdout window {s['window']['holdout_start']} to {s['window']['holdout_end']}, frozen "
                  f"{s['created_utc']} (fingerprint {s['holdout_sha']}). Embargo from {s['window']['embargo_start']}.", "",
                  "| Split | Dates | Range | Daily RV of BTC perp, min / median / max (bps) |", "|---|---|---|---|"]
        for name in ("development", "embargo", "holdout"):
            ds = s[name]
            vals = [rv[d] for d in ds if d in rv]
            rng = f"{ds[0]} to {ds[-1]}" if ds else "-"
            stats = f"{min(vals):.0f} / {np.median(vals):.0f} / {max(vals):.0f}" if vals else "-"
            lines.append(f"| {name} | {len(ds)} | {rng} | {stats} |")
        dev = [rv[d] for d in s["development"] if d in rv]
        hold = [rv[d] for d in s["holdout"] if d in rv]
        if dev and hold and (max(hold) > 1.2 * max(dev) or min(hold) < min(dev) / 1.2):
            lines += ["", "**Warning:** the holdout contains volatility outside the development range. "
                      "Results on it test extrapolation, not just generalisation."]
        lines += ["", f"{len(s['folds'])} walk-forward folds inside development."]
        if s.get("arrived_after_freeze"):
            lines += [f"{len(s['arrived_after_freeze'])} dates arrived after the freeze and are in no split."]

    out = cfg.reports_dir / "REPORT.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n")
    print(f"wrote {out}")


def cmd_record(cfg, args):
    import asyncio
    from .recorder import record
    stats = asyncio.run(record(cfg, args.minutes))
    for topic, n in sorted(stats.items()):
        print(f"{topic}: {n:,} messages")


def cmd_build(cfg, args):
    cmd_normalize(cfg, args)
    cmd_episodes(cfg, args)
    cmd_splits(cfg, argparse.Namespace(force=False))
    cmd_report(cfg, args)


def main(argv: list[str] | None = None) -> None:
    p = argparse.ArgumentParser(prog="arbdata")
    p.add_argument("--config", default=None)
    sub = p.add_subparsers(dest="cmd", required=True)

    def dated(sp):
        sp.add_argument("--start", required=True)
        sp.add_argument("--end", required=True)

    def streamsel(sp):
        sp.add_argument("--source", action="append", help="bybit_ob, binance_bt or tardis (repeatable)")
        sp.add_argument("--filter", action="append", help="substring of a stream key (repeatable)")

    sp = sub.add_parser("download"); dated(sp); streamsel(sp); sp.add_argument("--dry-run", action="store_true")
    sp.add_argument("--trades", action="store_true", help="download Bybit's public trade archive instead of order books")
    sp = sub.add_parser("normalize"); dated(sp); streamsel(sp); sp.add_argument("--force", action="store_true")
    sp = sub.add_parser("episodes"); dated(sp); sp.add_argument("--pair", action="append"); sp.add_argument("--force", action="store_true")
    sp = sub.add_parser("splits"); sp.add_argument("--force", action="store_true", help="move the holdout (only before any evaluation)")
    sub.add_parser("report")
    sp = sub.add_parser("record", help="record Bybit's live 10 ms book and trades (see arbdata/recorder.py)")
    sp.add_argument("--minutes", type=float, default=None, help="stop after this long (default: run until stopped)")
    sp = sub.add_parser("build"); dated(sp); streamsel(sp); sp.add_argument("--pair", action="append"); sp.add_argument("--force", action="store_true")

    args = p.parse_args(argv)
    cfg = load_config(args.config)
    {"download": cmd_download, "normalize": cmd_normalize, "episodes": cmd_episodes,
     "splits": cmd_splits, "report": cmd_report, "build": cmd_build, "record": cmd_record}[args.cmd](cfg, args)


if __name__ == "__main__":
    sys.exit(main())
