# Taker strategies with inventory accounted: wld_perp_binance_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0.

## Fees 2.35 bps per leg (average of the two venues)

71 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 30% | -404 [-516, -310] | -422 [-535, -328] | -417 [-528, -324] |
| optimistic | 50.0 ms | Gap size only | 30% | 4 [1, 7] | 3 [1, 7] | 3 [1, 7] |
| optimistic | 50.0 ms | Prior only | 41% | 9 [4, 15] | 8 [3, 14] | 8 [3, 14] |
| optimistic | 50.0 ms | Slow always | 34% | 14 [8, 22] | 13 [6, 20] | 13 [6, 20] |
| optimistic | 50.0 ms | Cascade | 40% | 6 [1, 11] | 4 [-0, 10] | 4 [-0, 10] |
| conservative | 50.0 ms | Naive | 7% | -297 [-393, -216] | -309 [-406, -228] | -309 [-406, -228] |
| conservative | 50.0 ms | Gap size only | 9% | -1 [-2, 1] | -1 [-2, 0] | -1 [-2, 0] |
| conservative | 50.0 ms | Prior only | 8% | -1 [-2, 0] | -1 [-3, 0] | -1 [-3, 0] |
| conservative | 50.0 ms | Slow always | 32% | 0 [-1, 2] | 0 [-1, 1] | 0 [-1, 1] |
| conservative | 50.0 ms | Cascade | 23% | -0 [-1, 1] | -0 [-1, 0] | -0 [-1, 0] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 50.0 ms | Cascade − Naive | +421 [+327, +535] |
| optimistic | 50.0 ms | Cascade − Slow always | -8 [-14, -3] |
| optimistic | 50.0 ms | Prior only − Gap size only | +5 [+1, +9] |
| optimistic | 50.0 ms | Cascade − Gap size only | +1 [-3, +5] |
| conservative | 50.0 ms | Cascade − Naive | +308 [+228, +406] |
| conservative | 50.0 ms | Cascade − Slow always | -0 [-2, +1] |
| conservative | 50.0 ms | Prior only − Gap size only | -0 [-1, +0] |
| conservative | 50.0 ms | Cascade − Gap size only | +1 [-1, +2] |

