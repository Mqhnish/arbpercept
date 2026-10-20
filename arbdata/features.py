"""Causal features describing the market at the instant an opportunity is born.

Rule: a feature at time t may use only rows with t' <= t. Trailing windows are
right-closed at t (the current update is known at t). Anything that defines a
reference level the label is measured against (the "normal" basis) is left-closed,
so the current update is compared with history rather than with itself.
tests/test_no_lookahead.py enforces this by truncating the future and checking that
every feature is unchanged.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def _time_index(t: np.ndarray) -> pd.DatetimeIndex:
    return pd.DatetimeIndex(pd.to_datetime(t, unit="us"))


def trailing_reference(t: np.ndarray, x: np.ndarray, window_s: float) -> np.ndarray:
    """Median of x over (t - window, t): strictly past values only."""
    s = pd.Series(x, index=_time_index(t))
    return s.rolling(f"{int(window_s * 1000)}ms", closed="left").median().to_numpy()


def rolling_context(al: pd.DataFrame, vol_windows_s: list[float], rate_windows_s: list[float]) -> dict[str, np.ndarray]:
    """Trailing-window series over every event; features index into these at births."""
    idx = _time_index(al.t.to_numpy())
    mid_ref = ((al.a_mid + al.b_mid) / 2).to_numpy()
    r = np.zeros(len(mid_ref))
    r[1:] = np.diff(np.log(mid_ref))
    r = np.nan_to_num(r)
    r2 = pd.Series(r * r, index=idx)
    ctx: dict[str, np.ndarray] = {}
    for w in vol_windows_s:
        ctx[f"f_rv_{w}s_bps"] = np.sqrt(r2.rolling(f"{int(w * 1000)}ms").sum().to_numpy()) * 1e4
    for leg in ("a", "b"):
        # Raw updates per second, counting only updates already known at each instant.
        upd = pd.Series(np.where(al[f"{leg}_is_update"], al[f"{leg}_credit"].fillna(0), 0).astype(float), index=idx)
        for w in rate_windows_s:
            ctx[f"f_{leg}_rate_{w}s"] = upd.rolling(f"{int(w * 1000)}ms").sum().to_numpy() / w
    return ctx


def features_at(al: pd.DataFrame, ctx: dict[str, np.ndarray], basis_dev_bps: np.ndarray,
                idx: np.ndarray) -> pd.DataFrame:
    row = al.iloc[idx]
    f: dict[str, np.ndarray] = {}
    for leg in ("a", "b"):
        mid = row[f"{leg}_mid"].to_numpy()
        bid, ask = row[f"{leg}_bid_px"].to_numpy(), row[f"{leg}_ask_px"].to_numpy()
        f[f"f_{leg}_spread_bps"] = (ask - bid) / mid * 1e4
        f[f"f_{leg}_bid_notional"] = bid * row[f"{leg}_bid_sz"].to_numpy()
        f[f"f_{leg}_ask_notional"] = ask * row[f"{leg}_ask_sz"].to_numpy()
        f[f"f_{leg}_bid_depth5_notional"] = bid * row[f"{leg}_bid_depth5"].to_numpy()
        f[f"f_{leg}_ask_depth5_notional"] = ask * row[f"{leg}_ask_depth5"].to_numpy()
        f[f"f_{leg}_age_ms"] = row[f"{leg}_age_ms"].to_numpy()
        f[f"f_{leg}_lag_ms"] = row[f"{leg}_lag_ms"].to_numpy()
    a_mid, b_mid = row.a_mid.to_numpy(), row.b_mid.to_numpy()
    f["f_basis_bps"] = (b_mid - a_mid) / a_mid * 1e4
    f["f_basis_dev_bps"] = basis_dev_bps[idx]
    for k, v in ctx.items():
        f[k] = v[idx]
    ts = pd.to_datetime(row.t.to_numpy(), unit="us", utc=True)
    hour = ts.hour.to_numpy() + ts.minute.to_numpy() / 60
    f["f_hour_sin"] = np.sin(2 * np.pi * hour / 24)
    f["f_hour_cos"] = np.cos(2 * np.pi * hour / 24)
    f["f_weekend"] = (ts.dayofweek.to_numpy() >= 5).astype(np.int8)
    return pd.DataFrame(f)


def trade_flow_at(trades: pd.DataFrame | None, birth_ts: np.ndarray, windows_s: list[float],
                  margin_us: int, leg: str) -> dict[str, np.ndarray]:
    """Order flow from trades stamped at least margin_us before each birth.

    Trades carry matching-engine time but reach an observer a little later, so a trade
    stamped just before a birth may not have been seen yet. Only trades with
    ts <= birth - margin count, within a trailing window of that cut-off.
    Without a trade record for the leg the columns are NaN, never zero.
    """
    out: dict[str, np.ndarray] = {}
    if trades is None or trades.empty:
        for w in windows_s:
            for name in ("trades_per_s", "notional_per_s", "flow_imbalance"):
                out[f"f_{leg}_{name}_{w}s"] = np.full(len(birth_ts), np.nan)
        return out
    ts = trades.ts.to_numpy()
    notional = (trades.price * trades["size"]).to_numpy()
    cs_n = np.concatenate(([0.0], np.cumsum(notional)))
    cs_s = np.concatenate(([0.0], np.cumsum(notional * trades.side.to_numpy())))
    cut = birth_ts - margin_us
    hi = np.searchsorted(ts, cut, side="right")
    for w in windows_s:
        lo = np.searchsorted(ts, cut - int(w * 1e6), side="right")
        total = cs_n[hi] - cs_n[lo]
        out[f"f_{leg}_trades_per_s_{w}s"] = (hi - lo) / w
        out[f"f_{leg}_notional_per_s_{w}s"] = total / w
        out[f"f_{leg}_flow_imbalance_{w}s"] = np.where(total > 0, (cs_s[hi] - cs_s[lo]) / np.where(total > 0, total, 1), 0.0)
    return out
