# Taker strategies with inventory accounted: eth_perp_binance_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0. Optimistic and conservative are two simulation assumptions about the sampled Bybit book between snapshots, not guaranteed bounds on the truth.

## Fees 2.35 bps per leg (average of the two venues)

180 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 21% | -235 [-342, -159] | -266 [-377, -185] | -230 [-311, -169] |
| optimistic | 50.0 ms | Gap size only | 30% | 9 [6, 13] | 7 [4, 10] | 7 [4, 10] |
| optimistic | 50.0 ms | Prior only | 33% | 11 [7, 14] | 8 [5, 11] | 8 [5, 11] |
| optimistic | 50.0 ms | Slow always | 48% | 23 [17, 28] | 15 [11, 21] | 15 [11, 21] |
| optimistic | 50.0 ms | Cascade | 48% | 23 [18, 28] | 15 [11, 21] | 15 [11, 21] |
| conservative | 50.0 ms | Naive | 6% | -285 [-384, -210] | -296 [-397, -219] | -277 [-358, -212] |
| conservative | 50.0 ms | Prior only | 0% | -0 [-0, 0] | -0 [-0, 0] | -0 [-0, 0] |
| conservative | 50.0 ms | Slow always | 32% | -0 [-0, 0] | -0 [-1, 0] | -0 [-1, 0] |
| conservative | 50.0 ms | Cascade | 15% | -0 [-1, 0] | -0 [-1, -0] | -0 [-1, -0] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 50.0 ms | Cascade − Naive | +246 [+182, +330] |
| optimistic | 50.0 ms | Cascade − Slow always | -0 [-0, +0] |
| optimistic | 50.0 ms | Prior only − Gap size only | +0 [-2, +3] |
| optimistic | 50.0 ms | Cascade − Gap size only | +8 [+5, +11] |
| conservative | 50.0 ms | Cascade − Naive | +277 [+212, +357] |
| conservative | 50.0 ms | Cascade − Slow always | -0 [-1, +1] |

Closing, capped. Executed: really traded within the displayed size. Assumed: the rest, booked at the last quotes whatever their size. The last columns charge an extra cost on that rest.

| Fill bound | Latency | Strategy | Days with a rest | Rest, mean USD | Executed | Assumed | +5 bps | +10 bps | +25 bps |
|---|---|---|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 3 of 180 | 357 | -11 | -0 | -231 [-311, -169] | -231 [-311, -170] | -231 [-312, -170] |
| optimistic | 50.0 ms | Gap size only | 2 of 180 | 143 | -2 | -0 | 7 [4, 10] | 7 [4, 10] | 7 [4, 10] |
| optimistic | 50.0 ms | Prior only | 2 of 180 | 46 | -3 | -0 | 8 [5, 11] | 8 [4, 11] | 7 [4, 11] |
| optimistic | 50.0 ms | Slow always | 3 of 180 | 287 | -6 | -0 | 15 [11, 21] | 15 [11, 20] | 15 [10, 20] |
| optimistic | 50.0 ms | Cascade | 3 of 180 | 287 | -6 | -0 | 15 [11, 20] | 15 [11, 20] | 15 [10, 20] |
| conservative | 50.0 ms | Naive | 2 of 180 | 160 | -7 | -0 | -277 [-358, -212] | -277 [-358, -212] | -277 [-358, -213] |
| conservative | 50.0 ms | Prior only | 0 of 180 | 0 | +0 | +0 | -0 [-0, 0] | -0 [-0, 0] | -0 [-0, 0] |
| conservative | 50.0 ms | Slow always | 1 of 180 | 20 | -0 | -0 | -0 [-1, 0] | -0 [-1, 0] | -0 [-1, 0] |
| conservative | 50.0 ms | Cascade | 1 of 180 | 20 | -0 | -0 | -0 [-1, -0] | -0 [-1, -0] | -0 [-1, -0] |

Against the earlier run `_v7_real`, realised and capped:

| Fill bound | Latency | Strategy | This run − earlier run |
|---|---|---|---|
| optimistic | 50.0 ms | Naive | -57 [-71, -46] |
| optimistic | 50.0 ms | Gap size only | +1 [+0, +2] |
| optimistic | 50.0 ms | Prior only | -5 [-8, -2] |
| optimistic | 50.0 ms | Slow always | +0 [-1, +2] |
| optimistic | 50.0 ms | Cascade | +1 [-0, +3] |
| conservative | 50.0 ms | Naive | -48 [-61, -38] |
| conservative | 50.0 ms | Prior only | +0 [-0, +1] |
| conservative | 50.0 ms | Slow always | -0 [-1, +1] |
| conservative | 50.0 ms | Cascade | -0 [-1, +1] |

