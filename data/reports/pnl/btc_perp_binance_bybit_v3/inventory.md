# Taker strategies with inventory accounted: btc_perp_binance_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, the remainder closed with taker orders at the day's end. Capped: no trade that takes the position past $50,000.

## Fees 1 bps per leg

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 1 ms | Naive | 78% | 2,377 [1,617, 3,304] | -9,397 [-14,594, -4,825] | 125 [20, 262] |
| optimistic | 1 ms | Prior only | 79% | 2,398 [1,631, 3,339] | -7,060 [-11,160, -3,491] | 191 [70, 345] |
| optimistic | 1 ms | Slow always | 80% | 2,431 [1,656, 3,379] | -7,793 [-12,292, -3,862] | 216 [88, 380] |
| optimistic | 1 ms | Cascade | 80% | 2,424 [1,655, 3,368] | -8,061 [-12,723, -4,004] | 196 [79, 346] |
| optimistic | 10 ms | Naive | 71% | 392 [157, 597] | -9,972 [-15,016, -5,556] | -1,315 [-1,862, -856] |
| optimistic | 10 ms | Prior only | 74% | 918 [650, 1,244] | -3,053 [-4,846, -1,510] | -314 [-435, -211] |
| optimistic | 10 ms | Slow always | 79% | 1,145 [817, 1,544] | -4,067 [-6,520, -1,963] | -152 [-215, -96] |
| optimistic | 10 ms | Cascade | 79% | 1,145 [817, 1,544] | -4,067 [-6,520, -1,963] | -152 [-215, -96] |
| optimistic | 50 ms | Naive | 54% | -2,507 [-3,477, -1,692] | -10,523 [-15,055, -6,564] | -4,009 [-5,410, -2,822] |
| optimistic | 50 ms | Prior only | 59% | 102 [43, 177] | -770 [-1,194, -414] | -290 [-391, -201] |
| optimistic | 50 ms | Slow always | 77% | 355 [252, 484] | -1,522 [-2,497, -711] | -153 [-225, -91] |
| optimistic | 50 ms | Cascade | 77% | 355 [252, 484] | -1,521 [-2,494, -710] | -153 [-224, -91] |
| conservative | 1 ms | Naive | 49% | -5,497 [-7,171, -4,036] | -12,951 [-17,867, -8,625] | -6,317 [-8,253, -4,637] |
| conservative | 1 ms | Prior only | 75% | 147 [82, 214] | -1,877 [-3,017, -924] | -376 [-568, -223] |
| conservative | 1 ms | Slow always | 85% | 388 [281, 509] | -2,457 [-3,869, -1,247] | -233 [-378, -125] |
| conservative | 1 ms | Cascade | 85% | 389 [282, 510] | -2,455 [-3,867, -1,244] | -232 [-377, -124] |
| conservative | 10 ms | Naive | 43% | -6,133 [-8,006, -4,503] | -12,588 [-17,178, -8,551] | -6,626 [-8,630, -4,893] |
| conservative | 10 ms | Prior only | 73% | 62 [34, 91] | -1,066 [-1,720, -518] | -221 [-318, -139] |
| conservative | 10 ms | Slow always | 83% | 221 [158, 291] | -1,729 [-2,715, -888] | -186 [-264, -122] |
| conservative | 10 ms | Cascade | 83% | 221 [157, 292] | -1,725 [-2,709, -886] | -185 [-261, -122] |
| conservative | 50 ms | Naive | 32% | -7,737 [-10,092, -5,699] | -12,677 [-16,928, -8,906] | -8,034 [-10,488, -5,920] |
| conservative | 50 ms | Prior only | 63% | -20 [-28, -12] | -202 [-317, -108] | -70 [-92, -51] |
| conservative | 50 ms | Slow always | 80% | 46 [29, 66] | -668 [-1,032, -356] | -116 [-157, -79] |
| conservative | 50 ms | Cascade | 80% | 48 [29, 71] | -659 [-1,016, -352] | -113 [-151, -78] |

