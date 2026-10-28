# Taker strategies with inventory accounted: arb_perp_binance_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0. Optimistic and conservative are two simulation assumptions about the sampled Bybit book between snapshots, not guaranteed bounds on the truth.

## Fees 2.35 bps per leg (average of the two venues)

73 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 23% | -241 [-289, -196] | -260 [-313, -212] | -248 [-296, -204] |
| optimistic | 50.0 ms | Gap size only | 29% | 2 [0, 4] | 1 [-0, 3] | 1 [-0, 3] |
| optimistic | 50.0 ms | Prior only | 35% | 3 [1, 6] | 2 [-0, 4] | 2 [-0, 4] |
| optimistic | 50.0 ms | Slow always | 37% | 4 [1, 7] | 2 [-1, 5] | 2 [-1, 5] |
| optimistic | 50.0 ms | Cascade | 38% | 4 [1, 8] | 2 [-1, 6] | 2 [-1, 6] |
| conservative | 50.0 ms | Naive | 6% | -242 [-295, -194] | -249 [-304, -201] | -247 [-301, -199] |
| conservative | 50.0 ms | Gap size only | 14% | -1 [-2, -0] | -1 [-2, -0] | -1 [-2, -0] |
| conservative | 50.0 ms | Prior only | 20% | -0 [-1, -0] | -0 [-1, -0] | -0 [-1, -0] |
| conservative | 50.0 ms | Slow always | 27% | -1 [-2, -0] | -1 [-2, -0] | -1 [-2, -0] |
| conservative | 50.0 ms | Cascade | 35% | -0 [-1, -0] | -0 [-1, -0] | -0 [-1, -0] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 50.0 ms | Cascade − Naive | +251 [+206, +299] |
| optimistic | 50.0 ms | Cascade − Slow always | +0 [+0, +1] |
| optimistic | 50.0 ms | Prior only − Gap size only | +0 [-1, +2] |
| optimistic | 50.0 ms | Cascade − Gap size only | +1 [-2, +4] |
| conservative | 50.0 ms | Cascade − Naive | +247 [+199, +300] |
| conservative | 50.0 ms | Cascade − Slow always | +1 [+0, +2] |
| conservative | 50.0 ms | Prior only − Gap size only | +1 [+0, +1] |
| conservative | 50.0 ms | Cascade − Gap size only | +1 [+0, +2] |

Closing, capped. Executed: really traded within the displayed size. Assumed: the rest, booked at the last quotes whatever their size. The last columns charge an extra cost on that rest.

| Fill bound | Latency | Strategy | Days with a rest | Rest, mean USD | Executed | Assumed | +5 bps | +10 bps | +25 bps |
|---|---|---|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 3 of 73 | 697 | -12 | -0 | -249 [-296, -205] | -249 [-296, -205] | -250 [-297, -206] |
| optimistic | 50.0 ms | Gap size only | 0 of 73 | 0 | -1 | +0 | 1 [-0, 3] | 1 [-0, 3] | 1 [-0, 3] |
| optimistic | 50.0 ms | Prior only | 1 of 73 | 18 | -2 | -0 | 2 [-0, 4] | 2 [-0, 4] | 2 [-0, 4] |
| optimistic | 50.0 ms | Slow always | 0 of 73 | 0 | -2 | +0 | 2 [-1, 5] | 2 [-1, 5] | 2 [-1, 5] |
| optimistic | 50.0 ms | Cascade | 0 of 73 | 0 | -2 | +0 | 2 [-1, 6] | 2 [-1, 6] | 2 [-1, 6] |
| conservative | 50.0 ms | Naive | 1 of 73 | 94 | -7 | -0 | -247 [-301, -199] | -247 [-301, -199] | -247 [-301, -199] |
| conservative | 50.0 ms | Gap size only | 0 of 73 | 0 | -0 | +0 | -1 [-2, -0] | -1 [-2, -0] | -1 [-2, -0] |
| conservative | 50.0 ms | Prior only | 0 of 73 | 0 | -0 | +0 | -0 [-1, -0] | -0 [-1, -0] | -0 [-1, -0] |
| conservative | 50.0 ms | Slow always | 0 of 73 | 0 | -0 | +0 | -1 [-2, -0] | -1 [-2, -0] | -1 [-2, -0] |
| conservative | 50.0 ms | Cascade | 1 of 73 | 0 | -0 | -0 | -0 [-1, -0] | -0 [-1, -0] | -0 [-1, -0] |

Against the earlier run `_v7_real`, realised and capped:

| Fill bound | Latency | Strategy | This run − earlier run |
|---|---|---|---|
| optimistic | 50.0 ms | Naive | -40 [-49, -32] |
| optimistic | 50.0 ms | Gap size only | +1 [-0, +1] |
| optimistic | 50.0 ms | Prior only | -1 [-2, +1] |
| optimistic | 50.0 ms | Slow always | -1 [-2, +2] |
| optimistic | 50.0 ms | Cascade | +0 [-2, +3] |
| conservative | 50.0 ms | Naive | -32 [-41, -24] |
| conservative | 50.0 ms | Gap size only | +1 [-0, +2] |
| conservative | 50.0 ms | Prior only | +2 [+1, +2] |
| conservative | 50.0 ms | Slow always | +1 [+0, +1] |
| conservative | 50.0 ms | Cascade | -0 [-0, +0] |

