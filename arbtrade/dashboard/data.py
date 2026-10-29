"""What the dashboard shows, read from data/reports/ (the committed results; no raw data needed).

Every P&L number here is the inventory-accounted one written by analysis/inventory_check.py
(positions tracked, funding, the day-end close). Validation days without a trade count as $0,
using the run's meta.json day list when it has one. Intervals are day-bootstrap 95% intervals
(arbtrade/stats.py), paired when two strategies are compared.
"""

from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path

import numpy as np
import pandas as pd

from arbtrade.stats import boot_ci, paired_diff

STRATEGIES = ["naive fast path", "gap size only", "fast path + decay prior", "slow model always", "latency-aware cascade"]
SHORT = {"naive fast path": "Naive", "gap size only": "Gap size only", "fast path + decay prior": "Prior only",
         "slow model always": "Slow always", "latency-aware cascade": "Cascade"}
COMPARISONS = [("latency-aware cascade", "naive fast path"), ("latency-aware cascade", "gap size only"),
               ("latency-aware cascade", "slow model always"), ("fast path + decay prior", "gap size only")]
CAPS = {"capped": "$50k cap", "uncapped": "no cap"}


def _num(x) -> float | None:
    """JSON-safe float (NaN and inf become null)."""
    x = float(x)
    return x if np.isfinite(x) else None


def _ci(x: np.ndarray) -> dict:
    lo, hi = boot_ci(x)
    return {"mean": _num(np.mean(x)) if len(x) else None, "lo": _num(lo), "hi": _num(hi)}


def list_runs(reports: Path) -> list[dict]:
    """Every evaluation run that has inventory-accounted results, latest tag first."""
    out = []
    for d in sorted((reports / "pnl").glob("*/inventory_by_day.csv"), key=lambda p: p.parent.name):
        run = d.parent
        meta = json.loads((run / "meta.json").read_text()) if (run / "meta.json").exists() else {}
        pair = meta.get("pair") or run.name
        tag = run.name[len(pair):] if run.name.startswith(pair) else ""
        head = pd.read_csv(d, usecols=["date", "fee", "mode", "tau_ms"])
        parts = pair.removeprefix("tick_").split("_")  # <coin>_<market>_<venue a>_<venue b>
        out.append({"name": run.name, "pair": pair, "tag": tag, "coin": parts[0].upper(),
                    "venues": parts[2:4] if len(parts) >= 4 else None,
                    "days": int(head.date.nunique()), "fees": sorted(head.fee.unique().tolist()),
                    "taus": sorted(head.tau_ms.unique().tolist()), "modes": sorted(head["mode"].unique().tolist()),
                    "offset_aware": bool(meta.get("offset_aware")), "latencies_ms": meta.get("latencies_ms"),
                    "feed_delay_ms": meta.get("feed_delay_ms"), "deplete_liquidity": meta.get("deplete_liquidity"),
                    "first": str(head.date.min()), "last": str(head.date.max())})
    out.sort(key=lambda r: (r["tag"], r["coin"] in ("BTC", "ETH"), r["days"]), reverse=True)
    return out


@lru_cache(maxsize=16)
def _load(run_dir: str, mtime: float) -> tuple[pd.DataFrame, dict]:
    run = Path(run_dir)
    df = pd.read_csv(run / "inventory_by_day.csv")
    meta = json.loads((run / "meta.json").read_text()) if (run / "meta.json").exists() else {}
    return df, meta


def load_run(reports: Path, name: str) -> tuple[pd.DataFrame, dict]:
    run = (reports / "pnl" / name).resolve()
    if run.parent != (reports / "pnl").resolve() or not (run / "inventory_by_day.csv").exists():
        raise KeyError(name)
    return _load(str(run), (run / "inventory_by_day.csv").stat().st_mtime)


def validation_days(df: pd.DataFrame, meta: dict, fee: float) -> list[str]:
    """Every validation day at this fee, including days without a trade (from meta.json when it has them)."""
    per_fold = meta.get("val_days", {}).get(str(float(fee)))
    if per_fold:
        return sorted({d for days in per_fold.values() for d in days})
    return sorted(df[df.fee == fee].date.unique())


def fold_starts(meta: dict) -> list[str]:
    return [f["val"][0] for f in meta.get("folds", [])][1:]


