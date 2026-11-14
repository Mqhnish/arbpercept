# Taker strategies with inventory accounted: btc_perp_binance_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0. Optimistic and conservative are two simulation assumptions about the sampled Bybit book between snapshots, not guaranteed bounds on the truth.

## Fees 2.35 bps per leg (average of the two venues)

205 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 21% | -339 [-458, -240] | -384 [-510, -278] | -338 [-432, -254] |
| optimistic | 50.0 ms | Gap size only | 27% | 9 [5, 14] | 8 [4, 12] | 8 [4, 12] |
| optimistic | 50.0 ms | Prior only | 35% | 14 [8, 20] | 10 [4, 16] | 9 [3, 16] |
| optimistic | 50.0 ms | Slow always | 48% | 32 [22, 43] | 21 [11, 31] | 20 [10, 30] |
| optimistic | 50.0 ms | Cascade | 48% | 32 [22, 43] | 21 [11, 31] | 20 [10, 30] |
| conservative | 50.0 ms | Naive | 5% | -431 [-555, -322] | -442 [-568, -332] | -418 [-529, -319] |
| conservative | 50.0 ms | Gap size only | 3% | -0 [-1, -0] | -0 [-1, -0] | -0 [-1, -0] |
| conservative | 50.0 ms | Prior only | 14% | -1 [-2, -0] | -1 [-2, -0] | -1 [-2, -0] |
| conservative | 50.0 ms | Slow always | 18% | -1 [-2, -0] | -1 [-2, -0] | -1 [-2, -0] |
| conservative | 50.0 ms | Cascade | 13% | -1 [-1, -0] | -1 [-1, -0] | -1 [-1, -0] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 50.0 ms | Cascade − Naive | +358 [+271, +456] |
| optimistic | 50.0 ms | Cascade − Slow always | +0 [-0, +0] |
| optimistic | 50.0 ms | Prior only − Gap size only | +1 [-3, +5] |
| optimistic | 50.0 ms | Cascade − Gap size only | +12 [+4, +19] |
| conservative | 50.0 ms | Cascade − Naive | +417 [+319, +528] |
| conservative | 50.0 ms | Cascade − Slow always | +1 [-0, +1] |
| conservative | 50.0 ms | Prior only − Gap size only | -1 [-1, +0] |
| conservative | 50.0 ms | Cascade − Gap size only | -0 [-1, +0] |

Closing, capped. Executed: really traded within the displayed size. Assumed: the rest, booked at the last quotes whatever their size. The last columns charge an extra cost on that rest.

| Fill bound | Latency | Strategy | Days with a rest | Rest, mean USD | Executed | Assumed | +5 bps | +10 bps | +25 bps |
|---|---|---|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 7 of 205 | 782 | -12 | -0 | -338 [-432, -255] | -339 [-433, -255] | -340 [-434, -256] |
| optimistic | 50.0 ms | Gap size only | 0 of 205 | 0 | -1 | +0 | 8 [4, 12] | 8 [4, 12] | 8 [4, 12] |
| optimistic | 50.0 ms | Prior only | 1 of 205 | 25 | -4 | -0 | 9 [3, 16] | 9 [3, 16] | 9 [3, 16] |
| optimistic | 50.0 ms | Slow always | 4 of 205 | 398 | -9 | -0 | 20 [10, 30] | 19 [10, 30] | 19 [9, 29] |
| optimistic | 50.0 ms | Cascade | 4 of 205 | 398 | -9 | -0 | 20 [10, 30] | 19 [10, 30] | 19 [9, 29] |
| conservative | 50.0 ms | Naive | 2 of 205 | 154 | -7 | -0 | -418 [-529, -320] | -418 [-529, -320] | -418 [-529, -320] |
| conservative | 50.0 ms | Gap size only | 0 of 205 | 0 | -0 | +0 | -0 [-1, -0] | -0 [-1, -0] | -0 [-1, -0] |
| conservative | 50.0 ms | Prior only | 0 of 205 | 0 | -0 | +0 | -1 [-2, -0] | -1 [-2, -0] | -1 [-2, -0] |
| conservative | 50.0 ms | Slow always | 0 of 205 | 0 | -0 | +0 | -1 [-2, -0] | -1 [-2, -0] | -1 [-2, -0] |
| conservative | 50.0 ms | Cascade | 0 of 205 | 0 | -0 | +0 | -1 [-1, -0] | -1 [-1, -0] | -1 [-1, -0] |

Against the earlier run `_v9_real`, realised and capped:

| Fill bound | Latency | Strategy | This run − earlier run |
|---|---|---|---|
| optimistic | 50.0 ms | Naive | +0 [-0, +0] |
| optimistic | 50.0 ms | Gap size only | +0 [-0, +0] |
| optimistic | 50.0 ms | Prior only | -0 [-0, +0] |
| optimistic | 50.0 ms | Slow always | +5 [+2, +7] |
| optimistic | 50.0 ms | Cascade | +5 [+2, +8] |
| conservative | 50.0 ms | Naive | -0 [-0, +0] |
| conservative | 50.0 ms | Gap size only | +0 [-0, +0] |
| conservative | 50.0 ms | Prior only | +0 [+0, +0] |
| conservative | 50.0 ms | Slow always | +0 [-1, +1] |
| conservative | 50.0 ms | Cascade | -0 [-0, +0] |

