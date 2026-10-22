# Taker strategies with inventory accounted: doge_perp_binance_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0.

## Fees 2.35 bps per leg (average of the two venues)

73 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 26% | -409 [-552, -291] | -454 [-602, -331] | -418 [-555, -305] |
| optimistic | 50.0 ms | Gap size only | 27% | 3 [0, 6] | 2 [-0, 6] | 2 [-0, 6] |
| optimistic | 50.0 ms | Prior only | 35% | 6 [2, 10] | 4 [1, 8] | 4 [1, 8] |
| optimistic | 50.0 ms | Slow always | 42% | 4 [-1, 10] | 0 [-5, 6] | 0 [-5, 6] |
| optimistic | 50.0 ms | Cascade | 41% | 3 [-2, 8] | -2 [-7, 3] | -2 [-7, 3] |
| conservative | 50.0 ms | Naive | 6% | -403 [-544, -285] | -427 [-572, -306] | -411 [-548, -295] |
| conservative | 50.0 ms | Gap size only | 2% | -2 [-3, -1] | -2 [-3, -1] | -2 [-3, -1] |
| conservative | 50.0 ms | Prior only | 8% | -0 [-1, 0] | -0 [-1, 0] | -0 [-1, 0] |
| conservative | 50.0 ms | Slow always | 14% | -1 [-2, 0] | -1 [-2, -0] | -1 [-2, -0] |
| conservative | 50.0 ms | Cascade | 11% | -1 [-2, -0] | -1 [-2, -0] | -1 [-2, -0] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 50.0 ms | Cascade − Naive | +416 [+302, +552] |
| optimistic | 50.0 ms | Cascade − Slow always | -2 [-5, -0] |
| optimistic | 50.0 ms | Prior only − Gap size only | +2 [-1, +5] |
| optimistic | 50.0 ms | Cascade − Gap size only | -5 [-8, -1] |
| conservative | 50.0 ms | Cascade − Naive | +410 [+295, +547] |
| conservative | 50.0 ms | Cascade − Slow always | -0 [-1, +1] |
| conservative | 50.0 ms | Prior only − Gap size only | +1 [+0, +2] |
| conservative | 50.0 ms | Cascade − Gap size only | +1 [-0, +2] |

