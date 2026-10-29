"""Record Bybit's live top-of-book (10 ms) and trades, and Binance USD-M top-of-book (every change),
on one receive clock: 10x finer timing than the Bybit archive, and cross-venue data the free
archives no longer provide (Binance's bookTicker archive ends in March 2024).

    .venv/bin/python -m arbdata record                  # every bybit_live stream in the config, forever
    .venv/bin/python -m arbdata record --minutes 2      # a short test

Each message is written with this machine's receive time as one JSON line:
    {"recv_us": 1790812800123456, "msg": {...exactly as Bybit sent it...}}
into data/raw/bybit_live/<venue>/<pair>/<kind>/<YYYY-MM-DD>/<HH>_<run>.jsonl.gz (UTC hours,
one file per process run, flushed every 10 s so a crash loses seconds, not the hour).
Connection drops are logged to events.jsonl in the same day folder and the next message
after a reconnect carries "reconnect": true, so the normaliser marks the gap as an outage.

Run it on an always-on machine with its clock synced (chrony or systemd-timesyncd):
receive timestamps are only as good as the clock that stamps them.
"""

from __future__ import annotations

import asyncio
import datetime as dt
import gzip
import json
import signal
import ssl
import time
from pathlib import Path

import certifi
import orjson
import websockets

from .config import Config, Stream

WS_URL = {"spot": "wss://stream.bybit.com/v5/public/spot", "linear": "wss://stream.bybit.com/v5/public/linear"}
BINANCE_FUTURES_WS = "wss://fstream.binance.com/stream?streams="  # USD-M futures; Binance sends the pings
PING_EVERY_S = 20  # Bybit closes idle public connections; it documents a 20 s ping
STALL_S = 30  # nothing received for this long (not even a pong): the connection is dead, reconnect
# Verify TLS against certifi's CA bundle: some Python installs (python.org builds on macOS)
# ship without system root certificates. Verification stays on.
TLS = ssl.create_default_context(cafile=certifi.where())


class Stalled(Exception):
    """An open connection that has gone silent. Without this the receive loop waits on it forever."""


RUN_ID = time.strftime("%Y%m%dT%H%M%S", time.gmtime())  # one file per process run: a crash never corrupts a later run
FLUSH_EVERY_S = 10  # a crash loses at most this much; flushed gzip data stays readable


class HourlyWriter:
    """gzip files per UTC hour and per run; flushed often so a killed process loses seconds, not hours."""

    def __init__(self, cfg: Config, stream: Stream):
        self.base = cfg.data_root / "raw" / stream.source / stream.venue / stream.pair / stream.kind
        self.key: tuple[str, int] | None = None
        self.fh = None
        self.last_flush = time.monotonic()

    def day_dir(self, recv_us: int) -> Path:
        return self.base / dt.datetime.fromtimestamp(recv_us / 1e6, dt.timezone.utc).strftime("%Y-%m-%d")

    def write(self, recv_us: int, line: bytes) -> None:
        t = dt.datetime.fromtimestamp(recv_us / 1e6, dt.timezone.utc)
        key = (t.strftime("%Y-%m-%d"), t.hour)
        if key != self.key:
            self.close()
            path = self.base / key[0] / f"{key[1]:02d}_{RUN_ID}.jsonl.gz"
            path.parent.mkdir(parents=True, exist_ok=True)
            self.fh = gzip.open(path, "ab", compresslevel=6)
            self.key = key
        self.fh.write(line)
        if time.monotonic() - self.last_flush > FLUSH_EVERY_S:
            self.fh.flush()
            self.last_flush = time.monotonic()

    def event(self, recv_us: int, kind: str, detail: str = "") -> None:
        path = self.day_dir(recv_us) / "events.jsonl"
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "a") as fh:
            fh.write(json.dumps({"recv_us": recv_us, "event": kind, "detail": detail}) + "\n")

    def close(self) -> None:
        if self.fh:
            self.fh.close()
            self.fh = None


