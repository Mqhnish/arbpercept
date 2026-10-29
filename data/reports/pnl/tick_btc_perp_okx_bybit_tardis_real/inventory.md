# Taker strategies with inventory accounted: tick_btc_perp_okx_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0. Optimistic and conservative are two simulation assumptions about the sampled Bybit book between snapshots, not guaranteed bounds on the truth. No funding is charged on the okx leg: its history is not available.

## Fees 2.5 bps per leg (average of the two venues)

55 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 35.0 ms | Naive | 28% | -292 [-435, -170] | -333 [-479, -209] | -311 [-457, -189] |
| optimistic | 35.0 ms | Gap size only | 14% | -0 [-1, 1] | -0 [-1, 0] | -0 [-1, 0] |
| optimistic | 35.0 ms | Prior only | 40% | -2 [-3, -1] | -2 [-4, -1] | -2 [-4, -1] |
| optimistic | 35.0 ms | Slow always | 51% | -1 [-5, 4] | -3 [-8, 1] | -2 [-6, 1] |
| optimistic | 35.0 ms | Cascade | 42% | -3 [-8, 3] | -5 [-10, -0] | -4 [-8, -0] |
| conservative | 35.0 ms | Naive | 28% | -333 [-511, -185] | -369 [-551, -218] | -345 [-522, -200] |
| conservative | 35.0 ms | Gap size only | 14% | 0 [-1, 1] | -0 [-1, 0] | -0 [-1, 0] |
| conservative | 35.0 ms | Prior only | 17% | 0 [-1, 2] | 0 [-1, 2] | 0 [-1, 2] |
| conservative | 35.0 ms | Slow always | 34% | 1 [-1, 3] | 0 [-1, 2] | 0 [-1, 2] |
| conservative | 35.0 ms | Cascade | 30% | 0 [-2, 3] | -1 [-3, 2] | -1 [-3, 2] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 35.0 ms | Cascade − Naive | +307 [+187, +450] |
| optimistic | 35.0 ms | Cascade − Slow always | -2 [-3, -0] |
| optimistic | 35.0 ms | Prior only − Gap size only | -2 [-4, -1] |
| optimistic | 35.0 ms | Cascade − Gap size only | -4 [-7, -0] |
| conservative | 35.0 ms | Cascade − Naive | +344 [+199, +521] |
| conservative | 35.0 ms | Cascade − Slow always | -1 [-2, -0] |
| conservative | 35.0 ms | Prior only − Gap size only | +0 [-0, +1] |
| conservative | 35.0 ms | Cascade − Gap size only | -1 [-3, +1] |

Closing, capped. Executed: really traded within the displayed size. Assumed: the rest, booked at the last quotes whatever their size. The last columns charge an extra cost on that rest.

| Fill bound | Latency | Strategy | Days with a rest | Rest, mean USD | Executed | Assumed | +5 bps | +10 bps | +25 bps |
|---|---|---|---|---|---|---|---|---|---|
| optimistic | 35.0 ms | Naive | 0 of 55 | 0 | -15 | +0 | -311 [-457, -189] | -311 [-457, -189] | -311 [-457, -189] |
| optimistic | 35.0 ms | Gap size only | 0 of 55 | 0 | -0 | +0 | -0 [-1, 0] | -0 [-1, 0] | -0 [-1, 0] |
| optimistic | 35.0 ms | Prior only | 0 of 55 | 0 | -1 | +0 | -2 [-4, -1] | -2 [-4, -1] | -2 [-4, -1] |
| optimistic | 35.0 ms | Slow always | 0 of 55 | 0 | -2 | +0 | -2 [-6, 1] | -2 [-6, 1] | -2 [-6, 1] |
| optimistic | 35.0 ms | Cascade | 0 of 55 | 0 | -2 | +0 | -4 [-8, -0] | -4 [-8, -0] | -4 [-8, -0] |
| conservative | 35.0 ms | Naive | 0 of 55 | 0 | -15 | +0 | -345 [-522, -200] | -345 [-522, -200] | -345 [-522, -200] |
| conservative | 35.0 ms | Gap size only | 0 of 55 | 0 | -0 | +0 | -0 [-1, 0] | -0 [-1, 0] | -0 [-1, 0] |
| conservative | 35.0 ms | Prior only | 0 of 55 | 0 | -0 | +0 | 0 [-1, 2] | 0 [-1, 2] | 0 [-1, 2] |
| conservative | 35.0 ms | Slow always | 0 of 55 | 0 | -0 | +0 | 0 [-1, 2] | 0 [-1, 2] | 0 [-1, 2] |
| conservative | 35.0 ms | Cascade | 0 of 55 | 0 | -1 | +0 | -1 [-3, 2] | -1 [-3, 2] | -1 [-3, 2] |

