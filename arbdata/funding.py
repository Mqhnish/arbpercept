"""Perpetual funding rates for Binance USD-M and Bybit linear contracts, from free public sources.

A position held across a funding time pays (if long) or receives (if short) that venue's
rate times the position's notional. Cross-venue trades leave a long perpetual on one venue
and a short on the other, so they collect one rate and pay the other for as long as the
position stays open.

Binance publishes monthly files on data.binance.vision (the running month is fetched from
its public REST endpoint instead); Bybit serves its history through a public REST endpoint.
Stored per venue and symbol in data/funding/<venue>_<symbol>.parquet: ts (µs, the funding
time) and rate (fraction of notional per funding interval).

    .venv/bin/python -m arbdata.funding 2024-01-01 2024-02-01 --symbols BTCUSDT ETHUSDT
"""

from __future__ import annotations

import argparse
import datetime as dt
import io
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd
import requests

from .config import Config, load_config

BINANCE_MONTHLY = "https://data.binance.vision/data/futures/um/monthly/fundingRate/{symbol}/{symbol}-fundingRate-{month}.zip"
BINANCE_REST = "https://fapi.binance.com/fapi/v1/fundingRate"
BYBIT_REST = "https://api.bybit.com/v5/market/funding/history"
VENUES = ("binance", "bybit")


def funding_path(cfg: Config, venue: str, symbol: str) -> Path:
    return cfg.data_root / "funding" / f"{venue}_{symbol}.parquet"


def _ms(day: str) -> int:
    return int(dt.datetime.fromisoformat(day).replace(tzinfo=dt.timezone.utc).timestamp() * 1000)


def _frame(ts_ms, rate) -> pd.DataFrame:
    return pd.DataFrame({"ts": np.asarray(ts_ms, dtype=np.int64) * 1000, "rate": np.asarray(rate, dtype=float)})


def fetch_binance(symbol: str, start: str, end: str) -> pd.DataFrame:
    s, e = _ms(start), _ms(end)
    parts = []
    month = dt.date.fromisoformat(start).replace(day=1)
    while _ms(month.isoformat()) < e:
        r = requests.get(BINANCE_MONTHLY.format(symbol=symbol, month=month.strftime("%Y-%m")), timeout=30)
        if r.status_code == 200:
            with zipfile.ZipFile(io.BytesIO(r.content)) as z:
                df = pd.read_csv(z.open(z.namelist()[0]))
            parts.append(_frame(df.calc_time, df.last_funding_rate))
        elif r.status_code == 404:  # month not published yet: use the REST history
            m_end = min(e, _ms((month.replace(day=28) + dt.timedelta(days=4)).replace(day=1).isoformat()))
            q = requests.get(BINANCE_REST, params={"symbol": symbol, "startTime": _ms(month.isoformat()),
                                                   "endTime": m_end, "limit": 1000}, timeout=30)
            if q.status_code in (403, 451):  # Binance's API refuses some regions; we don't route around it
                print(f"  binance {symbol} {month:%Y-%m}: monthly file not published and the REST API refused "
                      f"this region (HTTP {q.status_code}); skipped")
            else:
                q.raise_for_status()
                rows = q.json()
                parts.append(_frame([x["fundingTime"] for x in rows], [float(x["fundingRate"]) for x in rows]))
        else:
            r.raise_for_status()
        month = (month.replace(day=28) + dt.timedelta(days=4)).replace(day=1)
    df = pd.concat(parts, ignore_index=True) if parts else _frame([], [])
    return df[(df.ts >= s * 1000) & (df.ts < e * 1000)]


def fetch_bybit(symbol: str, start: str, end: str) -> pd.DataFrame:
    s, e = _ms(start), _ms(end)
    parts, cursor = [], e
    while cursor > s:
        r = requests.get(BYBIT_REST, params={"category": "linear", "symbol": symbol, "startTime": s,
                                             "endTime": cursor, "limit": 200}, timeout=30)
        r.raise_for_status()
        rows = r.json()["result"]["list"]  # newest first
        if not rows:
            break
        parts.append(_frame([int(x["fundingRateTimestamp"]) for x in rows], [float(x["fundingRate"]) for x in rows]))
        oldest = min(int(x["fundingRateTimestamp"]) for x in rows)
        if oldest <= s or len(rows) < 200:
            break
        cursor = oldest - 1
    df = pd.concat(parts, ignore_index=True) if parts else _frame([], [])
    return df[(df.ts >= s * 1000) & (df.ts < e * 1000)]


def update(cfg: Config, venue: str, symbol: str, start: str, end: str) -> pd.DataFrame:
    new = (fetch_binance if venue == "binance" else fetch_bybit)(symbol, start, end)
    path = funding_path(cfg, venue, symbol)
    if path.exists():
        new = pd.concat([pd.read_parquet(path), new], ignore_index=True)
    new = new.drop_duplicates("ts", keep="last").sort_values("ts").reset_index(drop=True)
    path.parent.mkdir(parents=True, exist_ok=True)
    new.to_parquet(path, index=False)
    return new


def load_funding(cfg: Config, venue: str, symbol: str) -> pd.DataFrame:
    path = funding_path(cfg, venue, symbol)
    if not path.exists():
        raise FileNotFoundError(f"{path} missing: run python -m arbdata.funding <start> <end>")
    return pd.read_parquet(path)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("start")
    ap.add_argument("end", help="exclusive")
    ap.add_argument("--symbols", nargs="*", default=["BTCUSDT", "ETHUSDT"])
    args = ap.parse_args()
    cfg = load_config()
    for venue in VENUES:
        for sym in args.symbols:
            df = update(cfg, venue, sym, args.start, args.end)
            got = df[(df.ts >= _ms(args.start) * 1000) & (df.ts < _ms(args.end) * 1000)]
            print(f"{venue} {sym}: {len(got)} funding times, mean {got.rate.mean() * 1e4:+.2f} bps per interval")


if __name__ == "__main__":
    main()
