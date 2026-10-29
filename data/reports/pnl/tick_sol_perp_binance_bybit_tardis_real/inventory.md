# Taker strategies with inventory accounted: tick_sol_perp_binance_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0. Optimistic and conservative are two simulation assumptions about the sampled Bybit book between snapshots, not guaranteed bounds on the truth.

## Fees 2.35 bps per leg (average of the two venues)

49 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 22% | -343 [-512, -209] | -395 [-574, -255] | -376 [-543, -245] |
| optimistic | 50.0 ms | Gap size only | 29% | 29 [19, 40] | 20 [11, 31] | 20 [11, 31] |
| optimistic | 50.0 ms | Prior only | 29% | 30 [21, 41] | 21 [12, 31] | 20 [12, 30] |
| optimistic | 50.0 ms | Slow always | 33% | 33 [21, 46] | 21 [9, 33] | 19 [8, 32] |
| optimistic | 50.0 ms | Cascade | 33% | 36 [24, 51] | 22 [9, 36] | 20 [8, 34] |
| conservative | 50.0 ms | Naive | 22% | -451 [-650, -299] | -490 [-696, -333] | -468 [-657, -321] |
| conservative | 50.0 ms | Gap size only | 29% | 14 [6, 24] | 10 [2, 19] | 10 [2, 19] |
| conservative | 50.0 ms | Prior only | 34% | 14 [7, 22] | 10 [4, 19] | 10 [4, 19] |
| conservative | 50.0 ms | Slow always | 33% | 9 [3, 15] | 6 [1, 11] | 6 [1, 11] |
| conservative | 50.0 ms | Cascade | 34% | 18 [9, 28] | 10 [2, 20] | 10 [2, 19] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 50.0 ms | Cascade − Naive | +397 [+265, +568] |
| optimistic | 50.0 ms | Cascade − Slow always | +1 [-2, +4] |
| optimistic | 50.0 ms | Prior only − Gap size only | +0 [-3, +4] |
| optimistic | 50.0 ms | Cascade − Gap size only | +0 [-7, +8] |
| conservative | 50.0 ms | Cascade − Naive | +478 [+330, +669] |
| conservative | 50.0 ms | Cascade − Slow always | +3 [-2, +10] |
| conservative | 50.0 ms | Prior only − Gap size only | +1 [-3, +4] |
| conservative | 50.0 ms | Cascade − Gap size only | -0 [-4, +5] |

Closing, capped. Executed: really traded within the displayed size. Assumed: the rest, booked at the last quotes whatever their size. The last columns charge an extra cost on that rest.

| Fill bound | Latency | Strategy | Days with a rest | Rest, mean USD | Executed | Assumed | +5 bps | +10 bps | +25 bps |
|---|---|---|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 2 of 49 | 997 | -16 | -1 | -377 [-544, -246] | -377 [-544, -247] | -379 [-545, -248] |
| optimistic | 50.0 ms | Gap size only | 0 of 49 | 0 | -8 | +0 | 20 [11, 31] | 20 [11, 31] | 20 [11, 31] |
| optimistic | 50.0 ms | Prior only | 1 of 49 | 196 | -8 | -0 | 20 [11, 30] | 20 [11, 30] | 20 [11, 30] |
| optimistic | 50.0 ms | Slow always | 0 of 49 | 0 | -9 | +0 | 19 [8, 32] | 19 [8, 32] | 19 [8, 32] |
| optimistic | 50.0 ms | Cascade | 1 of 49 | 396 | -10 | -0 | 20 [8, 34] | 20 [7, 33] | 19 [7, 33] |
| conservative | 50.0 ms | Naive | 2 of 49 | 711 | -15 | -0 | -469 [-658, -322] | -469 [-658, -322] | -470 [-659, -324] |
| conservative | 50.0 ms | Gap size only | 0 of 49 | 0 | -4 | +0 | 10 [2, 19] | 10 [2, 19] | 10 [2, 19] |
| conservative | 50.0 ms | Prior only | 0 of 49 | 0 | -3 | +0 | 10 [4, 19] | 10 [4, 19] | 10 [4, 19] |
| conservative | 50.0 ms | Slow always | 0 of 49 | 0 | -3 | +0 | 6 [1, 11] | 6 [1, 11] | 6 [1, 11] |
| conservative | 50.0 ms | Cascade | 0 of 49 | 0 | -7 | +0 | 10 [2, 19] | 10 [2, 19] | 10 [2, 19] |

