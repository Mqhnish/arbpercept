# Taker strategies with inventory accounted: tick_btc_perp_binance_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0. Optimistic and conservative are two simulation assumptions about the sampled Bybit book between snapshots, not guaranteed bounds on the truth.

## Fees 2.35 bps per leg (average of the two venues)

56 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 33% | -376 [-616, -181] | -481 [-795, -238] | -406 [-659, -206] |
| optimistic | 50.0 ms | Gap size only | 34% | 6 [1, 12] | 3 [-1, 9] | 3 [-1, 9] |
| optimistic | 50.0 ms | Prior only | 35% | 12 [5, 19] | 7 [2, 13] | 7 [2, 13] |
| optimistic | 50.0 ms | Slow always | 46% | 22 [14, 31] | 9 [0, 19] | 9 [1, 18] |
| optimistic | 50.0 ms | Cascade | 44% | 23 [14, 33] | 11 [1, 21] | 11 [2, 20] |
| conservative | 50.0 ms | Naive | 30% | -476 [-814, -208] | -547 [-917, -257] | -493 [-824, -234] |
| conservative | 50.0 ms | Gap size only | 33% | 6 [1, 11] | 2 [-3, 8] | 2 [-3, 8] |
| conservative | 50.0 ms | Prior only | 31% | 8 [4, 14] | 4 [-1, 9] | 4 [-1, 9] |
| conservative | 50.0 ms | Slow always | 43% | 18 [12, 26] | 9 [2, 17] | 9 [2, 17] |
| conservative | 50.0 ms | Cascade | 42% | 19 [12, 27] | 10 [2, 18] | 10 [2, 18] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 50.0 ms | Cascade − Naive | +416 [+217, +670] |
| optimistic | 50.0 ms | Cascade − Slow always | +1 [-1, +4] |
| optimistic | 50.0 ms | Prior only − Gap size only | +4 [+0, +8] |
| optimistic | 50.0 ms | Cascade − Gap size only | +7 [+1, +15] |
| conservative | 50.0 ms | Cascade − Naive | +503 [+244, +834] |
| conservative | 50.0 ms | Cascade − Slow always | +1 [-0, +2] |
| conservative | 50.0 ms | Prior only − Gap size only | +2 [-2, +5] |
| conservative | 50.0 ms | Cascade − Gap size only | +7 [+1, +14] |

Closing, capped. Executed: really traded within the displayed size. Assumed: the rest, booked at the last quotes whatever their size. The last columns charge an extra cost on that rest.

| Fill bound | Latency | Strategy | Days with a rest | Rest, mean USD | Executed | Assumed | +5 bps | +10 bps | +25 bps |
|---|---|---|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 1 of 56 | 399 | -13 | -0 | -406 [-659, -207] | -406 [-659, -207] | -407 [-660, -208] |
| optimistic | 50.0 ms | Gap size only | 1 of 56 | 40 | -2 | -0 | 3 [-1, 9] | 3 [-1, 9] | 3 [-1, 9] |
| optimistic | 50.0 ms | Prior only | 1 of 56 | 40 | -4 | -0 | 7 [2, 13] | 7 [2, 13] | 7 [2, 13] |
| optimistic | 50.0 ms | Slow always | 2 of 56 | 223 | -10 | -0 | 9 [1, 18] | 9 [1, 18] | 9 [1, 18] |
| optimistic | 50.0 ms | Cascade | 1 of 56 | 219 | -10 | -0 | 10 [2, 20] | 10 [2, 20] | 10 [1, 20] |
| conservative | 50.0 ms | Naive | 1 of 56 | 399 | -13 | -0 | -493 [-824, -235] | -494 [-824, -235] | -494 [-825, -235] |
| conservative | 50.0 ms | Gap size only | 1 of 56 | 40 | -4 | -0 | 2 [-3, 8] | 2 [-3, 8] | 2 [-3, 7] |
| conservative | 50.0 ms | Prior only | 1 of 56 | 40 | -4 | -0 | 4 [-1, 9] | 4 [-1, 9] | 4 [-1, 9] |
| conservative | 50.0 ms | Slow always | 1 of 56 | 40 | -8 | -0 | 9 [2, 17] | 9 [2, 17] | 9 [2, 17] |
| conservative | 50.0 ms | Cascade | 1 of 56 | 219 | -8 | -0 | 10 [2, 18] | 9 [2, 18] | 9 [2, 17] |

