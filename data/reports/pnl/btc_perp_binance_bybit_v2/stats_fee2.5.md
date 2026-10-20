# P&L uncertainty and regimes: btc_perp_binance_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals. Fees 2.5 bps per leg, $10k per trade.

## Optimistic fill bound

| Latency | Days | Naive | Prior only | Slow always | Cascade | Cascade − Naive | Cascade − Slow always |
|---|---|---|---|---|---|---|---|
| 1 ms | 24 | 366 [138, 657] | 425 [163, 764] | 436 [169, 784] | 437 [169, 785] | +71 [+27, +131] | +0 [-0, +1] |
| 10 ms | 24 | -632 [-1,120, -264] | 119 [45, 215] | 178 [71, 318] | 172 [70, 308] | +805 [+339, +1,425] | -6 [-11, -2] |
| 50 ms | 24 | -1,707 [-2,951, -730] | 5 [-8, 23] | 59 [25, 109] | 58 [25, 107] | +1,764 [+759, +3,053] | -1 [-3, +0] |
| 100 ms | 24 | -2,384 [-4,135, -994] | -2 [-4, -1] | 5 [0, 10] | 4 [0, 9] | +2,389 [+995, +4,142] | -1 [-2, +0] |

## Conservative fill bound

| Latency | Days | Naive | Prior only | Slow always | Cascade | Cascade − Naive | Cascade − Slow always |
|---|---|---|---|---|---|---|---|
| 0 ms | 24 | -2,538 [-4,329, -1,156] | 92 [24, 174] | 10 [-10, 37] | 90 [23, 170] | +2,628 [+1,192, +4,486] | +81 [+29, +148] |
| 1 ms | 24 | -2,868 [-4,915, -1,287] | -26 [-51, -6] | 7 [-7, 27] | 7 [-7, 27] | +2,875 [+1,286, +4,931] | +0 [-2, +2] |
| 10 ms | 24 | -2,763 [-4,758, -1,206] | -8 [-18, -1] | 1 [-3, 6] | -0 [-5, 5] | +2,762 [+1,206, +4,760] | -2 [-4, +1] |
| 50 ms | 24 | -2,800 [-4,863, -1,164] | -2 [-3, -0] | -2 [-5, -0] | -3 [-7, -1] | +2,796 [+1,161, +4,859] | -1 [-2, +0] |
| 100 ms | 24 | -2,738 [-4,764, -1,120] | -1 [-2, -0] | 1 [-1, 3] | -1 [-2, 0] | +2,737 [+1,120, +4,763] | -1 [-3, +0] |

## By volatility regime at 10 ms latency

| Fill bound | Regime | Days | Naive | Prior only | Slow always | Cascade |
|---|---|---|---|---|---|---|
| conservative | calm | 8 | -206 | -1 | -1 | -0 |
| conservative | normal | 8 | -1,206 | -1 | -1 | 0 |
| conservative | volatile | 8 | -6,877 | -23 | 5 | -1 |
| optimistic | calm | 8 | -21 | 17 | 21 | 21 |
| optimistic | normal | 8 | -284 | 35 | 54 | 53 |
| optimistic | volatile | 8 | -1,592 | 306 | 459 | 443 |
