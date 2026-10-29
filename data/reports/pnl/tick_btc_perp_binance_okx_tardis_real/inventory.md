# Taker strategies with inventory accounted: tick_btc_perp_binance_okx

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0. Optimistic and conservative are two simulation assumptions about the sampled Bybit book between snapshots, not guaranteed bounds on the truth. No funding is charged on the okx leg: its history is not available.

## Fees 1.85 bps per leg (average of the two venues)

60 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 20% | -399 [-541, -276] | -449 [-609, -314] | -427 [-588, -299] |
| optimistic | 50.0 ms | Gap size only | 34% | 2 [-0, 5] | 1 [-1, 4] | 1 [-1, 4] |
| optimistic | 50.0 ms | Prior only | 31% | 1 [-1, 4] | 1 [-2, 3] | 1 [-2, 3] |
| optimistic | 50.0 ms | Slow always | 35% | -1 [-10, 5] | -5 [-13, 1] | -6 [-14, 0] |
| optimistic | 50.0 ms | Cascade | 37% | -1 [-10, 5] | -4 [-11, 1] | -5 [-13, 1] |
| conservative | 50.0 ms | Naive | 20% | -420 [-570, -291] | -462 [-626, -323] | -430 [-581, -303] |
| conservative | 50.0 ms | Gap size only | 33% | 2 [-0, 5] | 2 [-1, 4] | 2 [-1, 4] |
| conservative | 50.0 ms | Prior only | 32% | 1 [-2, 3] | 0 [-2, 2] | 0 [-2, 2] |
| conservative | 50.0 ms | Slow always | 37% | 3 [-1, 6] | 0 [-3, 3] | 0 [-3, 3] |
| conservative | 50.0 ms | Cascade | 37% | 4 [1, 7] | 1 [-1, 4] | 1 [-1, 4] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 50.0 ms | Cascade − Naive | +423 [+295, +581] |
| optimistic | 50.0 ms | Cascade − Slow always | +1 [-1, +3] |
| optimistic | 50.0 ms | Prior only − Gap size only | -1 [-2, +0] |
| optimistic | 50.0 ms | Cascade − Gap size only | -6 [-13, -1] |
| conservative | 50.0 ms | Cascade − Naive | +431 [+304, +582] |
| conservative | 50.0 ms | Cascade − Slow always | +1 [-0, +3] |
| conservative | 50.0 ms | Prior only − Gap size only | -1 [-3, -0] |
| conservative | 50.0 ms | Cascade − Gap size only | -0 [-1, +1] |

Closing, capped. Executed: really traded within the displayed size. Assumed: the rest, booked at the last quotes whatever their size. The last columns charge an extra cost on that rest.

| Fill bound | Latency | Strategy | Days with a rest | Rest, mean USD | Executed | Assumed | +5 bps | +10 bps | +25 bps |
|---|---|---|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 1 of 60 | 670 | -13 | -0 | -428 [-588, -299] | -428 [-588, -299] | -429 [-588, -300] |
| optimistic | 50.0 ms | Gap size only | 1 of 60 | 164 | -1 | -0 | 1 [-1, 4] | 1 [-1, 4] | 1 [-1, 3] |
| optimistic | 50.0 ms | Prior only | 1 of 60 | 164 | -1 | -0 | 1 [-2, 3] | 0 [-2, 3] | 0 [-2, 3] |
| optimistic | 50.0 ms | Slow always | 1 of 60 | 164 | -4 | -0 | -6 [-14, 0] | -6 [-14, 0] | -6 [-15, 0] |
| optimistic | 50.0 ms | Cascade | 1 of 60 | 164 | -4 | -0 | -5 [-13, 1] | -5 [-13, 1] | -5 [-13, 1] |
| conservative | 50.0 ms | Naive | 1 of 60 | 813 | -13 | -0 | -430 [-582, -304] | -431 [-582, -304] | -432 [-584, -306] |
| conservative | 50.0 ms | Gap size only | 1 of 60 | 164 | -1 | -0 | 2 [-1, 4] | 1 [-1, 4] | 1 [-1, 4] |
| conservative | 50.0 ms | Prior only | 1 of 60 | 164 | -1 | -0 | 0 [-2, 2] | 0 [-2, 2] | -0 [-2, 2] |
| conservative | 50.0 ms | Slow always | 1 of 60 | 164 | -2 | -0 | 0 [-3, 3] | 0 [-3, 3] | -0 [-4, 3] |
| conservative | 50.0 ms | Cascade | 1 of 60 | 164 | -2 | -0 | 1 [-1, 4] | 1 [-1, 4] | 1 [-2, 4] |

