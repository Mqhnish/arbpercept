# Live cross-venue decay, ETH perpetual, Binance vs Bybit, 2026-10-19

0.96 h after warm-up, one receive clock.

| Venue | Quote changes | Feed latency to us, median / p99 (ms) |
|---|---|---|
| binance | 8,937 | 45 / 208 |
| bybit | 158,674 | 9 / 35 |

| Hurdle | Births per hour | Open after 10 ms | Open after 50 ms | Open after 100 ms | Open after 200 ms | Open after 500 ms | Median life (ms) |
|---|---|---|---|---|---|---|---|
| gross>1bps | 177 | 65% | 48% | 35% | 26% | 16% | 43 |
| gross>2bps | 3 | 67% | 0% | 0% | 0% | 0% | 11 |
| gross>5bps | 0 | - | - | - | - | - | - |
| gross>10bps | 0 | - | - | - | - | - | - |
