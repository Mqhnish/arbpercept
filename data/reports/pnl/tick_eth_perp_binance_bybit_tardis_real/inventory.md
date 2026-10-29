# Taker strategies with inventory accounted: tick_eth_perp_binance_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0. Optimistic and conservative are two simulation assumptions about the sampled Bybit book between snapshots, not guaranteed bounds on the truth.

## Fees 2.35 bps per leg (average of the two venues)

55 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 29% | -338 [-533, -183] | -410 [-617, -243] | -411 [-620, -244] |
| optimistic | 50.0 ms | Gap size only | 40% | 29 [14, 48] | 21 [9, 36] | 16 [8, 27] |
| optimistic | 50.0 ms | Prior only | 45% | 23 [12, 36] | 16 [8, 27] | 15 [7, 24] |
| optimistic | 50.0 ms | Slow always | 46% | 46 [25, 70] | 28 [14, 46] | 22 [11, 36] |
| optimistic | 50.0 ms | Cascade | 44% | 50 [29, 75] | 31 [16, 50] | 25 [14, 38] |
| conservative | 50.0 ms | Naive | 27% | -452 [-728, -241] | -511 [-796, -290] | -497 [-773, -285] |
| conservative | 50.0 ms | Gap size only | 41% | 22 [11, 35] | 15 [8, 25] | 13 [7, 21] |
| conservative | 50.0 ms | Prior only | 40% | 21 [11, 32] | 14 [7, 22] | 12 [6, 20] |
| conservative | 50.0 ms | Slow always | 42% | 27 [14, 43] | 16 [7, 27] | 12 [5, 19] |
| conservative | 50.0 ms | Cascade | 40% | 31 [17, 49] | 17 [8, 30] | 12 [5, 20] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 50.0 ms | Cascade − Naive | +436 [+267, +647] |
| optimistic | 50.0 ms | Cascade − Slow always | +2 [-1, +6] |
| optimistic | 50.0 ms | Prior only − Gap size only | -2 [-6, +2] |
| optimistic | 50.0 ms | Cascade − Gap size only | +8 [+3, +14] |
| conservative | 50.0 ms | Cascade − Naive | +509 [+296, +785] |
| conservative | 50.0 ms | Cascade − Slow always | +0 [-2, +3] |
| conservative | 50.0 ms | Prior only − Gap size only | -1 [-3, +2] |
| conservative | 50.0 ms | Cascade − Gap size only | -1 [-6, +3] |

Closing, capped. Executed: really traded within the displayed size. Assumed: the rest, booked at the last quotes whatever their size. The last columns charge an extra cost on that rest.

| Fill bound | Latency | Strategy | Days with a rest | Rest, mean USD | Executed | Assumed | +5 bps | +10 bps | +25 bps |
|---|---|---|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 2 of 55 | 740 | -16 | -0 | -411 [-620, -244] | -412 [-620, -244] | -413 [-621, -245] |
| optimistic | 50.0 ms | Gap size only | 0 of 55 | 0 | -6 | +0 | 16 [8, 27] | 16 [8, 27] | 16 [8, 27] |
| optimistic | 50.0 ms | Prior only | 0 of 55 | 0 | -5 | +0 | 15 [7, 24] | 15 [7, 24] | 15 [7, 24] |
| optimistic | 50.0 ms | Slow always | 0 of 55 | 0 | -10 | +0 | 22 [11, 36] | 22 [11, 36] | 22 [11, 36] |
| optimistic | 50.0 ms | Cascade | 0 of 55 | 0 | -11 | +0 | 25 [14, 38] | 25 [14, 38] | 25 [14, 38] |
| conservative | 50.0 ms | Naive | 2 of 55 | 729 | -14 | -0 | -497 [-774, -285] | -498 [-774, -286] | -499 [-775, -287] |
| conservative | 50.0 ms | Gap size only | 0 of 55 | 0 | -5 | +0 | 13 [7, 21] | 13 [7, 21] | 13 [7, 21] |
| conservative | 50.0 ms | Prior only | 0 of 55 | 0 | -5 | +0 | 12 [6, 20] | 12 [6, 20] | 12 [6, 20] |
| conservative | 50.0 ms | Slow always | 0 of 55 | 0 | -7 | +0 | 12 [5, 19] | 12 [5, 19] | 12 [5, 19] |
| conservative | 50.0 ms | Cascade | 0 of 55 | 0 | -8 | +0 | 12 [5, 20] | 12 [5, 20] | 12 [5, 20] |

