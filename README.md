# Latency-aware cross-asset arbitrage (Perceptron 2026, Problem 6)

An arbitrage opportunity is worth acting on only if it will still be there when the order arrives. This project measures how fast crypto mispricings close, predicts whether each one will survive a given latency, and uses that prediction to decide how much thinking each opportunity can afford: act on a fast check, wait for a slower and better model, or skip.

## What's in the repository

| Part | Path | What it does |
|---|---|---|
| Data pipeline | `arbdata/` | Downloads free archives (Bybit, Binance, Tardis) and perpetual funding rates (`funding.py`), and records Bybit and Binance live. Rebuilds order books, validates them against independent trade records, and labels every opportunity with its lifetime and causal features. Leakage-safe, frozen date splits. See [DATA_CARD.md](DATA_CARD.md). |
| Slow-path statistics | `arbdata/kalman.py` | A Kalman filter on the pair's log-spread (and a two-state hedge-ratio version), plus an OU mean-reversion half-life. Numba-compiled and causal. |
| Trading system | `arbtrade/` | Replay execution with injected latency, IOC legs, fees and leg risk (`replay.py`). Fast prior, slow model, isotonic calibration and cascade policies (`policies.py`), with the slow model compiled to a Numba tree walker (`compiled.py`). Walk-forward P&L-vs-latency evaluation (`evaluate.py`). Maker-taker execution (`makertaker.py`), a live paper trader (`live.py`), and inventory accounting: positions per venue, funding, end-of-day closing and a position cap (`inventory.py`). |
| Analysis | `analysis/` | Decay models and figures (`decay_pilot.py`, `decay_figures.py`), the P&L chart and intervals (`pnl_figure.py`, `pnl_stats.py`), the 100 ms vs 10 ms resolution check (`resolution_check.py`), models retrained on our 10 ms recordings (`live_prior.py`, `live_decay.py`), and the maker-taker sweeps (`maker_taker.py`, `maker_taker_live.py`). |
| Live recorder | `arbdata/recorder.py`, `deploy/` | Records Bybit's 10 ms book and trades, and Binance USD-M top-of-book, on one receive clock. A systemd unit is provided for an always-on VM. |
| Tests | `tests/` | Run with `.venv/bin/python -m pytest`. They cover book rebuild, outage detection, censoring, splits, trade validation with planted faults, Kalman/OU against known answers, replay mechanics, and a lookahead test that cuts the raw feeds at each decision and checks nothing changes. They use synthetic data only, so they run without the data folders. GitHub Actions runs them on every pull request (`.github/workflows/tests.yml`). |

## How the decision works

1. **Fast path (microseconds):** the fee-adjusted gap between venues crosses a threshold. For cross-venue pairs the gap is measured against the venues' usual offset (`--offset-aware`), since a steady offset is not arbitrage.
2. **Decay prior (1.5 µs, measured):** a six-feature logistic model estimates q, the chance both legs still fill after the order latency. The expected value in bps is `q·(edge − fees) + (1 − q)·L`, where L is the measured average outcome of incomplete fills (leg risk).
3. **Cascade:**
   - If the prior is confidently positive, act now.
   - If it's confidently negative, skip.
   - Otherwise wait for the slow model: gradient boosting on every feature, including the Kalman and OU statistics and order flow. Compiled to a Numba tree walker, it takes 6.4 µs (it took 3–28 ms in Python). Re-read the book, and trade only if the gap is still there.

   Both models' probabilities pass through an isotonic calibration fitted on calibration days. The two confidence margins are also chosen on calibration days, never on the days being scored.

Before any order goes out, each trigger passes four checks, and every decision is logged with its reason (`python -m arbtrade.live --decisions out.jsonl`):
- **Stale:** both books must have updated within the last 5 s, so a dead feed can't look like a gap.
- **Thin:** at least $100 shown on both books.
- **Expected value:** the decay prior's expected value must be positive.
- **Inventory:** the trade must not push the net position past the cap ($50k by default). Trades that shrink the position always pass.

With the slow model at microseconds, model compute no longer costs edge; network latency does (about 8 ms to Bybit and 50 ms to Binance from our machine, stored once as `order_latency_ms` in `config/sources.yaml`). The 6.4 µs is model inference only. The slow model's features are computed offline, so their live cost is not yet measured. The cascade's job is now the decay-aware decision itself, and it keeps room for heavier models later.

## Running it

