"""The dashboard on synthetic report files: the numbers it serves, its HTTP API, and the paper session."""

import json
import threading
import time
import urllib.request
from http.server import ThreadingHTTPServer

import numpy as np
import pandas as pd
import pytest

from arbtrade.dashboard import data as D
from arbtrade.dashboard import paper as Pmod
from arbtrade.dashboard.server import App, make_handler
from arbtrade.stats import boot_ci

DAYS = [f"2024-01-{d:02d}" for d in range(1, 11)]
QUIET = "2024-01-05"  # a validation day without a single trade


def _write_run(reports, pair, tag, seed, offset=0.0):
    rng = np.random.default_rng(seed)
    run = reports / "pnl" / f"{pair}{tag}"
    run.mkdir(parents=True)
    rows = []
    for d in DAYS:
        if d == QUIET:
            continue
        for strat in D.STRATEGIES:
            for cap in ("no cap", "$50k cap"):
                for mode in ("optimistic", "conservative"):
                    rows.append({"date": d, "fee": 2.35, "mode": mode, "tau_ms": 50.0, "strategy": strat, "cap": cap,
                                 "trades": 4, "one_way_share": 0.5, "old": 1.0, "funding": -0.1, "flatten": -0.4,
                                 "close_unfilled": 0.0, "realised": float(rng.normal(offset, 5)), "kept": 4})
    pd.DataFrame(rows).to_csv(run / "inventory_by_day.csv", index=False)
    (run / "meta.json").write_text(json.dumps({"pair": pair, "offset_aware": True, "offset_window_s": 300.0,
                                               "latencies_ms": {"50.0": [50.0, 8.0]},
                                               "folds": [{"train": ["2023-12-01", "2023-12-31"], "val": DAYS[:5]},
                                                         {"train": ["2023-12-01", "2024-01-05"], "val": DAYS[5:]}],
                                               "val_days": {"2.35": {"0": DAYS[:5], "1": DAYS[5:]}}}))
    (run / "inventory.md").write_text("# x\n\nno new trades in the day's last 60 s while the position is worked down\n")
    pd.DataFrame({"fee_bps_per_leg": [2.35], "fee_a_bps": [1.7], "fee_b_bps": [3.0]}).to_csv(run / "pnl_vs_latency_folds.csv", index=False)
    return pd.DataFrame(rows)


@pytest.fixture
def reports(tmp_path):
    r = tmp_path / "data" / "reports"
    r.mkdir(parents=True)
    _write_run(r, "btc_perp_binance_bybit", "_v9", 0, offset=5.0)
    _write_run(r, "eth_perp_binance_bybit", "_v9", 1, offset=-1.0)
    (r / "decay").mkdir()
    pd.DataFrame({"pair": ["p", "p"], "births": ["clean", "clean"], "hurdle": ["h", "h"], "tau_ms": [500, 1000],
                  "model": ["m", "m"], "auc": [0.8, 0.7]}).to_csv(r / "decay" / "summary_v2.csv", index=False)
    pd.DataFrame({"hurdle": ["h", "h"], "t_ms": [100.0, 200.0], "surely_alive": [0.5, 0.3],
                  "possibly_alive": [1.0, 0.4], "n": [10, 10]}).to_csv(r / "decay" / "fig_survival.csv", index=False)
    return r


def test_runs_are_listed_with_their_setup(reports):
    runs = D.list_runs(reports)
    assert [r["coin"] for r in runs] == ["BTC", "ETH"]
    assert runs[0]["tag"] == "_v9" and runs[0]["fees"] == [2.35] and runs[0]["taus"] == [50.0]
    assert runs[0]["days"] == len(DAYS) - 1


def test_summary_matches_a_direct_computation_and_counts_quiet_days(reports):
    df = pd.read_csv(reports / "pnl" / "btc_perp_binance_bybit_v9" / "inventory_by_day.csv")
    s = D.run_summary(reports, "btc_perp_binance_bybit_v9", 2.35, 50.0, "optimistic", "capped")
    assert s["days"] == DAYS and s["fold_starts"] == [DAYS[5]]
    casc = next(x for x in s["strategies"] if x["key"] == "latency-aware cascade")
    want = (df[(df.strategy == "latency-aware cascade") & (df["mode"] == "optimistic") & (df.cap == "$50k cap")]
            .set_index("date").realised.reindex(DAYS, fill_value=0.0).to_numpy())
    assert np.isclose(casc["mean"], want.mean())                     # the quiet day counts as $0
    assert (casc["lo"], casc["hi"]) == pytest.approx(boot_ci(want))
    assert casc["daily"][DAYS.index(QUIET)] == 0.0
    assert np.isclose(casc["cum"][-1], want.sum())
    assert np.isclose(casc["parts"]["trades"] + casc["parts"]["funding"] + casc["parts"]["close"], casc["mean"])
    assert s["setup"]["venue_fees_bps"] == [1.7, 3.0] and "60 s" in s["setup"]["close"]
    assert {(p["a"], p["b"]) for p in s["pairs"]} >= {("Cascade", "Naive"), ("Cascade", "Gap size only")}


