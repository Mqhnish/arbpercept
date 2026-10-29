# Taker strategies with inventory accounted: tick_eth_perp_binance_okx

Mean net P&L per validation day (USD) with day-bootstrap 95% intervals, $10k per trade. Old: each hedged trade credited with the whole gap. Realised: positions tracked, funding paid or received, no new trades in the day's last 60 s while the position is worked down, never taking more than both books show. Capped: no trade that takes the position past $50,000 at the price of that trade. Validation days without a trade count as $0. Optimistic and conservative are two simulation assumptions about the sampled Bybit book between snapshots, not guaranteed bounds on the truth. No funding is charged on the okx leg: its history is not available.

## Fees 1.85 bps per leg (average of the two venues)

60 validation days.

| Fill bound | Latency | Strategy | Trades going one way | Old | Realised, no cap | Realised, capped |
|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 17% | -695 [-906, -509] | -744 [-963, -553] | -730 [-943, -540] |
| optimistic | 50.0 ms | Gap size only | 12% | -0 [-1, 1] | -0 [-1, 0] | -0 [-1, 0] |
| optimistic | 50.0 ms | Prior only | 24% | -0 [-1, 2] | -1 [-2, 1] | -1 [-2, 1] |
| optimistic | 50.0 ms | Slow always | 27% | -1 [-3, 2] | -4 [-7, -1] | -4 [-7, -1] |
| optimistic | 50.0 ms | Cascade | 26% | -2 [-4, -0] | -5 [-8, -2] | -5 [-7, -2] |
| conservative | 50.0 ms | Naive | 17% | -720 [-941, -525] | -761 [-989, -560] | -736 [-953, -544] |
| conservative | 50.0 ms | Gap size only | 15% | 0 [-1, 1] | -0 [-1, 0] | -0 [-1, 0] |
| conservative | 50.0 ms | Prior only | 20% | 0 [-2, 3] | -0 [-2, 2] | -0 [-2, 2] |
| conservative | 50.0 ms | Slow always | 24% | 2 [-1, 4] | 1 [-1, 3] | 1 [-1, 3] |
| conservative | 50.0 ms | Cascade | 26% | 1 [-1, 3] | 0 [-2, 2] | 0 [-2, 2] |

Paired differences, realised and capped (same days resampled for both):

| Fill bound | Latency | Comparison | Difference per day |
|---|---|---|---|
| optimistic | 50.0 ms | Cascade − Naive | +725 [+536, +937] |
| optimistic | 50.0 ms | Cascade − Slow always | -1 [-3, +1] |
| optimistic | 50.0 ms | Prior only − Gap size only | -0 [-2, +1] |
| optimistic | 50.0 ms | Cascade − Gap size only | -4 [-7, -2] |
| conservative | 50.0 ms | Cascade − Naive | +737 [+543, +953] |
| conservative | 50.0 ms | Cascade − Slow always | -1 [-2, +0] |
| conservative | 50.0 ms | Prior only − Gap size only | +0 [-2, +2] |
| conservative | 50.0 ms | Cascade − Gap size only | +0 [-1, +2] |

Closing, capped. Executed: really traded within the displayed size. Assumed: the rest, booked at the last quotes whatever their size. The last columns charge an extra cost on that rest.

| Fill bound | Latency | Strategy | Days with a rest | Rest, mean USD | Executed | Assumed | +5 bps | +10 bps | +25 bps |
|---|---|---|---|---|---|---|---|---|---|
| optimistic | 50.0 ms | Naive | 0 of 60 | 0 | -10 | +0 | -730 [-943, -540] | -730 [-943, -540] | -730 [-943, -540] |
| optimistic | 50.0 ms | Gap size only | 0 of 60 | 0 | -0 | +0 | -0 [-1, 0] | -0 [-1, 0] | -0 [-1, 0] |
| optimistic | 50.0 ms | Prior only | 0 of 60 | 0 | -0 | +0 | -1 [-2, 1] | -1 [-2, 1] | -1 [-2, 1] |
| optimistic | 50.0 ms | Slow always | 0 of 60 | 0 | -3 | +0 | -4 [-7, -1] | -4 [-7, -1] | -4 [-7, -1] |
| optimistic | 50.0 ms | Cascade | 0 of 60 | 0 | -2 | +0 | -5 [-7, -2] | -5 [-7, -2] | -5 [-7, -2] |
| conservative | 50.0 ms | Naive | 0 of 60 | 0 | -10 | +0 | -736 [-953, -544] | -736 [-953, -544] | -736 [-953, -544] |
| conservative | 50.0 ms | Gap size only | 0 of 60 | 0 | -0 | +0 | -0 [-1, 0] | -0 [-1, 0] | -0 [-1, 0] |
| conservative | 50.0 ms | Prior only | 0 of 60 | 0 | -0 | +0 | -0 [-2, 2] | -0 [-2, 2] | -0 [-2, 2] |
| conservative | 50.0 ms | Slow always | 0 of 60 | 0 | -1 | +0 | 1 [-1, 3] | 1 [-1, 3] | 1 [-1, 3] |
| conservative | 50.0 ms | Cascade | 0 of 60 | 0 | -1 | +0 | 0 [-2, 2] | 0 [-2, 2] | 0 [-2, 2] |

