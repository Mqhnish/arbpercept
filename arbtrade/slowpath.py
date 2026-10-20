"""The slow model's features, one quote at a time, for the live engine.

    .venv/bin/python -m arbtrade.slowpath                  # time it on synthetic quotes
    .venv/bin/python -m arbtrade.slowpath --replay 2026-10-20   # time it on our recordings

Offline, the slow path's features are computed for a whole day at once (arbdata/features.py and
arbdata/kalman.py, called from arbdata/episodes.py label_pair_day). The live engine sees one quote
at a time. SlowFeatures keeps the same statistics as running state, so at every price change it
gives the value the offline code gives for that row. tests/test_slowpath.py checks this on
synthetic quotes pushed through both paths.

Offline rows are price changes: a size-only update is folded into the price change before it
(arbdata/normalize.py). So the state here moves on price changes only. Size-only updates are
counted for the update rates, and they keep a feed alive.

At each price change, as offline:
  f_kalman_dev_bps, f_kalman_z   the log-spread log(b mid) - log(a mid) against a local-level Kalman
                                 filter's prediction from earlier rows (kalman.local_level)
  f_ou_halflife_s                mean-reversion half-life from 1 s bars of that deviation, completed
                                 seconds only (kalman.ou_halflife_s)
  f_rv_{w}s_bps                  realised volatility of the pair mid over (t - w, t]
  f_{leg}_rate_{w}s              raw updates per second over (t - w, t], credited as align.py does
  f_basis_bps, f_basis_dev_bps   b's mid over a's, and its gap to the median of earlier rows
  f_{leg}_spread_bps, f_{leg}_bid_notional, f_{leg}_ask_notional, f_{leg}_age_ms,
  f_hour_sin, f_hour_cos, f_weekend

A row is valid when both feeds have sent something within max_gap_ms. That is the rule quality.py
uses for a feed that is down. Invalid rows do not update the Kalman filter.

Not computed here, because the live engine has no input for them yet: book depth, feed lag (needs
exchange timestamps), trade flow (needs the trade feeds), f_edge_change_1s_bps and f_recent_births.

Two known differences from offline, both rare on live feeds:
- Updates that share one microsecond are one row offline, but separate rows here.
- Offline marks a resync (lost messages) as invalid. Live feeds have no resync flag.
"""

from __future__ import annotations

import argparse
import json
import math
import time
from collections import deque

from sortedcontainers import SortedList

NAN = math.nan
LOG2 = math.log(2)


class LocalLevel:
    """kalman.local_level, one row at a time."""

    def __init__(self, q_per_s: float, r: float):
        self.q, self.r = q_per_s, r
        self.m, self.p = NAN, 1e6
        self.last_t: int | None = None

    def step(self, t: int, y: float) -> tuple[float, float]:
        """The prediction for this row from earlier rows (level, variance), then the update with y.
        y = NaN (an invalid row) moves time on but does not update the level."""
        if self.last_t is None:
            self.last_t = t
        if math.isnan(self.m):
            if not math.isnan(y):
                self.m, self.p, self.last_t = y, self.r, t
            return NAN, NAN
        self.p = self.p + self.q * ((t - self.last_t) / 1e6)
        self.last_t = t
        m, p = self.m, self.p
        if not math.isnan(y):
            k = p / (p + self.r)
            self.m = m + k * (y - m)
            self.p = (1 - k) * p
        return m, p


