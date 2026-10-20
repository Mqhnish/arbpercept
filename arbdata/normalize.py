"""Turn each raw source into one canonical top-of-book (L1) table per stream-day.

Canonical columns (timestamps are integer microseconds since the Unix epoch, UTC):
    avail_ts    when the quote became observable (the clock all causality uses)
    exch_ts     the exchange's own event time
    bid_px, bid_sz, ask_px, ask_sz
    bid_depth5, ask_depth5   size summed over the best five levels (NaN if the source has only L1)
    n_raw       raw updates in this row's run. Tick sources fold size-only updates into the
                preceding price change, so edges stay exact while files stay small. n_raw
                includes updates that arrive AFTER avail_ts, so it must never be used as a
                feature at avail_ts; align.py credits it only once the run has closed.
    resync      True on the first row after the book was rebuilt or messages were missed

Each normalizer also returns a RawFeed: the silences in the raw update stream. Feed
health is judged from raw updates, because a quiet market (no price change) and a dead
feed (no messages at all) look the same once size-only updates are folded away.
"""

from __future__ import annotations

import gzip
import zipfile
import zlib
from pathlib import Path

import numpy as np
import orjson
import pandas as pd
import pyarrow as pa
import pyarrow.csv as pacsv
from sortedcontainers import SortedDict

L1_COLUMNS = ["avail_ts", "exch_ts", "bid_px", "bid_sz", "ask_px", "ask_sz",
              "bid_depth5", "ask_depth5", "n_raw", "resync"]

# Raw silences longer than this are recorded; each source's max_gap_ms decides which matter.
SILENCE_RECORD_US = 500_000


class RawFeed:
    """Raw update times of one stream-day: when it started, ended, and fell silent.

    Times may arrive out of order (some archive files interleave chunks), so they are
    collected and sorted before silences are measured; out_of_order counts the backward
    steps in arrival order, as a data-quality signal.
    """

    def __init__(self) -> None:
        self._parts: list[np.ndarray] = []
        self._last_arrival: int | None = None
        self.out_of_order = 0
        self._done: tuple | None = None

    def observe(self, ts: np.ndarray) -> None:
        if len(ts) == 0:
            return
        ts = np.asarray(ts, dtype=np.int64)
        prev = np.concatenate(([self._last_arrival], ts[:-1])) if self._last_arrival is not None else ts[:-1]
        cur = ts if self._last_arrival is not None else ts[1:]
        self.out_of_order += int(np.sum(cur < prev))
        self._last_arrival = int(ts[-1])
        self._parts.append(ts)
        self._done = None

    def _finish(self) -> tuple:
        if self._done is None:
            ts = np.sort(np.concatenate(self._parts)) if self._parts else np.array([], dtype=np.int64)
            gaps = np.diff(ts)
            i = np.flatnonzero(gaps > SILENCE_RECORD_US)
            silences = [(int(ts[k]), int(ts[k + 1])) for k in i]
            self._done = (int(ts[0]) if len(ts) else None, int(ts[-1]) if len(ts) else None, len(ts), silences)
        return self._done

    @property
    def first_ts(self) -> int | None:
        return self._finish()[0]

    @property
    def last_ts(self) -> int | None:
        return self._finish()[1]

    @property
    def n(self) -> int:
        return self._finish()[2]

    @property
    def silences(self) -> list[tuple[int, int]]:
        return self._finish()[3]

    def silences_frame(self) -> pd.DataFrame:
        s = np.array(self.silences, dtype=np.int64).reshape(-1, 2)
        return pd.DataFrame({"start_ts": s[:, 0], "end_ts": s[:, 1]})


def _frame(cols: dict[str, list | np.ndarray]) -> pd.DataFrame:
    df = pd.DataFrame({
        "avail_ts": np.asarray(cols["avail_ts"], dtype=np.int64),
        "exch_ts": np.asarray(cols["exch_ts"], dtype=np.int64),
        "bid_px": np.asarray(cols["bid_px"], dtype=np.float64),
        "bid_sz": np.asarray(cols["bid_sz"], dtype=np.float64),
        "ask_px": np.asarray(cols["ask_px"], dtype=np.float64),
        "ask_sz": np.asarray(cols["ask_sz"], dtype=np.float64),
        "bid_depth5": np.asarray(cols["bid_depth5"], dtype=np.float64),
        "ask_depth5": np.asarray(cols["ask_depth5"], dtype=np.float64),
        "n_raw": np.asarray(cols["n_raw"], dtype=np.int32),
        "resync": np.asarray(cols["resync"], dtype=bool),
    })
    # Stable sort keeps the source's update order among equal timestamps.
    return df.sort_values("avail_ts", kind="stable").reset_index(drop=True)


