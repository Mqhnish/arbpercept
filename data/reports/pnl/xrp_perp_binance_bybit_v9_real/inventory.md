# Taker strategies with inventory accounted: xrp_perp_binance_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0. Optimistic and conservative are two simulation assumptions about the sampled Bybit book between snapshots, not guaranteed bounds on the truth.

## Fees 2.35 bps per leg (average of the two venues)

73 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 22% | -531 [-693, -391] | -615 [-792, -460] | -525 [-679, -395] |
| optimistic | 50.0 ms | Gap size only | 29% | -10 [-30, 1] | -14 [-36, 0] | -12 [-34, 1] |
| optimistic | 50.0 ms | Prior only | 27% | 8 [1, 17] | 1 [-5, 9] | 2 [-4, 10] |
| optimistic | 50.0 ms | Slow always | 32% | 6 [-0, 13] | -4 [-10, 3] | -2 [-7, 5] |
| optimistic | 50.0 ms | Cascade | 30% | 11 [3, 20] | 5 [-2, 14] | 5 [-2, 14] |
| conservative | 50.0 ms | Naive | 6% | -569 [-749, -417] | -595 [-782, -436] | -551 [-717, -409] |
| conservative | 50.0 ms | Gap size only | 0% | -0 [-1, -0] | -0 [-1, -0] | -0 [-1, -0] |
| conservative | 50.0 ms | Prior only | 10% | -1 [-2, -0] | -1 [-2, -0] | -1 [-2, -0] |
| conservative | 50.0 ms | Slow always | 12% | -1 [-2, -0] | -1 [-2, -0] | -1 [-2, -0] |
| conservative | 50.0 ms | Cascade | 20% | -1 [-1, -0] | -1 [-1, -0] | -1 [-1, -0] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 50.0 ms | Cascade − Naive | +531 [+395, +690] |
| optimistic | 50.0 ms | Cascade − Slow always | +7 [+2, +12] |
| optimistic | 50.0 ms | Prior only − Gap size only | +15 [-2, +38] |
| optimistic | 50.0 ms | Cascade − Gap size only | +18 [+1, +40] |
| conservative | 50.0 ms | Cascade − Naive | +551 [+409, +716] |
| conservative | 50.0 ms | Cascade − Slow always | +0 [-1, +2] |
| conservative | 50.0 ms | Prior only − Gap size only | -1 [-1, +0] |
| conservative | 50.0 ms | Cascade − Gap size only | -0 [-1, +0] |

Closing, capped. Executed: really traded within the displayed size. Assumed: the rest, booked at the last quotes whatever their size. The last columns charge an extra cost on that rest.

| Fill bound | Latency | Strategy | Days with a rest | Rest, mean USD | Executed | Assumed | +5 bps | +10 bps | +25 bps |
|---|---|---|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 3 of 73 | 919 | -18 | -0 | -526 [-680, -395] | -526 [-680, -396] | -528 [-681, -397] |
| optimistic | 50.0 ms | Gap size only | 1 of 73 | 237 | -2 | -0 | -12 [-34, 1] | -12 [-34, 1] | -13 [-35, 1] |
| optimistic | 50.0 ms | Prior only | 2 of 73 | 149 | -5 | -0 | 2 [-4, 10] | 2 [-4, 10] | 2 [-5, 10] |
| optimistic | 50.0 ms | Slow always | 3 of 73 | 837 | -6 | -1 | -2 [-8, 5] | -2 [-8, 5] | -4 [-11, 4] |
| optimistic | 50.0 ms | Cascade | 3 of 73 | 526 | -5 | -0 | 5 [-2, 14] | 5 [-2, 14] | 4 [-3, 13] |
| conservative | 50.0 ms | Naive | 0 of 73 | 0 | -11 | +0 | -551 [-717, -409] | -551 [-717, -409] | -551 [-717, -409] |
| conservative | 50.0 ms | Gap size only | 0 of 73 | 0 | +0 | +0 | -0 [-1, -0] | -0 [-1, -0] | -0 [-1, -0] |
| conservative | 50.0 ms | Prior only | 0 of 73 | 0 | -0 | +0 | -1 [-2, -0] | -1 [-2, -0] | -1 [-2, -0] |
| conservative | 50.0 ms | Slow always | 0 of 73 | 0 | -0 | +0 | -1 [-2, -0] | -1 [-2, -0] | -1 [-2, -0] |
| conservative | 50.0 ms | Cascade | 0 of 73 | 0 | -0 | +0 | -1 [-1, -0] | -1 [-1, -0] | -1 [-1, -0] |

Against the earlier run `_v7_real`, realised and capped:

| Fill bound | Latency | Strategy | This run − earlier run |
|---|---|---|---|
| optimistic | 50.0 ms | Naive | -109 [-144, -79] |
| optimistic | 50.0 ms | Gap size only | -5 [-11, -0] |
| optimistic | 50.0 ms | Prior only | -4 [-10, +1] |
| optimistic | 50.0 ms | Slow always | -5 [-10, +0] |
| optimistic | 50.0 ms | Cascade | -2 [-6, +1] |
| conservative | 50.0 ms | Naive | -82 [-107, -59] |
| conservative | 50.0 ms | Gap size only | +1 [+0, +1] |
| conservative | 50.0 ms | Prior only | +2 [+1, +3] |
| conservative | 50.0 ms | Slow always | -0 [-2, +1] |
| conservative | 50.0 ms | Cascade | +0 [-1, +1] |

