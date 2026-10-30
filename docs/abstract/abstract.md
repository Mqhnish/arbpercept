# Latency-aware cross-venue arbitrage

Best viewed on our website, with interactive charts: [mqhnish.github.io/arbpercept](https://mqhnish.github.io/arbpercept/).

Code: [github.com/Mqhnish/arbpercept](https://github.com/Mqhnish/arbpercept).

## Problem & theme

Problem 6, Cross-Asset Statistical Arbitrage with Latency Budgets (Theme 3). A correct signal is worthless if the [gap closes before the order lands](#figures?f=surv), so we price each opportunity at the latency it will face, then act, think longer, or skip. It suits us: we already record three venues and replay every fill.

## Understanding of the challenge

Gaps decay while we compute and orders travel, so we rank candidates by the edge left after latency and fees.

- **Venue offset.** Binance and Bybit sit a drifting 0.4–3 bps apart; most raw gaps are that offset, repaid when positions close.
- **Sampling artefacts.** [About half the Bybit spot–perpetual gaps above 1 bps in the 100 ms archive are absent from 5.8 hours of our 10 ms recordings](#reports?p=resolution_check_BTC_2026-10-19.md).

## Proposed approach

Each candidate i is scored in bps at latency τ (feed delay, compute, order travel):

[formula]

q is the joint probability that both IOC legs fill at the observed prices after τ, learned from replayed fills; ê is the gap against the usual offset, c both legs' fees, ℓ̄ the average outcome of incomplete fills.

[architecture diagram]

_Figure 1. Decision pipeline. Timings measured on our machine._

- **Data (about 260 GB raw).** Bybit 100 ms books, validated against trades, and Binance ticks (May 2023–Jan 2024; Bybit also Sep–Oct 2026); Tardis.dev ticks on Binance, Bybit, OKX (one day a month, 2020–2026); funding; our 10 ms recordings of ten coins on three venues.
- **Fast path and [prior](#decay).** Fee-adjusted gap against a trailing 5-minute offset, then a calibrated six-feature logistic model of q (1.5 µs).
- **Slow model.** Gradient boosting on 27–43 causal features (Kalman, Ornstein–Uhlenbeck); the 23-feature live path takes about 30 µs.
- **Replay.** Order latency 50 ms Binance, 8 ms Bybit (estimated; no real orders), Bybit feed delay 45 ms, top-tier fees, $10k trades, $50k cap, optimistic and conservative fills.
- **Cross-asset pairs** (spot vs perpetual, ETH/BTC): [decay AUC 0.78–0.91 against 0.49–0.87 for gap size](#decay); no edge after fees.

## Minimum viable (built)

| Problem bullet | What exists | Demo |
|---|---|---|
| Detect mispricings with a threshold or statistical model | Offset-aware fast path; Kalman/OU fair value | [Paper trader logs every decision](#paper) |
| Report how fast opportunities decay | [On our recordings, 61% of raw BTC Binance–Bybit gaps above 1 bps survive 50 ms, 31% 500 ms](#decay) | [Dashboard](#results) |

## Stretch ambitions (both built)

- **[Simulated end-to-end latency budget](#results?run=btc_perp_binance_bybit_v9_real).** Next step from decay: P&L at our latencies, model time included.
- **[Paper-trading demo](#paper).** Live feeds, simulated fills, P&L; fast path and raw-gap prior so far.

## Novelty / differentiation

The starter baseline thresholds a paired price series. Two departures each changed the result (development days):

- **Gaps against the usual offset, with honest inventory.** Raw-gap "profit" was mostly the offset and vanished once each trade carried its position, funding and depth-limited close.
- **Decay-gated decisions.** [Trading every gap loses $94–925 a day per coin](#figures?f=naive). Gated, with optimistic fills, the cascade profits on [five of nine coins](#coins?tag=_v9_real&mode=optimistic) (intervals above zero; [$15 a day on BTC and ETH, BTC 95% CI $7 to $23, 205 days](#figures?f=btc)) and [beats a gap-size-only model on ETH, SOL, WLD and XRP (BTC borderline)](#figures?f=coins). [Conservative fills break even on the 100 ms archive](#coins?tag=_v9_real&mode=conservative); [on Tardis](#figures?f=tardis), which sees every quote, they keep [$10–12 a day on BTC, ETH and SOL, every interval above zero](#coins?tag=_tardis_real&mode=conservative). [OKX pairs show no edge](#coins?tag=_tardis_real&mode=optimistic) at assumed OKX costs.

The cascade calls the slow model only when the prior is unsure; its P&L stays within $7 a day of "slow always".

## Evaluation plan

Five policies, identical replays: naive, gap-size-only model, prior, slow always, cascade.

| Metric | Compared against |
|---|---|
| Net P&L/day after all costs at 1–50 ms latency; paired day-bootstrap 95% CIs | Naive, gap-size rule |
| [AUC, Brier skill, calibration of q and of P(gap open after τ)](#decay) | Gap size; constant survival rate |
| Median stage latency (µs); p99 on the VM | Order-latency budget |

Walk-forward folds, one-day embargo, training-day thresholds. [BTC spot–perpetual AUC at 500 ms falls from 0.78 on the archive to 0.65 on our recordings](#reports?p=live/live_decay.md), so archive AUCs look optimistic. Two locked test sets (Bybit 10–18 Oct 2026; Binance vs Bybit Feb–Mar 2024, setup fixed before download) are opened once, results reported in full.

## Feasibility and risks

### Team

- **Mohnish Rawat:** data and systems: recorders, Parquet pipeline, replay and inventory engine (Python, Numba).
- **Anay Sharma:** statistics: offset-aware evaluation, latency and fees, live slow path, dashboard.
- **Arnav Jain:** backtesting and front end.

MVP and both stretch goals run ([165 tests, including a lookahead check](https://github.com/Mqhnish/arbpercept/tree/main/tests)).

### Milestones

| Week (from 10 Nov) | Owner | Milestone | Done when |
|---|---|---|---|
| 1–2 | Mohnish | 10 ms recording from Singapore, Tokyo VMs | Two weeks, under 1% missing |
| 1–2 | Anay | Offset-aware prior, slow model live | Cascade runs live |
| 3 | Anay | Interval-censored survival model | Beats 0.74 AUC at 50 ms |
| 3 | Arnav | p50/p99 stage latency on the VM | On the dashboard |
| 4 | Anay, Mohnish | Maker-taker with queue cancellations | Re-scored; Midway report 1 Dec |
| 5 | All | Open locked tests once; slides | Reported in full |

### Risks

- **Fees exceed most gaps.** Top-tier taker fees are 1.7–3 bps a leg; 2026 gaps rarely pass 2 bps. We report conservative fills; maker-taker replays $17–19 a day on 11 held-out January 2024 days.
- **Data gaps.** Outages are found from silences and skipped sequence numbers; their episodes are kept censored (lifetime at least what was observed).
