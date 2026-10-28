"""Live paper trading: the fast path and decay prior running on real feeds, with paper fills.

    .venv/bin/python -m arbtrade.live --minutes 10                 # live Binance + Bybit BTC perpetual
    .venv/bin/python -m arbtrade.live --replay 2026-10-20          # the same engine over our recordings

One engine serves both modes, so the live demo is testable offline. Every quote update goes
through PaperEngine.on_quote in receive-time order:
  1. orders whose arrival time has passed are filled or rejected against that venue's book
     as it stood when they arrived (the state before this update);
  2. the update is applied;
  3. the fast path checks both directions; when a gap opens above the trigger, each policy
     decides, and a traded pair sends one IOC order per venue, each arriving after that
     venue's own latency. A one-sided fill is closed one latency later.
Policies run side by side on the same triggers: "naive" trades everything, "prior" trades
when the decay prior's expected value is positive, and "slow" (optional) trades when a compiled
slow model's expected value is positive.

Gaps are measured against the venues' usual offset (offset_window_s, 300 s by default; 0 turns
it off), as in `arbtrade.evaluate --offset-aware`: the trailing median of venue a's mid minus
venue b's mid, sampled at price changes while both books are fresh, using only earlier samples.
A persistent offset is not a gap. Until the first sample exists, nothing triggers. The prior
must have been trained the same way (--train-prior); a prior trained on raw gaps is not used.

The slow model (slow=..., see PaperEngine) is a CompiledTrees model (arbtrade/compiled.py). Its
features come from arbtrade/slowpath.py, which updates them on every quote and matches the offline
features value for value. It is only usable from Python for now: the command line has no way yet to
train one on recorded days or load one from disk.

Every trigger gets a recorded decision per policy, with its reason, checked in this order:
  SKIP_STALE      a venue's book has not updated for stale_ms (a dead feed, not a quiet book:
                  Bybit stays silent for up to ~3 s when nothing changes)
  SKIP_THIN       the size both books show is worth less than min_notional
  SKIP_EV         the model's expected value is not positive (prior and slow policies)
  SKIP_INVENTORY  the trade would push the policy's net position past cap_usd; trades that
                  shrink the position always pass (see inventory.py for why positions matter)
  ENTER           orders sent
"""

from __future__ import annotations

import argparse
import asyncio
import json
import math
import time
from collections import deque
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
from sortedcontainers import SortedList

from .policies import FAST_FEATURES
from .slowpath import SlowFeatures

# Feature settings a slow model bundle uses unless it carries its own (as in config/sources.yaml).
SLOW_FEATURE_DEFAULTS = {"vol_windows_s": [1, 10, 60], "rate_windows_s": [1, 10], "kalman_q_bps_per_sqrt_s": 0.2,
                         "kalman_r_bps": 0.5, "ou_window_s": 300}


@dataclass
class Book:
    bid: float = math.nan
    ask: float = math.nan
    bsz: float = 0.0
    asz: float = 0.0
    t: int = 0              # receive time of the last update (µs)
    t_change: int = 0       # receive time of the last price change (µs)


@dataclass
class Order:
    venue: str
    side: int               # +1 buy, -1 sell
    limit: float
    qty: float
    arrive: int
    group: int
    filled: float = 0.0
    price: float = math.nan
    done: bool = False


@dataclass
class Trade:
    policy: str
    t: int
    edge_bps: float
    features: dict = field(default_factory=dict)
    orders: list = field(default_factory=list)
    unwind: list = field(default_factory=list)
    pnl: float = 0.0
    settled: bool = False
    dq_a_intended: float = 0.0