class OUHalfLife:
    """kalman.ou_halflife_s, one row at a time.

    Each completed second puts its last value (as-of) on a 1 s grid. Consecutive grid values are
    the AR(1) pairs. A row gets the half-life from the pairs that end at the last completed second.
    As offline, window sums are differences of running totals since the first row, so both paths
    do the same arithmetic.
    """

    def __init__(self, window_s: int = 300, max_s: float = 3600.0):
        self.w, self.max_s = int(window_s), max_s
        self.sec: int | None = None          # the second of the latest row
        self.last = NAN                      # the latest row's value
        self.grid_prev: float | None = None  # the grid value of the last completed second
        self.tot = (0.0, 0.0, 0.0, 0.0, 0.0)  # running sums of x, y, x*x, x*y and the pair count
        self.cum = deque([self.tot], maxlen=self.w + 1)  # totals after each of the last w pairs, and before them
        self.n_pairs = 0
        self.hl = NAN

    def step(self, t: int, x: float) -> float:
        s = t // 1_000_000
        if self.sec is None:
            self.sec = s
        while self.sec < s:  # every second before this row's is now complete (after a long silence: ~1 µs each)
            self._close(self.last)
            self.sec += 1
        self.last = x
        return self.hl if self.n_pairs else NAN

    def _close(self, g: float) -> None:
        x, self.grid_prev = self.grid_prev, g
        if x is None:
            return
        ok = not (math.isnan(x) or math.isnan(g))
        x0, y0 = (x, g) if ok else (0.0, 0.0)
        sx, sy, sxx, sxy, n = self.tot
        self.tot = (sx + x0, sy + y0, sxx + x0 * x0, sxy + x0 * y0, n + (1.0 if ok else 0.0))
        self.cum.append(self.tot)
        self.n_pairs += 1
        lo, hi = self.cum[0], self.cum[-1]
        nn = hi[4] - lo[4]
        sx, sy, sxx, sxy = hi[0] - lo[0], hi[1] - lo[1], hi[2] - lo[2], hi[3] - lo[3]
        m = max(nn, 1.0)
        var = sxx - sx * sx / m
        b = (sxy - sx * sy / m) / var if nn >= self.w // 2 and var > 0 else NAN
        if 0 < b < 1:
            hl = LOG2 / -math.log(min(max(b, 1e-12), 1 - 1e-12))
        elif b >= 1:
            hl = self.max_s
        else:
            hl = NAN
        self.hl = self.max_s if hl > self.max_s else hl


def _window_us(window_s: float) -> int:
    """A window in µs, rounded to whole ms as pandas reads the offline windows ("1000ms")."""
    return int(window_s * 1000) * 1000


class WindowSum:
    """Sum of the values in (t - w, t], kept as pandas keeps a rolling sum.

    The running total is Kahan-compensated, so it does not drift over a day. It restarts when the
    window empties. A window of identical values gives exactly n times the value, so a quiet window
    reads exactly zero."""

    def __init__(self, window_s: float):
        self.w = _window_us(window_s)
        self.q: deque = deque()
        self._reset()

    def _reset(self) -> None:
        self.sum = self.c_add = self.c_rem = 0.0
        self.same, self.prev = 0, NAN

    def add(self, t: int, v: float) -> None:
        q, cut = self.q, t - self.w
        if q and q[0][0] <= cut:
            while q and q[0][0] <= cut:
                y = -q.popleft()[1] - self.c_rem
                s = self.sum + y
                self.c_rem = s - self.sum - y
                self.sum = s
            if not q:
                self._reset()
        q.append((t, v))
        y = v - self.c_add
        s = self.sum + y
        self.c_add = s - self.sum - y
        self.sum = s
        self.same = self.same + 1 if v == self.prev else 1
        self.prev = v

    def value(self) -> float:
        n = len(self.q)
        return self.prev * n if self.same >= n else self.sum


