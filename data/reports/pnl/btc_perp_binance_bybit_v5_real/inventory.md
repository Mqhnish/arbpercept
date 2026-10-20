# Taker strategies with inventory accounted: btc_perp_binance_bybit

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0.

## Fees 2.35 bps per leg (average of the two venues)

24 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 27% | -556 [-964, -241] | -643 [-1,083, -301] | -567 [-961, -263] |
| optimistic | 50.0 ms | Gap size only | 33% | 40 [11, 78] | 35 [8, 72] | 34 [8, 69] |
| optimistic | 50.0 ms | Prior only | 37% | 67 [22, 127] | 62 [17, 122] | 61 [17, 122] |
| optimistic | 50.0 ms | Slow always | 44% | 86 [33, 156] | 74 [23, 144] | 73 [23, 141] |
| optimistic | 50.0 ms | Cascade | 38% | 82 [31, 149] | 71 [20, 138] | 69 [20, 135] |
| conservative | 50.0 ms | Naive | 4% | -726 [-1,245, -326] | -740 [-1,263, -337] | -730 [-1,257, -329] |
| conservative | 50.0 ms | Gap size only | 7% | -5 [-11, -0] | -5 [-12, -0] | -5 [-12, -0] |
| conservative | 50.0 ms | Prior only | 8% | -3 [-8, -0] | -4 [-8, -0] | -4 [-8, -0] |
| conservative | 50.0 ms | Slow always | 12% | -1 [-4, 1] | -1 [-4, 1] | -1 [-4, 1] |
| conservative | 50.0 ms | Cascade | 7% | 0 [-1, 1] | -0 [-1, 1] | -0 [-1, 1] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 50.0 ms | Cascade − Naive | +636 [+284, +1,093] |
| optimistic | 50.0 ms | Cascade − Slow always | -4 [-10, +1] |
| optimistic | 50.0 ms | Prior only − Gap size only | +27 [+8, +53] |
| optimistic | 50.0 ms | Cascade − Gap size only | +35 [+10, +66] |
| conservative | 50.0 ms | Cascade − Naive | +730 [+329, +1,256] |
| conservative | 50.0 ms | Cascade − Slow always | +1 [+0, +4] |
| conservative | 50.0 ms | Prior only − Gap size only | +2 [+0, +4] |
| conservative | 50.0 ms | Cascade − Gap size only | +5 [+0, +12] |