class PaperEngine:
    """slow (optional): a slow model bundle, a dict with
         model               a CompiledTrees (arbtrade/compiled.py)
         features            the model's input columns, in order
         loss_bps            average outcome of a trade that does not fully fill (default: loss_bps)
         cal_x, cal_y        an isotonic calibration (optional), as for the prior
         cfg_features        feature settings it was trained with (default SLOW_FEATURE_DEFAULTS)
         basis_ref_window_s  default 300
    A model that needs a feature the engine cannot compute live is refused."""

    def __init__(self, venues: tuple[str, str], trigger_bps: float, fee_bps: float, latency_ms: dict[str, float],
                 notional: float = 10_000.0, prior: dict | None = None, loss_bps: float = -1.0,
                 stale_ms: float = 5_000.0, cap_usd: float = math.inf, min_notional: float = 100.0,
                 offset_window_s: float | None = None, slow: dict | None = None):
        self.va, self.vb = venues
        self.books = {v: Book() for v in venues}
        self.trigger, self.fee = trigger_bps, fee_bps / 1e4
        self.lat = {v: int(latency_ms[v] * 1000) for v in venues}
        self.notional = notional
        self.prior, self.loss_bps = prior, loss_bps
        self.open_dir = {+1: False, -1: False}
        self.pending: list[Order] = []
        self.trades: list[Trade] = []
        self.unsettled: list[Trade] = []
        self.mid_hist: deque = deque()  # (t, squared log return of the pair mid) over the last second
        self.last_mid = math.nan
        self.triggers = 0
        self.stale_us, self.cap_usd, self.min_notional = int(stale_ms * 1000), cap_usd, min_notional
        self.pos: dict[str, float] = {}       # per policy: net position on venue a (base units), incl. orders in flight
        self.decisions: list[dict] = []
        # The venues' usual offset: a-minus-b mid samples (bps) over the trailing window, kept sorted for the median.
        self.off_win_us = int(offset_window_s * 1e6) if offset_window_s else 0
        self.off_samples: deque = deque()
        self.off_sorted = SortedList()
        # The slow model and its features, updated on every quote (a book counts as down after stale_ms).
        self.slow, self.sf, self.slow_us = slow, None, []
        if slow is not None:
            self.sf = SlowFeatures(slow.get("cfg_features", SLOW_FEATURE_DEFAULTS),
                                   slow.get("basis_ref_window_s", 300.0), max_gap_ms=stale_ms)
            missing = [f for f in slow["features"] if f not in self.sf.names() and f not in FAST_FEATURES]
            if missing:
                raise ValueError(f"the slow model needs features the live engine cannot compute: {missing}")

    # ---- the venues' usual offset -------------------------------------------------------
    def offset_ref(self, t: int) -> float:
        """Median of the offset samples in [t - window, t): strictly earlier than the current update."""
        while self.off_samples and self.off_samples[0][0] < t - self.off_win_us:
            self.off_sorted.remove(self.off_samples.popleft()[1])
        n = len(self.off_sorted)
        if n == 0:
            return math.nan
        return self.off_sorted[n // 2] if n % 2 else (self.off_sorted[n // 2 - 1] + self.off_sorted[n // 2]) / 2

    def _sample_offset(self, t: int, mid: float) -> None:
        a, b = self.books[self.va], self.books[self.vb]
        if t - a.t > self.stale_us or t - b.t > self.stale_us:
            return  # a dead feed must not drag the reference
        x = ((a.bid + a.ask) / 2 - (b.bid + b.ask) / 2) / mid * 1e4
        self.off_samples.append((t, x))
        self.off_sorted.add(x)

    # ---- decision features (the six the prior was trained on) -----------------------
    def _features(self, t: int, edge: float) -> dict[str, float]:
        a, b = self.books[self.va], self.books[self.vb]
        rv = math.sqrt(sum(r for _, r in self.mid_hist)) * 1e4
        return {"edge_birth_bps": edge,
                "f_a_spread_bps": (a.ask - a.bid) / ((a.ask + a.bid) / 2) * 1e4,
                "f_b_spread_bps": (b.ask - b.bid) / ((b.ask + b.bid) / 2) * 1e4,
                "f_a_age_ms": (t - a.t_change) / 1000, "f_b_age_ms": (t - b.t_change) / 1000,
                "f_rv_1s_bps": rv}

    def _prior_ev(self, x: dict[str, float]) -> float:
        p = self.prior
        z = np.array([x[f] for f in p.get("features", FAST_FEATURES)])
        z = np.where(np.isnan(z), p["median"], z)
        q = 1 / (1 + math.exp(-float(((z - p["mu"]) / p["sd"]) @ p["w"] + p["b"])))
        if p.get("cal_x") is not None:  # isotonic calibration fitted on calibration days
            q = float(np.interp(q, p["cal_x"], p["cal_y"]))
        return q * (x["edge_birth_bps"] - self.trigger) + (1 - q) * self.loss_bps

    def _slow_ev(self, x: dict[str, float]) -> float:
        """The slow model's expected value (bps) on the fast features plus the incremental slow ones."""
        s = self.slow
        q = s["model"].predict_one(np.array([x[f] for f in s["features"]], dtype=np.float64))
        if s.get("cal_x") is not None:
            q = float(np.interp(q, s["cal_x"], s["cal_y"]))
        return q * (x["edge_birth_bps"] - self.trigger) + (1 - q) * s.get("loss_bps", self.loss_bps)

    # ---- order handling ---------------------------------------------------------------
    def _fill(self, o: Order) -> None:
        bk = self.books[o.venue]
        if math.isinf(o.limit):  # an unwind is a market order: it closes the whole position at the touch
            o.filled, o.price, o.done = o.qty, (bk.ask if o.side > 0 else bk.bid), True
            return
        if o.side > 0 and bk.ask <= o.limit:
            o.filled, o.price = min(o.qty, bk.asz), bk.ask
        elif o.side < 0 and bk.bid >= o.limit:
            o.filled, o.price = min(o.qty, bk.bsz), bk.bid
        o.done = True

    def _settle(self, tr: Trade, t: int) -> None:
        legs = tr.orders
        if not all(o.done for o in legs + tr.unwind):
            return
        if not tr.unwind:
            buy = next(o for o in legs if o.side > 0)
            sell = next(o for o in legs if o.side < 0)
            excess = buy.filled - sell.filled
            if abs(excess) > 1e-12:  # one-sided or uneven: close the excess where it was filled
                v = buy.venue if excess > 0 else sell.venue
                side = -1 if excess > 0 else +1
                tr.unwind.append(Order(v, side, math.inf if side > 0 else -math.inf, abs(excess), t + self.lat[v], -1))
                self.pending.append(tr.unwind[-1])
                return
        cash = 0.0
        for o in legs + tr.unwind:
            if o.filled > 0:
                cash += -o.side * o.filled * o.price - self.fee * o.filled * o.price
        tr.pnl, tr.settled = cash, True
        actual = sum(o.side * o.filled for o in legs + tr.unwind if o.venue == self.va and o.filled > 0)
        self.pos[tr.policy] = self.pos.get(tr.policy, 0.0) + actual - tr.dq_a_intended

    def on_quote(self, venue: str, t: int, bid: float, ask: float, bsz: float, asz: float) -> None:
        # 1. orders that reached their exchange before this update see the previous book
        due = [o for o in self.pending if o.arrive <= t]
        if due:
            self.pending = [o for o in self.pending if o.arrive > t]
            for o in sorted(due, key=lambda o: o.arrive):
                self._fill(o)
            for tr in list(self.unsettled):
                self._settle(tr, t)
            self.unsettled = [tr for tr in self.unsettled if not tr.settled]
        # 2. apply the update
        bk = self.books[venue]
        price_change = bid != bk.bid or ask != bk.ask
        if price_change:
            bk.t_change = t
        bk.bid, bk.ask, bk.bsz, bk.asz, bk.t = bid, ask, bsz, asz, t
        if self.sf is not None:
            self.sf.update(0 if venue == self.va else 1, t, bid, ask, bsz, asz)
        a, b = self.books[self.va], self.books[self.vb]
        if math.isnan(a.bid) or math.isnan(b.bid):
            return
        mid = (a.bid + a.ask + b.bid + b.ask) / 4
        if not math.isnan(self.last_mid):
            self.mid_hist.append((t, math.log(mid / self.last_mid) ** 2))
        self.last_mid = mid
        while self.mid_hist and self.mid_hist[0][0] <= t - 1_000_000:
            self.mid_hist.popleft()
        # 3. fast path: a gap opening in either direction (+1: sell a, buy b), measured against the
        #    usual offset when there is one (NaN before the first sample: nothing opens)
        ref = self.offset_ref(t) if self.off_win_us else 0.0
        for d, (sell, buy) in ((+1, (a, b)), (-1, (b, a))):
            edge = (sell.bid - buy.ask) / mid * 1e4
            rel = edge - d * ref
            is_open = rel > self.trigger
            if is_open and not self.open_dir[d]:
                self.triggers += 1
                x = self._features(t, rel)
                policies = ["naive"] + ["prior"] * (self.prior is not None) + ["slow"] * (self.slow is not None)
                for policy in policies:
                    t0 = time.perf_counter_ns()
                    xp = {**x, **self.sf.features()} if policy == "slow" else x  # the slow features at this update
                    action, reason, qty = self._decide(policy, t, d, mid, sell, buy, xp)
                    if policy == "slow":
                        self.slow_us.append((time.perf_counter_ns() - t0) / 1000)
                    self.decisions.append({"t": t, "direction": f"sell {self.va if d > 0 else self.vb} / buy "
                                           f"{self.vb if d > 0 else self.va}", "edge_bps": round(edge, 3),
                                           "edge_rel_bps": round(rel, 3), "policy": policy, "action": action,
                                           "reason": reason})
                    if action == "ENTER":
                        self._send(policy, t, d, edge, sell, buy, xp, qty)
            self.open_dir[d] = is_open
        # 4. only now add this update to the offset reference, so decisions never see their own sample
        if self.off_win_us and price_change:
            self._sample_offset(t, mid)

    def _decide(self, policy: str, t: int, d: int, mid: float, sell: Book, buy: Book, x: dict) -> tuple[str, str, float]:
        for v in (self.va, self.vb):
            age = t - self.books[v].t
            if age > self.stale_us:
                return "SKIP_STALE", f"{v} book last updated {age / 1e6:.1f} s ago", 0.0
        qty = min(self.notional / mid, sell.bsz, buy.asz)
        if qty * mid < self.min_notional:
            return "SKIP_THIN", f"only ${qty * mid:,.0f} shown on both books", 0.0
        if policy == "prior":
            ev = self._prior_ev(x)
            if ev <= 0:
                return "SKIP_EV", f"prior expected value {ev:+.2f} bps", 0.0
        if policy == "slow":
            ev = self._slow_ev(x)
            if ev <= 0:
                return "SKIP_EV", f"slow model expected value {ev:+.2f} bps", 0.0
        pos = self.pos.get(policy, 0.0)
        new = pos + (-qty if d > 0 else qty)  # d > 0 sells on venue a
        if abs(new) * mid > self.cap_usd and abs(new) >= abs(pos):
            return "SKIP_INVENTORY", f"position would reach ${abs(new) * mid:,.0f} (cap ${self.cap_usd:,.0f})", 0.0
        return "ENTER", f"gap {x['edge_birth_bps']:.2f} bps", qty

    def _send(self, policy: str, t: int, d: int, edge: float, sell: Book, buy: Book, x: dict | None = None,
              qty: float | None = None) -> None:
        sv, bv = (self.va, self.vb) if d > 0 else (self.vb, self.va)
        if qty is None:
            qty = min(self.notional / ((sell.bid + buy.ask) / 2), sell.bsz, buy.asz)
        tr = Trade(policy, t, edge, features=x or {})
        tr.dq_a_intended = -qty if d > 0 else qty
        self.pos[policy] = self.pos.get(policy, 0.0) + tr.dq_a_intended
        tr.orders = [Order(sv, -1, sell.bid, qty, t + self.lat[sv], len(self.trades)),
                     Order(bv, +1, buy.ask, qty, t + self.lat[bv], len(self.trades))]
        self.pending.extend(tr.orders)
        self.trades.append(tr)
        self.unsettled.append(tr)

    def summary(self) -> dict[str, dict]:
        out = {}
        for policy in sorted({tr.policy for tr in self.trades} | {d["policy"] for d in self.decisions} | {"naive"}):
            done = [tr for tr in self.trades if tr.policy == policy and tr.settled]
            full = [tr for tr in done if all(o.filled >= o.qty - 1e-12 for o in tr.orders)]
            acts: dict[str, int] = {}
            for dec in self.decisions:
                if dec["policy"] == policy:
                    acts[dec["action"]] = acts.get(dec["action"], 0) + 1
            out[policy] = {"trades": len(done), "full_fills": len(full),
                           "pnl_usd": round(sum(tr.pnl for tr in done), 2),
                           f"position_on_{self.va}": round(self.pos.get(policy, 0.0), 6), "decisions": acts}
            if policy == "slow" and self.slow_us:  # wall time of the slow features and model per trigger
                out[policy]["decision_us_median"] = round(float(np.median(self.slow_us)), 1)
        return out


def train_prior(cfg, out: Path, fee_bps: float = 1.0, lat_a_ms: float = 50.0, lat_b_ms: float = 8.0,
                pair: str = "btc_perp_binance_bybit", offset_window_s: float | None = 300.0) -> dict:
    """Fit the six-feature decay prior on development days of the archived cross-venue pair.

    Births are labelled as the live engine sees them: against the venues' usual offset when
    offset_window_s is set. Labels: did both legs fully fill, each after its own venue's latency
    (optimistic bound)? The prior is fitted on the first 70% of days with births and calibrated
    (isotonic) on the rest. The leg-risk term is net of the offset (pnl_rel_bps).
    """
    import pandas as pd
    from arbdata.splits import dates_for
    from .evaluate import load_day, replay_day
    from .policies import Calibrator, FastPrior, miss_loss_bps
    splits = json.loads(cfg.splits_path.read_text())
    have = {p.stem for p in (cfg.data_root / "episodes" / pair).glob("*.parquet")}
    days = []
    for d in sorted(set(dates_for(splits, "development")) & have):
        got = load_day(cfg, pair, d, 2 * fee_bps, offset_window_s)
        if got is None or not len(got[0]):
            continue
        eps, legs = got
        days.append((eps, replay_day(eps, legs, lat_a_ms, fee_bps, "optimistic", delay_b_ms=lat_b_ms)))
    cut = max(1, int(len(days) * 0.7))
    X = pd.concat([e for e, _ in days[:cut]], ignore_index=True)
    o = pd.concat([r for _, r in days[:cut]], ignore_index=True)
    fp = FastPrior().fit(X, o.full_fill.to_numpy())
    cal = None
    if days[cut:]:
        Xc = pd.concat([e for e, _ in days[cut:]], ignore_index=True)
        oc = pd.concat([r for _, r in days[cut:]], ignore_index=True)
        cal = Calibrator().fit(fp.predict(Xc), oc.full_fill.to_numpy()).to_arrays()
    prior = {"features": fp.features, "median": fp.median.tolist(), "mu": fp.mu.tolist(), "sd": fp.sd.tolist(),
             "w": fp.w.tolist(), "b": float(fp.b), "cal_x": cal[0] if cal else None, "cal_y": cal[1] if cal else None,
             "loss_bps": miss_loss_bps(o, "pnl_rel_bps"), "offset_window_s": offset_window_s,
             "asset": pair.split("_")[0].upper(),
             "trained_on": f"{pair}, {len(X):,} triggers on {cut} days, calibrated on {len(days) - cut} days",
             "latency_ms": {"a": lat_a_ms, "b": lat_b_ms}, "fee_bps": fee_bps,
             "full_fill_rate": float(o.full_fill.mean())}
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(prior, indent=1))
    return prior