# ---------------------------------------------------------------------------
# Bybit order book archive: one JSON message per line, a snapshot then deltas.
# ---------------------------------------------------------------------------

def _bybit_book_rows(messages) -> tuple[pd.DataFrame, RawFeed]:
    """Rebuild top of book from Bybit order book messages.

    messages yields (avail_us, msg, forced_resync). A snapshot after the first counts as a
    rebuild unless its update id continues the sequence (level-1 streams re-send an unchanged
    snapshot every few seconds with the same id). Skipped update ids mean lost messages.
    """
    bids: SortedDict = SortedDict()
    asks: SortedDict = SortedDict()
    cols: dict[str, list] = {c: [] for c in L1_COLUMNS}
    raw_ts: list[int] = []
    have_book = False
    resync_next = False
    prev_u = None
    for avail_us, msg, forced in messages:
        raw_ts.append(avail_us)
        data = msg["data"]
        u = data.get("u")
        if forced and have_book:
            resync_next = True
        if msg["type"] == "snapshot":
            if have_book and not (u is not None and prev_u is not None and u in (prev_u, prev_u + 1)):
                resync_next = True
            bids.clear()
            asks.clear()
            have_book = True
        elif not have_book:
            continue  # a delta cannot be applied before the first snapshot
        elif prev_u is not None and u is not None and u != prev_u + 1:
            resync_next = True  # update ids skipped: messages were lost
        prev_u = u
        for px, sz in data["b"]:
            p, s = float(px), float(sz)
            if s == 0.0:
                bids.pop(p, None)
            else:
                bids[p] = s
        for px, sz in data["a"]:
            p, s = float(px), float(sz)
            if s == 0.0:
                asks.pop(p, None)
            else:
                asks[p] = s
        if not bids or not asks:
            continue
        bp, bs = bids.peekitem(-1)
        ap, az = asks.peekitem(0)
        cols["avail_ts"].append(avail_us)
        cols["exch_ts"].append(msg.get("cts", msg["ts"]) * 1000)
        cols["bid_px"].append(bp)
        cols["bid_sz"].append(bs)
        cols["ask_px"].append(ap)
        cols["ask_sz"].append(az)
        cols["bid_depth5"].append(sum(bids.values()[-5:]))
        cols["ask_depth5"].append(sum(asks.values()[:5]))
        cols["n_raw"].append(1)
        cols["resync"].append(resync_next)
        resync_next = False
    feed = RawFeed()
    feed.observe(np.sort(np.asarray(raw_ts, dtype=np.int64)))
    return _frame(cols), feed


def normalize_bybit(path: Path) -> tuple[pd.DataFrame, RawFeed]:
    """Bybit public archive: one JSON message per line; avail_ts = Bybit publish time."""
    def messages():
        with zipfile.ZipFile(path) as zf:
            member = next(m for m in zf.namelist() if not m.endswith("/"))
            with zf.open(member) as fh:
                for line in fh:
                    if line.strip():
                        msg = orjson.loads(line)
                        yield msg["ts"] * 1000, msg, False
    return _bybit_book_rows(messages())


def normalize_bybit_live(day_dir: Path) -> tuple[pd.DataFrame, RawFeed]:
    """Our own recordings: avail_ts = this machine's receive time, a true observer clock."""
    def lines(f):
        # A recorder killed mid-hour leaves a file without its gzip trailer: keep what was flushed.
        try:
            with gzip.open(f, "rb") as fh:
                for line in fh:
                    yield line
        except (EOFError, gzip.BadGzipFile, zlib.error):
            return

    def messages():
        recs = []
        for f in sorted(day_dir.glob("*.jsonl.gz")):
            for line in lines(f):
                if not line.strip() or not line.endswith(b"\n"):
                    continue  # a half-written last line
                rec = orjson.loads(line)
                if rec["msg"].get("topic", "").startswith("orderbook"):
                    recs.append(rec)
        recs.sort(key=lambda r: r["recv_us"])  # several runs within an hour interleave by receive time
        for rec in recs:
            yield rec["recv_us"], rec["msg"], rec.get("reconnect", False)
    return _bybit_book_rows(messages())


# ---------------------------------------------------------------------------
# Tick-level CSV sources: stream in batches and fold size-only updates.
# ---------------------------------------------------------------------------

