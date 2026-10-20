"""Data quality: clean obviously broken quotes, find feed outages, and measure the rest.

Cleaning only removes rows that cannot be real tradable quotes. Everything else is
measured and reported, so exclusions are explicit decisions rather than silent drops.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

DAY_US = 86_400_000_000


def clean(df: pd.DataFrame, spike_bps: float) -> tuple[pd.DataFrame, dict[str, int]]:
    dropped: dict[str, int] = {}

    bad = ~((df.bid_px > 0) & (df.ask_px > 0) & (df.bid_sz > 0) & (df.ask_sz > 0))
    dropped["nonpositive"] = int(bad.sum())
    df = df[~bad]

    # A locked or crossed book on a single venue means a missed update, not an opportunity.
    crossed = df.bid_px >= df.ask_px
    dropped["crossed_or_locked"] = int(crossed.sum())
    df = df[~crossed]

    # Isolated spikes: one update jumps by more than spike_bps and the next one reverts.
    mid = ((df.bid_px + df.ask_px) / 2).to_numpy()
    if len(mid) > 2:
        lr = np.log(mid)
        jump_in = np.abs(lr[1:-1] - lr[:-2]) * 1e4
        revert = np.abs(lr[2:] - lr[:-2]) * 1e4
        spike = np.zeros(len(mid), dtype=bool)
        spike[1:-1] = (jump_in > spike_bps) & (revert < spike_bps / 2)
        dropped["spikes"] = int(spike.sum())
        df = df[~spike]
    else:
        dropped["spikes"] = 0

    return df.reset_index(drop=True), dropped


def down_windows(silences: pd.DataFrame, last_raw_ts: int | None, day_start_us: int,
                 max_gap_ms: float) -> np.ndarray:
    """Intervals (start, end) during which a feed counts as down.

    A feed is down from max_gap after its last raw update until the next raw update
    arrives. Knowing this at time t needs only updates at or before t, so it is causal.
    """
    g = int(max_gap_ms * 1000)
    long = silences[(silences.end_ts - silences.start_ts) > g]
    w = [np.column_stack([long.start_ts.to_numpy() + g, long.end_ts.to_numpy()])]
    day_end = day_start_us + DAY_US
    if last_raw_ts is not None and day_end - last_raw_ts > g:
        w.append(np.array([[last_raw_ts + g, np.iinfo(np.int64).max]]))
    return np.concatenate(w).astype(np.int64)


def in_windows(t: np.ndarray, windows: np.ndarray) -> np.ndarray:
    """True where t falls inside any (start, end) window (start exclusive, end exclusive)."""
    if len(windows) == 0:
        return np.zeros(len(t), dtype=bool)
    order = np.argsort(windows[:, 0])
    ws, we = windows[order, 0], windows[order, 1]
    i = np.searchsorted(ws, t, side="left") - 1
    return (i >= 0) & (t < we[np.maximum(i, 0)])


def assess(df: pd.DataFrame, silences: pd.DataFrame, first_raw_ts: int | None, last_raw_ts: int | None,
           n_raw: int, day_start_us: int, max_gap_ms: float) -> dict[str, float]:
    if df.empty or first_raw_ts is None:
        return {"rows": 0, "raw_updates": n_raw, "coverage": 0.0}
    g = max_gap_ms * 1000
    day_end = day_start_us + DAY_US
    dur = (silences.end_ts - silences.start_ts).to_numpy()
    edges = np.array([first_raw_ts - day_start_us, day_end - last_raw_ts])
    all_gaps = np.concatenate([dur, edges])
    down = all_gaps[all_gaps > g]
    t = df.avail_ts.to_numpy()
    lag_ms = (df.avail_ts - df.exch_ts).to_numpy() / 1000
    step_ms = np.diff(t) / 1000
    mid = (df.bid_px + df.ask_px) / 2
    spread_bps = ((df.ask_px - df.bid_px) / mid * 1e4).to_numpy()
    # Daily realised volatility from 1-minute mids: used to check that every split
    # contains comparable market regimes.
    minute_mid = pd.Series(mid.to_numpy(), index=pd.to_datetime(t, unit="us")).resample("1min").last().dropna()
    rv_bps = float(np.sqrt(np.sum(np.diff(np.log(minute_mid.to_numpy())) ** 2)) * 1e4) if len(minute_mid) > 1 else float("nan")
    return {
        "rows": int(len(df)),
        "raw_updates": int(n_raw),
        "coverage": float(1 - down.sum() / DAY_US),
        "n_outages": int(len(down)),
        "max_raw_silence_s": float(all_gaps.max() / 1e6),
        "resyncs": int(df.resync.sum()),
        "price_change_step_ms_median": float(np.median(step_ms)) if len(step_ms) else float("nan"),
        "feed_lag_ms_median": float(np.median(lag_ms)),
        "feed_lag_ms_p99": float(np.percentile(lag_ms, 99)),
        "feed_lag_negative_share": float((lag_ms < 0).mean()),
        "spread_bps_median": float(np.median(spread_bps)),
        "daily_rv_bps": rv_bps,
        "first_raw_ts": int(first_raw_ts),
        "last_raw_ts": int(last_raw_ts),
        "mid_first": float(mid.iloc[0]),
        "mid_last": float(mid.iloc[-1]),
    }


TRADE_SHIFTS_MS = (-500, -200, -100, -50, -20, 0, 20, 50, 100, 200, 500)
FAR_BPS = 5.0
ANOMALY_OUT_SHARE = 0.5    # a minute is anomalous if most of its trades print outside the band
ANOMALY_MIN_TRADES = 20


def trade_consistency(book: pd.DataFrame, trades: pd.DataFrame) -> dict[str, float]:
    """Check reconstructed quotes against Bybit's independent trade record.

    Each trade (matching-engine time) is placed between the two book snapshots that
    bracket it on the same matching-engine clock, giving a band from the lower bid to
    the higher ask. Large orders sweep several levels, so prints slightly beyond the band
    on the aggressor's side are normal. Two things are not:
      wrong_side_share  buyer-initiated prints below the band or seller-initiated above it
      far_share         prints more than FAR_BPS beyond the band
    Both rise on volatile days too, so they are reported but do not decide pass or fail.
    What separates a broken book from a fast market is persistence: the longest run of
    consecutive minutes in which most trades print outside the band (planted faults: a
    10-minute corrupted book gives a 10-minute run, real days at most 2). The shift that
    maximises the in-band share estimates any clock offset between trade and book feeds.
    RPI trades are excluded because RPI orders are hidden from the public book stream.
    """
    t = trades[~trades.rpi]
    out: dict[str, float] = {"n_trades": int(len(trades)), "rpi_share": float(trades.rpi.mean()) if len(trades) else 0.0}
    if t.empty or book.empty:
        return out
    b = book.sort_values("exch_ts", kind="stable")
    bt = b.exch_ts.to_numpy()
    bid, ask = b.bid_px.to_numpy(), b.ask_px.to_numpy()
    px, side, ts = t.price.to_numpy(), t.side.to_numpy(), t.ts.to_numpy()

    def bracket(shift_ms):
        i = np.searchsorted(bt, ts + shift_ms * 1000, side="right") - 1
        ok = (i >= 0) & (i + 1 < len(bt))
        i = i[ok]
        return ok, np.minimum(bid[i], bid[i + 1]), np.maximum(ask[i], ask[i + 1]), (bid[i] + ask[i]) / 2

    shares = {}
    for shift in TRADE_SHIFTS_MS:
        ok, lo, hi = bracket(shift)[:3]
        shares[shift] = float(np.mean((px[ok] >= lo) & (px[ok] <= hi))) if ok.any() else float("nan")
    ok, lo, hi, mid = bracket(0)
    p, sd = px[ok], side[ok]
    above, below = p > hi, p < lo
    beyond_bps = np.where(above, p - hi, np.where(below, lo - p, 0.0)) / mid * 1e4
    best = max(shares, key=lambda k: (shares[k], -abs(k)))  # ties go to the smallest offset
    # Persistence: market sweeps are brief bursts, a broken book is wrong for minutes on end.
    minute = ts[ok] // 60_000_000
    m = pd.DataFrame({"minute": minute, "out": above | below}).groupby("minute").out.agg(["mean", "size"])
    bad = ((m["mean"] > ANOMALY_OUT_SHARE) & (m["size"] >= ANOMALY_MIN_TRADES))
    bad = bad.reindex(range(int(m.index.min()), int(m.index.max()) + 1), fill_value=False).to_numpy()
    run = longest = 0
    for x in bad:
        run = run + 1 if x else 0
        longest = max(longest, run)
    out.update({
        "anomalous_minute_share": float(bad.mean()),
        "longest_anomaly_run_min": int(longest),
        "in_band_share": shares[0],
        "sweep_share": float(np.mean((above & (sd > 0)) | (below & (sd < 0)))),
        "wrong_side_share": float(np.mean((above & (sd < 0)) | (below & (sd > 0)))),
        "far_share": float(np.mean(beyond_bps > FAR_BPS)),
        "best_shift_ms": best,
    })
    return out
