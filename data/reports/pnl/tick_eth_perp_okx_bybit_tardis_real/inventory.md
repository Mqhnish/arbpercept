# Taker strategies with inventory accounted: tick_eth_perp_okx_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0. Optimistic and conservative are two simulation assumptions about the sampled Bybit book between snapshots, not guaranteed bounds on the truth. No funding is charged on the okx leg: its history is not available.

## Fees 2.5 bps per leg (average of the two venues)

54 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 35.0 ms | Naive | 24% | -369 [-522, -240] | -440 [-607, -296] | -423 [-587, -281] |
| optimistic | 35.0 ms | Prior only | 32% | 1 [-0, 3] | -0 [-2, 1] | -0 [-2, 1] |
| optimistic | 35.0 ms | Slow always | 34% | 2 [-3, 9] | -3 [-7, 2] | -3 [-7, 2] |
| optimistic | 35.0 ms | Cascade | 42% | 2 [-1, 4] | -2 [-4, -0] | -2 [-4, -0] |
| conservative | 35.0 ms | Naive | 24% | -461 [-688, -284] | -519 [-772, -320] | -490 [-725, -304] |
| conservative | 35.0 ms | Prior only | 26% | 2 [-1, 8] | 1 [-2, 5] | 1 [-2, 5] |
| conservative | 35.0 ms | Slow always | 41% | 2 [-1, 8] | 1 [-1, 6] | 1 [-1, 6] |
| conservative | 35.0 ms | Cascade | 41% | 2 [-1, 8] | 1 [-2, 6] | 1 [-2, 6] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 35.0 ms | Cascade − Naive | +421 [+280, +584] |
| optimistic | 35.0 ms | Cascade − Slow always | +1 [-3, +4] |
| conservative | 35.0 ms | Cascade − Naive | +491 [+305, +726] |
| conservative | 35.0 ms | Cascade − Slow always | -0 [-0, +0] |

Closing, capped. Executed: really traded within the displayed size. Assumed: the rest, booked at the last quotes whatever their size. The last columns charge an extra cost on that rest.

| Fill bound | Latency | Strategy | Days with a rest | Rest, mean USD | Executed | Assumed | +5 bps | +10 bps | +25 bps |
|---|---|---|---|---|---|---|---|---|---|
| optimistic | 35.0 ms | Naive | 2 of 54 | 406 | -15 | -0 | -423 [-587, -281] | -423 [-587, -281] | -424 [-588, -281] |
| optimistic | 35.0 ms | Prior only | 0 of 54 | 0 | -1 | +0 | -0 [-2, 1] | -0 [-2, 1] | -0 [-2, 1] |
| optimistic | 35.0 ms | Slow always | 0 of 54 | 0 | -5 | +0 | -3 [-7, 2] | -3 [-7, 2] | -3 [-7, 2] |
| optimistic | 35.0 ms | Cascade | 0 of 54 | 0 | -3 | +0 | -2 [-4, -0] | -2 [-4, -0] | -2 [-4, -0] |
| conservative | 35.0 ms | Naive | 1 of 54 | 68 | -16 | -0 | -490 [-725, -304] | -490 [-725, -304] | -490 [-725, -304] |
| conservative | 35.0 ms | Prior only | 0 of 54 | 0 | -1 | +0 | 1 [-2, 5] | 1 [-2, 5] | 1 [-2, 5] |
| conservative | 35.0 ms | Slow always | 0 of 54 | 0 | -1 | +0 | 1 [-1, 6] | 1 [-1, 6] | 1 [-1, 6] |
| conservative | 35.0 ms | Cascade | 0 of 54 | 0 | -1 | +0 | 1 [-2, 6] | 1 [-2, 6] | 1 [-2, 6] |

