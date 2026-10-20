import gzip

import numpy as np
import pandas as pd

from arbdata.normalize import normalize_bybit_trades
from arbdata.quality import trade_consistency


def _gz(tmp_path, name, text):
    path = tmp_path / name
    with gzip.open(path, "wt") as fh:
        fh.write(text)
    return path


def test_linear_and_spot_formats(tmp_path):
    lin = _gz(tmp_path, "lin.csv.gz",
              "timestamp,symbol,side,size,price,tickDirection,trdMatchID,grossValue,homeNotional,foreignNotional,RPI\n"
              "1790812800.1031,BTCUSDT,Buy,0.001,100.5,ZeroPlusTick,x,1,0.001,0.1,0\n"
              "1790812800.015,BTCUSDT,Sell,0.042,100.0,MinusTick,y,1,0.042,4.2,1\n")
    df = normalize_bybit_trades(lin, "linear")
    assert df.ts.tolist() == [1790812800015000, 1790812800103100]  # sorted, microseconds
    assert df.side.tolist() == [-1, 1] and df.rpi.tolist() == [True, False]
    spot = _gz(tmp_path, "spot.csv.gz", "id,timestamp,price,volume,side,rpi\n1,1790812800247,100.1,0.5,sell,0\n")
    df = normalize_bybit_trades(spot, "spot")
    assert df.ts.tolist() == [1790812800247000] and df.side.tolist() == [-1] and df["size"].tolist() == [0.5]


def _book_and_trades(shift_ms=0):
    t = np.arange(0, 100_000_000, 100_000, dtype=np.int64)  # 100 ms snapshots for 100 s
    mid = 100 + np.cumsum(np.random.default_rng(0).normal(0, 0.3, len(t)))
    book = pd.DataFrame({"exch_ts": t, "bid_px": mid - 0.05, "ask_px": mid + 0.05})
    i = np.arange(0, len(t) - 1, 3)
    side = np.where(i % 2 == 0, 1, -1)
    trades = pd.DataFrame({"ts": t[i] + 40_000 + shift_ms * 1000,
                           "price": np.where(side > 0, book.ask_px.to_numpy()[i], book.bid_px.to_numpy()[i]),
                           "size": 1.0, "side": side, "rpi": False})
    return book, trades


def test_consistent_trades_pass():
    c = trade_consistency(*_book_and_trades())
    assert c["in_band_share"] == 1.0 and c["wrong_side_share"] == 0.0 and c["far_share"] == 0.0
    assert c["best_shift_ms"] == 0


def test_clock_offset_is_detected():
    book, trades = _book_and_trades(shift_ms=200)  # trade clock 200 ms ahead of the book's
    c = trade_consistency(book, trades)
    assert c["best_shift_ms"] == -200
    assert c["in_band_share"] < 1.0


def _long_day(minutes=30):
    rng = np.random.default_rng(1)
    t = np.arange(0, minutes * 60_000_000, 100_000, dtype=np.int64)
    mid = 100 + np.cumsum(rng.normal(0, 0.05, len(t)))
    book = pd.DataFrame({"exch_ts": t, "bid_px": mid - 0.05, "ask_px": mid + 0.05})
    i = np.arange(0, len(t) - 1, 2)
    side = rng.choice([-1, 1], len(i))
    trades = pd.DataFrame({"ts": t[i] + 50_000, "size": 1.0, "side": side, "rpi": False,
                           "price": np.where(side > 0, book.ask_px.to_numpy()[i], book.bid_px.to_numpy()[i])})
    return book, trades


def test_persistent_book_fault_is_caught():
    book, trades = _long_day()
    clean = trade_consistency(book, trades)
    assert clean["longest_anomaly_run_min"] == 0
    bad = book.copy()
    w = (bad.exch_ts >= 600_000_000) & (bad.exch_ts < 1_200_000_000)  # wrong for 10 minutes
    bad.loc[w, ["bid_px", "ask_px"]] += 1.0
    c = trade_consistency(bad, trades)
    assert c["longest_anomaly_run_min"] >= 9


def test_clock_skew_is_caught_by_shift():
    book, trades = _long_day()
    c = trade_consistency(book.assign(exch_ts=book.exch_ts + 300_000), trades)
    assert abs(c["best_shift_ms"]) >= 200
