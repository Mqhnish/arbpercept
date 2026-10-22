# Taker strategies with inventory accounted: aave_perp_binance_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0.

## Fees 2.35 bps per leg (average of the two venues)

64 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 26% | -69 [-86, -54] | -81 [-99, -63] | -80 [-98, -63] |
| optimistic | 50.0 ms | Gap size only | 31% | 3 [1, 5] | 2 [1, 4] | 2 [1, 4] |
| optimistic | 50.0 ms | Prior only | 46% | 5 [3, 8] | 4 [2, 6] | 4 [2, 6] |
| optimistic | 50.0 ms | Slow always | 40% | 4 [2, 7] | 3 [1, 6] | 3 [1, 6] |
| optimistic | 50.0 ms | Cascade | 39% | 5 [1, 8] | 2 [-1, 6] | 2 [-1, 6] |
| conservative | 50.0 ms | Naive | 6% | -75 [-95, -56] | -80 [-100, -60] | -80 [-100, -60] |
| conservative | 50.0 ms | Prior only | 9% | -0 [-0, -0] | -0 [-1, -0] | -0 [-1, -0] |
| conservative | 50.0 ms | Slow always | 27% | -0 [-1, 0] | -0 [-1, 0] | -0 [-1, 0] |
| conservative | 50.0 ms | Cascade | 24% | -0 [-0, 0] | -0 [-0, 0] | -0 [-0, 0] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 50.0 ms | Cascade − Naive | +82 [+64, +101] |
| optimistic | 50.0 ms | Cascade − Slow always | -1 [-4, +1] |
| optimistic | 50.0 ms | Prior only − Gap size only | +2 [+1, +4] |
| optimistic | 50.0 ms | Cascade − Gap size only | +0 [-2, +3] |
| conservative | 50.0 ms | Cascade − Naive | +79 [+60, +100] |
| conservative | 50.0 ms | Cascade − Slow always | +0 [-0, +1] |

