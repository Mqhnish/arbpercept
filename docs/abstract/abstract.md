# Latency-aware cross-venue arbitrage

Best viewed on our website, with interactive charts: [mqhnish.github.io/arbpercept](https://mqhnish.github.io/arbpercept/).

Code: [github.com/Mqhnish/arbpercept](https://github.com/Mqhnish/arbpercept).

## Problem & theme

Cross-asset statistical arbitrage with latency budgets, built for Perceptron 2026 (IIT Bombay × Optiver, Problem 6). A correct signal is worthless if [the gap closes before the order lands](#figures?f=surv), so we price each opportunity at the latency it will face, then act, think longer, or skip.

## Understanding of the challenge

- **Venue offset.** Binance and Bybit sit a drifting 0.4–3 bps apart; most raw gaps are that offset, repaid when positions close.
- **Sampling artefacts.** [About half the Bybit spot–perpetual gaps above 1 bps in the 100 ms archive are absent from 5.8 hours of our 10 ms recordings](#reports?p=resolution_check_BTC_2026-10-19.md).

## Proposed approach

Each candidate i is scored in bps at latency τ (feed delay, compute, order travel):

[formula]

q is the joint probability that both IOC legs fill at the observed prices after τ, learned from replayed fills; ê is the gap against the usual offset, c both legs' fees, ℓ̄ the average outcome of incomplete fills (predicted per trigger on the slow path).

[architecture diagram]

_Figure 1. Decision pipeline. Timings measured on our machine._

- **Data (about 295 GB raw).** Bybit 100 ms books and Binance ticks (May 2023–Jan 2024; Bybit also Sep–Oct 2026); Tardis.dev ticks, three venues (one day a month, 2020–2026); funding; our 10 ms recordings of ten coins on three venues (since 19 Oct 2026).
- **Fast path and [prior](#decay).** Fee-adjusted gap against a trailing 5-minute offset, then a calibrated six-feature logistic model of q (1.5 µs).
- **Slow model.** Gradient boosting on 28–36 causal features (Kalman, Ornstein–Uhlenbeck) for q, plus a second model for the cost of a miss: 20 µs per trigger compiled. The live path computes 23 features in about 30 µs.
- **Replay.** Order latency 50 ms Binance, 8 ms Bybit (estimated; no real orders), Bybit feed delay 45 ms, 40 µs slow wait, top-tier fees, $10k trades, $50k cap, optimistic and conservative fills.

## Minimum viable (built)

| Problem bullet | What exists | Demo |
|---|---|---|
| Detect mispricings | Offset-aware fast path; Kalman/OU fair value | [Paper trader logs every decision](#paper) |
| Report decay | [On our recordings, 61% of raw BTC Binance–Bybit gaps above 1 bps survive 50 ms, 31% 500 ms](#decay) | [Dashboard](#results) |

## Stretch ambitions (both built)

- **[Simulated end-to-end latency budget](#results?run=btc_perp_binance_bybit_v10_real).** P&L at our latencies, model time included.
- **[Paper-trading demo](#paper).** Live feeds, simulated fills; fast path and raw-gap prior so far.

## Novelty / differentiation

The starter baseline thresholds a paired price series. Three departures each changed the result (development days):

- **Gaps against the usual offset, with inventory counted.** Raw-gap "profit" was mostly the offset; it vanished once trades carried position, funding and a depth-limited close.
- **Decay-gated decisions.** [Trading every gap loses $94–925 a day per coin](#figures?f=naive). Gated, with optimistic fills, the cascade profits on [seven of nine coins](#coins?tag=_v10_real&mode=optimistic) (intervals above zero; BTC $20 a day, 95% CI $10 to $30, 205 days; up to $34 on SOL) and beats a gap-size-only model on seven, ARB borderline, DOGE not. [Conservative fills break even on the 100 ms archive](#coins?tag=_v10_real&mode=conservative); [on Tardis](#figures?f=tardis) they keep [$10–12 a day on BTC, ETH and SOL, every interval above zero](#coins?tag=_tardis_real&mode=conservative) (earlier model). [OKX pairs show no edge](#coins?tag=_tardis_real&mode=optimistic).
- **The cost of a miss, per trigger.** A miss is no fill (free) or an unwound leg (a loss); one average overcharged the harmless ones. Predicting it per trigger lifted P&L after closing on BTC (+$5 a day), SOL, TIA, WLD and AAVE (paired intervals above zero) and left four coins unchanged.

The cascade calls the slow model only when the prior is unsure, within $5 a day of "slow always".

## Evaluation plan

Five policies, identical replays: naive, gap-size-only, prior, slow always, cascade.

| Metric | Compared against |
|---|---|
| Net P&L/day after all costs at 1–50 ms latency; paired day-bootstrap 95% CIs | Naive, gap-size rule |
| [AUC, Brier skill, calibration of q and of P(gap open after τ)](#decay) | Gap size; constant survival rate |
| Median stage latency (µs); p99 on the VM | Order-latency budget |

Walk-forward folds, one-day embargo, training-day thresholds. [BTC spot–perpetual AUC at 500 ms falls from 0.78 on the archive to 0.65 on our recordings](#reports?p=live/live_decay.md), so archive AUCs look optimistic. The miss-cost design was chosen on validation days, so its gains are not out-of-sample. Two locked test sets (Bybit 10–18 Oct 2026; Binance vs Bybit Feb–Mar 2024) are unopened; we open them once and report everything.

## Feasibility and risks

### Team

- **Mohnish Rawat:** data and systems: recorders, pipeline, replay and inventory engine.
- **Anay Sharma:** statistics: evaluation, latency and fees, live slow path.
- **Arnav Jain:** backtesting and front end.

MVP and both stretch goals run ([168 tests, including a lookahead check](https://github.com/Mqhnish/arbpercept/tree/main/tests)).

### Status and next steps (17 Nov 2026)

- **Done:** 10 ms recording since 19 Oct (laptop); prior, slow model and miss cost in replay.
- **Next:** cloud VMs in Singapore and Tokyo; retrain on weeks of 10 ms data; a live slow model; maker-taker (replays $17–19 a day at top-tier fees on 11 held-out January 2024 days).

### Risks

- **Fees exceed most gaps.** Top-tier taker fees are 1.7–3 bps a leg, base tiers 5–5.5 bps, and 2026 gaps rarely pass 2 bps; at base-tier fees we found no profit. Slower strategies on free public data (funding carry, baskets, trend) were tested the same way: only funding carry is reliably positive, about 3% a year and falling.
- **Data gaps.** Outages are found from silences and skipped sequence numbers; affected episodes stay censored.
