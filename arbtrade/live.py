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
when the decay prior's expected value is positive.

Every trigger gets a recorded decision per policy, with its reason, checked in this order:
  SKIP_STALE      a venue's book has not updated for stale_ms (a dead feed, not a quiet book:
                  Bybit stays silent for up to ~3 s when nothing changes)
  SKIP_THIN       the size both books show is worth less than min_notional
  SKIP_EV         the prior's expected value is not positive (prior policy only)
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

from .policies import FAST_FEATURES


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
    def __init__(self, venues: tuple[str, str], trigger_bps: float, fee_bps: float, latency_ms: dict[str, float],
                 notional: float = 10_000.0, prior: dict | None = None, loss_bps: float = -1.0,
                 stale_ms: float = 5_000.0, cap_usd: float = math.inf, min_notional: float = 100.0):
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
        z = np.array([x[f] for f in FAST_FEATURES])
        z = np.where(np.isnan(z), p["median"], z)
        q = 1 / (1 + math.exp(-float(((z - p["mu"]) / p["sd"]) @ p["w"] + p["b"])))
        return q * (x["edge_birth_bps"] - self.trigger) + (1 - q) * self.loss_bps

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
        if bid != bk.bid or ask != bk.ask:
            bk.t_change = t
        bk.bid, bk.ask, bk.bsz, bk.asz, bk.t = bid, ask, bsz, asz, t
        a, b = self.books[self.va], self.books[self.vb]
        if math.isnan(a.bid) or math.isnan(b.bid):
            return
        mid = (a.bid + a.ask + b.bid + b.ask) / 4
        if not math.isnan(self.last_mid):
            self.mid_hist.append((t, math.log(mid / self.last_mid) ** 2))
        self.last_mid = mid
        while self.mid_hist and self.mid_hist[0][0] <= t - 1_000_000:
            self.mid_hist.popleft()
        # 3. fast path: a gap opening in either direction (+1: sell a, buy b)
        for d, (sell, buy) in ((+1, (a, b)), (-1, (b, a))):
            edge = (sell.bid - buy.ask) / mid * 1e4
            is_open = edge > self.trigger
            if is_open and not self.open_dir[d]:
                self.triggers += 1
                x = self._features(t, edge)
                for policy in ("naive", "prior") if self.prior is not None else ("naive",):
                    action, reason, qty = self._decide(policy, t, d, mid, sell, buy, x)
                    self.decisions.append({"t": t, "direction": f"sell {self.va if d > 0 else self.vb} / buy "
                                           f"{self.vb if d > 0 else self.va}", "edge_bps": round(edge, 3),
                                           "policy": policy, "action": action, "reason": reason})
                    if action == "ENTER":
                        self._send(policy, t, d, edge, sell, buy, x, qty)
            self.open_dir[d] = is_open

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
        return out


def train_prior(cfg, out: Path, fee_bps: float = 1.0, latency_ms: float = 56.0, pair: str = "btc_perp_binance_bybit") -> dict:
    """Fit the six-feature decay prior on development days of the archived cross-venue pair.

    Labels: did both legs fully fill after latency_ms (optimistic bound)? The slower venue's
    latency is used because both legs must arrive for the trade to be complete.
    """
    import pandas as pd
    from arbdata.splits import dates_for
    from .evaluate import load_day, replay_day
    from .policies import FastPrior, miss_loss_bps
    splits = json.loads(cfg.splits_path.read_text())
    have = {p.stem for p in (cfg.data_root / "episodes" / pair).glob("*.parquet")}
    X, outs = [], []
    for d in sorted(set(dates_for(splits, "development")) & have):
        got = load_day(cfg, pair, d, 2 * fee_bps)
        if got is None:
            continue
        eps, legs = got
        X.append(eps)
        outs.append(replay_day(eps, legs, latency_ms, fee_bps, "optimistic"))
    X, o = pd.concat(X, ignore_index=True), pd.concat(outs, ignore_index=True)
    fp = FastPrior().fit(X, o.full_fill.to_numpy())
    prior = {"median": fp.median.tolist(), "mu": fp.mu.tolist(), "sd": fp.sd.tolist(), "w": fp.w.tolist(),
             "b": float(fp.b), "loss_bps": miss_loss_bps(o), "trained_on": f"{pair}, {len(X):,} triggers",
             "latency_ms": latency_ms, "fee_bps": fee_bps, "full_fill_rate": float(o.full_fill.mean())}
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(prior, indent=1))
    return prior


def load_prior(path: Path) -> dict:
    p = json.loads(path.read_text())
    return {k: np.asarray(v) if isinstance(v, list) else v for k, v in p.items()}


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

    tasks = [asyncio.create_task(binance()), asyncio.create_task(bybit())]
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
    ap.add_argument("--lat-binance", type=float, default=56.0, help="one-way order latency to Binance (ms)")
    ap.add_argument("--lat-bybit", type=float, default=7.0, help="one-way order latency to Bybit (ms)")
    ap.add_argument("--prior", default="data/reports/live/prior.json")
    ap.add_argument("--stale-ms", type=float, default=5_000.0, help="skip triggers when a book is older than this")
    ap.add_argument("--cap-usd", type=float, default=50_000.0, help="cap on each policy's net position")
    ap.add_argument("--decisions", default=None, help="write every decision and its reason to this JSONL file")
    ap.add_argument("--train-prior", action="store_true", help="fit the prior on development days and save it")
    args = ap.parse_args()
    cfg = load_config()
    if args.train_prior:
        p = train_prior(cfg, Path(args.prior), args.fee, max(args.lat_binance, args.lat_bybit))
        print(f"saved {args.prior}: {p['trained_on']}, full-fill rate {p['full_fill_rate']:.1%}, loss if missed {p['loss_bps']:.2f} bps")
        return
    prior_path = Path(args.prior)
    prior = load_prior(prior_path) if prior_path.exists() else None
    trigger = args.trigger if args.trigger is not None else 2 * args.fee
    eng = PaperEngine(("binance", "bybit"), trigger, args.fee,
                      {"binance": args.lat_binance, "bybit": args.lat_bybit},
                      prior=prior, loss_bps=prior.get("loss_bps", -1.0) if prior else -1.0,
                      stale_ms=args.stale_ms, cap_usd=args.cap_usd)
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
