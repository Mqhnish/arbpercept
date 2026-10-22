# Taker strategies with inventory accounted: btc_perp_binance_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0.

## Fees 2.35 bps per leg (average of the two venues)

205 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 25% | -241 [-337, -163] | -285 [-389, -202] | -240 [-309, -180] |
| optimistic | 50.0 ms | Gap size only | 30% | 8 [3, 13] | 6 [2, 11] | 6 [2, 11] |
| optimistic | 50.0 ms | Prior only | 40% | 22 [16, 29] | 17 [11, 23] | 16 [11, 22] |
| optimistic | 50.0 ms | Slow always | 50% | 29 [22, 37] | 19 [13, 27] | 18 [12, 25] |
| optimistic | 50.0 ms | Cascade | 46% | 29 [22, 37] | 19 [12, 27] | 18 [11, 25] |
| conservative | 50.0 ms | Naive | 5% | -349 [-451, -259] | -361 [-465, -269] | -337 [-427, -258] |
| conservative | 50.0 ms | Gap size only | 11% | -0 [-1, 0] | -0 [-1, 0] | -0 [-1, 0] |
| conservative | 50.0 ms | Prior only | 10% | -1 [-2, 0] | -1 [-2, 0] | -1 [-2, 0] |
| conservative | 50.0 ms | Slow always | 40% | -0 [-1, 0] | -1 [-2, -1] | -1 [-2, -1] |
| conservative | 50.0 ms | Cascade | 43% | -0 [-1, -0] | -1 [-2, -1] | -1 [-2, -1] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 50.0 ms | Cascade − Naive | +258 [+194, +330] |
| optimistic | 50.0 ms | Cascade − Slow always | -0 [-2, +1] |
| optimistic | 50.0 ms | Prior only − Gap size only | +10 [+6, +13] |
| optimistic | 50.0 ms | Cascade − Gap size only | +11 [+8, +15] |
| conservative | 50.0 ms | Cascade − Naive | +336 [+257, +426] |
| conservative | 50.0 ms | Cascade − Slow always | +0 [-0, +1] |
| conservative | 50.0 ms | Prior only − Gap size only | -0 [-1, +1] |
| conservative | 50.0 ms | Cascade − Gap size only | -1 [-1, +0] |

