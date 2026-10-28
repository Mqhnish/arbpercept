# Taker strategies with inventory accounted: aave_perp_binance_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0. Optimistic and conservative are two simulation assumptions about the sampled Bybit book between snapshots, not guaranteed bounds on the truth.

## Fees 2.35 bps per leg (average of the two venues)

64 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 22% | -84 [-104, -65] | -95 [-117, -75] | -94 [-115, -74] |
| optimistic | 50.0 ms | Gap size only | 29% | 3 [1, 5] | 3 [1, 4] | 3 [1, 4] |
| optimistic | 50.0 ms | Prior only | 42% | 6 [3, 8] | 4 [2, 6] | 4 [2, 6] |
| optimistic | 50.0 ms | Slow always | 38% | 4 [2, 7] | 4 [1, 6] | 4 [1, 6] |
| optimistic | 50.0 ms | Cascade | 37% | 5 [2, 8] | 2 [-0, 5] | 2 [-0, 5] |
| conservative | 50.0 ms | Naive | 5% | -86 [-110, -65] | -90 [-114, -68] | -90 [-114, -68] |
| conservative | 50.0 ms | Prior only | 15% | -0 [-0, -0] | -0 [-0, -0] | -0 [-0, -0] |
| conservative | 50.0 ms | Slow always | 16% | -0 [-1, 0] | -0 [-1, 0] | -0 [-1, 0] |
| conservative | 50.0 ms | Cascade | 17% | -0 [-1, -0] | -0 [-1, -0] | -0 [-1, -0] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 50.0 ms | Cascade − Naive | +96 [+75, +118] |
| optimistic | 50.0 ms | Cascade − Slow always | -1 [-3, -0] |
| optimistic | 50.0 ms | Prior only − Gap size only | +1 [+0, +3] |
| optimistic | 50.0 ms | Cascade − Gap size only | -0 [-2, +2] |
| conservative | 50.0 ms | Cascade − Naive | +89 [+68, +113] |
| conservative | 50.0 ms | Cascade − Slow always | -0 [-0, +0] |

Closing, capped. Executed: really traded within the displayed size. Assumed: the rest, booked at the last quotes whatever their size. The last columns charge an extra cost on that rest.

| Fill bound | Latency | Strategy | Days with a rest | Rest, mean USD | Executed | Assumed | +5 bps | +10 bps | +25 bps |
|---|---|---|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 10 of 64 | 2,418 | -9 | -2 | -95 [-117, -75] | -96 [-118, -76] | -100 [-122, -79] |
| optimistic | 50.0 ms | Gap size only | 1 of 64 | 0 | -1 | -0 | 3 [1, 4] | 3 [1, 4] | 3 [1, 4] |
| optimistic | 50.0 ms | Prior only | 0 of 64 | 0 | -2 | +0 | 4 [2, 6] | 4 [2, 6] | 4 [2, 6] |
| optimistic | 50.0 ms | Slow always | 0 of 64 | 0 | -1 | +0 | 4 [1, 6] | 4 [1, 6] | 4 [1, 6] |
| optimistic | 50.0 ms | Cascade | 0 of 64 | 0 | -3 | +0 | 2 [-0, 5] | 2 [-0, 5] | 2 [-0, 5] |
| conservative | 50.0 ms | Naive | 1 of 64 | 65 | -4 | -0 | -90 [-114, -68] | -90 [-114, -68] | -90 [-114, -68] |
| conservative | 50.0 ms | Prior only | 0 of 64 | 0 | -0 | +0 | -0 [-0, -0] | -0 [-0, -0] | -0 [-0, -0] |
| conservative | 50.0 ms | Slow always | 0 of 64 | 0 | -0 | +0 | -0 [-1, 0] | -0 [-1, 0] | -0 [-1, 0] |
| conservative | 50.0 ms | Cascade | 0 of 64 | 0 | -0 | +0 | -0 [-1, -0] | -0 [-1, -0] | -0 [-1, -0] |

Against the earlier run `_v7_real`, realised and capped:

| Fill bound | Latency | Strategy | This run − earlier run |
|---|---|---|---|
| optimistic | 50.0 ms | Naive | -14 [-19, -10] |
| optimistic | 50.0 ms | Gap size only | +0 [-0, +1] |
| optimistic | 50.0 ms | Prior only | -0 [-1, +1] |
| optimistic | 50.0 ms | Slow always | +0 [-1, +1] |
| optimistic | 50.0 ms | Cascade | -0 [-2, +2] |
| conservative | 50.0 ms | Naive | -10 [-14, -6] |
| conservative | 50.0 ms | Prior only | +0 [-0, +0] |
| conservative | 50.0 ms | Slow always | +0 [-0, +0] |
| conservative | 50.0 ms | Cascade | -0 [-1, +0] |

