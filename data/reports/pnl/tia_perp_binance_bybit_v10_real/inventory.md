# Taker strategies with inventory accounted: tia_perp_binance_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0. Optimistic and conservative are two simulation assumptions about the sampled Bybit book between snapshots, not guaranteed bounds on the truth.

## Fees 2.35 bps per leg (average of the two venues)

42 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 22% | -791 [-1,041, -582] | -808 [-1,062, -594] | -803 [-1,056, -590] |
| optimistic | 50.0 ms | Gap size only | 20% | 9 [5, 13] | 8 [4, 12] | 8 [4, 12] |
| optimistic | 50.0 ms | Prior only | 31% | 22 [16, 30] | 20 [13, 27] | 20 [13, 27] |
| optimistic | 50.0 ms | Slow always | 33% | 33 [23, 43] | 30 [21, 39] | 30 [21, 39] |
| optimistic | 50.0 ms | Cascade | 33% | 32 [23, 43] | 29 [21, 39] | 29 [21, 39] |
| conservative | 50.0 ms | Naive | 7% | -803 [-1,049, -592] | -812 [-1,062, -598] | -810 [-1,057, -598] |
| conservative | 50.0 ms | Gap size only | 18% | -0 [-0, -0] | -0 [-1, -0] | -0 [-1, -0] |
| conservative | 50.0 ms | Prior only | 18% | -0 [-0, -0] | -0 [-0, -0] | -0 [-0, -0] |
| conservative | 50.0 ms | Slow always | 26% | 0 [-0, 0] | -0 [-0, 0] | -0 [-0, 0] |
| conservative | 50.0 ms | Cascade | 27% | 0 [-0, 0] | -0 [-0, 0] | -0 [-0, 0] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 50.0 ms | Cascade − Naive | +832 [+614, +1,093] |
| optimistic | 50.0 ms | Cascade − Slow always | -0 [-1, -0] |
| optimistic | 50.0 ms | Prior only − Gap size only | +12 [+8, +16] |
| optimistic | 50.0 ms | Cascade − Gap size only | +21 [+15, +29] |
| conservative | 50.0 ms | Cascade − Naive | +810 [+598, +1,057] |
| conservative | 50.0 ms | Cascade − Slow always | -0 [-0, +0] |
| conservative | 50.0 ms | Prior only − Gap size only | +0 [-0, +0] |
| conservative | 50.0 ms | Cascade − Gap size only | +0 [-0, +0] |

Closing, capped. Executed: really traded within the displayed size. Assumed: the rest, booked at the last quotes whatever their size. The last columns charge an extra cost on that rest.

| Fill bound | Latency | Strategy | Days with a rest | Rest, mean USD | Executed | Assumed | +5 bps | +10 bps | +25 bps |
|---|---|---|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 0 of 42 | 0 | -13 | +0 | -803 [-1,056, -590] | -803 [-1,056, -590] | -803 [-1,056, -590] |
| optimistic | 50.0 ms | Gap size only | 0 of 42 | 0 | -1 | +0 | 8 [4, 12] | 8 [4, 12] | 8 [4, 12] |
| optimistic | 50.0 ms | Prior only | 1 of 42 | 0 | -3 | +0 | 20 [13, 27] | 20 [13, 27] | 20 [13, 27] |
| optimistic | 50.0 ms | Slow always | 0 of 42 | 0 | -3 | +0 | 30 [21, 39] | 30 [21, 39] | 30 [21, 39] |
| optimistic | 50.0 ms | Cascade | 0 of 42 | 0 | -3 | +0 | 29 [21, 39] | 29 [21, 39] | 29 [21, 39] |
| conservative | 50.0 ms | Naive | 0 of 42 | 0 | -10 | +0 | -810 [-1,057, -598] | -810 [-1,057, -598] | -810 [-1,057, -598] |
| conservative | 50.0 ms | Gap size only | 0 of 42 | 0 | -0 | +0 | -0 [-1, -0] | -0 [-1, -0] | -0 [-1, -0] |
| conservative | 50.0 ms | Prior only | 0 of 42 | 0 | +0 | +0 | -0 [-0, -0] | -0 [-0, -0] | -0 [-0, -0] |
| conservative | 50.0 ms | Slow always | 0 of 42 | 0 | -0 | +0 | -0 [-0, 0] | -0 [-0, 0] | -0 [-0, 0] |
| conservative | 50.0 ms | Cascade | 0 of 42 | 0 | -0 | +0 | -0 [-0, 0] | -0 [-0, 0] | -0 [-0, 0] |

Against the earlier run `_v9_real`, realised and capped:

| Fill bound | Latency | Strategy | This run − earlier run |
|---|---|---|---|
| optimistic | 50.0 ms | Naive | +0 [-0, +0] |
| optimistic | 50.0 ms | Gap size only | -0 [-0, -0] |
| optimistic | 50.0 ms | Prior only | -0 [-0, +0] |
| optimistic | 50.0 ms | Slow always | +20 [+15, +27] |
| optimistic | 50.0 ms | Cascade | +19 [+14, +25] |
| conservative | 50.0 ms | Naive | -0 [-0, +0] |
| conservative | 50.0 ms | Gap size only | -0 [-0, -0] |
| conservative | 50.0 ms | Prior only | -0 [-0, -0] |
| conservative | 50.0 ms | Slow always | -0 [-1, +0] |
| conservative | 50.0 ms | Cascade | -0 [-0, +0] |

