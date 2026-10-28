# Taker strategies with inventory accounted: doge_perp_binance_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0. Optimistic and conservative are two simulation assumptions about the sampled Bybit book between snapshots, not guaranteed bounds on the truth.

## Fees 2.35 bps per leg (average of the two venues)

73 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 22% | -501 [-676, -357] | -548 [-727, -398] | -504 [-667, -366] |
| optimistic | 50.0 ms | Gap size only | 25% | -1 [-9, 5] | -2 [-12, 5] | -2 [-12, 5] |
| optimistic | 50.0 ms | Prior only | 38% | 8 [4, 12] | 4 [1, 8] | 4 [1, 8] |
| optimistic | 50.0 ms | Slow always | 42% | 5 [-0, 10] | -1 [-6, 5] | -1 [-6, 4] |
| optimistic | 50.0 ms | Cascade | 37% | 5 [-1, 10] | -2 [-7, 4] | -0 [-6, 5] |
| conservative | 50.0 ms | Naive | 5% | -463 [-617, -333] | -477 [-634, -346] | -465 [-614, -340] |
| conservative | 50.0 ms | Gap size only | 5% | -2 [-3, -1] | -2 [-3, -1] | -2 [-3, -1] |
| conservative | 50.0 ms | Prior only | 15% | 0 [-1, 1] | 0 [-1, 1] | 0 [-1, 1] |
| conservative | 50.0 ms | Slow always | 14% | -0 [-0, 1] | -0 [-0, 0] | -0 [-0, 0] |
| conservative | 50.0 ms | Cascade | 17% | 0 [-0, 1] | 0 [-0, 1] | 0 [-0, 1] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 50.0 ms | Cascade − Naive | +503 [+364, +668] |
| optimistic | 50.0 ms | Cascade − Slow always | +0 [-3, +3] |
| optimistic | 50.0 ms | Prior only − Gap size only | +7 [-1, +17] |
| optimistic | 50.0 ms | Cascade − Gap size only | +2 [-5, +12] |
| conservative | 50.0 ms | Cascade − Naive | +466 [+340, +615] |
| conservative | 50.0 ms | Cascade − Slow always | +0 [-0, +1] |
| conservative | 50.0 ms | Prior only − Gap size only | +2 [+1, +3] |
| conservative | 50.0 ms | Cascade − Gap size only | +2 [+1, +3] |

Closing, capped. Executed: really traded within the displayed size. Assumed: the rest, booked at the last quotes whatever their size. The last columns charge an extra cost on that rest.

| Fill bound | Latency | Strategy | Days with a rest | Rest, mean USD | Executed | Assumed | +5 bps | +10 bps | +25 bps |
|---|---|---|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 4 of 73 | 623 | -16 | -0 | -504 [-668, -366] | -504 [-668, -367] | -505 [-669, -368] |
| optimistic | 50.0 ms | Gap size only | 1 of 73 | 122 | -1 | -0 | -2 [-12, 5] | -2 [-12, 4] | -2 [-12, 4] |
| optimistic | 50.0 ms | Prior only | 2 of 73 | 275 | -3 | -0 | 4 [1, 8] | 4 [1, 8] | 4 [0, 7] |
| optimistic | 50.0 ms | Slow always | 2 of 73 | 285 | -5 | -0 | -1 [-6, 4] | -1 [-6, 4] | -1 [-7, 4] |
| optimistic | 50.0 ms | Cascade | 2 of 73 | 641 | -5 | -0 | -1 [-6, 4] | -1 [-6, 4] | -2 [-8, 4] |
| conservative | 50.0 ms | Naive | 4 of 73 | 660 | -12 | -0 | -466 [-615, -340] | -466 [-615, -340] | -467 [-616, -341] |
| conservative | 50.0 ms | Gap size only | 0 of 73 | 0 | -0 | +0 | -2 [-3, -1] | -2 [-3, -1] | -2 [-3, -1] |
| conservative | 50.0 ms | Prior only | 0 of 73 | 0 | -0 | +0 | 0 [-1, 1] | 0 [-1, 1] | 0 [-1, 1] |
| conservative | 50.0 ms | Slow always | 0 of 73 | 0 | -0 | +0 | -0 [-0, 0] | -0 [-0, 0] | -0 [-0, 0] |
| conservative | 50.0 ms | Cascade | 0 of 73 | 0 | -0 | +0 | 0 [-0, 1] | 0 [-0, 1] | 0 [-0, 1] |

Against the earlier run `_v7_real`, realised and capped:

| Fill bound | Latency | Strategy | This run − earlier run |
|---|---|---|---|
| optimistic | 50.0 ms | Naive | -86 [-116, -61] |
| optimistic | 50.0 ms | Gap size only | -5 [-13, +0] |
| optimistic | 50.0 ms | Prior only | +0 [-2, +2] |
| optimistic | 50.0 ms | Slow always | -1 [-4, +2] |
| optimistic | 50.0 ms | Cascade | +2 [-2, +6] |
| conservative | 50.0 ms | Naive | -55 [-70, -41] |
| conservative | 50.0 ms | Gap size only | +0 [-1, +1] |
| conservative | 50.0 ms | Prior only | +0 [-0, +1] |
| conservative | 50.0 ms | Slow always | +1 [+0, +2] |
| conservative | 50.0 ms | Cascade | +1 [+1, +2] |

