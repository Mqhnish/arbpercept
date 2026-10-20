"""Slow-path statistics: a Kalman filter on the pair's log-spread, and an OU half-life.

Kalman (local level). The fair log-spread mu drifts as a random walk (variance q per second)
and each observation is mu plus noise (variance r). At every event the filter's prediction
uses only past data; the innovation z = (y - mu_pred) / sqrt(P_pred + r) says how surprising
the current spread is. For same-asset pairs the hedge ratio is 1, so the spread is the basis.
kalman_regression() is the two-state version (y = alpha + beta * x) for pairs of different
assets, where the hedge ratio itself drifts.

OU half-life. On a 1-second grid of the spread's deviation from the filtered level, an AR(1)
fit over a trailing window gives b; theta = -ln(b) / dt and half-life = ln 2 / theta. Only
completed seconds before an event are used.
"""

from __future__ import annotations

import numpy as np

try:
    from numba import njit
except ImportError:  # pragma: no cover - numba is optional, the maths is identical
    def njit(*args, **kwargs):
        return (lambda f: f) if not args or not callable(args[0]) else args[0]


@njit(cache=True)
def local_level(t_us, y, q_per_s, r):
    n = len(y)
    m_pred = np.empty(n)
    p_pred = np.empty(n)
    m, p = np.nan, 1e6
    last_t = t_us[0] if n else 0
    for i in range(n):
        if np.isnan(m):
            if not np.isnan(y[i]):
                m, p = y[i], r
                last_t = t_us[i]
            m_pred[i], p_pred[i] = np.nan, np.nan
            continue
        dt = (t_us[i] - last_t) / 1e6
        last_t = t_us[i]
        p = p + q_per_s * dt
        m_pred[i], p_pred[i] = m, p
        if not np.isnan(y[i]):
            k = p / (p + r)
            m = m + k * (y[i] - m)
            p = (1 - k) * p
    return m_pred, p_pred


@njit(cache=True)
def kalman_regression(t_us, y, x, q_alpha, q_beta, r):
    """State (alpha, beta), both random walks; returns predicted alpha, beta and innovation z."""
    n = len(y)
    a_out, b_out, z_out = np.empty(n), np.empty(n), np.empty(n)
    a, b = 0.0, 1.0
    P00, P01, P11 = 1.0, 0.0, 1.0
    last_t = t_us[0] if n else 0
    for i in range(n):
        dt = (t_us[i] - last_t) / 1e6
        last_t = t_us[i]
        P00 += q_alpha * dt
        P11 += q_beta * dt
        a_out[i], b_out[i] = a, b
        if np.isnan(y[i]) or np.isnan(x[i]):
            z_out[i] = np.nan
            continue
        e = y[i] - (a + b * x[i])
        s = P00 + 2 * x[i] * P01 + x[i] * x[i] * P11 + r
        z_out[i] = e / np.sqrt(s)
        k0 = (P00 + x[i] * P01) / s
        k1 = (P01 + x[i] * P11) / s
        a += k0 * e
        b += k1 * e
        n00 = P00 - k0 * (P00 + x[i] * P01)
        n01 = P01 - k0 * (P01 + x[i] * P11)
        n11 = P11 - k1 * (P01 + x[i] * P11)
        P00, P01, P11 = n00, n01, n11
    return a_out, b_out, z_out


def ou_halflife_s(t_us: np.ndarray, dev: np.ndarray, window_s: int = 300, max_s: float = 3600.0) -> np.ndarray:
    """Half-life (s) of mean reversion of dev, from completed 1 s bars before each event."""
    n = len(t_us)
    out = np.full(n, np.nan)
    if n == 0:
        return out
    t0 = (t_us[0] // 1_000_000) * 1_000_000
    k = (t_us - t0) // 1_000_000  # the second each event falls in
    nsec = int(k[-1]) + 1
    # value at the end of each second = last observation within or before it (as-of)
    last_idx = np.searchsorted(t_us, t0 + (np.arange(nsec) + 1) * 1_000_000, side="left") - 1
    grid = np.where(last_idx >= 0, dev[np.maximum(last_idx, 0)], np.nan)
    x, y = grid[:-1], grid[1:]
    ok = ~(np.isnan(x) | np.isnan(y))
    x0, y0 = np.where(ok, x, 0.0), np.where(ok, y, 0.0)
    c = lambda v: np.concatenate(([0.0], np.cumsum(v)))
    Sx, Sy, Sxx, Sxy, N = c(x0), c(y0), c(x0 * x0), c(x0 * y0), c(ok.astype(float))
    # regression over pairs ending at second j uses pairs (j - window, j]
    j = np.arange(len(x))
    lo = np.maximum(j + 1 - window_s, 0)
    hi = j + 1
    nn = N[hi] - N[lo]
    sx, sy, sxx, sxy = Sx[hi] - Sx[lo], Sy[hi] - Sy[lo], Sxx[hi] - Sxx[lo], Sxy[hi] - Sxy[lo]
    var = sxx - sx * sx / np.maximum(nn, 1)
    b = np.where((nn >= window_s // 2) & (var > 0), (sxy - sx * sy / np.maximum(nn, 1)) / np.where(var > 0, var, 1), np.nan)
    hl = np.where((b > 0) & (b < 1), np.log(2) / -np.log(np.clip(b, 1e-12, 1 - 1e-12)), np.where(b >= 1, max_s, np.nan))
    hl = np.minimum(hl, max_s)
    # an event in second k may use pairs ending at second k-1 at the latest (completed seconds only)
    use = k.astype(np.int64) - 2  # pair index j covers seconds (j, j+1); last completed pair ends at second k-1
    valid = use >= 0
    out[valid] = hl[np.minimum(use[valid], len(hl) - 1)]
    return out