def load_prior(path: Path) -> dict:
    p = json.loads(path.read_text())
    return {k: np.asarray(v) if isinstance(v, list) and k != "features" else v for k, v in p.items()}


def prior_matches(prior: dict, offset_window_s: float | None) -> bool:
    """A prior is only valid for the gaps it was trained on: raw gaps, or gaps against the same offset window."""
    return (prior.get("offset_window_s") or None) == (offset_window_s or None)


def prior_is_for(prior: dict, asset: str) -> bool:
    """Whether a saved prior was trained on this asset (its "asset" field, or its trained_on text for older files)."""
    if prior.get("asset"):
        return str(prior["asset"]).upper() == asset.upper()
    text = str(prior.get("trained_on", ""))
    return text.lower().startswith(f"{asset.lower()}_") or f" {asset.upper()} " in f" {text} "


def prior_file(asset: str, offset_window_s: float | None) -> str:
    """Where --train-prior saves a prior, so find_prior can tell priors apart by name too."""
    return f"prior_{asset.upper()}_" + (f"offset{offset_window_s:g}s" if offset_window_s else "raw") + ".json"


def find_prior(folder: Path, asset: str, offset_window_s: float | None) -> tuple[Path | None, str]:
    """The saved prior in folder for this asset, trained on the same gaps as this run, and a note saying
    which one was picked, or why none was. Newest file first when several fit."""
    gaps = lambda w: f"gaps against a {w:g} s offset" if w else "raw gaps"
    files = sorted(folder.glob("prior*.json"), key=lambda p: p.stat().st_mtime, reverse=True) if folder.is_dir() else []
    mine = [(p, load_prior(p)) for p in files]
    mine = [(p, pr) for p, pr in mine if prior_is_for(pr, asset)]
    for p, pr in mine:
        if prior_matches(pr, offset_window_s):
            return p, f"Prior {p.name}: {pr.get('trained_on', '')}."
    train = (f"python -m arbtrade.live --train-prior --asset {asset}"
             + (f" --offset-window-s {offset_window_s:g}" if offset_window_s else " --offset-window-s 0"))
    if mine:
        other = sorted({gaps(pr.get("offset_window_s")) for _, pr in mine})
        return None, (f"The saved {asset} priors were trained on {', '.join(other)}, not {gaps(offset_window_s)}, "
                      f"so only the naive policy runs. Train a matching one with: {train}")
    return None, f"No saved {asset} prior: only the naive policy runs. Train one with: {train}"


