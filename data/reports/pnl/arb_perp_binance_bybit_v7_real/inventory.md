# Taker strategies with inventory accounted: arb_perp_binance_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0.

## Fees 2.35 bps per leg (average of the two venues)

73 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 27% | -200 [-240, -163] | -218 [-262, -178] | -208 [-248, -171] |
| optimistic | 50.0 ms | Gap size only | 31% | 1 [-1, 3] | 1 [-1, 3] | 1 [-1, 3] |
| optimistic | 50.0 ms | Prior only | 36% | 3 [1, 6] | 2 [0, 5] | 2 [0, 5] |
| optimistic | 50.0 ms | Slow always | 39% | 4 [2, 6] | 2 [0, 5] | 2 [0, 5] |
| optimistic | 50.0 ms | Cascade | 40% | 3 [1, 6] | 2 [0, 4] | 2 [0, 4] |
| conservative | 50.0 ms | Naive | 7% | -209 [-253, -169] | -219 [-266, -178] | -215 [-260, -174] |
| conservative | 50.0 ms | Gap size only | 14% | -2 [-3, -0] | -2 [-3, -1] | -2 [-3, -1] |
| conservative | 50.0 ms | Prior only | 15% | -2 [-3, -1] | -2 [-3, -1] | -2 [-3, -1] |
| conservative | 50.0 ms | Slow always | 25% | -2 [-3, -1] | -2 [-3, -1] | -2 [-3, -1] |
| conservative | 50.0 ms | Cascade | 26% | -0 [-0, 0] | -0 [-0, -0] | -0 [-0, -0] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 50.0 ms | Cascade − Naive | +210 [+173, +251] |
| optimistic | 50.0 ms | Cascade − Slow always | -0 [-2, +0] |
| optimistic | 50.0 ms | Prior only − Gap size only | +2 [-0, +4] |
| optimistic | 50.0 ms | Cascade − Gap size only | +1 [-1, +4] |
| conservative | 50.0 ms | Cascade − Naive | +215 [+174, +260] |
| conservative | 50.0 ms | Cascade − Slow always | +2 [+1, +3] |
| conservative | 50.0 ms | Prior only − Gap size only | -0 [-1, +1] |
| conservative | 50.0 ms | Cascade − Gap size only | +2 [+1, +3] |

