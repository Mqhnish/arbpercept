# Taker strategies with inventory accounted: tick_sol_perp_okx_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0. Optimistic and conservative are two simulation assumptions about the sampled Bybit book between snapshots, not guaranteed bounds on the truth. No funding is charged on the okx leg: its history is not available.

## Fees 2.5 bps per leg (average of the two venues)

48 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 35.0 ms | Naive | 20% | -368 [-525, -236] | -425 [-590, -287] | -390 [-546, -260] |
| optimistic | 35.0 ms | Gap size only | 47% | 1 [-1, 2] | -0 [-2, 1] | -0 [-2, 1] |
| optimistic | 35.0 ms | Prior only | 35% | -2 [-8, 2] | -4 [-11, -0] | -4 [-11, -0] |
| optimistic | 35.0 ms | Slow always | 39% | 3 [-2, 8] | 0 [-4, 4] | -0 [-4, 4] |
| optimistic | 35.0 ms | Cascade | 35% | -2 [-9, 4] | -5 [-13, -0] | -5 [-13, -0] |
| conservative | 35.0 ms | Naive | 20% | -412 [-572, -278] | -448 [-615, -309] | -421 [-577, -289] |
| conservative | 35.0 ms | Gap size only | 50% | -0 [-1, 1] | -0 [-1, 1] | -0 [-1, 1] |
| conservative | 35.0 ms | Prior only | 36% | -1 [-2, 0] | -1 [-2, -0] | -1 [-2, -0] |
| conservative | 35.0 ms | Slow always | 42% | 2 [0, 4] | 1 [0, 3] | 1 [0, 3] |
| conservative | 35.0 ms | Cascade | 37% | 0 [-3, 3] | -2 [-5, 1] | -2 [-5, 1] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 35.0 ms | Cascade − Naive | +385 [+255, +540] |
| optimistic | 35.0 ms | Cascade − Slow always | -5 [-12, -1] |
| optimistic | 35.0 ms | Prior only − Gap size only | -4 [-9, -0] |
| optimistic | 35.0 ms | Cascade − Gap size only | -5 [-12, -0] |
| conservative | 35.0 ms | Cascade − Naive | +419 [+288, +575] |
| conservative | 35.0 ms | Cascade − Slow always | -3 [-6, -1] |
| conservative | 35.0 ms | Prior only − Gap size only | -1 [-2, +1] |
| conservative | 35.0 ms | Cascade − Gap size only | -2 [-4, +0] |

Closing, capped. Executed: really traded within the displayed size. Assumed: the rest, booked at the last quotes whatever their size. The last columns charge an extra cost on that rest.

| Fill bound | Latency | Strategy | Days with a rest | Rest, mean USD | Executed | Assumed | +5 bps | +10 bps | +25 bps |
|---|---|---|---|---|---|---|---|---|---|
| optimistic | 35.0 ms | Naive | 4 of 48 | 908 | -17 | -1 | -391 [-547, -261] | -391 [-547, -262] | -393 [-549, -263] |
| optimistic | 35.0 ms | Gap size only | 0 of 48 | 0 | -1 | +0 | -0 [-2, 1] | -0 [-2, 1] | -0 [-2, 1] |
| optimistic | 35.0 ms | Prior only | 1 of 48 | 179 | -2 | -0 | -4 [-11, -0] | -4 [-11, -0] | -5 [-11, -0] |
| optimistic | 35.0 ms | Slow always | 0 of 48 | 0 | -3 | +0 | -0 [-4, 4] | -0 [-4, 4] | -0 [-4, 4] |
| optimistic | 35.0 ms | Cascade | 0 of 48 | 0 | -3 | +0 | -5 [-13, -0] | -5 [-13, -0] | -5 [-13, -0] |
| conservative | 35.0 ms | Naive | 4 of 48 | 950 | -17 | -1 | -421 [-578, -290] | -422 [-578, -290] | -423 [-579, -292] |
| conservative | 35.0 ms | Gap size only | 0 of 48 | 0 | -0 | +0 | -0 [-1, 1] | -0 [-1, 1] | -0 [-1, 1] |
| conservative | 35.0 ms | Prior only | 0 of 48 | 0 | -0 | +0 | -1 [-2, -0] | -1 [-2, -0] | -1 [-2, -0] |
| conservative | 35.0 ms | Slow always | 0 of 48 | 0 | -0 | +0 | 1 [0, 3] | 1 [0, 3] | 1 [0, 3] |
| conservative | 35.0 ms | Cascade | 0 of 48 | 0 | -2 | +0 | -2 [-5, 1] | -2 [-5, 1] | -2 [-5, 1] |

