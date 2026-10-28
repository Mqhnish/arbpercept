# Taker strategies with inventory accounted: tia_perp_binance_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0. Optimistic and conservative are two simulation assumptions about the sampled Bybit book between snapshots, not guaranteed bounds on the truth.

## Fees 2.35 bps per leg (average of the two venues)

42 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 22% | -791 [-1,041, -582] | -808 [-1,062, -594] | -803 [-1,056, -590] |
| optimistic | 50.0 ms | Gap size only | 20% | 9 [5, 13] | 8 [4, 12] | 8 [4, 12] |
| optimistic | 50.0 ms | Prior only | 31% | 23 [16, 30] | 20 [13, 27] | 20 [13, 27] |
| optimistic | 50.0 ms | Slow always | 38% | 14 [8, 22] | 9 [4, 15] | 9 [4, 15] |
| optimistic | 50.0 ms | Cascade | 38% | 15 [9, 23] | 10 [5, 16] | 10 [5, 16] |
| conservative | 50.0 ms | Naive | 7% | -803 [-1,049, -592] | -812 [-1,062, -598] | -810 [-1,057, -598] |
| conservative | 50.0 ms | Gap size only | 25% | -0 [-0, -0] | -0 [-0, -0] | -0 [-0, -0] |
| conservative | 50.0 ms | Prior only | 18% | -0 [-0, -0] | -0 [-0, -0] | -0 [-0, -0] |
| conservative | 50.0 ms | Slow always | 34% | 0 [-0, 1] | 0 [-0, 1] | 0 [-0, 1] |
| conservative | 50.0 ms | Cascade | 36% | 0 [-0, 0] | 0 [-0, 0] | 0 [-0, 0] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 50.0 ms | Cascade − Naive | +813 [+598, +1,070] |
| optimistic | 50.0 ms | Cascade − Slow always | +1 [+0, +2] |
| optimistic | 50.0 ms | Prior only − Gap size only | +12 [+8, +16] |
| optimistic | 50.0 ms | Cascade − Gap size only | +2 [-1, +6] |
| conservative | 50.0 ms | Cascade − Naive | +810 [+598, +1,057] |
| conservative | 50.0 ms | Cascade − Slow always | -0 [-1, +0] |
| conservative | 50.0 ms | Prior only − Gap size only | -0 [-0, +0] |
| conservative | 50.0 ms | Cascade − Gap size only | +0 [-0, +0] |

Closing, capped. Executed: really traded within the displayed size. Assumed: the rest, booked at the last quotes whatever their size. The last columns charge an extra cost on that rest.

| Fill bound | Latency | Strategy | Days with a rest | Rest, mean USD | Executed | Assumed | +5 bps | +10 bps | +25 bps |
|---|---|---|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 0 of 42 | 0 | -13 | +0 | -803 [-1,056, -590] | -803 [-1,056, -590] | -803 [-1,056, -590] |
| optimistic | 50.0 ms | Gap size only | 0 of 42 | 0 | -1 | +0 | 8 [4, 12] | 8 [4, 12] | 8 [4, 12] |
| optimistic | 50.0 ms | Prior only | 1 of 42 | 0 | -3 | +0 | 20 [13, 27] | 20 [13, 27] | 20 [13, 27] |
| optimistic | 50.0 ms | Slow always | 0 of 42 | 0 | -6 | +0 | 9 [4, 15] | 9 [4, 15] | 9 [4, 15] |
| optimistic | 50.0 ms | Cascade | 0 of 42 | 0 | -5 | +0 | 10 [5, 16] | 10 [5, 16] | 10 [5, 16] |
| conservative | 50.0 ms | Naive | 0 of 42 | 0 | -10 | +0 | -810 [-1,057, -598] | -810 [-1,057, -598] | -810 [-1,057, -598] |
| conservative | 50.0 ms | Gap size only | 0 of 42 | 0 | -0 | +0 | -0 [-0, -0] | -0 [-0, -0] | -0 [-0, -0] |
| conservative | 50.0 ms | Prior only | 0 of 42 | 0 | +0 | +0 | -0 [-0, -0] | -0 [-0, -0] | -0 [-0, -0] |
| conservative | 50.0 ms | Slow always | 0 of 42 | 0 | -0 | +0 | 0 [-0, 1] | 0 [-0, 1] | 0 [-0, 1] |
| conservative | 50.0 ms | Cascade | 0 of 42 | 0 | -0 | +0 | 0 [-0, 0] | 0 [-0, 0] | 0 [-0, 0] |

Against the earlier run `_v7_real`, realised and capped:

| Fill bound | Latency | Strategy | This run − earlier run |
|---|---|---|---|
| optimistic | 50.0 ms | Naive | -134 [-168, -103] |
| optimistic | 50.0 ms | Gap size only | +1 [-0, +2] |
| optimistic | 50.0 ms | Prior only | +3 [+1, +6] |
| optimistic | 50.0 ms | Slow always | -0 [-3, +2] |
| optimistic | 50.0 ms | Cascade | +1 [-2, +4] |
| conservative | 50.0 ms | Naive | -127 [-161, -97] |
| conservative | 50.0 ms | Gap size only | +0 [-0, +0] |
| conservative | 50.0 ms | Prior only | +0 [+0, +0] |
| conservative | 50.0 ms | Slow always | +2 [+1, +3] |
| conservative | 50.0 ms | Cascade | +1 [+0, +3] |

