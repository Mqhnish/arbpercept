"""Download raw daily files from the free public sources.

Raw files are immutable: once a file is on disk it is never rewritten, and every
download is recorded (URL, size, SHA-256) in data/raw/manifest.jsonl so any
dataset build can be traced back to exact inputs.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import time
from dataclasses import dataclass
from pathlib import Path

import requests

from .config import Config, Stream

BYBIT_URL = "https://quote-saver.bycsi.com/orderbook/{market}/{symbol}/{date}_{symbol}_ob{depth}.data.zip"
# Bybit renamed its linear archives from ob500 to ob200 during 2025; spot has always been ob200.
BYBIT_DEPTHS = {"linear": (200, 500), "spot": (200,)}
BINANCE_BT_URL = "https://data.binance.vision/data/futures/um/daily/bookTicker/{symbol}/{symbol}-bookTicker-{date}.zip"
TARDIS_URL = "https://datasets.tardis.dev/v1/{exchange}/quotes/{y}/{m:02d}/{d:02d}/{symbol}.csv.gz"

RAW_EXT = {"bybit_ob": ".zip", "binance_bt": ".zip", "tardis": ".csv.gz", "bybit_live": "", "binance_live": ""}  # live: a folder per day

# Bybit's public trade archive: every trade with its matching-engine time. An independent
# record used to validate reconstructed books and to describe order flow.
BYBIT_TRADES_URL = {
    "linear": "https://public.bybit.com/trading/{symbol}/{symbol}{date}.csv.gz",
    "spot": "https://public.bybit.com/spot/{symbol}/{symbol}_{date}.csv.gz",
}

USER_AGENT = "arbdata/0.1 (student research; python-requests)"


class BlockedError(RuntimeError):
    """The server answered with a bot-protection page. We stop rather than work around it."""


@dataclass
class Result:
    stream: str
    date: str
    status: str  # "downloaded" | "exists" | "missing" | "skipped" | "error"
    detail: str = ""
    bytes: int = 0


def candidate_urls(stream: Stream, date: str) -> list[str]:
    day = dt.date.fromisoformat(date)
    if stream.source == "bybit_ob":
        return [
            BYBIT_URL.format(market=stream.market, symbol=stream.symbol, date=date, depth=depth)
            for depth in BYBIT_DEPTHS[stream.market]
        ]
    if stream.source == "binance_bt":
        return [BINANCE_BT_URL.format(symbol=stream.symbol, date=date)]
    if stream.source == "tardis":
        return [TARDIS_URL.format(exchange=stream.exchange, y=day.year, m=day.month, d=day.day, symbol=stream.symbol)]
    raise ValueError(f"unknown source {stream.source}")


def _looks_blocked(resp: requests.Response) -> bool:
    if resp.status_code not in (403, 429, 503):
        return False
    head = resp.content[:4096].decode(errors="ignore").lower()
    return "cloudflare" in head or "attention required" in head or "captcha" in head


def _fetch(session: requests.Session, url: str, dest: Path, headers: dict[str, str]) -> tuple[str, int, str]:
    """Stream url to dest. Returns (status, bytes, sha256). Retries transient failures only."""
    tmp = dest.with_suffix(dest.suffix + ".part")
    last_err = ""
    for attempt in range(4):
        try:
            with session.get(url, stream=True, timeout=(15, 120), headers=headers) as resp:
                if resp.status_code == 404:
                    return "missing", 0, ""
                if _looks_blocked(resp):
                    raise BlockedError(
                        f"{url} returned a bot-protection page (HTTP {resp.status_code}). "
                        "Download this file in your browser, or use an API key, and place it at "
                        f"{dest}. arbdata will not try to bypass the check."
                    )
                if resp.status_code >= 500 or resp.status_code == 429:
                    last_err = f"HTTP {resp.status_code}"
                    time.sleep(2 ** attempt)
                    continue
                if resp.status_code != 200:
                    return "error", 0, f"HTTP {resp.status_code}"
                h = hashlib.sha256()
                n = 0
                dest.parent.mkdir(parents=True, exist_ok=True)
                with open(tmp, "wb") as out:
                    for chunk in resp.iter_content(chunk_size=1 << 20):
                        out.write(chunk)
                        h.update(chunk)
                        n += len(chunk)
                expected = resp.headers.get("Content-Length")
                if expected is not None and int(expected) != n:
                    last_err = f"truncated: got {n} of {expected} bytes"
                    tmp.unlink(missing_ok=True)
                    time.sleep(2 ** attempt)
                    continue
                tmp.rename(dest)
                return "downloaded", n, h.hexdigest()
        except (requests.ConnectionError, requests.Timeout) as exc:
            last_err = type(exc).__name__
            tmp.unlink(missing_ok=True)
            time.sleep(2 ** attempt)
    return "error", 0, last_err


def _log_manifest(cfg: Config, stream_key: str, date: str, url: str, dest: Path, nbytes: int, digest: str) -> None:
    with open(cfg.manifest_path, "a") as mf:
        mf.write(json.dumps({
            "stream": stream_key, "date": date, "url": url, "path": str(dest.relative_to(cfg.data_root)),
            "bytes": nbytes, "sha256": digest,
            "downloaded_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        }) + "\n")


def download_trades(cfg: Config, streams: list[Stream], dates: list[str], pause_s: float = 0.3) -> list[Result]:
    session = requests.Session()
    session.headers["User-Agent"] = USER_AGENT
    cfg.manifest_path.parent.mkdir(parents=True, exist_ok=True)
    results: list[Result] = []
    for date in dates:
        for stream in streams:
            if stream.source not in ("bybit_ob", "bybit_live"):
                continue
            dest = cfg.trades_raw_path(stream, date)
            if dest.exists():
                results.append(Result(stream.key, date, "exists", bytes=dest.stat().st_size))
                continue
            url = BYBIT_TRADES_URL[stream.market].format(symbol=stream.symbol, date=date)
            status, nbytes, digest = _fetch(session, url, dest, {})
            if status == "downloaded":
                _log_manifest(cfg, f"trades:{stream.key}", date, url, dest, nbytes, digest)
            results.append(Result(stream.key, date, status, url if status == "downloaded" else digest, nbytes))
            print(f"{date} trades {stream.key}: {status} {nbytes / 1e6:.0f} MB", flush=True)
            time.sleep(pause_s)
    return results


def download(cfg: Config, streams: list[Stream], dates: list[str], pause_s: float = 0.5) -> list[Result]:
    session = requests.Session()
    session.headers["User-Agent"] = USER_AGENT
    tardis_key = os.environ.get("TARDIS_API_KEY")
    results: list[Result] = []
    cfg.manifest_path.parent.mkdir(parents=True, exist_ok=True)
    for date in dates:
        for stream in streams:
            dest = cfg.raw_path(stream, date, RAW_EXT[stream.source])
            if dest.exists():
                results.append(Result(stream.key, date, "exists", bytes=dest.stat().st_size))
                continue
            headers: dict[str, str] = {}
            if stream.source == "tardis":
                if tardis_key:
                    headers["Authorization"] = f"Bearer {tardis_key}"
                elif dt.date.fromisoformat(date).day != 1:
                    results.append(Result(stream.key, date, "skipped", "Tardis is free only on the 1st"))
                    continue
            status, detail, nbytes = "missing", "", 0
            for url in candidate_urls(stream, date):
                status, nbytes, digest = _fetch(session, url, dest, headers)
                if status == "downloaded":
                    _log_manifest(cfg, stream.key, date, url, dest, nbytes, digest)
                    detail = url
                    break
                if status == "error":
                    detail = digest
                    break
            results.append(Result(stream.key, date, status, detail, nbytes))
            print(f"{date} {stream.key}: {status} {nbytes / 1e6:.0f} MB {detail}".rstrip(), flush=True)
            time.sleep(pause_s)
    return results


def date_range(start: str, end: str) -> list[str]:
    d0, d1 = dt.date.fromisoformat(start), dt.date.fromisoformat(end)
    return [(d0 + dt.timedelta(days=i)).isoformat() for i in range((d1 - d0).days + 1)]
