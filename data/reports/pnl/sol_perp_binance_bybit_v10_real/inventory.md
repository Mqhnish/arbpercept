# Taker strategies with inventory accounted: sol_perp_binance_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0. Optimistic and conservative are two simulation assumptions about the sampled Bybit book between snapshots, not guaranteed bounds on the truth.

## Fees 2.35 bps per leg (average of the two venues)

68 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 21% | -936 [-1,139, -754] | -979 [-1,194, -788] | -925 [-1,118, -751] |
| optimistic | 50.0 ms | Gap size only | 24% | 19 [11, 29] | 16 [9, 25] | 16 [9, 25] |
| optimistic | 50.0 ms | Prior only | 32% | 22 [11, 36] | 15 [6, 27] | 15 [6, 27] |
| optimistic | 50.0 ms | Slow always | 37% | 41 [28, 57] | 34 [22, 49] | 34 [22, 49] |
| optimistic | 50.0 ms | Cascade | 37% | 40 [27, 56] | 34 [21, 48] | 34 [21, 48] |
| conservative | 50.0 ms | Naive | 4% | -811 [-996, -647] | -826 [-1,015, -659] | -807 [-985, -649] |
| conservative | 50.0 ms | Gap size only | 8% | -1 [-2, -0] | -1 [-2, -0] | -1 [-2, -0] |
| conservative | 50.0 ms | Prior only | 14% | -1 [-2, 0] | -1 [-2, 0] | -1 [-2, 0] |
| conservative | 50.0 ms | Slow always | 9% | -0 [-2, 1] | -0 [-2, 1] | -0 [-2, 1] |
| conservative | 50.0 ms | Cascade | 13% | -0 [-0, 0] | -0 [-1, 0] | -0 [-1, 0] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 50.0 ms | Cascade − Naive | +959 [+778, +1,157] |
| optimistic | 50.0 ms | Cascade − Slow always | -1 [-2, +0] |
| optimistic | 50.0 ms | Prior only − Gap size only | -1 [-7, +5] |
| optimistic | 50.0 ms | Cascade − Gap size only | +18 [+12, +24] |
| conservative | 50.0 ms | Cascade − Naive | +807 [+649, +985] |
| conservative | 50.0 ms | Cascade − Slow always | +0 [-1, +2] |
| conservative | 50.0 ms | Prior only − Gap size only | +0 [-1, +1] |
| conservative | 50.0 ms | Cascade − Gap size only | +1 [+0, +2] |

Closing, capped. Executed: really traded within the displayed size. Assumed: the rest, booked at the last quotes whatever their size. The last columns charge an extra cost on that rest.

| Fill bound | Latency | Strategy | Days with a rest | Rest, mean USD | Executed | Assumed | +5 bps | +10 bps | +25 bps |
|---|---|---|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 0 of 68 | 0 | -13 | +0 | -925 [-1,118, -751] | -925 [-1,118, -751] | -925 [-1,118, -751] |
| optimistic | 50.0 ms | Gap size only | 0 of 68 | 0 | -3 | +0 | 16 [9, 25] | 16 [9, 25] | 16 [9, 25] |
| optimistic | 50.0 ms | Prior only | 0 of 68 | 0 | -7 | +0 | 15 [6, 27] | 15 [6, 27] | 15 [6, 27] |
| optimistic | 50.0 ms | Slow always | 1 of 68 | 0 | -7 | -0 | 34 [22, 49] | 34 [22, 49] | 34 [22, 49] |
| optimistic | 50.0 ms | Cascade | 1 of 68 | 0 | -7 | -0 | 34 [21, 48] | 34 [21, 48] | 34 [21, 48] |
| conservative | 50.0 ms | Naive | 1 of 68 | 0 | -10 | -0 | -807 [-985, -649] | -807 [-985, -649] | -807 [-985, -649] |
| conservative | 50.0 ms | Gap size only | 0 of 68 | 0 | -0 | +0 | -1 [-2, -0] | -1 [-2, -0] | -1 [-2, -0] |
| conservative | 50.0 ms | Prior only | 0 of 68 | 0 | -0 | +0 | -1 [-2, 0] | -1 [-2, 0] | -1 [-2, 0] |
| conservative | 50.0 ms | Slow always | 0 of 68 | 0 | -0 | +0 | -0 [-2, 1] | -0 [-2, 1] | -0 [-2, 1] |
| conservative | 50.0 ms | Cascade | 0 of 68 | 0 | -0 | +0 | -0 [-1, 0] | -0 [-1, 0] | -0 [-1, 0] |

Against the earlier run `_v9_real`, realised and capped:

| Fill bound | Latency | Strategy | This run − earlier run |
|---|---|---|---|
| optimistic | 50.0 ms | Naive | -0 [-0, +0] |
| optimistic | 50.0 ms | Gap size only | +0 [-0, +0] |
| optimistic | 50.0 ms | Prior only | +0 [-0, +0] |
| optimistic | 50.0 ms | Slow always | +10 [+6, +13] |
| optimistic | 50.0 ms | Cascade | +9 [+6, +13] |
| conservative | 50.0 ms | Naive | +0 [-0, +0] |
| conservative | 50.0 ms | Gap size only | -0 [-0, +0] |
| conservative | 50.0 ms | Prior only | +0 [-0, +0] |
| conservative | 50.0 ms | Slow always | -1 [-2, +1] |
| conservative | 50.0 ms | Cascade | -0 [-1, +1] |

