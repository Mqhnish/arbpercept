# Taker strategies with inventory accounted: xrp_perp_binance_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0.

## Fees 2.35 bps per leg (average of the two venues)

73 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 25% | -412 [-537, -304] | -489 [-628, -367] | -417 [-536, -314] |
| optimistic | 50.0 ms | Gap size only | 32% | -5 [-20, 4] | -9 [-25, 3] | -7 [-24, 3] |
| optimistic | 50.0 ms | Prior only | 26% | 10 [4, 19] | 7 [0, 14] | 7 [0, 14] |
| optimistic | 50.0 ms | Slow always | 32% | 8 [2, 15] | 4 [-1, 10] | 3 [-2, 9] |
| optimistic | 50.0 ms | Cascade | 30% | 11 [4, 19] | 8 [2, 15] | 8 [2, 15] |
| conservative | 50.0 ms | Naive | 7% | -483 [-640, -350] | -522 [-688, -380] | -470 [-614, -346] |
| conservative | 50.0 ms | Gap size only | 1% | -1 [-2, -0] | -1 [-2, -0] | -1 [-2, -0] |
| conservative | 50.0 ms | Prior only | 4% | -2 [-4, -1] | -3 [-4, -1] | -3 [-4, -1] |
| conservative | 50.0 ms | Slow always | 11% | -1 [-2, 1] | -1 [-2, 1] | -1 [-2, 1] |
| conservative | 50.0 ms | Cascade | 5% | -1 [-1, -0] | -1 [-1, -0] | -1 [-1, -0] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 50.0 ms | Cascade − Naive | +425 [+318, +548] |
| optimistic | 50.0 ms | Cascade − Slow always | +5 [+2, +7] |
| optimistic | 50.0 ms | Prior only − Gap size only | +14 [+2, +30] |
| optimistic | 50.0 ms | Cascade − Gap size only | +15 [+3, +32] |
| conservative | 50.0 ms | Cascade − Naive | +469 [+346, +614] |
| conservative | 50.0 ms | Cascade − Slow always | +0 [-1, +1] |
| conservative | 50.0 ms | Prior only − Gap size only | -2 [-3, -1] |
| conservative | 50.0 ms | Cascade − Gap size only | +0 [+0, +1] |

