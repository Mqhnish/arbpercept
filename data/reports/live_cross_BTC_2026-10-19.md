# Live cross-venue decay, BTC perpetual, Binance vs Bybit, 2026-10-19

0.96 h after warm-up, one receive clock.

| Venue | Quote changes | Feed latency to us, median / p99 (ms) |
|---|---|---|
| binance | 6,439 | 50 / 287 |
| bybit | 102,414 | 8 / 38 |

| Hurdle | Births per hour | Open after 10 ms | Open after 50 ms | Open after 100 ms | Open after 200 ms | Open after 500 ms | Median life (ms) |
|---|---|---|---|---|---|---|---|
| gross>1bps | 244 | 84% | 65% | 54% | 50% | 41% | 168 |
| gross>2bps | 4 | 75% | 0% | 0% | 0% | 0% | 15 |
| gross>5bps | 0 | - | - | - | - | - | - |
| gross>10bps | 0 | - | - | - | - | - | - |
