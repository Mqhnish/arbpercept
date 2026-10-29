# Tardis first-of-month days: nine cross-venue pairs

Tardis.dev's free days (the 1st of each month), January 2020 to October 2026, BTC, ETH and SOL perpetuals on Binance, OKX and Bybit. Every top-of-book change on all three venues, stamped by one Tardis collector. February and March 2024 (the frozen cross-venue test) were never downloaded. Walk-forward validation days only.

Realised P&L per validation day (USD), positions capped at $50k, funding charged, the position worked down over each day's last 60 s. Day-bootstrap 95% intervals. Full reports: `tick_<coin>_perp_<venues>_tardis_real/inventory.md`.

Setup: `--deplete-liquidity --slow-wait-ms 0.03 --offset-aware`, plus per venue:

| Venue | Taker fee | Order latency | Feed delay | Source |
|---|---|---|---|---|
| Binance | 1.7 bps | 50 ms | 0 ms | measured from our machine (as in v9) |
| Bybit | 3.0 bps | 8 ms | 45 ms | measured from our machine (as in v9) |
| OKX | 2.0 bps | 35 ms | 0 ms | **assumed**, not measured |

Caveats:
- The latencies are applied on Tardis's collector clock, not ours, so they are assumptions about a trader placed like us, not measurements on this data.
- OKX funding is not charged: OKX's API keeps only the last 3 months.
- Tardis records every Bybit top-of-book change, unlike the 100 ms Bybit archive behind the v9 runs, so the optimistic and conservative fills are much closer here.

| Pair | Validation days | Cascade, optimistic | Cascade, conservative | Gap-size rule, optimistic | Naive, optimistic | Cascade − gap-size, optimistic | Cascade − gap-size, conservative |
|---|---|---|---|---|---|---|---|
| BTC Binance–Bybit | 56 | 11 [2, 20] | 10 [2, 18] | 3 [-1, 9] | -406 [-659, -206] | +7 [+1, +15] | +7 [+1, +14] |
| BTC Binance–OKX | 60 | -5 [-13, 1] | 1 [-1, 4] | 1 [-1, 4] | -427 [-588, -299] | -6 [-13, -1] | -0 [-1, +1] |
| BTC OKX–Bybit | 55 | -4 [-8, -0] | -1 [-3, 2] | -0 [-1, 0] | -311 [-457, -189] | -4 [-7, -0] | -1 [-3, +1] |
| ETH Binance–Bybit | 55 | 25 [14, 38] | 12 [5, 20] | 16 [8, 27] | -411 [-620, -244] | +8 [+3, +14] | -1 [-6, +3] |
| ETH Binance–OKX | 60 | -5 [-7, -2] | 0 [-2, 2] | -0 [-1, 0] | -730 [-943, -540] | -4 [-7, -2] | +0 [-1, +2] |
| ETH OKX–Bybit | 54 | -2 [-4, -0] | 1 [-2, 6] | no trades | -423 [-587, -281] | n/a | n/a |
| SOL Binance–Bybit | 49 | 20 [8, 34] | 10 [2, 19] | 20 [11, 31] | -376 [-543, -245] | +0 [-7, +8] | -0 [-4, +5] |
| SOL Binance–OKX | 49 | -4 [-8, -1] | 0 [-0, 1] | -0 [-0, -0] | -642 [-864, -461] | -4 [-8, -1] | +0 [-0, +1] |
| SOL OKX–Bybit | 48 | -5 [-13, -0] | -2 [-5, 1] | -0 [-2, 1] | -390 [-546, -260] | -5 [-12, -0] | -2 [-4, +0] |