class _RunCollapser:
    """Keep the first row of every run of unchanged (bid_px, ask_px); count the run length.

    Works across batch boundaries so a run split between two batches is counted once.
    """

    def __init__(self) -> None:
        self.parts: list[dict[str, np.ndarray]] = []
        self.last_px: tuple[float, float] | None = None

    def add(self, avail, exch, bp, bs, ap, az) -> None:
        n = len(bp)
        if n == 0:
            return
        changed = np.empty(n, dtype=bool)
        changed[1:] = (bp[1:] != bp[:-1]) | (ap[1:] != ap[:-1])
        changed[0] = self.last_px is None or (bp[0], ap[0]) != self.last_px
        self.last_px = (bp[-1], ap[-1])
        keep = np.flatnonzero(changed)
        if len(keep) == 0 or keep[0] != 0:
            # Leading rows continue the previous batch's last run.
            lead = n if len(keep) == 0 else keep[0]
            if self.parts:
                self.parts[-1]["n_raw"][-1] += lead
        if len(keep) == 0:
            return
        counts = np.diff(np.append(keep, n)).astype(np.int32)
        self.parts.append({
            "avail_ts": avail[keep], "exch_ts": exch[keep],
            "bid_px": bp[keep], "bid_sz": bs[keep], "ask_px": ap[keep], "ask_sz": az[keep],
            "n_raw": counts,
        })

    def frame(self) -> pd.DataFrame:
        if not self.parts:
            return pd.DataFrame(columns=L1_COLUMNS)
        cols = {k: np.concatenate([p[k] for p in self.parts]) for k in self.parts[0]}
        n = len(cols["bid_px"])
        cols["bid_depth5"] = np.full(n, np.nan)
        cols["ask_depth5"] = np.full(n, np.nan)
        cols["resync"] = np.zeros(n, dtype=bool)
        return _frame(cols)


def _np(batch: pa.RecordBatch, name: str, dtype) -> np.ndarray:
    return batch.column(name).to_numpy(zero_copy_only=False).astype(dtype, copy=False)


def normalize_binance_bt(path: Path) -> tuple[pd.DataFrame, RawFeed]:
    """Binance USD-M bookTicker archive. Rows are put in book order by update_id first:
    most files already are, but some interleave chunks (2 Jan 2024 had 180k backward steps)."""
    names = ["update_id", "best_bid_price", "best_bid_qty", "best_ask_price", "best_ask_qty",
             "transaction_time", "event_time"]
    with zipfile.ZipFile(path) as zf:
        member = next(m for m in zf.namelist() if m.endswith(".csv"))
        with zf.open(member) as fh:
            has_header = fh.readline().startswith(b"update_id")
        with zf.open(member) as fh:
            table = pacsv.read_csv(
                fh,
                read_options=pacsv.ReadOptions(column_names=names, skip_rows=1 if has_header else 0, block_size=64 << 20),
                convert_options=pacsv.ConvertOptions(column_types={
                    "update_id": pa.int64(),
                    "best_bid_price": pa.float64(), "best_bid_qty": pa.float64(),
                    "best_ask_price": pa.float64(), "best_ask_qty": pa.float64(),
                    "transaction_time": pa.int64(), "event_time": pa.int64()}),
            )
    feed = RawFeed()
    feed.observe(table.column("event_time").to_numpy() * 1000)  # arrival order, to count disorder
    uid = table.column("update_id").to_numpy()
    if np.any(np.diff(uid) < 0):
        table = table.take(pa.array(np.argsort(uid, kind="stable")))
    col = _RunCollapser()
    for batch in table.to_batches(max_chunksize=4_000_000):
        col.add(_np(batch, "event_time", np.int64) * 1000, _np(batch, "transaction_time", np.int64) * 1000,
                _np(batch, "best_bid_price", np.float64), _np(batch, "best_bid_qty", np.float64),
                _np(batch, "best_ask_price", np.float64), _np(batch, "best_ask_qty", np.float64))
    return col.frame(), feed


def normalize_tardis(path: Path) -> tuple[pd.DataFrame, RawFeed]:
    stream = pa.input_stream(str(path), compression="gzip")
    reader = pacsv.open_csv(
        stream,
        read_options=pacsv.ReadOptions(block_size=64 << 20),
        convert_options=pacsv.ConvertOptions(
            include_columns=["timestamp", "local_timestamp", "bid_price", "bid_amount", "ask_price", "ask_amount"],
            column_types={"timestamp": pa.int64(), "local_timestamp": pa.int64(),
                          "bid_price": pa.float64(), "bid_amount": pa.float64(),
                          "ask_price": pa.float64(), "ask_amount": pa.float64()}),
    )
    feed = RawFeed()
    col = _RunCollapser()
    for batch in reader:
        avail = _np(batch, "local_timestamp", np.int64)
        feed.observe(avail)
        bp = _np(batch, "bid_price", np.float64)
        ap = _np(batch, "ask_price", np.float64)
        ok = ~(np.isnan(bp) | np.isnan(ap))  # one side of the book empty: no usable quote
        col.add(avail[ok], _np(batch, "timestamp", np.int64)[ok],
                bp[ok], _np(batch, "bid_amount", np.float64)[ok],
                ap[ok], _np(batch, "ask_amount", np.float64)[ok])
    return col.frame(), feed


