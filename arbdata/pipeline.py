"""Orchestration: raw files -> clean L1 -> aligned pairs -> labelled episodes -> splits."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from . import splits as splits_mod
from .align import align
from .config import Config
from .download import RAW_EXT
from .episodes import label_pair_day
from .normalize import NORMALIZERS, normalize_bybit_trades
from .quality import assess, clean, down_windows, trade_consistency


def _write_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=1))


SIZE_COLUMNS = ("bid_sz", "ask_sz", "bid_sz_min", "ask_sz_min", "bid_depth5", "ask_depth5")


def quality_path(cfg: Config, stream_key: str, date: str) -> Path:
    return cfg.reports_dir / "quality" / stream_key / f"{date}.json"


def normalize_day(cfg: Config, stream_key: str, date: str, force: bool = False) -> dict | None:
    stream = cfg.streams[stream_key]
    raw = cfg.raw_path(stream, date, RAW_EXT[stream.source])
    out = cfg.l1_path(stream, date)
    qpath = quality_path(cfg, stream_key, date)
    if out.exists() and qpath.exists() and not force:
        report = json.loads(qpath.read_text())
    elif raw.exists():
        df, feed = NORMALIZERS[stream.source](raw)
        if stream.contract_size:  # sizes quoted in contracts (OKX swaps) -> base units
            for c in SIZE_COLUMNS:
                if c in df:
                    df[c] = df[c] * stream.contract_size
        df, dropped = clean(df, cfg.quality["spike_bps"])
        src = cfg.sources[stream.source]
        silences = feed.silences_frame()
        report = {"stream": stream_key, "date": date, "dropped": dropped,
                  **assess(df, silences, feed.first_ts, feed.last_ts, feed.n, day_start_us(date), src["max_gap_ms"]),
                  "raw_out_of_order": feed.out_of_order}
        out.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(out, compression="zstd", index=False)
        silences.to_parquet(silences_path(cfg, stream_key, date), index=False)
    else:
        return None
    report = _add_trades(cfg, stream_key, date, report, force)
    report["passes"] = _passes(cfg, report)
    _write_json(qpath, report)
    return report


def _add_trades(cfg: Config, stream_key: str, date: str, report: dict, force: bool) -> dict:
    """Normalize the day's independent trade record and check the book against it."""
    stream = cfg.streams[stream_key]
    raw = cfg.trades_raw_path(stream, date)
    out = cfg.trades_path(stream, date)
    if stream.source not in ("bybit_ob", "bybit_live") or not raw.exists():
        return report
    if "trades" in report and out.exists() and not force:
        return report
    trades = normalize_bybit_trades(raw, stream.market)
    out.parent.mkdir(parents=True, exist_ok=True)
    trades.to_parquet(out, compression="zstd", index=False)
    report["trades"] = trade_consistency(pd.read_parquet(cfg.l1_path(stream, date)), trades)
    return report


def _passes(cfg: Config, report: dict) -> bool:
    ok = report.get("coverage", 0.0) >= cfg.quality["min_coverage"]
    t = report.get("trades", {})
    if "longest_anomaly_run_min" in t:
        q = cfg.quality
        ok = ok and t["longest_anomaly_run_min"] <= q["max_anomaly_run_min"] \
            and t["anomalous_minute_share"] <= q["max_anomalous_minute_share"] \
            and abs(t["best_shift_ms"]) <= q["max_clock_shift_ms"]
    return bool(ok)


def load_trades(cfg: Config, stream_key: str, date: str) -> pd.DataFrame | None:
    path = cfg.trades_path(cfg.streams[stream_key], date)
    return pd.read_parquet(path) if path.exists() else None


def day_start_us(date: str) -> int:
    return int(pd.Timestamp(date, tz="UTC").value // 1000)


def silences_path(cfg: Config, stream_key: str, date: str) -> Path:
    return cfg.l1_path(cfg.streams[stream_key], date).with_suffix(".silences.parquet")


def leg_down_windows(cfg: Config, stream_key: str, date: str, report: dict):
    return down_windows(pd.read_parquet(silences_path(cfg, stream_key, date)), report.get("last_raw_ts"),
                        day_start_us(date), cfg.source_cfg(stream_key)["max_gap_ms"])


def episodes_day(cfg: Config, pair_name: str, date: str, force: bool = False) -> dict:
    pair = cfg.pairs[pair_name]
    out = cfg.episodes_path(pair_name, date)
    summary_path = cfg.reports_dir / "episodes" / pair_name / f"{date}.json"
    if out.exists() and summary_path.exists() and not force:
        return json.loads(summary_path.read_text())
    legs, downs = [], []
    for key in (pair.a, pair.b):
        q = quality_path(cfg, key, date)
        if not q.exists():
            return {"pair": pair_name, "date": date, "status": "no_data", "detail": key}
        rep = json.loads(q.read_text())
        if not rep["passes"]:
            summary = {"pair": pair_name, "date": date, "status": "excluded",
                       "detail": f"{key} coverage {rep['coverage']:.3f} below threshold"}
            _write_json(summary_path, summary)
            return summary
        legs.append(pd.read_parquet(cfg.l1_path(cfg.streams[key], date)))
        downs.append(leg_down_windows(cfg, key, date, rep))

    al = align(legs[0], legs[1], downs[0], downs[1])
    hurdles = {f"gross>{h:g}bps": float(h) for h in cfg.episodes["hurdles_bps"]}
    if cfg.episodes.get("retail_taker_hurdle"):
        hurdles["retail_taker"] = cfg.retail_hurdle_bps(pair)
    leg_res = (cfg.source_cfg(pair.a)["resolution_ms"], cfg.source_cfg(pair.b)["resolution_ms"])
    trades = (load_trades(cfg, pair.a, date), load_trades(cfg, pair.b, date))
    ep = label_pair_day(al, pair, date, hurdles, cfg.resolution_ms(pair), cfg.episodes, cfg.features,
                        leg_resolution_ms=leg_res, trades=trades)
    out.parent.mkdir(parents=True, exist_ok=True)
    ep.to_parquet(out, compression="zstd", index=False)

    counts = {}
    if not ep.empty:
        g = ep.groupby(["hurdle_name", "direction"])
        counts = {f"{h}|{d}": {"n": int(len(x)), "died_share": float(x.died.mean()),
                               "median_obs_ms": float(x.obs_ms.median()),
                               "sub_resolution_share": float(x.sub_resolution.mean()),
                               "resolved_median_obs_ms": float(x.obs_ms[~x.sub_resolution].median())
                               if (~x.sub_resolution).any() else float("nan"),
                               "stale_share": float(x.stale_birth.mean()),
                               "stale_partner_share": float(x.stale_partner.mean())}
                  for (h, d), x in g}
    summary = {"pair": pair_name, "date": date, "status": "ok", "events": int(len(al)),
               "valid_share": float(al.valid.mean()), "episodes": int(len(ep)), "by_hurdle": counts}
    _write_json(summary_path, summary)
    return summary


def episode_dates(cfg: Config) -> list[str]:
    root = cfg.data_root / "episodes"
    return sorted({p.stem for p in root.glob("*/*.parquet")}) if root.exists() else []


def build_splits(cfg: Config, force: bool = False) -> dict:
    s = cfg.splits
    proposed = splits_mod.make_splits(episode_dates(cfg), s["holdout_fraction"], s["min_holdout_days"],
                                      s["embargo_days"], s["n_folds"], splits_mod.cross_window())
    return splits_mod.save_frozen(proposed, cfg.splits_path, force=force)