def run_summary(reports: Path, name: str, fee: float, tau: float, mode: str, cap: str) -> dict:
    """Everything the Results view needs for one run and one setting."""
    df, meta = load_run(reports, name)
    days = validation_days(df, meta, fee)
    here = df[(df.fee == fee) & (df.tau_ms == tau) & (df["mode"] == mode) & (df.cap == CAPS[cap])]
    present = [s for s in STRATEGIES if s in set(here.strategy)]
    per = {s: here[here.strategy == s].set_index("date") for s in present}
    col = lambda s, c: per[s][c].reindex(days, fill_value=0.0)

    strategies = []
    for s in present:
        g, x = per[s], col(s, "realised").to_numpy()
        trades = g.kept.reindex(days, fill_value=0).to_numpy()
        funding, flatten = col(s, "funding").to_numpy(), col(s, "flatten").to_numpy()
        strategies.append({
            "key": s, "label": SHORT[s], **_ci(x),
            "trades_per_day": _num(trades.mean()) if len(trades) else None,
            "one_way": _num(np.average(g.one_way_share, weights=g.trades)) if g.trades.sum() else None,
            "win_days": _num((x > 0).mean()) if len(x) else None,
            "worst_day": _num(x.min()) if len(x) else None, "best_day": _num(x.max()) if len(x) else None,
            "parts": {"trades": _num((x - funding - flatten).mean()), "funding": _num(funding.mean()),
                      "close": _num(flatten.mean())},
            "daily": [_num(v) for v in x], "cum": [_num(v) for v in np.cumsum(x)],
        })
    pairs = []
    for a, b in COMPARISONS:
        if a in per and b in per:
            m, lo, hi = paired_diff(per[a]["realised"], per[b]["realised"], days)
            pairs.append({"a": SHORT[a], "b": SHORT[b], "mean": _num(m), "lo": _num(lo), "hi": _num(hi)})

    # Realised P&L against latency, when the run kept trades at several latencies.
    taus = sorted(df[(df.fee == fee) & (df["mode"] == mode)].tau_ms.unique().tolist())
    by_tau = []
    if len(taus) > 1:
        sub = df[(df.fee == fee) & (df["mode"] == mode) & (df.cap == CAPS[cap])]
        for s in present:
            pts = []
            for t in taus:
                g = sub[(sub.tau_ms == t) & (sub.strategy == s)].set_index("date").realised.reindex(days, fill_value=0.0)
                pts.append({"tau": t, **_ci(g.to_numpy())})
            by_tau.append({"key": s, "label": SHORT[s], "points": pts})

    venue_fees = None
    folds_csv = reports / "pnl" / name / "pnl_vs_latency_folds.csv"
    if folds_csv.exists():
        f = pd.read_csv(folds_csv, nrows=200)
        if {"fee_a_bps", "fee_b_bps"} <= set(f.columns):
            f = f[np.isclose(f.fee_bps_per_leg, fee)]
            if len(f):
                venue_fees = [float(f.fee_a_bps.iloc[0]), float(f.fee_b_bps.iloc[0])]

    close = None  # how the day-end close was scored, as the run's own report says
    md = reports / "pnl" / name / "inventory.md"
    if md.exists():
        m = re.search(r"day's last (\d+(?:\.\d+)?) s", md.read_text(encoding="utf-8"))
        close = f"no trades in the last {m.group(1)} s; close within shown size" if m else "closed at the last quotes"

    parts = meta.get("pair", name).removeprefix("tick_").split("_")
    return {"run": name, "pair": meta.get("pair", name), "venues": parts[2:4] if len(parts) >= 4 else None, "fee": fee, "tau": tau, "mode": mode, "cap": cap,
            "days": days, "fold_starts": [d for d in fold_starts(meta) if d in set(days)],
            "strategies": strategies, "pairs": pairs, "by_tau": by_tau,
            "setup": {"venue_fees_bps": venue_fees, "close": close, "latencies_ms": meta.get("latencies_ms"), "feed_delay_ms": meta.get("feed_delay_ms"),
                      "deplete_liquidity": meta.get("deplete_liquidity"), "offset_aware": meta.get("offset_aware"),
                      "offset_window_s": meta.get("offset_window_s"), "slow_latency": meta.get("latency_ms")}}


