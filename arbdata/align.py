"""Put two quote streams on one event clock without looking ahead.

Every update of either leg is an event. At each event the other leg contributes its
most recent quote at or before that instant (an as-of join on avail_ts), which is
exactly what a trader watching both feeds would know at that moment.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from .quality import in_windows

LEG_COLUMNS = ["avail_ts", "exch_ts", "bid_px", "bid_sz", "ask_px", "ask_sz",
               "bid_depth5", "ask_depth5", "credit", "resync"]


def _with_credit(leg: pd.DataFrame) -> pd.DataFrame:
    """Raw updates known by each row's time.

    A row's own n_raw counts size updates that arrive after it, so it is credited only
    when the run closes, at the next price change: row i is credited with n_raw[i-1]
    (its own price change plus the previous run's trailing size updates).
    """
    n = leg.n_raw.to_numpy()
    credit = np.empty(len(n), dtype=np.int64)
    if len(n):
        credit[0] = 1
        credit[1:] = n[:-1]
    return leg.assign(credit=credit)


def align(a: pd.DataFrame, b: pd.DataFrame, down_a: np.ndarray, down_b: np.ndarray) -> pd.DataFrame:
    t = np.union1d(a.avail_ts.to_numpy(), b.avail_ts.to_numpy())
    out = pd.DataFrame({"t": t})
    for name, leg, down in (("a", a, down_a), ("b", b, down_b)):
        leg = _with_credit(leg)
        # Several updates sharing one timestamp: the last one is the state after that instant,
        # and the credits of all of them are known by then.
        credit = leg.groupby("avail_ts", sort=False).credit.transform("sum")
        leg = leg.assign(credit=credit)[LEG_COLUMNS].drop_duplicates("avail_ts", keep="last")
        leg = leg.rename(columns={c: f"{name}_{c}" for c in LEG_COLUMNS})
        out = pd.merge_asof(out, leg, left_on="t", right_on=f"{name}_avail_ts",
                            direction="backward", allow_exact_matches=True)
        present = out[f"{name}_avail_ts"].notna().to_numpy()
        out[f"{name}_age_ms"] = (out.t - out[f"{name}_avail_ts"]) / 1000  # time since the quote last changed
        out[f"{name}_lag_ms"] = (out[f"{name}_avail_ts"] - out[f"{name}_exch_ts"]) / 1000
        out[f"{name}_is_update"] = (out.t == out[f"{name}_avail_ts"]).to_numpy()
        # A resync row means messages before it were lost: that instant is not trustworthy.
        resync_now = out[f"{name}_is_update"].to_numpy() & (out[f"{name}_resync"].to_numpy() == True)  # noqa: E712 (NaN-safe)
        out[f"{name}_ok"] = present & ~in_windows(t, down) & ~resync_now
        out = out.drop(columns=[f"{name}_exch_ts", f"{name}_resync"])
    out["valid"] = out.a_ok & out.b_ok
    out = out.drop(columns=["a_ok", "b_ok"])
    out["a_mid"] = (out.a_bid_px + out.a_ask_px) / 2
    out["b_mid"] = (out.b_bid_px + out.b_ask_px) / 2
    return out