def normalize_bybit_live_trades(day_dir: Path) -> pd.DataFrame:
    """Trades from our Bybit recordings (publicTrade), in the same columns as the archive's
    trades: ts (µs, matching engine), price, size, side (+1 buyer-initiated), rpi."""
    rows = []
    for f in sorted(day_dir.glob("*.jsonl.gz")):
        try:
            with gzip.open(f, "rb") as fh:
                for line in fh:
                    if not (line.strip() and line.endswith(b"\n")):
                        continue
                    msg = orjson.loads(line)["msg"]
                    if not msg.get("topic", "").startswith("publicTrade"):
                        continue
                    for d in msg["data"]:
                        rows.append((d["T"] * 1000, float(d["p"]), float(d["v"]), 1 if d["S"] == "Buy" else -1,
                                     bool(d.get("RPI", False))))
        except (EOFError, gzip.BadGzipFile, zlib.error):
            pass
    df = pd.DataFrame(rows, columns=["ts", "price", "size", "side", "rpi"])
    df["side"] = df.side.astype(np.int8)
    return df.drop_duplicates().sort_values("ts", kind="stable").reset_index(drop=True)


def normalize_binance_live(day_dir: Path) -> tuple[pd.DataFrame, RawFeed]:
    """Our Binance USD-M bookTicker recordings: avail_ts = receive time, exch_ts = transaction time.
    Rows are put in update-id order, then size-only changes are folded like the archive."""
    recs = []
    for f in sorted(day_dir.glob("*.jsonl.gz")):
        try:
            with gzip.open(f, "rb") as fh:
                for line in fh:
                    if line.strip() and line.endswith(b"\n"):
                        r = orjson.loads(line)
                        d = r["msg"]["data"]
                        recs.append((d["u"], r["recv_us"], d["T"] * 1000, float(d["b"]), float(d["B"]),
                                     float(d["a"]), float(d["A"])))
        except (EOFError, gzip.BadGzipFile, zlib.error):
            pass  # a killed run: keep what was flushed
    feed = RawFeed()
    col = _RunCollapser()
    if recs:
        a = np.array(recs, dtype=float)
        a = a[np.argsort(a[:, 0], kind="stable")]
        recv = a[:, 1].astype(np.int64)
        feed.observe(np.sort(recv))
        col.add(recv, a[:, 2].astype(np.int64), a[:, 3], a[:, 4], a[:, 5], a[:, 6])
    return col.frame(), feed


NORMALIZERS = {"bybit_ob": normalize_bybit, "binance_bt": normalize_binance_bt, "tardis": normalize_tardis,
               "bybit_live": normalize_bybit_live, "binance_live": normalize_binance_live}


# ---------------------------------------------------------------------------
# Bybit public trade archive: one row per trade, matching-engine time.
# ---------------------------------------------------------------------------

TRADE_COLUMNS = ["ts", "price", "size", "side", "rpi"]


def normalize_bybit_trades(path: Path, market: str) -> pd.DataFrame:
    """Columns: ts (µs, matching engine), price, size (base units), side (+1 buyer-initiated,
    -1 seller-initiated), rpi (trade against a Retail Price Improvement order, which the
    public order book stream does not show)."""
    table = pacsv.read_csv(str(path))
    cols = set(table.column_names)
    if market == "linear":
        ts = np.round(table.column("timestamp").to_numpy().astype(np.float64) * 1e6).astype(np.int64)
        size = table.column("size").to_numpy().astype(np.float64)
        side_raw = table.column("side").to_pylist()
        rpi = table.column("RPI").to_numpy().astype(bool) if "RPI" in cols else np.zeros(len(ts), dtype=bool)
    else:
        ts = table.column("timestamp").to_numpy().astype(np.int64) * 1000
        size = table.column("volume").to_numpy().astype(np.float64)
        side_raw = table.column("side").to_pylist()
        rpi = table.column("rpi").to_numpy().astype(bool) if "rpi" in cols else np.zeros(len(ts), dtype=bool)
    side = np.where(np.char.lower(np.asarray(side_raw, dtype=str)) == "buy", 1, -1).astype(np.int8)
    df = pd.DataFrame({"ts": ts, "price": table.column("price").to_numpy().astype(np.float64),
                       "size": size, "side": side, "rpi": rpi})
    return df.sort_values("ts", kind="stable").reset_index(drop=True)
