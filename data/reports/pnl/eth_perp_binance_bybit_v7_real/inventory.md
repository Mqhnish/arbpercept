# Taker strategies with inventory accounted: eth_perp_binance_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0.

## Fees 2.35 bps per leg (average of the two venues)

180 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 24% | -173 [-262, -110] | -203 [-298, -135] | -173 [-242, -122] |
| optimistic | 50.0 ms | Gap size only | 30% | 8 [5, 11] | 6 [3, 9] | 6 [3, 9] |
| optimistic | 50.0 ms | Prior only | 39% | 16 [12, 21] | 13 [9, 17] | 13 [9, 17] |
| optimistic | 50.0 ms | Slow always | 49% | 23 [18, 28] | 15 [11, 21] | 15 [11, 20] |
| optimistic | 50.0 ms | Cascade | 44% | 21 [16, 27] | 14 [9, 19] | 14 [9, 19] |
| conservative | 50.0 ms | Naive | 7% | -232 [-316, -169] | -244 [-332, -179] | -229 [-300, -173] |
| conservative | 50.0 ms | Gap size only | 6% | 0 [-0, 1] | 0 [-0, 1] | 0 [-0, 1] |
| conservative | 50.0 ms | Prior only | 2% | -0 [-1, 0] | -0 [-1, 0] | -0 [-1, 0] |
| conservative | 50.0 ms | Slow always | 27% | -0 [-1, 1] | -0 [-1, 1] | -0 [-1, 1] |
| conservative | 50.0 ms | Cascade | 21% | -0 [-1, 1] | -0 [-1, 1] | -0 [-1, 1] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 50.0 ms | Cascade − Naive | +187 [+133, +259] |
| optimistic | 50.0 ms | Cascade − Slow always | -1 [-2, -0] |
| optimistic | 50.0 ms | Prior only − Gap size only | +7 [+4, +9] |
| optimistic | 50.0 ms | Cascade − Gap size only | +8 [+5, +11] |
| conservative | 50.0 ms | Cascade − Naive | +228 [+173, +299] |
| conservative | 50.0 ms | Cascade − Slow always | -0 [-1, +1] |
| conservative | 50.0 ms | Prior only − Gap size only | -1 [-2, +0] |
| conservative | 50.0 ms | Cascade − Gap size only | -1 [-1, -0] |