async def _run_market(market: str, streams: list[Stream], cfg: Config, stop: asyncio.Event, stats: dict) -> None:
    writers = {s.symbol: HourlyWriter(cfg, s) for s in streams}
    topics = [t for s in streams for t in (f"orderbook.1.{s.symbol}", f"publicTrade.{s.symbol}")]
    backoff = 1.0
    pending_mark: set[str] = set()  # symbols whose next message follows a reconnect
    while not stop.is_set():
        try:
            async with websockets.connect(WS_URL[market], ssl=TLS, ping_interval=None, max_size=2**22) as ws:
                await ws.send(json.dumps({"op": "subscribe", "args": topics}))
                last_ping = last_msg = time.monotonic()
                backoff = 1.0
                while not stop.is_set():
                    if time.monotonic() - last_ping > PING_EVERY_S:
                        await ws.send(json.dumps({"op": "ping"}))
                        last_ping = time.monotonic()
                    try:
                        raw = await asyncio.wait_for(ws.recv(), timeout=5)
                    except asyncio.TimeoutError:
                        if time.monotonic() - last_msg > STALL_S:
                            raise Stalled(f"nothing received for {STALL_S} s")
                        continue
                    last_msg = time.monotonic()
                    recv_us = time.time_ns() // 1000
                    msg = orjson.loads(raw)
                    topic = msg.get("topic")
                    if not topic:
                        continue  # subscription acks and pongs
                    symbol = topic.rsplit(".", 1)[-1]
                    rec = {"recv_us": recv_us, "msg": msg}
                    if symbol in pending_mark and topic.startswith("orderbook"):
                        rec["reconnect"] = True
                        pending_mark.discard(symbol)
                    writers[symbol].write(recv_us, orjson.dumps(rec) + b"\n")
                    stats[topic] = stats.get(topic, 0) + 1
        except (OSError, websockets.WebSocketException, Stalled) as exc:
            now = time.time_ns() // 1000
            for w in writers.values():
                w.event(now, "disconnect", f"{type(exc).__name__}: {exc}")
            pending_mark = set(writers)
            await asyncio.sleep(backoff)
            backoff = min(backoff * 2, 60)
    for w in writers.values():
        w.close()


async def _run_binance(streams: list[Stream], cfg: Config, stop: asyncio.Event, stats: dict) -> None:
    """Binance USD-M bookTicker: every top-of-book change, subscribed through the URL."""
    writers = {s.symbol: HourlyWriter(cfg, s) for s in streams}
    url = BINANCE_FUTURES_WS + "/".join(f"{s.symbol.lower()}@bookTicker" for s in streams)
    backoff = 1.0
    pending_mark: set[str] = set()
    while not stop.is_set():
        try:
            async with websockets.connect(url, ssl=TLS, ping_interval=None, max_size=2**22) as ws:
                last_msg = time.monotonic()
                backoff = 1.0
                while not stop.is_set():
                    try:
                        raw = await asyncio.wait_for(ws.recv(), timeout=5)
                    except asyncio.TimeoutError:
                        if time.monotonic() - last_msg > STALL_S:
                            raise Stalled(f"nothing received for {STALL_S} s")
                        continue
                    last_msg = time.monotonic()
                    recv_us = time.time_ns() // 1000
                    msg = orjson.loads(raw)
                    data = msg.get("data")
                    if not data or "s" not in data:
                        continue
                    symbol = data["s"]
                    rec = {"recv_us": recv_us, "msg": msg}
                    if symbol in pending_mark:
                        rec["reconnect"] = True
                        pending_mark.discard(symbol)
                    writers[symbol].write(recv_us, orjson.dumps(rec) + b"\n")
                    stats[msg["stream"]] = stats.get(msg["stream"], 0) + 1
        except (OSError, websockets.WebSocketException, Stalled) as exc:
            now = time.time_ns() // 1000
            for w in writers.values():
                w.event(now, "disconnect", f"{type(exc).__name__}: {exc}")
            pending_mark = set(writers)
            await asyncio.sleep(backoff)
            backoff = min(backoff * 2, 60)
    for w in writers.values():
        w.close()


async def record(cfg: Config, minutes: float | None = None) -> dict:
    streams = [s for s in cfg.streams.values() if s.source in ("bybit_live", "binance_live")]
    if not streams:
        raise SystemExit("no live streams in the config")
    stop = asyncio.Event()
    loop = asyncio.get_running_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, stop.set)
    if minutes:
        loop.call_later(minutes * 60, stop.set)
    stats: dict = {}
    by_market: dict[str, list[Stream]] = {}
    for s in streams:
        if s.source == "bybit_live":
            by_market.setdefault(s.market, []).append(s)
    binance = [s for s in streams if s.source == "binance_live"]
    tasks = [_run_market(m, ss, cfg, stop, stats) for m, ss in by_market.items()]
    if binance:
        tasks.append(_run_binance(binance, cfg, stop, stats))
    await asyncio.gather(*tasks)
    return stats