# ---- inputs ---------------------------------------------------------------------------

def replay_events(cfg, date: str | list[str], asset: str = "BTC"):
    """(t, venue, bid, ask, bsz, asz) from our recordings, in receive-time order, over one or more dates.
    Only the stretch where both venues were recording is replayed."""
    import pandas as pd
    from arbdata.normalize import normalize_binance_live, normalize_bybit_live
    pair = f"{asset}-USDT"
    parts = []
    for d in ([date] if isinstance(date, str) else date):
        a, _ = normalize_binance_live(cfg.raw_path(cfg.streams[f"binance_live/binance/{pair}/perp"], d, ""))
        b, _ = normalize_bybit_live(cfg.raw_path(cfg.streams[f"bybit_live/bybit/{pair}/perp"], d, ""))
        if a.empty or b.empty:
            continue
        lo = max(a.avail_ts.min(), b.avail_ts.min())
        parts += [a[a.avail_ts >= lo].assign(venue="binance"), b[b.avail_ts >= lo].assign(venue="bybit")]
    ev = pd.concat(parts).sort_values("avail_ts", kind="stable")
    return ev[["avail_ts", "venue", "bid_px", "ask_px", "bid_sz", "ask_sz"]].itertuples(index=False, name=None)


async def live_events(minutes: float, asset: str = "BTC"):
    import ssl

    import certifi
    import orjson
    import websockets
    tls = ssl.create_default_context(cafile=certifi.where())
    q: asyncio.Queue = asyncio.Queue()
    stop = time.time() + minutes * 60
    sym = f"{asset}USDT"

    async def binance():
        async with websockets.connect(f"wss://fstream.binance.com/ws/{sym.lower()}@bookTicker", ssl=tls) as ws:
            while time.time() < stop:
                d = orjson.loads(await ws.recv())
                await q.put((time.time_ns() // 1000, "binance", float(d["b"]), float(d["a"]), float(d["B"]), float(d["A"])))

    async def bybit():
        async with websockets.connect("wss://stream.bybit.com/v5/public/linear", ssl=tls, ping_interval=None) as ws:
            await ws.send(json.dumps({"op": "subscribe", "args": [f"orderbook.1.{sym}"]}))
            last_ping = time.time()
            while time.time() < stop:
                if time.time() - last_ping > 20:
                    await ws.send(json.dumps({"op": "ping"}))
                    last_ping = time.time()
                m = orjson.loads(await ws.recv())
                if m.get("topic", "").startswith("orderbook") and m["data"]["b"] and m["data"]["a"]:
                    (bp, bs), (ap, az) = m["data"]["b"][0], m["data"]["a"][0]
                    await q.put((time.time_ns() // 1000, "bybit", float(bp), float(ap), float(bs), float(az)))

    async def forever(name, feed):
        """Reconnect after a dropped connection. While a feed is down its book goes stale, and the
        engine's stale check skips triggers until it is back."""
        while time.time() < stop:
            try:
                await feed()
            except Exception as e:  # noqa: BLE001 - any network error: log it and reconnect
                print(f"{time.strftime('%H:%M:%S')} {name} disconnected ({type(e).__name__}: {e}); reconnecting", flush=True)
                await asyncio.sleep(1)

    tasks = [asyncio.create_task(forever("binance", binance)), asyncio.create_task(forever("bybit", bybit))]
    while time.time() < stop:
        try:
            yield await asyncio.wait_for(q.get(), 1)
        except asyncio.TimeoutError:
            continue
    for t in tasks:
        t.cancel()


def main() -> None:
    from arbdata.config import load_config
    ap = argparse.ArgumentParser()
    ap.add_argument("--minutes", type=float, default=10)
    ap.add_argument("--replay", default=None, help="a recorded date instead of live feeds")
    ap.add_argument("--asset", default="BTC")
    ap.add_argument("--fee", type=float, default=1.0, help="taker fee in bps per leg")
    ap.add_argument("--trigger", type=float, default=None,
                    help="gap (bps) that fires the fast path; default covers both legs' fees")
    ap.add_argument("--lat-binance", type=float, default=None,
                    help="one-way order latency to Binance (ms); default from config/sources.yaml")
    ap.add_argument("--lat-bybit", type=float, default=None,
                    help="one-way order latency to Bybit (ms); default from config/sources.yaml")
    ap.add_argument("--offset-window-s", type=float, default=300.0,
                    help="measure gaps against the venues' trailing offset over this window; 0 = against zero")
    ap.add_argument("--prior", default=None,
                    help="a saved prior; default: the newest one in data/reports/live for this asset and gap definition")
    ap.add_argument("--stale-ms", type=float, default=5_000.0, help="skip triggers when a book is older than this")
    ap.add_argument("--cap-usd", type=float, default=50_000.0, help="cap on each policy's net position")
    ap.add_argument("--decisions", default=None, help="write every decision and its reason to this JSONL file")
    ap.add_argument("--train-prior", action="store_true", help="fit the prior on development days and save it")
    args = ap.parse_args()
    cfg = load_config()
    lat_bn = args.lat_binance if args.lat_binance is not None else cfg.latency_ms.get("binance", 50.0)
    lat_by = args.lat_bybit if args.lat_bybit is not None else cfg.latency_ms.get("bybit", 8.0)
    window = args.offset_window_s or None
    live_dir = cfg.reports_dir / "live"
    if args.train_prior:
        # <asset>_perp_binance_bybit: leg a is Binance, leg b is Bybit
        out = Path(args.prior) if args.prior else live_dir / prior_file(args.asset, window)
        p = train_prior(cfg, out, args.fee, lat_bn, lat_by, pair=f"{args.asset.lower()}_perp_binance_bybit",
                        offset_window_s=window)
        print(f"saved {out}: {p['trained_on']}, full-fill rate {p['full_fill_rate']:.1%}, loss if missed {p['loss_bps']:.2f} bps")
        return
    if args.prior:
        prior_path = Path(args.prior)
        prior = load_prior(prior_path) if prior_path.exists() else None
        if prior is not None and not prior_matches(prior, window):
            gaps = lambda w: f"gaps against a {w:g} s offset" if w else "raw gaps"
            print(f"{prior_path} was trained on {gaps(prior.get('offset_window_s'))}, but this run measures {gaps(window)}. "
                  "Running the naive policy only; retrain with --train-prior.", flush=True)
            prior = None
    else:
        prior_path, note = find_prior(live_dir, args.asset, window)
        prior = load_prior(prior_path) if prior_path else None
        print(note, flush=True)
    trigger = args.trigger if args.trigger is not None else 2 * args.fee
    eng = PaperEngine(("binance", "bybit"), trigger, args.fee,
                      {"binance": lat_bn, "bybit": lat_by},
                      prior=prior, loss_bps=prior.get("loss_bps", -1.0) if prior else -1.0,
                      stale_ms=args.stale_ms, cap_usd=args.cap_usd, offset_window_s=window)
    if args.replay:
        for t, v, bid, ask, bsz, asz in replay_events(cfg, args.replay, args.asset):
            eng.on_quote(v, int(t), bid, ask, bsz, asz)
    else:
        async def run():
            last = time.time()
            async for t, v, bid, ask, bsz, asz in live_events(args.minutes, args.asset):
                eng.on_quote(v, t, bid, ask, bsz, asz)
                if time.time() - last > 30:
                    print(time.strftime("%H:%M:%S"), f"triggers {eng.triggers}", eng.summary(), flush=True)
                    last = time.time()
        asyncio.run(run())
    print(json.dumps({"triggers": eng.triggers, **eng.summary()}, indent=1))
    if args.decisions:
        with open(args.decisions, "w") as f:
            for dec in eng.decisions:
                f.write(json.dumps(dec) + "\n")


if __name__ == "__main__":
    main()
