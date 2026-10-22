# Taker strategies with inventory accounted: sol_perp_binance_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0.

## Fees 2.35 bps per leg (average of the two venues)

68 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 26% | -765 [-934, -614] | -806 [-985, -648] | -759 [-919, -614] |
| optimistic | 50.0 ms | Gap size only | 26% | 18 [10, 27] | 15 [8, 24] | 15 [8, 24] |
| optimistic | 50.0 ms | Prior only | 30% | 23 [12, 38] | 19 [10, 32] | 19 [10, 32] |
| optimistic | 50.0 ms | Slow always | 39% | 30 [19, 45] | 26 [15, 40] | 26 [15, 40] |
| optimistic | 50.0 ms | Cascade | 40% | 30 [19, 44] | 26 [15, 39] | 26 [15, 39] |
| conservative | 50.0 ms | Naive | 4% | -700 [-859, -559] | -719 [-882, -575] | -698 [-849, -563] |
| conservative | 50.0 ms | Gap size only | 12% | -1 [-1, 0] | -1 [-1, 0] | -1 [-1, 0] |
| conservative | 50.0 ms | Prior only | 9% | -1 [-2, 0] | -1 [-2, -0] | -1 [-2, -0] |
| conservative | 50.0 ms | Slow always | 26% | 1 [-1, 2] | 0 [-1, 2] | 0 [-1, 2] |
| conservative | 50.0 ms | Cascade | 26% | 0 [-1, 1] | -0 [-1, 1] | -0 [-1, 1] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 50.0 ms | Cascade − Naive | +785 [+636, +950] |
| optimistic | 50.0 ms | Cascade − Slow always | -0 [-0, +0] |
| optimistic | 50.0 ms | Prior only − Gap size only | +4 [-1, +10] |
| optimistic | 50.0 ms | Cascade − Gap size only | +11 [+6, +18] |
| conservative | 50.0 ms | Cascade − Naive | +698 [+563, +848] |
| conservative | 50.0 ms | Cascade − Slow always | -0 [-1, +1] |
| conservative | 50.0 ms | Prior only − Gap size only | -0 [-1, +0] |
| conservative | 50.0 ms | Cascade − Gap size only | +0 [-1, +2] |