```bash
python3 -m venv .venv && .venv/bin/pip install -e ".[dev,models,live]"
```

For the exact versions the tests last passed with, install `requirements-lock.txt` first, then `pip install -e . --no-deps`. On Windows, use `.venv\Scripts\python` wherever these commands say `.venv/bin/python`.

```bash
.venv/bin/python -m arbdata download --start 2026-09-07 --end 2026-10-18 --source bybit_ob
```

```bash
.venv/bin/python -m arbdata build --start 2026-09-07 --end 2026-10-18
```

```bash
.venv/bin/python -m arbtrade.evaluate --pair btc_perp_binance_bybit --fees 1.0 --offset-aware --dump-trades --tag _v5
```

```bash
.venv/bin/python analysis/inventory_check.py --tag _v5 --baseline-tag _v4_offset
```

Useful `arbtrade.evaluate` options:
- `--venue-fees A B`: one taker fee per venue (leg a, leg b), for example `--venue-fees 1.7 3.0`.
- `--leg-latency-ms A B`: one order latency per venue instead of the equal-latency sweep, for example `--leg-latency-ms 50 8`.

`inventory_check.py` stops trading in each day's last 60 s and works the position down without taking more than the books show (`--close-window-s 0` gives the old close at the last quotes). It reports paired day-bootstrap differences against the naive and gap-size-only baselines, and against an earlier run with `--baseline-tag`.

```bash
.venv/bin/python -m arbdata record
```

Analysis (all on development days; none of these opens the holdout):

```bash
.venv/bin/python analysis/decay_pilot.py
```

```bash
.venv/bin/python analysis/decay_figures.py
```

```bash
.venv/bin/python analysis/pnl_figure.py --fee 1.0
```

```bash
.venv/bin/python analysis/pnl_stats.py --tag _v2 --fee 1.0
```

```bash
.venv/bin/python analysis/maker_taker.py
```

```bash
.venv/bin/python analysis/live_cross_check.py 2026-10-20
```

```bash
.venv/bin/python analysis/resolution_check.py 2026-10-19
```

```bash
.venv/bin/python analysis/live_prior.py 2026-10-19 2026-10-20
```

```bash
.venv/bin/python analysis/live_decay.py 2026-10-19 2026-10-20
```

```bash
.venv/bin/python analysis/maker_taker_live.py 2026-10-19 2026-10-20
```

The last five read the live recordings. The resolution check also needs Bybit's archive for that date, which is published the next UTC day.

## Evaluation rules