class TrailingMedian:
    """Median of the values in [t - w, t): features.trailing_reference, one row at a time.

    push() records a row's value. It counts only for later rows, so the newest value waits outside
    the sorted list until a later time asks. The median itself is only looked up by ref()."""

    def __init__(self, window_s: float):
        self.w = _window_us(window_s)
        self.q: deque = deque()
        self.sorted = SortedList()
        self.pending: tuple[int, float] | None = None

    def _settle(self, t: int) -> None:
        if self.pending is not None and self.pending[0] < t:
            self.q.append(self.pending)
            self.sorted.add(self.pending[1])
            self.pending = None
        while self.q and self.q[0][0] < t - self.w:
            self.sorted.remove(self.q.popleft()[1])

    def push(self, t: int, x: float) -> None:
        self._settle(t)
        self.pending = (t, x)

    def ref(self, t: int) -> float:
        """The median of values pushed before t, within the window."""
        self._settle(t)
        n = len(self.sorted)
        if n == 0:
            return NAN
        return self.sorted[n // 2] if n % 2 else (self.sorted[n // 2 - 1] + self.sorted[n // 2]) / 2


class SlowFeatures:
    """Every slow-path feature the live engine can compute, updated one quote at a time.

    cfg_features: the features section of config/sources.yaml (vol_windows_s, rate_windows_s,
    kalman_q_bps_per_sqrt_s, kalman_r_bps, ou_window_s). basis_ref_window_s: from the episodes
    section. max_gap_ms: the silence after which a feed counts as down."""

    def __init__(self, cfg_features: dict, basis_ref_window_s: float = 300.0, max_gap_ms: float = 5_000.0):
        f = cfg_features
        self.vol_w, self.rate_w = list(f["vol_windows_s"]), list(f["rate_windows_s"])
        self.r = (f.get("kalman_r_bps", 0.5) * 1e-4) ** 2
        self.kf = LocalLevel((f.get("kalman_q_bps_per_sqrt_s", 0.2) * 1e-4) ** 2, self.r)
        self.ou = OUHalfLife(int(f.get("ou_window_s", 300)))
        self.rv = [WindowSum(w) for w in self.vol_w]
        self.basis_ref = TrailingMedian(basis_ref_window_s)
        self.gap_us = int(max_gap_ms * 1000)
        # Per leg (0 = a, 1 = b): the book at its last price change, and raw-update bookkeeping.
        self.bid, self.ask, self.bsz, self.asz = [NAN, NAN], [NAN, NAN], [NAN, NAN], [NAN, NAN]
        self.t_change: list[int | None] = [None, None]
        self.t_raw: list[int | None] = [None, None]
        self.since = [0, 0]                 # size-only updates since the last price change
        self.rate_q = [[deque() for _ in self.rate_w] for _ in range(2)]  # (t, credit) per leg and window
        self.rate_n = [[0 for _ in self.rate_w] for _ in range(2)]
        self.last_log_mid = NAN
        self.t: int | None = None
        self.basis = self.dev = self.z = self.hl = NAN
        self.rate_us = [_window_us(w) for w in self.rate_w]
        legs = [f"f_{leg}_{k}" for leg in "ab" for k in ("spread_bps", "bid_notional", "ask_notional", "age_ms")]
        self._names = (*legs, "f_basis_bps", "f_basis_dev_bps", *(f"f_rv_{w}s_bps" for w in self.vol_w),
                       *(f"f_{leg}_rate_{w}s" for leg in "ab" for w in self.rate_w),
                       "f_kalman_dev_bps", "f_kalman_z", "f_ou_halflife_s", "f_hour_sin", "f_hour_cos", "f_weekend")

    def names(self) -> list[str]:
        """The feature names, as offline, in the order features() builds them."""
        return list(self._names)

    def update(self, leg: int, t: int, bid: float, ask: float, bsz: float, asz: float) -> bool:
        """One raw update of leg 0 (a) or 1 (b), in receive-time order. True if it was a price change."""
        self.t_raw[leg] = t
        if bid == self.bid[leg] and ask == self.ask[leg]:
            self.since[leg] += 1
            return False
        credit = 1 + self.since[leg]  # this price change and the size-only updates before it
        self.since[leg] = 0
        self.bid[leg], self.ask[leg], self.bsz[leg], self.asz[leg], self.t_change[leg] = bid, ask, bsz, asz, t
        self._row(leg, t, credit)
        return True

    def _row(self, leg: int, t: int, credit: int) -> None:
        self.t = t
        a_mid = (self.bid[0] + self.ask[0]) / 2
        b_mid = (self.bid[1] + self.ask[1]) / 2
        # realised volatility: squared log returns of the pair mid (zero until both legs have quoted)
        lm = math.log((a_mid + b_mid) / 2)
        r = lm - self.last_log_mid
        self.last_log_mid = lm
        r2 = 0.0 if math.isnan(r) else r * r
        for ws in self.rv:
            ws.add(t, r2)
        # update rates: each price change brings its credit; old credits leave the window
        for k in (0, 1):
            qs, ns = self.rate_q[k], self.rate_n[k]
            for j, w_us in enumerate(self.rate_us):
                q, cut = qs[j], t - w_us
                while q and q[0][0] <= cut:
                    ns[j] -= q.popleft()[1]
                if k == leg:
                    q.append((t, credit))
                    ns[j] += credit
        # Kalman deviation and its half-life: only rows where both feeds are alive update the filter
        ta, tb = self.t_raw
        valid = ta is not None and tb is not None and t - ta <= self.gap_us and t - tb <= self.gap_us
        spread = math.log(b_mid) - math.log(a_mid)
        m, p = self.kf.step(t, spread if valid else NAN)
        self.dev = spread - m
        self.z = self.dev / math.sqrt(p + self.r)
        self.hl = self.ou.step(t, self.dev)
        # basis against the median of earlier rows
        self.basis = (b_mid - a_mid) / a_mid * 1e4
        if not math.isnan(self.basis):
            self.basis_ref.push(t, self.basis)

    def features(self) -> dict[str, float]:
        """The features at the latest price change."""
        t = self.t
        vals: list[float] = []
        for k in (0, 1):
            bid, ask, tc = self.bid[k], self.ask[k], self.t_change[k]
            vals += [(ask - bid) / ((bid + ask) / 2) * 1e4, bid * self.bsz[k], ask * self.asz[k],
                     NAN if tc is None else (t - tc) / 1000]
        vals += [self.basis, self.basis - self.basis_ref.ref(t)]
        for ws in self.rv:
            v = ws.value()
            vals.append(math.sqrt(v) * 1e4 if v >= 0 else NAN)
        for k in (0, 1):
            vals += [n / w for n, w in zip(self.rate_n[k], self.rate_w)]
        hour = (t // 3_600_000_000) % 24 + ((t // 60_000_000) % 60) / 60
        vals += [self.dev * 1e4, self.z, self.hl, math.sin(2 * math.pi * hour / 24), math.cos(2 * math.pi * hour / 24),
                 float((t // 86_400_000_000 + 3) % 7 >= 5)]  # 1 Jan 1970 was a Thursday
        return dict(zip(self._names, vals))


# ---- timing -------------------------------------------------------------------------------

def synthetic_quotes(seconds: float = 600.0, step_ms: tuple[float, float] = (20.0, 10.0), seed: int = 0,
                     t0: int = 1_760_000_000_000_000) -> list[tuple]:
    """(t, leg, bid, ask, bsz, asz) for two venues quoting one random-walk price, in time order.
    About 30% of updates change a price; the rest change sizes only, as on real feeds."""
    import numpy as np
    rng = np.random.default_rng(seed)
    out = []
    for leg, step in enumerate(step_ms):
        n = int(seconds * 1000 / step)
        t = t0 + 2 * np.cumsum(rng.integers(int(step * 250), int(step * 750), n)) + leg  # even/odd: no shared stamps
        ticks = np.where(rng.random(n) < 0.3, rng.choice([-1, 1], n), 0)  # 0.1 price ticks
        bid = np.round((600_000 + leg + np.cumsum(ticks)) * 0.1, 1)
        sz = rng.uniform(0.1, 5, (n, 2))
        out += [(int(t[i]), leg, float(bid[i]), float(bid[i]) + 0.1, float(sz[i, 0]), float(sz[i, 1])) for i in range(n)]
    out.sort()
    return out


def benchmark(events: list[tuple], cfg_features: dict, basis_ref_window_s: float = 300.0,
              n_triggers: int = 5_000, seed: int = 0) -> dict:
    """Wall time of the slow path, one quote at a time, in µs.

    Every quote pays the update (means: update_us over all quotes, and split into price changes and
    size-only updates). A trigger also pays for building the feature vector and for the model
    (medians over n_triggers calls, as evaluate.measure_latencies times inference). The model is a
    compiled boosted model the size of SlowModel's (200 trees, up to 31 leaves), fitted to the
    stream's own feature vectors with made-up labels: only its size matters here. engine_*: the
    paper engine's whole on_quote, without and with the slow model."""
    import numpy as np
    from sklearn.ensemble import HistGradientBoostingClassifier

    from .compiled import CompiledTrees
    from .live import PaperEngine
    sf = SlowFeatures(cfg_features, basis_ref_window_s)
    names = sf.names()
    clock = time.perf_counter_ns
    rows, every = [], max(1, len(events) // 8_000)
    row_ns = size_ns = n_rows = 0
    for k, (t, leg, bid, ask, bsz, asz) in enumerate(events):
        t0 = clock()
        is_row = sf.update(leg, t, bid, ask, bsz, asz)
        dt = clock() - t0
        if is_row:
            row_ns, n_rows = row_ns + dt, n_rows + 1
        else:
            size_ns += dt
        if k % every == 0 and sf.t is not None:  # states to fit the model on (outside the timing)
            rows.append([sf.features()[n] for n in names])
    X = np.nan_to_num(np.asarray(rows, dtype=float))
    y = (np.random.default_rng(seed).random(len(X)) < 1 / (1 + np.exp(-X[:, names.index("f_kalman_z")]))).astype(int)
    ct = CompiledTrees(HistGradientBoostingClassifier(max_iter=200, learning_rate=0.05, max_leaf_nodes=31,
                                                      min_samples_leaf=20, early_stopping=False,
                                                      random_state=0).fit(X, y))

    def median_us(step) -> float:
        ts = []
        for _ in range(n_triggers):
            t0 = clock()
            step()
            ts.append(clock() - t0)
        return float(np.median(ts)) / 1e3

    x = np.array([sf.features()[n] for n in names])
    features_us = median_us(lambda: np.array([v for v in sf.features().values()]))
    inference_us = median_us(lambda: ct.predict_one(x))
    trigger_us = median_us(lambda: ct.predict_one(np.array([v for v in sf.features().values()])))

    def engine_us(slow) -> tuple[float, int]:
        e = PaperEngine(("a", "b"), 2.0, 1.0, {"a": 50.0, "b": 8.0}, slow=slow)
        t0 = clock()
        for t, leg, bid, ask, bsz, asz in events:
            e.on_quote("ab"[leg], t, bid, ask, bsz, asz)
        return (clock() - t0) / len(events) / 1e3, e.triggers
    plain_us, _ = engine_us(None)
    slow_us, triggers = engine_us({"model": ct, "features": names, "cfg_features": cfg_features,
                                   "basis_ref_window_s": basis_ref_window_s})
    n_size = len(events) - n_rows
    return {"quotes": len(events), "price_changes": n_rows, "features": len(names), "trees": ct.n_trees,
            "update_us": (row_ns + size_ns) / len(events) / 1e3, "update_price_change_us": row_ns / max(n_rows, 1) / 1e3,
            "update_size_only_us": size_ns / max(n_size, 1) / 1e3, "features_us": features_us,
            "inference_us": inference_us, "trigger_us": trigger_us, "engine_us_per_quote": plain_us,
            "engine_with_slow_us_per_quote": slow_us, "engine_triggers": triggers}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--replay", default=None, help="time it on a recorded date instead of synthetic quotes")
    ap.add_argument("--asset", default="BTC")
    ap.add_argument("--minutes", type=float, default=30.0, help="length of the synthetic stream")
    ap.add_argument("--repeats", type=int, default=3, help="runs to take the median over")
    ap.add_argument("--out", default=None, help="also write the result to this JSON file")
    args = ap.parse_args()
    import platform
    import statistics

    from arbdata.config import load_config
    cfg = load_config()
    if args.replay:
        from .live import replay_events
        venue = {"binance": 0, "bybit": 1}
        events = [(int(t), venue[v], bid, ask, bsz, asz) for t, v, bid, ask, bsz, asz in replay_events(cfg, args.replay, args.asset)]
    else:
        events = synthetic_quotes(args.minutes * 60)
    runs = [benchmark(events, cfg.features, cfg.episodes["basis_ref_window_s"]) for _ in range(args.repeats)]
    res = {k: statistics.median(r[k] for r in runs) if isinstance(v, float) else v for k, v in runs[0].items()}
    res.update(input=f"recordings {args.replay} {args.asset}" if args.replay else f"synthetic, {args.minutes:g} min",
               machine=f"{platform.processor()}, {platform.system()} {platform.release()}, Python {platform.python_version()}",
               runs=len(runs), note="µs values are medians over the runs (see benchmark() for what each one is)")
    print(json.dumps(res, indent=1))
    if args.out:
        with open(args.out, "w") as fh:
            json.dump(res, fh, indent=1)


if __name__ == "__main__":
    main()
