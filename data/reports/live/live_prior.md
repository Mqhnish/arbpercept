# Decay prior on the current market (2026-10-19, 2026-10-20)

Trigger 1.0 bps, latencies Binance 50 ms / Bybit 8 ms, $10k per trade, train on the first 70% of triggers in time, test on the last 30%.

## BTC

1,758 triggers over 7.9 h; 51% filled on both legs. Test AUC 0.57 (gap size alone 0.48).

| Fee per leg (bps) | Trade every trigger | Prior-gated | Trades taken by the prior |
|---|---|---|---|
| 0 | $221 | $221 | 528 of 528 |
| 0.5 | $-46 | $14 | 14 of 528 |
| 1 | $-313 | $15 | 2 of 528 |
| 2.5 | $-1,114 | $11 | 1 of 528 |

## ETH

3,166 triggers over 7.9 h; 51% filled on both legs. Test AUC 0.67 (gap size alone 0.48).

| Fee per leg (bps) | Trade every trigger | Prior-gated | Trades taken by the prior |
|---|---|---|---|
| 0 | $247 | $250 | 927 of 950 |
| 0.5 | $-129 | $3 | 59 of 950 |
| 1 | $-504 | $-3 | 6 of 950 |
| 2.5 | $-1,630 | $0 | 1 of 950 |