- **Holdout:** 10–18 Oct 2026 is frozen and locked behind `ARBDATA_UNLOCK_HOLDOUT=1`. Open it once, at the end.
- **Results so far:** everything reported here comes from development days, with walk-forward folds (training always before validation, one embargo day).
- **Two fill bounds:** the Bybit archive is sampled every 100 ms, so simulated fills on that leg are reported as an optimistic and a conservative bound. The 10 ms recorder narrows them.
- **The holdout has no cross-venue data.** All Binance vs Bybit data (January 2024) is in development, and the holdout window holds Bybit archive days only. So the taker and maker-taker strategies below cannot be scored on it. A separate cross-venue holdout (for example February–March 2024, which Binance's archive still covers) has to be frozen before anyone looks at it.

## Results so far (development data only)

All numbers below were re-run after the review fixes (offset-relative labelling, per-venue fees and latency, a depth-limited close, the cap at each trade's price, and $0 days for days without trades).

**Profit, with inventory accounted.** Binance vs Bybit BTC perpetual, January 2024, 24 walk-forward validation days, $10k per trade. Gaps are measured against the venues' trailing 5-minute offset. Positions are capped at $50k, funding is charged, no new trades are taken in each day's last 60 s, and the position is closed without taking more than the books show. Net P&L per validation day, with day-bootstrap 95% intervals.

*Realistic setup* (`data/reports/pnl/btc_perp_binance_bybit_v5_real/inventory.md`): top-tier taker fees per venue (Binance 1.7 bps, Bybit 3.0 bps) and the order latencies measured from our machine (Binance 50 ms, Bybit 8 ms).

| Fill bound | Naive fast path | Gap size only | Fast + decay prior | Slow model always | Cascade |
|---|---|---|---|---|---|
| Optimistic | −$567 [−961, −263] | $34 [8, 69] | $61 [17, 122] | $73 [23, 141] | **$69 [20, 135]** |
| Conservative | −$730 [−1,257, −329] | −$5 [−12, −0] | −$4 [−8, −0] | −$1 [−4, 1] | $0 [−1, 1] |

Paired differences (same days resampled): cascade minus naive is +$636 a day [+284, +1,093] with optimistic fills and +$730 [+329, +1,256] with conservative ones. Cascade minus the gap-size-only rule is +$35 [+10, +66] and +$5 [+0, +12].

*Fee sweep at 1 bps per leg, equal latency on both legs* (`data/reports/pnl/btc_perp_binance_bybit_v5/inventory.md`), for comparison with earlier runs:

| Latency, fill bound | Naive fast path | Gap size only | Cascade | Cascade − gap size only |
|---|---|---|---|---|
| 1 ms, optimistic | $228 [69, 449] | $360 [174, 606] | $370 [170, 637] | +$10 [−8, +32] |
| 10 ms, optimistic | −$1,074 [−1,567, −665] | $144 [83, 227] | $105 [30, 215] | −$39 [−77, −0] |
| 50 ms, optimistic | −$2,557 [−3,660, −1,636] | $98 [33, 190] | $157 [78, 271] | +$59 [+36, +86] |
| 10 ms, conservative | −$4,505 [−6,349, −2,971] | −$0 [−2, 1] | −$19 [−33, −8] | −$19 [−34, −7] |

- **What the fixes changed.** Labelling births on the offset-relative gap finds about four times as many opportunities (173,702 at 1 bps, against 44,102 when raw births were filtered). Day by day, the cascade is statistically unchanged from the earlier run (+$9 a day [−37, +68] at 10 ms, optimistic), while naive trading looks much worse because it now takes every relative gap.
- **Against a simple rule.** The decay models beat trading every gap above the fee threshold (the gap-size-only rule) in the realistic setup and at 50 ms, but not at 10 ms in the 1 bps sweep. Their edge over a simple rule is real but not uniform.
- **With conservative fills** every gated policy is close to break-even, and naive trading loses $600–4,700 a day.
- **Cascade vs slow-always:** statistically the same. The slow model's 6.4 µs is inference only; computing its features live has not been timed yet.
- **Why earlier numbers were higher.** Versions before the inventory accounting credited each trade with the whole gap measured from zero. In January 2024 Binance's BTC perpetual traded 0.5–3 bps below Bybit's, so most trades went the same way and mainly harvested that offset, which closing the positions pays back (`..._v3/inventory.md`).
- **Not yet modelled:** the delay before the trader sees each venue's quotes, the same displayed size being reused by trades close together, and a cross-venue holdout (see Evaluation rules).

Fills are limited to displayed top-of-book size, with no queue position or market impact.

**Decay** (`data/reports/decay/clean_vs_all.md`). Walk-forward AUC of "the gap is still open after 500 ms", births above 1 bps:

| Pair | All births | Clean births only | Gap size alone (clean) | Our 10 ms recordings (preliminary) |
|---|---|---|---|---|
| Binance vs Bybit BTC perpetual | 0.85 | 0.83 | 0.58 | 0.65 |
| Bybit BTC spot vs perpetual | 0.91 | 0.78 | 0.49 | 0.65 |
| Bybit ETH spot vs perpetual | 0.85 | 0.84 | 0.57 | 0.70 |
| Bybit ETH vs BTC (ratio) | 0.92 | 0.91 | 0.87 | not recorded |

- **Clean births** (both quotes fresh at birth) are the labels the 100 ms archive can be trusted on; the headline uses them.
- **The archive overstates predictability.** On our own 10 ms recordings the boosted model scores 0.64–0.74 at 50–500 ms on all four live pairs (about 5 h train, 2–3 h test), against 0.41–0.65 for gap size. More recording days should raise this.
- **Calibration:** the boosted model is already well calibrated (expected calibration error 0.01–0.03), and isotonic calibration does not improve it. It matters for the logistic prior (error up to 0.07), which is where it changed the P&L above.

**Maker-taker execution** (`arbtrade/makertaker.py`, `data/reports/maker_taker/summary.md`). Rest a buy or sell at Bybit's best price whenever Binance's price, as observed, covers both fees plus a margin. Queue behind the displayed size, fill from real Bybit trades, and hedge on Binance as a taker after both latencies. Positions, funding and closing are accounted as above.
- **January 2024, out of sample** (margin chosen on the first 20 days, P&L reported on the last 11), top-tier fees (0 maker, 1.7 bps taker), $50k cap, each partial fill hedged on its own: **+$17–19 a day [5, 36] from our machine** and **+$32–37 [10, 63] co-located** (`data/reports/maker_taker/summary.md`). Mid tier is about $4–12 a day; base tier is indistinguishable from zero.
- **Without inventory accounting** this was reported as $202 a day. Closing the one-way position (88% of fills went the same way) costs most of it; without a cap the same strategy loses $178 a day.
- **Today's market** (15.5 h of our recordings, a first look): between −$1.50 and +$1.10 an hour across settings. An earlier "$5–11 an hour" came partly from quotes frozen by a network outage, which a stale-quote guard now rejects.
- **Simplifications:** cancellations by others in the queue are ignored (pessimistic), one order per quoting spell, and no requotes.

**Current-market prior** (`data/reports/live/live_prior.md`, 7.9 h of recordings, split by time). At 1 bps per leg, trading every trigger loses $313 (BTC) and $504 (ETH) over the 2.4 h test window, while the prior-gated version stays at about $0. The prior is weakly predictive on so little data (AUC 0.57–0.67).

**Statistical-arbitrage pairs** (convergence trades: enter, hold until the dislocation closes or 60 s, exit; `arbtrade/convergence.py`):
- **At 1 bps per leg,** BTC spot vs perpetual and ETH vs BTC are not tradable. Naive loses $60–460 a day, and the decay-gated policies stand aside (about $0).
- **With no fees,** gating turns naive losses into gains under conservative fills. For example, the cascade makes +$957 a day vs naive's −$450 for BTC spot vs perpetual at 10 ms.

**Fee reality check:**
- **Published fees:** top-tier taker fees are about 1.7 bps per leg (Binance VIP 9) and 3 bps (Bybit PRO 6), per third-party comparisons; base tiers are 5–5.5 bps.
- **Current markets:** live data from October 2026 shows Binance and Bybit BTC perpetuals offset by a steady ~0.44 bps, with gaps above 2 bps almost never occurring. Neither taker-taker nor maker-taker arbitrage is profitable here at student-scale fees.

The decision framework (decay prediction plus latency-aware gating) is what carries over, to maker-taker execution and to other pairs.

## Ideas taken from other projects

We compared our system with three public arbitrage projects and adopted what was missing. None of them uses a predictive model; their strength is execution bookkeeping. All code here is our own implementation of the ideas.

| Idea | Source | Where it lives here |
|---|---|---|
| Per-venue inventory, a rebalancing cost and an inventory cap; never assume positions close for free | [TacosyHorchata/hackathon-btc-arbitrage](https://github.com/TacosyHorchata/hackathon-btc-arbitrage) | `arbtrade/inventory.py`, applied by `analysis/inventory_check.py` and `analysis/maker_taker.py` |
| A recorded reason for every accept or skip; stale-book rejection; a minimum size | the same project | `PaperEngine` decisions in `arbtrade/live.py`; the stale guard also in `arbtrade/makertaker.py` |
| Funding rates: a perpetual position pays or earns funding while it is held | [ksmit323/funding-rate-arbitrage](https://github.com/ksmit323/funding-rate-arbitrage) | `arbdata/funding.py`, charged in `inventory.py` |
| Per-venue fee tiers and a minimum-profit setting | [ArbiFlow](https://www.hackquest.io/projects/ArbiFlow) | `--venue-fees` in `arbtrade.evaluate`, the tier sweep in `analysis/maker_taker.py`, and the trigger (minimum profit). `config/sources.yaml` stores only VIP0 taker fees. |

## Next steps (from what the data showed)

1. **Record continuously on a VM** ([DEPLOY.md](DEPLOY.md)) and retrain the prior, decay and slow models on weeks of 10 ms data. January 2024 and October 2026 behave very differently: about 450 triggers an hour at 2 bps then, almost none now.
2. **Maker-taker, version 2:** estimate queue cancellations from book size changes, requote when the price moves, add inventory limits, and gate quotes with the decay model so we quote only when the Binance side is likely to hold until the hedge.
3. **Run the resolution check on more days** as Bybit publishes them, to firm up how many archive episodes are stale-quote artifacts.
4. **Web dashboard for the live demo**, on top of `arbtrade/live.py`.
5. **Open the holdout once, at the end** (`ARBDATA_UNLOCK_HOLDOUT=1`), and report it as it comes out.
