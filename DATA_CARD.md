# Data card: cross-asset arbitrage decay dataset

This pipeline (`arbdata`) builds one dataset of arbitrage opportunity episodes from four free sources and our own live recording, each used for what it does best. It is designed so that a model trained on it is not flattered by leakage, look-ahead or a lucky split.

## Sources and what each contributes

| Source | Instruments | Coverage | Resolution | Clocks | Role |
|---|---|---|---|---|---|
| Bybit public order book archive (`bybit_ob`) | BTC, ETH spot and USDT perpetual | Perpetual: Jun 2023 onward. Spot: ~Apr 2025 onward. Daily. | 100 ms snapshots with deltas, 200–500 levels | Publish time `ts`, matching engine time `cts` | Main dataset: continuous same-venue spot vs perpetual, so no cross-venue clock problem |
| Binance USD-M bookTicker archive (`binance_bt`) | BTC, ETH perpetual | 16 May 2023 to 30 Mar 2024, daily | Every top-of-book change (ms) | `event_time`, `transaction_time` | Continuous cross-venue perpetual vs perpetual against Bybit for ~10 months |
| Bybit public trade archive | BTC, ETH spot and USDT perpetual | Daily | Every trade (0.1 ms on perpetual, 1 ms on spot) | Matching-engine time | An independent record used to validate every reconstructed book, check clock alignment, and describe order flow |
| Our own live recording (`bybit_live`) | BTC, ETH spot and USDT perpetual | From 19 Oct 2026, while the recorder runs | Level 1, every change (12 ms median step measured) | This machine's receive time, plus matching-engine time | 10× finer timing than the archive, a true observer clock across legs, and a direct measurement of our own latency to Bybit (45 ms median, ~400 ms p99 from a home connection). That is feed delay measured from recorded timestamps. The order latencies used in simulation (8 ms Bybit, 50 ms Binance) are a separate measurement, kept in `order_latency_ms` in `config/sources.yaml` |
| Our own Binance recording (`binance_live`) | BTC, ETH USD-M perpetual | From 19 Oct 2026 (19:07 UTC), while the recorder runs | Every top-of-book change (~650 updates/s for both) | Same receive clock as `bybit_live`, plus transaction time | Current cross-venue data with a common observer clock (Binance's free bookTicker archive ends in March 2024) |
| Perpetual funding rates (`arbdata/funding.py`) | BTC, ETH USDT perpetual on Binance and Bybit | January 2024 on both; October 2026 on Bybit (Binance publishes a month's file after it ends, and its REST API refuses this region) | Every funding time (8 h) | Funding timestamp | What a position held across a funding time pays or receives. Cross-venue trades leave opposite positions on the two venues, so the P&L of carrying them depends on the difference in rates (January 2024 BTC: Bybit minus Binance averaged +0.10 bps per 8 h, sd 0.51) |
| Tardis.dev free days (`tardis`) | BTC spot and perpetual on Binance, OKX, Bybit | 1st of each month | Every top-of-book change (µs) | Collector receive time and exchange time | Tick-level ground truth: sub-100 ms lifetimes, a common observer clock across venues, and a check on how much 100 ms sampling misses |

Not used, and why:
- **Massive (formerly Polygon):** historical crypto is trades and bars only, with no bid/ask quotes.
- **Binance spot public data:** trades only, no quotes.
- **Kaggle-style datasets:** one-minute bars are far too coarse.
- **USD-quoted venues (Coinbase, Kraken):** USD and USDT are different currencies. Comparing them directly would label FX moves as arbitrage.

Tardis serves a bot check to scripted downloads from some networks. The downloader stops with a clear message rather than working around it. Download those files in a browser, or set `TARDIS_API_KEY`, and place them at the path the error names. Check each provider's terms of use before publishing data or results.

## Pipeline

```
download -> normalize + clean -> align pairs -> label episodes + causal features -> frozen splits -> report
```

```bash
.venv/bin/python -m arbdata download --start 2026-09-01 --end 2026-10-15 --source bybit_ob
.venv/bin/python -m arbdata download --start 2026-09-01 --end 2026-10-15 --source bybit_ob --trades
.venv/bin/python -m arbdata build --start 2026-09-01 --end 2026-10-15
.venv/bin/python -m pytest
```

`data/reports/REPORT.md` summarises quality, episode counts and splits after every build. Every raw file's URL, size and SHA-256 are in `data/raw/manifest.jsonl`. Raw files are never modified.

## Tables

**L1 (one per stream-day):** `avail_ts`, `exch_ts` (µs, UTC), `bid_px`, `bid_sz`, `ask_px`, `ask_sz`, `bid_depth5`, `ask_depth5`, `n_raw`, `resync`.
- `avail_ts` is when the quote became observable. All causality uses it. For the exchange archives it is the exchange's publish time, so those pairs describe a zero-network-latency observer. Network latency is added later, in simulation.
- Tick sources fold size-only updates into the preceding price change. Edges are therefore exact, and `n_raw` keeps the true update count. For example, 19.9M raw Binance updates on 15 Jan 2024 became 384k price changes.
- `n_raw` includes updates that arrive after `avail_ts`, so it is never used directly as a feature. Alignment credits each run's count only when the run closes.

**Silences (one per stream-day, `{date}.silences.parquet`):** gaps of more than 0.5 s in the *raw* update stream. Feed health is judged from these, not from price changes, because after folding, a quiet market and a dead feed look identical.

**Trades (one per Bybit stream-day):** `ts` (µs, matching engine), `price`, `size`, `side` (+1 buyer-initiated, −1 seller-initiated), `rpi`.
- `rpi` marks trades against Retail Price Improvement orders. Those orders are hidden from the public book stream, so RPI trades are left out of validation.

**Episodes (one per pair-day):** one row per (direction, hurdle, birth).
- `birth_ts`, `obs_ms`, `lower_ms`, `upper_ms`, `died`, `end_reason`
- `edge_birth_bps`, `edge_peak_bps`, `t_to_peak_ms`, `n_events`, `stale_birth`, `stale_partner`, `sub_resolution`, `resolution_ms`
- `stale_partner`: a sampled leg's quote was more than half a step old at the birth, so it may already have changed unseen.
- Feature columns prefixed `f_`. They cover spreads, top-of-book and depth notional, quote ages, feed lags, the basis and its deviation, trailing volatility, update rates, recent births, edge momentum, time of day, the slow-path statistics (`f_kalman_z` and `f_kalman_dev_bps` from a Kalman filter on the log-spread, `f_ou_halflife_s` from completed 1 s bars), and trade flow per leg (trades and notional per second, buy-minus-sell imbalance). Trade-flow columns are NaN for legs without a trade record.

**Funding (one per venue and symbol, `data/funding/<venue>_<symbol>.parquet`):** `ts` (µs, the funding time), `rate` (fraction of notional per interval; a long pays it, a short receives it). Fetched with `python -m arbdata.funding <start> <end>`.

**Edges, in bps of mid, after crossing both spreads:**
- **Cross pairs:** sell at one venue's bid and buy at the other's ask. The stored dataset measures this against zero. `label_pair_day(..., cross_offset_window_s=300)` measures it against the venues' trailing offset instead: the strictly-past median of mid a minus mid b, skipping moments when a leg is down. Then `edge_birth_bps` is the relative gap and `edge_offset_bps` is the offset that was subtracted. `arbtrade.evaluate --offset-aware` labels births this way.
- **Basis pairs:** the perpetual-minus-spot dislocation from its trailing 5-minute median. Profit here depends on the basis reverting, so it is a statistical edge, not a locked-in one.
- **Ratio pairs (cross-asset, e.g. ETH vs BTC perpetual on Bybit):** how far one asset's executable price sits from its fair value, given the other's executable price. Fair value is log(b) = α + β·log(a), with intercept and hedge ratio tracked by a two-state Kalman filter using only past data. Also a statistical edge.
  - **Caveat:** the filter's fair value adapts within about 4 s, so a "death" can be reversion or adaptation. Most lifetimes are far shorter (median 199 ms at 2 bps), but only a holding-period simulation can judge profitability.

## Practices built in, and what each prevents

| Practice | Prevents |
|---|---|
| Features use only data at or before the birth instant. `tests/test_no_lookahead.py` cuts the *raw* feeds at each birth, rebuilds everything and checks every feature is unchanged. Three planted leaks (a future-peeking reference level, folded update counts used too early, and trades counted 100 ms early) all fail it. |
| Trade features count only trades stamped at least 50 ms before a birth | Using trades an observer could not have seen yet: they carry matching-engine time but arrive later |
| Every Bybit book is checked against the independent trade record. A day fails on a persistent mismatch (5+ consecutive minutes where most trades miss the book) or a clock offset over 20 ms. Planted faults (a 10-minute corrupted book, a 300 ms skew) are both caught, while every real day passes. | Undetected reconstruction errors and misaligned clocks. A stricter "trades inside the spread" rule was rejected: it failed 9 of the most volatile days for normal sweeps, and dropping them would have biased the data toward calm markets. |
| `stale_partner` flag on births where a sampled leg's quote is over half a step old (kept by default, `drop_stale_partner=True` for the cleanest labels) | Treating fresh-against-stale quote comparisons, the main source of 100 ms sampling artifacts, as real opportunities | Look-ahead bias, the most common reason backtests look too good |
| Raw update times are sorted before silences are measured, and Binance rows are put back in update-id order (the 2 Jan 2024 file interleaves chunks: 180,806 backward jumps); disorder is reported per day | A shuffled file creating fake day-long outages, or a book rebuilt in the wrong order |
| A snapshot that continues the update-id sequence is not a rebuild (level-1 streams re-send unchanged snapshots; archive files end with one) | False resyncs |
| Feed outages detected from raw update silences, never from price changes | Quiet markets mislabelled as outages (this once made a healthy Binance day read 57% coverage) |
| Reference levels (normal basis) are left-closed windows | The label being measured against itself |
| Splits are by calendar date, identical across sources, never random | Same-day near-duplicates in train and test; a day's tick-level twin leaking across splits |
| Embargo day between train and validation and before the holdout | Regime and autocorrelation bleed across a boundary |
| Holdout = the most recent calendar window, frozen on first creation; data added later is assigned by date (older dates join development); readable only with `ARBDATA_UNLOCK_HOLDOUT=1` | Tuning on the test set; quietly moving the test set after a bad result |
| Walk-forward folds (train always before validation) | Training on the future |
| Censored episodes kept with `died=False`; births before valid data dropped | Lifetimes biased short by dropping long-lived episodes; invented birth times |
| Interval bounds `[lower_ms, upper_ms]` from each pair's resolution, plus a `sub_resolution` flag (kept by default) | False precision from 100 ms sampling, and the upward bias that dropping short episodes would cause |
| Gaps over `max_gap_ms` and missed updates (`resync`) invalidate the moment | Fake opportunities from a frozen feed |
| Crossed or locked single-venue books and isolated spikes removed; counts reported | Bad ticks labelled as arbitrage |
| `stale_birth` flag when a leg's publish lag exceeds 250 ms (dropped by default on load) | Opportunities that exist only because one feed is late |
| Several hurdles stored, chosen on validation only | Overfitting a single fee assumption |
| Per-split volatility check in the report | A holdout that tests a different regime than the one trained on, unnoticed |
| Day-stream excluded below 95% gap-free coverage | Days with outages distorting lifetimes |

## Recording live data

```bash
caffeinate -i .venv/bin/python -m arbdata record
```

It records Bybit (BTC and ETH, spot and perpetual, 10 ms level 1 plus trades) and Binance USD-M (BTC and ETH perpetual, every top-of-book change) on one receive clock. On a Mac, `caffeinate` keeps it awake while the recorder runs. On a Linux VM, use `deploy/arbdata-recorder.service`. The recorder writes one gzip file per hour and per run, flushed every 10 s, so a crash loses seconds and never corrupts other files. Reconnects are logged and marked, and the normaliser treats them as resyncs. About 140 MB a day for Bybit and 800 MB a day for Binance. Keep the machine's clock synced: receive timestamps are only as good as the clock.

`analysis/resolution_check.py <date>` compares a recorded day with Bybit's 100 ms archive for the same hours, once the archive for that date is published (the next UTC day).

## Using it

```python
from arbdata.dataset import load_episodes
train = load_episodes(split="train", fold=0, hurdle="gross>2bps")
val   = load_episodes(split="val",   fold=0, hurdle="gross>2bps")
```

Fit scalers, thresholds and hyperparameters on `train`, compare them on `val`, and evaluate on the holdout once. Survival models should use `lower_ms`/`upper_ms` (interval censoring, for example lifelines' `fit_interval_censoring`). Report results per pair and per volatility regime, not only pooled. Do not pool 100 ms and tick-level episodes without `resolution_ms` as a stratum or feature.

## Current build (rebuilt 20 Oct 2026 with final code)

**What's in it:**
- Bybit BTC and ETH spot and perpetual order books, every day from 7 Sep to 18 Oct 2026 (42 days).
- Binance vs Bybit BTC perpetual for all of January 2024 (31 days).
- Bybit's trade records for all of these days.
- Our own 10 ms live recording from 19 Oct 2026 onward.

**Quality:** all 230 stream-days passed.
- **Coverage:** the lowest gap-free coverage on any day was 99.06%, with at most 2 book rebuilds per day.
- **Trade check:** all 199 stream-days with a trade record passed. No day had more than 2 consecutive mismatched minutes, and the trade and book clocks agreed to 0 ms on every day.
- **Disorder:** one file (Binance, 2 Jan 2024) arrived out of order and was put back in update-id order.

**Splits:**
- Development: 63 dates.
- Embargo: 9 Oct.
- Holdout: 10–18 Oct 2026, frozen and still unopened.

The January 2024 month sits entirely in development, so the cross-venue pair is evaluated by walk-forward folds over its own dates.

**Development data only**, stale births dropped. "Fresh" = births where every sampled leg's quote was less than half a step old.

| Pair | Hurdle | Days | Episodes per day | Shorter than one 100 ms step | Resolved lifetime, median / p90 | Fresh births per day | Fresh: shorter than one step |
|---|---|---|---|---|---|---|---|
| Bybit BTC spot vs perpetual | gross > 1 bps | 32 | 5,016 | 69% | 586 / 4,300 ms | 2,189 | 39% |
| Same | gross > 2 bps | 32 | 613 | 93% | 200 / 2,418 ms | 79 | 63% |
| Same | gross > 5 bps | 31 | 31 | 95% | 400 / 6,991 ms | 2.6 | 55% |
| Bybit ETH spot vs perpetual | gross > 1 bps | 32 | 12,120 | 73% | 300 / 1,824 ms | 3,070 | 64% |
| Same | gross > 2 bps | 32 | 1,703 | 91% | 176 / 499 ms | 367 | 84% |
| Bybit ETH vs BTC perpetual (ratio) | gross > 2 bps | 32 | 2,028 | 66% | 199 / 597 ms | 1,269 | 50% |
| Same | gross > 5 bps | 32 | 128 | 73% | 199 / 595 ms | 79 | 60% |
| Binance vs Bybit BTC perpetual (Jan 2024) | gross > 2 bps | 31 | 10,854 | 42% | 637 / 7,703 ms | 7,433 | 39% |
| Same | 2-fill retail taker (10.5 bps) | 30 | 118 | 84% | 171 / 617 ms | 64 | 81% |

What this suggests so far:
- **Big gaps die within one sampling step.** The larger the dislocation, the more often it closes within 100 ms, so tick-level data is needed to time the opportunities that matter.
- **Most short episodes are stale-quote artifacts.** On the Bybit pair at 2 bps, 87% of births compare a fresh quote with one over 50 ms old, and 98% of those die within one step. Fresh births are far cleaner, but scarce: about 79 a day at 2 bps.
- **Episode counts follow volatility.** Across development days, episode count and daily volatility have a rank correlation of 0.95. The busiest days are the most volatile ones, not data faults. Report results per volatility regime.
- **Below-fee gaps persist; gaps above fees die fast.** On the January cross-venue month, gaps above 2 bps have a resolved median life of 637 ms (p90 7.7 s). Gaps clearing full retail fees live a median of 171 ms (p90 617 ms), and 84% of those die within one 100 ms step.
- **ETH dislocations decay faster than BTC's:** 300 ms vs 586 ms resolved median at 1 bps.
- **Survival is predictable from causal features** (walk-forward AUC at 500 ms, `data/reports/decay/`):

  | Pair | All births | Fresh births only | Gap size alone |
  |---|---|---|---|
  | Binance vs Bybit BTC perpetual | 0.85 | 0.83 | 0.57 |
  | Bybit BTC spot vs perpetual | 0.91 | 0.78 | 0.60 |
  | Bybit ETH spot vs perpetual | 0.85 | 0.84 | 0.56 |
  | Bybit ETH vs BTC (ratio) | 0.92 | 0.91 | 0.84 |

  Performance is stable across calm, normal and volatile days. On the three same-asset pairs gap size is nearly useless. On the cross-asset ratio pair it carries most of the signal: larger dislocations last longer, partly because the Kalman fair value takes seconds to absorb them.

  These archive scores are an upper bound. On our own 10 ms recordings the same model scores 0.64–0.74 at 50–500 ms (`analysis/live_decay.py`, a few hours of data so far), and the boosted model is already well calibrated (expected calibration error 0.01–0.03; `data/reports/decay/clean_vs_all.md`).

## Known limitations

- **100 ms cadence:** Bybit archive pairs cannot time opportunities that open and close within one 100 ms step, and many of their opportunities are not real. Measured on 19 Oct 2026 against our 10 ms recording of the same 5.8 hours (`analysis/resolution_check.py`, matching births in the same direction within 100 ms):
  - **Above 1 bps:** only 47% (BTC) and 52% (ETH) of archive spot-vs-perpetual births exist in the 10 ms data. Among births shorter than one step, only 30–32% are real, and those real ones last a median of 12–17 ms.
  - **Above 2 bps (ETH):** the archive shows 14 births an hour, but only 6% are real; the 10 ms data shows 2 an hour.
  - **What to do:** treat archive episodes as an upper bound, and use `drop_stale_partner` or the 10 ms recordings where timing matters.
- **Trade-flow features use a fixed 50 ms publish allowance.** That's above the observed book feed lag p99 (42 ms). A trade feed's own lag is not measured, so check the features' importance with the allowance at 100 ms too.
- **Bybit sends nothing while its book is unchanged:** a silence of up to 3 s is treated as quiet, not as an outage.
- **No common receive clock:** Binance and Bybit archive timestamps are each exchange's own publish clock, so a few ms of clock offset between exchanges is possible. Our recorder stamps both venues on one receive clock, so the live recordings can estimate it (Tardis's free days, the other option, were blocked to scripted downloads).
- **Fees:** fees are published VIP0 taker rates and should be checked against current schedules. Edges are stored gross.
- **Day boundaries:** each day is processed independently. The first 5 minutes are warm-up (no births), and runs crossing midnight are censored.
- **Tardis free days:** one day a month is too few for tick-level training on its own. Use them for validation and calibration of the 100 ms data.