def coins(reports: Path, tag: str, mode: str, cap: str) -> dict:
    """One row per pair run with this tag: each strategy's realised P&L per day, and the cascade's edge over the rules."""
    rows = []
    for r in list_runs(reports):
        if r["tag"] != tag:
            continue
        df, meta = load_run(reports, r["name"])
        fee, tau = r["fees"][0], r["taus"][-1]
        days = validation_days(df, meta, fee)
        here = df[(df.fee == fee) & (df.tau_ms == tau) & (df["mode"] == mode) & (df.cap == CAPS[cap])]
        series = {s: here[here.strategy == s].set_index("date").realised for s in STRATEGIES if s in set(here.strategy)}
        cells = {SHORT[s]: _ci(v.reindex(days, fill_value=0.0).to_numpy()) for s, v in series.items()}
        edge = None
        if "latency-aware cascade" in series and "gap size only" in series:
            m, lo, hi = paired_diff(series["latency-aware cascade"], series["gap size only"], days)
            edge = {"mean": _num(m), "lo": _num(lo), "hi": _num(hi)}
        trades = here[here.strategy == "latency-aware cascade"].set_index("date").kept.reindex(days, fill_value=0)
        cum = {SHORT[s]: [_num(v) for v in np.cumsum(series[s].reindex(days, fill_value=0.0).to_numpy())]
               for s in ("latency-aware cascade", "gap size only") if s in series}
        rows.append({"coin": r["coin"], "venues": r["venues"], "run": r["name"], "days": len(days), "first": days[0] if days else None,
                     "last": days[-1] if days else None, "strategies": cells, "edge_vs_gap": edge,
                     "trades_per_day": _num(trades.mean()) if len(trades) else None, "dates": days, "cum": cum})
    rows.sort(key=lambda x: -(x["strategies"].get("Cascade", {}).get("mean") or -1e9))
    tags = sorted({r["tag"] for r in list_runs(reports) if r["tag"]})
    return {"tag": tag, "mode": mode, "cap": cap, "rows": rows, "tags": tags}


def decay(reports: Path) -> dict:
    """Walk-forward AUC and calibration of the decay models (analysis/decay_pilot.py)."""
    path = reports / "decay" / "summary_v2.csv"
    if not path.exists():
        path = reports / "decay" / "summary.csv"
    if not path.exists():
        return {"rows": []}
    df = pd.read_csv(path)
    keep = ["pair", "births", "hurdle", "tau_ms", "model", "folds", "n_val", "alive", "undecidable", "auc", "auc_sd",
            "bss", "ece"]
    df = df[[c for c in keep if c in df.columns]]
    return {"source": path.name, "rows": json.loads(df.to_json(orient="records")), "survival": survival(reports)}


def survival(reports: Path) -> dict | None:
    """Share of births still open t ms after birth, per hurdle (analysis/decay_figures.py). The band is
    what 100 ms sampling allows: surely open (lower bound) to possibly open (upper bound)."""
    path = reports / "decay" / "fig_survival.csv"
    if not path.exists():
        return None
    df = pd.read_csv(path).sort_values(["hurdle", "t_ms"])
    pair = None
    script = reports.parent.parent / "analysis" / "decay_figures.py"
    if script.exists():
        m = re.search(r'^PAIR\s*=\s*"([^"]+)"', script.read_text(encoding="utf-8"), re.M)
        pair = m.group(1) if m else None
    curves = {h: {"t": g.t_ms.tolist(), "lo": g.surely_alive.tolist(), "hi": g.possibly_alive.tolist(),
                  "n": int(g.n.iloc[0])} for h, g in df.groupby("hurdle")}
    return {"pair": pair, "curves": curves}


def notes(reports: Path) -> list[dict]:
    """Markdown reports worth reading in full, for the Reports view."""
    out = []
    for p in sorted(reports.rglob("*.md")):
        if "episodes" in p.parts or "quality" in p.parts:
            continue
        out.append({"path": p.relative_to(reports).as_posix(), "size": p.stat().st_size})
    return out


def read_note(reports: Path, rel: str) -> str:
    p = (reports / rel).resolve()
    if reports.resolve() not in p.parents or p.suffix != ".md" or not p.exists():
        raise KeyError(rel)
    return p.read_text(encoding="utf-8")
