import json
import zipfile

import numpy as np

import gzip

from arbdata.normalize import RawFeed, _RunCollapser, normalize_bybit, normalize_bybit_live
from arbdata.quality import down_windows, in_windows


def _bybit_zip(tmp_path, messages):
    path = tmp_path / "ob.data.zip"
    with zipfile.ZipFile(path, "w") as zf:
        zf.writestr("2026-01-01_BTCUSDT_ob200.data", "\n".join(json.dumps(m) for m in messages) + "\n")
    return path


def _msg(kind, ts, u, bids, asks):
    return {"topic": "orderbook.200.BTCUSDT", "ts": ts, "type": kind, "cts": ts - 1,
            "data": {"s": "BTCUSDT", "b": bids, "a": asks, "u": u, "seq": u}}


def test_bybit_book_reconstruction(tmp_path):
    msgs = [
        _msg("snapshot", 1000, 1, [["100", "1"], ["99", "2"], ["98", "3"]], [["101", "1"], ["102", "2"]]),
        _msg("delta", 1100, 2, [["100", "0"]], []),            # best bid removed
        _msg("delta", 1200, 3, [], [["100.5", "4"]]),          # new best ask inside the spread
        _msg("delta", 1300, 7, [["99.5", "1"]], []),           # update ids skipped
        _msg("snapshot", 1400, 1, [["90", "1"]], [["91", "1"]]),  # u restarts: service restart, book rebuilt
    ]
    df, feed = normalize_bybit(_bybit_zip(tmp_path, msgs))
    assert feed.n == 5 and feed.first_ts == 1_000_000 and feed.last_ts == 1_400_000
    assert df.bid_px.tolist() == [100, 99, 99, 99.5, 90]
    assert df.ask_px.tolist() == [101, 101, 100.5, 100.5, 91]
    assert df.bid_depth5.tolist()[:2] == [6, 5]
    assert df.avail_ts.tolist() == [1_000_000, 1_100_000, 1_200_000, 1_300_000, 1_400_000]
    assert df.exch_ts.iloc[0] == 999_000
    assert df.resync.tolist() == [False, False, False, True, True]


def test_bybit_ignores_deltas_before_first_snapshot(tmp_path):
    msgs = [_msg("delta", 900, 5, [["100", "1"]], [["101", "1"]]),
            _msg("snapshot", 1000, 6, [["100", "1"]], [["101", "1"]])]
    df, _ = normalize_bybit(_bybit_zip(tmp_path, msgs))
    assert len(df) == 1 and not df.resync.iloc[0]


def test_run_collapse_counts_across_batches():
    c = _RunCollapser()
    t = np.arange(6, dtype=np.int64)
    # prices: A A B | B B C  (batch boundary inside the B run)
    bp = np.array([1.0, 1.0, 2.0, 2.0, 2.0, 3.0])
    ap = bp + 1
    sz = np.arange(6, dtype=float) + 1
    c.add(t[:3], t[:3], bp[:3], sz[:3], ap[:3], sz[:3])
    c.add(t[3:], t[3:], bp[3:], sz[3:], ap[3:], sz[3:])
    df = c.frame()
    assert df.bid_px.tolist() == [1.0, 2.0, 3.0]
    assert df.n_raw.tolist() == [2, 3, 1]
    assert df.bid_sz.tolist() == [1.0, 3.0, 6.0]  # size at the moment the price changed
    assert df.n_raw.sum() == 6


def test_raw_silences_across_batches_and_down_windows():
    feed = RawFeed()
    feed.observe(np.array([0, 100_000, 200_000], dtype=np.int64))
    feed.observe(np.array([2_200_000, 2_300_000], dtype=np.int64))  # 2 s silence across the boundary
    assert feed.n == 5
    assert feed.silences == [(200_000, 2_200_000)]
    day0 = 0
    down = down_windows(feed.silences_frame(), feed.last_ts, day0, max_gap_ms=1000)
    # down from 1 s after the last update until the next one arrives, plus the rest of the day
    assert down[0].tolist() == [1_200_000, 2_200_000]
    assert down[1][0] == 3_300_000
    t = np.array([1_100_000, 1_200_001, 2_199_999, 2_200_000, 3_000_000, 3_400_000])
    assert in_windows(t, down).tolist() == [False, True, True, False, False, True]


def test_quiet_market_is_not_an_outage():
    # Many raw updates, but the price never changes: one L1 row, no silences.
    c, feed = _RunCollapser(), RawFeed()
    t = np.arange(0, 10_000_000, 50_000, dtype=np.int64)
    px = np.full(len(t), 100.0)
    feed.observe(t)
    c.add(t, t, px, np.ones(len(t)), px + 1, np.ones(len(t)))
    assert len(c.frame()) == 1 and c.frame().n_raw.iloc[0] == len(t)
    assert feed.silences == []


