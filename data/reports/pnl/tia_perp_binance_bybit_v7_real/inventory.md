# Taker strategies with inventory accounted: tia_perp_binance_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0.

## Fees 2.35 bps per leg (average of the two venues)

42 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 25% | -655 [-871, -474] | -672 [-892, -486] | -669 [-890, -484] |
| optimistic | 50.0 ms | Gap size only | 19% | 8 [4, 12] | 7 [3, 11] | 7 [3, 11] |
| optimistic | 50.0 ms | Prior only | 29% | 17 [11, 24] | 16 [11, 22] | 16 [11, 22] |
| optimistic | 50.0 ms | Slow always | 35% | 13 [7, 21] | 10 [4, 16] | 10 [4, 16] |
| optimistic | 50.0 ms | Cascade | 34% | 14 [7, 21] | 10 [4, 16] | 10 [4, 16] |
| conservative | 50.0 ms | Naive | 8% | -676 [-888, -495] | -685 [-901, -502] | -683 [-896, -502] |
| conservative | 50.0 ms | Gap size only | 6% | -0 [-0, -0] | -0 [-0, -0] | -0 [-0, -0] |
| conservative | 50.0 ms | Prior only | 28% | -0 [-1, -0] | -0 [-1, -0] | -0 [-1, -0] |
| conservative | 50.0 ms | Slow always | 32% | -1 [-2, -0] | -2 [-3, -0] | -2 [-3, -0] |
| conservative | 50.0 ms | Cascade | 32% | -1 [-2, -0] | -1 [-3, -0] | -1 [-3, -0] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 50.0 ms | Cascade − Naive | +679 [+492, +902] |
| optimistic | 50.0 ms | Cascade − Slow always | -0 [-1, +1] |
| optimistic | 50.0 ms | Prior only − Gap size only | +9 [+6, +14] |
| optimistic | 50.0 ms | Cascade − Gap size only | +3 [-1, +7] |
| conservative | 50.0 ms | Cascade − Naive | +682 [+501, +894] |
| conservative | 50.0 ms | Cascade − Slow always | +0 [-0, +0] |
| conservative | 50.0 ms | Prior only − Gap size only | -0 [-1, -0] |
| conservative | 50.0 ms | Cascade − Gap size only | -1 [-3, -0] |

