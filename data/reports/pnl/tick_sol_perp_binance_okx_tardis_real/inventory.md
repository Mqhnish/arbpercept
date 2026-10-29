# Taker strategies with inventory accounted: tick_sol_perp_binance_okx

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0. Optimistic and conservative are two simulation assumptions about the sampled Bybit book between snapshots, not guaranteed bounds on the truth. No funding is charged on the okx leg: its history is not available.

## Fees 1.85 bps per leg (average of the two venues)

49 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 14% | -628 [-870, -434] | -678 [-932, -475] | -642 [-864, -461] |
| optimistic | 50.0 ms | Gap size only | 16% | -0 [-0, -0] | -0 [-0, -0] | -0 [-0, -0] |
| optimistic | 50.0 ms | Prior only | 13% | -0 [-2, 2] | -0 [-2, 1] | -0 [-2, 1] |
| optimistic | 50.0 ms | Slow always | 30% | -3 [-8, -0] | -5 [-10, -1] | -5 [-9, -1] |
| optimistic | 50.0 ms | Cascade | 32% | -3 [-8, 1] | -4 [-9, -1] | -4 [-8, -1] |
| conservative | 50.0 ms | Naive | 13% | -614 [-853, -426] | -642 [-889, -448] | -614 [-830, -438] |
| conservative | 50.0 ms | Gap size only | 17% | -0 [-0, -0] | -0 [-0, -0] | -0 [-0, -0] |
| conservative | 50.0 ms | Prior only | 15% | -0 [-1, 1] | -0 [-1, 1] | -0 [-1, 1] |
| conservative | 50.0 ms | Slow always | 26% | -1 [-2, 1] | -1 [-2, 1] | -1 [-2, 1] |
| conservative | 50.0 ms | Cascade | 27% | 0 [-0, 1] | 0 [-0, 1] | 0 [-0, 1] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 50.0 ms | Cascade − Naive | +639 [+457, +859] |
| optimistic | 50.0 ms | Cascade − Slow always | +1 [-0, +2] |
| optimistic | 50.0 ms | Prior only − Gap size only | -0 [-2, +1] |
| optimistic | 50.0 ms | Cascade − Gap size only | -4 [-8, -1] |
| conservative | 50.0 ms | Cascade − Naive | +614 [+438, +830] |
| conservative | 50.0 ms | Cascade − Slow always | +1 [-0, +2] |
| conservative | 50.0 ms | Prior only − Gap size only | +0 [-1, +1] |
| conservative | 50.0 ms | Cascade − Gap size only | +0 [-0, +1] |

Closing, capped. Executed: really traded within the displayed size. Assumed: the rest, booked at the last quotes whatever their size. The last columns charge an extra cost on that rest.

| Fill bound | Latency | Strategy | Days with a rest | Rest, mean USD | Executed | Assumed | +5 bps | +10 bps | +25 bps |
|---|---|---|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 3 of 49 | 658 | -16 | -1 | -643 [-864, -461] | -643 [-864, -462] | -644 [-865, -463] |
| optimistic | 50.0 ms | Gap size only | 0 of 49 | 0 | -0 | +0 | -0 [-0, -0] | -0 [-0, -0] | -0 [-0, -0] |
| optimistic | 50.0 ms | Prior only | 0 of 49 | 0 | -0 | +0 | -0 [-2, 1] | -0 [-2, 1] | -0 [-2, 1] |
| optimistic | 50.0 ms | Slow always | 0 of 49 | 0 | -1 | +0 | -5 [-9, -1] | -5 [-9, -1] | -5 [-9, -1] |
| optimistic | 50.0 ms | Cascade | 0 of 49 | 0 | -1 | +0 | -4 [-8, -1] | -4 [-8, -1] | -4 [-8, -1] |
| conservative | 50.0 ms | Naive | 2 of 49 | 534 | -13 | -1 | -614 [-830, -438] | -614 [-831, -439] | -615 [-832, -440] |
| conservative | 50.0 ms | Gap size only | 0 of 49 | 0 | -0 | +0 | -0 [-0, -0] | -0 [-0, -0] | -0 [-0, -0] |
| conservative | 50.0 ms | Prior only | 0 of 49 | 0 | -0 | +0 | -0 [-1, 1] | -0 [-1, 1] | -0 [-1, 1] |
| conservative | 50.0 ms | Slow always | 0 of 49 | 0 | -0 | +0 | -1 [-2, 1] | -1 [-2, 1] | -1 [-2, 1] |
| conservative | 50.0 ms | Cascade | 0 of 49 | 0 | -0 | +0 | 0 [-0, 1] | 0 [-0, 1] | 0 [-0, 1] |