def test_live_level1_snapshots_are_not_resyncs(tmp_path):
    """Level-1 live messages are all snapshots; ids that continue (or repeat, for the
    3-second re-send) are normal. A reconnect or an id jump is a resync."""
    day = tmp_path / "2026-10-19"
    day.mkdir()
    def rec(recv, u, bid, ask, **kw):
        m = _msg("snapshot", recv // 1000, u, [[str(bid), "1"]], [[str(ask), "1"]])
        m["topic"] = "orderbook.1.BTCUSDT"
        return json.dumps({"recv_us": recv, "msg": m, **kw})
    lines = [rec(1_000_000, 10, 100, 101), rec(1_012_000, 11, 100, 101.5), rec(4_012_000, 11, 100, 101.5),
             rec(4_020_000, 15, 99, 100), rec(9_000_000, 16, 98, 99, reconnect=True),
             json.dumps({"recv_us": 9_001_000, "msg": {"topic": "publicTrade.BTCUSDT", "data": []}})]
    with gzip.open(day / "16.jsonl.gz", "wt") as fh:
        fh.write("\n".join(lines) + "\n")
    df, feed = normalize_bybit_live(day)
    assert df.avail_ts.tolist() == [1_000_000, 1_012_000, 4_012_000, 4_020_000, 9_000_000]  # receive time
    assert df.resync.tolist() == [False, False, False, True, True]
    assert df.ask_px.tolist() == [101, 101.5, 101.5, 100, 99]
    assert feed.n == 5  # trades are not book updates


def test_raw_feed_sorts_out_of_order_arrivals():
    feed = RawFeed()
    feed.observe(np.array([0, 100_000, 86_000_000_000], dtype=np.int64))   # a chunk from the end of the day
    feed.observe(np.array([200_000, 300_000], dtype=np.int64))              # then back to the start
    assert feed.out_of_order == 1
    assert feed.first_ts == 0 and feed.last_ts == 86_000_000_000 and feed.n == 5
    assert feed.silences == [(300_000, 86_000_000_000)]  # one real silence, no day-long fake ones


def test_binance_rows_restored_to_book_order(tmp_path):
    from arbdata.normalize import normalize_binance_bt
    header = "update_id,best_bid_price,best_bid_qty,best_ask_price,best_ask_qty,transaction_time,event_time\n"
    rows = ["3,100.2,1,100.3,1,1003,1004", "1,100.0,1,100.1,1,1001,1002", "2,100.1,1,100.2,1,1002,1003"]
    path = tmp_path / "bt.zip"
    with zipfile.ZipFile(path, "w") as zf:
        zf.writestr("BTCUSDT-bookTicker.csv", header + "\n".join(rows) + "\n")
    df, feed = normalize_binance_bt(path)
    assert df.bid_px.tolist() == [100.0, 100.1, 100.2]
    assert feed.out_of_order == 1


def test_live_reader_keeps_flushed_data_of_a_killed_run(tmp_path):
    day = tmp_path / "2026-10-20"
    day.mkdir()
    def rec(recv, u):
        m = _msg("snapshot", recv // 1000, u, [["100", "1"]], [["101", "1"]])
        m["topic"] = "orderbook.1.BTCUSDT"
        return (json.dumps({"recv_us": recv, "msg": m}) + "\n").encode()
    # A run killed after a flush: valid data, then no gzip trailer.
    fh = gzip.open(day / "03_run1.jsonl.gz", "wb")
    fh.write(rec(1_000_000, 1) + rec(1_010_000, 2))
    fh.flush()
    raw = (day / "03_run1.jsonl.gz").read_bytes()
    fh.close()
    (day / "03_run1.jsonl.gz").write_bytes(raw)  # drop the trailer, as a kill would
    with gzip.open(day / "03_run2.jsonl.gz", "wb") as fh2:
        fh2.write(rec(5_000_000, 900))
    df, _ = normalize_bybit_live(day)
    assert df.avail_ts.tolist() == [1_000_000, 1_010_000, 5_000_000]
    assert df.resync.tolist() == [False, False, True]  # the restart is a resync


def test_binance_live_recording(tmp_path):
    from arbdata.normalize import normalize_binance_live
    day = tmp_path / "2026-10-20"
    day.mkdir()
    def rec(recv, u, b, a, B=1.0):
        return json.dumps({"recv_us": recv, "msg": {"stream": "btcusdt@bookTicker", "data": {
            "e": "bookTicker", "u": u, "s": "BTCUSDT", "b": str(b), "B": str(B), "a": str(a), "A": "2", "T": recv // 1000 - 5, "E": recv // 1000 - 4}}})
    lines = [rec(1_000_000, 10, 100.0, 100.1), rec(1_020_000, 12, 100.0, 100.1, B=3.0),  # size-only change
             rec(1_010_000, 11, 100.0, 100.1, B=2.0), rec(1_030_000, 13, 100.1, 100.2)]   # arrives out of order
    with gzip.open(day / "03_run.jsonl.gz", "wt") as fh:
        fh.write("\n".join(lines) + "\n")
    df, feed = normalize_binance_live(day)
    assert df.bid_px.tolist() == [100.0, 100.1] and df.n_raw.tolist() == [3, 1]
    assert df.avail_ts.tolist() == [1_000_000, 1_030_000] and df.exch_ts.iloc[0] == 995_000
    assert feed.n == 4


def test_collapser_keeps_the_smallest_size_of_each_price_run_across_batches():
    from arbdata.normalize import _RunCollapser
    c = _RunCollapser()
    ts = np.arange(5, dtype=np.int64)
    # run 1: price 100/101 with bid sizes 5, 2, 7 (split across two batches); run 2: new price
    c.add(ts[:2], ts[:2], np.array([100.0, 100.0]), np.array([5.0, 2.0]), np.array([101.0, 101.0]), np.array([4.0, 4.0]))
    c.add(ts[2:], ts[2:], np.array([100.0, 100.5, 100.5]), np.array([7.0, 3.0, 1.0]), np.array([101.0, 101.0, 101.0]),
          np.array([4.0, 6.0, 0.5]))
    f = c.frame()
    assert f.bid_sz.tolist() == [5.0, 3.0] and f.bid_sz_min.tolist() == [2.0, 1.0] and f.ask_sz_min.tolist() == [4.0, 0.5]
    assert f.n_raw.tolist() == [3, 2]
