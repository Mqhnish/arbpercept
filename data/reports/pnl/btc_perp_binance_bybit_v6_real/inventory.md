# Taker strategies with inventory accounted: btc_perp_binance_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0.

## Fees 2.35 bps per leg (average of the two venues)

24 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 25% | -310 [-530, -140] | -380 [-623, -189] | -346 [-576, -167] |
| optimistic | 50.0 ms | Gap size only | 36% | 13 [4, 26] | 9 [1, 20] | 9 [1, 20] |
| optimistic | 50.0 ms | Prior only | 37% | 67 [26, 120] | 58 [18, 111] | 58 [18, 110] |
| optimistic | 50.0 ms | Slow always | 41% | 74 [31, 136] | 58 [17, 119] | 57 [17, 116] |
| optimistic | 50.0 ms | Cascade | 41% | 73 [30, 135] | 58 [16, 118] | 57 [17, 116] |
| conservative | 50.0 ms | Naive | 3% | -558 [-940, -262] | -569 [-954, -270] | -561 [-945, -265] |
| conservative | 50.0 ms | Gap size only | 7% | -3 [-7, -0] | -3 [-7, -0] | -3 [-7, -0] |
| conservative | 50.0 ms | Prior only | 9% | -3 [-7, -0] | -3 [-7, -0] | -3 [-7, -0] |
| conservative | 50.0 ms | Slow always | 23% | 0 [-4, 5] | -0 [-5, 5] | -0 [-5, 5] |
| conservative | 50.0 ms | Cascade | 21% | -0 [-5, 4] | -1 [-5, 4] | -1 [-5, 4] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 50.0 ms | Cascade − Naive | +402 [+185, +681] |
| optimistic | 50.0 ms | Cascade − Slow always | -1 [-2, +0] |
| optimistic | 50.0 ms | Prior only − Gap size only | +48 [+15, +92] |
| optimistic | 50.0 ms | Cascade − Gap size only | +48 [+14, +96] |
| conservative | 50.0 ms | Cascade − Naive | +560 [+264, +946] |
| conservative | 50.0 ms | Cascade − Slow always | -1 [-2, +0] |
| conservative | 50.0 ms | Prior only − Gap size only | +0 [-1, +2] |
| conservative | 50.0 ms | Cascade − Gap size only | +3 [-0, +8] |

Against the earlier run `_v5_real`, realised and capped:

| Fill bound | Latency | Strategy | This run − earlier run |
|---|---|---|---|
| optimistic | 50.0 ms | Naive | +222 [+95, +394] |
| optimistic | 50.0 ms | Gap size only | -25 [-51, -5] |
| optimistic | 50.0 ms | Prior only | -4 [-13, +4] |
| optimistic | 50.0 ms | Slow always | -16 [-33, -4] |
| optimistic | 50.0 ms | Cascade | -12 [-32, +1] |
| conservative | 50.0 ms | Naive | +169 [+62, +312] |
| conservative | 50.0 ms | Gap size only | +2 [-0, +5] |
| conservative | 50.0 ms | Prior only | +0 [-1, +2] |
| conservative | 50.0 ms | Slow always | +1 [-3, +5] |
| conservative | 50.0 ms | Cascade | -1 [-4, +3] |

