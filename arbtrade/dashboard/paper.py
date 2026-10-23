"""Run the paper trader (arbtrade/live.py PaperEngine) in the background, for the dashboard.

Two sources: live Binance and Bybit feeds, or one of our recorded days replayed at a chosen
speed. The engine is the same one `python -m arbtrade.live` runs; this module only feeds it in
a thread and takes snapshots for the page. Every engine access holds one lock.
"""

from __future__ import annotations

import asyncio
import math
import threading
import time
from collections import deque
from pathlib import Path

from arbtrade.live import PaperEngine, live_events, load_prior, prior_matches, replay_events

HISTORY_STEP_US = 500_000   # one point of gap history per half second of market time
HISTORY_LEN = 1_200          # ten minutes at that step


class PaperSession:
    def __init__(self, cfg, prior_path: Path):
        self.cfg, self.prior_path = cfg, prior_path
        self.lock = threading.Lock()
        self.stop_flag = threading.Event()
        self.thread: threading.Thread | None = None
        self.engine: PaperEngine | None = None
        self.state: dict = {"status": "idle"}
        self.history: deque = deque(maxlen=HISTORY_LEN)
        self.last_hist_t = 0

    # ---- control ------------------------------------------------------------------------
    def start(self, opts: dict) -> dict:
        with self.lock:
            if self.thread is not None and self.thread.is_alive():
                raise RuntimeError("a session is already running; stop it first")
            source = opts.get("source", "live")
            fee = float(opts.get("fee", 1.0))
            window = float(opts.get("offset_window_s", 300.0)) or None
            lat = {"binance": float(opts.get("lat_binance") or self.cfg.latency_ms.get("binance", 50.0)),
                   "bybit": float(opts.get("lat_bybit") or self.cfg.latency_ms.get("bybit", 8.0))}
            prior, note = None, "No prior file: running the naive policy only."
            if self.prior_path.exists():
                p = load_prior(self.prior_path)
                if prior_matches(p, window):
                    prior, note = p, f"Prior: {p.get('trained_on', self.prior_path.name)}."
                else:
                    note = ("The saved prior was trained on raw gaps, not gaps against the usual offset, so only the "
                            "naive policy runs. Retrain it with: python -m arbtrade.live --train-prior")
            self.engine = PaperEngine(("binance", "bybit"), 2 * fee, fee, lat, prior=prior,
                                      loss_bps=prior.get("loss_bps", -1.0) if prior else -1.0,
                                      cap_usd=float(opts.get("cap_usd", 50_000.0)), offset_window_s=window)
            self.history.clear()
            self.last_hist_t = 0
            self.stop_flag.clear()
            self.state = {"status": "starting", "source": source, "asset": opts.get("asset", "BTC"),
                          "date": opts.get("date"), "speed": opts.get("speed", "max"), "minutes": float(opts.get("minutes", 10)),
                          "fee": fee, "latency_ms": lat, "offset_window_s": window, "note": note, "error": None,
                          "events": 0, "started": time.time(), "market_t0": None, "market_t": None}
            self.thread = threading.Thread(target=self._run, daemon=True)
            self.thread.start()
            return dict(self.state)

    def stop(self) -> None:
        self.stop_flag.set()

    # ---- feeding the engine -----------------------------------------------------------------
    def _on_quote(self, v, t, bid, ask, bsz, asz) -> None:
        with self.lock:
            e = self.engine
            e.on_quote(v, int(t), bid, ask, bsz, asz)
            st = self.state
            st["events"] += 1
            st["market_t0"] = st["market_t0"] or int(t)
            st["market_t"] = int(t)
            if t - self.last_hist_t >= HISTORY_STEP_US:
                self.last_hist_t = int(t)
                g = self._gaps(int(t))
                if g:
                    self.history.append(g)

    def _gaps(self, t: int) -> dict | None:
        e = self.engine
        a, b = e.books[e.va], e.books[e.vb]
        if any(math.isnan(x) for x in (a.bid, a.ask, b.bid, b.ask)):
            return None
        mid = (a.bid + a.ask + b.bid + b.ask) / 4
        ref = e.offset_ref(t) if e.off_win_us else 0.0
        sell_a = (a.bid - b.ask) / mid * 1e4
        sell_b = (b.bid - a.ask) / mid * 1e4
        nan = lambda x: None if x is None or math.isnan(x) else round(x, 3)
        return {"t": t // 1000, "sell_a": nan(sell_a - ref), "sell_b": nan(sell_b + ref),
                "raw_a": nan(sell_a), "raw_b": nan(sell_b), "offset": nan(ref)}

    def _run(self) -> None:
        try:
            with self.lock:
                self.state["status"] = "running"
            if self.state["source"] == "replay":
                self._replay()
            else:
                asyncio.run(self._live())
            with self.lock:
                self.state["status"] = "stopped" if self.stop_flag.is_set() else "finished"
        except Exception as ex:  # noqa: BLE001 - shown on the page as it is
            with self.lock:
                self.state["status"] = "error"
                self.state["error"] = f"{type(ex).__name__}: {ex}"

    def _replay(self) -> None:
        speed = self.state["speed"]
        rate = None if speed == "max" else float(speed)
        wall0, t0 = time.time(), None
        for t, v, bid, ask, bsz, asz in replay_events(self.cfg, self.state["date"], self.state["asset"]):
            if self.stop_flag.is_set():
                return
            t0 = t0 or t
            if rate:  # hold back until wall time catches up with market time / speed
                ahead = (t - t0) / 1e6 / rate - (time.time() - wall0)
                if ahead > 0:
                    time.sleep(min(ahead, 0.5))
            self._on_quote(v, t, bid, ask, bsz, asz)

    async def _live(self) -> None:
        async for t, v, bid, ask, bsz, asz in live_events(self.state["minutes"], self.state["asset"]):
            if self.stop_flag.is_set():
                return
            self._on_quote(v, t, bid, ask, bsz, asz)

    # ---- what the page sees -------------------------------------------------------------------
    def snapshot(self, n_decisions: int = 150) -> dict:
        with self.lock:
            st = dict(self.state)
            e = self.engine
            if e is None:
                return st
            now = st.get("market_t") or 0
            books = {}
            for v in (e.va, e.vb):
                bk = e.books[v]
                books[v] = {"bid": None if math.isnan(bk.bid) else bk.bid, "ask": None if math.isnan(bk.ask) else bk.ask,
                            "bid_sz": bk.bsz, "ask_sz": bk.asz, "age_ms": (now - bk.t) / 1000 if bk.t else None}
            st.update({
                "books": books, "gaps": self._gaps(now) if now else None, "trigger_bps": e.trigger,
                "triggers": e.triggers, "summary": e.summary(), "history": list(self.history),
                "decisions": [dict(d) for d in e.decisions[-n_decisions:]][::-1],
                "offset_samples": len(e.off_samples), "elapsed_s": time.time() - st["started"],
                "widest": {k: max((h[k] for h in self.history if h[k] is not None), default=None) for k in ("sell_a", "sell_b")},
                "market_elapsed_s": (now - st["market_t0"]) / 1e6 if st.get("market_t0") else 0.0,
            })
            return st
