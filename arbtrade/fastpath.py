"""The fast path: a compiled, allocation-free check of the fee-adjusted cross-venue gap.

stream_triggers() walks a merged update stream exactly as a live loop would: on every
update it refreshes that venue's best bid and ask and tests both trade directions against
the trigger threshold. It fires on the update where a gap opens (not on every update while
it stays open). benchmark() times it on real data.
"""

from __future__ import annotations

import time

import numpy as np

try:
    from numba import njit
except ImportError:  # pragma: no cover
    def njit(*args, **kwargs):
        return (lambda f: f) if not args or not callable(args[0]) else args[0]


@njit(cache=True)
def stream_triggers(venue, bid, ask, threshold_bps):
    """venue[i] is 0 or 1; returns the event indices where a direction's gap opens and the direction
    (+1: sell venue 0, buy venue 1; -1: sell venue 1, buy venue 0)."""
    n = len(venue)
    out_idx = np.empty(n, np.int64)
    out_dir = np.empty(n, np.int8)
    k = 0
    b0 = a0 = b1 = a1 = np.nan
    open_fwd = open_bwd = False
    for i in range(n):
        if venue[i] == 0:
            b0, a0 = bid[i], ask[i]
        else:
            b1, a1 = bid[i], ask[i]
        if np.isnan(b0) or np.isnan(b1):
            continue
        mid = 0.25 * (b0 + a0 + b1 + a1)
        fwd = (b0 - a1) / mid * 1e4 > threshold_bps
        bwd = (b1 - a0) / mid * 1e4 > threshold_bps
        if fwd and not open_fwd:
            out_idx[k], out_dir[k] = i, 1
            k += 1
        if bwd and not open_bwd:
            out_idx[k], out_dir[k] = i, -1
            k += 1
        open_fwd, open_bwd = fwd, bwd
    return out_idx[:k], out_dir[:k]


def merged_stream(leg_a, leg_b) -> tuple[np.ndarray, ...]:
    """Merge two L1 tables into one update stream ordered by avail_ts."""
    t = np.concatenate([leg_a.avail_ts.to_numpy(), leg_b.avail_ts.to_numpy()])
    v = np.concatenate([np.zeros(len(leg_a), np.int8), np.ones(len(leg_b), np.int8)])
    bid = np.concatenate([leg_a.bid_px.to_numpy(), leg_b.bid_px.to_numpy()])
    ask = np.concatenate([leg_a.ask_px.to_numpy(), leg_b.ask_px.to_numpy()])
    o = np.argsort(t, kind="stable")
    return t[o], v[o], bid[o], ask[o]


def benchmark(leg_a, leg_b, threshold_bps: float, repeats: int = 5) -> dict:
    t, v, bid, ask = merged_stream(leg_a, leg_b)
    stream_triggers(v[:100], bid[:100], ask[:100], threshold_bps)  # compile outside the timing
    best = np.inf
    for _ in range(repeats):
        t0 = time.perf_counter()
        idx, _ = stream_triggers(v, bid, ask, threshold_bps)
        best = min(best, time.perf_counter() - t0)
    return {"updates": int(len(v)), "triggers": int(len(idx)), "seconds": best, "ns_per_update": best / len(v) * 1e9}
