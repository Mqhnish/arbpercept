# Latency-aware cross-venue arbitrage

Perceptron 2026 · Problem 6 · github.com/Mqhnish/arbpercept

## Problem & theme

Problem 6, Cross-Asset Statistical Arbitrage with Latency Budgets (Theme 3). A correct signal is worthless if the [gap closes before the order lands](#figures?f=surv). We price each opportunity at the latency it will face, then act, think longer, or skip.

## Understanding of the challenge

Gaps decay while we compute and orders travel, so we rank the edge left after latency and fees. Two traps:

- **A steady venue offset.** Binance and Bybit sit a drifting 0.5–3 bps apart; most raw gaps are that offset, and the positions they leave cost the same to close.
- **Sampling artefacts.** [About half the opportunities in 100 ms archives are absent from our 10 ms recordings](#reports?p=resolution_check_BTC_2026-10-19.md).

## Proposed approach

Each candidate i is scored at its latency τ (feed delay, compute, order travel):

[formula]

q is the joint probability that both IOC legs fill at the observed prices after τ, distinct from the gap's survival probability; ê is the gap against the usual offset, c both legs' fees, ℓ̄ the average partial-fill outcome on training days.

[architecture diagram]

_Figure 1. Decision pipeline. Latencies measured on our machine._

- **Data.** Bybit 100 ms books and Binance ticks (May 2023–Jan 2024); Tardis.dev ticks on Binance, Bybit, OKX (first day of each month, 2020–2026); funding; our 10 ms recordings of ten coins.
- **Fast path.** Fee-adjusted top-of-book gap against a trailing 5-minute offset, about 2 µs per quote.
- **[Decay prior](#decay).** Six-feature logistic model of q, isotonically calibrated (1.5 µs).
- **Slow model.** Gradient boosting on 23 causal features (Kalman fair spread, Ornstein–Uhlenbeck half-life): about 15 µs per decision plus about 12 µs per price change, under 0.5% of the 8 ms order latency.
- **Replay.** Order latency estimated from measured network round trips (50 ms Binance, 8 ms Bybit; no real orders placed), measured feed delay, fees, depth used by fills, a $50k cap, two fill bounds.

## Minimum viable (built)

| Problem bullet | What exists | Demo |
|---|---|---|
| Detect mispricings with a threshold or statistical model | Offset-aware fast path; Kalman/OU fair value | [Paper trader logs every decision](#paper) |
| Report how fast opportunities decay | [Survival curves, median lifetimes, AUC of P(gap open after τ)](#decay) | [Dashboard regenerates both per run](#results) |

## Stretch ambitions (both built)

- **[Simulated end-to-end latency budget](#results?run=btc_perp_binance_bybit_v9_real).** Replay charges feed delay, order latency and measured model time.
- **[Paper-trading demo](#paper).** Live Binance and Bybit feeds, simulated fills, P&L, positions.

## Novelty: why this beats the obvious baseline

The starter baseline thresholds a paired price series. Three departures each changed the result (development-day replays; test sets locked):

- **Gaps against the usual offset, not zero.** Raw-gap "profit" was mostly the offset and vanished once positions, funding and closing costs were scored.
- **Decay-gated decisions.** [Trading every gap loses $94–925 a day per coin](#figures?f=naive). Gated, with optimistic fills, the cascade makes a small profit on [five of nine coins](#coins?tag=_v9_real&mode=optimistic) (intervals above zero; [$15 a day on BTC and ETH, BTC 95% CI $7 to $23, 205 days](#figures?f=btc)) and [beats a gap-size rule on five](#figures?f=coins). [Conservative fills break even on the 100 ms archive](#coins?tag=_v9_real&mode=conservative), which sees Bybit only in snapshots. [On Tardis tick data](#figures?f=tardis), which sees every quote change, they keep [$10–12 a day on BTC, ETH and SOL, every interval above zero](#coins?tag=_tardis_real&mode=conservative). [OKX pairs show no edge](#coins?tag=_tardis_real&mode=optimistic) at our assumed OKX fee and latency.
- **Inventory-honest P&L.** Every trade carries its position, funding and depth-limited close.

The cascade matches "slow model always" because the slow model costs only 15 µs; it leaves room for heavier models. Charts: [mqhnish.github.io/arbpercept](https://mqhnish.github.io/arbpercept/#figures).

## Evaluation plan

Five policies on identical replays: naive, gap-size rule, prior, slow always, cascade.

| Metric | Compared against |
|---|---|
| Net P&L/day after all costs; paired day-bootstrap 95% CIs | Naive, gap-size rule |
| [AUC, Brier skill, calibration of P(gap open after τ)](#decay) | Gap size; constant survival rate |
| Median stage latency (µs); p99 on the VM | Order-latency budget |

Walk-forward folds, one-day embargo, thresholds from training days. [Decay-model AUC on our 10 ms recordings is 0.64–0.74 at 50–500 ms](#reports?p=live/live_decay.md), so archive AUCs are an upper bound. Two locked test sets (Bybit 10–18 Oct 2026; Binance vs Bybit Feb–Mar 2024) are opened once and reported whatever they show.

## Feasibility and risks

### Team

- **Mohnish Rawat:** data and systems: recorders, Parquet pipeline, replay and inventory engine (Python, Numba).
- **Anay Sharma:** statistics: offset-aware evaluation, latency and fees, live slow path, dashboard.
- **Arnav Jain:** backtesting and front end.

The MVP and both stretch goals already run ([165 tests, including a lookahead check](https://github.com/Mqhnish/arbpercept/tree/main/tests)); all runs: [mqhnish.github.io/arbpercept](https://mqhnish.github.io/arbpercept/#results).

### Milestones

| Week | Owner | Milestone | Done when |
|---|---|---|---|
| 1–2 | Mohnish | 10 ms recording on a VM near exchanges | Two weeks, under 1% gaps |
| 3 | Anay | Interval-censored survival model | Beats gap size at 50 ms |
| 3 | Arnav | p50/p99 stage latency on the VM | On the dashboard |
| 4 | Anay, Mohnish | Maker-taker queue model | BTC cascade CI above $0 |
| 5 | All | Open locked tests once; slides | Reported as they come out |

### Risks and mitigations

- **Fees exceed most gaps.** Taker fees are 1.7–3 bps a leg; 2026 gaps rarely pass 2 bps. We report the conservative bound and test maker-taker and mid-caps.
- **Overfitting.** Calibration-day choices, paired comparisons, locked tests.
- **Unsynchronised clocks.** Both venues share one receive clock.
- **Data gaps.** Outages are detected from silences and skipped sequence numbers; affected episodes are kept censored.
