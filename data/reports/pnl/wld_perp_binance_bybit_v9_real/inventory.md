# Taker strategies with inventory accounted: wld_perp_binance_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0. Optimistic and conservative are two simulation assumptions about the sampled Bybit book between snapshots, not guaranteed bounds on the truth.

## Fees 2.35 bps per leg (average of the two venues)

71 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 24% | -452 [-581, -345] | -471 [-600, -363] | -465 [-593, -358] |
| optimistic | 50.0 ms | Gap size only | 28% | 2 [-0, 6] | 2 [-1, 6] | 2 [-1, 6] |
| optimistic | 50.0 ms | Prior only | 39% | 11 [5, 18] | 8 [3, 15] | 8 [3, 15] |
| optimistic | 50.0 ms | Slow always | 37% | 15 [8, 23] | 13 [6, 20] | 13 [6, 20] |
| optimistic | 50.0 ms | Cascade | 40% | 10 [4, 16] | 8 [3, 14] | 8 [3, 14] |
| conservative | 50.0 ms | Naive | 6% | -346 [-459, -252] | -356 [-470, -262] | -356 [-470, -262] |
| conservative | 50.0 ms | Gap size only | 2% | -0 [-1, -0] | -0 [-1, -0] | -0 [-1, -0] |
| conservative | 50.0 ms | Prior only | 19% | -0 [-1, 1] | -0 [-1, 0] | -0 [-1, 0] |
| conservative | 50.0 ms | Slow always | 29% | 0 [-0, 2] | 0 [-1, 2] | 0 [-1, 2] |
| conservative | 50.0 ms | Cascade | 26% | -0 [-1, 0] | -0 [-1, 0] | -0 [-1, 0] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 50.0 ms | Cascade − Naive | +473 [+365, +603] |
| optimistic | 50.0 ms | Cascade − Slow always | -4 [-8, -1] |
| optimistic | 50.0 ms | Prior only − Gap size only | +6 [+2, +11] |
| optimistic | 50.0 ms | Cascade − Gap size only | +6 [+2, +11] |
| conservative | 50.0 ms | Cascade − Naive | +356 [+262, +470] |
| conservative | 50.0 ms | Cascade − Slow always | -1 [-2, +0] |
| conservative | 50.0 ms | Prior only − Gap size only | -0 [-1, +1] |
| conservative | 50.0 ms | Cascade − Gap size only | -0 [-1, +1] |

Closing, capped. Executed: really traded within the displayed size. Assumed: the rest, booked at the last quotes whatever their size. The last columns charge an extra cost on that rest.

| Fill bound | Latency | Strategy | Days with a rest | Rest, mean USD | Executed | Assumed | +5 bps | +10 bps | +25 bps |
|---|---|---|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 3 of 71 | 1,033 | -13 | -1 | -465 [-593, -359] | -466 [-593, -360] | -467 [-595, -361] |
| optimistic | 50.0 ms | Gap size only | 0 of 71 | 0 | -0 | +0 | 2 [-1, 6] | 2 [-1, 6] | 2 [-1, 6] |
| optimistic | 50.0 ms | Prior only | 0 of 71 | 0 | -3 | +0 | 8 [3, 15] | 8 [3, 15] | 8 [3, 15] |
| optimistic | 50.0 ms | Slow always | 0 of 71 | 0 | -2 | +0 | 13 [6, 20] | 13 [6, 20] | 13 [6, 20] |
| optimistic | 50.0 ms | Cascade | 0 of 71 | 0 | -1 | +0 | 8 [3, 14] | 8 [3, 14] | 8 [3, 14] |
| conservative | 50.0 ms | Naive | 2 of 71 | 352 | -10 | -0 | -356 [-471, -262] | -357 [-471, -262] | -357 [-471, -263] |
| conservative | 50.0 ms | Gap size only | 0 of 71 | 0 | -0 | +0 | -0 [-1, -0] | -0 [-1, -0] | -0 [-1, -0] |
| conservative | 50.0 ms | Prior only | 0 of 71 | 0 | -0 | +0 | -0 [-1, 0] | -0 [-1, 0] | -0 [-1, 0] |
| conservative | 50.0 ms | Slow always | 0 of 71 | 0 | -0 | +0 | 0 [-1, 2] | 0 [-1, 2] | 0 [-1, 2] |
| conservative | 50.0 ms | Cascade | 0 of 71 | 0 | -0 | +0 | -0 [-1, 0] | -0 [-1, 0] | -0 [-1, 0] |

Against the earlier run `_v7_real`, realised and capped:

| Fill bound | Latency | Strategy | This run − earlier run |
|---|---|---|---|
| optimistic | 50.0 ms | Naive | -48 [-65, -34] |
| optimistic | 50.0 ms | Gap size only | -1 [-2, -0] |
| optimistic | 50.0 ms | Prior only | +0 [-3, +3] |
| optimistic | 50.0 ms | Slow always | -0 [-2, +2] |
| optimistic | 50.0 ms | Cascade | +4 [+0, +8] |
| conservative | 50.0 ms | Naive | -48 [-65, -33] |
| conservative | 50.0 ms | Gap size only | +1 [-1, +2] |
| conservative | 50.0 ms | Prior only | +1 [-1, +2] |
| conservative | 50.0 ms | Slow always | +0 [-0, +1] |
| conservative | 50.0 ms | Cascade | -0 [-0, +0] |

