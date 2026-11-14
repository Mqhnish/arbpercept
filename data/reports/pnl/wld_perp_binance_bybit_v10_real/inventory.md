# Taker strategies with inventory accounted: wld_perp_binance_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0. Optimistic and conservative are two simulation assumptions about the sampled Bybit book between snapshots, not guaranteed bounds on the truth.

## Fees 2.35 bps per leg (average of the two venues)

71 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 24% | -452 [-581, -345] | -471 [-600, -363] | -465 [-593, -358] |
| optimistic | 50.0 ms | Gap size only | 29% | 2 [-0, 6] | 2 [-1, 6] | 2 [-1, 6] |
| optimistic | 50.0 ms | Prior only | 39% | 11 [5, 18] | 8 [3, 15] | 8 [3, 15] |
| optimistic | 50.0 ms | Slow always | 40% | 32 [22, 43] | 29 [20, 40] | 29 [20, 40] |
| optimistic | 50.0 ms | Cascade | 39% | 28 [19, 38] | 25 [17, 35] | 25 [17, 35] |
| conservative | 50.0 ms | Naive | 6% | -346 [-459, -252] | -356 [-470, -262] | -356 [-470, -262] |
| conservative | 50.0 ms | Gap size only | 2% | -0 [-1, -0] | -0 [-1, -0] | -0 [-1, -0] |
| conservative | 50.0 ms | Prior only | 19% | -0 [-1, 1] | -0 [-1, 0] | -0 [-1, 0] |
| conservative | 50.0 ms | Slow always | 19% | -1 [-2, -1] | -1 [-2, -1] | -1 [-2, -1] |
| conservative | 50.0 ms | Cascade | 12% | 0 [-0, 1] | 0 [-0, 1] | 0 [-0, 1] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 50.0 ms | Cascade − Naive | +490 [+378, +625] |
| optimistic | 50.0 ms | Cascade − Slow always | -4 [-7, -1] |
| optimistic | 50.0 ms | Prior only − Gap size only | +6 [+2, +11] |
| optimistic | 50.0 ms | Cascade − Gap size only | +23 [+15, +32] |
| conservative | 50.0 ms | Cascade − Naive | +356 [+262, +470] |
| conservative | 50.0 ms | Cascade − Slow always | +1 [+1, +2] |
| conservative | 50.0 ms | Prior only − Gap size only | -0 [-1, +1] |
| conservative | 50.0 ms | Cascade − Gap size only | +0 [-0, +1] |

Closing, capped. Executed: really traded within the displayed size. Assumed: the rest, booked at the last quotes whatever their size. The last columns charge an extra cost on that rest.

| Fill bound | Latency | Strategy | Days with a rest | Rest, mean USD | Executed | Assumed | +5 bps | +10 bps | +25 bps |
|---|---|---|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 3 of 71 | 1,033 | -13 | -1 | -465 [-593, -359] | -466 [-593, -360] | -467 [-595, -361] |
| optimistic | 50.0 ms | Gap size only | 0 of 71 | 0 | -0 | +0 | 2 [-1, 6] | 2 [-1, 6] | 2 [-1, 6] |
| optimistic | 50.0 ms | Prior only | 0 of 71 | 0 | -3 | +0 | 8 [3, 15] | 8 [3, 15] | 8 [3, 15] |
| optimistic | 50.0 ms | Slow always | 0 of 71 | 0 | -3 | +0 | 29 [20, 40] | 29 [20, 40] | 29 [20, 40] |
| optimistic | 50.0 ms | Cascade | 0 of 71 | 0 | -2 | +0 | 25 [17, 35] | 25 [17, 35] | 25 [17, 35] |
| conservative | 50.0 ms | Naive | 2 of 71 | 352 | -10 | -0 | -356 [-471, -262] | -357 [-471, -262] | -357 [-471, -263] |
| conservative | 50.0 ms | Gap size only | 0 of 71 | 0 | -0 | +0 | -0 [-1, -0] | -0 [-1, -0] | -0 [-1, -0] |
| conservative | 50.0 ms | Prior only | 0 of 71 | 0 | -0 | +0 | -0 [-1, 0] | -0 [-1, 0] | -0 [-1, 0] |
| conservative | 50.0 ms | Slow always | 0 of 71 | 0 | -0 | +0 | -1 [-2, -1] | -1 [-2, -1] | -1 [-2, -1] |
| conservative | 50.0 ms | Cascade | 0 of 71 | 0 | -0 | +0 | 0 [-0, 1] | 0 [-0, 1] | 0 [-0, 1] |

Against the earlier run `_v9_real`, realised and capped:

| Fill bound | Latency | Strategy | This run − earlier run |
|---|---|---|---|
| optimistic | 50.0 ms | Naive | +0 [-0, +0] |
| optimistic | 50.0 ms | Gap size only | -0 [-0, +0] |
| optimistic | 50.0 ms | Prior only | -0 [-0, +0] |
| optimistic | 50.0 ms | Slow always | +17 [+12, +22] |
| optimistic | 50.0 ms | Cascade | +17 [+12, +23] |
| conservative | 50.0 ms | Naive | -0 [-0, +0] |
| conservative | 50.0 ms | Gap size only | -0 [-0, +0] |
| conservative | 50.0 ms | Prior only | -0 [-0, +0] |
| conservative | 50.0 ms | Slow always | -2 [-3, -0] |
| conservative | 50.0 ms | Cascade | +0 [+0, +1] |