def test_coins_rank_pairs_and_unknown_runs_are_refused(reports):
    c = D.coins(reports, "_v9", "optimistic", "capped")
    assert [r["coin"] for r in c["rows"]] == ["BTC", "ETH"]           # sorted by cascade P&L
    assert len(c["rows"][0]["cum"]["Cascade"]) == len(DAYS)
    with pytest.raises(KeyError):
        D.load_run(reports, "../../etc")


def test_decay_and_notes(reports):
    d = D.decay(reports)
    assert len(d["rows"]) == 2 and d["survival"]["curves"]["h"]["lo"] == [0.5, 0.3]
    notes = [n["path"] for n in D.notes(reports)]
    assert "pnl/btc_perp_binance_bybit_v9/inventory.md" in notes
    assert "day's last 60 s" in D.read_note(reports, notes[0])
    for bad in ("../README.md", "pnl/btc_perp_binance_bybit_v9/meta.json"):
        with pytest.raises(KeyError):
            D.read_note(reports, bad)


def test_http_api_and_static_files(reports):
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), make_handler(App(reports, None)))
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{httpd.server_address[1]}"
    get = lambda p: urllib.request.urlopen(base + p, timeout=10)
    try:
        assert len(json.load(get("/api/runs"))) == 2
        s = json.load(get("/api/run?name=btc_perp_binance_bybit_v9&fee=2.35&tau=50&mode=optimistic&cap=capped"))
        assert len(s["strategies"]) == 5
        page = get("/")
        assert page.headers["Content-Type"].startswith("text/html") and b"arbpercept" in page.read()
        assert get("/static/app.js").headers["Content-Type"].startswith("text/javascript")
        assert json.load(get("/api/paper"))["status"] == "unavailable"
        for bad in ("/api/run?name=nope&fee=2.35&tau=50", "/static/../server.py", "/api/nothing"):
            with pytest.raises(urllib.error.HTTPError) as e:
                get(bad)
            assert e.value.code == 404
    finally:
        httpd.shutdown()


def test_paper_session_replays_and_reports(monkeypatch, tmp_path):
    t0 = 1_700_000_000_000_000
    events = []
    for k in range(400):  # Binance sits ~1 bp above Bybit; a 3 bps jump on Binance at 300 s
        t = t0 + k * 1_000_000
        jump = 0.03 if k == 300 else 0.0
        wiggle = 0.0001 * (k % 2)  # prices move a little every second, so the offset is sampled all along
        events.append((t, "binance", 100.005 + jump + wiggle, 100.015 + jump + wiggle, 5.0, 5.0))
        events.append((t + 500_000, "bybit", 99.995 + wiggle, 100.005 + wiggle, 5.0, 5.0))
    monkeypatch.setattr(Pmod, "replay_events", lambda cfg, date, asset: iter(events))
    cfg = type("Cfg", (), {"latency_ms": {"binance": 50.0, "bybit": 8.0}})()
    s = Pmod.PaperSession(cfg, tmp_path / "no_prior.json")
    s.start({"source": "replay", "date": "2024-01-01", "speed": "max", "fee": 0.5, "offset_window_s": 300})
    for _ in range(100):
        if s.snapshot()["status"] in ("finished", "error"):
            break
        time.sleep(0.05)
    snap = s.snapshot()
    assert snap["status"] == "finished", snap.get("error")
    assert snap["events"] == len(events) and "naive policy only" in snap["note"]
    assert snap["triggers"] == 1                                       # only the jump beyond the usual offset
    assert snap["decisions"][0]["action"] == "ENTER" and snap["summary"]["naive"]["trades"] == 1
    assert snap["books"]["binance"]["bid"] == pytest.approx(100.005)
    assert len(snap["history"]) > 100 and snap["widest"]["sell_a"] > 1.5
    with pytest.raises(RuntimeError):
        s.thread = threading.Thread(target=time.sleep, args=(0.5,))
        s.thread.start()
        s.start({"source": "replay"})                                  # one session at a time
