# Dataset report

## Stream quality

Trade check: Bybit's independent trade record against the reconstructed book. In band = share of trades printing between the bracketing snapshots' quotes; sweeps beyond the band are normal on volatile days. A day fails on persistence (5+ consecutive minutes where most trades miss the book) or a clock offset over 20 ms.

| Date | Stream | Rows | Coverage | Longest raw silence (s) | Resyncs | Feed lag p50/p99 (ms) | Spread p50 (bps) | Daily RV (bps) | Trades in band | Longest anomaly (min) | Clock offset (ms) | Passes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2023-05-16 | binance_bt/binance/BTC-USDT/perp | 80,334 | 0.413 | 42587.2 | 0 | 5.0 / 13.0 | 0.04 | 119 | no trade record | - | - | NO |
| 2023-05-16 | binance_bt/binance/ETH-USDT/perp | 61,753 | 0.413 | 42587.2 | 0 | 5.0 / 15.0 | 0.06 | 120 | no trade record | - | - | NO |
| 2023-05-16 | bybit_ob/bybit/BTC-USDT/perp | 856,131 | 1.000 | 1.5 | 0 | 0.0 / 0.0 | 0.04 | 171 | 96.4% | 0 | 0 | yes |
| 2023-05-16 | bybit_ob/bybit/ETH-USDT/perp | 835,677 | 1.000 | 1.0 | 0 | 0.0 / 0.0 | 0.06 | 165 | 96.3% | 1 | 0 | yes |
| 2023-05-17 | binance_bt/binance/BTC-USDT/perp | 140,506 | 0.627 | 31582.7 | 0 | 5.0 / 21.0 | 0.04 | 180 | no trade record | - | - | NO |
| 2023-05-17 | binance_bt/binance/ETH-USDT/perp | 120,400 | 0.627 | 31582.7 | 0 | 5.0 / 21.0 | 0.06 | 158 | no trade record | - | - | NO |
| 2023-05-17 | bybit_ob/bybit/BTC-USDT/perp | 857,394 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 198 | 93.1% | 1 | 0 | yes |
| 2023-05-17 | bybit_ob/bybit/ETH-USDT/perp | 838,142 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 186 | 95.1% | 1 | 0 | yes |
| 2023-05-18 | binance_bt/binance/BTC-USDT/perp | 220,524 | 1.000 | 2.8 | 0 | 5.0 / 26.0 | 0.04 | 223 | no trade record | - | - | yes |
| 2023-05-18 | binance_bt/binance/ETH-USDT/perp | 146,320 | 1.000 | 3.1 | 0 | 5.0 / 23.0 | 0.06 | 195 | no trade record | - | - | yes |
| 2023-05-18 | bybit_ob/bybit/BTC-USDT/perp | 856,530 | 1.000 | 1.5 | 0 | 0.0 / 0.0 | 0.04 | 218 | 93.4% | 0 | 0 | yes |
| 2023-05-18 | bybit_ob/bybit/ETH-USDT/perp | 836,323 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 193 | 94.0% | 1 | 0 | yes |
| 2023-05-19 | binance_bt/binance/BTC-USDT/perp | 136,803 | 1.000 | 3.0 | 0 | 5.0 / 16.0 | 0.04 | 179 | no trade record | - | - | yes |
| 2023-05-19 | binance_bt/binance/ETH-USDT/perp | 115,024 | 1.000 | 2.3 | 0 | 5.0 / 14.0 | 0.06 | 172 | no trade record | - | - | yes |
| 2023-05-19 | bybit_ob/bybit/BTC-USDT/perp | 853,140 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 176 | 94.7% | 0 | 0 | yes |
| 2023-05-19 | bybit_ob/bybit/ETH-USDT/perp | 828,122 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 168 | 96.6% | 1 | 0 | yes |
| 2023-05-20 | binance_bt/binance/BTC-USDT/perp | 43,059 | 1.000 | 3.0 | 0 | 5.0 / 15.0 | 0.04 | 94 | no trade record | - | - | yes |
| 2023-05-20 | binance_bt/binance/ETH-USDT/perp | 43,314 | 1.000 | 3.8 | 0 | 5.0 / 13.0 | 0.06 | 99 | no trade record | - | - | yes |
| 2023-05-20 | bybit_ob/bybit/BTC-USDT/perp | 847,721 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 89 | 97.7% | 1 | 0 | yes |
| 2023-05-20 | bybit_ob/bybit/ETH-USDT/perp | 812,964 | 1.000 | 1.0 | 0 | 0.0 / 0.0 | 0.06 | 95 | 96.6% | 0 | 0 | yes |
| 2023-05-21 | binance_bt/binance/BTC-USDT/perp | 72,277 | 1.000 | 3.1 | 0 | 5.0 / 19.0 | 0.04 | 136 | no trade record | - | - | yes |
| 2023-05-21 | binance_bt/binance/ETH-USDT/perp | 60,853 | 1.000 | 3.6 | 0 | 5.0 / 15.0 | 0.06 | 117 | no trade record | - | - | yes |
| 2023-05-21 | bybit_ob/bybit/BTC-USDT/perp | 852,685 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 130 | 93.0% | 0 | 0 | yes |
| 2023-05-21 | bybit_ob/bybit/ETH-USDT/perp | 821,339 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 114 | 96.9% | 0 | 0 | yes |
| 2023-05-22 | binance_bt/binance/BTC-USDT/perp | 107,894 | 1.000 | 4.3 | 0 | 5.0 / 17.0 | 0.04 | 157 | no trade record | - | - | yes |
| 2023-05-22 | binance_bt/binance/ETH-USDT/perp | 95,166 | 1.000 | 7.0 | 0 | 5.0 / 14.0 | 0.06 | 141 | no trade record | - | - | yes |
| 2023-05-22 | bybit_ob/bybit/BTC-USDT/perp | 855,553 | 1.000 | 1.5 | 0 | 0.0 / 0.0 | 0.04 | 154 | 94.8% | 0 | 0 | yes |
| 2023-05-22 | bybit_ob/bybit/ETH-USDT/perp | 830,500 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 141 | 94.0% | 1 | 0 | yes |
| 2023-05-23 | binance_bt/binance/BTC-USDT/perp | 136,180 | 1.000 | 2.1 | 0 | 5.0 / 25.0 | 0.04 | 157 | no trade record | - | - | yes |
| 2023-05-23 | binance_bt/binance/ETH-USDT/perp | 133,597 | 1.000 | 4.2 | 0 | 5.0 / 22.0 | 0.05 | 195 | no trade record | - | - | yes |
| 2023-05-23 | bybit_ob/bybit/BTC-USDT/perp | 856,809 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 153 | 94.0% | 0 | 0 | yes |
| 2023-05-23 | bybit_ob/bybit/ETH-USDT/perp | 838,245 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 194 | 92.6% | 1 | 0 | yes |
| 2023-05-24 | binance_bt/binance/BTC-USDT/perp | 217,499 | 1.000 | 3.6 | 0 | 5.0 / 36.0 | 0.04 | 203 | no trade record | - | - | yes |
| 2023-05-24 | binance_bt/binance/ETH-USDT/perp | 176,817 | 1.000 | 2.0 | 0 | 5.0 / 26.0 | 0.06 | 199 | no trade record | - | - | yes |
| 2023-05-24 | bybit_ob/bybit/BTC-USDT/perp | 858,516 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 202 | 92.8% | 1 | 0 | yes |
| 2023-05-24 | bybit_ob/bybit/ETH-USDT/perp | 842,077 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 197 | 92.7% | 1 | 0 | yes |
| 2023-05-25 | binance_bt/binance/BTC-USDT/perp | 144,357 | 1.000 | 2.7 | 0 | 5.0 / 50.0 | 0.04 | 189 | no trade record | - | - | yes |
| 2023-05-25 | binance_bt/binance/ETH-USDT/perp | 125,445 | 1.000 | 2.7 | 0 | 5.0 / 33.0 | 0.06 | 200 | no trade record | - | - | yes |
| 2023-05-25 | bybit_ob/bybit/BTC-USDT/perp | 858,977 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 184 | 92.7% | 1 | 0 | yes |
| 2023-05-25 | bybit_ob/bybit/ETH-USDT/perp | 837,887 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 198 | 91.6% | 1 | 0 | yes |
| 2023-05-26 | binance_bt/binance/BTC-USDT/perp | 106,843 | 1.000 | 1.7 | 0 | 5.0 / 20.0 | 0.04 | 136 | no trade record | - | - | yes |
| 2023-05-26 | binance_bt/binance/ETH-USDT/perp | 98,102 | 1.000 | 1.5 | 0 | 5.0 / 14.0 | 0.06 | 132 | no trade record | - | - | yes |
| 2023-05-26 | bybit_ob/bybit/BTC-USDT/perp | 857,479 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 131 | 95.3% | 1 | 0 | yes |
| 2023-05-26 | bybit_ob/bybit/ETH-USDT/perp | 837,392 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 130 | 94.4% | 1 | 0 | yes |
| 2023-05-27 | binance_bt/binance/BTC-USDT/perp | 41,993 | 1.000 | 0.8 | 0 | 5.0 / 22.0 | 0.04 | 98 | no trade record | - | - | yes |
| 2023-05-27 | binance_bt/binance/ETH-USDT/perp | 46,245 | 1.000 | 1.4 | 0 | 5.0 / 16.0 | 0.05 | 112 | no trade record | - | - | yes |
| 2023-05-27 | bybit_ob/bybit/BTC-USDT/perp | 849,574 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 93 | 96.4% | 0 | 0 | yes |
| 2023-05-27 | bybit_ob/bybit/ETH-USDT/perp | 807,778 | 1.000 | 0.8 | 0 | 0.0 / 0.0 | 0.05 | 106 | 95.5% | 0 | 0 | yes |
| 2023-05-28 | binance_bt/binance/BTC-USDT/perp | 148,456 | 1.000 | 1.0 | 0 | 6.0 / 496.0 | 0.04 | 204 | no trade record | - | - | yes |
| 2023-05-28 | binance_bt/binance/ETH-USDT/perp | 139,970 | 1.000 | 1.6 | 0 | 5.0 / 84.0 | 0.05 | 225 | no trade record | - | - | yes |
| 2023-05-28 | bybit_ob/bybit/BTC-USDT/perp | 857,084 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 202 | 90.2% | 1 | 0 | yes |
| 2023-05-28 | bybit_ob/bybit/ETH-USDT/perp | 828,927 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 225 | 89.5% | 1 | 0 | yes |
| 2023-05-29 | binance_bt/binance/BTC-USDT/perp | 137,999 | 1.000 | 2.0 | 0 | 5.0 / 29.0 | 0.04 | 178 | no trade record | - | - | yes |
| 2023-05-29 | binance_bt/binance/ETH-USDT/perp | 122,146 | 1.000 | 2.2 | 0 | 5.0 / 19.0 | 0.05 | 168 | no trade record | - | - | yes |
| 2023-05-29 | bybit_ob/bybit/BTC-USDT/perp | 856,659 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 176 | 94.0% | 0 | 0 | yes |
| 2023-05-29 | bybit_ob/bybit/ETH-USDT/perp | 828,601 | 1.000 | 0.8 | 0 | 0.0 / 0.0 | 0.05 | 166 | 94.4% | 1 | 0 | yes |
| 2023-05-30 | binance_bt/binance/BTC-USDT/perp | 127,804 | 1.000 | 2.0 | 0 | 5.0 / 20.0 | 0.04 | 173 | no trade record | - | - | yes |
| 2023-05-30 | binance_bt/binance/ETH-USDT/perp | 113,474 | 1.000 | 4.3 | 0 | 5.0 / 17.0 | 0.05 | 168 | no trade record | - | - | yes |
| 2023-05-30 | bybit_ob/bybit/BTC-USDT/perp | 856,480 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 172 | 94.9% | 1 | 0 | yes |
| 2023-05-30 | bybit_ob/bybit/ETH-USDT/perp | 833,212 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 166 | 95.0% | 1 | 0 | yes |
| 2023-05-31 | binance_bt/binance/BTC-USDT/perp | 163,776 | 1.000 | 3.7 | 0 | 5.0 / 36.0 | 0.04 | 197 | no trade record | - | - | yes |
| 2023-05-31 | binance_bt/binance/ETH-USDT/perp | 132,922 | 1.000 | 5.5 | 0 | 5.0 / 13.0 | 0.05 | 179 | no trade record | - | - | yes |
| 2023-05-31 | bybit_ob/bybit/BTC-USDT/perp | 858,911 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 194 | 93.9% | 0 | 0 | yes |
| 2023-05-31 | bybit_ob/bybit/ETH-USDT/perp | 835,059 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 176 | 96.1% | 0 | 0 | yes |
| 2023-06-01 | binance_bt/binance/BTC-USDT/perp | 137,961 | 1.000 | 1.8 | 0 | 5.0 / 17.0 | 0.04 | 203 | no trade record | - | - | yes |
| 2023-06-01 | binance_bt/binance/ETH-USDT/perp | 129,397 | 1.000 | 2.6 | 0 | 5.0 / 11.0 | 0.05 | 197 | no trade record | - | - | yes |
| 2023-06-01 | bybit_ob/bybit/BTC-USDT/perp | 857,441 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 200 | 93.3% | 1 | 0 | yes |
| 2023-06-01 | bybit_ob/bybit/ETH-USDT/perp | 827,140 | 1.000 | 0.8 | 0 | 0.0 / 0.0 | 0.05 | 193 | 95.4% | 0 | 0 | yes |
| 2023-06-02 | binance_bt/binance/BTC-USDT/perp | 153,600 | 1.000 | 3.5 | 0 | 5.0 / 15.0 | 0.04 | 185 | no trade record | - | - | yes |
| 2023-06-02 | binance_bt/binance/ETH-USDT/perp | 132,274 | 1.000 | 3.6 | 0 | 5.0 / 11.0 | 0.05 | 167 | no trade record | - | - | yes |
| 2023-06-02 | bybit_ob/bybit/BTC-USDT/perp | 858,198 | 1.000 | 1.5 | 0 | 0.0 / 0.0 | 0.04 | 184 | 93.3% | 1 | 0 | yes |
| 2023-06-02 | bybit_ob/bybit/ETH-USDT/perp | 829,118 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 164 | 93.9% | 1 | 0 | yes |
| 2023-06-03 | binance_bt/binance/BTC-USDT/perp | 47,855 | 1.000 | 2.8 | 0 | 5.0 / 24.0 | 0.04 | 106 | no trade record | - | - | yes |
| 2023-06-03 | binance_bt/binance/ETH-USDT/perp | 51,642 | 1.000 | 4.7 | 0 | 5.0 / 11.0 | 0.05 | 105 | no trade record | - | - | yes |
| 2023-06-03 | bybit_ob/bybit/BTC-USDT/perp | 850,387 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 100 | 95.4% | 0 | 0 | yes |
| 2023-06-03 | bybit_ob/bybit/ETH-USDT/perp | 803,988 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 103 | 97.7% | 0 | 0 | yes |
| 2023-06-04 | binance_bt/binance/BTC-USDT/perp | 60,310 | 1.000 | 2.2 | 0 | 5.0 / 23.0 | 0.04 | 121 | no trade record | - | - | yes |
| 2023-06-04 | binance_bt/binance/ETH-USDT/perp | 61,904 | 1.000 | 3.0 | 0 | 5.0 / 12.0 | 0.05 | 123 | no trade record | - | - | yes |
| 2023-06-04 | bybit_ob/bybit/BTC-USDT/perp | 850,566 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 117 | 92.9% | 0 | 0 | yes |
| 2023-06-04 | bybit_ob/bybit/ETH-USDT/perp | 803,713 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 120 | 95.9% | 1 | 0 | yes |
| 2023-06-05 | binance_bt/binance/BTC-USDT/perp | 397,135 | 1.000 | 2.0 | 0 | 5.0 / 39.0 | 0.08 | 281 | no trade record | - | - | yes |
| 2023-06-05 | binance_bt/binance/ETH-USDT/perp | 305,313 | 1.000 | 4.0 | 0 | 5.0 / 27.0 | 0.11 | 266 | no trade record | - | - | yes |
| 2023-06-05 | bybit_ob/bybit/BTC-USDT/perp | 858,533 | 1.000 | 1.5 | 0 | 0.0 / 0.0 | 0.04 | 284 | 90.1% | 1 | 0 | yes |
| 2023-06-05 | bybit_ob/bybit/ETH-USDT/perp | 832,007 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 268 | 90.4% | 0 | 0 | yes |
| 2023-06-06 | binance_bt/binance/BTC-USDT/perp | 302,056 | 1.000 | 2.2 | 0 | 5.0 / 13.0 | 0.04 | 275 | no trade record | - | - | yes |
| 2023-06-06 | binance_bt/binance/ETH-USDT/perp | 214,162 | 1.000 | 3.3 | 0 | 5.0 / 11.0 | 0.06 | 226 | no trade record | - | - | yes |
| 2023-06-06 | bybit_ob/bybit/BTC-USDT/perp | 857,828 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 273 | 91.9% | 0 | 0 | yes |
| 2023-06-06 | bybit_ob/bybit/ETH-USDT/perp | 824,305 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 227 | 93.0% | 0 | 0 | yes |
| 2023-06-07 | binance_bt/binance/BTC-USDT/perp | 282,009 | 1.000 | 1.8 | 0 | 5.0 / 13.0 | 0.04 | 282 | no trade record | - | - | yes |
| 2023-06-07 | binance_bt/binance/ETH-USDT/perp | 199,223 | 1.000 | 2.9 | 0 | 5.0 / 11.0 | 0.05 | 229 | no trade record | - | - | yes |
| 2023-06-07 | bybit_ob/bybit/BTC-USDT/perp | 859,100 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 279 | 94.3% | 0 | 0 | yes |
| 2023-06-07 | bybit_ob/bybit/ETH-USDT/perp | 830,908 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 228 | 93.7% | 1 | 0 | yes |
| 2023-06-08 | binance_bt/binance/BTC-USDT/perp | 127,254 | 1.000 | 4.7 | 0 | 5.0 / 12.0 | 0.04 | 180 | no trade record | - | - | yes |
| 2023-06-08 | binance_bt/binance/ETH-USDT/perp | 99,308 | 1.000 | 3.3 | 0 | 5.0 / 10.0 | 0.05 | 143 | no trade record | - | - | yes |
| 2023-06-08 | bybit_ob/bybit/BTC-USDT/perp | 855,864 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 178 | 95.8% | 0 | 0 | yes |
| 2023-06-08 | bybit_ob/bybit/ETH-USDT/perp | 810,961 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 140 | 94.6% | 1 | 0 | yes |
| 2023-06-09 | binance_bt/binance/BTC-USDT/perp | 106,043 | 1.000 | 5.2 | 0 | 5.0 / 12.0 | 0.04 | 149 | no trade record | - | - | yes |
| 2023-06-09 | binance_bt/binance/ETH-USDT/perp | 96,044 | 1.000 | 4.1 | 0 | 5.0 / 11.0 | 0.05 | 135 | no trade record | - | - | yes |
| 2023-06-09 | bybit_ob/bybit/BTC-USDT/perp | 855,911 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 145 | 94.0% | 1 | 0 | yes |
| 2023-06-09 | bybit_ob/bybit/ETH-USDT/perp | 813,834 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 135 | 94.8% | 0 | 0 | yes |
| 2023-06-10 | binance_bt/binance/BTC-USDT/perp | 325,022 | 1.000 | 3.9 | 0 | 5.0 / 14.0 | 0.04 | 283 | no trade record | - | - | yes |
| 2023-06-10 | binance_bt/binance/ETH-USDT/perp | 378,538 | 1.000 | 5.2 | 0 | 5.0 / 17.0 | 0.06 | 300 | no trade record | - | - | yes |
| 2023-06-10 | bybit_ob/bybit/BTC-USDT/perp | 859,426 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 281 | 92.6% | 0 | 0 | yes |
| 2023-06-10 | bybit_ob/bybit/ETH-USDT/perp | 836,216 | 1.000 | 0.8 | 0 | 0.0 / 0.0 | 0.06 | 303 | 93.2% | 1 | 0 | yes |
| 2023-06-11 | binance_bt/binance/BTC-USDT/perp | 123,002 | 1.000 | 4.0 | 0 | 5.0 / 10.0 | 0.04 | 165 | no trade record | - | - | yes |
| 2023-06-11 | binance_bt/binance/ETH-USDT/perp | 121,672 | 1.000 | 4.0 | 0 | 5.0 / 9.0 | 0.06 | 170 | no trade record | - | - | yes |
| 2023-06-11 | bybit_ob/bybit/BTC-USDT/perp | 856,728 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 163 | 95.5% | 0 | 0 | yes |
| 2023-06-11 | bybit_ob/bybit/ETH-USDT/perp | 817,033 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 169 | 97.6% | 0 | 0 | yes |
| 2023-06-12 | binance_bt/binance/BTC-USDT/perp | 159,017 | 1.000 | 4.1 | 0 | 5.0 / 10.0 | 0.04 | 190 | no trade record | - | - | yes |
| 2023-06-12 | binance_bt/binance/ETH-USDT/perp | 176,894 | 1.000 | 4.1 | 0 | 5.0 / 9.0 | 0.06 | 213 | no trade record | - | - | yes |
| 2023-06-12 | bybit_ob/bybit/BTC-USDT/perp | 858,214 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 187 | 96.1% | 0 | 0 | yes |
| 2023-06-12 | bybit_ob/bybit/ETH-USDT/perp | 828,412 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 212 | 97.0% | 1 | 0 | yes |
| 2023-06-13 | binance_bt/binance/BTC-USDT/perp | 214,513 | 1.000 | 4.0 | 0 | 5.0 / 10.0 | 0.04 | 209 | no trade record | - | - | yes |
| 2023-06-13 | binance_bt/binance/ETH-USDT/perp | 200,010 | 1.000 | 4.0 | 0 | 5.0 / 9.0 | 0.06 | 218 | no trade record | - | - | yes |
| 2023-06-13 | bybit_ob/bybit/BTC-USDT/perp | 858,222 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 207 | 93.7% | 1 | 0 | yes |
| 2023-06-13 | bybit_ob/bybit/ETH-USDT/perp | 827,636 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 213 | 94.3% | 1 | 0 | yes |
| 2023-06-14 | binance_bt/binance/BTC-USDT/perp | 233,471 | 1.000 | 4.3 | 0 | 5.0 / 31.0 | 0.04 | 254 | no trade record | - | - | yes |
| 2023-06-14 | binance_bt/binance/ETH-USDT/perp | 264,183 | 1.000 | 4.3 | 0 | 5.0 / 45.0 | 0.06 | 347 | no trade record | - | - | yes |
| 2023-06-14 | bybit_ob/bybit/BTC-USDT/perp | 855,646 | 1.000 | 9.6 | 3 | 0.0 / 0.0 | 0.04 | 253 | 91.9% | 0 | 0 | yes |
| 2023-06-14 | bybit_ob/bybit/ETH-USDT/perp | 819,948 | 1.000 | 9.4 | 3 | 0.0 / 0.0 | 0.06 | 352 | 89.7% | 0 | 0 | yes |
| 2023-06-15 | binance_bt/binance/BTC-USDT/perp | 206,692 | 1.000 | 8.0 | 0 | 5.0 / 10.0 | 0.04 | 198 | no trade record | - | - | yes |
| 2023-06-15 | binance_bt/binance/ETH-USDT/perp | 180,177 | 1.000 | 8.0 | 0 | 5.0 / 9.0 | 0.06 | 198 | no trade record | - | - | yes |
| 2023-06-15 | bybit_ob/bybit/BTC-USDT/perp | 858,557 | 1.000 | 1.5 | 0 | 0.0 / 0.0 | 0.04 | 199 | 94.7% | 0 | 0 | yes |
| 2023-06-15 | bybit_ob/bybit/ETH-USDT/perp | 833,325 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 197 | 96.9% | 0 | 0 | yes |
| 2023-06-16 | binance_bt/binance/BTC-USDT/perp | 229,715 | 1.000 | 4.0 | 0 | 5.0 / 10.0 | 0.04 | 216 | no trade record | - | - | yes |
| 2023-06-16 | binance_bt/binance/ETH-USDT/perp | 181,563 | 1.000 | 4.0 | 0 | 5.0 / 9.0 | 0.06 | 215 | no trade record | - | - | yes |
| 2023-06-16 | bybit_ob/bybit/BTC-USDT/perp | 855,750 | 1.000 | 1.5 | 0 | 0.0 / 0.0 | 0.04 | 211 | 91.9% | 1 | 0 | yes |
| 2023-06-16 | bybit_ob/bybit/ETH-USDT/perp | 819,405 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 213 | 94.0% | 1 | 0 | yes |
| 2023-06-17 | binance_bt/binance/BTC-USDT/perp | 127,717 | 1.000 | 4.1 | 0 | 5.0 / 11.0 | 0.04 | 187 | no trade record | - | - | yes |
| 2023-06-17 | binance_bt/binance/ETH-USDT/perp | 112,038 | 1.000 | 4.1 | 0 | 5.0 / 10.0 | 0.06 | 224 | no trade record | - | - | yes |
| 2023-06-17 | bybit_ob/bybit/BTC-USDT/perp | 853,644 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 182 | 92.1% | 0 | 0 | yes |
| 2023-06-17 | bybit_ob/bybit/ETH-USDT/perp | 803,368 | 1.000 | 0.8 | 0 | 0.0 / 0.0 | 0.06 | 221 | 93.2% | 1 | 0 | yes |
| 2023-06-18 | binance_bt/binance/BTC-USDT/perp | 101,920 | 1.000 | 4.5 | 0 | 5.0 / 10.0 | 0.04 | 135 | no trade record | - | - | yes |
| 2023-06-18 | binance_bt/binance/ETH-USDT/perp | 91,504 | 1.000 | 4.2 | 0 | 5.0 / 10.0 | 0.06 | 142 | no trade record | - | - | yes |
| 2023-06-18 | bybit_ob/bybit/BTC-USDT/perp | 852,813 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 134 | 94.7% | 1 | 0 | yes |
| 2023-06-18 | bybit_ob/bybit/ETH-USDT/perp | 802,093 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 140 | 96.6% | 1 | 0 | yes |
| 2023-06-19 | binance_bt/binance/BTC-USDT/perp | 171,911 | 1.000 | 4.3 | 0 | 5.0 / 11.0 | 0.04 | 178 | no trade record | - | - | yes |
| 2023-06-19 | binance_bt/binance/ETH-USDT/perp | 152,854 | 1.000 | 5.3 | 0 | 5.0 / 10.0 | 0.06 | 188 | no trade record | - | - | yes |
| 2023-06-19 | bybit_ob/bybit/BTC-USDT/perp | 851,867 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 178 | 92.8% | 1 | 0 | yes |
| 2023-06-19 | bybit_ob/bybit/ETH-USDT/perp | 807,498 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 183 | 94.5% | 0 | 0 | yes |
| 2023-06-20 | binance_bt/binance/BTC-USDT/perp | 329,100 | 1.000 | 4.5 | 0 | 5.0 / 20.0 | 0.04 | 262 | no trade record | - | - | yes |
| 2023-06-20 | binance_bt/binance/ETH-USDT/perp | 189,696 | 1.000 | 3.5 | 0 | 5.0 / 11.0 | 0.06 | 215 | no trade record | - | - | yes |
| 2023-06-20 | bybit_ob/bybit/BTC-USDT/perp | 856,536 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 263 | 92.1% | 1 | 0 | yes |
| 2023-06-20 | bybit_ob/bybit/ETH-USDT/perp | 833,973 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 214 | 94.0% | 1 | 0 | yes |
| 2023-06-21 | binance_bt/binance/BTC-USDT/perp | 594,033 | 1.000 | 3.6 | 0 | 5.0 / 71.0 | 0.03 | 369 | no trade record | - | - | yes |
| 2023-06-21 | binance_bt/binance/ETH-USDT/perp | 340,825 | 1.000 | 4.1 | 0 | 5.0 / 12.0 | 0.06 | 300 | no trade record | - | - | yes |
| 2023-06-21 | bybit_ob/bybit/BTC-USDT/perp | 860,145 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 369 | 91.0% | 0 | 0 | yes |
| 2023-06-21 | bybit_ob/bybit/ETH-USDT/perp | 847,164 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 297 | 92.3% | 1 | 0 | yes |
| 2023-06-22 | binance_bt/binance/BTC-USDT/perp | 303,406 | 1.000 | 6.0 | 0 | 5.0 / 12.0 | 0.03 | 253 | no trade record | - | - | yes |
| 2023-06-22 | binance_bt/binance/ETH-USDT/perp | 209,668 | 1.000 | 6.0 | 0 | 5.0 / 11.0 | 0.05 | 238 | no trade record | - | - | yes |
| 2023-06-22 | bybit_ob/bybit/BTC-USDT/perp | 858,002 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 254 | 94.4% | 0 | 0 | yes |
| 2023-06-22 | bybit_ob/bybit/ETH-USDT/perp | 841,611 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 237 | 94.9% | 1 | 0 | yes |
| 2023-06-23 | binance_bt/binance/BTC-USDT/perp | 412,838 | 1.000 | 3.0 | 0 | 5.0 / 187.0 | 0.03 | 322 | no trade record | - | - | yes |
| 2023-06-23 | binance_bt/binance/ETH-USDT/perp | 250,898 | 1.000 | 4.0 | 0 | 5.0 / 10.0 | 0.05 | 275 | no trade record | - | - | yes |
| 2023-06-23 | bybit_ob/bybit/BTC-USDT/perp | 857,214 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 320 | 91.4% | 0 | 0 | yes |
| 2023-06-23 | bybit_ob/bybit/ETH-USDT/perp | 843,710 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 272 | 94.1% | 1 | 0 | yes |
| 2023-06-24 | binance_bt/binance/BTC-USDT/perp | 162,593 | 1.000 | 3.6 | 0 | 5.0 / 12.0 | 0.03 | 171 | no trade record | - | - | yes |
| 2023-06-24 | binance_bt/binance/ETH-USDT/perp | 125,997 | 1.000 | 3.2 | 0 | 5.0 / 10.0 | 0.05 | 170 | no trade record | - | - | yes |
| 2023-06-24 | bybit_ob/bybit/BTC-USDT/perp | 852,658 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 169 | 95.1% | 1 | 0 | yes |
| 2023-06-24 | bybit_ob/bybit/ETH-USDT/perp | 827,210 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 169 | 96.1% | 1 | 0 | yes |
| 2023-06-25 | binance_bt/binance/BTC-USDT/perp | 153,350 | 1.000 | 2.4 | 0 | 5.0 / 13.0 | 0.03 | 180 | no trade record | - | - | yes |
| 2023-06-25 | binance_bt/binance/ETH-USDT/perp | 178,350 | 1.000 | 3.2 | 0 | 5.0 / 11.0 | 0.05 | 217 | no trade record | - | - | yes |
| 2023-06-25 | bybit_ob/bybit/BTC-USDT/perp | 851,224 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 178 | 95.2% | 1 | 0 | yes |
| 2023-06-25 | bybit_ob/bybit/ETH-USDT/perp | 839,922 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 213 | 95.9% | 1 | 0 | yes |
| 2023-06-26 | binance_bt/binance/BTC-USDT/perp | 245,415 | 1.000 | 5.1 | 0 | 5.0 / 13.0 | 0.03 | 223 | no trade record | - | - | yes |
| 2023-06-26 | binance_bt/binance/ETH-USDT/perp | 224,512 | 1.000 | 5.1 | 0 | 5.0 / 11.0 | 0.05 | 250 | no trade record | - | - | yes |
| 2023-06-26 | bybit_ob/bybit/BTC-USDT/perp | 857,460 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 223 | 94.9% | 0 | 0 | yes |
| 2023-06-26 | bybit_ob/bybit/ETH-USDT/perp | 844,442 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 249 | 94.3% | 0 | 0 | yes |
| 2023-06-27 | binance_bt/binance/BTC-USDT/perp | 199,403 | 1.000 | 2.9 | 0 | 5.0 / 13.0 | 0.03 | 201 | no trade record | - | - | yes |
| 2023-06-27 | binance_bt/binance/ETH-USDT/perp | 173,820 | 1.000 | 3.8 | 0 | 5.0 / 12.0 | 0.05 | 214 | no trade record | - | - | yes |
| 2023-06-27 | bybit_ob/bybit/BTC-USDT/perp | 856,389 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 200 | 94.5% | 0 | 0 | yes |
| 2023-06-27 | bybit_ob/bybit/ETH-USDT/perp | 841,634 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 215 | 94.9% | 1 | 0 | yes |
| 2023-06-28 | binance_bt/binance/BTC-USDT/perp | 185,911 | 1.000 | 2.2 | 0 | 5.0 / 13.0 | 0.03 | 207 | no trade record | - | - | yes |
| 2023-06-28 | binance_bt/binance/ETH-USDT/perp | 183,947 | 1.000 | 2.4 | 0 | 5.0 / 11.0 | 0.05 | 231 | no trade record | - | - | yes |
| 2023-06-28 | bybit_ob/bybit/BTC-USDT/perp | 856,881 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 210 | 94.0% | 1 | 0 | yes |
| 2023-06-28 | bybit_ob/bybit/ETH-USDT/perp | 847,111 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 232 | 94.0% | 0 | 0 | yes |
| 2023-06-29 | binance_bt/binance/BTC-USDT/perp | 159,140 | 1.000 | 3.8 | 0 | 5.0 / 13.0 | 0.03 | 182 | no trade record | - | - | yes |
| 2023-06-29 | binance_bt/binance/ETH-USDT/perp | 130,326 | 1.000 | 3.8 | 0 | 5.0 / 11.0 | 0.05 | 185 | no trade record | - | - | yes |
| 2023-06-29 | bybit_ob/bybit/BTC-USDT/perp | 855,653 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 181 | 94.2% | 1 | 0 | yes |
| 2023-06-29 | bybit_ob/bybit/ETH-USDT/perp | 852,882 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 184 | 94.7% | 1 | 0 | yes |
| 2023-06-30 | binance_bt/binance/BTC-USDT/perp | 459,642 | 1.000 | 2.5 | 0 | 5.0 / 15.0 | 0.06 | 399 | no trade record | - | - | yes |
| 2023-06-30 | binance_bt/binance/ETH-USDT/perp | 410,785 | 1.000 | 3.9 | 0 | 5.0 / 11.0 | 0.05 | 416 | no trade record | - | - | yes |
| 2023-06-30 | bybit_ob/bybit/BTC-USDT/perp | 859,737 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 408 | 89.4% | 0 | 0 | yes |
| 2023-06-30 | bybit_ob/bybit/ETH-USDT/perp | 859,912 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 413 | 91.7% | 1 | 0 | yes |
| 2023-07-01 | binance_bt/binance/BTC-USDT/perp | 62,487 | 1.000 | 6.9 | 0 | 5.0 / 12.0 | 0.03 | 102 | no trade record | - | - | yes |
| 2023-07-01 | binance_bt/binance/ETH-USDT/perp | 98,924 | 1.000 | 6.9 | 0 | 5.0 / 10.0 | 0.05 | 150 | no trade record | - | - | yes |
| 2023-07-01 | bybit_ob/bybit/BTC-USDT/perp | 853,242 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 94 | 96.9% | 1 | 0 | yes |
| 2023-07-01 | bybit_ob/bybit/ETH-USDT/perp | 851,842 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 147 | 96.9% | 1 | 0 | yes |
| 2023-07-02 | binance_bt/binance/BTC-USDT/perp | 95,884 | 1.000 | 2.5 | 0 | 5.0 / 13.0 | 0.03 | 169 | no trade record | - | - | yes |
| 2023-07-02 | binance_bt/binance/ETH-USDT/perp | 150,740 | 1.000 | 4.5 | 0 | 5.0 / 11.0 | 0.05 | 232 | no trade record | - | - | yes |
| 2023-07-02 | bybit_ob/bybit/BTC-USDT/perp | 854,053 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 176 | 93.9% | 1 | 0 | yes |
| 2023-07-02 | bybit_ob/bybit/ETH-USDT/perp | 851,824 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 236 | 92.4% | 1 | 0 | yes |
| 2023-07-03 | binance_bt/binance/BTC-USDT/perp | 146,410 | 1.000 | 3.9 | 0 | 5.0 / 16.0 | 0.03 | 170 | no trade record | - | - | yes |
| 2023-07-03 | binance_bt/binance/ETH-USDT/perp | 150,610 | 1.000 | 3.0 | 0 | 5.0 / 13.0 | 0.05 | 194 | no trade record | - | - | yes |
| 2023-07-03 | bybit_ob/bybit/BTC-USDT/perp | 860,678 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 167 | 93.3% | 0 | 0 | yes |
| 2023-07-03 | bybit_ob/bybit/ETH-USDT/perp | 854,271 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 194 | 94.9% | 0 | 0 | yes |
| 2023-07-04 | binance_bt/binance/BTC-USDT/perp | 111,117 | 1.000 | 4.7 | 0 | 5.0 / 15.0 | 0.03 | 150 | no trade record | - | - | yes |
| 2023-07-04 | binance_bt/binance/ETH-USDT/perp | 100,827 | 1.000 | 4.1 | 0 | 5.0 / 12.0 | 0.05 | 148 | no trade record | - | - | yes |
| 2023-07-04 | bybit_ob/bybit/BTC-USDT/perp | 858,356 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 146 | 91.6% | 1 | 0 | yes |
| 2023-07-04 | bybit_ob/bybit/ETH-USDT/perp | 849,121 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 147 | 94.6% | 1 | 0 | yes |
| 2023-07-05 | binance_bt/binance/BTC-USDT/perp | 122,964 | 1.000 | 4.1 | 0 | 6.0 / 14.0 | 0.03 | 145 | no trade record | - | - | yes |
| 2023-07-05 | binance_bt/binance/ETH-USDT/perp | 128,582 | 1.000 | 4.2 | 0 | 5.0 / 12.0 | 0.05 | 168 | no trade record | - | - | yes |
| 2023-07-05 | bybit_ob/bybit/BTC-USDT/perp | 857,122 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 143 | 94.9% | 0 | 0 | yes |
| 2023-07-05 | bybit_ob/bybit/ETH-USDT/perp | 849,231 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 168 | 94.4% | 0 | 0 | yes |
| 2023-07-06 | binance_bt/binance/BTC-USDT/perp | 309,230 | 1.000 | 2.5 | 0 | 5.0 / 14.0 | 0.03 | 268 | no trade record | - | - | yes |
| 2023-07-06 | binance_bt/binance/ETH-USDT/perp | 251,646 | 1.000 | 4.5 | 0 | 5.0 / 10.0 | 0.05 | 261 | no trade record | - | - | yes |
| 2023-07-06 | bybit_ob/bybit/BTC-USDT/perp | 859,356 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 271 | 92.0% | 0 | 0 | yes |
| 2023-07-06 | bybit_ob/bybit/ETH-USDT/perp | 854,725 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 255 | 92.7% | 1 | 0 | yes |
| 2023-07-07 | binance_bt/binance/BTC-USDT/perp | 159,203 | 1.000 | 4.6 | 0 | 6.0 / 27.0 | 0.03 | 186 | no trade record | - | - | yes |
| 2023-07-07 | binance_bt/binance/ETH-USDT/perp | 135,010 | 1.000 | 3.1 | 0 | 5.0 / 15.0 | 0.05 | 197 | no trade record | - | - | yes |
| 2023-07-07 | bybit_ob/bybit/BTC-USDT/perp | 857,464 | 1.000 | 1.5 | 0 | 0.0 / 0.0 | 0.03 | 189 | 94.1% | 1 | 0 | yes |
| 2023-07-07 | bybit_ob/bybit/ETH-USDT/perp | 850,733 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 196 | 94.6% | 1 | 0 | yes |
| 2023-07-08 | binance_bt/binance/BTC-USDT/perp | 41,063 | 1.000 | 3.6 | 0 | 6.0 / 22.0 | 0.03 | 93 | no trade record | - | - | yes |
| 2023-07-08 | binance_bt/binance/ETH-USDT/perp | 56,396 | 1.000 | 2.5 | 0 | 5.0 / 14.0 | 0.05 | 116 | no trade record | - | - | yes |
| 2023-07-08 | bybit_ob/bybit/BTC-USDT/perp | 853,426 | 1.000 | 1.5 | 0 | 0.0 / 0.0 | 0.03 | 89 | 96.6% | 0 | 0 | yes |
| 2023-07-08 | bybit_ob/bybit/ETH-USDT/perp | 846,013 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 115 | 97.1% | 1 | 0 | yes |
| 2023-07-09 | binance_bt/binance/BTC-USDT/perp | 51,611 | 1.000 | 5.1 | 0 | 6.0 / 25.0 | 0.03 | 108 | no trade record | - | - | yes |
| 2023-07-09 | binance_bt/binance/ETH-USDT/perp | 64,420 | 1.000 | 4.9 | 0 | 5.0 / 16.0 | 0.05 | 131 | no trade record | - | - | yes |
| 2023-07-09 | bybit_ob/bybit/BTC-USDT/perp | 856,065 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 101 | 95.6% | 0 | 0 | yes |
| 2023-07-09 | bybit_ob/bybit/ETH-USDT/perp | 845,148 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 127 | 95.6% | 1 | 0 | yes |
| 2023-07-10 | binance_bt/binance/BTC-USDT/perp | 169,903 | 1.000 | 4.6 | 0 | 6.0 / 68.0 | 0.03 | 206 | no trade record | - | - | yes |
| 2023-07-10 | binance_bt/binance/ETH-USDT/perp | 124,533 | 1.000 | 4.7 | 0 | 6.0 / 15.0 | 0.05 | 181 | no trade record | - | - | yes |
| 2023-07-10 | bybit_ob/bybit/BTC-USDT/perp | 860,871 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 203 | 94.2% | 0 | 0 | yes |
| 2023-07-10 | bybit_ob/bybit/ETH-USDT/perp | 855,133 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 182 | 94.1% | 0 | 0 | yes |
| 2023-07-11 | binance_bt/binance/BTC-USDT/perp | 122,669 | 1.000 | 4.4 | 0 | 6.0 / 26.0 | 0.03 | 152 | no trade record | - | - | yes |
| 2023-07-11 | binance_bt/binance/ETH-USDT/perp | 79,566 | 1.000 | 4.6 | 0 | 6.0 / 15.0 | 0.05 | 137 | no trade record | - | - | yes |
| 2023-07-11 | bybit_ob/bybit/BTC-USDT/perp | 859,703 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 146 | 94.8% | 0 | 0 | yes |
| 2023-07-11 | bybit_ob/bybit/ETH-USDT/perp | 851,547 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 137 | 97.4% | 1 | 0 | yes |
| 2023-07-12 | binance_bt/binance/BTC-USDT/perp | 186,681 | 1.000 | 3.8 | 0 | 6.0 / 30.0 | 0.03 | 184 | no trade record | - | - | yes |
| 2023-07-12 | binance_bt/binance/ETH-USDT/perp | 130,733 | 1.000 | 3.4 | 0 | 5.0 / 15.0 | 0.05 | 168 | no trade record | - | - | yes |
| 2023-07-12 | bybit_ob/bybit/BTC-USDT/perp | 860,495 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 181 | 93.1% | 1 | 0 | yes |
| 2023-07-12 | bybit_ob/bybit/ETH-USDT/perp | 853,568 | 1.000 | 1.0 | 0 | 0.0 / 0.0 | 0.05 | 165 | 93.3% | 1 | 0 | yes |
| 2023-07-13 | binance_bt/binance/BTC-USDT/perp | 326,717 | 1.000 | 2.2 | 0 | 6.0 / 53.0 | 0.03 | 260 | no trade record | - | - | yes |
| 2023-07-13 | binance_bt/binance/ETH-USDT/perp | 291,800 | 1.000 | 2.8 | 0 | 5.0 / 28.0 | 0.10 | 293 | no trade record | - | - | yes |
| 2023-07-13 | bybit_ob/bybit/BTC-USDT/perp | 861,109 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 263 | 91.2% | 1 | 0 | yes |
| 2023-07-13 | bybit_ob/bybit/ETH-USDT/perp | 854,939 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 289 | 92.0% | 1 | 0 | yes |
| 2023-07-14 | binance_bt/binance/BTC-USDT/perp | 282,965 | 1.000 | 2.2 | 0 | 6.0 / 26.0 | 0.03 | 245 | no trade record | - | - | yes |
| 2023-07-14 | binance_bt/binance/ETH-USDT/perp | 250,615 | 1.000 | 4.9 | 0 | 5.0 / 16.0 | 0.05 | 281 | no trade record | - | - | yes |
| 2023-07-14 | bybit_ob/bybit/BTC-USDT/perp | 861,022 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 245 | 92.0% | 1 | 0 | yes |
| 2023-07-14 | bybit_ob/bybit/ETH-USDT/perp | 856,843 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 278 | 91.5% | 0 | 0 | yes |
| 2023-07-15 | binance_bt/binance/BTC-USDT/perp | 31,521 | 1.000 | 1.9 | 0 | 6.0 / 22.0 | 0.03 | 74 | no trade record | - | - | yes |
| 2023-07-15 | binance_bt/binance/ETH-USDT/perp | 45,928 | 1.000 | 3.1 | 0 | 5.0 / 14.0 | 0.05 | 106 | no trade record | - | - | yes |
| 2023-07-15 | bybit_ob/bybit/BTC-USDT/perp | 854,837 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 70 | 97.7% | 1 | 0 | yes |
| 2023-07-15 | bybit_ob/bybit/ETH-USDT/perp | 845,754 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 102 | 98.6% | 0 | 0 | yes |
| 2023-07-16 | binance_bt/binance/BTC-USDT/perp | 59,304 | 1.000 | 3.3 | 0 | 6.0 / 22.0 | 0.03 | 110 | no trade record | - | - | yes |
| 2023-07-16 | binance_bt/binance/ETH-USDT/perp | 64,639 | 1.000 | 3.7 | 0 | 5.0 / 14.0 | 0.05 | 129 | no trade record | - | - | yes |
| 2023-07-16 | bybit_ob/bybit/BTC-USDT/perp | 855,996 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 111 | 91.7% | 1 | 0 | yes |
| 2023-07-16 | bybit_ob/bybit/ETH-USDT/perp | 845,557 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 127 | 96.7% | 1 | 0 | yes |
| 2023-07-17 | binance_bt/binance/BTC-USDT/perp | 145,256 | 1.000 | 3.5 | 0 | 6.0 / 24.0 | 0.03 | 183 | no trade record | - | - | yes |
| 2023-07-17 | binance_bt/binance/ETH-USDT/perp | 136,254 | 1.000 | 3.7 | 0 | 5.0 / 15.0 | 0.05 | 198 | no trade record | - | - | yes |
| 2023-07-17 | bybit_ob/bybit/BTC-USDT/perp | 858,252 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 185 | 90.7% | 1 | 0 | yes |
| 2023-07-17 | bybit_ob/bybit/ETH-USDT/perp | 851,586 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 198 | 90.5% | 1 | 0 | yes |
| 2023-07-18 | binance_bt/binance/BTC-USDT/perp | 156,072 | 1.000 | 2.5 | 0 | 6.0 / 18.0 | 0.03 | 189 | no trade record | - | - | yes |
| 2023-07-18 | binance_bt/binance/ETH-USDT/perp | 109,971 | 1.000 | 4.8 | 0 | 5.0 / 13.0 | 0.05 | 175 | no trade record | - | - | yes |
| 2023-07-18 | bybit_ob/bybit/BTC-USDT/perp | 859,617 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 185 | 92.7% | 0 | 0 | yes |
| 2023-07-18 | bybit_ob/bybit/ETH-USDT/perp | 854,264 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 174 | 95.3% | 0 | 0 | yes |
| 2023-07-19 | binance_bt/binance/BTC-USDT/perp | 123,775 | 1.000 | 3.2 | 0 | 6.0 / 21.0 | 0.03 | 150 | no trade record | - | - | yes |
| 2023-07-19 | binance_bt/binance/ETH-USDT/perp | 108,299 | 1.000 | 6.8 | 0 | 6.0 / 15.0 | 0.05 | 166 | no trade record | - | - | yes |
| 2023-07-19 | bybit_ob/bybit/BTC-USDT/perp | 860,141 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 148 | 94.7% | 1 | 0 | yes |
| 2023-07-19 | bybit_ob/bybit/ETH-USDT/perp | 853,380 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 166 | 90.4% | 1 | 0 | yes |
| 2023-07-20 | binance_bt/binance/BTC-USDT/perp | 162,620 | 1.000 | 3.4 | 0 | 6.0 / 24.0 | 0.03 | 169 | no trade record | - | - | yes |
| 2023-07-20 | binance_bt/binance/ETH-USDT/perp | 140,184 | 1.000 | 2.0 | 0 | 5.0 / 14.0 | 0.05 | 171 | no trade record | - | - | yes |
| 2023-07-20 | bybit_ob/bybit/BTC-USDT/perp | 860,084 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 172 | 90.4% | 1 | 0 | yes |
| 2023-07-20 | bybit_ob/bybit/ETH-USDT/perp | 854,463 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 169 | 93.2% | 1 | 0 | yes |
| 2023-07-21 | binance_bt/binance/BTC-USDT/perp | 78,442 | 1.000 | 2.4 | 0 | 6.0 / 20.0 | 0.03 | 122 | no trade record | - | - | yes |
| 2023-07-21 | binance_bt/binance/ETH-USDT/perp | 70,507 | 1.000 | 4.7 | 0 | 5.0 / 14.0 | 0.05 | 124 | no trade record | - | - | yes |
| 2023-07-21 | bybit_ob/bybit/BTC-USDT/perp | 858,624 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 119 | 95.4% | 0 | 0 | yes |
| 2023-07-21 | bybit_ob/bybit/ETH-USDT/perp | 852,052 | 1.000 | 1.0 | 0 | 0.0 / 0.0 | 0.05 | 121 | 93.6% | 2 | 0 | yes |
| 2023-07-22 | binance_bt/binance/BTC-USDT/perp | 36,397 | 1.000 | 2.5 | 0 | 6.0 / 21.0 | 0.03 | 85 | no trade record | - | - | yes |
| 2023-07-22 | binance_bt/binance/ETH-USDT/perp | 45,742 | 1.000 | 3.9 | 0 | 6.0 / 94.0 | 0.05 | 148 | no trade record | - | - | yes |
| 2023-07-22 | bybit_ob/bybit/BTC-USDT/perp | 856,936 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 81 | 96.4% | 1 | 0 | yes |
| 2023-07-22 | bybit_ob/bybit/ETH-USDT/perp | 845,617 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 143 | 90.7% | 1 | 0 | yes |
| 2023-07-23 | binance_bt/binance/BTC-USDT/perp | 61,493 | 1.000 | 1.9 | 0 | 6.0 / 20.0 | 0.03 | 109 | no trade record | - | - | yes |
| 2023-07-23 | binance_bt/binance/ETH-USDT/perp | 58,886 | 1.000 | 2.8 | 0 | 5.0 / 16.0 | 0.05 | 127 | no trade record | - | - | yes |
| 2023-07-23 | bybit_ob/bybit/BTC-USDT/perp | 857,903 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 108 | 95.2% | 1 | 0 | yes |
| 2023-07-23 | bybit_ob/bybit/ETH-USDT/perp | 849,022 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 126 | 88.5% | 1 | 0 | yes |
| 2023-07-24 | binance_bt/binance/BTC-USDT/perp | 156,584 | 1.000 | 1.7 | 0 | 6.0 / 40.0 | 0.03 | 241 | no trade record | - | - | yes |
| 2023-07-24 | binance_bt/binance/ETH-USDT/perp | 111,857 | 1.000 | 3.2 | 0 | 5.0 / 18.0 | 0.05 | 193 | no trade record | - | - | yes |
| 2023-07-24 | bybit_ob/bybit/BTC-USDT/perp | 859,753 | 1.000 | 1.5 | 0 | 0.0 / 0.0 | 0.03 | 243 | 91.4% | 1 | 0 | yes |
| 2023-07-24 | bybit_ob/bybit/ETH-USDT/perp | 850,824 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 219 | 94.4% | 1 | 0 | yes |
| 2023-07-25 | binance_bt/binance/BTC-USDT/perp | 59,588 | 1.000 | 4.0 | 0 | 6.0 / 16.0 | 0.03 | 108 | no trade record | - | - | yes |
| 2023-07-25 | binance_bt/binance/ETH-USDT/perp | 58,541 | 1.000 | 5.2 | 0 | 6.0 / 13.0 | 0.05 | 113 | no trade record | - | - | yes |
| 2023-07-25 | bybit_ob/bybit/BTC-USDT/perp | 858,116 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 104 | 96.9% | 0 | 0 | yes |
| 2023-07-25 | bybit_ob/bybit/ETH-USDT/perp | 845,371 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 107 | 95.9% | 0 | 0 | yes |
| 2023-07-26 | binance_bt/binance/BTC-USDT/perp | 112,687 | 1.000 | 3.3 | 0 | 6.0 / 20.0 | 0.03 | 158 | no trade record | - | - | yes |
| 2023-07-26 | binance_bt/binance/ETH-USDT/perp | 99,672 | 1.000 | 2.4 | 0 | 6.0 / 15.0 | 0.05 | 149 | no trade record | - | - | yes |
| 2023-07-26 | bybit_ob/bybit/BTC-USDT/perp | 861,243 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 154 | 93.6% | 0 | 0 | yes |
| 2023-07-26 | bybit_ob/bybit/ETH-USDT/perp | 848,857 | 1.000 | 0.8 | 0 | 0.0 / 0.0 | 0.05 | 145 | 92.0% | 0 | 0 | yes |
| 2023-07-27 | binance_bt/binance/BTC-USDT/perp | 67,495 | 1.000 | 2.8 | 0 | 6.0 / 19.0 | 0.03 | 106 | no trade record | - | - | yes |
| 2023-07-27 | binance_bt/binance/ETH-USDT/perp | 65,365 | 1.000 | 5.9 | 0 | 6.0 / 15.0 | 0.05 | 112 | no trade record | - | - | yes |
| 2023-07-27 | bybit_ob/bybit/BTC-USDT/perp | 861,305 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 102 | 96.5% | 1 | 0 | yes |
| 2023-07-27 | bybit_ob/bybit/ETH-USDT/perp | 848,746 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 109 | 94.0% | 0 | 0 | yes |
| 2023-07-28 | binance_bt/binance/BTC-USDT/perp | 62,056 | 1.000 | 5.4 | 0 | 6.0 / 19.0 | 0.03 | 102 | no trade record | - | - | yes |
| 2023-07-28 | binance_bt/binance/ETH-USDT/perp | 48,491 | 1.000 | 5.2 | 0 | 6.0 / 15.1 | 0.05 | 95 | no trade record | - | - | yes |
| 2023-07-28 | bybit_ob/bybit/BTC-USDT/perp | 860,735 | 1.000 | 1.5 | 0 | 0.0 / 0.0 | 0.03 | 98 | 95.4% | 1 | 0 | yes |
| 2023-07-28 | bybit_ob/bybit/ETH-USDT/perp | 838,198 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 91 | 94.0% | 1 | 0 | yes |
| 2023-07-29 | binance_bt/binance/BTC-USDT/perp | 15,524 | 1.000 | 5.3 | 0 | 6.0 / 18.0 | 0.03 | 50 | no trade record | - | - | yes |
| 2023-07-29 | binance_bt/binance/ETH-USDT/perp | 18,489 | 1.000 | 5.4 | 0 | 6.0 / 14.0 | 0.05 | 60 | no trade record | - | - | yes |
| 2023-07-29 | bybit_ob/bybit/BTC-USDT/perp | 858,692 | 1.000 | 1.5 | 0 | 0.0 / 0.0 | 0.03 | 45 | 97.4% | 1 | 0 | yes |
| 2023-07-29 | bybit_ob/bybit/ETH-USDT/perp | 819,650 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 55 | 97.3% | 1 | 0 | yes |
| 2023-07-30 | binance_bt/binance/BTC-USDT/perp | 45,724 | 1.000 | 3.5 | 0 | 6.0 / 18.0 | 0.03 | 98 | no trade record | - | - | yes |
| 2023-07-30 | binance_bt/binance/ETH-USDT/perp | 48,714 | 1.000 | 3.6 | 0 | 6.0 / 14.0 | 0.05 | 102 | no trade record | - | - | yes |
| 2023-07-30 | bybit_ob/bybit/BTC-USDT/perp | 858,225 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 97 | 94.2% | 0 | 0 | yes |
| 2023-07-30 | bybit_ob/bybit/ETH-USDT/perp | 840,705 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 98 | 95.0% | 1 | 0 | yes |
| 2023-07-31 | binance_bt/binance/BTC-USDT/perp | 69,739 | 1.000 | 2.6 | 0 | 6.0 / 18.0 | 0.03 | 115 | no trade record | - | - | yes |
| 2023-07-31 | binance_bt/binance/ETH-USDT/perp | 52,533 | 1.000 | 3.6 | 0 | 6.0 / 15.0 | 0.05 | 110 | no trade record | - | - | yes |
| 2023-07-31 | bybit_ob/bybit/BTC-USDT/perp | 860,841 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 115 | 95.0% | 0 | 0 | yes |
| 2023-07-31 | bybit_ob/bybit/ETH-USDT/perp | 845,856 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 109 | 97.4% | 0 | 0 | yes |
| 2023-08-01 | binance_bt/binance/BTC-USDT/perp | 155,207 | 1.000 | 3.4 | 0 | 6.0 / 26.0 | 0.03 | 183 | no trade record | - | - | yes |
| 2023-08-01 | binance_bt/binance/ETH-USDT/perp | 120,155 | 1.000 | 3.6 | 0 | 6.0 / 25.0 | 0.05 | 214 | no trade record | - | - | yes |
| 2023-08-01 | bybit_ob/bybit/BTC-USDT/perp | 862,592 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 183 | 89.3% | 0 | 0 | yes |
| 2023-08-01 | bybit_ob/bybit/ETH-USDT/perp | 845,915 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 205 | 90.4% | 1 | 0 | yes |
| 2023-08-02 | binance_bt/binance/BTC-USDT/perp | 174,213 | 1.000 | 2.9 | 0 | 6.0 / 16.0 | 0.03 | 183 | no trade record | - | - | yes |
| 2023-08-02 | binance_bt/binance/ETH-USDT/perp | 110,852 | 1.000 | 2.7 | 0 | 6.0 / 14.0 | 0.05 | 159 | no trade record | - | - | yes |
| 2023-08-02 | bybit_ob/bybit/BTC-USDT/perp | 862,639 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 182 | 92.5% | 1 | 0 | yes |
| 2023-08-02 | bybit_ob/bybit/ETH-USDT/perp | 847,925 | 1.000 | 0.8 | 0 | 0.0 / 0.0 | 0.05 | 159 | 93.5% | 0 | 0 | yes |
| 2023-08-03 | binance_bt/binance/BTC-USDT/perp | 91,478 | 1.000 | 3.6 | 0 | 6.0 / 17.0 | 0.03 | 117 | no trade record | - | - | yes |
| 2023-08-03 | binance_bt/binance/ETH-USDT/perp | 74,743 | 1.000 | 4.8 | 0 | 6.0 / 15.0 | 0.05 | 128 | no trade record | - | - | yes |
| 2023-08-03 | bybit_ob/bybit/BTC-USDT/perp | 862,655 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 118 | 94.4% | 1 | 0 | yes |
| 2023-08-03 | bybit_ob/bybit/ETH-USDT/perp | 846,839 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 130 | 89.0% | 1 | 0 | yes |
| 2023-08-04 | binance_bt/binance/BTC-USDT/perp | 78,270 | 1.000 | 6.4 | 0 | 6.0 / 1240.0 | 0.03 | 109 | no trade record | - | - | yes |
| 2023-08-04 | binance_bt/binance/ETH-USDT/perp | 76,872 | 1.000 | 6.4 | 0 | 6.0 / 1196.0 | 0.05 | 131 | no trade record | - | - | yes |
| 2023-08-04 | bybit_ob/bybit/BTC-USDT/perp | 862,250 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 105 | 93.9% | 0 | 0 | yes |
| 2023-08-04 | bybit_ob/bybit/ETH-USDT/perp | 842,975 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 128 | 92.3% | 1 | 0 | yes |
| 2023-08-05 | binance_bt/binance/BTC-USDT/perp | 15,264 | 1.000 | 5.4 | 0 | 6.0 / 19.0 | 0.03 | 48 | no trade record | - | - | yes |
| 2023-08-05 | binance_bt/binance/ETH-USDT/perp | 16,870 | 1.000 | 4.5 | 0 | 6.0 / 15.0 | 0.05 | 61 | no trade record | - | - | yes |
| 2023-08-05 | bybit_ob/bybit/BTC-USDT/perp | 861,960 | 1.000 | 1.5 | 0 | 0.0 / 0.0 | 0.03 | 44 | 97.7% | 1 | 0 | yes |
| 2023-08-05 | bybit_ob/bybit/ETH-USDT/perp | 833,580 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 57 | 93.6% | 1 | 0 | yes |
| 2023-08-06 | binance_bt/binance/BTC-USDT/perp | 17,795 | 1.000 | 7.4 | 0 | 6.0 / 17.0 | 0.03 | 61 | no trade record | - | - | yes |
| 2023-08-06 | binance_bt/binance/ETH-USDT/perp | 20,435 | 1.000 | 5.4 | 0 | 6.0 / 23.0 | 0.05 | 73 | no trade record | - | - | yes |
| 2023-08-06 | bybit_ob/bybit/BTC-USDT/perp | 862,220 | 1.000 | 1.5 | 0 | 0.0 / 0.0 | 0.03 | 61 | 95.5% | 0 | 0 | yes |
| 2023-08-06 | bybit_ob/bybit/ETH-USDT/perp | 841,669 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 72 | 96.6% | 0 | 0 | yes |
| 2023-08-07 | binance_bt/binance/BTC-USDT/perp | 94,678 | 1.000 | 3.8 | 0 | 6.0 / 15.0 | 0.03 | 132 | no trade record | - | - | yes |
| 2023-08-07 | binance_bt/binance/ETH-USDT/perp | 84,708 | 1.000 | 5.4 | 0 | 6.0 / 16.0 | 0.06 | 144 | no trade record | - | - | yes |
| 2023-08-07 | bybit_ob/bybit/BTC-USDT/perp | 862,740 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 128 | 91.7% | 1 | 0 | yes |
| 2023-08-07 | bybit_ob/bybit/ETH-USDT/perp | 848,263 | 1.000 | 0.8 | 0 | 0.0 / 0.0 | 0.05 | 141 | 92.3% | 1 | 0 | yes |
| 2023-08-08 | binance_bt/binance/BTC-USDT/perp | 142,186 | 1.000 | 5.3 | 0 | 6.0 / 14.0 | 0.03 | 164 | no trade record | - | - | yes |
| 2023-08-08 | binance_bt/binance/ETH-USDT/perp | 87,923 | 1.000 | 5.2 | 0 | 6.0 / 14.0 | 0.05 | 140 | no trade record | - | - | yes |
| 2023-08-08 | bybit_ob/bybit/BTC-USDT/perp | 863,136 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 164 | 90.7% | 1 | 0 | yes |
| 2023-08-08 | bybit_ob/bybit/ETH-USDT/perp | 850,716 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 137 | 87.5% | 1 | 0 | yes |
| 2023-08-09 | binance_bt/binance/BTC-USDT/perp | 111,938 | 1.000 | 7.5 | 0 | 6.0 / 14.0 | 0.03 | 138 | no trade record | - | - | yes |
| 2023-08-09 | binance_bt/binance/ETH-USDT/perp | 61,251 | 1.000 | 3.7 | 0 | 6.0 / 14.0 | 0.05 | 110 | no trade record | - | - | yes |
| 2023-08-09 | bybit_ob/bybit/BTC-USDT/perp | 862,811 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 135 | 94.0% | 0 | 0 | yes |
| 2023-08-09 | bybit_ob/bybit/ETH-USDT/perp | 854,996 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 107 | 80.2% | 1 | 0 | yes |
| 2023-08-10 | binance_bt/binance/BTC-USDT/perp | 74,274 | 1.000 | 4.8 | 0 | 6.0 / 14.0 | 0.03 | 103 | no trade record | - | - | yes |
| 2023-08-10 | binance_bt/binance/ETH-USDT/perp | 50,101 | 1.000 | 3.0 | 0 | 6.0 / 14.0 | 0.05 | 94 | no trade record | - | - | yes |
| 2023-08-10 | bybit_ob/bybit/BTC-USDT/perp | 861,753 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 100 | 95.4% | 1 | 0 | yes |
| 2023-08-10 | bybit_ob/bybit/ETH-USDT/perp | 842,597 | 1.000 | 1.0 | 0 | 0.0 / 0.0 | 0.05 | 91 | 96.5% | 2 | 0 | yes |
| 2023-08-11 | binance_bt/binance/BTC-USDT/perp | 44,868 | 1.000 | 5.8 | 0 | 6.0 / 17.0 | 0.03 | 80 | no trade record | - | - | yes |
| 2023-08-11 | binance_bt/binance/ETH-USDT/perp | 35,342 | 1.000 | 5.6 | 0 | 6.0 / 17.0 | 0.05 | 76 | no trade record | - | - | yes |
| 2023-08-11 | bybit_ob/bybit/BTC-USDT/perp | 861,507 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 77 | 94.8% | 1 | 0 | yes |
| 2023-08-11 | bybit_ob/bybit/ETH-USDT/perp | 848,227 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 71 | 96.1% | 0 | 0 | yes |
| 2023-08-12 | binance_bt/binance/BTC-USDT/perp | 6,052 | 1.000 | 4.0 | 0 | 6.0 / 15.0 | 0.03 | 27 | no trade record | - | - | yes |
| 2023-08-12 | binance_bt/binance/ETH-USDT/perp | 7,336 | 1.000 | 4.4 | 0 | 6.0 / 16.0 | 0.05 | 36 | no trade record | - | - | yes |
| 2023-08-12 | bybit_ob/bybit/BTC-USDT/perp | 858,060 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 25 | 97.6% | 0 | 0 | yes |
| 2023-08-12 | bybit_ob/bybit/ETH-USDT/perp | 817,075 | 1.000 | 0.8 | 0 | 0.0 / 0.0 | 0.05 | 32 | 59.5% | 1 | 0 | yes |
| 2023-08-13 | binance_bt/binance/BTC-USDT/perp | 9,890 | 1.000 | 3.2 | 0 | 6.0 / 15.0 | 0.03 | 41 | no trade record | - | - | yes |
| 2023-08-13 | binance_bt/binance/ETH-USDT/perp | 16,792 | 1.000 | 3.3 | 0 | 6.0 / 13.0 | 0.05 | 62 | no trade record | - | - | yes |
| 2023-08-13 | bybit_ob/bybit/BTC-USDT/perp | 858,915 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 42 | 96.2% | 1 | 0 | yes |
| 2023-08-13 | bybit_ob/bybit/ETH-USDT/perp | 808,605 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 63 | 95.5% | 1 | 0 | yes |
| 2023-08-14 | binance_bt/binance/BTC-USDT/perp | 75,893 | 1.000 | 3.1 | 0 | 6.0 / 13.0 | 0.03 | 112 | no trade record | - | - | yes |
| 2023-08-14 | binance_bt/binance/ETH-USDT/perp | 37,692 | 1.000 | 2.8 | 0 | 6.0 / 13.0 | 0.05 | 83 | no trade record | - | - | yes |
| 2023-08-14 | bybit_ob/bybit/BTC-USDT/perp | 861,347 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 111 | 94.6% | 1 | 0 | yes |
| 2023-08-14 | bybit_ob/bybit/ETH-USDT/perp | 834,334 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 84 | 96.0% | 1 | 0 | yes |
| 2023-08-15 | binance_bt/binance/BTC-USDT/perp | 49,293 | 1.000 | 5.1 | 0 | 6.0 / 13.0 | 0.03 | 87 | no trade record | - | - | yes |
| 2023-08-15 | binance_bt/binance/ETH-USDT/perp | 41,320 | 1.000 | 5.1 | 0 | 6.0 / 16.0 | 0.05 | 114 | no trade record | - | - | yes |
| 2023-08-15 | bybit_ob/bybit/BTC-USDT/perp | 861,137 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.03 | 87 | 95.3% | 0 | 0 | yes |
| 2023-08-15 | bybit_ob/bybit/ETH-USDT/perp | 828,170 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 115 | 92.3% | 0 | 0 | yes |
| 2023-08-16 | binance_bt/binance/BTC-USDT/perp | 88,535 | 1.000 | 5.1 | 0 | 6.0 / 14.0 | 0.03 | 119 | no trade record | - | - | yes |
| 2023-08-16 | binance_bt/binance/ETH-USDT/perp | 63,771 | 1.000 | 4.5 | 0 | 6.0 / 12.0 | 0.06 | 131 | no trade record | - | - | yes |
| 2023-08-16 | bybit_ob/bybit/BTC-USDT/perp | 861,818 | 1.000 | 1.5 | 0 | 0.0 / 0.0 | 0.03 | 118 | 94.0% | 0 | 0 | yes |
| 2023-08-16 | bybit_ob/bybit/ETH-USDT/perp | 825,937 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 128 | 95.3% | 1 | 0 | yes |
| 2023-08-17 | binance_bt/binance/BTC-USDT/perp | 532,653 | 1.000 | 4.1 | 0 | 6.0 / 77.0 | 0.07 | 844 | no trade record | - | - | yes |
| 2023-08-17 | binance_bt/binance/ETH-USDT/perp | 504,447 | 1.000 | 5.0 | 0 | 6.0 / 109.0 | 0.12 | 956 | no trade record | - | - | yes |
| 2023-08-17 | bybit_ob/bybit/BTC-USDT/perp | 863,053 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 935 | 86.6% | 1 | 0 | yes |
| 2023-08-17 | bybit_ob/bybit/ETH-USDT/perp | 847,215 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 1093 | 86.9% | 1 | 0 | yes |
| 2023-08-18 | binance_bt/binance/BTC-USDT/perp | 283,723 | 1.000 | 3.9 | 0 | 6.0 / 12.0 | 0.04 | 281 | no trade record | - | - | yes |
| 2023-08-18 | binance_bt/binance/ETH-USDT/perp | 247,134 | 1.000 | 3.6 | 0 | 6.0 / 11.0 | 0.06 | 303 | no trade record | - | - | yes |
| 2023-08-18 | bybit_ob/bybit/BTC-USDT/perp | 862,388 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 285 | 94.2% | 0 | 0 | yes |
| 2023-08-18 | bybit_ob/bybit/ETH-USDT/perp | 848,113 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 309 | 96.0% | 0 | 0 | yes |
| 2023-08-19 | binance_bt/binance/BTC-USDT/perp | 88,429 | 1.000 | 4.2 | 0 | 6.0 / 13.0 | 0.04 | 133 | no trade record | - | - | yes |
| 2023-08-19 | binance_bt/binance/ETH-USDT/perp | 86,320 | 1.000 | 4.2 | 0 | 6.0 / 12.0 | 0.06 | 143 | no trade record | - | - | yes |
| 2023-08-19 | bybit_ob/bybit/BTC-USDT/perp | 857,929 | 1.000 | 1.5 | 0 | 0.0 / 0.0 | 0.04 | 133 | 96.2% | 0 | 0 | yes |
| 2023-08-19 | bybit_ob/bybit/ETH-USDT/perp | 804,831 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 142 | 95.1% | 1 | 0 | yes |
| 2023-08-20 | binance_bt/binance/BTC-USDT/perp | 49,994 | 1.000 | 4.4 | 0 | 6.0 / 15.0 | 0.04 | 106 | no trade record | - | - | yes |
| 2023-08-20 | binance_bt/binance/ETH-USDT/perp | 68,378 | 1.000 | 4.8 | 0 | 6.0 / 13.0 | 0.06 | 131 | no trade record | - | - | yes |
| 2023-08-20 | bybit_ob/bybit/BTC-USDT/perp | 856,231 | 1.000 | 1.5 | 0 | 0.0 / 0.0 | 0.04 | 102 | 95.4% | 0 | 0 | yes |
| 2023-08-20 | bybit_ob/bybit/ETH-USDT/perp | 801,548 | 1.000 | 0.8 | 0 | 0.0 / 0.0 | 0.06 | 130 | 97.3% | 1 | 0 | yes |
| 2023-08-21 | binance_bt/binance/BTC-USDT/perp | 108,708 | 1.000 | 5.8 | 0 | 6.0 / 13.0 | 0.04 | 144 | no trade record | - | - | yes |
| 2023-08-21 | binance_bt/binance/ETH-USDT/perp | 124,582 | 1.000 | 4.4 | 0 | 6.0 / 12.0 | 0.06 | 158 | no trade record | - | - | yes |
| 2023-08-21 | bybit_ob/bybit/BTC-USDT/perp | 858,464 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 141 | 96.1% | 0 | 0 | yes |
| 2023-08-21 | bybit_ob/bybit/ETH-USDT/perp | 824,810 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 155 | 96.3% | 0 | 0 | yes |
| 2023-08-22 | binance_bt/binance/BTC-USDT/perp | 144,830 | 1.000 | 4.5 | 0 | 6.0 / 13.0 | 0.04 | 205 | no trade record | - | - | yes |
| 2023-08-22 | binance_bt/binance/ETH-USDT/perp | 195,453 | 1.000 | 2.6 | 0 | 6.0 / 12.0 | 0.06 | 250 | no trade record | - | - | yes |
| 2023-08-22 | bybit_ob/bybit/BTC-USDT/perp | 860,829 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 204 | 91.8% | 1 | 0 | yes |
| 2023-08-22 | bybit_ob/bybit/ETH-USDT/perp | 831,823 | 1.000 | 0.8 | 0 | 0.0 / 0.0 | 0.06 | 248 | 90.7% | 0 | 0 | yes |
| 2023-08-23 | binance_bt/binance/BTC-USDT/perp | 180,731 | 1.000 | 3.3 | 0 | 6.0 / 14.0 | 0.04 | 209 | no trade record | - | - | yes |
| 2023-08-23 | binance_bt/binance/ETH-USDT/perp | 204,925 | 1.000 | 4.3 | 0 | 6.0 / 14.0 | 0.06 | 236 | no trade record | - | - | yes |
| 2023-08-23 | bybit_ob/bybit/BTC-USDT/perp | 863,036 | 1.000 | 1.5 | 0 | 0.0 / 0.0 | 0.04 | 207 | 94.5% | 0 | 0 | yes |
| 2023-08-23 | bybit_ob/bybit/ETH-USDT/perp | 854,065 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 233 | 94.7% | 0 | 0 | yes |
| 2023-08-24 | binance_bt/binance/BTC-USDT/perp | 123,897 | 1.000 | 2.9 | 0 | 6.0 / 14.0 | 0.04 | 147 | no trade record | - | - | yes |
| 2023-08-24 | binance_bt/binance/ETH-USDT/perp | 112,880 | 1.000 | 2.1 | 0 | 6.0 / 13.0 | 0.06 | 158 | no trade record | - | - | yes |
| 2023-08-24 | bybit_ob/bybit/BTC-USDT/perp | 861,855 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 147 | 94.4% | 1 | 0 | yes |
| 2023-08-24 | bybit_ob/bybit/ETH-USDT/perp | 852,355 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 158 | 96.2% | 0 | 0 | yes |
| 2023-08-25 | binance_bt/binance/BTC-USDT/perp | 130,420 | 1.000 | 2.8 | 0 | 6.0 / 13.0 | 0.04 | 160 | no trade record | - | - | yes |
| 2023-08-25 | binance_bt/binance/ETH-USDT/perp | 146,685 | 1.000 | 2.0 | 0 | 6.0 / 13.0 | 0.06 | 199 | no trade record | - | - | yes |
| 2023-08-25 | bybit_ob/bybit/BTC-USDT/perp | 860,405 | 1.000 | 1.5 | 0 | 0.0 / 0.0 | 0.04 | 159 | 95.6% | 1 | 0 | yes |
| 2023-08-25 | bybit_ob/bybit/ETH-USDT/perp | 854,678 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 200 | 94.6% | 0 | 0 | yes |
| 2023-08-26 | binance_bt/binance/BTC-USDT/perp | 16,827 | 1.000 | 1.8 | 0 | 6.0 / 25.0 | 0.04 | 59 | no trade record | - | - | yes |
| 2023-08-26 | binance_bt/binance/ETH-USDT/perp | 22,530 | 1.000 | 2.6 | 0 | 6.0 / 19.0 | 0.06 | 72 | no trade record | - | - | yes |
| 2023-08-26 | bybit_ob/bybit/BTC-USDT/perp | 857,535 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 53 | 98.0% | 0 | 0 | yes |
| 2023-08-26 | bybit_ob/bybit/ETH-USDT/perp | 845,218 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 67 | 97.7% | 1 | 0 | yes |
| 2023-08-27 | binance_bt/binance/BTC-USDT/perp | 22,868 | 1.000 | 1.2 | 0 | 6.0 / 13.0 | 0.04 | 71 | no trade record | - | - | yes |
| 2023-08-27 | binance_bt/binance/ETH-USDT/perp | 32,771 | 1.000 | 2.7 | 0 | 6.0 / 12.0 | 0.06 | 86 | no trade record | - | - | yes |
| 2023-08-27 | bybit_ob/bybit/BTC-USDT/perp | 859,295 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 64 | 98.3% | 0 | 0 | yes |
| 2023-08-27 | bybit_ob/bybit/ETH-USDT/perp | 835,153 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 82 | 96.1% | 1 | 0 | yes |
| 2023-08-28 | binance_bt/binance/BTC-USDT/perp | 86,393 | 1.000 | 4.1 | 0 | 6.0 / 13.0 | 0.04 | 134 | no trade record | - | - | yes |
| 2023-08-28 | binance_bt/binance/ETH-USDT/perp | 111,383 | 1.000 | 4.6 | 0 | 6.0 / 13.0 | 0.06 | 175 | no trade record | - | - | yes |
| 2023-08-28 | bybit_ob/bybit/BTC-USDT/perp | 862,284 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 132 | 95.5% | 1 | 0 | yes |
| 2023-08-28 | bybit_ob/bybit/ETH-USDT/perp | 854,215 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 174 | 92.6% | 1 | 0 | yes |
| 2023-08-29 | binance_bt/binance/BTC-USDT/perp | 424,105 | 1.000 | 2.8 | 0 | 6.0 / 13.0 | 0.07 | 388 | no trade record | - | - | yes |
| 2023-08-29 | binance_bt/binance/ETH-USDT/perp | 352,636 | 1.000 | 3.9 | 0 | 6.0 / 12.0 | 0.12 | 315 | no trade record | - | - | yes |
| 2023-08-29 | bybit_ob/bybit/BTC-USDT/perp | 863,191 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 380 | 88.3% | 1 | 0 | yes |
| 2023-08-29 | bybit_ob/bybit/ETH-USDT/perp | 857,484 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 305 | 90.3% | 0 | 0 | yes |
| 2023-08-30 | binance_bt/binance/BTC-USDT/perp | 156,728 | 1.000 | 4.3 | 0 | 6.0 / 15.0 | 0.04 | 190 | no trade record | - | - | yes |
| 2023-08-30 | binance_bt/binance/ETH-USDT/perp | 121,962 | 1.000 | 3.8 | 0 | 6.0 / 15.0 | 0.06 | 172 | no trade record | - | - | yes |
| 2023-08-30 | bybit_ob/bybit/BTC-USDT/perp | 863,064 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 188 | 93.4% | 0 | 0 | yes |
| 2023-08-30 | bybit_ob/bybit/ETH-USDT/perp | 855,247 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 172 | 95.5% | 1 | 0 | yes |
| 2023-08-31 | binance_bt/binance/BTC-USDT/perp | 282,278 | 1.000 | 4.3 | 0 | 6.0 / 16.0 | 0.04 | 273 | no trade record | - | - | yes |
| 2023-08-31 | binance_bt/binance/ETH-USDT/perp | 214,974 | 1.000 | 4.3 | 0 | 6.0 / 14.0 | 0.06 | 239 | no trade record | - | - | yes |
| 2023-08-31 | bybit_ob/bybit/BTC-USDT/perp | 862,732 | 1.000 | 1.5 | 0 | 0.0 / 0.0 | 0.04 | 271 | 87.7% | 1 | 0 | yes |
| 2023-08-31 | bybit_ob/bybit/ETH-USDT/perp | 851,269 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 236 | 93.6% | 0 | 0 | yes |
| 2023-09-01 | binance_bt/binance/BTC-USDT/perp | 200,912 | 1.000 | 3.2 | 0 | 6.0 / 19.0 | 0.04 | 211 | no trade record | - | - | yes |
| 2023-09-01 | binance_bt/binance/ETH-USDT/perp | 192,434 | 1.000 | 4.1 | 0 | 6.0 / 16.0 | 0.06 | 206 | no trade record | - | - | yes |
| 2023-09-01 | bybit_ob/bybit/BTC-USDT/perp | 862,354 | 1.000 | 1.5 | 0 | 0.0 / 0.0 | 0.04 | 218 | 93.4% | 0 | 0 | yes |
| 2023-09-01 | bybit_ob/bybit/ETH-USDT/perp | 852,496 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 205 | 93.9% | 1 | 0 | yes |
| 2023-09-02 | binance_bt/binance/BTC-USDT/perp | 40,418 | 1.000 | 4.1 | 0 | 7.0 / 17.0 | 0.04 | 89 | no trade record | - | - | yes |
| 2023-09-02 | binance_bt/binance/ETH-USDT/perp | 44,856 | 1.000 | 3.6 | 0 | 6.0 / 15.0 | 0.06 | 102 | no trade record | - | - | yes |
| 2023-09-02 | bybit_ob/bybit/BTC-USDT/perp | 860,426 | 1.000 | 1.5 | 0 | 0.0 / 0.0 | 0.04 | 84 | 97.6% | 0 | 0 | yes |
| 2023-09-02 | bybit_ob/bybit/ETH-USDT/perp | 847,395 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 101 | 98.3% | 0 | 0 | yes |
| 2023-09-03 | binance_bt/binance/BTC-USDT/perp | 62,897 | 1.000 | 4.0 | 0 | 6.0 / 22.0 | 0.04 | 117 | no trade record | - | - | yes |
| 2023-09-03 | binance_bt/binance/ETH-USDT/perp | 55,050 | 1.000 | 4.2 | 0 | 6.0 / 21.0 | 0.06 | 115 | no trade record | - | - | yes |
| 2023-09-03 | bybit_ob/bybit/BTC-USDT/perp | 860,719 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 114 | 95.2% | 0 | 0 | yes |
| 2023-09-03 | bybit_ob/bybit/ETH-USDT/perp | 842,447 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 114 | 96.2% | 0 | 0 | yes |
| 2023-09-04 | binance_bt/binance/BTC-USDT/perp | 92,082 | 1.000 | 3.6 | 0 | 6.0 / 18.0 | 0.04 | 136 | no trade record | - | - | yes |
| 2023-09-04 | binance_bt/binance/ETH-USDT/perp | 82,461 | 1.000 | 2.8 | 0 | 6.0 / 17.0 | 0.06 | 131 | no trade record | - | - | yes |
| 2023-09-04 | bybit_ob/bybit/BTC-USDT/perp | 861,226 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 135 | 96.0% | 1 | 0 | yes |
| 2023-09-04 | bybit_ob/bybit/ETH-USDT/perp | 845,466 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 130 | 95.9% | 1 | 0 | yes |
| 2023-09-05 | binance_bt/binance/BTC-USDT/perp | 97,042 | 1.000 | 5.7 | 0 | 6.0 / 22.0 | 0.04 | 126 | no trade record | - | - | yes |
| 2023-09-05 | binance_bt/binance/ETH-USDT/perp | 102,277 | 1.000 | 3.5 | 0 | 6.0 / 23.0 | 0.06 | 140 | no trade record | - | - | yes |
| 2023-09-05 | bybit_ob/bybit/BTC-USDT/perp | 861,639 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 126 | 95.2% | 0 | 0 | yes |
| 2023-09-05 | bybit_ob/bybit/ETH-USDT/perp | 852,513 | 1.000 | 1.0 | 0 | 0.0 / 0.0 | 0.06 | 141 | 95.2% | 1 | 0 | yes |
| 2023-09-06 | binance_bt/binance/BTC-USDT/perp | 140,323 | 1.000 | 2.0 | 0 | 6.0 / 17.0 | 0.04 | 170 | no trade record | - | - | yes |
| 2023-09-06 | binance_bt/binance/ETH-USDT/perp | 146,963 | 1.000 | 2.2 | 0 | 6.0 / 14.0 | 0.06 | 210 | no trade record | - | - | yes |
| 2023-09-06 | bybit_ob/bybit/BTC-USDT/perp | 860,297 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.04 | 167 | 92.7% | 1 | 0 | yes |
| 2023-09-06 | bybit_ob/bybit/ETH-USDT/perp | 852,759 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 209 | 90.9% | 1 | 0 | yes |
| 2023-09-07 | binance_bt/binance/BTC-USDT/perp | 119,467 | 1.000 | 5.6 | 0 | 7.0 / 45.0 | 0.04 | 165 | no trade record | - | - | yes |
| 2023-09-07 | binance_bt/binance/ETH-USDT/perp | 106,849 | 1.000 | 5.3 | 0 | 6.0 / 42.0 | 0.06 | 148 | no trade record | - | - | yes |
| 2023-09-07 | bybit_ob/bybit/BTC-USDT/perp | 858,881 | 1.000 | 12.8 | 2 | 0.0 / 0.0 | 0.04 | 163 | 93.1% | 1 | 0 | yes |
| 2023-09-07 | bybit_ob/bybit/ETH-USDT/perp | 843,591 | 1.000 | 15.6 | 2 | 0.0 / 0.0 | 0.06 | 150 | 93.5% | 1 | 0 | yes |
| 2023-09-08 | binance_bt/binance/BTC-USDT/perp | 111,942 | 1.000 | 6.3 | 0 | 7.0 / 51.0 | 0.04 | 164 | no trade record | - | - | yes |
| 2023-09-08 | binance_bt/binance/ETH-USDT/perp | 103,394 | 1.000 | 6.2 | 0 | 6.0 / 53.0 | 0.06 | 147 | no trade record | - | - | yes |
| 2023-09-08 | bybit_ob/bybit/BTC-USDT/perp | 861,372 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 165 | 95.2% | 1 | 0 | yes |
| 2023-09-08 | bybit_ob/bybit/ETH-USDT/perp | 846,983 | 1.000 | 0.6 | 0 | 0.0 / 0.0 | 0.06 | 149 | 95.9% | 2 | 0 | yes |
| 2023-09-09 | binance_bt/binance/BTC-USDT/perp | 16,825 | 1.000 | 6.9 | 0 | 7.0 / 90.0 | 0.04 | 62 | no trade record | - | - | yes |
| 2023-09-09 | binance_bt/binance/ETH-USDT/perp | 17,716 | 1.000 | 6.9 | 0 | 6.0 / 87.0 | 0.06 | 55 | no trade record | - | - | yes |
| 2023-09-09 | bybit_ob/bybit/BTC-USDT/perp | 855,714 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 57 | 97.9% | 1 | 0 | yes |
| 2023-09-09 | bybit_ob/bybit/ETH-USDT/perp | 832,456 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 53 | 98.8% | 0 | 0 | yes |
| 2023-09-10 | binance_bt/binance/BTC-USDT/perp | 65,955 | 1.000 | 6.3 | 0 | 7.0 / 63.0 | 0.04 | 119 | no trade record | - | - | yes |
| 2023-09-10 | binance_bt/binance/ETH-USDT/perp | 97,549 | 1.000 | 6.5 | 0 | 6.0 / 50.0 | 0.06 | 151 | no trade record | - | - | yes |
| 2023-09-10 | bybit_ob/bybit/BTC-USDT/perp | 858,851 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 117 | 94.8% | 0 | 0 | yes |
| 2023-09-10 | bybit_ob/bybit/ETH-USDT/perp | 850,954 | 1.000 | 0.5 | 0 | 0.0 / 0.0 | 0.06 | 152 | 93.6% | 1 | 0 | yes |
| 2023-09-11 | binance_bt/binance/BTC-USDT/perp | 252,751 | 1.000 | 3.9 | 0 | 6.0 / 37.0 | 0.04 | 230 | no trade record | - | - | yes |
| 2023-09-11 | binance_bt/binance/ETH-USDT/perp | 278,791 | 1.000 | 4.9 | 0 | 6.0 / 32.0 | 0.06 | 316 | no trade record | - | - | yes |
| 2023-09-11 | bybit_ob/bybit/BTC-USDT/perp | 861,945 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 227 | 92.5% | 0 | 0 | yes |
| 2023-09-11 | bybit_ob/bybit/ETH-USDT/perp | 855,588 | 1.000 | 0.5 | 0 | 0.0 / 0.0 | 0.06 | 306 | 88.5% | 1 | 0 | yes |
| 2023-09-12 | binance_bt/binance/BTC-USDT/perp | 353,882 | 0.986 | 1191.1 | 0 | 6.0 / 176.0 | 0.04 | 287 | no trade record | - | - | yes |
| 2023-09-12 | binance_bt/binance/ETH-USDT/perp | 273,588 | 0.986 | 1191.2 | 0 | 6.0 / 251.0 | 0.06 | 267 | no trade record | - | - | yes |
| 2023-09-12 | bybit_ob/bybit/BTC-USDT/perp | 861,708 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 286 | 91.6% | 0 | 0 | yes |
| 2023-09-12 | bybit_ob/bybit/ETH-USDT/perp | 857,117 | 1.000 | 0.6 | 0 | 0.0 / 0.0 | 0.06 | 266 | 90.8% | 1 | 0 | yes |
| 2023-09-13 | binance_bt/binance/BTC-USDT/perp | 202,039 | 1.000 | 4.5 | 0 | 6.0 / 40.0 | 0.04 | 194 | no trade record | - | - | yes |
| 2023-09-13 | binance_bt/binance/ETH-USDT/perp | 169,214 | 1.000 | 6.1 | 0 | 6.0 / 39.0 | 0.06 | 213 | no trade record | - | - | yes |
| 2023-09-13 | bybit_ob/bybit/BTC-USDT/perp | 862,578 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 197 | 94.2% | 1 | 0 | yes |
| 2023-09-13 | bybit_ob/bybit/ETH-USDT/perp | 855,960 | 1.000 | 0.6 | 0 | 0.0 / 0.0 | 0.06 | 215 | 92.4% | 2 | 0 | yes |
| 2023-09-14 | binance_bt/binance/BTC-USDT/perp | 194,672 | 1.000 | 4.2 | 0 | 7.0 / 61.0 | 0.04 | 191 | no trade record | - | - | yes |
| 2023-09-14 | binance_bt/binance/ETH-USDT/perp | 159,426 | 1.000 | 3.6 | 0 | 6.0 / 61.0 | 0.06 | 192 | no trade record | - | - | yes |
| 2023-09-14 | bybit_ob/bybit/BTC-USDT/perp | 862,624 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 188 | 92.6% | 1 | 0 | yes |
| 2023-09-14 | bybit_ob/bybit/ETH-USDT/perp | 853,217 | 1.000 | 0.5 | 0 | 0.0 / 0.0 | 0.06 | 193 | 92.7% | 1 | 0 | yes |
| 2023-09-15 | binance_bt/binance/BTC-USDT/perp | 117,516 | 1.000 | 5.9 | 0 | 7.0 / 43.0 | 0.04 | 143 | no trade record | - | - | yes |
| 2023-09-15 | binance_bt/binance/ETH-USDT/perp | 97,167 | 1.000 | 6.0 | 0 | 6.0 / 39.0 | 0.06 | 145 | no trade record | - | - | yes |
| 2023-09-15 | bybit_ob/bybit/BTC-USDT/perp | 862,149 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 143 | 96.6% | 0 | 0 | yes |
| 2023-09-15 | bybit_ob/bybit/ETH-USDT/perp | 848,544 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 144 | 95.0% | 1 | 0 | yes |
| 2023-09-16 | binance_bt/binance/BTC-USDT/perp | 47,410 | 1.000 | 5.0 | 0 | 7.0 / 39.0 | 0.04 | 94 | no trade record | - | - | yes |
| 2023-09-16 | binance_bt/binance/ETH-USDT/perp | 49,279 | 1.000 | 5.0 | 0 | 6.0 / 35.0 | 0.06 | 100 | no trade record | - | - | yes |
| 2023-09-16 | bybit_ob/bybit/BTC-USDT/perp | 862,340 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 90 | 98.7% | 0 | 0 | yes |
| 2023-09-16 | bybit_ob/bybit/ETH-USDT/perp | 843,116 | 1.000 | 0.6 | 0 | 0.0 / 0.0 | 0.06 | 97 | 98.3% | 0 | 0 | yes |
| 2023-09-17 | binance_bt/binance/BTC-USDT/perp | 33,595 | 1.000 | 6.3 | 0 | 7.0 / 69.1 | 0.04 | 72 | no trade record | - | - | yes |
| 2023-09-17 | binance_bt/binance/ETH-USDT/perp | 55,869 | 1.000 | 4.3 | 0 | 6.0 / 49.0 | 0.06 | 108 | no trade record | - | - | yes |
| 2023-09-17 | bybit_ob/bybit/BTC-USDT/perp | 862,325 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 71 | 98.6% | 1 | 0 | yes |
| 2023-09-17 | bybit_ob/bybit/ETH-USDT/perp | 828,349 | 1.000 | 0.6 | 0 | 0.0 / 0.0 | 0.06 | 107 | 95.3% | 1 | 0 | yes |
| 2023-09-18 | binance_bt/binance/BTC-USDT/perp | 242,964 | 1.000 | 2.1 | 0 | 7.0 / 47.0 | 0.04 | 206 | no trade record | - | - | yes |
| 2023-09-18 | binance_bt/binance/ETH-USDT/perp | 174,049 | 1.000 | 3.5 | 0 | 6.0 / 47.0 | 0.06 | 190 | no trade record | - | - | yes |
| 2023-09-18 | bybit_ob/bybit/BTC-USDT/perp | 863,524 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 205 | 93.0% | 1 | 0 | yes |
| 2023-09-18 | bybit_ob/bybit/ETH-USDT/perp | 851,496 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 187 | 95.8% | 0 | 0 | yes |
| 2023-09-19 | binance_bt/binance/BTC-USDT/perp | 217,286 | 1.000 | 2.2 | 0 | 7.0 / 36.0 | 0.04 | 210 | no trade record | - | - | yes |
| 2023-09-19 | binance_bt/binance/ETH-USDT/perp | 120,624 | 1.000 | 3.1 | 0 | 6.0 / 39.0 | 0.06 | 165 | no trade record | - | - | yes |
| 2023-09-19 | bybit_ob/bybit/BTC-USDT/perp | 863,165 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 208 | 94.8% | 0 | 0 | yes |
| 2023-09-19 | bybit_ob/bybit/ETH-USDT/perp | 848,980 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 165 | 96.9% | 1 | 0 | yes |
| 2023-09-20 | binance_bt/binance/BTC-USDT/perp | 197,635 | 1.000 | 4.3 | 0 | 6.0 / 20.0 | 0.04 | 192 | no trade record | - | - | yes |
| 2023-09-20 | binance_bt/binance/ETH-USDT/perp | 139,583 | 1.000 | 4.2 | 0 | 6.0 / 21.0 | 0.06 | 195 | no trade record | - | - | yes |
| 2023-09-20 | bybit_ob/bybit/BTC-USDT/perp | 863,180 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 195 | 93.6% | 0 | 0 | yes |
| 2023-09-20 | bybit_ob/bybit/ETH-USDT/perp | 849,552 | 1.000 | 0.6 | 0 | 0.0 / 0.0 | 0.06 | 196 | 95.3% | 0 | 0 | yes |
| 2023-09-21 | binance_bt/binance/BTC-USDT/perp | 156,007 | 0.924 | 6328.7 | 0 | 6.0 / 18.0 | 0.04 | 159 | no trade record | - | - | NO |
| 2023-09-21 | binance_bt/binance/ETH-USDT/perp | 134,898 | 0.924 | 6328.7 | 0 | 6.0 / 17.0 | 0.06 | 198 | no trade record | - | - | NO |
| 2023-09-21 | bybit_ob/bybit/BTC-USDT/perp | 863,245 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 158 | 93.9% | 1 | 0 | yes |
| 2023-09-21 | bybit_ob/bybit/ETH-USDT/perp | 854,718 | 1.000 | 0.5 | 0 | 0.0 / 0.0 | 0.06 | 194 | 93.4% | 1 | 0 | yes |
| 2023-09-22 | binance_bt/binance/BTC-USDT/perp | 50,816 | 0.778 | 19190.7 | 0 | 6.0 / 19.0 | 0.04 | 96 | no trade record | - | - | NO |
| 2023-09-22 | binance_bt/binance/ETH-USDT/perp | 56,783 | 0.778 | 19191.1 | 0 | 6.0 / 15.0 | 0.06 | 114 | no trade record | - | - | NO |
| 2023-09-22 | bybit_ob/bybit/BTC-USDT/perp | 862,839 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 113 | 97.2% | 1 | 0 | yes |
| 2023-09-22 | bybit_ob/bybit/ETH-USDT/perp | 854,775 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 135 | 94.9% | 1 | 0 | yes |
| 2023-09-23 | binance_bt/binance/BTC-USDT/perp | 15,228 | 1.000 | 4.0 | 0 | 6.0 / 16.0 | 0.04 | 52 | no trade record | - | - | yes |
| 2023-09-23 | binance_bt/binance/ETH-USDT/perp | 19,720 | 1.000 | 4.3 | 0 | 6.0 / 15.0 | 0.06 | 69 | no trade record | - | - | yes |
| 2023-09-23 | bybit_ob/bybit/BTC-USDT/perp | 860,460 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 45 | 98.5% | 0 | 0 | yes |
| 2023-09-23 | bybit_ob/bybit/ETH-USDT/perp | 829,542 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 65 | 99.1% | 0 | 0 | yes |
| 2023-09-24 | binance_bt/binance/BTC-USDT/perp | 58,984 | 1.000 | 4.8 | 0 | 6.0 / 21.0 | 0.04 | 143 | no trade record | - | - | yes |
| 2023-09-24 | binance_bt/binance/ETH-USDT/perp | 53,908 | 1.000 | 3.5 | 0 | 6.0 / 17.0 | 0.06 | 126 | no trade record | - | - | yes |
| 2023-09-24 | bybit_ob/bybit/BTC-USDT/perp | 860,742 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 138 | 91.5% | 0 | 0 | yes |
| 2023-09-24 | bybit_ob/bybit/ETH-USDT/perp | 823,897 | 1.000 | 0.8 | 0 | 0.0 / 0.0 | 0.06 | 127 | 95.8% | 0 | 0 | yes |
| 2023-09-25 | binance_bt/binance/BTC-USDT/perp | 114,773 | 1.000 | 3.4 | 0 | 6.0 / 16.0 | 0.04 | 151 | no trade record | - | - | yes |
| 2023-09-25 | binance_bt/binance/ETH-USDT/perp | 108,814 | 1.000 | 4.4 | 0 | 6.0 / 14.0 | 0.06 | 168 | no trade record | - | - | yes |
| 2023-09-25 | bybit_ob/bybit/BTC-USDT/perp | 863,110 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 148 | 94.6% | 0 | 0 | yes |
| 2023-09-25 | bybit_ob/bybit/ETH-USDT/perp | 853,106 | 1.000 | 0.8 | 0 | 0.0 / 0.0 | 0.06 | 164 | 80.7% | 1 | 0 | yes |
| 2023-09-26 | binance_bt/binance/BTC-USDT/perp | 66,428 | 1.000 | 5.0 | 0 | 6.0 / 20.0 | 0.04 | 112 | no trade record | - | - | yes |
| 2023-09-26 | binance_bt/binance/ETH-USDT/perp | 83,718 | 1.000 | 5.0 | 0 | 6.0 / 17.0 | 0.06 | 131 | no trade record | - | - | yes |
| 2023-09-26 | bybit_ob/bybit/BTC-USDT/perp | 862,673 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 110 | 93.2% | 1 | 0 | yes |
| 2023-09-26 | bybit_ob/bybit/ETH-USDT/perp | 852,627 | 1.000 | 0.6 | 0 | 0.0 / 0.0 | 0.06 | 129 | 97.3% | 0 | 0 | yes |
| 2023-09-27 | binance_bt/binance/BTC-USDT/perp | 142,771 | 1.000 | 5.0 | 0 | 6.0 / 16.0 | 0.04 | 167 | no trade record | - | - | yes |
| 2023-09-27 | binance_bt/binance/ETH-USDT/perp | 139,566 | 1.000 | 5.0 | 0 | 6.0 / 15.0 | 0.06 | 179 | no trade record | - | - | yes |
| 2023-09-27 | bybit_ob/bybit/BTC-USDT/perp | 863,096 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 165 | 93.6% | 1 | 0 | yes |
| 2023-09-27 | bybit_ob/bybit/ETH-USDT/perp | 855,011 | 1.000 | 0.5 | 0 | 0.0 / 0.0 | 0.06 | 177 | 93.8% | 0 | 0 | yes |
| 2023-09-28 | binance_bt/binance/BTC-USDT/perp | 208,919 | 1.000 | 5.5 | 0 | 6.0 / 15.0 | 0.04 | 204 | no trade record | - | - | yes |
| 2023-09-28 | binance_bt/binance/ETH-USDT/perp | 204,269 | 1.000 | 5.5 | 0 | 6.0 / 13.0 | 0.06 | 213 | no trade record | - | - | yes |
| 2023-09-28 | bybit_ob/bybit/BTC-USDT/perp | 863,281 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 203 | 92.1% | 1 | 0 | yes |
| 2023-09-28 | bybit_ob/bybit/ETH-USDT/perp | 858,407 | 1.000 | 0.5 | 0 | 0.0 / 0.0 | 0.06 | 210 | 92.5% | 1 | 0 | yes |
| 2023-09-29 | binance_bt/binance/BTC-USDT/perp | 151,245 | 1.000 | 3.4 | 0 | 6.0 / 16.0 | 0.04 | 174 | no trade record | - | - | yes |
| 2023-09-29 | binance_bt/binance/ETH-USDT/perp | 160,157 | 1.000 | 4.8 | 0 | 6.0 / 14.0 | 0.06 | 199 | no trade record | - | - | yes |
| 2023-09-29 | bybit_ob/bybit/BTC-USDT/perp | 863,327 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 173 | 93.8% | 0 | 0 | yes |
| 2023-09-29 | bybit_ob/bybit/ETH-USDT/perp | 855,644 | 1.000 | 0.5 | 0 | 0.0 / 0.0 | 0.06 | 196 | 91.9% | 1 | 0 | yes |
| 2023-09-30 | binance_bt/binance/BTC-USDT/perp | 37,107 | 1.000 | 3.7 | 0 | 6.0 / 15.0 | 0.04 | 81 | no trade record | - | - | yes |
| 2023-09-30 | binance_bt/binance/ETH-USDT/perp | 72,906 | 1.000 | 4.5 | 0 | 6.0 / 12.0 | 0.06 | 138 | no trade record | - | - | yes |
| 2023-09-30 | bybit_ob/bybit/BTC-USDT/perp | 861,988 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 74 | 97.3% | 0 | 0 | yes |
| 2023-09-30 | bybit_ob/bybit/ETH-USDT/perp | 848,391 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 136 | 93.6% | 0 | 0 | yes |
| 2023-10-01 | binance_bt/binance/AAVE-USDT/perp | 54,917 | 0.948 | 22.7 | 0 | 5.0 / 10.0 | 1.45 | 389 | no trade record | - | - | NO |
| 2023-10-01 | binance_bt/binance/ARB-USDT/perp | 100,726 | 1.000 | 6.8 | 0 | 5.0 / 11.0 | 1.07 | 476 | no trade record | - | - | yes |
| 2023-10-01 | binance_bt/binance/BTC-USDT/perp | 144,009 | 1.000 | 3.6 | 0 | 6.0 / 25.0 | 0.04 | 354 | no trade record | - | - | yes |
| 2023-10-01 | binance_bt/binance/DOGE-USDT/perp | 11,914 | 1.000 | 4.7 | 0 | 6.0 / 19.9 | 1.61 | 180 | no trade record | - | - | yes |
| 2023-10-01 | binance_bt/binance/ETH-USDT/perp | 179,987 | 1.000 | 4.7 | 0 | 6.0 / 18.0 | 0.06 | 548 | no trade record | - | - | yes |
| 2023-10-01 | binance_bt/binance/SOL-USDT/perp | 345,925 | 1.000 | 4.8 | 0 | 5.0 / 10.0 | 0.83 | 736 | no trade record | - | - | yes |
| 2023-10-01 | binance_bt/binance/WLD-USDT/perp | 328,120 | 1.000 | 4.4 | 0 | 5.0 / 8.0 | 0.60 | 544 | no trade record | - | - | yes |
| 2023-10-01 | binance_bt/binance/XRP-USDT/perp | 8,509 | 1.000 | 4.5 | 0 | 6.0 / 16.0 | 1.93 | 191 | no trade record | - | - | yes |
| 2023-10-01 | binance_bt/binance/ZEC-USDT/perp | 6,413 | 0.792 | 44.9 | 0 | 5.0 / 12.0 | 3.66 | 241 | no trade record | - | - | NO |
| 2023-10-01 | bybit_ob/bybit/AAVE-USDT/perp | 342,194 | 0.963 | 8.4 | 0 | 0.0 / 0.0 | 1.45 | 388 | 91.8% | 1 | 0 | yes |
| 2023-10-01 | bybit_ob/bybit/ARB-USDT/perp | 707,845 | 1.000 | 2.6 | 0 | 0.0 / 0.0 | 1.06 | 473 | 93.0% | 1 | 0 | yes |
| 2023-10-01 | bybit_ob/bybit/BTC-USDT/perp | 862,784 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 390 | 88.8% | 0 | 0 | yes |
| 2023-10-01 | bybit_ob/bybit/DOGE-USDT/perp | 524,000 | 1.000 | 3.1 | 0 | 0.0 / 0.0 | 1.61 | 176 | 97.2% | 0 | 20 | yes |
| 2023-10-01 | bybit_ob/bybit/ETH-USDT/perp | 850,056 | 1.000 | 0.5 | 0 | 0.0 / 0.0 | 0.06 | 556 | 88.1% | 1 | 0 | yes |
| 2023-10-01 | bybit_ob/bybit/SOL-USDT/perp | 777,999 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.44 | 716 | 88.8% | 0 | 0 | yes |
| 2023-10-01 | bybit_ob/bybit/WLD-USDT/perp | 479,718 | 0.999 | 5.3 | 0 | 0.0 / 0.0 | 5.88 | 543 | 95.4% | 0 | 20 | yes |
| 2023-10-01 | bybit_ob/bybit/XRP-USDT/perp | 587,029 | 1.000 | 2.4 | 0 | 0.0 / 0.0 | 1.93 | 187 | 97.5% | 1 | 20 | yes |
| 2023-10-01 | bybit_ob/bybit/ZEC-USDT/perp | 88,328 | 0.556 | 32.1 | 0 | 0.0 / 0.0 | 18.26 | 273 | 97.2% | 1 | 500 | NO |
| 2023-10-02 | binance_bt/binance/AAVE-USDT/perp | 67,844 | 0.974 | 15.3 | 0 | 5.0 / 15.0 | 1.45 | 401 | no trade record | - | - | yes |
| 2023-10-02 | binance_bt/binance/ARB-USDT/perp | 111,286 | 1.000 | 6.6 | 0 | 5.0 / 15.0 | 1.07 | 493 | no trade record | - | - | yes |
| 2023-10-02 | binance_bt/binance/BTC-USDT/perp | 351,788 | 1.000 | 4.7 | 0 | 6.0 / 18.0 | 0.04 | 279 | no trade record | - | - | yes |
| 2023-10-02 | binance_bt/binance/DOGE-USDT/perp | 22,018 | 1.000 | 4.2 | 0 | 6.0 / 19.0 | 1.62 | 374 | no trade record | - | - | yes |
| 2023-10-02 | binance_bt/binance/ETH-USDT/perp | 310,814 | 1.000 | 3.5 | 0 | 6.0 / 16.0 | 0.06 | 339 | no trade record | - | - | yes |
| 2023-10-02 | binance_bt/binance/SOL-USDT/perp | 385,654 | 1.000 | 3.5 | 0 | 5.0 / 12.0 | 0.43 | 617 | no trade record | - | - | yes |
| 2023-10-02 | binance_bt/binance/WLD-USDT/perp | 278,005 | 1.000 | 4.3 | 0 | 5.0 / 11.0 | 0.61 | 635 | no trade record | - | - | yes |
| 2023-10-02 | binance_bt/binance/XRP-USDT/perp | 18,733 | 1.000 | 4.8 | 0 | 6.0 / 25.0 | 1.95 | 413 | no trade record | - | - | yes |
| 2023-10-02 | binance_bt/binance/ZEC-USDT/perp | 9,493 | 0.821 | 41.2 | 0 | 5.0 / 15.0 | 3.67 | 350 | no trade record | - | - | NO |
| 2023-10-02 | bybit_ob/bybit/AAVE-USDT/perp | 424,474 | 0.986 | 5.4 | 0 | 0.0 / 0.0 | 1.44 | 380 | 91.2% | 1 | 0 | yes |
| 2023-10-02 | bybit_ob/bybit/ARB-USDT/perp | 767,664 | 1.000 | 1.6 | 0 | 0.0 / 0.0 | 1.04 | 482 | 91.7% | 1 | 0 | yes |
| 2023-10-02 | bybit_ob/bybit/BTC-USDT/perp | 863,588 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 279 | 90.5% | 1 | 0 | yes |
| 2023-10-02 | bybit_ob/bybit/DOGE-USDT/perp | 579,412 | 1.000 | 3.0 | 0 | 0.0 / 0.0 | 1.58 | 340 | 91.8% | 1 | 20 | yes |
| 2023-10-02 | bybit_ob/bybit/ETH-USDT/perp | 858,163 | 1.000 | 0.5 | 0 | 0.0 / 0.0 | 0.06 | 334 | 90.5% | 1 | 0 | yes |
| 2023-10-02 | bybit_ob/bybit/SOL-USDT/perp | 832,230 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.42 | 599 | 91.2% | 0 | 0 | yes |
| 2023-10-02 | bybit_ob/bybit/WLD-USDT/perp | 471,198 | 0.999 | 5.0 | 0 | 0.0 / 0.0 | 5.91 | 639 | 95.5% | 0 | 50 | NO |
| 2023-10-02 | bybit_ob/bybit/XRP-USDT/perp | 628,819 | 1.000 | 2.0 | 0 | 0.0 / 0.0 | 1.92 | 417 | 95.4% | 0 | 20 | yes |
| 2023-10-02 | bybit_ob/bybit/ZEC-USDT/perp | 104,312 | 0.647 | 24.2 | 0 | 0.0 / 0.0 | 17.97 | 384 | 99.1% | 1 | 0 | NO |
| 2023-10-03 | binance_bt/binance/AAVE-USDT/perp | 64,358 | 0.962 | 20.0 | 0 | 5.0 / 11.0 | 1.54 | 365 | no trade record | - | - | yes |
| 2023-10-03 | binance_bt/binance/ARB-USDT/perp | 65,962 | 1.000 | 6.0 | 0 | 5.0 / 13.0 | 1.10 | 342 | no trade record | - | - | yes |
| 2023-10-03 | binance_bt/binance/BTC-USDT/perp | 184,796 | 1.000 | 3.9 | 0 | 6.0 / 17.0 | 0.04 | 176 | no trade record | - | - | yes |
| 2023-10-03 | binance_bt/binance/DOGE-USDT/perp | 10,265 | 1.000 | 4.4 | 0 | 6.0 / 22.0 | 1.63 | 156 | no trade record | - | - | yes |
| 2023-10-03 | binance_bt/binance/ETH-USDT/perp | 174,906 | 1.000 | 4.0 | 0 | 6.0 / 15.0 | 0.06 | 178 | no trade record | - | - | yes |
| 2023-10-03 | binance_bt/binance/SOL-USDT/perp | 365,969 | 1.000 | 4.3 | 0 | 5.0 / 11.0 | 0.43 | 504 | no trade record | - | - | yes |
| 2023-10-03 | binance_bt/binance/WLD-USDT/perp | 211,274 | 1.000 | 4.4 | 0 | 5.0 / 10.0 | 0.64 | 480 | no trade record | - | - | yes |
| 2023-10-03 | binance_bt/binance/XRP-USDT/perp | 31,179 | 1.000 | 3.9 | 0 | 5.0 / 12.0 | 1.95 | 478 | no trade record | - | - | yes |
| 2023-10-03 | binance_bt/binance/ZEC-USDT/perp | 6,558 | 0.822 | 44.0 | 0 | 5.0 / 11.0 | 3.70 | 250 | no trade record | - | - | NO |
| 2023-10-03 | bybit_ob/bybit/AAVE-USDT/perp | 408,174 | 0.979 | 6.6 | 0 | 0.0 / 0.0 | 1.51 | 361 | 89.9% | 1 | 0 | yes |
| 2023-10-03 | bybit_ob/bybit/ARB-USDT/perp | 719,844 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 1.09 | 329 | 92.8% | 1 | 0 | yes |
| 2023-10-03 | bybit_ob/bybit/BTC-USDT/perp | 863,023 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 175 | 93.8% | 1 | 0 | yes |
| 2023-10-03 | bybit_ob/bybit/DOGE-USDT/perp | 538,853 | 1.000 | 3.3 | 0 | 0.0 / 0.0 | 1.62 | 151 | 98.5% | 0 | 0 | yes |
| 2023-10-03 | bybit_ob/bybit/ETH-USDT/perp | 847,237 | 1.000 | 0.6 | 0 | 0.0 / 0.0 | 0.06 | 171 | 96.3% | 1 | 0 | yes |
| 2023-10-03 | bybit_ob/bybit/SOL-USDT/perp | 797,457 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 0.42 | 505 | 91.3% | 1 | 0 | yes |
| 2023-10-03 | bybit_ob/bybit/WLD-USDT/perp | 430,221 | 0.999 | 4.9 | 0 | 0.0 / 0.0 | 6.14 | 469 | 98.7% | 0 | 20 | yes |
| 2023-10-03 | bybit_ob/bybit/XRP-USDT/perp | 579,497 | 1.000 | 2.7 | 0 | 0.0 / 0.0 | 1.96 | 483 | 94.4% | 0 | 20 | yes |
| 2023-10-03 | bybit_ob/bybit/ZEC-USDT/perp | 96,961 | 0.614 | 25.5 | 0 | 0.0 / 0.0 | 18.37 | 300 | 99.1% | 0 | 0 | NO |
| 2023-10-04 | binance_bt/binance/AAVE-USDT/perp | 49,822 | 0.968 | 22.6 | 0 | 5.0 / 11.0 | 1.56 | 337 | no trade record | - | - | yes |
| 2023-10-04 | binance_bt/binance/ARB-USDT/perp | 83,572 | 0.999 | 7.2 | 0 | 5.0 / 12.0 | 1.15 | 407 | no trade record | - | - | yes |
| 2023-10-04 | binance_bt/binance/BTC-USDT/perp | 167,213 | 1.000 | 4.0 | 0 | 6.0 / 14.0 | 0.04 | 167 | no trade record | - | - | yes |
| 2023-10-04 | binance_bt/binance/DOGE-USDT/perp | 12,745 | 1.000 | 3.9 | 0 | 6.0 / 16.0 | 1.65 | 187 | no trade record | - | - | yes |
| 2023-10-04 | binance_bt/binance/ETH-USDT/perp | 184,805 | 1.000 | 3.4 | 0 | 6.0 / 13.0 | 0.06 | 204 | no trade record | - | - | yes |
| 2023-10-04 | binance_bt/binance/SOL-USDT/perp | 297,031 | 1.000 | 4.5 | 0 | 5.0 / 10.0 | 0.44 | 480 | no trade record | - | - | yes |
| 2023-10-04 | binance_bt/binance/WLD-USDT/perp | 228,992 | 1.000 | 5.6 | 0 | 5.0 / 9.0 | 0.67 | 610 | no trade record | - | - | yes |
| 2023-10-04 | binance_bt/binance/XRP-USDT/perp | 41,442 | 1.000 | 3.5 | 0 | 5.0 / 10.0 | 1.89 | 419 | no trade record | - | - | yes |
| 2023-10-04 | binance_bt/binance/ZEC-USDT/perp | 6,956 | 0.817 | 28.6 | 0 | 5.0 / 11.0 | 3.77 | 291 | no trade record | - | - | NO |
| 2023-10-04 | bybit_ob/bybit/AAVE-USDT/perp | 369,687 | 0.977 | 5.7 | 0 | 0.0 / 0.0 | 1.54 | 333 | 93.2% | 1 | 0 | yes |
| 2023-10-04 | bybit_ob/bybit/ARB-USDT/perp | 752,377 | 1.000 | 1.3 | 0 | 0.0 / 0.0 | 1.14 | 395 | 94.0% | 1 | 0 | yes |
| 2023-10-04 | bybit_ob/bybit/BTC-USDT/perp | 862,656 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 166 | 93.2% | 1 | 0 | yes |
| 2023-10-04 | bybit_ob/bybit/DOGE-USDT/perp | 529,475 | 1.000 | 3.1 | 0 | 0.0 / 0.0 | 1.64 | 174 | 96.8% | 1 | 20 | yes |
| 2023-10-04 | bybit_ob/bybit/ETH-USDT/perp | 849,362 | 1.000 | 0.8 | 0 | 0.0 / 0.0 | 0.06 | 196 | 93.1% | 1 | 0 | yes |
| 2023-10-04 | bybit_ob/bybit/SOL-USDT/perp | 806,980 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.43 | 478 | 87.0% | 2 | 0 | yes |
| 2023-10-04 | bybit_ob/bybit/WLD-USDT/perp | 422,781 | 0.997 | 7.2 | 0 | 0.0 / 0.0 | 6.59 | 598 | 98.3% | 0 | 20 | yes |
| 2023-10-04 | bybit_ob/bybit/XRP-USDT/perp | 713,927 | 1.000 | 2.0 | 0 | 0.0 / 0.0 | 1.88 | 420 | 96.0% | 0 | 20 | yes |
| 2023-10-04 | bybit_ob/bybit/ZEC-USDT/perp | 89,505 | 0.593 | 35.5 | 0 | 0.0 / 0.0 | 18.71 | 349 | 99.1% | 0 | 0 | NO |
| 2023-10-05 | binance_bt/binance/AAVE-USDT/perp | 115,416 | 0.997 | 8.7 | 0 | 5.0 / 9.0 | 1.48 | 576 | no trade record | - | - | yes |
| 2023-10-05 | binance_bt/binance/ARB-USDT/perp | 51,975 | 0.999 | 7.3 | 0 | 5.0 / 13.0 | 1.16 | 300 | no trade record | - | - | yes |
| 2023-10-05 | binance_bt/binance/BTC-USDT/perp | 166,543 | 1.000 | 4.0 | 0 | 6.0 / 14.0 | 0.04 | 183 | no trade record | - | - | yes |
| 2023-10-05 | binance_bt/binance/DOGE-USDT/perp | 8,116 | 1.000 | 4.6 | 0 | 6.0 / 17.0 | 1.64 | 133 | no trade record | - | - | yes |
| 2023-10-05 | binance_bt/binance/ETH-USDT/perp | 182,845 | 1.000 | 2.0 | 0 | 6.0 / 12.0 | 0.06 | 182 | no trade record | - | - | yes |
| 2023-10-05 | binance_bt/binance/SOL-USDT/perp | 235,386 | 1.000 | 4.3 | 0 | 5.0 / 11.0 | 0.44 | 395 | no trade record | - | - | yes |
| 2023-10-05 | binance_bt/binance/WLD-USDT/perp | 222,074 | 1.000 | 6.0 | 0 | 5.0 / 9.0 | 0.66 | 427 | no trade record | - | - | yes |
| 2023-10-05 | binance_bt/binance/XRP-USDT/perp | 14,068 | 1.000 | 4.6 | 0 | 5.0 / 14.0 | 1.92 | 252 | no trade record | - | - | yes |
| 2023-10-05 | binance_bt/binance/ZEC-USDT/perp | 5,629 | 0.755 | 37.5 | 0 | 5.0 / 11.0 | 3.70 | 209 | no trade record | - | - | NO |
| 2023-10-05 | bybit_ob/bybit/AAVE-USDT/perp | 494,739 | 0.992 | 5.4 | 0 | 0.0 / 0.0 | 1.45 | 568 | 90.3% | 1 | 0 | yes |
| 2023-10-05 | bybit_ob/bybit/ARB-USDT/perp | 723,822 | 1.000 | 1.6 | 0 | 0.0 / 0.0 | 1.14 | 290 | 91.2% | 2 | 0 | yes |
| 2023-10-05 | bybit_ob/bybit/BTC-USDT/perp | 862,702 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 184 | 92.9% | 1 | 0 | yes |
| 2023-10-05 | bybit_ob/bybit/DOGE-USDT/perp | 520,353 | 1.000 | 3.0 | 0 | 0.0 / 0.0 | 1.64 | 124 | 97.5% | 0 | 20 | yes |
| 2023-10-05 | bybit_ob/bybit/ETH-USDT/perp | 837,614 | 1.000 | 0.9 | 0 | 0.0 / 0.0 | 0.06 | 178 | 94.0% | 1 | 0 | yes |
| 2023-10-05 | bybit_ob/bybit/SOL-USDT/perp | 768,644 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.43 | 397 | 95.0% | 0 | 0 | yes |
| 2023-10-05 | bybit_ob/bybit/WLD-USDT/perp | 418,561 | 0.995 | 7.4 | 0 | 0.0 / 0.0 | 6.46 | 425 | 98.9% | 0 | 20 | yes |
| 2023-10-05 | bybit_ob/bybit/XRP-USDT/perp | 598,703 | 1.000 | 2.3 | 0 | 0.0 / 0.0 | 1.91 | 254 | 97.4% | 0 | 20 | yes |
| 2023-10-05 | bybit_ob/bybit/ZEC-USDT/perp | 86,778 | 0.581 | 23.2 | 0 | 0.0 / 0.0 | 18.43 | 254 | 99.9% | 0 | 0 | NO |
| 2023-10-06 | binance_bt/binance/AAVE-USDT/perp | 41,662 | 0.991 | 10.7 | 0 | 5.0 / 13.0 | 1.48 | 302 | no trade record | - | - | yes |
| 2023-10-06 | binance_bt/binance/ARB-USDT/perp | 46,923 | 0.999 | 7.1 | 0 | 5.0 / 15.0 | 1.15 | 294 | no trade record | - | - | yes |
| 2023-10-06 | binance_bt/binance/BTC-USDT/perp | 220,787 | 1.000 | 7.0 | 0 | 6.0 / 16.0 | 0.04 | 228 | no trade record | - | - | yes |
| 2023-10-06 | binance_bt/binance/DOGE-USDT/perp | 7,045 | 1.000 | 7.7 | 0 | 6.0 / 24.0 | 1.64 | 119 | no trade record | - | - | yes |
| 2023-10-06 | binance_bt/binance/ETH-USDT/perp | 193,545 | 1.000 | 7.1 | 0 | 6.0 / 15.0 | 0.06 | 188 | no trade record | - | - | yes |
| 2023-10-06 | binance_bt/binance/SOL-USDT/perp | 240,092 | 1.000 | 7.1 | 0 | 5.0 / 11.0 | 0.44 | 396 | no trade record | - | - | yes |
| 2023-10-06 | binance_bt/binance/WLD-USDT/perp | 235,150 | 1.000 | 7.9 | 0 | 5.0 / 9.0 | 0.65 | 501 | no trade record | - | - | yes |
| 2023-10-06 | binance_bt/binance/XRP-USDT/perp | 9,083 | 1.000 | 6.0 | 0 | 5.0 / 20.0 | 1.92 | 188 | no trade record | - | - | yes |
| 2023-10-06 | binance_bt/binance/ZEC-USDT/perp | 5,766 | 0.761 | 36.9 | 0 | 5.0 / 14.0 | 3.69 | 213 | no trade record | - | - | NO |
| 2023-10-06 | bybit_ob/bybit/AAVE-USDT/perp | 390,995 | 0.993 | 5.1 | 0 | 0.0 / 0.0 | 1.47 | 296 | 93.1% | 1 | 0 | yes |
| 2023-10-06 | bybit_ob/bybit/ARB-USDT/perp | 714,917 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 1.14 | 286 | 94.3% | 1 | 0 | yes |
| 2023-10-06 | bybit_ob/bybit/BTC-USDT/perp | 862,997 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 227 | 92.7% | 0 | 0 | yes |
| 2023-10-06 | bybit_ob/bybit/DOGE-USDT/perp | 510,854 | 1.000 | 3.3 | 0 | 0.0 / 0.0 | 1.64 | 110 | 98.5% | 1 | 20 | yes |
| 2023-10-06 | bybit_ob/bybit/ETH-USDT/perp | 848,788 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 189 | 92.8% | 1 | 0 | yes |
| 2023-10-06 | bybit_ob/bybit/SOL-USDT/perp | 794,838 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.43 | 396 | 94.3% | 0 | 0 | yes |
| 2023-10-06 | bybit_ob/bybit/WLD-USDT/perp | 422,382 | 0.995 | 5.4 | 0 | 0.0 / 0.0 | 6.42 | 496 | 98.5% | 0 | 20 | yes |
| 2023-10-06 | bybit_ob/bybit/XRP-USDT/perp | 566,325 | 1.000 | 2.1 | 0 | 0.0 / 0.0 | 1.91 | 190 | 97.9% | 0 | 20 | yes |
| 2023-10-06 | bybit_ob/bybit/ZEC-USDT/perp | 90,792 | 0.614 | 20.5 | 0 | 0.0 / 0.0 | 18.40 | 276 | 97.4% | 0 | 20 | NO |
| 2023-10-07 | binance_bt/binance/AAVE-USDT/perp | 28,734 | 0.978 | 17.0 | 0 | 5.0 / 9.0 | 1.51 | 297 | no trade record | - | - | yes |
| 2023-10-07 | binance_bt/binance/ARB-USDT/perp | 24,313 | 0.996 | 9.3 | 0 | 5.0 / 13.0 | 1.14 | 206 | no trade record | - | - | yes |
| 2023-10-07 | binance_bt/binance/BTC-USDT/perp | 52,406 | 1.000 | 3.7 | 0 | 6.0 / 17.0 | 0.04 | 88 | no trade record | - | - | yes |
| 2023-10-07 | binance_bt/binance/DOGE-USDT/perp | 3,068 | 1.000 | 4.7 | 0 | 5.0 / 21.0 | 1.63 | 85 | no trade record | - | - | yes |
| 2023-10-07 | binance_bt/binance/ETH-USDT/perp | 52,579 | 1.000 | 2.6 | 0 | 6.0 / 16.0 | 0.06 | 90 | no trade record | - | - | yes |
| 2023-10-07 | binance_bt/binance/SOL-USDT/perp | 141,538 | 1.000 | 5.1 | 0 | 5.0 / 10.0 | 0.43 | 350 | no trade record | - | - | yes |
| 2023-10-07 | binance_bt/binance/WLD-USDT/perp | 188,887 | 1.000 | 5.9 | 0 | 5.0 / 8.0 | 0.62 | 463 | no trade record | - | - | yes |
| 2023-10-07 | binance_bt/binance/XRP-USDT/perp | 2,827 | 1.000 | 4.6 | 0 | 5.0 / 13.7 | 1.92 | 104 | no trade record | - | - | yes |
| 2023-10-07 | binance_bt/binance/ZEC-USDT/perp | 2,514 | 0.780 | 28.0 | 0 | 5.0 / 10.9 | 3.73 | 165 | no trade record | - | - | NO |
| 2023-10-07 | bybit_ob/bybit/AAVE-USDT/perp | 299,264 | 0.973 | 8.3 | 0 | 0.0 / 0.0 | 1.50 | 295 | 92.5% | 1 | 0 | yes |
| 2023-10-07 | bybit_ob/bybit/ARB-USDT/perp | 663,687 | 1.000 | 2.0 | 0 | 0.0 / 0.0 | 1.14 | 200 | 94.4% | 1 | 0 | yes |
| 2023-10-07 | bybit_ob/bybit/BTC-USDT/perp | 861,960 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 83 | 97.5% | 0 | 0 | yes |
| 2023-10-07 | bybit_ob/bybit/DOGE-USDT/perp | 458,487 | 0.999 | 4.2 | 0 | 0.0 / 0.0 | 1.63 | 75 | 98.9% | 0 | 0 | yes |
| 2023-10-07 | bybit_ob/bybit/ETH-USDT/perp | 838,653 | 1.000 | 0.8 | 0 | 0.0 / 0.0 | 0.06 | 83 | 97.3% | 0 | 0 | yes |
| 2023-10-07 | bybit_ob/bybit/SOL-USDT/perp | 751,251 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.43 | 348 | 95.1% | 0 | 0 | yes |
| 2023-10-07 | bybit_ob/bybit/WLD-USDT/perp | 384,916 | 0.996 | 4.9 | 0 | 0.0 / 0.0 | 6.11 | 460 | 98.6% | 0 | 20 | yes |
| 2023-10-07 | bybit_ob/bybit/XRP-USDT/perp | 474,441 | 1.000 | 4.2 | 0 | 0.0 / 0.0 | 1.92 | 103 | 98.6% | 0 | 20 | yes |
| 2023-10-07 | bybit_ob/bybit/ZEC-USDT/perp | 72,899 | 0.526 | 28.8 | 0 | 0.0 / 0.0 | 18.60 | 213 | 99.5% | 0 | 0 | NO |
| 2023-10-08 | binance_bt/binance/AAVE-USDT/perp | 21,440 | 0.966 | 14.3 | 0 | 5.0 / 11.0 | 1.52 | 214 | no trade record | - | - | yes |
| 2023-10-08 | binance_bt/binance/ARB-USDT/perp | 34,670 | 0.999 | 7.9 | 0 | 5.0 / 12.0 | 1.18 | 261 | no trade record | - | - | yes |
| 2023-10-08 | binance_bt/binance/BTC-USDT/perp | 78,048 | 1.000 | 3.8 | 0 | 6.0 / 14.0 | 0.04 | 117 | no trade record | - | - | yes |
| 2023-10-08 | binance_bt/binance/DOGE-USDT/perp | 3,749 | 1.000 | 3.6 | 0 | 6.0 / 18.0 | 1.64 | 91 | no trade record | - | - | yes |
| 2023-10-08 | binance_bt/binance/ETH-USDT/perp | 96,424 | 1.000 | 2.4 | 0 | 6.0 / 12.0 | 0.06 | 129 | no trade record | - | - | yes |
| 2023-10-08 | binance_bt/binance/SOL-USDT/perp | 116,890 | 1.000 | 4.0 | 0 | 5.0 / 10.0 | 0.43 | 269 | no trade record | - | - | yes |
| 2023-10-08 | binance_bt/binance/WLD-USDT/perp | 124,781 | 0.998 | 7.3 | 0 | 5.0 / 8.0 | 0.63 | 333 | no trade record | - | - | yes |
| 2023-10-08 | binance_bt/binance/XRP-USDT/perp | 3,473 | 1.000 | 2.8 | 0 | 5.0 / 14.0 | 1.93 | 108 | no trade record | - | - | yes |
| 2023-10-08 | binance_bt/binance/ZEC-USDT/perp | 2,992 | 0.737 | 30.4 | 0 | 5.0 / 9.0 | 3.81 | 161 | no trade record | - | - | NO |
| 2023-10-08 | bybit_ob/bybit/AAVE-USDT/perp | 305,446 | 0.975 | 7.7 | 0 | 0.0 / 0.0 | 1.52 | 209 | 93.0% | 1 | 0 | yes |
| 2023-10-08 | bybit_ob/bybit/ARB-USDT/perp | 679,255 | 1.000 | 2.8 | 0 | 0.0 / 0.0 | 1.17 | 249 | 95.0% | 0 | 0 | yes |
| 2023-10-08 | bybit_ob/bybit/BTC-USDT/perp | 862,778 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 114 | 95.3% | 1 | 0 | yes |
| 2023-10-08 | bybit_ob/bybit/DOGE-USDT/perp | 490,117 | 1.000 | 3.6 | 0 | 0.0 / 0.0 | 1.64 | 83 | 98.5% | 0 | 20 | yes |
| 2023-10-08 | bybit_ob/bybit/ETH-USDT/perp | 844,275 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 123 | 95.9% | 1 | 0 | yes |
| 2023-10-08 | bybit_ob/bybit/SOL-USDT/perp | 734,545 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.43 | 270 | 95.8% | 1 | 0 | yes |
| 2023-10-08 | bybit_ob/bybit/WLD-USDT/perp | 359,730 | 0.991 | 6.1 | 0 | 0.0 / 0.0 | 6.30 | 336 | 98.9% | 0 | 20 | yes |
| 2023-10-08 | bybit_ob/bybit/XRP-USDT/perp | 566,277 | 1.000 | 4.3 | 0 | 0.0 / 0.0 | 1.92 | 101 | 98.8% | 0 | 20 | yes |
| 2023-10-08 | bybit_ob/bybit/ZEC-USDT/perp | 78,671 | 0.565 | 21.1 | 0 | 0.0 / 0.0 | 18.85 | 240 | 99.9% | 0 | 0 | NO |
| 2023-10-09 | binance_bt/binance/AAVE-USDT/perp | 53,975 | 0.975 | 13.6 | 0 | 5.0 / 11.0 | 1.59 | 337 | no trade record | - | - | yes |
| 2023-10-09 | binance_bt/binance/ARB-USDT/perp | 81,273 | 1.000 | 8.0 | 0 | 5.0 / 11.0 | 1.25 | 410 | no trade record | - | - | yes |
| 2023-10-09 | binance_bt/binance/BTC-USDT/perp | 164,824 | 1.000 | 2.0 | 0 | 6.0 / 14.0 | 0.04 | 174 | no trade record | - | - | yes |
| 2023-10-09 | binance_bt/binance/DOGE-USDT/perp | 19,881 | 1.000 | 4.6 | 0 | 6.0 / 13.0 | 1.72 | 289 | no trade record | - | - | yes |
| 2023-10-09 | binance_bt/binance/ETH-USDT/perp | 218,270 | 1.000 | 3.1 | 0 | 6.0 / 13.0 | 0.06 | 255 | no trade record | - | - | yes |
| 2023-10-09 | binance_bt/binance/SOL-USDT/perp | 207,286 | 1.000 | 4.5 | 0 | 5.0 / 11.0 | 0.45 | 380 | no trade record | - | - | yes |
| 2023-10-09 | binance_bt/binance/WLD-USDT/perp | 231,751 | 0.998 | 8.3 | 0 | 5.0 / 9.0 | 0.67 | 435 | no trade record | - | - | yes |
| 2023-10-09 | binance_bt/binance/XRP-USDT/perp | 22,081 | 1.000 | 2.0 | 0 | 6.0 / 14.0 | 2.02 | 332 | no trade record | - | - | yes |
| 2023-10-09 | binance_bt/binance/ZEC-USDT/perp | 6,421 | 0.795 | 35.4 | 0 | 5.0 / 11.0 | 3.95 | 305 | no trade record | - | - | NO |
| 2023-10-09 | bybit_ob/bybit/AAVE-USDT/perp | 376,628 | 0.980 | 5.1 | 0 | 0.0 / 0.0 | 1.57 | 342 | 92.4% | 1 | 0 | yes |
| 2023-10-09 | bybit_ob/bybit/ARB-USDT/perp | 685,180 | 1.000 | 2.4 | 0 | 0.0 / 0.0 | 1.22 | 414 | 86.6% | 1 | 0 | yes |
| 2023-10-09 | bybit_ob/bybit/BTC-USDT/perp | 863,511 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 175 | 94.0% | 1 | 0 | yes |
| 2023-10-09 | bybit_ob/bybit/DOGE-USDT/perp | 577,247 | 1.000 | 3.7 | 0 | 0.0 / 0.0 | 1.70 | 323 | 87.0% | 1 | 20 | yes |
| 2023-10-09 | bybit_ob/bybit/ETH-USDT/perp | 853,425 | 1.000 | 1.0 | 0 | 0.0 / 0.0 | 0.06 | 276 | 90.9% | 1 | 0 | yes |
| 2023-10-09 | bybit_ob/bybit/SOL-USDT/perp | 760,801 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.45 | 383 | 93.2% | 1 | 0 | yes |
| 2023-10-09 | bybit_ob/bybit/WLD-USDT/perp | 407,952 | 0.993 | 7.6 | 0 | 0.0 / 0.0 | 6.50 | 444 | 92.2% | 6 | 20 | NO |
| 2023-10-09 | bybit_ob/bybit/XRP-USDT/perp | 653,990 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 1.99 | 379 | 94.3% | 0 | 20 | yes |
| 2023-10-09 | bybit_ob/bybit/ZEC-USDT/perp | 105,220 | 0.675 | 21.6 | 0 | 0.0 / 0.0 | 19.51 | 397 | 95.3% | 0 | 200 | NO |
| 2023-10-10 | binance_bt/binance/AAVE-USDT/perp | 39,966 | 0.968 | 17.9 | 0 | 5.0 / 11.0 | 1.57 | 352 | no trade record | - | - | yes |
| 2023-10-10 | binance_bt/binance/ARB-USDT/perp | 44,451 | 0.999 | 6.7 | 0 | 5.0 / 12.0 | 1.22 | 291 | no trade record | - | - | yes |
| 2023-10-10 | binance_bt/binance/BTC-USDT/perp | 113,889 | 1.000 | 4.1 | 0 | 6.0 / 15.0 | 0.04 | 152 | no trade record | - | - | yes |
| 2023-10-10 | binance_bt/binance/DOGE-USDT/perp | 7,805 | 1.000 | 3.2 | 0 | 6.0 / 17.0 | 1.71 | 150 | no trade record | - | - | yes |
| 2023-10-10 | binance_bt/binance/ETH-USDT/perp | 156,023 | 1.000 | 4.1 | 0 | 6.0 / 13.0 | 0.06 | 190 | no trade record | - | - | yes |
| 2023-10-10 | binance_bt/binance/SOL-USDT/perp | 149,099 | 1.000 | 4.5 | 0 | 5.0 / 11.0 | 0.46 | 318 | no trade record | - | - | yes |
| 2023-10-10 | binance_bt/binance/WLD-USDT/perp | 164,124 | 0.998 | 7.1 | 0 | 5.0 / 9.0 | 0.66 | 350 | no trade record | - | - | yes |
| 2023-10-10 | binance_bt/binance/XRP-USDT/perp | 8,258 | 1.000 | 3.1 | 0 | 5.0 / 14.0 | 2.02 | 190 | no trade record | - | - | yes |
| 2023-10-10 | binance_bt/binance/ZEC-USDT/perp | 3,439 | 0.769 | 32.1 | 0 | 5.0 / 11.0 | 3.92 | 222 | no trade record | - | - | NO |
| 2023-10-10 | bybit_ob/bybit/AAVE-USDT/perp | 397,082 | 0.984 | 11.8 | 2 | 0.0 / 0.0 | 1.56 | 353 | 96.7% | 1 | 0 | yes |
| 2023-10-10 | bybit_ob/bybit/ARB-USDT/perp | 734,281 | 1.000 | 11.8 | 3 | 0.0 / 0.0 | 1.22 | 284 | 96.7% | 1 | 0 | yes |
| 2023-10-10 | bybit_ob/bybit/BTC-USDT/perp | 863,836 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 150 | 95.1% | 0 | 0 | yes |
| 2023-10-10 | bybit_ob/bybit/DOGE-USDT/perp | 543,234 | 1.000 | 11.8 | 3 | 0.0 / 0.0 | 1.70 | 145 | 98.3% | 0 | 0 | yes |
| 2023-10-10 | bybit_ob/bybit/ETH-USDT/perp | 858,711 | 1.000 | 0.5 | 0 | 0.0 / 0.0 | 0.06 | 190 | 95.2% | 1 | 0 | yes |
| 2023-10-10 | bybit_ob/bybit/SOL-USDT/perp | 762,247 | 1.000 | 12.7 | 1 | 0.0 / 0.0 | 0.45 | 321 | 95.8% | 0 | 0 | yes |
| 2023-10-10 | bybit_ob/bybit/WLD-USDT/perp | 390,237 | 0.991 | 12.8 | 1 | 0.0 / 0.0 | 6.52 | 344 | 99.6% | 0 | 20 | yes |
| 2023-10-10 | bybit_ob/bybit/XRP-USDT/perp | 614,077 | 1.000 | 11.7 | 2 | 0.0 / 0.0 | 2.01 | 188 | 98.0% | 0 | 20 | yes |
| 2023-10-10 | bybit_ob/bybit/ZEC-USDT/perp | 99,058 | 0.652 | 23.7 | 3 | 0.0 / 0.0 | 19.55 | 306 | 99.7% | 0 | 0 | NO |
| 2023-10-11 | binance_bt/binance/AAVE-USDT/perp | 40,528 | 0.968 | 13.9 | 0 | 5.0 / 12.0 | 1.59 | 329 | no trade record | - | - | yes |
| 2023-10-11 | binance_bt/binance/ARB-USDT/perp | 53,454 | 0.999 | 6.5 | 0 | 5.0 / 14.0 | 1.24 | 332 | no trade record | - | - | yes |
| 2023-10-11 | binance_bt/binance/BTC-USDT/perp | 192,136 | 1.000 | 3.8 | 0 | 6.0 / 18.0 | 0.04 | 195 | no trade record | - | - | yes |
| 2023-10-11 | binance_bt/binance/DOGE-USDT/perp | 13,394 | 1.000 | 4.1 | 0 | 6.0 / 20.0 | 1.72 | 245 | no trade record | - | - | yes |
| 2023-10-11 | binance_bt/binance/ETH-USDT/perp | 201,122 | 1.000 | 3.9 | 0 | 6.0 / 13.0 | 0.06 | 242 | no trade record | - | - | yes |
| 2023-10-11 | binance_bt/binance/SOL-USDT/perp | 178,285 | 1.000 | 3.9 | 0 | 5.0 / 12.0 | 0.46 | 349 | no trade record | - | - | yes |
| 2023-10-11 | binance_bt/binance/WLD-USDT/perp | 362,946 | 1.000 | 5.3 | 0 | 5.0 / 9.0 | 1.22 | 526 | no trade record | - | - | yes |
| 2023-10-11 | binance_bt/binance/XRP-USDT/perp | 15,007 | 1.000 | 4.1 | 0 | 6.0 / 14.9 | 2.07 | 275 | no trade record | - | - | yes |
| 2023-10-11 | binance_bt/binance/ZEC-USDT/perp | 5,007 | 0.807 | 28.1 | 0 | 5.0 / 12.0 | 4.01 | 280 | no trade record | - | - | NO |
| 2023-10-11 | bybit_ob/bybit/AAVE-USDT/perp | 388,499 | 0.990 | 5.2 | 0 | 0.0 / 0.0 | 1.58 | 341 | 96.4% | 1 | 0 | yes |
| 2023-10-11 | bybit_ob/bybit/ARB-USDT/perp | 758,068 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 1.23 | 334 | 95.9% | 1 | 0 | yes |
| 2023-10-11 | bybit_ob/bybit/BTC-USDT/perp | 863,956 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 199 | 90.7% | 1 | 0 | yes |
| 2023-10-11 | bybit_ob/bybit/DOGE-USDT/perp | 574,950 | 1.000 | 2.8 | 0 | 0.0 / 0.0 | 1.70 | 255 | 96.9% | 1 | 20 | yes |
| 2023-10-11 | bybit_ob/bybit/ETH-USDT/perp | 860,235 | 1.000 | 1.0 | 0 | 0.0 / 0.0 | 0.06 | 239 | 95.8% | 1 | 0 | yes |
| 2023-10-11 | bybit_ob/bybit/SOL-USDT/perp | 782,088 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.45 | 354 | 95.6% | 1 | 0 | yes |
| 2023-10-11 | bybit_ob/bybit/WLD-USDT/perp | 513,551 | 0.999 | 5.3 | 0 | 0.0 / 0.0 | 6.31 | 532 | 99.1% | 0 | 0 | yes |
| 2023-10-11 | bybit_ob/bybit/XRP-USDT/perp | 649,825 | 1.000 | 2.0 | 0 | 0.0 / 0.0 | 2.05 | 301 | 98.0% | 0 | 20 | yes |
| 2023-10-11 | bybit_ob/bybit/ZEC-USDT/perp | 112,356 | 0.712 | 19.7 | 0 | 0.0 / 0.0 | 19.90 | 336 | 99.8% | 0 | 0 | NO |
| 2023-10-12 | binance_bt/binance/AAVE-USDT/perp | 33,265 | 0.956 | 16.2 | 0 | 5.0 / 11.0 | 1.60 | 265 | no trade record | - | - | yes |
| 2023-10-12 | binance_bt/binance/ARB-USDT/perp | 48,796 | 0.998 | 9.3 | 0 | 5.0 / 11.0 | 1.26 | 319 | no trade record | - | - | yes |
| 2023-10-12 | binance_bt/binance/BTC-USDT/perp | 108,806 | 1.000 | 4.0 | 0 | 6.0 / 13.0 | 0.04 | 139 | no trade record | - | - | yes |
| 2023-10-12 | binance_bt/binance/DOGE-USDT/perp | 8,835 | 1.000 | 4.3 | 0 | 6.0 / 15.0 | 1.74 | 152 | no trade record | - | - | yes |
| 2023-10-12 | binance_bt/binance/ETH-USDT/perp | 170,267 | 1.000 | 4.0 | 0 | 6.0 / 12.0 | 0.07 | 200 | no trade record | - | - | yes |
| 2023-10-12 | binance_bt/binance/SOL-USDT/perp | 152,831 | 1.000 | 4.3 | 0 | 5.0 / 10.0 | 0.47 | 325 | no trade record | - | - | yes |
| 2023-10-12 | binance_bt/binance/WLD-USDT/perp | 228,004 | 1.000 | 4.9 | 0 | 5.0 / 8.0 | 0.68 | 460 | no trade record | - | - | yes |
| 2023-10-12 | binance_bt/binance/XRP-USDT/perp | 12,682 | 1.000 | 3.9 | 0 | 5.0 / 13.0 | 2.09 | 220 | no trade record | - | - | yes |
| 2023-10-12 | binance_bt/binance/ZEC-USDT/perp | 5,513 | 0.771 | 37.6 | 0 | 5.0 / 10.0 | 4.05 | 237 | no trade record | - | - | NO |
| 2023-10-12 | bybit_ob/bybit/AAVE-USDT/perp | 368,819 | 0.989 | 7.4 | 0 | 0.0 / 0.0 | 1.59 | 268 | 96.1% | 1 | 0 | yes |
| 2023-10-12 | bybit_ob/bybit/ARB-USDT/perp | 747,876 | 1.000 | 6.0 | 0 | 0.0 / 0.0 | 1.25 | 312 | 96.6% | 0 | 0 | yes |
| 2023-10-12 | bybit_ob/bybit/BTC-USDT/perp | 863,760 | 1.000 | 12.1 | 0 | 0.0 / 0.0 | 0.04 | 139 | 96.2% | 0 | 0 | yes |
| 2023-10-12 | bybit_ob/bybit/DOGE-USDT/perp | 504,874 | 1.000 | 6.0 | 0 | 0.0 / 0.0 | 1.73 | 154 | 97.8% | 0 | 0 | yes |
| 2023-10-12 | bybit_ob/bybit/ETH-USDT/perp | 858,958 | 1.000 | 7.3 | 0 | 0.0 / 0.0 | 0.06 | 197 | 93.4% | 0 | 0 | yes |
| 2023-10-12 | bybit_ob/bybit/SOL-USDT/perp | 758,140 | 1.000 | 6.8 | 0 | 0.0 / 0.0 | 0.47 | 328 | 95.2% | 1 | 0 | yes |
| 2023-10-12 | bybit_ob/bybit/WLD-USDT/perp | 445,380 | 0.995 | 7.1 | 0 | 0.0 / 0.0 | 6.75 | 458 | 99.6% | 0 | 0 | yes |
| 2023-10-12 | bybit_ob/bybit/XRP-USDT/perp | 642,828 | 1.000 | 7.4 | 0 | 0.0 / 0.0 | 2.08 | 221 | 98.3% | 0 | 20 | yes |
| 2023-10-12 | bybit_ob/bybit/ZEC-USDT/perp | 103,620 | 0.681 | 20.6 | 0 | 0.0 / 0.0 | 20.18 | 294 | 100.0% | 0 | 0 | NO |
| 2023-10-13 | binance_bt/binance/AAVE-USDT/perp | 24,202 | 0.935 | 13.9 | 0 | 5.0 / 12.0 | 1.58 | 225 | no trade record | - | - | NO |
| 2023-10-13 | binance_bt/binance/ARB-USDT/perp | 36,098 | 0.997 | 8.3 | 0 | 5.0 / 12.0 | 1.25 | 269 | no trade record | - | - | yes |
| 2023-10-13 | binance_bt/binance/BTC-USDT/perp | 107,906 | 1.000 | 5.5 | 0 | 6.0 / 14.0 | 0.04 | 153 | no trade record | - | - | yes |
| 2023-10-13 | binance_bt/binance/DOGE-USDT/perp | 9,586 | 1.000 | 6.0 | 0 | 6.0 / 25.0 | 1.72 | 182 | no trade record | - | - | yes |
| 2023-10-13 | binance_bt/binance/ETH-USDT/perp | 143,167 | 1.000 | 4.8 | 0 | 6.0 / 12.0 | 0.06 | 179 | no trade record | - | - | yes |
| 2023-10-13 | binance_bt/binance/SOL-USDT/perp | 135,465 | 1.000 | 6.0 | 0 | 5.0 / 11.0 | 0.47 | 283 | no trade record | - | - | yes |
| 2023-10-13 | binance_bt/binance/WLD-USDT/perp | 167,937 | 0.999 | 7.3 | 0 | 5.0 / 9.0 | 0.70 | 377 | no trade record | - | - | yes |
| 2023-10-13 | binance_bt/binance/XRP-USDT/perp | 8,213 | 1.000 | 5.9 | 0 | 6.0 / 16.0 | 2.08 | 212 | no trade record | - | - | yes |
| 2023-10-13 | binance_bt/binance/ZEC-USDT/perp | 5,205 | 0.761 | 40.3 | 0 | 5.0 / 10.0 | 4.05 | 234 | no trade record | - | - | NO |
| 2023-10-13 | bybit_ob/bybit/AAVE-USDT/perp | 333,744 | 0.986 | 6.4 | 0 | 0.0 / 0.0 | 1.58 | 226 | 95.8% | 1 | 0 | yes |
| 2023-10-13 | bybit_ob/bybit/ARB-USDT/perp | 730,737 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 1.24 | 267 | 96.8% | 0 | 0 | yes |
| 2023-10-13 | bybit_ob/bybit/BTC-USDT/perp | 863,942 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 153 | 93.3% | 1 | 0 | yes |
| 2023-10-13 | bybit_ob/bybit/DOGE-USDT/perp | 485,392 | 1.000 | 3.0 | 0 | 0.0 / 0.0 | 1.72 | 185 | 96.6% | 0 | 20 | yes |
| 2023-10-13 | bybit_ob/bybit/ETH-USDT/perp | 857,680 | 1.000 | 0.5 | 0 | 0.0 / 0.0 | 0.06 | 178 | 93.9% | 1 | 0 | yes |
| 2023-10-13 | bybit_ob/bybit/SOL-USDT/perp | 757,668 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.47 | 289 | 93.4% | 0 | 0 | yes |
| 2023-10-13 | bybit_ob/bybit/WLD-USDT/perp | 354,444 | 0.992 | 7.0 | 0 | 0.0 / 0.0 | 6.80 | 376 | 99.5% | 0 | 0 | yes |
| 2023-10-13 | bybit_ob/bybit/XRP-USDT/perp | 631,127 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 2.07 | 205 | 98.5% | 0 | 0 | yes |
| 2023-10-13 | bybit_ob/bybit/ZEC-USDT/perp | 95,372 | 0.618 | 17.1 | 0 | 0.0 / 0.0 | 20.18 | 305 | 99.8% | 0 | 0 | NO |
| 2023-10-14 | binance_bt/binance/AAVE-USDT/perp | 13,189 | 0.871 | 18.8 | 0 | 5.0 / 11.0 | 1.56 | 217 | no trade record | - | - | NO |
| 2023-10-14 | binance_bt/binance/ARB-USDT/perp | 10,842 | 0.994 | 8.4 | 0 | 5.0 / 13.0 | 1.24 | 145 | no trade record | - | - | yes |
| 2023-10-14 | binance_bt/binance/BTC-USDT/perp | 23,021 | 1.000 | 4.3 | 0 | 6.0 / 16.0 | 0.04 | 66 | no trade record | - | - | yes |
| 2023-10-14 | binance_bt/binance/DOGE-USDT/perp | 3,916 | 1.000 | 3.9 | 0 | 5.0 / 19.0 | 1.70 | 129 | no trade record | - | - | yes |
| 2023-10-14 | binance_bt/binance/ETH-USDT/perp | 46,941 | 1.000 | 4.5 | 0 | 6.0 / 13.0 | 0.06 | 88 | no trade record | - | - | yes |
| 2023-10-14 | binance_bt/binance/SOL-USDT/perp | 73,307 | 1.000 | 7.4 | 0 | 5.0 / 10.0 | 0.46 | 216 | no trade record | - | - | yes |
| 2023-10-14 | binance_bt/binance/WLD-USDT/perp | 76,099 | 0.994 | 11.9 | 0 | 5.0 / 8.0 | 0.68 | 256 | no trade record | - | - | yes |
| 2023-10-14 | binance_bt/binance/XRP-USDT/perp | 2,235 | 1.000 | 4.6 | 0 | 5.0 / 18.3 | 2.06 | 100 | no trade record | - | - | yes |
| 2023-10-14 | binance_bt/binance/ZEC-USDT/perp | 2,523 | 0.653 | 68.3 | 0 | 5.0 / 8.0 | 3.99 | 167 | no trade record | - | - | NO |
| 2023-10-14 | bybit_ob/bybit/AAVE-USDT/perp | 250,223 | 0.953 | 9.5 | 0 | 0.0 / 0.0 | 1.55 | 215 | 96.1% | 0 | 0 | yes |
| 2023-10-14 | bybit_ob/bybit/ARB-USDT/perp | 700,697 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 1.24 | 135 | 98.9% | 0 | 0 | yes |
| 2023-10-14 | bybit_ob/bybit/BTC-USDT/perp | 863,662 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 61 | 97.1% | 1 | 0 | yes |
| 2023-10-14 | bybit_ob/bybit/DOGE-USDT/perp | 427,623 | 0.999 | 4.1 | 0 | 0.0 / 0.0 | 1.69 | 125 | 98.6% | 1 | 0 | yes |
| 2023-10-14 | bybit_ob/bybit/ETH-USDT/perp | 850,727 | 1.000 | 0.6 | 0 | 0.0 / 0.0 | 0.06 | 85 | 97.1% | 1 | 0 | yes |
| 2023-10-14 | bybit_ob/bybit/SOL-USDT/perp | 681,557 | 1.000 | 2.2 | 0 | 0.0 / 0.0 | 0.45 | 219 | 95.9% | 0 | 0 | yes |
| 2023-10-14 | bybit_ob/bybit/WLD-USDT/perp | 256,415 | 0.958 | 8.3 | 0 | 0.0 / 0.0 | 6.76 | 258 | 99.7% | 0 | 0 | yes |
| 2023-10-14 | bybit_ob/bybit/XRP-USDT/perp | 554,910 | 1.000 | 3.0 | 0 | 0.0 / 0.0 | 2.06 | 100 | 99.9% | 0 | 0 | yes |
| 2023-10-14 | bybit_ob/bybit/ZEC-USDT/perp | 98,678 | 0.544 | 20.6 | 0 | 0.0 / 0.0 | 19.90 | 215 | 99.9% | 0 | 0 | NO |
| 2023-10-15 | binance_bt/binance/AAVE-USDT/perp | 13,276 | 0.914 | 17.9 | 0 | 5.0 / 12.0 | 1.56 | 162 | no trade record | - | - | NO |
| 2023-10-15 | binance_bt/binance/ARB-USDT/perp | 17,917 | 0.992 | 11.4 | 0 | 5.0 / 14.0 | 1.25 | 169 | no trade record | - | - | yes |
| 2023-10-15 | binance_bt/binance/BTC-USDT/perp | 50,261 | 1.000 | 5.3 | 0 | 6.0 / 19.0 | 0.04 | 99 | no trade record | - | - | yes |
| 2023-10-15 | binance_bt/binance/DOGE-USDT/perp | 4,066 | 1.000 | 5.3 | 0 | 6.0 / 20.0 | 1.69 | 107 | no trade record | - | - | yes |
| 2023-10-15 | binance_bt/binance/ETH-USDT/perp | 70,223 | 1.000 | 5.4 | 0 | 6.0 / 14.0 | 0.06 | 109 | no trade record | - | - | yes |
| 2023-10-15 | binance_bt/binance/SOL-USDT/perp | 75,331 | 0.999 | 8.1 | 0 | 5.0 / 11.0 | 0.46 | 201 | no trade record | - | - | yes |
| 2023-10-15 | binance_bt/binance/WLD-USDT/perp | 118,306 | 0.996 | 8.6 | 0 | 5.0 / 9.0 | 0.67 | 324 | no trade record | - | - | yes |
| 2023-10-15 | binance_bt/binance/XRP-USDT/perp | 2,825 | 1.000 | 5.3 | 0 | 6.0 / 18.8 | 2.06 | 114 | no trade record | - | - | yes |
| 2023-10-15 | binance_bt/binance/ZEC-USDT/perp | 3,075 | 0.751 | 50.3 | 0 | 5.0 / 9.0 | 4.00 | 180 | no trade record | - | - | NO |
| 2023-10-15 | bybit_ob/bybit/AAVE-USDT/perp | 225,256 | 0.928 | 7.0 | 0 | 0.0 / 0.0 | 1.56 | 161 | 97.3% | 0 | 0 | NO |
| 2023-10-15 | bybit_ob/bybit/ARB-USDT/perp | 707,741 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 1.24 | 164 | 99.2% | 0 | 0 | yes |
| 2023-10-15 | bybit_ob/bybit/BTC-USDT/perp | 862,890 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 96 | 92.7% | 0 | 0 | yes |
| 2023-10-15 | bybit_ob/bybit/DOGE-USDT/perp | 441,503 | 1.000 | 4.6 | 0 | 0.0 / 0.0 | 1.68 | 104 | 97.9% | 0 | 0 | yes |
| 2023-10-15 | bybit_ob/bybit/ETH-USDT/perp | 852,163 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.06 | 107 | 95.8% | 1 | 0 | yes |
| 2023-10-15 | bybit_ob/bybit/SOL-USDT/perp | 677,371 | 1.000 | 2.1 | 0 | 0.0 / 0.0 | 0.46 | 202 | 94.1% | 1 | 0 | yes |
| 2023-10-15 | bybit_ob/bybit/WLD-USDT/perp | 296,723 | 0.974 | 8.8 | 0 | 0.0 / 0.0 | 6.65 | 330 | 99.1% | 0 | 20 | yes |
| 2023-10-15 | bybit_ob/bybit/XRP-USDT/perp | 543,378 | 1.000 | 3.0 | 0 | 0.0 / 0.0 | 2.05 | 113 | 99.4% | 0 | 0 | yes |
| 2023-10-15 | bybit_ob/bybit/ZEC-USDT/perp | 76,943 | 0.505 | 18.3 | 0 | 0.0 / 0.0 | 19.94 | 243 | 99.9% | 0 | 0 | NO |
| 2023-10-16 | binance_bt/binance/AAVE-USDT/perp | 60,839 | 0.965 | 14.4 | 0 | 6.0 / 13.0 | 1.57 | 378 | no trade record | - | - | yes |
| 2023-10-16 | binance_bt/binance/ARB-USDT/perp | 76,120 | 0.999 | 7.3 | 0 | 6.0 / 71.8 | 1.24 | 356 | no trade record | - | - | yes |
| 2023-10-16 | binance_bt/binance/BTC-USDT/perp | 640,187 | 1.000 | 4.2 | 0 | 6.0 / 70.0 | 0.11 | 597 | no trade record | - | - | yes |
| 2023-10-16 | binance_bt/binance/DOGE-USDT/perp | 21,909 | 1.000 | 4.6 | 0 | 6.0 / 17.0 | 1.68 | 314 | no trade record | - | - | yes |
| 2023-10-16 | binance_bt/binance/ETH-USDT/perp | 352,299 | 1.000 | 4.3 | 0 | 6.0 / 14.0 | 0.12 | 313 | no trade record | - | - | yes |
| 2023-10-16 | binance_bt/binance/SOL-USDT/perp | 394,416 | 1.000 | 4.8 | 0 | 6.0 / 34.0 | 0.83 | 568 | no trade record | - | - | yes |
| 2023-10-16 | binance_bt/binance/WLD-USDT/perp | 330,394 | 0.998 | 8.0 | 0 | 5.0 / 10.0 | 1.24 | 574 | no trade record | - | - | yes |
| 2023-10-16 | binance_bt/binance/XRP-USDT/perp | 23,354 | 1.000 | 4.3 | 0 | 6.0 / 17.0 | 2.03 | 299 | no trade record | - | - | yes |
| 2023-10-16 | binance_bt/binance/ZEC-USDT/perp | 8,963 | 0.802 | 44.1 | 0 | 5.0 / 13.0 | 3.93 | 320 | no trade record | - | - | NO |
| 2023-10-16 | bybit_ob/bybit/AAVE-USDT/perp | 377,605 | 0.983 | 8.3 | 1 | 0.0 / 0.0 | 1.55 | 378 | 93.9% | 1 | 0 | yes |
| 2023-10-16 | bybit_ob/bybit/ARB-USDT/perp | 746,905 | 1.000 | 8.9 | 1 | 0.0 / 0.0 | 1.23 | 350 | 91.3% | 0 | 20 | yes |
| 2023-10-16 | bybit_ob/bybit/BTC-USDT/perp | 863,899 | 1.000 | 8.9 | 1 | 0.0 / 0.0 | 0.04 | 603 | 80.2% | 0 | 0 | yes |
| 2023-10-16 | bybit_ob/bybit/DOGE-USDT/perp | 518,832 | 1.000 | 9.2 | 1 | 0.0 / 0.0 | 1.67 | 319 | 96.0% | 0 | 0 | yes |
| 2023-10-16 | bybit_ob/bybit/ETH-USDT/perp | 860,438 | 1.000 | 9.6 | 1 | 0.0 / 0.0 | 0.06 | 315 | 88.8% | 1 | 0 | yes |
| 2023-10-16 | bybit_ob/bybit/SOL-USDT/perp | 797,743 | 1.000 | 7.9 | 1 | 0.0 / 0.0 | 0.43 | 574 | 89.8% | 0 | 0 | yes |
| 2023-10-16 | bybit_ob/bybit/WLD-USDT/perp | 395,155 | 0.988 | 8.4 | 1 | 0.0 / 0.0 | 6.31 | 578 | 98.2% | 1 | 20 | yes |
| 2023-10-16 | bybit_ob/bybit/XRP-USDT/perp | 643,519 | 1.000 | 8.3 | 1 | 0.0 / 0.0 | 2.03 | 298 | 95.9% | 0 | 20 | yes |
| 2023-10-16 | bybit_ob/bybit/ZEC-USDT/perp | 113,594 | 0.658 | 21.0 | 1 | 0.0 / 0.0 | 19.59 | 368 | 99.5% | 0 | 50 | NO |
| 2023-10-17 | binance_bt/binance/AAVE-USDT/perp | 26,770 | 0.964 | 16.1 | 0 | 5.0 / 11.0 | 1.61 | 261 | no trade record | - | - | yes |
| 2023-10-17 | binance_bt/binance/ARB-USDT/perp | 38,010 | 0.998 | 9.8 | 0 | 5.0 / 13.0 | 1.27 | 251 | no trade record | - | - | yes |
| 2023-10-17 | binance_bt/binance/BTC-USDT/perp | 198,805 | 1.000 | 4.2 | 0 | 6.0 / 14.0 | 0.04 | 208 | no trade record | - | - | yes |
| 2023-10-17 | binance_bt/binance/DOGE-USDT/perp | 9,888 | 1.000 | 4.5 | 0 | 6.0 / 17.0 | 1.70 | 162 | no trade record | - | - | yes |
| 2023-10-17 | binance_bt/binance/ETH-USDT/perp | 145,557 | 1.000 | 4.4 | 0 | 6.0 / 13.0 | 0.06 | 173 | no trade record | - | - | yes |
| 2023-10-17 | binance_bt/binance/SOL-USDT/perp | 268,262 | 1.000 | 4.6 | 0 | 5.0 / 11.0 | 0.42 | 396 | no trade record | - | - | yes |
| 2023-10-17 | binance_bt/binance/WLD-USDT/perp | 286,993 | 0.999 | 8.2 | 0 | 5.0 / 9.0 | 1.20 | 468 | no trade record | - | - | yes |
| 2023-10-17 | binance_bt/binance/XRP-USDT/perp | 8,848 | 1.000 | 4.5 | 0 | 6.0 / 33.0 | 2.05 | 175 | no trade record | - | - | yes |
| 2023-10-17 | binance_bt/binance/ZEC-USDT/perp | 5,569 | 0.802 | 29.4 | 0 | 5.0 / 9.0 | 4.05 | 210 | no trade record | - | - | NO |
| 2023-10-17 | bybit_ob/bybit/AAVE-USDT/perp | 382,844 | 0.980 | 6.1 | 0 | 0.0 / 0.0 | 1.59 | 255 | 94.5% | 1 | 0 | yes |
| 2023-10-17 | bybit_ob/bybit/ARB-USDT/perp | 727,969 | 1.000 | 2.1 | 0 | 0.0 / 0.0 | 1.24 | 242 | 97.6% | 1 | 0 | yes |
| 2023-10-17 | bybit_ob/bybit/BTC-USDT/perp | 863,985 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 212 | 93.6% | 0 | 0 | yes |
| 2023-10-17 | bybit_ob/bybit/DOGE-USDT/perp | 456,722 | 1.000 | 4.4 | 0 | 0.0 / 0.0 | 1.68 | 173 | 97.1% | 1 | 0 | yes |
| 2023-10-17 | bybit_ob/bybit/ETH-USDT/perp | 860,915 | 1.000 | 0.5 | 0 | 0.0 / 0.0 | 0.06 | 173 | 93.8% | 1 | 0 | yes |
| 2023-10-17 | bybit_ob/bybit/SOL-USDT/perp | 806,939 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 0.42 | 399 | 94.0% | 0 | 0 | yes |
| 2023-10-17 | bybit_ob/bybit/WLD-USDT/perp | 395,512 | 0.993 | 7.8 | 0 | 0.0 / 0.0 | 6.14 | 475 | 99.4% | 0 | 20 | yes |
| 2023-10-17 | bybit_ob/bybit/XRP-USDT/perp | 654,620 | 1.000 | 2.6 | 0 | 0.0 / 0.0 | 2.04 | 181 | 98.4% | 0 | 20 | yes |
| 2023-10-17 | bybit_ob/bybit/ZEC-USDT/perp | 118,939 | 0.686 | 14.6 | 0 | 0.0 / 0.0 | 19.94 | 246 | 99.1% | 0 | 0 | NO |
| 2023-10-18 | binance_bt/binance/AAVE-USDT/perp | 17,534 | 0.946 | 20.3 | 0 | 5.0 / 12.0 | 1.61 | 225 | no trade record | - | - | NO |
| 2023-10-18 | binance_bt/binance/ARB-USDT/perp | 33,054 | 0.998 | 8.7 | 0 | 5.0 / 12.0 | 1.28 | 248 | no trade record | - | - | yes |
| 2023-10-18 | binance_bt/binance/BTC-USDT/perp | 179,566 | 1.000 | 3.8 | 0 | 6.0 / 14.0 | 0.04 | 204 | no trade record | - | - | yes |
| 2023-10-18 | binance_bt/binance/DOGE-USDT/perp | 7,029 | 1.000 | 4.0 | 0 | 6.0 / 15.0 | 1.71 | 152 | no trade record | - | - | yes |
| 2023-10-18 | binance_bt/binance/ETH-USDT/perp | 137,808 | 1.000 | 2.8 | 0 | 6.0 / 12.0 | 0.06 | 164 | no trade record | - | - | yes |
| 2023-10-18 | binance_bt/binance/SOL-USDT/perp | 172,305 | 1.000 | 5.4 | 0 | 5.0 / 11.0 | 0.42 | 316 | no trade record | - | - | yes |
| 2023-10-18 | binance_bt/binance/WLD-USDT/perp | 257,795 | 1.000 | 5.6 | 0 | 5.0 / 8.0 | 0.68 | 482 | no trade record | - | - | yes |
| 2023-10-18 | binance_bt/binance/XRP-USDT/perp | 5,721 | 1.000 | 4.4 | 0 | 6.0 / 41.0 | 2.05 | 169 | no trade record | - | - | yes |
| 2023-10-18 | binance_bt/binance/ZEC-USDT/perp | 5,937 | 0.769 | 39.8 | 0 | 5.0 / 9.0 | 4.04 | 235 | no trade record | - | - | NO |
| 2023-10-18 | bybit_ob/bybit/AAVE-USDT/perp | 324,671 | 0.980 | 6.7 | 0 | 0.0 / 0.0 | 1.60 | 227 | 96.9% | 1 | 0 | yes |
| 2023-10-18 | bybit_ob/bybit/ARB-USDT/perp | 723,990 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 1.27 | 241 | 98.4% | 0 | 0 | yes |
| 2023-10-18 | bybit_ob/bybit/BTC-USDT/perp | 863,984 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.04 | 207 | 91.3% | 0 | 0 | yes |
| 2023-10-18 | bybit_ob/bybit/DOGE-USDT/perp | 452,818 | 1.000 | 5.0 | 0 | 0.0 / 0.0 | 1.70 | 161 | 94.5% | 1 | 0 | yes |
| 2023-10-18 | bybit_ob/bybit/ETH-USDT/perp | 858,667 | 1.000 | 0.5 | 0 | 0.0 / 0.0 | 0.06 | 167 | 95.6% | 1 | 0 | yes |
| 2023-10-18 | bybit_ob/bybit/SOL-USDT/perp | 785,431 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 0.42 | 321 | 94.5% | 0 | 0 | yes |
| 2023-10-18 | bybit_ob/bybit/WLD-USDT/perp | 407,487 | 0.996 | 5.7 | 0 | 0.0 / 0.0 | 6.30 | 487 | 99.3% | 0 | 0 | yes |
| 2023-10-18 | bybit_ob/bybit/XRP-USDT/perp | 564,398 | 1.000 | 2.7 | 0 | 0.0 / 0.0 | 2.04 | 174 | 91.3% | 1 | 20 | yes |
| 2023-10-18 | bybit_ob/bybit/ZEC-USDT/perp | 133,025 | 0.744 | 20.0 | 0 | 0.0 / 0.0 | 20.18 | 297 | 99.7% | 0 | 100 | NO |
| 2023-10-19 | binance_bt/binance/AAVE-USDT/perp | 50,268 | 0.945 | 18.0 | 0 | 5.0 / 9.0 | 1.62 | 340 | no trade record | - | - | NO |
| 2023-10-19 | binance_bt/binance/ARB-USDT/perp | 34,870 | 0.998 | 8.2 | 0 | 5.0 / 13.0 | 1.30 | 273 | no trade record | - | - | yes |
| 2023-10-19 | binance_bt/binance/BTC-USDT/perp | 217,539 | 1.000 | 4.5 | 0 | 6.0 / 13.0 | 0.04 | 188 | no trade record | - | - | yes |
| 2023-10-19 | binance_bt/binance/DOGE-USDT/perp | 9,539 | 1.000 | 5.0 | 0 | 6.0 / 13.0 | 1.72 | 159 | no trade record | - | - | yes |
| 2023-10-19 | binance_bt/binance/ETH-USDT/perp | 149,372 | 1.000 | 4.8 | 0 | 6.0 / 12.0 | 0.06 | 176 | no trade record | - | - | yes |
| 2023-10-19 | binance_bt/binance/SOL-USDT/perp | 300,638 | 1.000 | 4.8 | 0 | 5.0 / 11.0 | 0.42 | 451 | no trade record | - | - | yes |
| 2023-10-19 | binance_bt/binance/WLD-USDT/perp | 258,011 | 0.999 | 7.7 | 0 | 5.0 / 8.0 | 0.70 | 507 | no trade record | - | - | yes |
| 2023-10-19 | binance_bt/binance/XRP-USDT/perp | 35,345 | 1.000 | 4.4 | 0 | 5.0 / 11.0 | 2.05 | 428 | no trade record | - | - | yes |
| 2023-10-19 | binance_bt/binance/ZEC-USDT/perp | 6,647 | 0.768 | 45.4 | 0 | 5.0 / 9.0 | 4.03 | 233 | no trade record | - | - | NO |
| 2023-10-19 | bybit_ob/bybit/AAVE-USDT/perp | 350,659 | 0.974 | 12.0 | 1 | 0.0 / 0.0 | 1.61 | 336 | 94.4% | 0 | 0 | yes |
| 2023-10-19 | bybit_ob/bybit/ARB-USDT/perp | 701,090 | 1.000 | 13.7 | 1 | 0.0 / 0.0 | 1.29 | 268 | 98.2% | 0 | 0 | yes |
| 2023-10-19 | bybit_ob/bybit/BTC-USDT/perp | 863,863 | 1.000 | 9.7 | 1 | 0.0 / 0.0 | 0.04 | 189 | 92.5% | 0 | 0 | yes |
| 2023-10-19 | bybit_ob/bybit/DOGE-USDT/perp | 505,367 | 1.000 | 13.7 | 1 | 0.0 / 0.0 | 1.72 | 161 | 98.3% | 0 | 0 | yes |
| 2023-10-19 | bybit_ob/bybit/ETH-USDT/perp | 858,043 | 1.000 | 11.3 | 1 | 0.0 / 0.0 | 0.06 | 175 | 95.3% | 1 | 0 | yes |
| 2023-10-19 | bybit_ob/bybit/SOL-USDT/perp | 807,857 | 1.000 | 14.0 | 1 | 0.0 / 0.0 | 0.41 | 457 | 92.5% | 0 | 0 | yes |
| 2023-10-19 | bybit_ob/bybit/WLD-USDT/perp | 390,716 | 0.993 | 14.2 | 1 | 0.0 / 0.0 | 6.85 | 507 | 97.8% | 0 | 50 | NO |
| 2023-10-19 | bybit_ob/bybit/XRP-USDT/perp | 644,617 | 1.000 | 11.6 | 1 | 0.0 / 0.0 | 2.07 | 435 | 94.4% | 0 | 20 | yes |
| 2023-10-19 | bybit_ob/bybit/ZEC-USDT/perp | 132,535 | 0.753 | 14.7 | 1 | 0.0 / 0.0 | 20.10 | 298 | 99.2% | 0 | 0 | NO |
| 2023-10-20 | binance_bt/binance/AAVE-USDT/perp | 91,790 | 0.982 | 14.0 | 0 | 5.0 / 16.0 | 1.54 | 509 | no trade record | - | - | yes |
| 2023-10-20 | binance_bt/binance/ARB-USDT/perp | 48,374 | 0.998 | 9.8 | 0 | 6.0 / 28.0 | 1.27 | 279 | no trade record | - | - | yes |
| 2023-10-20 | binance_bt/binance/BTC-USDT/perp | 415,966 | 1.000 | 6.4 | 0 | 6.0 / 30.0 | 0.03 | 260 | no trade record | - | - | yes |
| 2023-10-20 | binance_bt/binance/DOGE-USDT/perp | 10,236 | 1.000 | 5.6 | 0 | 6.0 / 26.0 | 1.68 | 165 | no trade record | - | - | yes |
| 2023-10-20 | binance_bt/binance/ETH-USDT/perp | 218,368 | 1.000 | 5.3 | 0 | 6.0 / 20.0 | 0.06 | 200 | no trade record | - | - | yes |
| 2023-10-20 | binance_bt/binance/SOL-USDT/perp | 485,567 | 1.000 | 6.4 | 0 | 5.0 / 19.0 | 0.39 | 540 | no trade record | - | - | yes |
| 2023-10-20 | binance_bt/binance/WLD-USDT/perp | 294,485 | 0.998 | 8.9 | 0 | 5.0 / 14.0 | 0.69 | 473 | no trade record | - | - | yes |
| 2023-10-20 | binance_bt/binance/XRP-USDT/perp | 28,377 | 1.000 | 5.6 | 0 | 5.0 / 20.0 | 1.94 | 339 | no trade record | - | - | yes |
| 2023-10-20 | binance_bt/binance/ZEC-USDT/perp | 8,719 | 0.861 | 36.4 | 0 | 5.0 / 18.0 | 3.95 | 213 | no trade record | - | - | NO |
| 2023-10-20 | bybit_ob/bybit/AAVE-USDT/perp | 434,167 | 0.988 | 6.3 | 0 | 0.0 / 0.0 | 1.52 | 510 | 92.0% | 1 | 0 | yes |
| 2023-10-20 | bybit_ob/bybit/ARB-USDT/perp | 728,488 | 1.000 | 2.1 | 0 | 0.0 / 0.0 | 1.26 | 272 | 98.2% | 1 | 0 | yes |
| 2023-10-20 | bybit_ob/bybit/BTC-USDT/perp | 863,967 | 1.000 | 1.3 | 0 | 0.0 / 0.0 | 0.03 | 259 | 89.1% | 0 | 0 | yes |
| 2023-10-20 | bybit_ob/bybit/DOGE-USDT/perp | 565,480 | 1.000 | 3.0 | 0 | 0.0 / 0.0 | 1.67 | 168 | 97.1% | 1 | 20 | yes |
| 2023-10-20 | bybit_ob/bybit/ETH-USDT/perp | 860,903 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.06 | 200 | 94.4% | 1 | 0 | yes |
| 2023-10-20 | bybit_ob/bybit/SOL-USDT/perp | 828,428 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 0.37 | 541 | 91.8% | 0 | 0 | yes |
| 2023-10-20 | bybit_ob/bybit/WLD-USDT/perp | 409,561 | 0.993 | 5.7 | 0 | 0.0 / 0.0 | 6.56 | 481 | 99.1% | 0 | 0 | yes |
| 2023-10-20 | bybit_ob/bybit/XRP-USDT/perp | 710,095 | 1.000 | 2.7 | 0 | 0.0 / 0.0 | 1.93 | 349 | 96.6% | 0 | 20 | yes |
| 2023-10-20 | bybit_ob/bybit/ZEC-USDT/perp | 150,369 | 0.782 | 14.3 | 0 | 0.0 / 0.0 | 19.70 | 289 | 98.8% | 0 | 100 | NO |
| 2023-10-21 | binance_bt/binance/AAVE-USDT/perp | 46,226 | 0.979 | 18.8 | 0 | 5.0 / 15.0 | 1.51 | 350 | no trade record | - | - | yes |
| 2023-10-21 | binance_bt/binance/ARB-USDT/perp | 36,604 | 0.998 | 10.5 | 0 | 6.0 / 22.0 | 1.22 | 264 | no trade record | - | - | yes |
| 2023-10-21 | binance_bt/binance/BTC-USDT/perp | 149,219 | 1.000 | 6.2 | 0 | 7.0 / 24.0 | 0.03 | 159 | no trade record | - | - | yes |
| 2023-10-21 | binance_bt/binance/DOGE-USDT/perp | 9,603 | 1.000 | 6.0 | 0 | 6.0 / 23.0 | 1.65 | 162 | no trade record | - | - | yes |
| 2023-10-21 | binance_bt/binance/ETH-USDT/perp | 124,319 | 1.000 | 6.2 | 0 | 6.0 / 20.0 | 0.06 | 149 | no trade record | - | - | yes |
| 2023-10-21 | binance_bt/binance/SOL-USDT/perp | 636,320 | 1.000 | 6.2 | 0 | 5.0 / 13.0 | 0.67 | 642 | no trade record | - | - | yes |
| 2023-10-21 | binance_bt/binance/WLD-USDT/perp | 277,786 | 0.997 | 8.3 | 0 | 5.0 / 11.0 | 1.22 | 549 | no trade record | - | - | yes |
| 2023-10-21 | binance_bt/binance/XRP-USDT/perp | 13,268 | 1.000 | 6.0 | 0 | 6.0 / 21.0 | 1.93 | 216 | no trade record | - | - | yes |
| 2023-10-21 | binance_bt/binance/ZEC-USDT/perp | 7,072 | 0.783 | 30.3 | 0 | 5.0 / 13.0 | 3.93 | 200 | no trade record | - | - | NO |
| 2023-10-21 | bybit_ob/bybit/AAVE-USDT/perp | 363,421 | 0.981 | 6.3 | 0 | 0.0 / 0.0 | 1.48 | 353 | 94.8% | 1 | 0 | yes |
| 2023-10-21 | bybit_ob/bybit/ARB-USDT/perp | 729,929 | 1.000 | 1.6 | 0 | 0.0 / 0.0 | 1.22 | 255 | 98.5% | 0 | 0 | yes |
| 2023-10-21 | bybit_ob/bybit/BTC-USDT/perp | 863,802 | 1.000 | 1.3 | 0 | 0.0 / 0.0 | 0.03 | 158 | 91.7% | 1 | 0 | yes |
| 2023-10-21 | bybit_ob/bybit/DOGE-USDT/perp | 505,815 | 1.000 | 3.8 | 0 | 0.0 / 0.0 | 1.65 | 164 | 99.0% | 1 | 0 | yes |
| 2023-10-21 | bybit_ob/bybit/ETH-USDT/perp | 858,416 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.06 | 149 | 95.1% | 1 | 0 | yes |
| 2023-10-21 | bybit_ob/bybit/SOL-USDT/perp | 829,925 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 0.35 | 669 | 87.7% | 0 | 0 | yes |
| 2023-10-21 | bybit_ob/bybit/WLD-USDT/perp | 396,152 | 0.991 | 6.6 | 0 | 0.0 / 0.0 | 6.50 | 553 | 97.8% | 0 | 20 | yes |
| 2023-10-21 | bybit_ob/bybit/XRP-USDT/perp | 597,451 | 1.000 | 2.8 | 0 | 0.0 / 0.0 | 1.93 | 218 | 97.9% | 0 | 20 | yes |
| 2023-10-21 | bybit_ob/bybit/ZEC-USDT/perp | 152,944 | 0.780 | 16.6 | 0 | 0.0 / 0.0 | 19.63 | 276 | 98.2% | 0 | 20 | NO |
| 2023-10-22 | binance_bt/binance/AAVE-USDT/perp | 197,085 | 0.999 | 7.1 | 0 | 5.0 / 10.0 | 1.41 | 682 | no trade record | - | - | yes |
| 2023-10-22 | binance_bt/binance/ARB-USDT/perp | 48,602 | 0.999 | 7.1 | 0 | 5.0 / 19.0 | 1.21 | 338 | no trade record | - | - | yes |
| 2023-10-22 | binance_bt/binance/BTC-USDT/perp | 121,593 | 1.000 | 7.0 | 0 | 7.0 / 25.0 | 0.03 | 159 | no trade record | - | - | yes |
| 2023-10-22 | binance_bt/binance/DOGE-USDT/perp | 12,636 | 1.000 | 7.1 | 0 | 6.0 / 29.0 | 1.65 | 197 | no trade record | - | - | yes |
| 2023-10-22 | binance_bt/binance/ETH-USDT/perp | 167,945 | 1.000 | 6.5 | 0 | 6.0 / 18.0 | 0.06 | 191 | no trade record | - | - | yes |
| 2023-10-22 | binance_bt/binance/SOL-USDT/perp | 430,532 | 1.000 | 7.0 | 0 | 5.0 / 13.0 | 0.35 | 492 | no trade record | - | - | yes |
| 2023-10-22 | binance_bt/binance/WLD-USDT/perp | 348,118 | 0.998 | 9.9 | 0 | 5.0 / 10.0 | 1.19 | 575 | no trade record | - | - | yes |
| 2023-10-22 | binance_bt/binance/XRP-USDT/perp | 10,409 | 1.000 | 7.0 | 0 | 6.0 / 25.0 | 1.94 | 197 | no trade record | - | - | yes |
| 2023-10-22 | binance_bt/binance/ZEC-USDT/perp | 8,236 | 0.769 | 46.4 | 0 | 5.0 / 15.0 | 3.94 | 277 | no trade record | - | - | NO |
| 2023-10-22 | bybit_ob/bybit/AAVE-USDT/perp | 586,820 | 0.999 | 4.7 | 0 | 0.0 / 0.0 | 1.32 | 678 | 92.9% | 1 | 0 | yes |
| 2023-10-22 | bybit_ob/bybit/ARB-USDT/perp | 725,896 | 1.000 | 2.2 | 0 | 0.0 / 0.0 | 1.20 | 328 | 97.7% | 0 | 0 | yes |
| 2023-10-22 | bybit_ob/bybit/BTC-USDT/perp | 863,942 | 1.000 | 1.3 | 0 | 0.0 / 0.0 | 0.03 | 161 | 93.1% | 1 | 0 | yes |
| 2023-10-22 | bybit_ob/bybit/DOGE-USDT/perp | 509,890 | 1.000 | 3.9 | 0 | 0.0 / 0.0 | 1.64 | 195 | 97.6% | 0 | 20 | yes |
| 2023-10-22 | bybit_ob/bybit/ETH-USDT/perp | 859,160 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.06 | 191 | 94.8% | 0 | 0 | yes |
| 2023-10-22 | bybit_ob/bybit/SOL-USDT/perp | 827,297 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 0.35 | 492 | 92.3% | 1 | 0 | yes |
| 2023-10-22 | bybit_ob/bybit/WLD-USDT/perp | 470,463 | 0.997 | 5.6 | 0 | 0.0 / 0.0 | 6.19 | 572 | 99.0% | 0 | 0 | yes |
| 2023-10-22 | bybit_ob/bybit/XRP-USDT/perp | 595,067 | 1.000 | 3.1 | 0 | 0.0 / 0.0 | 1.92 | 206 | 97.8% | 0 | 20 | yes |
| 2023-10-22 | bybit_ob/bybit/ZEC-USDT/perp | 138,625 | 0.773 | 20.7 | 0 | 0.0 / 0.0 | 19.55 | 343 | 98.7% | 0 | 50 | NO |
| 2023-10-23 | binance_bt/binance/AAVE-USDT/perp | 305,830 | 1.000 | 6.2 | 0 | 5.0 / 12.0 | 1.26 | 840 | no trade record | - | - | yes |
| 2023-10-23 | binance_bt/binance/ARB-USDT/perp | 125,136 | 1.000 | 5.6 | 0 | 6.0 / 362.6 | 1.19 | 472 | no trade record | - | - | yes |
| 2023-10-23 | binance_bt/binance/BTC-USDT/perp | 1,059,370 | 1.000 | 4.6 | 0 | 6.0 / 340.0 | 0.07 | 703 | no trade record | - | - | yes |
| 2023-10-23 | binance_bt/binance/DOGE-USDT/perp | 80,154 | 1.000 | 7.2 | 0 | 6.0 / 17.5 | 1.58 | 485 | no trade record | - | - | yes |
| 2023-10-23 | binance_bt/binance/ETH-USDT/perp | 610,311 | 1.000 | 2.2 | 0 | 6.0 / 21.0 | 0.06 | 407 | no trade record | - | - | yes |
| 2023-10-23 | binance_bt/binance/SOL-USDT/perp | 1,493,091 | 1.000 | 5.6 | 0 | 5.0 / 26.0 | 0.67 | 801 | no trade record | - | - | yes |
| 2023-10-23 | binance_bt/binance/WLD-USDT/perp | 678,331 | 1.000 | 6.5 | 0 | 5.0 / 11.0 | 1.26 | 694 | no trade record | - | - | yes |
| 2023-10-23 | binance_bt/binance/XRP-USDT/perp | 64,033 | 1.000 | 7.2 | 0 | 6.0 / 18.0 | 1.90 | 400 | no trade record | - | - | yes |
| 2023-10-23 | binance_bt/binance/ZEC-USDT/perp | 18,226 | 0.932 | 26.5 | 0 | 6.0 / 18.0 | 3.82 | 400 | no trade record | - | - | NO |
| 2023-10-23 | bybit_ob/bybit/AAVE-USDT/perp | 709,458 | 1.000 | 3.2 | 0 | 0.0 / 0.0 | 1.20 | 837 | 91.7% | 1 | 0 | yes |
| 2023-10-23 | bybit_ob/bybit/ARB-USDT/perp | 760,784 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 1.18 | 468 | 96.7% | 0 | 0 | yes |
| 2023-10-23 | bybit_ob/bybit/BTC-USDT/perp | 864,001 | 1.000 | 1.3 | 0 | 0.0 / 0.0 | 0.03 | 762 | 80.9% | 1 | 0 | yes |
| 2023-10-23 | bybit_ob/bybit/DOGE-USDT/perp | 722,127 | 1.000 | 2.1 | 0 | 0.0 / 0.0 | 1.56 | 487 | 96.8% | 1 | 0 | yes |
| 2023-10-23 | bybit_ob/bybit/ETH-USDT/perp | 862,779 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.06 | 407 | 88.1% | 1 | 0 | yes |
| 2023-10-23 | bybit_ob/bybit/SOL-USDT/perp | 852,701 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 0.34 | 811 | 87.3% | 0 | 0 | yes |
| 2023-10-23 | bybit_ob/bybit/WLD-USDT/perp | 554,676 | 1.000 | 3.7 | 0 | 0.0 / 0.0 | 6.46 | 698 | 98.8% | 0 | 20 | yes |
| 2023-10-23 | bybit_ob/bybit/XRP-USDT/perp | 733,900 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 1.89 | 402 | 88.8% | 1 | 20 | yes |
| 2023-10-23 | bybit_ob/bybit/ZEC-USDT/perp | 156,857 | 0.846 | 14.9 | 0 | 0.0 / 0.0 | 19.03 | 472 | 98.8% | 1 | 50 | NO |
| 2023-10-24 | binance_bt/binance/AAVE-USDT/perp | 253,564 | 0.999 | 6.3 | 0 | 5.0 / 14.0 | 1.21 | 776 | no trade record | - | - | yes |
| 2023-10-24 | binance_bt/binance/ARB-USDT/perp | 203,289 | 1.000 | 5.2 | 0 | 6.0 / 20.0 | 1.13 | 663 | no trade record | - | - | yes |
| 2023-10-24 | binance_bt/binance/BTC-USDT/perp | 1,249,983 | 1.000 | 5.2 | 0 | 6.0 / 20.0 | 0.06 | 511 | no trade record | - | - | yes |
| 2023-10-24 | binance_bt/binance/DOGE-USDT/perp | 104,113 | 1.000 | 5.2 | 0 | 6.0 / 17.0 | 1.51 | 628 | no trade record | - | - | yes |
| 2023-10-24 | binance_bt/binance/ETH-USDT/perp | 706,779 | 1.000 | 5.2 | 0 | 6.0 / 17.0 | 0.06 | 459 | no trade record | - | - | yes |
| 2023-10-24 | binance_bt/binance/SOL-USDT/perp | 2,417,115 | 1.000 | 5.2 | 0 | 5.0 / 16.0 | 0.65 | 859 | no trade record | - | - | yes |
| 2023-10-24 | binance_bt/binance/WLD-USDT/perp | 1,071,894 | 1.000 | 6.2 | 0 | 5.0 / 11.0 | 1.22 | 984 | no trade record | - | - | yes |
| 2023-10-24 | binance_bt/binance/XRP-USDT/perp | 123,192 | 1.000 | 5.9 | 0 | 6.0 / 15.0 | 1.82 | 747 | no trade record | - | - | yes |
| 2023-10-24 | binance_bt/binance/ZEC-USDT/perp | 29,478 | 0.981 | 12.7 | 0 | 5.0 / 17.0 | 3.67 | 585 | no trade record | - | - | yes |
| 2023-10-24 | bybit_ob/bybit/AAVE-USDT/perp | 651,851 | 1.000 | 4.1 | 0 | 0.0 / 0.0 | 1.19 | 782 | 93.0% | 1 | 0 | yes |
| 2023-10-24 | bybit_ob/bybit/ARB-USDT/perp | 815,499 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 1.10 | 657 | 96.1% | 0 | 0 | yes |
| 2023-10-24 | bybit_ob/bybit/BTC-USDT/perp | 863,975 | 1.000 | 1.3 | 0 | 0.0 / 0.0 | 0.03 | 515 | 85.0% | 0 | 0 | yes |
| 2023-10-24 | bybit_ob/bybit/DOGE-USDT/perp | 784,293 | 1.000 | 1.6 | 0 | 0.0 / 0.0 | 1.49 | 631 | 96.1% | 0 | 0 | yes |
| 2023-10-24 | bybit_ob/bybit/ETH-USDT/perp | 863,582 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.06 | 459 | 87.9% | 0 | 0 | yes |
| 2023-10-24 | bybit_ob/bybit/SOL-USDT/perp | 856,312 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.32 | 859 | 86.7% | 1 | 0 | yes |
| 2023-10-24 | bybit_ob/bybit/WLD-USDT/perp | 662,376 | 1.000 | 3.5 | 0 | 0.0 / 0.0 | 5.96 | 984 | 97.4% | 0 | 20 | yes |
| 2023-10-24 | bybit_ob/bybit/XRP-USDT/perp | 802,769 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 1.81 | 737 | 89.3% | 1 | 20 | yes |
| 2023-10-24 | bybit_ob/bybit/ZEC-USDT/perp | 179,345 | 0.855 | 14.0 | 0 | 0.0 / 0.0 | 18.23 | 624 | 99.6% | 1 | 0 | NO |
| 2023-10-25 | binance_bt/binance/AAVE-USDT/perp | 193,514 | 0.999 | 7.1 | 0 | 5.0 / 13.0 | 1.21 | 574 | no trade record | - | - | yes |
| 2023-10-25 | binance_bt/binance/ARB-USDT/perp | 123,202 | 1.000 | 6.3 | 0 | 6.0 / 17.0 | 1.12 | 473 | no trade record | - | - | yes |
| 2023-10-25 | binance_bt/binance/BTC-USDT/perp | 554,608 | 1.000 | 6.3 | 0 | 6.0 / 18.0 | 0.03 | 305 | no trade record | - | - | yes |
| 2023-10-25 | binance_bt/binance/DOGE-USDT/perp | 88,611 | 1.000 | 6.2 | 0 | 6.0 / 16.0 | 1.51 | 500 | no trade record | - | - | yes |
| 2023-10-25 | binance_bt/binance/ETH-USDT/perp | 408,472 | 1.000 | 3.9 | 0 | 6.0 / 16.0 | 0.06 | 303 | no trade record | - | - | yes |
| 2023-10-25 | binance_bt/binance/SOL-USDT/perp | 1,905,867 | 1.000 | 6.2 | 0 | 5.0 / 13.0 | 0.62 | 794 | no trade record | - | - | yes |
| 2023-10-25 | binance_bt/binance/WLD-USDT/perp | 898,514 | 1.000 | 7.2 | 0 | 5.0 / 11.0 | 1.17 | 829 | no trade record | - | - | yes |
| 2023-10-25 | binance_bt/binance/XRP-USDT/perp | 33,478 | 1.000 | 6.2 | 0 | 6.0 / 20.0 | 1.81 | 341 | no trade record | - | - | yes |
| 2023-10-25 | binance_bt/binance/ZEC-USDT/perp | 26,895 | 0.970 | 15.6 | 0 | 5.0 / 13.0 | 3.66 | 409 | no trade record | - | - | yes |
| 2023-10-25 | bybit_ob/bybit/AAVE-USDT/perp | 594,268 | 0.999 | 3.6 | 0 | 0.0 / 0.0 | 1.20 | 572 | 93.7% | 1 | 0 | yes |
| 2023-10-25 | bybit_ob/bybit/ARB-USDT/perp | 792,222 | 1.000 | 1.3 | 0 | 0.0 / 0.0 | 1.11 | 469 | 97.7% | 0 | 0 | yes |
| 2023-10-25 | bybit_ob/bybit/BTC-USDT/perp | 863,994 | 1.000 | 1.3 | 0 | 0.0 / 0.0 | 0.03 | 310 | 88.8% | 0 | 0 | yes |
| 2023-10-25 | bybit_ob/bybit/DOGE-USDT/perp | 733,744 | 1.000 | 2.3 | 0 | 0.0 / 0.0 | 1.51 | 511 | 94.1% | 0 | 0 | yes |
| 2023-10-25 | bybit_ob/bybit/ETH-USDT/perp | 862,976 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.06 | 301 | 92.0% | 1 | 0 | yes |
| 2023-10-25 | bybit_ob/bybit/SOL-USDT/perp | 852,989 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 0.31 | 797 | 87.6% | 0 | 0 | yes |
| 2023-10-25 | bybit_ob/bybit/WLD-USDT/perp | 657,062 | 1.000 | 3.3 | 0 | 0.0 / 0.0 | 5.76 | 826 | 97.5% | 0 | 20 | yes |
| 2023-10-25 | bybit_ob/bybit/XRP-USDT/perp | 723,426 | 1.000 | 2.3 | 0 | 0.0 / 0.0 | 1.80 | 349 | 98.2% | 0 | 20 | yes |
| 2023-10-25 | bybit_ob/bybit/ZEC-USDT/perp | 178,686 | 0.851 | 14.7 | 0 | 0.0 / 0.0 | 18.20 | 467 | 99.3% | 0 | 50 | NO |
| 2023-10-26 | binance_bt/binance/AAVE-USDT/perp | 224,464 | 0.996 | 14.1 | 0 | 5.0 / 11.0 | 1.27 | 530 | no trade record | - | - | yes |
| 2023-10-26 | binance_bt/binance/ARB-USDT/perp | 277,144 | 1.000 | 5.6 | 0 | 6.0 / 13.0 | 1.08 | 648 | no trade record | - | - | yes |
| 2023-10-26 | binance_bt/binance/BTC-USDT/perp | 317,886 | 1.000 | 5.5 | 0 | 7.0 / 16.0 | 0.03 | 233 | no trade record | - | - | yes |
| 2023-10-26 | binance_bt/binance/DOGE-USDT/perp | 199,569 | 1.000 | 5.6 | 0 | 6.0 / 11.0 | 1.42 | 680 | no trade record | - | - | yes |
| 2023-10-26 | binance_bt/binance/ETH-USDT/perp | 431,758 | 1.000 | 5.5 | 0 | 6.0 / 14.0 | 0.06 | 337 | no trade record | - | - | yes |
| 2023-10-26 | binance_bt/binance/SOL-USDT/perp | 1,187,290 | 1.000 | 4.7 | 0 | 6.0 / 12.0 | 0.62 | 576 | no trade record | - | - | yes |
| 2023-10-26 | binance_bt/binance/WLD-USDT/perp | 906,504 | 1.000 | 4.1 | 0 | 5.0 / 10.0 | 1.14 | 811 | no trade record | - | - | yes |
| 2023-10-26 | binance_bt/binance/XRP-USDT/perp | 36,551 | 1.000 | 5.2 | 0 | 6.0 / 15.0 | 1.82 | 343 | no trade record | - | - | yes |
| 2023-10-26 | binance_bt/binance/ZEC-USDT/perp | 27,625 | 0.971 | 16.7 | 0 | 6.0 / 11.0 | 3.64 | 414 | no trade record | - | - | yes |
| 2023-10-26 | bybit_ob/bybit/AAVE-USDT/perp | 577,523 | 0.997 | 5.1 | 0 | 0.0 / 0.0 | 1.23 | 534 | 90.9% | 1 | 0 | yes |
| 2023-10-26 | bybit_ob/bybit/ARB-USDT/perp | 817,215 | 1.000 | 1.3 | 0 | 0.0 / 0.0 | 1.05 | 636 | 94.8% | 0 | 0 | yes |
| 2023-10-26 | bybit_ob/bybit/BTC-USDT/perp | 864,001 | 1.000 | 1.3 | 0 | 0.0 / 0.0 | 0.03 | 235 | 92.3% | 1 | 0 | yes |
| 2023-10-26 | bybit_ob/bybit/DOGE-USDT/perp | 792,659 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 1.40 | 681 | 94.7% | 0 | 0 | yes |
| 2023-10-26 | bybit_ob/bybit/ETH-USDT/perp | 863,162 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.06 | 335 | 90.8% | 1 | 0 | yes |
| 2023-10-26 | bybit_ob/bybit/SOL-USDT/perp | 849,010 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 0.31 | 582 | 89.4% | 1 | 0 | yes |
| 2023-10-26 | bybit_ob/bybit/WLD-USDT/perp | 651,016 | 1.000 | 2.9 | 0 | 0.0 / 0.0 | 5.63 | 811 | 98.1% | 0 | 20 | yes |
| 2023-10-26 | bybit_ob/bybit/XRP-USDT/perp | 693,338 | 1.000 | 3.0 | 0 | 0.0 / 0.0 | 1.80 | 347 | 97.9% | 0 | 20 | yes |
| 2023-10-26 | bybit_ob/bybit/ZEC-USDT/perp | 181,214 | 0.868 | 14.3 | 0 | 0.0 / 0.0 | 17.97 | 473 | 99.3% | 0 | 20 | NO |
| 2023-10-27 | binance_bt/binance/AAVE-USDT/perp | 129,608 | 0.991 | 9.9 | 0 | 6.0 / 11.0 | 1.29 | 436 | no trade record | - | - | yes |
| 2023-10-27 | binance_bt/binance/ARB-USDT/perp | 112,653 | 1.000 | 6.9 | 0 | 6.0 / 13.0 | 1.10 | 478 | no trade record | - | - | yes |
| 2023-10-27 | binance_bt/binance/BTC-USDT/perp | 231,941 | 1.000 | 4.7 | 0 | 7.0 / 16.0 | 0.03 | 218 | no trade record | - | - | yes |
| 2023-10-27 | binance_bt/binance/DOGE-USDT/perp | 68,743 | 1.000 | 6.5 | 0 | 6.0 / 13.0 | 1.46 | 435 | no trade record | - | - | yes |
| 2023-10-27 | binance_bt/binance/ETH-USDT/perp | 272,951 | 1.000 | 4.8 | 0 | 6.0 / 14.0 | 0.06 | 257 | no trade record | - | - | yes |
| 2023-10-27 | binance_bt/binance/SOL-USDT/perp | 1,025,826 | 1.000 | 4.8 | 0 | 6.0 / 11.0 | 0.61 | 554 | no trade record | - | - | yes |
| 2023-10-27 | binance_bt/binance/WLD-USDT/perp | 845,016 | 1.000 | 5.8 | 0 | 5.0 / 9.0 | 1.12 | 779 | no trade record | - | - | yes |
| 2023-10-27 | binance_bt/binance/XRP-USDT/perp | 24,899 | 1.000 | 2.1 | 0 | 6.0 / 19.0 | 1.84 | 315 | no trade record | - | - | yes |
| 2023-10-27 | binance_bt/binance/ZEC-USDT/perp | 20,580 | 0.962 | 16.9 | 0 | 5.0 / 10.0 | 3.69 | 343 | no trade record | - | - | yes |
| 2023-10-27 | bybit_ob/bybit/AAVE-USDT/perp | 491,249 | 0.995 | 5.1 | 0 | 0.0 / 0.0 | 1.28 | 434 | 92.9% | 1 | 0 | yes |
| 2023-10-27 | bybit_ob/bybit/ARB-USDT/perp | 799,392 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 1.09 | 471 | 94.8% | 1 | 0 | yes |
| 2023-10-27 | bybit_ob/bybit/BTC-USDT/perp | 863,099 | 1.000 | 1.3 | 0 | 0.0 / 0.0 | 0.03 | 217 | 90.5% | 1 | 0 | yes |
| 2023-10-27 | bybit_ob/bybit/DOGE-USDT/perp | 698,745 | 1.000 | 2.3 | 0 | 0.0 / 0.0 | 1.41 | 437 | 95.4% | 0 | 0 | yes |
| 2023-10-27 | bybit_ob/bybit/ETH-USDT/perp | 861,879 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.06 | 253 | 91.5% | 1 | 0 | yes |
| 2023-10-27 | bybit_ob/bybit/SOL-USDT/perp | 837,147 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 0.31 | 557 | 90.8% | 1 | 0 | yes |
| 2023-10-27 | bybit_ob/bybit/WLD-USDT/perp | 616,662 | 1.000 | 3.7 | 0 | 0.0 / 0.0 | 5.45 | 783 | 98.3% | 0 | 0 | yes |
| 2023-10-27 | bybit_ob/bybit/XRP-USDT/perp | 638,570 | 1.000 | 2.7 | 0 | 0.0 / 0.0 | 1.82 | 315 | 97.2% | 0 | 0 | yes |
| 2023-10-27 | bybit_ob/bybit/ZEC-USDT/perp | 146,267 | 0.834 | 16.1 | 0 | 0.0 / 0.0 | 18.26 | 415 | 99.8% | 0 | 0 | NO |
| 2023-10-28 | binance_bt/binance/AAVE-USDT/perp | 51,504 | 0.965 | 14.2 | 0 | 5.0 / 11.0 | 1.26 | 313 | no trade record | - | - | yes |
| 2023-10-28 | binance_bt/binance/ARB-USDT/perp | 40,286 | 1.000 | 7.5 | 0 | 6.0 / 13.0 | 1.09 | 265 | no trade record | - | - | yes |
| 2023-10-28 | binance_bt/binance/BTC-USDT/perp | 88,797 | 1.000 | 4.7 | 0 | 7.0 / 19.0 | 0.03 | 145 | no trade record | - | - | yes |
| 2023-10-28 | binance_bt/binance/DOGE-USDT/perp | 20,889 | 1.000 | 4.7 | 0 | 6.0 / 12.0 | 1.46 | 235 | no trade record | - | - | yes |
| 2023-10-28 | binance_bt/binance/ETH-USDT/perp | 99,847 | 1.000 | 3.8 | 0 | 6.0 / 15.0 | 0.06 | 143 | no trade record | - | - | yes |
| 2023-10-28 | binance_bt/binance/SOL-USDT/perp | 328,844 | 1.000 | 5.4 | 0 | 5.0 / 11.0 | 0.32 | 321 | no trade record | - | - | yes |
| 2023-10-28 | binance_bt/binance/WLD-USDT/perp | 453,939 | 1.000 | 5.7 | 0 | 5.0 / 9.0 | 1.07 | 551 | no trade record | - | - | yes |
| 2023-10-28 | binance_bt/binance/XRP-USDT/perp | 5,362 | 1.000 | 3.9 | 0 | 6.0 / 15.4 | 1.83 | 143 | no trade record | - | - | yes |
| 2023-10-28 | binance_bt/binance/ZEC-USDT/perp | 10,016 | 0.881 | 22.8 | 0 | 5.0 / 10.0 | 3.62 | 238 | no trade record | - | - | NO |
| 2023-10-28 | bybit_ob/bybit/AAVE-USDT/perp | 343,924 | 0.979 | 5.3 | 0 | 0.0 / 0.0 | 1.25 | 313 | 94.9% | 1 | 0 | yes |
| 2023-10-28 | bybit_ob/bybit/ARB-USDT/perp | 755,496 | 1.000 | 2.1 | 0 | 0.0 / 0.0 | 1.09 | 254 | 98.3% | 1 | 0 | yes |
| 2023-10-28 | bybit_ob/bybit/BTC-USDT/perp | 863,926 | 1.000 | 1.3 | 0 | 0.0 / 0.0 | 0.03 | 150 | 91.0% | 0 | 0 | yes |
| 2023-10-28 | bybit_ob/bybit/DOGE-USDT/perp | 586,802 | 1.000 | 4.6 | 0 | 0.0 / 0.0 | 1.45 | 241 | 96.3% | 1 | 0 | yes |
| 2023-10-28 | bybit_ob/bybit/ETH-USDT/perp | 859,229 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.06 | 142 | 92.4% | 1 | 0 | yes |
| 2023-10-28 | bybit_ob/bybit/SOL-USDT/perp | 793,995 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.31 | 324 | 94.0% | 1 | 0 | yes |
| 2023-10-28 | bybit_ob/bybit/WLD-USDT/perp | 493,258 | 0.998 | 5.0 | 0 | 0.0 / 0.0 | 5.35 | 554 | 97.8% | 0 | 20 | yes |
| 2023-10-28 | bybit_ob/bybit/XRP-USDT/perp | 547,523 | 1.000 | 3.5 | 0 | 0.0 / 0.0 | 1.83 | 141 | 99.4% | 0 | 20 | yes |
| 2023-10-28 | bybit_ob/bybit/ZEC-USDT/perp | 103,205 | 0.699 | 16.2 | 0 | 0.0 / 0.0 | 17.97 | 298 | 99.7% | 0 | 0 | NO |
| 2023-10-29 | binance_bt/binance/AAVE-USDT/perp | 79,782 | 0.980 | 14.2 | 0 | 5.0 / 13.0 | 1.25 | 379 | no trade record | - | - | yes |
| 2023-10-29 | binance_bt/binance/ARB-USDT/perp | 52,665 | 1.000 | 8.4 | 0 | 6.0 / 17.0 | 1.09 | 332 | no trade record | - | - | yes |
| 2023-10-29 | binance_bt/binance/BTC-USDT/perp | 111,165 | 1.000 | 5.2 | 0 | 7.0 / 23.0 | 0.03 | 149 | no trade record | - | - | yes |
| 2023-10-29 | binance_bt/binance/DOGE-USDT/perp | 27,209 | 1.000 | 6.4 | 0 | 6.0 / 18.0 | 1.46 | 247 | no trade record | - | - | yes |
| 2023-10-29 | binance_bt/binance/ETH-USDT/perp | 109,286 | 1.000 | 4.7 | 0 | 6.0 / 20.0 | 0.06 | 154 | no trade record | - | - | yes |
| 2023-10-29 | binance_bt/binance/SOL-USDT/perp | 389,055 | 1.000 | 5.6 | 0 | 5.0 / 13.0 | 0.60 | 341 | no trade record | - | - | yes |
| 2023-10-29 | binance_bt/binance/WLD-USDT/perp | 313,196 | 1.000 | 6.5 | 0 | 5.0 / 11.0 | 1.08 | 442 | no trade record | - | - | yes |
| 2023-10-29 | binance_bt/binance/XRP-USDT/perp | 9,197 | 1.000 | 5.6 | 0 | 6.0 / 19.0 | 1.81 | 200 | no trade record | - | - | yes |
| 2023-10-29 | binance_bt/binance/ZEC-USDT/perp | 11,412 | 0.903 | 21.4 | 0 | 5.0 / 13.0 | 3.60 | 234 | no trade record | - | - | NO |
| 2023-10-29 | bybit_ob/bybit/AAVE-USDT/perp | 421,164 | 0.991 | 5.7 | 0 | 0.0 / 0.0 | 1.21 | 385 | 95.8% | 0 | 0 | yes |
| 2023-10-29 | bybit_ob/bybit/ARB-USDT/perp | 761,115 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 1.08 | 322 | 97.8% | 1 | 0 | yes |
| 2023-10-29 | bybit_ob/bybit/BTC-USDT/perp | 863,993 | 1.000 | 1.3 | 0 | 0.0 / 0.0 | 0.03 | 151 | 92.1% | 1 | 0 | yes |
| 2023-10-29 | bybit_ob/bybit/DOGE-USDT/perp | 571,854 | 1.000 | 2.8 | 0 | 0.0 / 0.0 | 1.45 | 254 | 94.7% | 1 | 0 | yes |
| 2023-10-29 | bybit_ob/bybit/ETH-USDT/perp | 859,868 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.06 | 155 | 92.5% | 1 | 0 | yes |
| 2023-10-29 | bybit_ob/bybit/SOL-USDT/perp | 804,559 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 0.31 | 346 | 92.4% | 1 | 0 | yes |
| 2023-10-29 | bybit_ob/bybit/WLD-USDT/perp | 468,217 | 0.999 | 4.2 | 0 | 0.0 / 0.0 | 5.45 | 451 | 98.8% | 0 | 20 | yes |
| 2023-10-29 | bybit_ob/bybit/XRP-USDT/perp | 611,406 | 1.000 | 3.1 | 0 | 0.0 / 0.0 | 1.80 | 201 | 99.5% | 0 | 0 | yes |
| 2023-10-29 | bybit_ob/bybit/ZEC-USDT/perp | 114,968 | 0.741 | 15.8 | 0 | 0.0 / 0.0 | 17.94 | 304 | 99.1% | 0 | 0 | NO |
| 2023-10-30 | binance_bt/binance/AAVE-USDT/perp | 111,782 | 0.987 | 10.2 | 0 | 6.0 / 12.0 | 1.21 | 422 | no trade record | - | - | yes |
| 2023-10-30 | binance_bt/binance/ARB-USDT/perp | 82,914 | 1.000 | 6.8 | 0 | 6.0 / 14.0 | 1.06 | 374 | no trade record | - | - | yes |
| 2023-10-30 | binance_bt/binance/BTC-USDT/perp | 193,329 | 1.000 | 3.6 | 0 | 7.0 / 18.0 | 0.03 | 198 | no trade record | - | - | yes |
| 2023-10-30 | binance_bt/binance/DOGE-USDT/perp | 37,028 | 1.000 | 4.9 | 0 | 6.0 / 16.0 | 1.45 | 279 | no trade record | - | - | yes |
| 2023-10-30 | binance_bt/binance/ETH-USDT/perp | 208,981 | 1.000 | 4.9 | 0 | 6.0 / 16.0 | 0.06 | 231 | no trade record | - | - | yes |
| 2023-10-30 | binance_bt/binance/SOL-USDT/perp | 817,197 | 1.000 | 6.8 | 0 | 6.0 / 12.0 | 0.57 | 509 | no trade record | - | - | yes |
| 2023-10-30 | binance_bt/binance/WLD-USDT/perp | 507,177 | 1.000 | 6.8 | 0 | 5.0 / 10.0 | 1.06 | 569 | no trade record | - | - | yes |
| 2023-10-30 | binance_bt/binance/XRP-USDT/perp | 26,513 | 1.000 | 4.0 | 0 | 6.0 / 14.0 | 1.75 | 356 | no trade record | - | - | yes |
| 2023-10-30 | binance_bt/binance/ZEC-USDT/perp | 13,771 | 0.956 | 20.9 | 0 | 6.0 / 11.0 | 3.54 | 293 | no trade record | - | - | yes |
| 2023-10-30 | bybit_ob/bybit/AAVE-USDT/perp | 467,110 | 0.995 | 4.7 | 0 | 0.0 / 0.0 | 1.19 | 419 | 93.8% | 1 | 0 | yes |
| 2023-10-30 | bybit_ob/bybit/ARB-USDT/perp | 775,837 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 1.05 | 366 | 94.9% | 1 | 0 | yes |
| 2023-10-30 | bybit_ob/bybit/BTC-USDT/perp | 863,938 | 1.000 | 1.3 | 0 | 0.0 / 0.0 | 0.03 | 201 | 90.1% | 0 | 0 | yes |
| 2023-10-30 | bybit_ob/bybit/DOGE-USDT/perp | 644,187 | 1.000 | 2.8 | 0 | 0.0 / 0.0 | 1.44 | 281 | 95.2% | 1 | 20 | yes |
| 2023-10-30 | bybit_ob/bybit/ETH-USDT/perp | 862,343 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.06 | 233 | 90.7% | 1 | 0 | yes |
| 2023-10-30 | bybit_ob/bybit/SOL-USDT/perp | 820,830 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 0.29 | 516 | 88.3% | 0 | 0 | yes |
| 2023-10-30 | bybit_ob/bybit/WLD-USDT/perp | 541,439 | 0.999 | 4.9 | 0 | 0.0 / 0.0 | 5.33 | 567 | 98.7% | 0 | 20 | yes |
| 2023-10-30 | bybit_ob/bybit/XRP-USDT/perp | 699,120 | 1.000 | 2.0 | 0 | 0.0 / 0.0 | 1.77 | 358 | 97.6% | 0 | 20 | yes |
| 2023-10-30 | bybit_ob/bybit/ZEC-USDT/perp | 134,490 | 0.810 | 15.3 | 0 | 0.0 / 0.0 | 17.62 | 371 | 99.5% | 0 | 0 | NO |
| 2023-10-31 | binance_bt/binance/AAVE-USDT/perp | 126,763 | 0.984 | 10.0 | 0 | 6.0 / 11.0 | 1.24 | 446 | no trade record | - | - | yes |
| 2023-10-31 | binance_bt/binance/ARB-USDT/perp | 109,511 | 1.000 | 6.6 | 0 | 6.0 / 13.0 | 1.07 | 436 | no trade record | - | - | yes |
| 2023-10-31 | binance_bt/binance/BTC-USDT/perp | 190,822 | 1.000 | 6.6 | 0 | 7.0 / 15.0 | 0.03 | 175 | no trade record | - | - | yes |
| 2023-10-31 | binance_bt/binance/DOGE-USDT/perp | 56,835 | 1.000 | 5.8 | 0 | 6.0 / 13.0 | 1.47 | 394 | no trade record | - | - | yes |
| 2023-10-31 | binance_bt/binance/ETH-USDT/perp | 201,956 | 1.000 | 5.3 | 0 | 6.0 / 14.0 | 0.06 | 205 | no trade record | - | - | yes |
| 2023-10-31 | binance_bt/binance/SOL-USDT/perp | 1,154,852 | 1.000 | 6.6 | 0 | 6.0 / 11.0 | 0.55 | 554 | no trade record | - | - | yes |
| 2023-10-31 | binance_bt/binance/TIA-USDT/perp | 605,804 | 0.250 | 64800.7 | 0 | 5.0 / 8.0 | 5.15 | 1287 | no trade record | - | - | NO |
| 2023-10-31 | binance_bt/binance/WLD-USDT/perp | 766,235 | 1.000 | 6.6 | 0 | 5.0 / 9.0 | 1.04 | 680 | no trade record | - | - | yes |
| 2023-10-31 | binance_bt/binance/XRP-USDT/perp | 77,420 | 1.000 | 3.6 | 0 | 6.0 / 11.0 | 1.69 | 522 | no trade record | - | - | yes |
| 2023-10-31 | binance_bt/binance/ZEC-USDT/perp | 17,110 | 0.959 | 14.7 | 0 | 6.0 / 10.0 | 3.56 | 389 | no trade record | - | - | yes |
| 2023-10-31 | bybit_ob/bybit/AAVE-USDT/perp | 472,966 | 0.997 | 4.8 | 0 | 0.0 / 0.0 | 1.22 | 442 | 93.6% | 1 | 0 | yes |
| 2023-10-31 | bybit_ob/bybit/ARB-USDT/perp | 773,918 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 1.05 | 430 | 94.1% | 1 | 0 | yes |
| 2023-10-31 | bybit_ob/bybit/BTC-USDT/perp | 864,002 | 1.000 | 1.3 | 0 | 0.0 / 0.0 | 0.03 | 177 | 91.7% | 1 | 0 | yes |
| 2023-10-31 | bybit_ob/bybit/DOGE-USDT/perp | 672,283 | 1.000 | 3.1 | 0 | 0.0 / 0.0 | 1.45 | 395 | 94.1% | 0 | 0 | yes |
| 2023-10-31 | bybit_ob/bybit/ETH-USDT/perp | 862,659 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.06 | 206 | 91.9% | 1 | 0 | yes |
| 2023-10-31 | bybit_ob/bybit/SOL-USDT/perp | 850,881 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 0.28 | 558 | 89.1% | 1 | 0 | yes |
| 2023-10-31 | bybit_ob/bybit/TIA-USDT/perp | 214,413 | 0.273 | 61264.4 | 0 | 0.0 / 0.0 | 6.16 | 1368 | 81.7% | 0 | 20 | NO |
| 2023-10-31 | bybit_ob/bybit/WLD-USDT/perp | 620,557 | 1.000 | 2.9 | 0 | 0.0 / 0.0 | 5.07 | 677 | 98.7% | 0 | 20 | yes |
| 2023-10-31 | bybit_ob/bybit/XRP-USDT/perp | 740,981 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 1.68 | 530 | 95.3% | 0 | 20 | yes |
| 2023-10-31 | bybit_ob/bybit/ZEC-USDT/perp | 143,422 | 0.813 | 15.7 | 0 | 0.0 / 0.0 | 17.68 | 453 | 98.9% | 0 | 50 | NO |
| 2023-11-01 | binance_bt/binance/AAVE-USDT/perp | 315,131 | 0.992 | 11.3 | 0 | 6.0 / 10.0 | 1.23 | 713 | no trade record | - | - | yes |
| 2023-11-01 | binance_bt/binance/ARB-USDT/perp | 220,235 | 1.000 | 6.4 | 0 | 6.0 / 13.0 | 1.07 | 568 | no trade record | - | - | yes |
| 2023-11-01 | binance_bt/binance/BTC-USDT/perp | 382,778 | 1.000 | 6.2 | 0 | 7.0 / 19.0 | 0.03 | 263 | no trade record | - | - | yes |
| 2023-11-01 | binance_bt/binance/DOGE-USDT/perp | 59,205 | 1.000 | 6.2 | 0 | 6.0 / 13.0 | 1.50 | 362 | no trade record | - | - | yes |
| 2023-11-01 | binance_bt/binance/ETH-USDT/perp | 341,181 | 1.000 | 6.2 | 0 | 6.0 / 15.0 | 0.06 | 291 | no trade record | - | - | yes |
| 2023-11-01 | binance_bt/binance/SOL-USDT/perp | 3,710,799 | 1.000 | 4.8 | 0 | 6.0 / 11.0 | 0.53 | 1022 | no trade record | - | - | yes |
| 2023-11-01 | binance_bt/binance/TIA-USDT/perp | 1,264,325 | 1.000 | 6.5 | 0 | 5.0 / 8.0 | 3.48 | 1736 | no trade record | - | - | yes |
| 2023-11-01 | binance_bt/binance/WLD-USDT/perp | 662,486 | 1.000 | 6.8 | 0 | 6.0 / 10.0 | 1.05 | 609 | no trade record | - | - | yes |
| 2023-11-01 | binance_bt/binance/XRP-USDT/perp | 46,746 | 1.000 | 4.3 | 0 | 6.0 / 14.0 | 1.67 | 416 | no trade record | - | - | yes |
| 2023-11-01 | binance_bt/binance/ZEC-USDT/perp | 21,812 | 0.951 | 15.7 | 0 | 6.0 / 11.0 | 3.61 | 389 | no trade record | - | - | yes |
| 2023-11-01 | bybit_ob/bybit/AAVE-USDT/perp | 580,072 | 0.998 | 4.7 | 0 | 0.0 / 0.0 | 1.22 | 714 | 89.2% | 1 | 0 | yes |
| 2023-11-01 | bybit_ob/bybit/ARB-USDT/perp | 784,841 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 1.05 | 562 | 93.4% | 1 | 0 | yes |
| 2023-11-01 | bybit_ob/bybit/BTC-USDT/perp | 863,994 | 1.000 | 1.3 | 0 | 0.0 / 0.0 | 0.03 | 265 | 84.8% | 2 | 0 | yes |
| 2023-11-01 | bybit_ob/bybit/DOGE-USDT/perp | 676,886 | 1.000 | 2.8 | 0 | 0.0 / 0.0 | 1.49 | 374 | 97.1% | 1 | 0 | yes |
| 2023-11-01 | bybit_ob/bybit/ETH-USDT/perp | 863,069 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.06 | 292 | 87.5% | 1 | 0 | yes |
| 2023-11-01 | bybit_ob/bybit/SOL-USDT/perp | 857,200 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 0.26 | 1018 | 78.6% | 2 | 0 | yes |
| 2023-11-01 | bybit_ob/bybit/TIA-USDT/perp | 808,512 | 1.000 | 1.3 | 0 | 0.0 / 0.0 | 2.23 | 1743 | 83.2% | 1 | 20 | yes |
| 2023-11-01 | bybit_ob/bybit/WLD-USDT/perp | 609,041 | 1.000 | 2.9 | 0 | 0.0 / 0.0 | 5.22 | 613 | 98.8% | 0 | 0 | yes |
| 2023-11-01 | bybit_ob/bybit/XRP-USDT/perp | 761,581 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 1.67 | 424 | 95.4% | 1 | 20 | yes |
| 2023-11-01 | bybit_ob/bybit/ZEC-USDT/perp | 172,698 | 0.850 | 13.8 | 0 | 0.0 / 0.0 | 17.97 | 442 | 99.0% | 0 | 0 | NO |
| 2023-11-02 | binance_bt/binance/AAVE-USDT/perp | 656,635 | 0.998 | 8.5 | 0 | 5.0 / 10.0 | 2.03 | 1003 | no trade record | - | - | yes |
| 2023-11-02 | binance_bt/binance/ARB-USDT/perp | 198,598 | 1.000 | 3.3 | 0 | 6.0 / 13.0 | 1.02 | 525 | no trade record | - | - | yes |
| 2023-11-02 | binance_bt/binance/BTC-USDT/perp | 347,505 | 1.000 | 4.7 | 0 | 7.0 / 18.0 | 0.03 | 231 | no trade record | - | - | yes |
| 2023-11-02 | binance_bt/binance/DOGE-USDT/perp | 67,187 | 1.000 | 3.1 | 0 | 6.0 / 14.0 | 1.47 | 405 | no trade record | - | - | yes |
| 2023-11-02 | binance_bt/binance/ETH-USDT/perp | 288,222 | 1.000 | 4.8 | 0 | 6.0 / 15.0 | 0.06 | 240 | no trade record | - | - | yes |
| 2023-11-02 | binance_bt/binance/SOL-USDT/perp | 3,210,061 | 1.000 | 4.0 | 0 | 6.0 / 11.0 | 0.49 | 890 | no trade record | - | - | yes |
| 2023-11-02 | binance_bt/binance/TIA-USDT/perp | 1,151,730 | 1.000 | 7.3 | 0 | 5.0 / 8.0 | 3.09 | 1634 | no trade record | - | - | yes |
| 2023-11-02 | binance_bt/binance/WLD-USDT/perp | 626,057 | 1.000 | 5.0 | 0 | 6.0 / 10.0 | 1.14 | 577 | no trade record | - | - | yes |
| 2023-11-02 | binance_bt/binance/XRP-USDT/perp | 50,372 | 1.000 | 4.7 | 0 | 6.0 / 15.0 | 1.65 | 419 | no trade record | - | - | yes |
| 2023-11-02 | binance_bt/binance/ZEC-USDT/perp | 24,878 | 0.965 | 15.3 | 0 | 6.0 / 11.0 | 3.63 | 414 | no trade record | - | - | yes |
| 2023-11-02 | bybit_ob/bybit/AAVE-USDT/perp | 697,293 | 1.000 | 5.1 | 0 | 0.0 / 0.0 | 1.08 | 995 | 88.4% | 1 | 0 | yes |
| 2023-11-02 | bybit_ob/bybit/ARB-USDT/perp | 816,460 | 1.000 | 0.9 | 0 | 0.0 / 0.0 | 1.00 | 524 | 89.8% | 1 | 0 | yes |
| 2023-11-02 | bybit_ob/bybit/BTC-USDT/perp | 863,998 | 1.000 | 1.3 | 0 | 0.0 / 0.0 | 0.03 | 233 | 88.6% | 1 | 0 | yes |
| 2023-11-02 | bybit_ob/bybit/DOGE-USDT/perp | 691,484 | 1.000 | 2.5 | 0 | 0.0 / 0.0 | 1.45 | 413 | 95.5% | 1 | 20 | yes |
| 2023-11-02 | bybit_ob/bybit/ETH-USDT/perp | 863,152 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.05 | 240 | 92.2% | 0 | 0 | yes |
| 2023-11-02 | bybit_ob/bybit/SOL-USDT/perp | 859,845 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 0.24 | 895 | 78.6% | 1 | 0 | yes |
| 2023-11-02 | bybit_ob/bybit/TIA-USDT/perp | 817,810 | 1.000 | 1.3 | 0 | 0.0 / 0.0 | 1.99 | 1629 | 84.6% | 1 | 0 | yes |
| 2023-11-02 | bybit_ob/bybit/WLD-USDT/perp | 607,598 | 1.000 | 3.0 | 0 | 0.0 / 0.0 | 5.39 | 578 | 98.4% | 0 | 20 | yes |
| 2023-11-02 | bybit_ob/bybit/XRP-USDT/perp | 735,287 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 1.64 | 425 | 94.1% | 1 | 0 | yes |
| 2023-11-02 | bybit_ob/bybit/ZEC-USDT/perp | 176,017 | 0.880 | 12.7 | 0 | 0.0 / 0.0 | 17.75 | 464 | 99.4% | 0 | 50 | NO |
| 2023-11-03 | binance_bt/binance/AAVE-USDT/perp | 334,438 | 0.995 | 10.8 | 0 | 5.0 / 11.0 | 2.20 | 524 | no trade record | - | - | yes |
| 2023-11-03 | binance_bt/binance/ARB-USDT/perp | 352,339 | 1.000 | 6.9 | 0 | 5.0 / 11.0 | 1.88 | 646 | no trade record | - | - | yes |
| 2023-11-03 | binance_bt/binance/BTC-USDT/perp | 266,802 | 1.000 | 6.9 | 0 | 7.0 / 16.0 | 0.03 | 213 | no trade record | - | - | yes |
| 2023-11-03 | binance_bt/binance/DOGE-USDT/perp | 32,039 | 1.000 | 6.9 | 0 | 6.0 / 15.0 | 1.49 | 299 | no trade record | - | - | yes |
| 2023-11-03 | binance_bt/binance/ETH-USDT/perp | 230,198 | 1.000 | 6.1 | 0 | 6.0 / 15.0 | 0.06 | 229 | no trade record | - | - | yes |
| 2023-11-03 | binance_bt/binance/SOL-USDT/perp | 2,369,697 | 1.000 | 6.9 | 0 | 5.0 / 11.0 | 0.77 | 763 | no trade record | - | - | yes |
| 2023-11-03 | binance_bt/binance/TIA-USDT/perp | 951,926 | 1.000 | 6.2 | 0 | 5.0 / 8.0 | 3.41 | 1020 | no trade record | - | - | yes |
| 2023-11-03 | binance_bt/binance/WLD-USDT/perp | 433,720 | 0.999 | 8.1 | 0 | 5.0 / 10.0 | 1.67 | 510 | no trade record | - | - | yes |
| 2023-11-03 | binance_bt/binance/XRP-USDT/perp | 28,550 | 1.000 | 5.5 | 0 | 6.0 / 14.0 | 1.66 | 356 | no trade record | - | - | yes |
| 2023-11-03 | binance_bt/binance/ZEC-USDT/perp | 18,802 | 0.954 | 23.6 | 0 | 5.0 / 11.0 | 3.70 | 341 | no trade record | - | - | yes |
| 2023-11-03 | bybit_ob/bybit/AAVE-USDT/perp | 593,323 | 0.999 | 4.0 | 0 | 0.0 / 0.0 | 1.11 | 523 | 93.4% | 1 | 0 | yes |
| 2023-11-03 | bybit_ob/bybit/ARB-USDT/perp | 825,260 | 1.000 | 1.0 | 0 | 0.0 / 0.0 | 1.04 | 643 | 91.3% | 0 | 0 | yes |
| 2023-11-03 | bybit_ob/bybit/BTC-USDT/perp | 864,000 | 1.000 | 1.3 | 0 | 0.0 / 0.0 | 0.03 | 214 | 89.4% | 0 | 0 | yes |
| 2023-11-03 | bybit_ob/bybit/DOGE-USDT/perp | 586,699 | 1.000 | 3.2 | 0 | 0.0 / 0.0 | 1.48 | 304 | 97.5% | 1 | 0 | yes |
| 2023-11-03 | bybit_ob/bybit/ETH-USDT/perp | 863,172 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.06 | 228 | 92.2% | 1 | 0 | yes |
| 2023-11-03 | bybit_ob/bybit/SOL-USDT/perp | 856,548 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 0.26 | 767 | 84.0% | 1 | 0 | yes |
| 2023-11-03 | bybit_ob/bybit/TIA-USDT/perp | 790,295 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 1.74 | 1023 | 88.3% | 1 | 0 | yes |
| 2023-11-03 | bybit_ob/bybit/WLD-USDT/perp | 573,036 | 1.000 | 4.0 | 0 | 0.0 / 0.0 | 5.56 | 508 | 99.5% | 0 | 0 | yes |
| 2023-11-03 | bybit_ob/bybit/XRP-USDT/perp | 701,471 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 1.65 | 361 | 96.5% | 0 | 0 | yes |
| 2023-11-03 | bybit_ob/bybit/ZEC-USDT/perp | 143,861 | 0.823 | 14.2 | 0 | 0.0 / 0.0 | 18.43 | 409 | 99.1% | 1 | 0 | NO |
| 2023-11-04 | binance_bt/binance/AAVE-USDT/perp | 182,346 | 0.984 | 11.8 | 0 | 5.0 / 9.0 | 1.13 | 438 | no trade record | - | - | yes |
| 2023-11-04 | binance_bt/binance/ARB-USDT/perp | 261,825 | 1.000 | 5.0 | 0 | 5.0 / 10.0 | 0.95 | 465 | no trade record | - | - | yes |
| 2023-11-04 | binance_bt/binance/BTC-USDT/perp | 86,794 | 1.000 | 4.5 | 0 | 7.0 / 15.0 | 0.03 | 125 | no trade record | - | - | yes |
| 2023-11-04 | binance_bt/binance/DOGE-USDT/perp | 17,593 | 1.000 | 4.3 | 0 | 6.0 / 11.0 | 1.46 | 205 | no trade record | - | - | yes |
| 2023-11-04 | binance_bt/binance/ETH-USDT/perp | 126,149 | 1.000 | 4.4 | 0 | 6.0 / 12.0 | 0.05 | 159 | no trade record | - | - | yes |
| 2023-11-04 | binance_bt/binance/SOL-USDT/perp | 1,853,750 | 1.000 | 2.9 | 0 | 5.0 / 10.0 | 0.71 | 583 | no trade record | - | - | yes |
| 2023-11-04 | binance_bt/binance/TIA-USDT/perp | 641,545 | 0.994 | 8.6 | 0 | 5.0 / 8.0 | 2.44 | 718 | no trade record | - | - | yes |
| 2023-11-04 | binance_bt/binance/WLD-USDT/perp | 279,273 | 0.995 | 8.4 | 0 | 5.0 / 9.0 | 1.59 | 395 | no trade record | - | - | yes |
| 2023-11-04 | binance_bt/binance/XRP-USDT/perp | 11,796 | 1.000 | 5.1 | 0 | 6.0 / 12.0 | 1.63 | 196 | no trade record | - | - | yes |
| 2023-11-04 | binance_bt/binance/ZEC-USDT/perp | 15,959 | 0.904 | 25.5 | 0 | 5.0 / 9.0 | 3.61 | 275 | no trade record | - | - | NO |
| 2023-11-04 | bybit_ob/bybit/AAVE-USDT/perp | 485,722 | 0.998 | 4.3 | 0 | 0.0 / 0.0 | 1.12 | 437 | 92.6% | 1 | 0 | yes |
| 2023-11-04 | bybit_ob/bybit/ARB-USDT/perp | 804,616 | 1.000 | 1.0 | 0 | 0.0 / 0.0 | 0.94 | 464 | 91.7% | 1 | 0 | yes |
| 2023-11-04 | bybit_ob/bybit/BTC-USDT/perp | 863,981 | 1.000 | 1.3 | 0 | 0.0 / 0.0 | 0.03 | 124 | 89.6% | 1 | 0 | yes |
| 2023-11-04 | bybit_ob/bybit/DOGE-USDT/perp | 495,928 | 1.000 | 4.1 | 0 | 0.0 / 0.0 | 1.46 | 208 | 95.8% | 1 | 0 | yes |
| 2023-11-04 | bybit_ob/bybit/ETH-USDT/perp | 861,084 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.05 | 158 | 93.5% | 0 | 0 | yes |
| 2023-11-04 | bybit_ob/bybit/SOL-USDT/perp | 845,516 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 0.24 | 589 | 84.3% | 1 | 0 | yes |
| 2023-11-04 | bybit_ob/bybit/TIA-USDT/perp | 678,130 | 1.000 | 3.4 | 0 | 0.0 / 0.0 | 1.24 | 710 | 90.6% | 1 | 0 | yes |
| 2023-11-04 | bybit_ob/bybit/WLD-USDT/perp | 460,421 | 0.997 | 4.8 | 0 | 0.0 / 0.0 | 5.35 | 394 | 99.1% | 1 | 20 | yes |
| 2023-11-04 | bybit_ob/bybit/XRP-USDT/perp | 588,888 | 1.000 | 2.8 | 0 | 0.0 / 0.0 | 1.63 | 192 | 97.0% | 0 | 0 | yes |
| 2023-11-04 | bybit_ob/bybit/ZEC-USDT/perp | 132,272 | 0.810 | 17.4 | 0 | 0.0 / 0.0 | 17.97 | 340 | 99.7% | 0 | 20 | NO |
| 2023-11-05 | binance_bt/binance/AAVE-USDT/perp | 278,851 | 0.993 | 11.7 | 0 | 6.0 / 9.0 | 2.18 | 491 | no trade record | - | - | yes |
| 2023-11-05 | binance_bt/binance/ARB-USDT/perp | 268,911 | 1.000 | 4.8 | 0 | 6.0 / 11.0 | 1.81 | 482 | no trade record | - | - | yes |
| 2023-11-05 | binance_bt/binance/BTC-USDT/perp | 167,395 | 1.000 | 1.7 | 0 | 7.0 / 16.0 | 0.03 | 178 | no trade record | - | - | yes |
| 2023-11-05 | binance_bt/binance/DOGE-USDT/perp | 55,026 | 1.000 | 2.5 | 0 | 6.0 / 12.0 | 1.43 | 356 | no trade record | - | - | yes |
| 2023-11-05 | binance_bt/binance/ETH-USDT/perp | 287,267 | 1.000 | 1.4 | 0 | 6.0 / 13.0 | 0.05 | 245 | no trade record | - | - | yes |
| 2023-11-05 | binance_bt/binance/SOL-USDT/perp | 1,125,993 | 1.000 | 2.4 | 0 | 6.0 / 10.0 | 0.49 | 433 | no trade record | - | - | yes |
| 2023-11-05 | binance_bt/binance/TIA-USDT/perp | 533,292 | 0.989 | 10.1 | 0 | 5.0 / 8.0 | 2.08 | 626 | no trade record | - | - | yes |
| 2023-11-05 | binance_bt/binance/WLD-USDT/perp | 324,584 | 0.995 | 8.8 | 0 | 6.0 / 9.0 | 1.62 | 422 | no trade record | - | - | yes |
| 2023-11-05 | binance_bt/binance/XRP-USDT/perp | 72,632 | 1.000 | 1.8 | 0 | 6.0 / 11.0 | 1.57 | 455 | no trade record | - | - | yes |
| 2023-11-05 | binance_bt/binance/ZEC-USDT/perp | 23,282 | 0.950 | 17.3 | 0 | 6.0 / 10.0 | 3.53 | 347 | no trade record | - | - | yes |
| 2023-11-05 | bybit_ob/bybit/AAVE-USDT/perp | 550,067 | 0.999 | 3.4 | 0 | 0.0 / 0.0 | 1.12 | 488 | 91.4% | 1 | 0 | yes |
| 2023-11-05 | bybit_ob/bybit/ARB-USDT/perp | 804,697 | 1.000 | 1.1 | 0 | 0.0 / 0.0 | 0.92 | 487 | 91.7% | 1 | 0 | yes |
| 2023-11-05 | bybit_ob/bybit/BTC-USDT/perp | 863,991 | 1.000 | 1.3 | 0 | 0.0 / 0.0 | 0.03 | 178 | 87.4% | 1 | 0 | yes |
| 2023-11-05 | bybit_ob/bybit/DOGE-USDT/perp | 633,114 | 1.000 | 2.4 | 0 | 0.0 / 0.0 | 1.43 | 356 | 94.3% | 1 | 0 | yes |
| 2023-11-05 | bybit_ob/bybit/ETH-USDT/perp | 863,248 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.05 | 244 | 91.2% | 1 | 0 | yes |
| 2023-11-05 | bybit_ob/bybit/SOL-USDT/perp | 844,503 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 0.24 | 438 | 87.3% | 1 | 0 | yes |
| 2023-11-05 | bybit_ob/bybit/TIA-USDT/perp | 703,500 | 1.000 | 2.9 | 0 | 0.0 / 0.0 | 0.86 | 628 | 88.6% | 1 | 0 | yes |
| 2023-11-05 | bybit_ob/bybit/WLD-USDT/perp | 480,612 | 0.999 | 4.0 | 0 | 0.0 / 0.0 | 5.44 | 427 | 98.8% | 1 | 20 | yes |
| 2023-11-05 | bybit_ob/bybit/XRP-USDT/perp | 703,397 | 1.000 | 2.1 | 0 | 0.0 / 0.0 | 1.56 | 460 | 93.6% | 1 | 0 | yes |
| 2023-11-05 | bybit_ob/bybit/ZEC-USDT/perp | 152,927 | 0.843 | 11.7 | 0 | 0.0 / 0.0 | 17.59 | 410 | 98.5% | 0 | 0 | NO |
| 2023-11-06 | binance_bt/binance/AAVE-USDT/perp | 355,122 | 0.996 | 11.6 | 0 | 5.0 / 9.0 | 1.13 | 639 | no trade record | - | - | yes |
| 2023-11-06 | binance_bt/binance/ARB-USDT/perp | 302,207 | 1.000 | 5.7 | 0 | 6.0 / 10.0 | 1.77 | 499 | no trade record | - | - | yes |
| 2023-11-06 | binance_bt/binance/BTC-USDT/perp | 153,858 | 1.000 | 5.1 | 0 | 6.0 / 13.0 | 0.03 | 156 | no trade record | - | - | yes |
| 2023-11-06 | binance_bt/binance/DOGE-USDT/perp | 99,802 | 1.000 | 5.1 | 0 | 6.0 / 10.0 | 1.38 | 504 | no trade record | - | - | yes |
| 2023-11-06 | binance_bt/binance/ETH-USDT/perp | 217,788 | 1.000 | 5.1 | 0 | 6.0 / 11.0 | 0.05 | 219 | no trade record | - | - | yes |
| 2023-11-06 | binance_bt/binance/SOL-USDT/perp | 1,101,870 | 1.000 | 5.1 | 0 | 5.0 / 10.0 | 0.50 | 481 | no trade record | - | - | yes |
| 2023-11-06 | binance_bt/binance/TIA-USDT/perp | 531,865 | 0.977 | 12.2 | 0 | 5.0 / 8.0 | 2.15 | 555 | no trade record | - | - | yes |
| 2023-11-06 | binance_bt/binance/WLD-USDT/perp | 320,268 | 0.995 | 8.1 | 0 | 5.0 / 9.0 | 1.65 | 398 | no trade record | - | - | yes |
| 2023-11-06 | binance_bt/binance/XRP-USDT/perp | 172,839 | 1.000 | 5.2 | 0 | 6.0 / 9.0 | 1.45 | 584 | no trade record | - | - | yes |
| 2023-11-06 | binance_bt/binance/ZEC-USDT/perp | 26,983 | 0.960 | 15.1 | 0 | 5.0 / 9.0 | 3.47 | 373 | no trade record | - | - | yes |
| 2023-11-06 | bybit_ob/bybit/AAVE-USDT/perp | 615,781 | 1.000 | 3.4 | 0 | 0.0 / 0.0 | 1.05 | 632 | 91.4% | 1 | 0 | yes |
| 2023-11-06 | bybit_ob/bybit/ARB-USDT/perp | 814,979 | 1.000 | 0.9 | 0 | 0.0 / 0.0 | 0.90 | 503 | 89.7% | 1 | 0 | yes |
| 2023-11-06 | bybit_ob/bybit/BTC-USDT/perp | 864,002 | 1.000 | 1.3 | 0 | 0.0 / 0.0 | 0.03 | 157 | 93.1% | 1 | 0 | yes |
| 2023-11-06 | bybit_ob/bybit/DOGE-USDT/perp | 726,281 | 1.000 | 2.7 | 0 | 0.0 / 0.0 | 1.38 | 509 | 94.0% | 0 | 0 | yes |
| 2023-11-06 | bybit_ob/bybit/ETH-USDT/perp | 863,289 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.05 | 219 | 92.8% | 1 | 0 | yes |
| 2023-11-06 | bybit_ob/bybit/SOL-USDT/perp | 849,398 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 0.25 | 483 | 86.7% | 2 | 0 | yes |
| 2023-11-06 | bybit_ob/bybit/TIA-USDT/perp | 626,925 | 1.000 | 4.1 | 0 | 0.0 / 0.0 | 1.29 | 554 | 92.7% | 1 | 0 | yes |
| 2023-11-06 | bybit_ob/bybit/WLD-USDT/perp | 483,381 | 0.999 | 4.3 | 0 | 0.0 / 0.0 | 5.54 | 397 | 99.1% | 0 | 0 | yes |
| 2023-11-06 | bybit_ob/bybit/XRP-USDT/perp | 797,811 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 1.42 | 587 | 92.4% | 0 | 0 | yes |
| 2023-11-06 | bybit_ob/bybit/ZEC-USDT/perp | 175,850 | 0.895 | 10.7 | 0 | 0.0 / 0.0 | 17.14 | 430 | 98.8% | 0 | 20 | NO |
| 2023-11-07 | binance_bt/binance/AAVE-USDT/perp | 542,049 | 1.000 | 7.3 | 0 | 5.0 / 9.0 | 1.97 | 679 | no trade record | - | - | yes |
| 2023-11-07 | binance_bt/binance/ARB-USDT/perp | 315,082 | 1.000 | 4.5 | 0 | 6.0 / 10.0 | 1.80 | 494 | no trade record | - | - | yes |
| 2023-11-07 | binance_bt/binance/BTC-USDT/perp | 253,421 | 1.000 | 1.2 | 0 | 6.0 / 12.0 | 0.03 | 215 | no trade record | - | - | yes |
| 2023-11-07 | binance_bt/binance/DOGE-USDT/perp | 122,069 | 1.000 | 2.2 | 0 | 6.0 / 10.0 | 1.36 | 482 | no trade record | - | - | yes |
| 2023-11-07 | binance_bt/binance/ETH-USDT/perp | 254,823 | 1.000 | 2.7 | 0 | 6.0 / 11.0 | 0.05 | 238 | no trade record | - | - | yes |
| 2023-11-07 | binance_bt/binance/SOL-USDT/perp | 1,958,828 | 1.000 | 2.1 | 0 | 5.0 / 10.0 | 0.68 | 633 | no trade record | - | - | yes |
| 2023-11-07 | binance_bt/binance/TIA-USDT/perp | 552,730 | 0.993 | 12.5 | 0 | 5.0 / 8.0 | 2.88 | 769 | no trade record | - | - | yes |
| 2023-11-07 | binance_bt/binance/WLD-USDT/perp | 467,676 | 0.998 | 10.1 | 0 | 5.0 / 9.0 | 1.66 | 559 | no trade record | - | - | yes |
| 2023-11-07 | binance_bt/binance/XRP-USDT/perp | 150,593 | 1.000 | 1.4 | 0 | 6.0 / 10.0 | 1.48 | 806 | no trade record | - | - | yes |
| 2023-11-07 | binance_bt/binance/ZEC-USDT/perp | 31,104 | 0.970 | 14.8 | 0 | 6.0 / 10.0 | 3.43 | 446 | no trade record | - | - | yes |
| 2023-11-07 | bybit_ob/bybit/AAVE-USDT/perp | 681,513 | 1.000 | 3.2 | 0 | 0.0 / 0.0 | 1.03 | 682 | 91.5% | 1 | 0 | yes |
| 2023-11-07 | bybit_ob/bybit/ARB-USDT/perp | 819,530 | 1.000 | 0.8 | 0 | 0.0 / 0.0 | 0.92 | 494 | 91.0% | 1 | 0 | yes |
| 2023-11-07 | bybit_ob/bybit/BTC-USDT/perp | 863,990 | 1.000 | 1.3 | 0 | 0.0 / 0.0 | 0.03 | 217 | 88.9% | 1 | 0 | yes |
| 2023-11-07 | bybit_ob/bybit/DOGE-USDT/perp | 741,726 | 1.000 | 2.1 | 0 | 0.0 / 0.0 | 1.35 | 489 | 93.9% | 1 | 0 | yes |
| 2023-11-07 | bybit_ob/bybit/ETH-USDT/perp | 863,456 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.05 | 237 | 91.0% | 1 | 0 | yes |
| 2023-11-07 | bybit_ob/bybit/SOL-USDT/perp | 855,850 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 0.24 | 633 | 83.9% | 1 | 0 | yes |
| 2023-11-07 | bybit_ob/bybit/TIA-USDT/perp | 674,733 | 1.000 | 3.0 | 0 | 0.0 / 0.0 | 1.30 | 779 | 91.9% | 1 | 0 | yes |
| 2023-11-07 | bybit_ob/bybit/WLD-USDT/perp | 540,573 | 0.999 | 4.2 | 0 | 0.0 / 0.0 | 5.54 | 558 | 97.9% | 0 | 20 | yes |
| 2023-11-07 | bybit_ob/bybit/XRP-USDT/perp | 775,841 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 1.46 | 812 | 88.4% | 0 | 20 | yes |
| 2023-11-07 | bybit_ob/bybit/ZEC-USDT/perp | 197,245 | 0.906 | 13.4 | 0 | 0.0 / 0.0 | 17.02 | 502 | 98.7% | 0 | 0 | NO |
| 2023-11-08 | binance_bt/binance/AAVE-USDT/perp | 188,844 | 0.996 | 9.2 | 0 | 5.0 / 9.0 | 1.05 | 410 | no trade record | - | - | yes |
| 2023-11-08 | binance_bt/binance/ARB-USDT/perp | 171,045 | 1.000 | 5.1 | 0 | 6.0 / 11.0 | 0.94 | 368 | no trade record | - | - | yes |
| 2023-11-08 | binance_bt/binance/BTC-USDT/perp | 237,132 | 1.000 | 4.6 | 0 | 6.0 / 16.0 | 0.03 | 216 | no trade record | - | - | yes |
| 2023-11-08 | binance_bt/binance/DOGE-USDT/perp | 74,800 | 1.000 | 4.7 | 0 | 6.0 / 10.0 | 1.35 | 388 | no trade record | - | - | yes |
| 2023-11-08 | binance_bt/binance/ETH-USDT/perp | 141,297 | 1.000 | 4.6 | 0 | 6.0 / 11.0 | 0.05 | 181 | no trade record | - | - | yes |
| 2023-11-08 | binance_bt/binance/SOL-USDT/perp | 1,042,703 | 1.000 | 4.2 | 0 | 5.0 / 10.0 | 0.46 | 414 | no trade record | - | - | yes |
| 2023-11-08 | binance_bt/binance/TIA-USDT/perp | 446,005 | 0.952 | 14.1 | 0 | 5.0 / 8.0 | 2.10 | 547 | no trade record | - | - | yes |
| 2023-11-08 | binance_bt/binance/WLD-USDT/perp | 263,767 | 0.994 | 8.5 | 0 | 5.0 / 9.0 | 1.63 | 378 | no trade record | - | - | yes |
| 2023-11-08 | binance_bt/binance/XRP-USDT/perp | 60,410 | 1.000 | 4.5 | 0 | 6.0 / 10.0 | 1.46 | 359 | no trade record | - | - | yes |
| 2023-11-08 | binance_bt/binance/ZEC-USDT/perp | 23,203 | 0.930 | 22.1 | 0 | 5.0 / 9.0 | 3.38 | 372 | no trade record | - | - | NO |
| 2023-11-08 | bybit_ob/bybit/AAVE-USDT/perp | 525,079 | 0.999 | 3.8 | 0 | 0.0 / 0.0 | 1.03 | 411 | 93.9% | 1 | 0 | yes |
| 2023-11-08 | bybit_ob/bybit/ARB-USDT/perp | 784,694 | 1.000 | 2.0 | 0 | 0.0 / 0.0 | 0.93 | 369 | 93.7% | 1 | 0 | yes |
| 2023-11-08 | bybit_ob/bybit/BTC-USDT/perp | 863,825 | 1.000 | 1.3 | 0 | 0.0 / 0.0 | 0.03 | 215 | 88.2% | 1 | 0 | yes |
| 2023-11-08 | bybit_ob/bybit/DOGE-USDT/perp | 649,373 | 1.000 | 2.9 | 0 | 0.0 / 0.0 | 1.34 | 388 | 92.9% | 1 | 0 | yes |
| 2023-11-08 | bybit_ob/bybit/ETH-USDT/perp | 862,905 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.05 | 181 | 93.9% | 1 | 0 | yes |
| 2023-11-08 | bybit_ob/bybit/SOL-USDT/perp | 849,455 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 0.23 | 415 | 88.2% | 1 | 0 | yes |
| 2023-11-08 | bybit_ob/bybit/TIA-USDT/perp | 593,946 | 1.000 | 3.5 | 0 | 0.0 / 0.0 | 1.27 | 553 | 92.4% | 1 | 0 | yes |
| 2023-11-08 | bybit_ob/bybit/WLD-USDT/perp | 427,290 | 0.997 | 5.3 | 0 | 0.0 / 0.0 | 5.49 | 378 | 97.6% | 0 | 20 | yes |
| 2023-11-08 | bybit_ob/bybit/XRP-USDT/perp | 703,358 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 1.45 | 365 | 92.7% | 0 | 20 | yes |
| 2023-11-08 | bybit_ob/bybit/ZEC-USDT/perp | 152,182 | 0.855 | 11.5 | 0 | 0.0 / 0.0 | 16.68 | 416 | 94.0% | 1 | -20 | NO |
| 2023-11-09 | binance_bt/binance/AAVE-USDT/perp | 721,446 | 1.000 | 6.7 | 0 | 6.0 / 9.0 | 1.91 | 961 | no trade record | - | - | yes |
| 2023-11-09 | binance_bt/binance/ARB-USDT/perp | 702,171 | 1.000 | 5.4 | 0 | 6.0 / 11.0 | 1.81 | 1735 | no trade record | - | - | yes |
| 2023-11-09 | binance_bt/binance/BTC-USDT/perp | 806,080 | 1.000 | 2.5 | 0 | 6.0 / 49.0 | 0.05 | 435 | no trade record | - | - | yes |
| 2023-11-09 | binance_bt/binance/DOGE-USDT/perp | 235,745 | 1.000 | 3.0 | 0 | 6.0 / 10.0 | 1.43 | 1006 | no trade record | - | - | yes |
| 2023-11-09 | binance_bt/binance/ETH-USDT/perp | 1,013,397 | 1.000 | 3.4 | 0 | 6.0 / 24.0 | 0.14 | 613 | no trade record | - | - | yes |
| 2023-11-09 | binance_bt/binance/SOL-USDT/perp | 3,657,773 | 1.000 | 4.3 | 0 | 6.0 / 10.0 | 0.68 | 1284 | no trade record | - | - | yes |
| 2023-11-09 | binance_bt/binance/TIA-USDT/perp | 749,888 | 0.995 | 9.7 | 0 | 5.0 / 9.0 | 3.19 | 1239 | no trade record | - | - | yes |
| 2023-11-09 | binance_bt/binance/WLD-USDT/perp | 557,289 | 0.998 | 9.1 | 0 | 6.0 / 9.0 | 1.77 | 895 | no trade record | - | - | yes |
| 2023-11-09 | binance_bt/binance/XRP-USDT/perp | 228,812 | 1.000 | 3.8 | 0 | 6.0 / 10.0 | 1.55 | 932 | no trade record | - | - | yes |
| 2023-11-09 | binance_bt/binance/ZEC-USDT/perp | 57,588 | 0.984 | 16.0 | 0 | 6.0 / 10.0 | 3.56 | 1144 | no trade record | - | - | yes |
| 2023-11-09 | bybit_ob/bybit/AAVE-USDT/perp | 699,310 | 1.000 | 10.3 | 2 | 0.0 / 0.0 | 1.01 | 977 | 90.5% | 1 | 0 | yes |
| 2023-11-09 | bybit_ob/bybit/ARB-USDT/perp | 829,205 | 1.000 | 9.8 | 2 | 0.0 / 0.0 | 0.90 | 1822 | 84.3% | 1 | 0 | yes |
| 2023-11-09 | bybit_ob/bybit/BTC-USDT/perp | 863,805 | 1.000 | 9.8 | 2 | 0.0 / 0.0 | 0.03 | 432 | 85.1% | 1 | 0 | yes |
| 2023-11-09 | bybit_ob/bybit/DOGE-USDT/perp | 757,615 | 1.000 | 9.8 | 2 | 0.0 / 0.0 | 1.32 | 1108 | 86.3% | 1 | 20 | yes |
| 2023-11-09 | bybit_ob/bybit/ETH-USDT/perp | 863,613 | 1.000 | 9.1 | 2 | 0.0 / 0.0 | 0.05 | 602 | 80.7% | 0 | 0 | yes |
| 2023-11-09 | bybit_ob/bybit/SOL-USDT/perp | 860,409 | 1.000 | 10.1 | 2 | 0.0 / 0.0 | 0.22 | 1437 | 79.6% | 1 | 0 | yes |
| 2023-11-09 | bybit_ob/bybit/TIA-USDT/perp | 720,520 | 1.000 | 9.5 | 2 | 0.0 / 0.0 | 2.94 | 1243 | 89.7% | 1 | 0 | yes |
| 2023-11-09 | bybit_ob/bybit/WLD-USDT/perp | 565,355 | 0.999 | 12.3 | 2 | 0.0 / 0.0 | 5.40 | 914 | 96.1% | 0 | 20 | yes |
| 2023-11-09 | bybit_ob/bybit/XRP-USDT/perp | 769,802 | 1.000 | 10.3 | 2 | 0.0 / 0.0 | 1.46 | 976 | 84.1% | 1 | 20 | yes |
| 2023-11-09 | bybit_ob/bybit/ZEC-USDT/perp | 215,085 | 0.914 | 10.3 | 2 | 0.0 / 0.0 | 16.54 | 1210 | 89.7% | 1 | -50 | NO |
| 2023-11-10 | binance_bt/binance/AAVE-USDT/perp | 368,168 | 0.999 | 6.5 | 0 | 6.0 / 9.0 | 2.03 | 505 | no trade record | - | - | yes |
| 2023-11-10 | binance_bt/binance/ARB-USDT/perp | 391,087 | 1.000 | 4.1 | 0 | 6.0 / 10.0 | 1.66 | 586 | no trade record | - | - | yes |
| 2023-11-10 | binance_bt/binance/BTC-USDT/perp | 279,688 | 1.000 | 2.7 | 0 | 7.0 / 12.0 | 0.03 | 235 | no trade record | - | - | yes |
| 2023-11-10 | binance_bt/binance/DOGE-USDT/perp | 93,828 | 1.000 | 4.2 | 0 | 6.0 / 10.0 | 1.36 | 415 | no trade record | - | - | yes |
| 2023-11-10 | binance_bt/binance/ETH-USDT/perp | 389,124 | 1.000 | 2.3 | 0 | 6.0 / 11.0 | 0.05 | 305 | no trade record | - | - | yes |
| 2023-11-10 | binance_bt/binance/SOL-USDT/perp | 4,332,234 | 1.000 | 2.7 | 0 | 6.0 / 10.0 | 0.72 | 1027 | no trade record | - | - | yes |
| 2023-11-10 | binance_bt/binance/TIA-USDT/perp | 1,102,129 | 0.991 | 11.3 | 0 | 5.0 / 8.0 | 4.09 | 1443 | no trade record | - | - | yes |
| 2023-11-10 | binance_bt/binance/WLD-USDT/perp | 399,453 | 0.999 | 6.6 | 0 | 6.0 / 9.0 | 1.71 | 590 | no trade record | - | - | yes |
| 2023-11-10 | binance_bt/binance/XRP-USDT/perp | 70,929 | 1.000 | 4.2 | 0 | 6.0 / 10.0 | 1.53 | 381 | no trade record | - | - | yes |
| 2023-11-10 | binance_bt/binance/ZEC-USDT/perp | 32,863 | 0.984 | 13.1 | 0 | 6.0 / 9.0 | 3.38 | 480 | no trade record | - | - | yes |
| 2023-11-10 | bybit_ob/bybit/AAVE-USDT/perp | 610,539 | 1.000 | 3.2 | 0 | 0.0 / 0.0 | 1.02 | 501 | 92.7% | 1 | 0 | yes |
| 2023-11-10 | bybit_ob/bybit/ARB-USDT/perp | 821,764 | 1.000 | 0.9 | 0 | 0.0 / 0.0 | 0.85 | 593 | 88.5% | 1 | 0 | yes |
| 2023-11-10 | bybit_ob/bybit/BTC-USDT/perp | 863,992 | 1.000 | 0.6 | 0 | 0.0 / 0.0 | 0.03 | 238 | 91.7% | 1 | 0 | yes |
| 2023-11-10 | bybit_ob/bybit/DOGE-USDT/perp | 741,100 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 1.35 | 422 | 95.7% | 1 | 0 | yes |
| 2023-11-10 | bybit_ob/bybit/ETH-USDT/perp | 863,598 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 306 | 89.4% | 1 | 0 | yes |
| 2023-11-10 | bybit_ob/bybit/SOL-USDT/perp | 861,161 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.20 | 1027 | 79.4% | 1 | 0 | yes |
| 2023-11-10 | bybit_ob/bybit/TIA-USDT/perp | 700,218 | 1.000 | 3.4 | 0 | 0.0 / 0.0 | 3.72 | 1458 | 86.2% | 1 | 0 | yes |
| 2023-11-10 | bybit_ob/bybit/WLD-USDT/perp | 533,304 | 1.000 | 5.0 | 0 | 0.0 / 0.0 | 5.72 | 595 | 97.5% | 0 | 0 | yes |
| 2023-11-10 | bybit_ob/bybit/XRP-USDT/perp | 740,801 | 1.000 | 1.5 | 0 | 0.0 / 0.0 | 1.52 | 388 | 92.4% | 1 | 20 | yes |
| 2023-11-10 | bybit_ob/bybit/ZEC-USDT/perp | 184,928 | 0.887 | 12.5 | 0 | 0.0 / 0.0 | 16.74 | 530 | 98.5% | 1 | 50 | NO |
| 2023-11-11 | binance_bt/binance/AAVE-USDT/perp | 353,540 | 0.998 | 8.5 | 0 | 6.0 / 9.0 | 2.07 | 508 | no trade record | - | - | yes |
| 2023-11-11 | binance_bt/binance/ARB-USDT/perp | 278,484 | 1.000 | 4.3 | 0 | 6.0 / 11.0 | 0.89 | 491 | no trade record | - | - | yes |
| 2023-11-11 | binance_bt/binance/BTC-USDT/perp | 120,270 | 1.000 | 4.3 | 0 | 7.0 / 12.0 | 0.03 | 151 | no trade record | - | - | yes |
| 2023-11-11 | binance_bt/binance/DOGE-USDT/perp | 252,097 | 1.000 | 4.2 | 0 | 6.0 / 10.0 | 1.30 | 728 | no trade record | - | - | yes |
| 2023-11-11 | binance_bt/binance/ETH-USDT/perp | 248,058 | 1.000 | 4.2 | 0 | 6.0 / 11.0 | 0.05 | 251 | no trade record | - | - | yes |
| 2023-11-11 | binance_bt/binance/SOL-USDT/perp | 5,157,679 | 1.000 | 2.3 | 0 | 6.0 / 10.0 | 0.81 | 1118 | no trade record | - | - | yes |
| 2023-11-11 | binance_bt/binance/TIA-USDT/perp | 3,281,614 | 1.000 | 4.3 | 0 | 5.0 / 8.0 | 3.96 | 2180 | no trade record | - | - | yes |
| 2023-11-11 | binance_bt/binance/WLD-USDT/perp | 749,640 | 0.999 | 9.3 | 0 | 6.0 / 9.0 | 2.07 | 917 | no trade record | - | - | yes |
| 2023-11-11 | binance_bt/binance/XRP-USDT/perp | 77,317 | 1.000 | 2.6 | 0 | 6.0 / 10.0 | 1.52 | 438 | no trade record | - | - | yes |
| 2023-11-11 | binance_bt/binance/ZEC-USDT/perp | 35,713 | 0.965 | 18.4 | 0 | 6.0 / 9.0 | 3.36 | 500 | no trade record | - | - | yes |
| 2023-11-11 | bybit_ob/bybit/AAVE-USDT/perp | 577,300 | 0.999 | 4.5 | 0 | 0.0 / 0.0 | 1.03 | 505 | 90.8% | 1 | 0 | yes |
| 2023-11-11 | bybit_ob/bybit/ARB-USDT/perp | 808,528 | 1.000 | 0.9 | 0 | 0.0 / 0.0 | 0.87 | 510 | 91.6% | 1 | 0 | yes |
| 2023-11-11 | bybit_ob/bybit/BTC-USDT/perp | 863,979 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.03 | 152 | 92.2% | 1 | 0 | yes |
| 2023-11-11 | bybit_ob/bybit/DOGE-USDT/perp | 796,522 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 1.26 | 744 | 92.7% | 1 | 0 | yes |
| 2023-11-11 | bybit_ob/bybit/ETH-USDT/perp | 863,365 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 251 | 89.4% | 1 | 0 | yes |
| 2023-11-11 | bybit_ob/bybit/SOL-USDT/perp | 862,226 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.18 | 1132 | 73.9% | 1 | 0 | NO |
| 2023-11-11 | bybit_ob/bybit/TIA-USDT/perp | 842,760 | 1.000 | 1.3 | 0 | 0.0 / 0.0 | 5.19 | 2199 | 80.1% | 1 | 20 | yes |
| 2023-11-11 | bybit_ob/bybit/WLD-USDT/perp | 633,769 | 1.000 | 4.2 | 0 | 0.0 / 0.0 | 5.08 | 916 | 97.7% | 0 | 0 | yes |
| 2023-11-11 | bybit_ob/bybit/XRP-USDT/perp | 714,238 | 1.000 | 1.6 | 0 | 0.0 / 0.0 | 1.50 | 441 | 94.0% | 0 | 0 | yes |
| 2023-11-11 | bybit_ob/bybit/ZEC-USDT/perp | 184,501 | 0.872 | 13.1 | 0 | 0.0 / 0.0 | 16.52 | 538 | 86.3% | 1 | 0 | NO |
| 2023-11-12 | binance_bt/binance/AAVE-USDT/perp | 286,425 | 0.995 | 9.7 | 0 | 6.0 / 9.0 | 2.08 | 507 | no trade record | - | - | yes |
| 2023-11-12 | binance_bt/binance/ARB-USDT/perp | 244,083 | 1.000 | 8.3 | 0 | 6.0 / 10.0 | 0.90 | 473 | no trade record | - | - | yes |
| 2023-11-12 | binance_bt/binance/BTC-USDT/perp | 80,290 | 1.000 | 2.3 | 0 | 7.0 / 12.0 | 0.03 | 121 | no trade record | - | - | yes |
| 2023-11-12 | binance_bt/binance/DOGE-USDT/perp | 137,757 | 1.000 | 2.3 | 0 | 6.0 / 10.0 | 1.29 | 501 | no trade record | - | - | yes |
| 2023-11-12 | binance_bt/binance/ETH-USDT/perp | 178,402 | 1.000 | 2.6 | 0 | 6.0 / 11.0 | 0.05 | 200 | no trade record | - | - | yes |
| 2023-11-12 | binance_bt/binance/SOL-USDT/perp | 3,362,191 | 1.000 | 8.2 | 0 | 6.0 / 10.0 | 0.69 | 906 | no trade record | - | - | yes |
| 2023-11-12 | binance_bt/binance/TIA-USDT/perp | 2,392,797 | 1.000 | 4.0 | 0 | 5.0 / 9.0 | 3.04 | 1875 | no trade record | - | - | yes |
| 2023-11-12 | binance_bt/binance/WLD-USDT/perp | 403,038 | 0.995 | 9.2 | 0 | 6.0 / 9.0 | 1.58 | 592 | no trade record | - | - | yes |
| 2023-11-12 | binance_bt/binance/XRP-USDT/perp | 33,939 | 1.000 | 6.0 | 0 | 6.0 / 11.0 | 1.52 | 292 | no trade record | - | - | yes |
| 2023-11-12 | binance_bt/binance/ZEC-USDT/perp | 35,249 | 0.957 | 16.2 | 0 | 6.0 / 10.0 | 3.32 | 527 | no trade record | - | - | yes |
| 2023-11-12 | bybit_ob/bybit/AAVE-USDT/perp | 543,285 | 0.999 | 4.5 | 0 | 0.0 / 0.0 | 1.04 | 498 | 92.9% | 1 | 0 | yes |
| 2023-11-12 | bybit_ob/bybit/ARB-USDT/perp | 806,636 | 1.000 | 1.0 | 0 | 0.0 / 0.0 | 0.88 | 481 | 89.3% | 1 | 0 | yes |
| 2023-11-12 | bybit_ob/bybit/BTC-USDT/perp | 863,999 | 1.000 | 0.3 | 0 | 0.0 / 0.0 | 0.03 | 122 | 94.3% | 0 | 0 | yes |
| 2023-11-12 | bybit_ob/bybit/DOGE-USDT/perp | 711,800 | 1.000 | 2.1 | 0 | 0.0 / 0.0 | 1.28 | 513 | 91.6% | 1 | 0 | yes |
| 2023-11-12 | bybit_ob/bybit/ETH-USDT/perp | 863,208 | 1.000 | 0.4 | 0 | 0.0 / 0.0 | 0.05 | 202 | 90.5% | 1 | 0 | yes |
| 2023-11-12 | bybit_ob/bybit/SOL-USDT/perp | 860,296 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.17 | 911 | 75.1% | 2 | 0 | NO |
| 2023-11-12 | bybit_ob/bybit/TIA-USDT/perp | 831,700 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 3.63 | 1915 | 79.7% | 2 | 20 | yes |
| 2023-11-12 | bybit_ob/bybit/WLD-USDT/perp | 533,847 | 0.999 | 5.2 | 0 | 0.0 / 0.0 | 5.20 | 586 | 97.2% | 0 | 20 | yes |
| 2023-11-12 | bybit_ob/bybit/XRP-USDT/perp | 624,895 | 1.000 | 2.7 | 0 | 0.0 / 0.0 | 1.51 | 293 | 97.0% | 1 | 0 | yes |
| 2023-11-12 | bybit_ob/bybit/ZEC-USDT/perp | 182,083 | 0.863 | 13.2 | 0 | 0.0 / 0.0 | 16.19 | 562 | 94.1% | 1 | -50 | NO |
| 2023-11-13 | binance_bt/binance/AAVE-USDT/perp | 368,155 | 0.999 | 9.0 | 0 | 6.0 / 27.0 | 2.07 | 613 | no trade record | - | - | yes |
| 2023-11-13 | binance_bt/binance/ARB-USDT/perp | 443,936 | 1.000 | 4.6 | 0 | 6.0 / 30.0 | 1.71 | 601 | no trade record | - | - | yes |
| 2023-11-13 | binance_bt/binance/BTC-USDT/perp | 216,916 | 1.000 | 4.3 | 0 | 7.0 / 51.0 | 0.03 | 191 | no trade record | - | - | yes |
| 2023-11-13 | binance_bt/binance/DOGE-USDT/perp | 182,957 | 1.000 | 4.5 | 0 | 6.0 / 36.0 | 1.32 | 498 | no trade record | - | - | yes |
| 2023-11-13 | binance_bt/binance/ETH-USDT/perp | 406,782 | 1.000 | 3.4 | 0 | 7.0 / 41.0 | 0.05 | 344 | no trade record | - | - | yes |
| 2023-11-13 | binance_bt/binance/SOL-USDT/perp | 3,837,958 | 1.000 | 4.3 | 0 | 6.0 / 18.0 | 0.85 | 973 | no trade record | - | - | yes |
| 2023-11-13 | binance_bt/binance/TIA-USDT/perp | 4,951,208 | 1.000 | 4.6 | 0 | 5.0 / 11.0 | 2.85 | 2219 | no trade record | - | - | yes |
| 2023-11-13 | binance_bt/binance/WLD-USDT/perp | 2,241,762 | 0.999 | 7.1 | 0 | 6.0 / 17.0 | 3.60 | 1507 | no trade record | - | - | yes |
| 2023-11-13 | binance_bt/binance/XRP-USDT/perp | 431,190 | 1.000 | 4.4 | 0 | 6.0 / 37.0 | 2.83 | 1281 | no trade record | - | - | yes |
| 2023-11-13 | binance_bt/binance/ZEC-USDT/perp | 50,336 | 0.976 | 13.8 | 0 | 6.0 / 34.0 | 3.30 | 515 | no trade record | - | - | yes |
| 2023-11-13 | bybit_ob/bybit/AAVE-USDT/perp | 612,832 | 1.000 | 3.6 | 0 | 0.0 / 0.0 | 1.04 | 610 | 90.2% | 1 | 0 | yes |
| 2023-11-13 | bybit_ob/bybit/ARB-USDT/perp | 824,112 | 1.000 | 1.0 | 0 | 0.0 / 0.0 | 0.87 | 604 | 89.2% | 1 | 0 | yes |
| 2023-11-13 | bybit_ob/bybit/BTC-USDT/perp | 863,995 | 1.000 | 0.3 | 0 | 0.0 / 0.0 | 0.03 | 192 | 89.1% | 1 | 0 | yes |
| 2023-11-13 | bybit_ob/bybit/DOGE-USDT/perp | 741,750 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 1.30 | 505 | 91.1% | 1 | 0 | yes |
| 2023-11-13 | bybit_ob/bybit/ETH-USDT/perp | 863,668 | 1.000 | 0.4 | 0 | 0.0 / 0.0 | 0.05 | 345 | 85.1% | 1 | 0 | yes |
| 2023-11-13 | bybit_ob/bybit/SOL-USDT/perp | 861,974 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.18 | 981 | 74.3% | 1 | 20 | NO |
| 2023-11-13 | bybit_ob/bybit/TIA-USDT/perp | 853,028 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 4.44 | 2255 | 77.9% | 1 | 20 | yes |
| 2023-11-13 | bybit_ob/bybit/WLD-USDT/perp | 716,750 | 1.000 | 3.1 | 0 | 0.0 / 0.0 | 4.41 | 1497 | 93.4% | 0 | 0 | yes |
| 2023-11-13 | bybit_ob/bybit/XRP-USDT/perp | 695,374 | 1.000 | 2.1 | 0 | 0.0 / 0.0 | 1.53 | 1286 | 74.2% | 0 | 20 | yes |
| 2023-11-13 | bybit_ob/bybit/ZEC-USDT/perp | 223,661 | 0.924 | 11.8 | 0 | 0.0 / 0.0 | 16.27 | 557 | 97.8% | 0 | 20 | NO |
| 2023-11-14 | binance_bt/binance/AAVE-USDT/perp | 303,065 | 0.997 | 7.8 | 0 | 6.0 / 40.0 | 2.14 | 603 | no trade record | - | - | yes |
| 2023-11-14 | binance_bt/binance/ARB-USDT/perp | 302,829 | 1.000 | 7.5 | 0 | 6.0 / 43.0 | 1.81 | 719 | no trade record | - | - | yes |
| 2023-11-14 | binance_bt/binance/BTC-USDT/perp | 362,082 | 1.000 | 7.5 | 0 | 7.0 / 72.0 | 0.05 | 326 | no trade record | - | - | yes |
| 2023-11-14 | binance_bt/binance/DOGE-USDT/perp | 155,072 | 1.000 | 7.5 | 0 | 6.0 / 53.0 | 1.40 | 581 | no trade record | - | - | yes |
| 2023-11-14 | binance_bt/binance/ETH-USDT/perp | 355,795 | 1.000 | 7.5 | 0 | 7.0 / 82.0 | 0.05 | 405 | no trade record | - | - | yes |
| 2023-11-14 | binance_bt/binance/SOL-USDT/perp | 3,634,996 | 1.000 | 7.5 | 0 | 6.0 / 26.0 | 0.74 | 1012 | no trade record | - | - | yes |
| 2023-11-14 | binance_bt/binance/TIA-USDT/perp | 8,422,806 | 1.000 | 7.5 | 0 | 5.0 / 15.0 | 2.56 | 2146 | no trade record | - | - | yes |
| 2023-11-14 | binance_bt/binance/WLD-USDT/perp | 2,051,203 | 1.000 | 7.5 | 0 | 5.0 / 26.0 | 2.24 | 1139 | no trade record | - | - | yes |
| 2023-11-14 | binance_bt/binance/XRP-USDT/perp | 126,882 | 1.000 | 7.5 | 0 | 6.0 / 82.0 | 1.63 | 741 | no trade record | - | - | yes |
| 2023-11-14 | binance_bt/binance/ZEC-USDT/perp | 41,300 | 0.971 | 15.1 | 0 | 6.0 / 47.0 | 3.43 | 555 | no trade record | - | - | yes |
| 2023-11-14 | bybit_ob/bybit/AAVE-USDT/perp | 562,829 | 0.999 | 4.6 | 0 | 0.0 / 0.0 | 1.09 | 574 | 88.4% | 1 | 0 | yes |
| 2023-11-14 | bybit_ob/bybit/ARB-USDT/perp | 800,000 | 1.000 | 1.0 | 0 | 0.0 / 0.0 | 0.91 | 714 | 88.1% | 1 | 0 | yes |
| 2023-11-14 | bybit_ob/bybit/BTC-USDT/perp | 863,996 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.03 | 320 | 84.5% | 0 | 0 | yes |
| 2023-11-14 | bybit_ob/bybit/DOGE-USDT/perp | 706,535 | 1.000 | 2.7 | 0 | 0.0 / 0.0 | 1.35 | 555 | 89.2% | 1 | 0 | yes |
| 2023-11-14 | bybit_ob/bybit/ETH-USDT/perp | 863,490 | 1.000 | 0.4 | 0 | 0.0 / 0.0 | 0.05 | 417 | 84.6% | 1 | 0 | yes |
| 2023-11-14 | bybit_ob/bybit/SOL-USDT/perp | 860,569 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.18 | 1013 | 74.6% | 1 | 0 | yes |
| 2023-11-14 | bybit_ob/bybit/TIA-USDT/perp | 854,777 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 3.53 | 2191 | 78.0% | 1 | 20 | yes |
| 2023-11-14 | bybit_ob/bybit/WLD-USDT/perp | 726,227 | 1.000 | 2.7 | 0 | 0.0 / 0.0 | 4.50 | 1116 | 94.8% | 1 | 20 | yes |
| 2023-11-14 | bybit_ob/bybit/XRP-USDT/perp | 730,338 | 1.000 | 2.5 | 0 | 0.0 / 0.0 | 1.53 | 708 | 87.5% | 1 | 20 | yes |
| 2023-11-14 | bybit_ob/bybit/ZEC-USDT/perp | 210,831 | 0.901 | 14.0 | 0 | 0.0 / 0.0 | 16.88 | 611 | 99.1% | 0 | 0 | NO |
| 2023-11-15 | binance_bt/binance/AAVE-USDT/perp | 224,803 | 0.997 | 8.2 | 0 | 6.0 / 49.0 | 2.10 | 439 | no trade record | - | - | yes |
| 2023-11-15 | binance_bt/binance/ARB-USDT/perp | 156,105 | 1.000 | 8.1 | 0 | 6.0 / 74.0 | 0.92 | 386 | no trade record | - | - | yes |
| 2023-11-15 | binance_bt/binance/BTC-USDT/perp | 406,332 | 1.000 | 7.8 | 0 | 7.0 / 456.0 | 0.03 | 361 | no trade record | - | - | yes |
| 2023-11-15 | binance_bt/binance/DOGE-USDT/perp | 70,037 | 1.000 | 8.1 | 0 | 6.0 / 144.6 | 1.36 | 353 | no trade record | - | - | yes |
| 2023-11-15 | binance_bt/binance/ETH-USDT/perp | 291,768 | 1.000 | 7.8 | 0 | 7.0 / 183.0 | 0.05 | 280 | no trade record | - | - | yes |
| 2023-11-15 | binance_bt/binance/SOL-USDT/perp | 4,233,059 | 1.000 | 7.9 | 0 | 6.0 / 22.0 | 0.52 | 842 | no trade record | - | - | yes |
| 2023-11-15 | binance_bt/binance/TIA-USDT/perp | 6,729,702 | 1.000 | 5.1 | 0 | 5.0 / 15.0 | 1.66 | 1351 | no trade record | - | - | yes |
| 2023-11-15 | binance_bt/binance/WLD-USDT/perp | 1,183,472 | 1.000 | 7.8 | 0 | 5.0 / 25.0 | 1.71 | 891 | no trade record | - | - | yes |
| 2023-11-15 | binance_bt/binance/XRP-USDT/perp | 40,526 | 1.000 | 7.8 | 0 | 6.0 / 460.0 | 1.58 | 312 | no trade record | - | - | yes |
| 2023-11-15 | binance_bt/binance/ZEC-USDT/perp | 27,647 | 0.981 | 15.8 | 0 | 6.0 / 48.0 | 3.36 | 391 | no trade record | - | - | yes |
| 2023-11-15 | bybit_ob/bybit/AAVE-USDT/perp | 567,181 | 1.000 | 3.5 | 0 | 0.0 / 0.0 | 1.07 | 438 | 91.3% | 1 | 0 | yes |
| 2023-11-15 | bybit_ob/bybit/ARB-USDT/perp | 797,908 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 0.89 | 390 | 94.3% | 1 | 0 | yes |
| 2023-11-15 | bybit_ob/bybit/BTC-USDT/perp | 863,976 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.03 | 372 | 84.7% | 1 | 0 | yes |
| 2023-11-15 | bybit_ob/bybit/DOGE-USDT/perp | 700,090 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 1.35 | 358 | 94.1% | 1 | 0 | yes |
| 2023-11-15 | bybit_ob/bybit/ETH-USDT/perp | 863,020 | 1.000 | 0.8 | 0 | 0.0 / 0.0 | 0.05 | 285 | 88.9% | 0 | 0 | yes |
| 2023-11-15 | bybit_ob/bybit/SOL-USDT/perp | 862,289 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.17 | 854 | 76.7% | 2 | 0 | yes |
| 2023-11-15 | bybit_ob/bybit/TIA-USDT/perp | 851,611 | 1.000 | 1.3 | 0 | 0.0 / 0.0 | 2.50 | 1377 | 80.1% | 1 | 20 | yes |
| 2023-11-15 | bybit_ob/bybit/WLD-USDT/perp | 678,807 | 1.000 | 3.7 | 0 | 0.0 / 0.0 | 4.23 | 879 | 94.8% | 1 | 0 | yes |
| 2023-11-15 | bybit_ob/bybit/XRP-USDT/perp | 672,315 | 1.000 | 2.5 | 0 | 0.0 / 0.0 | 1.57 | 319 | 94.8% | 1 | 0 | yes |
| 2023-11-15 | bybit_ob/bybit/ZEC-USDT/perp | 165,245 | 0.861 | 11.6 | 0 | 0.0 / 0.0 | 16.60 | 454 | 98.9% | 1 | 0 | NO |
| 2023-11-16 | binance_bt/binance/AAVE-USDT/perp | 304,233 | 0.999 | 7.6 | 0 | 6.0 / 50.0 | 2.07 | 658 | no trade record | - | - | yes |
| 2023-11-16 | binance_bt/binance/ARB-USDT/perp | 251,555 | 1.000 | 7.2 | 0 | 6.0 / 62.0 | 0.93 | 568 | no trade record | - | - | yes |
| 2023-11-16 | binance_bt/binance/BTC-USDT/perp | 411,918 | 1.000 | 7.3 | 0 | 8.0 / 81.0 | 0.03 | 293 | no trade record | - | - | yes |
| 2023-11-16 | binance_bt/binance/DOGE-USDT/perp | 401,389 | 1.000 | 6.0 | 0 | 6.0 / 49.0 | 1.29 | 867 | no trade record | - | - | yes |
| 2023-11-16 | binance_bt/binance/ETH-USDT/perp | 448,082 | 1.000 | 7.2 | 0 | 7.0 / 85.0 | 0.05 | 380 | no trade record | - | - | yes |
| 2023-11-16 | binance_bt/binance/SOL-USDT/perp | 3,631,820 | 1.000 | 7.5 | 0 | 6.0 / 36.0 | 0.59 | 949 | no trade record | - | - | yes |
| 2023-11-16 | binance_bt/binance/TIA-USDT/perp | 4,456,872 | 1.000 | 7.3 | 0 | 5.0 / 31.0 | 1.83 | 1197 | no trade record | - | - | yes |
| 2023-11-16 | binance_bt/binance/WLD-USDT/perp | 935,251 | 1.000 | 7.3 | 0 | 6.0 / 40.0 | 1.67 | 992 | no trade record | - | - | yes |
| 2023-11-16 | binance_bt/binance/XRP-USDT/perp | 73,196 | 1.000 | 7.2 | 0 | 7.0 / 112.0 | 1.63 | 421 | no trade record | - | - | yes |
| 2023-11-16 | bybit_ob/bybit/AAVE-USDT/perp | 614,496 | 1.000 | 4.1 | 0 | 0.0 / 0.0 | 1.06 | 655 | 86.9% | 1 | 0 | yes |
| 2023-11-16 | bybit_ob/bybit/ARB-USDT/perp | 762,802 | 1.000 | 2.0 | 0 | 0.0 / 0.0 | 0.87 | 577 | 89.7% | 1 | 0 | yes |
| 2023-11-16 | bybit_ob/bybit/BTC-USDT/perp | 863,987 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.03 | 296 | 87.9% | 0 | 0 | yes |
| 2023-11-16 | bybit_ob/bybit/DOGE-USDT/perp | 784,352 | 1.000 | 1.5 | 0 | 0.0 / 0.0 | 1.27 | 875 | 87.6% | 1 | 0 | yes |
| 2023-11-16 | bybit_ob/bybit/ETH-USDT/perp | 862,995 | 1.000 | 0.4 | 0 | 0.0 / 0.0 | 0.05 | 383 | 85.0% | 1 | 0 | yes |
| 2023-11-16 | bybit_ob/bybit/SOL-USDT/perp | 862,225 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.16 | 958 | 76.2% | 1 | 0 | yes |
| 2023-11-16 | bybit_ob/bybit/TIA-USDT/perp | 842,339 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 2.66 | 1225 | 79.4% | 1 | 20 | yes |
| 2023-11-16 | bybit_ob/bybit/WLD-USDT/perp | 680,068 | 1.000 | 3.8 | 0 | 0.0 / 0.0 | 4.25 | 985 | 95.8% | 0 | 0 | yes |
| 2023-11-16 | bybit_ob/bybit/XRP-USDT/perp | 710,761 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 1.56 | 428 | 92.6% | 1 | 0 | yes |
| 2023-11-16 | bybit_ob/bybit/ZEC-USDT/perp | 182,269 | 0.872 | 14.5 | 0 | 0.0 / 0.0 | 16.57 | 516 | 94.1% | 1 | -50 | NO |
| 2023-11-17 | binance_bt/binance/AAVE-USDT/perp | 249,035 | 0.998 | 7.9 | 0 | 6.0 / 42.0 | 2.16 | 507 | no trade record | - | - | yes |
| 2023-11-17 | binance_bt/binance/ARB-USDT/perp | 217,217 | 1.000 | 4.5 | 0 | 6.0 / 52.0 | 0.99 | 525 | no trade record | - | - | yes |
| 2023-11-17 | binance_bt/binance/BTC-USDT/perp | 332,251 | 1.000 | 7.3 | 0 | 7.0 / 268.0 | 0.03 | 281 | no trade record | - | - | yes |
| 2023-11-17 | binance_bt/binance/DOGE-USDT/perp | 393,548 | 1.000 | 6.0 | 0 | 6.0 / 36.0 | 1.23 | 836 | no trade record | - | - | yes |
| 2023-11-17 | binance_bt/binance/ETH-USDT/perp | 345,609 | 1.000 | 7.3 | 0 | 7.0 / 76.0 | 0.05 | 308 | no trade record | - | - | yes |
| 2023-11-17 | binance_bt/binance/SOL-USDT/perp | 3,156,846 | 1.000 | 7.4 | 0 | 6.0 / 29.0 | 0.52 | 874 | no trade record | - | - | yes |
| 2023-11-17 | binance_bt/binance/TIA-USDT/perp | 7,429,959 | 1.000 | 3.9 | 0 | 5.0 / 17.0 | 1.88 | 1464 | no trade record | - | - | yes |
| 2023-11-17 | binance_bt/binance/WLD-USDT/perp | 930,841 | 0.999 | 7.3 | 0 | 6.0 / 29.0 | 1.93 | 928 | no trade record | - | - | yes |
| 2023-11-17 | binance_bt/binance/XRP-USDT/perp | 54,673 | 1.000 | 3.3 | 0 | 7.0 / 128.8 | 1.67 | 369 | no trade record | - | - | yes |
| 2023-11-17 | binance_bt/binance/ZEC-USDT/perp | 37,221 | 0.983 | 13.4 | 0 | 6.0 / 41.0 | 3.47 | 451 | no trade record | - | - | yes |
| 2023-11-17 | bybit_ob/bybit/AAVE-USDT/perp | 601,594 | 1.000 | 3.7 | 0 | 0.0 / 0.0 | 1.13 | 502 | 92.8% | 1 | 0 | yes |
| 2023-11-17 | bybit_ob/bybit/ARB-USDT/perp | 711,170 | 1.000 | 2.5 | 0 | 0.0 / 0.0 | 0.95 | 528 | 91.5% | 1 | 0 | yes |
| 2023-11-17 | bybit_ob/bybit/BTC-USDT/perp | 863,932 | 1.000 | 0.3 | 0 | 0.0 / 0.0 | 0.03 | 281 | 88.9% | 1 | 0 | yes |
| 2023-11-17 | bybit_ob/bybit/DOGE-USDT/perp | 827,545 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 1.21 | 849 | 86.6% | 1 | 0 | yes |
| 2023-11-17 | bybit_ob/bybit/ETH-USDT/perp | 861,953 | 1.000 | 0.4 | 0 | 0.0 / 0.0 | 0.05 | 309 | 88.7% | 0 | 0 | yes |
| 2023-11-17 | bybit_ob/bybit/SOL-USDT/perp | 859,770 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.17 | 883 | 74.4% | 2 | 0 | yes |
| 2023-11-17 | bybit_ob/bybit/TIA-USDT/perp | 850,902 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 2.32 | 1489 | 76.7% | 1 | 20 | yes |
| 2023-11-17 | bybit_ob/bybit/WLD-USDT/perp | 661,347 | 1.000 | 4.2 | 0 | 0.0 / 0.0 | 4.88 | 940 | 92.8% | 0 | 20 | yes |
| 2023-11-17 | bybit_ob/bybit/XRP-USDT/perp | 718,894 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 1.63 | 377 | 94.9% | 0 | 20 | yes |
| 2023-11-17 | bybit_ob/bybit/ZEC-USDT/perp | 179,223 | 0.882 | 11.3 | 0 | 0.0 / 0.0 | 16.99 | 500 | 81.6% | 1 | 500 | NO |
| 2023-11-18 | binance_bt/binance/AAVE-USDT/perp | 106,803 | 0.991 | 10.3 | 0 | 6.0 / 17.0 | 1.18 | 432 | no trade record | - | - | yes |
| 2023-11-18 | binance_bt/binance/ARB-USDT/perp | 85,851 | 1.000 | 5.7 | 0 | 6.0 / 24.0 | 0.99 | 395 | no trade record | - | - | yes |
| 2023-11-18 | binance_bt/binance/BTC-USDT/perp | 79,561 | 1.000 | 4.7 | 0 | 7.0 / 39.0 | 0.03 | 126 | no trade record | - | - | yes |
| 2023-11-18 | binance_bt/binance/DOGE-USDT/perp | 253,716 | 1.000 | 4.7 | 0 | 6.0 / 13.9 | 1.25 | 754 | no trade record | - | - | yes |
| 2023-11-18 | binance_bt/binance/ETH-USDT/perp | 154,553 | 1.000 | 4.7 | 0 | 7.0 / 27.0 | 0.05 | 190 | no trade record | - | - | yes |
| 2023-11-18 | binance_bt/binance/SOL-USDT/perp | 1,264,473 | 1.000 | 4.7 | 0 | 6.0 / 20.0 | 0.36 | 619 | no trade record | - | - | yes |
| 2023-11-18 | binance_bt/binance/TIA-USDT/perp | 7,683,666 | 1.000 | 4.7 | 0 | 5.0 / 9.0 | 1.26 | 1136 | no trade record | - | - | yes |
| 2023-11-18 | binance_bt/binance/WLD-USDT/perp | 778,180 | 0.999 | 8.9 | 0 | 5.0 / 11.0 | 1.52 | 863 | no trade record | - | - | yes |
| 2023-11-18 | binance_bt/binance/XRP-USDT/perp | 24,927 | 1.000 | 4.0 | 0 | 6.0 / 26.0 | 1.66 | 258 | no trade record | - | - | yes |
| 2023-11-18 | binance_bt/binance/ZEC-USDT/perp | 22,959 | 0.950 | 24.3 | 0 | 6.0 / 16.0 | 3.54 | 363 | no trade record | - | - | yes |
| 2023-11-18 | bybit_ob/bybit/AAVE-USDT/perp | 501,110 | 0.999 | 4.4 | 0 | 0.0 / 0.0 | 1.15 | 429 | 92.6% | 1 | 0 | yes |
| 2023-11-18 | bybit_ob/bybit/ARB-USDT/perp | 602,825 | 1.000 | 3.6 | 0 | 0.0 / 0.0 | 0.98 | 396 | 88.4% | 1 | 20 | yes |
| 2023-11-18 | bybit_ob/bybit/BTC-USDT/perp | 863,888 | 1.000 | 0.3 | 0 | 0.0 / 0.0 | 0.03 | 126 | 93.2% | 1 | 0 | yes |
| 2023-11-18 | bybit_ob/bybit/DOGE-USDT/perp | 774,410 | 1.000 | 2.3 | 0 | 0.0 / 0.0 | 1.21 | 771 | 85.7% | 1 | 0 | yes |
| 2023-11-18 | bybit_ob/bybit/ETH-USDT/perp | 860,451 | 1.000 | 0.4 | 0 | 0.0 / 0.0 | 0.05 | 191 | 94.0% | 1 | 0 | yes |
| 2023-11-18 | bybit_ob/bybit/SOL-USDT/perp | 846,803 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.17 | 620 | 78.5% | 1 | 0 | yes |
| 2023-11-18 | bybit_ob/bybit/TIA-USDT/perp | 853,664 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 2.27 | 1141 | 76.4% | 1 | 20 | yes |
| 2023-11-18 | bybit_ob/bybit/WLD-USDT/perp | 594,014 | 1.000 | 4.3 | 0 | 0.0 / 0.0 | 5.08 | 871 | 95.7% | 1 | 20 | yes |
| 2023-11-18 | bybit_ob/bybit/XRP-USDT/perp | 643,339 | 1.000 | 2.5 | 0 | 0.0 / 0.0 | 1.65 | 262 | 98.1% | 0 | 20 | yes |
| 2023-11-18 | bybit_ob/bybit/ZEC-USDT/perp | 130,935 | 0.775 | 13.6 | 0 | 0.0 / 0.0 | 17.44 | 421 | 98.9% | 0 | 50 | NO |
| 2023-11-19 | binance_bt/binance/AAVE-USDT/perp | 74,909 | 0.987 | 11.0 | 0 | 6.0 / 32.0 | 1.15 | 305 | no trade record | - | - | yes |
| 2023-11-19 | binance_bt/binance/ARB-USDT/perp | 70,379 | 0.999 | 7.1 | 0 | 6.0 / 46.0 | 0.98 | 332 | no trade record | - | - | yes |
| 2023-11-19 | binance_bt/binance/BTC-USDT/perp | 104,432 | 1.000 | 5.9 | 0 | 8.0 / 99.0 | 0.03 | 146 | no trade record | - | - | yes |
| 2023-11-19 | binance_bt/binance/DOGE-USDT/perp | 70,343 | 1.000 | 8.6 | 0 | 6.0 / 38.0 | 1.28 | 384 | no trade record | - | - | yes |
| 2023-11-19 | binance_bt/binance/ETH-USDT/perp | 157,564 | 1.000 | 4.0 | 0 | 7.0 / 62.0 | 0.05 | 187 | no trade record | - | - | yes |
| 2023-11-19 | binance_bt/binance/SOL-USDT/perp | 1,107,918 | 1.000 | 6.2 | 0 | 6.0 / 27.0 | 0.33 | 531 | no trade record | - | - | yes |
| 2023-11-19 | binance_bt/binance/TIA-USDT/perp | 5,306,701 | 1.000 | 8.6 | 0 | 5.0 / 11.0 | 1.11 | 902 | no trade record | - | - | yes |
| 2023-11-19 | binance_bt/binance/WLD-USDT/perp | 2,382,039 | 1.000 | 8.7 | 0 | 5.0 / 11.0 | 1.30 | 1172 | no trade record | - | - | yes |
| 2023-11-19 | binance_bt/binance/XRP-USDT/perp | 26,448 | 1.000 | 7.3 | 0 | 6.0 / 47.0 | 1.64 | 280 | no trade record | - | - | yes |
| 2023-11-19 | binance_bt/binance/ZEC-USDT/perp | 11,280 | 0.918 | 22.1 | 0 | 6.0 / 40.0 | 3.50 | 293 | no trade record | - | - | NO |
| 2023-11-19 | bybit_ob/bybit/AAVE-USDT/perp | 455,440 | 0.998 | 5.0 | 0 | 0.0 / 0.0 | 1.13 | 308 | 93.4% | 1 | 0 | yes |
| 2023-11-19 | bybit_ob/bybit/ARB-USDT/perp | 578,008 | 1.000 | 3.4 | 0 | 0.0 / 0.0 | 0.97 | 334 | 90.9% | 1 | 0 | yes |
| 2023-11-19 | bybit_ob/bybit/BTC-USDT/perp | 863,928 | 1.000 | 0.3 | 0 | 0.0 / 0.0 | 0.03 | 146 | 89.9% | 1 | 0 | yes |
| 2023-11-19 | bybit_ob/bybit/DOGE-USDT/perp | 706,770 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 1.27 | 399 | 88.5% | 1 | 20 | yes |
| 2023-11-19 | bybit_ob/bybit/ETH-USDT/perp | 860,073 | 1.000 | 0.4 | 0 | 0.0 / 0.0 | 0.05 | 186 | 91.8% | 0 | 0 | yes |
| 2023-11-19 | bybit_ob/bybit/SOL-USDT/perp | 853,271 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.17 | 537 | 81.7% | 1 | 0 | yes |
| 2023-11-19 | bybit_ob/bybit/TIA-USDT/perp | 851,379 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 1.60 | 920 | 76.6% | 1 | 20 | yes |
| 2023-11-19 | bybit_ob/bybit/WLD-USDT/perp | 764,862 | 1.000 | 2.2 | 0 | 0.0 / 0.0 | 4.16 | 1160 | 91.7% | 1 | 0 | yes |
| 2023-11-19 | bybit_ob/bybit/XRP-USDT/perp | 636,147 | 1.000 | 2.1 | 0 | 0.0 / 0.0 | 1.63 | 287 | 97.2% | 0 | 0 | yes |
| 2023-11-19 | bybit_ob/bybit/ZEC-USDT/perp | 109,344 | 0.701 | 16.6 | 0 | 0.0 / 0.0 | 17.38 | 371 | 100.0% | 0 | 0 | NO |
| 2023-11-20 | binance_bt/binance/AAVE-USDT/perp | 191,051 | 0.996 | 9.2 | 0 | 6.0 / 24.0 | 2.16 | 395 | no trade record | - | - | yes |
| 2023-11-20 | binance_bt/binance/ARB-USDT/perp | 211,069 | 1.000 | 6.4 | 0 | 6.0 / 848.3 | 0.97 | 444 | no trade record | - | - | yes |
| 2023-11-20 | binance_bt/binance/BTC-USDT/perp | 384,909 | 1.000 | 6.4 | 0 | 7.0 / 1552.0 | 0.05 | 235 | no trade record | - | - | yes |
| 2023-11-20 | binance_bt/binance/DOGE-USDT/perp | 144,116 | 1.000 | 3.2 | 0 | 6.0 / 32.0 | 1.28 | 431 | no trade record | - | - | yes |
| 2023-11-20 | binance_bt/binance/ETH-USDT/perp | 408,702 | 1.000 | 5.2 | 0 | 7.0 / 34.0 | 0.10 | 281 | no trade record | - | - | yes |
| 2023-11-20 | binance_bt/binance/SOL-USDT/perp | 2,110,022 | 1.000 | 4.8 | 0 | 6.0 / 40.0 | 0.49 | 558 | no trade record | - | - | yes |
| 2023-11-20 | binance_bt/binance/TIA-USDT/perp | 5,557,600 | 1.000 | 3.6 | 0 | 5.0 / 12.0 | 1.03 | 1000 | no trade record | - | - | yes |
| 2023-11-20 | binance_bt/binance/WLD-USDT/perp | 2,331,199 | 1.000 | 3.7 | 0 | 5.0 / 13.0 | 1.55 | 1355 | no trade record | - | - | yes |
| 2023-11-20 | binance_bt/binance/XRP-USDT/perp | 43,929 | 1.000 | 3.1 | 0 | 6.0 / 52.7 | 1.63 | 267 | no trade record | - | - | yes |
| 2023-11-20 | binance_bt/binance/ZEC-USDT/perp | 15,431 | 0.963 | 17.2 | 0 | 6.0 / 31.0 | 3.45 | 362 | no trade record | - | - | yes |
| 2023-11-20 | bybit_ob/bybit/AAVE-USDT/perp | 558,754 | 1.000 | 3.4 | 0 | 0.0 / 0.0 | 1.10 | 397 | 92.9% | 1 | 0 | yes |
| 2023-11-20 | bybit_ob/bybit/ARB-USDT/perp | 697,263 | 1.000 | 2.9 | 0 | 0.0 / 0.0 | 0.95 | 449 | 89.2% | 1 | 0 | yes |
| 2023-11-20 | bybit_ob/bybit/BTC-USDT/perp | 863,996 | 1.000 | 0.3 | 0 | 0.0 / 0.0 | 0.03 | 237 | 86.9% | 1 | 0 | yes |
| 2023-11-20 | bybit_ob/bybit/DOGE-USDT/perp | 733,623 | 1.000 | 2.5 | 0 | 0.0 / 0.0 | 1.24 | 440 | 89.8% | 1 | 0 | yes |
| 2023-11-20 | bybit_ob/bybit/ETH-USDT/perp | 862,618 | 1.000 | 0.4 | 0 | 0.0 / 0.0 | 0.05 | 278 | 87.8% | 1 | 0 | yes |
| 2023-11-20 | bybit_ob/bybit/SOL-USDT/perp | 859,502 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.17 | 568 | 78.8% | 1 | 0 | yes |
| 2023-11-20 | bybit_ob/bybit/TIA-USDT/perp | 846,268 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 1.82 | 1026 | 77.0% | 1 | 20 | yes |
| 2023-11-20 | bybit_ob/bybit/WLD-USDT/perp | 751,155 | 1.000 | 2.7 | 0 | 0.0 / 0.0 | 4.31 | 1355 | 89.5% | 1 | 0 | yes |
| 2023-11-20 | bybit_ob/bybit/XRP-USDT/perp | 685,565 | 1.000 | 2.1 | 0 | 0.0 / 0.0 | 1.61 | 273 | 96.7% | 0 | 0 | yes |
| 2023-11-20 | bybit_ob/bybit/ZEC-USDT/perp | 126,883 | 0.738 | 16.6 | 0 | 0.0 / 0.0 | 17.14 | 422 | 77.9% | 1 | -50 | NO |
| 2023-11-21 | binance_bt/binance/AAVE-USDT/perp | 289,897 | 0.995 | 10.3 | 0 | 6.0 / 23.0 | 2.24 | 547 | no trade record | - | - | yes |
| 2023-11-21 | binance_bt/binance/ARB-USDT/perp | 401,113 | 1.000 | 6.5 | 0 | 6.0 / 36.0 | 1.96 | 573 | no trade record | - | - | yes |
| 2023-11-21 | binance_bt/binance/BTC-USDT/perp | 488,713 | 1.000 | 3.8 | 0 | 7.0 / 57.0 | 0.05 | 288 | no trade record | - | - | yes |
| 2023-11-21 | binance_bt/binance/DOGE-USDT/perp | 253,606 | 1.000 | 3.7 | 0 | 6.0 / 28.0 | 2.56 | 523 | no trade record | - | - | yes |
| 2023-11-21 | binance_bt/binance/ETH-USDT/perp | 516,641 | 1.000 | 3.6 | 0 | 7.0 / 32.0 | 0.10 | 341 | no trade record | - | - | yes |
| 2023-11-21 | binance_bt/binance/SOL-USDT/perp | 2,935,354 | 1.000 | 3.7 | 0 | 6.0 / 25.0 | 0.55 | 767 | no trade record | - | - | yes |
| 2023-11-21 | binance_bt/binance/TIA-USDT/perp | 6,821,841 | 1.000 | 3.5 | 0 | 5.0 / 11.0 | 1.26 | 1216 | no trade record | - | - | yes |
| 2023-11-21 | binance_bt/binance/WLD-USDT/perp | 1,992,272 | 1.000 | 4.3 | 0 | 5.0 / 13.0 | 1.67 | 1062 | no trade record | - | - | yes |
| 2023-11-21 | binance_bt/binance/XRP-USDT/perp | 97,104 | 1.000 | 3.7 | 0 | 6.0 / 40.0 | 1.72 | 402 | no trade record | - | - | yes |
| 2023-11-21 | binance_bt/binance/ZEC-USDT/perp | 34,834 | 0.954 | 19.3 | 0 | 6.0 / 25.0 | 3.65 | 504 | no trade record | - | - | yes |
| 2023-11-21 | bybit_ob/bybit/AAVE-USDT/perp | 587,777 | 1.000 | 4.2 | 0 | 0.0 / 0.0 | 1.13 | 548 | 92.1% | 2 | 0 | yes |
| 2023-11-21 | bybit_ob/bybit/ARB-USDT/perp | 704,983 | 1.000 | 2.6 | 0 | 0.0 / 0.0 | 0.98 | 580 | 89.4% | 1 | 0 | yes |
| 2023-11-21 | bybit_ob/bybit/BTC-USDT/perp | 863,949 | 1.000 | 0.3 | 0 | 0.0 / 0.0 | 0.03 | 290 | 84.5% | 1 | 0 | yes |
| 2023-11-21 | bybit_ob/bybit/DOGE-USDT/perp | 750,060 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 1.31 | 533 | 87.5% | 1 | 20 | yes |
| 2023-11-21 | bybit_ob/bybit/ETH-USDT/perp | 862,786 | 1.000 | 0.5 | 0 | 0.0 / 0.0 | 0.05 | 344 | 85.9% | 1 | 0 | yes |
| 2023-11-21 | bybit_ob/bybit/SOL-USDT/perp | 859,941 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.18 | 771 | 76.3% | 1 | 0 | yes |
| 2023-11-21 | bybit_ob/bybit/TIA-USDT/perp | 854,973 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 1.85 | 1247 | 76.8% | 1 | 20 | yes |
| 2023-11-21 | bybit_ob/bybit/WLD-USDT/perp | 755,424 | 1.000 | 2.6 | 0 | 0.0 / 0.0 | 4.24 | 1062 | 95.7% | 0 | 20 | yes |
| 2023-11-21 | bybit_ob/bybit/XRP-USDT/perp | 733,605 | 1.000 | 2.3 | 0 | 0.0 / 0.0 | 1.64 | 402 | 92.9% | 0 | 20 | yes |
| 2023-11-21 | bybit_ob/bybit/ZEC-USDT/perp | 181,645 | 0.811 | 16.6 | 0 | 0.0 / 0.0 | 17.53 | 556 | 97.9% | 0 | 0 | NO |
| 2023-11-22 | binance_bt/binance/AAVE-USDT/perp | 258,410 | 0.998 | 7.8 | 0 | 5.0 / 20.0 | 2.11 | 492 | no trade record | - | - | yes |
| 2023-11-22 | binance_bt/binance/ARB-USDT/perp | 148,637 | 1.000 | 5.4 | 0 | 6.0 / 78.0 | 1.04 | 371 | no trade record | - | - | yes |
| 2023-11-22 | binance_bt/binance/BTC-USDT/perp | 367,460 | 1.000 | 3.4 | 0 | 7.0 / 1268.0 | 0.05 | 225 | no trade record | - | - | yes |
| 2023-11-22 | binance_bt/binance/DOGE-USDT/perp | 71,152 | 1.000 | 3.4 | 0 | 6.0 / 31.0 | 1.36 | 280 | no trade record | - | - | yes |
| 2023-11-22 | binance_bt/binance/ETH-USDT/perp | 386,082 | 1.000 | 1.9 | 0 | 6.0 / 30.0 | 0.05 | 276 | no trade record | - | - | yes |
| 2023-11-22 | binance_bt/binance/SOL-USDT/perp | 1,726,583 | 1.000 | 3.4 | 0 | 6.0 / 25.0 | 0.37 | 545 | no trade record | - | - | yes |
| 2023-11-22 | binance_bt/binance/TIA-USDT/perp | 4,502,998 | 1.000 | 3.1 | 0 | 5.0 / 11.0 | 1.05 | 967 | no trade record | - | - | yes |
| 2023-11-22 | binance_bt/binance/WLD-USDT/perp | 1,384,279 | 1.000 | 4.8 | 0 | 5.0 / 12.0 | 1.59 | 1003 | no trade record | - | - | yes |
| 2023-11-22 | binance_bt/binance/XRP-USDT/perp | 31,772 | 1.000 | 3.7 | 0 | 6.0 / 45.0 | 1.69 | 277 | no trade record | - | - | yes |
| 2023-11-22 | binance_bt/binance/ZEC-USDT/perp | 19,618 | 0.980 | 16.5 | 0 | 6.0 / 28.0 | 3.61 | 330 | no trade record | - | - | yes |
| 2023-11-22 | bybit_ob/bybit/AAVE-USDT/perp | 607,427 | 1.000 | 3.6 | 0 | 0.0 / 0.0 | 1.11 | 497 | 92.7% | 1 | 0 | yes |
| 2023-11-22 | bybit_ob/bybit/ARB-USDT/perp | 695,985 | 1.000 | 2.1 | 0 | 0.0 / 0.0 | 1.00 | 370 | 93.8% | 1 | 0 | yes |
| 2023-11-22 | bybit_ob/bybit/BTC-USDT/perp | 863,996 | 1.000 | 0.3 | 0 | 0.0 / 0.0 | 0.03 | 228 | 88.7% | 1 | 0 | yes |
| 2023-11-22 | bybit_ob/bybit/DOGE-USDT/perp | 720,304 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 1.34 | 282 | 91.9% | 1 | 20 | yes |
| 2023-11-22 | bybit_ob/bybit/ETH-USDT/perp | 863,155 | 1.000 | 0.4 | 0 | 0.0 / 0.0 | 0.05 | 278 | 88.7% | 0 | 0 | yes |
| 2023-11-22 | bybit_ob/bybit/SOL-USDT/perp | 858,338 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.18 | 555 | 78.4% | 2 | 0 | yes |
| 2023-11-22 | bybit_ob/bybit/TIA-USDT/perp | 854,495 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 1.61 | 976 | 78.4% | 1 | 0 | yes |
| 2023-11-22 | bybit_ob/bybit/WLD-USDT/perp | 710,103 | 1.000 | 2.5 | 0 | 0.0 / 0.0 | 4.02 | 1006 | 94.2% | 0 | 20 | yes |
| 2023-11-22 | bybit_ob/bybit/XRP-USDT/perp | 709,542 | 1.000 | 1.6 | 0 | 0.0 / 0.0 | 1.68 | 275 | 97.5% | 1 | 0 | yes |
| 2023-11-22 | bybit_ob/bybit/ZEC-USDT/perp | 219,575 | 0.903 | 12.3 | 0 | 0.0 / 0.0 | 10.58 | 360 | 98.7% | 0 | 0 | NO |
| 2023-11-23 | binance_bt/binance/AAVE-USDT/perp | 171,155 | 0.991 | 9.2 | 0 | 5.0 / 18.0 | 2.05 | 455 | no trade record | - | - | yes |
| 2023-11-23 | binance_bt/binance/ARB-USDT/perp | 96,488 | 0.999 | 6.3 | 0 | 6.0 / 27.0 | 0.99 | 301 | no trade record | - | - | yes |
| 2023-11-23 | binance_bt/binance/BTC-USDT/perp | 188,562 | 1.000 | 2.8 | 0 | 7.0 / 38.0 | 0.03 | 157 | no trade record | - | - | yes |
| 2023-11-23 | binance_bt/binance/DOGE-USDT/perp | 39,893 | 1.000 | 3.6 | 0 | 6.0 / 32.0 | 1.32 | 212 | no trade record | - | - | yes |
| 2023-11-23 | binance_bt/binance/ETH-USDT/perp | 241,731 | 1.000 | 3.5 | 0 | 6.0 / 32.0 | 0.05 | 213 | no trade record | - | - | yes |
| 2023-11-23 | binance_bt/binance/SOL-USDT/perp | 1,383,331 | 1.000 | 3.5 | 0 | 6.0 / 19.0 | 0.35 | 442 | no trade record | - | - | yes |
| 2023-11-23 | binance_bt/binance/TIA-USDT/perp | 2,094,098 | 1.000 | 4.5 | 0 | 5.0 / 11.0 | 0.85 | 734 | no trade record | - | - | yes |
| 2023-11-23 | binance_bt/binance/WLD-USDT/perp | 600,158 | 0.998 | 10.8 | 0 | 5.0 / 12.0 | 1.26 | 567 | no trade record | - | - | yes |
| 2023-11-23 | binance_bt/binance/XRP-USDT/perp | 28,843 | 1.000 | 3.5 | 0 | 6.0 / 40.0 | 1.64 | 270 | no trade record | - | - | yes |
| 2023-11-23 | binance_bt/binance/ZEC-USDT/perp | 14,234 | 0.944 | 21.7 | 0 | 6.0 / 25.0 | 3.51 | 266 | no trade record | - | - | NO |
| 2023-11-23 | bybit_ob/bybit/AAVE-USDT/perp | 537,400 | 1.000 | 3.4 | 0 | 0.0 / 0.0 | 1.04 | 458 | 92.5% | 1 | 0 | yes |
| 2023-11-23 | bybit_ob/bybit/ARB-USDT/perp | 629,602 | 1.000 | 3.1 | 0 | 0.0 / 0.0 | 0.98 | 303 | 94.3% | 1 | 0 | yes |
| 2023-11-23 | bybit_ob/bybit/BTC-USDT/perp | 863,978 | 1.000 | 0.3 | 0 | 0.0 / 0.0 | 0.03 | 159 | 91.4% | 1 | 0 | yes |
| 2023-11-23 | bybit_ob/bybit/DOGE-USDT/perp | 648,555 | 1.000 | 3.5 | 0 | 0.0 / 0.0 | 1.32 | 214 | 91.6% | 1 | 0 | yes |
| 2023-11-23 | bybit_ob/bybit/ETH-USDT/perp | 861,117 | 1.000 | 0.4 | 0 | 0.0 / 0.0 | 0.05 | 214 | 90.4% | 1 | 0 | yes |
| 2023-11-23 | bybit_ob/bybit/SOL-USDT/perp | 850,705 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.17 | 448 | 80.7% | 1 | 0 | yes |
| 2023-11-23 | bybit_ob/bybit/TIA-USDT/perp | 824,235 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.88 | 749 | 80.6% | 1 | 0 | NO |
| 2023-11-23 | bybit_ob/bybit/WLD-USDT/perp | 561,893 | 0.999 | 4.5 | 0 | 0.0 / 0.0 | 4.15 | 567 | 96.3% | 1 | 0 | yes |
| 2023-11-23 | bybit_ob/bybit/XRP-USDT/perp | 675,550 | 1.000 | 2.7 | 0 | 0.0 / 0.0 | 1.63 | 267 | 97.1% | 1 | 0 | yes |
| 2023-11-23 | bybit_ob/bybit/ZEC-USDT/perp | 177,650 | 0.845 | 10.2 | 0 | 0.0 / 0.0 | 3.52 | 256 | 97.6% | 0 | 0 | NO |
| 2023-11-24 | binance_bt/binance/AAVE-USDT/perp | 199,624 | 0.988 | 12.5 | 0 | 5.0 / 22.0 | 2.04 | 395 | no trade record | - | - | yes |
| 2023-11-24 | binance_bt/binance/ARB-USDT/perp | 132,879 | 1.000 | 6.2 | 0 | 6.0 / 63.2 | 0.99 | 325 | no trade record | - | - | yes |
| 2023-11-24 | binance_bt/binance/BTC-USDT/perp | 341,340 | 1.000 | 1.5 | 0 | 7.0 / 350.0 | 0.05 | 246 | no trade record | - | - | yes |
| 2023-11-24 | binance_bt/binance/DOGE-USDT/perp | 49,237 | 1.000 | 2.6 | 0 | 6.0 / 50.0 | 1.30 | 254 | no trade record | - | - | yes |
| 2023-11-24 | binance_bt/binance/ETH-USDT/perp | 330,902 | 1.000 | 2.3 | 0 | 6.0 / 39.0 | 0.09 | 261 | no trade record | - | - | yes |
| 2023-11-24 | binance_bt/binance/SOL-USDT/perp | 1,125,408 | 1.000 | 2.4 | 0 | 6.0 / 27.0 | 0.35 | 400 | no trade record | - | - | yes |
| 2023-11-24 | binance_bt/binance/TIA-USDT/perp | 1,638,625 | 1.000 | 5.1 | 0 | 5.0 / 12.0 | 1.07 | 671 | no trade record | - | - | yes |
| 2023-11-24 | binance_bt/binance/WLD-USDT/perp | 726,755 | 0.999 | 8.1 | 0 | 5.0 / 13.0 | 1.59 | 743 | no trade record | - | - | yes |
| 2023-11-24 | binance_bt/binance/XRP-USDT/perp | 24,071 | 1.000 | 2.2 | 0 | 6.0 / 55.0 | 1.62 | 243 | no trade record | - | - | yes |
| 2023-11-24 | binance_bt/binance/ZEC-USDT/perp | 16,089 | 0.962 | 17.3 | 0 | 6.0 / 30.0 | 3.45 | 292 | no trade record | - | - | yes |
| 2023-11-24 | bybit_ob/bybit/AAVE-USDT/perp | 536,499 | 0.999 | 4.0 | 0 | 0.0 / 0.0 | 1.03 | 395 | 91.9% | 1 | 0 | yes |
| 2023-11-24 | bybit_ob/bybit/ARB-USDT/perp | 637,593 | 1.000 | 3.7 | 0 | 0.0 / 0.0 | 0.95 | 325 | 92.5% | 1 | 0 | yes |
| 2023-11-24 | bybit_ob/bybit/BTC-USDT/perp | 863,976 | 1.000 | 0.3 | 0 | 0.0 / 0.0 | 0.03 | 245 | 86.4% | 1 | 0 | yes |
| 2023-11-24 | bybit_ob/bybit/DOGE-USDT/perp | 683,317 | 1.000 | 2.3 | 0 | 0.0 / 0.0 | 1.29 | 255 | 95.0% | 1 | 0 | yes |
| 2023-11-24 | bybit_ob/bybit/ETH-USDT/perp | 860,805 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 261 | 85.8% | 1 | 0 | yes |
| 2023-11-24 | bybit_ob/bybit/SOL-USDT/perp | 854,286 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.17 | 405 | 80.8% | 1 | 0 | yes |
| 2023-11-24 | bybit_ob/bybit/TIA-USDT/perp | 821,933 | 1.000 | 1.5 | 0 | 0.0 / 0.0 | 0.90 | 684 | 81.4% | 1 | 0 | yes |
| 2023-11-24 | bybit_ob/bybit/WLD-USDT/perp | 607,674 | 1.000 | 3.7 | 0 | 0.0 / 0.0 | 4.02 | 742 | 93.9% | 1 | 0 | yes |
| 2023-11-24 | bybit_ob/bybit/XRP-USDT/perp | 639,325 | 1.000 | 2.0 | 0 | 0.0 / 0.0 | 1.61 | 242 | 95.4% | 1 | 20 | yes |
| 2023-11-24 | bybit_ob/bybit/ZEC-USDT/perp | 183,529 | 0.810 | 10.4 | 0 | 0.0 / 0.0 | 3.45 | 288 | 96.4% | 0 | 20 | NO |
| 2023-11-25 | binance_bt/binance/AAVE-USDT/perp | 140,677 | 0.969 | 16.2 | 0 | 5.0 / 14.0 | 2.00 | 341 | no trade record | - | - | yes |
| 2023-11-25 | binance_bt/binance/ARB-USDT/perp | 68,127 | 0.999 | 6.9 | 0 | 6.0 / 21.0 | 0.95 | 244 | no trade record | - | - | yes |
| 2023-11-25 | binance_bt/binance/BTC-USDT/perp | 52,775 | 1.000 | 3.8 | 0 | 7.0 / 41.0 | 0.03 | 80 | no trade record | - | - | yes |
| 2023-11-25 | binance_bt/binance/DOGE-USDT/perp | 28,536 | 1.000 | 3.8 | 0 | 6.0 / 25.0 | 1.28 | 201 | no trade record | - | - | yes |
| 2023-11-25 | binance_bt/binance/ETH-USDT/perp | 82,307 | 1.000 | 3.5 | 0 | 7.0 / 32.0 | 0.05 | 124 | no trade record | - | - | yes |
| 2023-11-25 | binance_bt/binance/SOL-USDT/perp | 816,084 | 1.000 | 3.9 | 0 | 5.0 / 14.0 | 0.34 | 376 | no trade record | - | - | yes |
| 2023-11-25 | binance_bt/binance/TIA-USDT/perp | 1,013,816 | 1.000 | 6.8 | 0 | 5.0 / 10.0 | 1.26 | 603 | no trade record | - | - | yes |
| 2023-11-25 | binance_bt/binance/WLD-USDT/perp | 1,070,042 | 1.000 | 5.0 | 0 | 5.0 / 9.0 | 1.50 | 719 | no trade record | - | - | yes |
| 2023-11-25 | binance_bt/binance/XRP-USDT/perp | 8,057 | 1.000 | 3.7 | 0 | 6.0 / 33.0 | 1.62 | 134 | no trade record | - | - | yes |
| 2023-11-25 | binance_bt/binance/ZEC-USDT/perp | 9,917 | 0.919 | 19.4 | 0 | 5.0 / 22.0 | 3.35 | 254 | no trade record | - | - | NO |
| 2023-11-25 | bybit_ob/bybit/AAVE-USDT/perp | 435,994 | 0.996 | 6.3 | 0 | 0.0 / 0.0 | 1.01 | 346 | 92.9% | 1 | 0 | yes |
| 2023-11-25 | bybit_ob/bybit/ARB-USDT/perp | 549,591 | 1.000 | 3.5 | 0 | 0.0 / 0.0 | 0.94 | 248 | 96.9% | 0 | 0 | yes |
| 2023-11-25 | bybit_ob/bybit/BTC-USDT/perp | 863,987 | 1.000 | 0.3 | 0 | 0.0 / 0.0 | 0.03 | 81 | 94.5% | 1 | 0 | yes |
| 2023-11-25 | bybit_ob/bybit/DOGE-USDT/perp | 571,651 | 1.000 | 3.0 | 0 | 0.0 / 0.0 | 1.27 | 205 | 88.4% | 1 | 20 | yes |
| 2023-11-25 | bybit_ob/bybit/ETH-USDT/perp | 853,838 | 1.000 | 0.8 | 0 | 0.0 / 0.0 | 0.05 | 122 | 94.5% | 1 | 0 | yes |
| 2023-11-25 | bybit_ob/bybit/SOL-USDT/perp | 844,325 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.17 | 379 | 79.3% | 1 | 0 | NO |
| 2023-11-25 | bybit_ob/bybit/TIA-USDT/perp | 791,543 | 1.000 | 2.2 | 0 | 0.0 / 0.0 | 0.72 | 623 | 85.2% | 1 | 0 | yes |
| 2023-11-25 | bybit_ob/bybit/WLD-USDT/perp | 670,985 | 1.000 | 2.6 | 0 | 0.0 / 0.0 | 3.73 | 718 | 94.2% | 0 | 20 | yes |
| 2023-11-25 | bybit_ob/bybit/XRP-USDT/perp | 522,893 | 1.000 | 2.8 | 0 | 0.0 / 0.0 | 1.61 | 131 | 96.8% | 1 | 20 | yes |
| 2023-11-25 | bybit_ob/bybit/ZEC-USDT/perp | 150,477 | 0.750 | 10.2 | 0 | 0.0 / 0.0 | 3.33 | 248 | 98.6% | 0 | 0 | NO |
| 2023-11-26 | binance_bt/binance/AAVE-USDT/perp | 193,170 | 0.986 | 11.9 | 0 | 5.0 / 21.0 | 1.98 | 348 | no trade record | - | - | yes |
| 2023-11-26 | binance_bt/binance/ARB-USDT/perp | 103,128 | 0.999 | 8.0 | 0 | 6.0 / 42.0 | 1.87 | 288 | no trade record | - | - | yes |
| 2023-11-26 | binance_bt/binance/BTC-USDT/perp | 142,569 | 1.000 | 3.9 | 0 | 7.0 / 721.3 | 0.05 | 127 | no trade record | - | - | yes |
| 2023-11-26 | binance_bt/binance/DOGE-USDT/perp | 47,993 | 1.000 | 4.4 | 0 | 6.0 / 45.0 | 1.31 | 228 | no trade record | - | - | yes |
| 2023-11-26 | binance_bt/binance/ETH-USDT/perp | 182,938 | 1.000 | 2.0 | 0 | 7.0 / 55.0 | 0.10 | 183 | no trade record | - | - | yes |
| 2023-11-26 | binance_bt/binance/SOL-USDT/perp | 826,155 | 1.000 | 3.8 | 0 | 6.0 / 22.0 | 0.35 | 327 | no trade record | - | - | yes |
| 2023-11-26 | binance_bt/binance/TIA-USDT/perp | 898,175 | 0.999 | 6.3 | 0 | 5.0 / 14.0 | 1.43 | 530 | no trade record | - | - | yes |
| 2023-11-26 | binance_bt/binance/WLD-USDT/perp | 843,852 | 1.000 | 6.0 | 0 | 5.0 / 11.0 | 1.47 | 688 | no trade record | - | - | yes |
| 2023-11-26 | binance_bt/binance/XRP-USDT/perp | 38,767 | 1.000 | 3.9 | 0 | 6.0 / 42.0 | 1.64 | 263 | no trade record | - | - | yes |
| 2023-11-26 | binance_bt/binance/ZEC-USDT/perp | 13,626 | 0.927 | 18.9 | 0 | 6.0 / 30.8 | 3.41 | 279 | no trade record | - | - | NO |
| 2023-11-26 | bybit_ob/bybit/AAVE-USDT/perp | 503,586 | 0.999 | 4.7 | 0 | 0.0 / 0.0 | 1.00 | 351 | 91.7% | 1 | 0 | yes |
| 2023-11-26 | bybit_ob/bybit/ARB-USDT/perp | 582,584 | 1.000 | 3.4 | 0 | 0.0 / 0.0 | 0.95 | 290 | 94.5% | 1 | 0 | yes |
| 2023-11-26 | bybit_ob/bybit/BTC-USDT/perp | 863,968 | 1.000 | 0.3 | 0 | 0.0 / 0.0 | 0.03 | 129 | 89.2% | 1 | 0 | yes |
| 2023-11-26 | bybit_ob/bybit/DOGE-USDT/perp | 597,150 | 1.000 | 2.5 | 0 | 0.0 / 0.0 | 1.28 | 229 | 91.4% | 1 | 0 | yes |
| 2023-11-26 | bybit_ob/bybit/ETH-USDT/perp | 858,698 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 180 | 89.9% | 1 | 0 | yes |
| 2023-11-26 | bybit_ob/bybit/SOL-USDT/perp | 846,532 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.17 | 338 | 79.3% | 1 | 0 | yes |
| 2023-11-26 | bybit_ob/bybit/TIA-USDT/perp | 780,206 | 1.000 | 2.2 | 0 | 0.0 / 0.0 | 0.92 | 547 | 85.4% | 1 | 0 | yes |
| 2023-11-26 | bybit_ob/bybit/WLD-USDT/perp | 630,548 | 1.000 | 3.4 | 0 | 0.0 / 0.0 | 3.73 | 680 | 95.3% | 0 | 0 | yes |
| 2023-11-26 | bybit_ob/bybit/XRP-USDT/perp | 586,319 | 1.000 | 2.6 | 0 | 0.0 / 0.0 | 1.61 | 262 | 92.4% | 0 | 20 | yes |
| 2023-11-26 | bybit_ob/bybit/ZEC-USDT/perp | 170,731 | 0.791 | 15.3 | 0 | 0.0 / 0.0 | 3.39 | 265 | 96.4% | 0 | 0 | NO |
| 2023-11-27 | binance_bt/binance/AAVE-USDT/perp | 180,135 | 0.993 | 12.4 | 0 | 5.0 / 24.0 | 2.08 | 358 | no trade record | - | - | yes |
| 2023-11-27 | binance_bt/binance/ARB-USDT/perp | 128,070 | 1.000 | 6.8 | 0 | 6.0 / 33.0 | 1.01 | 343 | no trade record | - | - | yes |
| 2023-11-27 | binance_bt/binance/BTC-USDT/perp | 255,642 | 1.000 | 3.1 | 0 | 7.0 / 59.0 | 0.05 | 190 | no trade record | - | - | yes |
| 2023-11-27 | binance_bt/binance/DOGE-USDT/perp | 125,233 | 1.000 | 3.6 | 0 | 6.0 / 30.0 | 1.29 | 448 | no trade record | - | - | yes |
| 2023-11-27 | binance_bt/binance/ETH-USDT/perp | 282,974 | 1.000 | 1.5 | 0 | 7.0 / 43.0 | 0.10 | 236 | no trade record | - | - | yes |
| 2023-11-27 | binance_bt/binance/SOL-USDT/perp | 1,264,196 | 1.000 | 3.0 | 0 | 6.0 / 20.0 | 0.37 | 440 | no trade record | - | - | yes |
| 2023-11-27 | binance_bt/binance/TIA-USDT/perp | 1,524,452 | 1.000 | 7.0 | 0 | 5.0 / 13.0 | 1.67 | 862 | no trade record | - | - | yes |
| 2023-11-27 | binance_bt/binance/WLD-USDT/perp | 915,392 | 1.000 | 7.3 | 0 | 5.0 / 12.0 | 1.56 | 796 | no trade record | - | - | yes |
| 2023-11-27 | binance_bt/binance/XRP-USDT/perp | 28,884 | 1.000 | 2.2 | 0 | 6.0 / 56.0 | 1.67 | 261 | no trade record | - | - | yes |
| 2023-11-27 | binance_bt/binance/ZEC-USDT/perp | 19,720 | 0.961 | 17.7 | 0 | 6.0 / 25.0 | 3.50 | 340 | no trade record | - | - | yes |
| 2023-11-27 | bybit_ob/bybit/AAVE-USDT/perp | 557,164 | 1.000 | 4.1 | 0 | 0.0 / 0.0 | 1.05 | 357 | 95.2% | 1 | 0 | yes |
| 2023-11-27 | bybit_ob/bybit/ARB-USDT/perp | 646,252 | 1.000 | 4.1 | 0 | 0.0 / 0.0 | 0.99 | 346 | 93.3% | 1 | 0 | yes |
| 2023-11-27 | bybit_ob/bybit/BTC-USDT/perp | 864,001 | 1.000 | 0.3 | 0 | 0.0 / 0.0 | 0.03 | 191 | 89.9% | 1 | 0 | yes |
| 2023-11-27 | bybit_ob/bybit/DOGE-USDT/perp | 742,900 | 1.000 | 2.2 | 0 | 0.0 / 0.0 | 1.27 | 453 | 89.4% | 1 | 0 | yes |
| 2023-11-27 | bybit_ob/bybit/ETH-USDT/perp | 861,652 | 1.000 | 0.6 | 0 | 0.0 / 0.0 | 0.05 | 237 | 90.2% | 0 | 0 | yes |
| 2023-11-27 | bybit_ob/bybit/SOL-USDT/perp | 858,055 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.18 | 445 | 80.3% | 1 | 0 | yes |
| 2023-11-27 | bybit_ob/bybit/TIA-USDT/perp | 819,860 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 1.07 | 876 | 82.3% | 1 | 0 | yes |
| 2023-11-27 | bybit_ob/bybit/WLD-USDT/perp | 653,176 | 1.000 | 3.2 | 0 | 0.0 / 0.0 | 3.93 | 792 | 94.3% | 0 | 0 | yes |
| 2023-11-27 | bybit_ob/bybit/XRP-USDT/perp | 651,690 | 1.000 | 2.3 | 0 | 0.0 / 0.0 | 1.66 | 259 | 95.2% | 1 | 20 | yes |
| 2023-11-27 | bybit_ob/bybit/ZEC-USDT/perp | 220,922 | 0.887 | 10.3 | 0 | 0.0 / 0.0 | 3.48 | 330 | 97.3% | 1 | 20 | NO |
| 2023-11-28 | binance_bt/binance/AAVE-USDT/perp | 224,444 | 0.995 | 13.3 | 0 | 5.0 / 22.0 | 2.04 | 390 | no trade record | - | - | yes |
| 2023-11-28 | binance_bt/binance/ARB-USDT/perp | 120,036 | 0.999 | 7.0 | 0 | 6.0 / 32.0 | 1.01 | 317 | no trade record | - | - | yes |
| 2023-11-28 | binance_bt/binance/BTC-USDT/perp | 300,164 | 1.000 | 2.1 | 0 | 7.0 / 40.0 | 0.05 | 203 | no trade record | - | - | yes |
| 2023-11-28 | binance_bt/binance/DOGE-USDT/perp | 82,836 | 1.000 | 2.7 | 0 | 6.0 / 37.0 | 1.30 | 371 | no trade record | - | - | yes |
| 2023-11-28 | binance_bt/binance/ETH-USDT/perp | 254,096 | 1.000 | 2.9 | 0 | 7.0 / 33.0 | 0.05 | 227 | no trade record | - | - | yes |
| 2023-11-28 | binance_bt/binance/SOL-USDT/perp | 936,141 | 1.000 | 3.7 | 0 | 6.0 / 21.0 | 0.36 | 422 | no trade record | - | - | yes |
| 2023-11-28 | binance_bt/binance/TIA-USDT/perp | 1,930,620 | 1.000 | 5.7 | 0 | 5.0 / 12.0 | 1.40 | 900 | no trade record | - | - | yes |
| 2023-11-28 | binance_bt/binance/WLD-USDT/perp | 593,814 | 1.000 | 7.2 | 0 | 5.0 / 14.0 | 1.17 | 583 | no trade record | - | - | yes |
| 2023-11-28 | binance_bt/binance/XRP-USDT/perp | 22,722 | 1.000 | 3.7 | 0 | 6.0 / 52.0 | 1.66 | 226 | no trade record | - | - | yes |
| 2023-11-28 | binance_bt/binance/ZEC-USDT/perp | 22,143 | 0.979 | 12.9 | 0 | 5.0 / 18.0 | 3.53 | 304 | no trade record | - | - | yes |
| 2023-11-28 | bybit_ob/bybit/AAVE-USDT/perp | 558,330 | 1.000 | 5.1 | 1 | 0.0 / 0.0 | 1.06 | 389 | 93.0% | 0 | 0 | yes |
| 2023-11-28 | bybit_ob/bybit/ARB-USDT/perp | 638,360 | 1.000 | 4.7 | 1 | 0.0 / 0.0 | 0.99 | 324 | 93.4% | 1 | 0 | yes |
| 2023-11-28 | bybit_ob/bybit/BTC-USDT/perp | 863,937 | 1.000 | 4.4 | 1 | 0.0 / 0.0 | 0.03 | 206 | 86.9% | 1 | 0 | yes |
| 2023-11-28 | bybit_ob/bybit/DOGE-USDT/perp | 693,314 | 1.000 | 4.7 | 1 | 0.0 / 0.0 | 1.27 | 376 | 87.4% | 1 | 0 | yes |
| 2023-11-28 | bybit_ob/bybit/ETH-USDT/perp | 860,965 | 1.000 | 2.5 | 1 | 0.0 / 0.0 | 0.05 | 226 | 90.7% | 1 | 0 | yes |
| 2023-11-28 | bybit_ob/bybit/SOL-USDT/perp | 858,533 | 1.000 | 3.8 | 1 | 0.0 / 0.0 | 0.18 | 431 | 78.8% | 1 | 0 | yes |
| 2023-11-28 | bybit_ob/bybit/TIA-USDT/perp | 834,894 | 1.000 | 3.3 | 1 | 0.0 / 0.0 | 0.71 | 918 | 80.2% | 1 | 0 | yes |
| 2023-11-28 | bybit_ob/bybit/WLD-USDT/perp | 606,197 | 1.000 | 4.0 | 1 | 0.0 / 0.0 | 4.04 | 582 | 93.7% | 1 | 0 | yes |
| 2023-11-28 | bybit_ob/bybit/XRP-USDT/perp | 633,196 | 1.000 | 3.6 | 1 | 0.0 / 0.0 | 1.65 | 230 | 97.5% | 0 | 0 | yes |
| 2023-11-28 | bybit_ob/bybit/ZEC-USDT/perp | 216,491 | 0.878 | 9.6 | 1 | 0.0 / 0.0 | 3.54 | 303 | 97.9% | 0 | 0 | NO |
| 2023-11-29 | binance_bt/binance/AAVE-USDT/perp | 100,077 | 0.994 | 11.2 | 0 | 6.0 / 24.0 | 1.04 | 332 | no trade record | - | - | yes |
| 2023-11-29 | binance_bt/binance/ARB-USDT/perp | 75,468 | 0.999 | 7.7 | 0 | 6.0 / 29.0 | 1.00 | 273 | no trade record | - | - | yes |
| 2023-11-29 | binance_bt/binance/BTC-USDT/perp | 259,200 | 1.000 | 3.5 | 0 | 7.0 / 54.0 | 0.03 | 186 | no trade record | - | - | yes |
| 2023-11-29 | binance_bt/binance/DOGE-USDT/perp | 83,086 | 1.000 | 3.7 | 0 | 6.0 / 24.0 | 1.25 | 376 | no trade record | - | - | yes |
| 2023-11-29 | binance_bt/binance/ETH-USDT/perp | 197,071 | 1.000 | 2.8 | 0 | 7.0 / 33.0 | 0.05 | 190 | no trade record | - | - | yes |
| 2023-11-29 | binance_bt/binance/SOL-USDT/perp | 1,138,662 | 1.000 | 3.4 | 0 | 6.0 / 19.0 | 0.34 | 500 | no trade record | - | - | yes |
| 2023-11-29 | binance_bt/binance/TIA-USDT/perp | 1,643,159 | 1.000 | 5.5 | 0 | 5.0 / 12.0 | 1.10 | 739 | no trade record | - | - | yes |
| 2023-11-29 | binance_bt/binance/WLD-USDT/perp | 534,672 | 1.000 | 6.2 | 0 | 5.0 / 14.0 | 0.83 | 561 | no trade record | - | - | yes |
| 2023-11-29 | binance_bt/binance/XRP-USDT/perp | 17,671 | 1.000 | 3.5 | 0 | 7.0 / 69.6 | 1.65 | 200 | no trade record | - | - | yes |
| 2023-11-29 | binance_bt/binance/ZEC-USDT/perp | 18,004 | 0.968 | 14.9 | 0 | 5.0 / 22.0 | 3.46 | 284 | no trade record | - | - | yes |
| 2023-11-29 | bybit_ob/bybit/AAVE-USDT/perp | 552,542 | 1.000 | 4.1 | 0 | 0.0 / 0.0 | 1.03 | 331 | 94.2% | 1 | 0 | yes |
| 2023-11-29 | bybit_ob/bybit/ARB-USDT/perp | 605,245 | 1.000 | 3.0 | 0 | 0.0 / 0.0 | 0.99 | 278 | 94.3% | 1 | 0 | yes |
| 2023-11-29 | bybit_ob/bybit/BTC-USDT/perp | 863,996 | 1.000 | 0.3 | 0 | 0.0 / 0.0 | 0.03 | 187 | 88.2% | 1 | 0 | yes |
| 2023-11-29 | bybit_ob/bybit/DOGE-USDT/perp | 680,503 | 1.000 | 2.2 | 0 | 0.0 / 0.0 | 1.24 | 377 | 90.3% | 1 | 0 | yes |
| 2023-11-29 | bybit_ob/bybit/ETH-USDT/perp | 859,082 | 1.000 | 0.6 | 0 | 0.0 / 0.0 | 0.05 | 189 | 89.7% | 1 | 0 | yes |
| 2023-11-29 | bybit_ob/bybit/SOL-USDT/perp | 856,392 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.17 | 508 | 77.3% | 1 | 0 | yes |
| 2023-11-29 | bybit_ob/bybit/TIA-USDT/perp | 815,672 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 0.78 | 762 | 80.9% | 1 | 20 | yes |
| 2023-11-29 | bybit_ob/bybit/WLD-USDT/perp | 575,720 | 1.000 | 2.9 | 0 | 0.0 / 0.0 | 3.92 | 554 | 92.8% | 1 | 0 | yes |
| 2023-11-29 | bybit_ob/bybit/XRP-USDT/perp | 607,215 | 1.000 | 3.0 | 0 | 0.0 / 0.0 | 1.64 | 202 | 97.1% | 0 | 20 | yes |
| 2023-11-29 | bybit_ob/bybit/ZEC-USDT/perp | 201,541 | 0.854 | 10.1 | 0 | 0.0 / 0.0 | 6.86 | 275 | 98.2% | 1 | 0 | NO |
| 2023-11-30 | binance_bt/binance/AAVE-USDT/perp | 63,137 | 0.990 | 10.2 | 0 | 6.0 / 24.0 | 1.05 | 260 | no trade record | - | - | yes |
| 2023-11-30 | binance_bt/binance/ARB-USDT/perp | 54,879 | 1.000 | 6.0 | 0 | 6.0 / 27.0 | 1.00 | 238 | no trade record | - | - | yes |
| 2023-11-30 | binance_bt/binance/BTC-USDT/perp | 172,079 | 1.000 | 3.8 | 0 | 7.0 / 37.0 | 0.03 | 145 | no trade record | - | - | yes |
| 2023-11-30 | binance_bt/binance/DOGE-USDT/perp | 73,908 | 1.000 | 4.6 | 0 | 6.0 / 20.0 | 1.23 | 358 | no trade record | - | - | yes |
| 2023-11-30 | binance_bt/binance/ETH-USDT/perp | 149,787 | 1.000 | 2.6 | 0 | 7.0 / 33.0 | 0.05 | 166 | no trade record | - | - | yes |
| 2023-11-30 | binance_bt/binance/SOL-USDT/perp | 804,870 | 1.000 | 3.8 | 0 | 6.0 / 17.0 | 0.33 | 392 | no trade record | - | - | yes |
| 2023-11-30 | binance_bt/binance/TIA-USDT/perp | 1,396,894 | 1.000 | 6.5 | 0 | 5.0 / 11.0 | 1.25 | 621 | no trade record | - | - | yes |
| 2023-11-30 | binance_bt/binance/WLD-USDT/perp | 381,795 | 0.998 | 8.0 | 0 | 5.0 / 14.0 | 0.84 | 467 | no trade record | - | - | yes |
| 2023-11-30 | binance_bt/binance/XRP-USDT/perp | 14,632 | 1.000 | 3.8 | 0 | 6.0 / 85.0 | 1.66 | 168 | no trade record | - | - | yes |
| 2023-11-30 | binance_bt/binance/ZEC-USDT/perp | 16,048 | 0.960 | 16.3 | 0 | 5.0 / 17.0 | 3.42 | 280 | no trade record | - | - | yes |
| 2023-11-30 | bybit_ob/bybit/AAVE-USDT/perp | 511,683 | 1.000 | 3.6 | 0 | 0.0 / 0.0 | 1.04 | 261 | 93.3% | 1 | 0 | yes |
| 2023-11-30 | bybit_ob/bybit/ARB-USDT/perp | 567,576 | 1.000 | 3.4 | 0 | 0.0 / 0.0 | 0.99 | 238 | 95.9% | 1 | 0 | yes |
| 2023-11-30 | bybit_ob/bybit/BTC-USDT/perp | 863,975 | 1.000 | 0.3 | 0 | 0.0 / 0.0 | 0.03 | 147 | 91.7% | 0 | 0 | yes |
| 2023-11-30 | bybit_ob/bybit/DOGE-USDT/perp | 699,149 | 1.000 | 2.0 | 0 | 0.0 / 0.0 | 1.22 | 362 | 90.4% | 1 | 0 | yes |
| 2023-11-30 | bybit_ob/bybit/ETH-USDT/perp | 858,699 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 167 | 93.3% | 1 | 0 | yes |
| 2023-11-30 | bybit_ob/bybit/SOL-USDT/perp | 854,708 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.17 | 399 | 78.7% | 2 | 0 | NO |
| 2023-11-30 | bybit_ob/bybit/TIA-USDT/perp | 814,494 | 1.000 | 1.5 | 0 | 0.0 / 0.0 | 0.83 | 636 | 79.5% | 1 | 20 | NO |
| 2023-11-30 | bybit_ob/bybit/WLD-USDT/perp | 533,130 | 1.000 | 5.1 | 0 | 0.0 / 0.0 | 4.18 | 462 | 96.7% | 0 | 0 | yes |
| 2023-11-30 | bybit_ob/bybit/XRP-USDT/perp | 599,415 | 1.000 | 2.8 | 0 | 0.0 / 0.0 | 1.65 | 169 | 95.8% | 0 | 20 | yes |
| 2023-11-30 | bybit_ob/bybit/ZEC-USDT/perp | 195,019 | 0.858 | 17.9 | 0 | 0.0 / 0.0 | 3.41 | 265 | 96.1% | 1 | 0 | NO |
| 2023-12-01 | binance_bt/binance/AAVE-USDT/perp | 84,058 | 0.985 | 11.0 | 0 | 6.0 / 30.0 | 1.02 | 292 | no trade record | - | - | yes |
| 2023-12-01 | binance_bt/binance/ARB-USDT/perp | 71,640 | 1.000 | 6.5 | 0 | 6.0 / 40.0 | 0.98 | 281 | no trade record | - | - | yes |
| 2023-12-01 | binance_bt/binance/BTC-USDT/perp | 282,750 | 1.000 | 4.0 | 0 | 7.0 / 95.0 | 0.05 | 192 | no trade record | - | - | yes |
| 2023-12-01 | binance_bt/binance/DOGE-USDT/perp | 54,357 | 1.000 | 3.9 | 0 | 6.0 / 32.0 | 1.21 | 265 | no trade record | - | - | yes |
| 2023-12-01 | binance_bt/binance/ETH-USDT/perp | 260,155 | 1.000 | 2.1 | 0 | 7.0 / 37.0 | 0.05 | 224 | no trade record | - | - | yes |
| 2023-12-01 | binance_bt/binance/SOL-USDT/perp | 725,004 | 1.000 | 3.8 | 0 | 6.0 / 27.0 | 0.33 | 385 | no trade record | - | - | yes |
| 2023-12-01 | binance_bt/binance/TIA-USDT/perp | 2,744,581 | 1.000 | 4.1 | 0 | 5.0 / 10.0 | 1.20 | 767 | no trade record | - | - | yes |
| 2023-12-01 | binance_bt/binance/WLD-USDT/perp | 338,564 | 0.998 | 8.7 | 0 | 5.0 / 21.0 | 0.82 | 388 | no trade record | - | - | yes |
| 2023-12-01 | binance_bt/binance/XRP-USDT/perp | 11,517 | 1.000 | 2.1 | 0 | 7.0 / 49.8 | 1.64 | 157 | no trade record | - | - | yes |
| 2023-12-01 | binance_bt/binance/ZEC-USDT/perp | 15,464 | 0.965 | 14.4 | 0 | 5.0 / 24.0 | 3.39 | 217 | no trade record | - | - | yes |
| 2023-12-01 | bybit_ob/bybit/AAVE-USDT/perp | 475,929 | 0.997 | 4.7 | 0 | 0.0 / 0.0 | 1.00 | 298 | 90.5% | 1 | 0 | yes |
| 2023-12-01 | bybit_ob/bybit/ARB-USDT/perp | 595,477 | 1.000 | 4.2 | 0 | 0.0 / 0.0 | 0.97 | 286 | 94.7% | 1 | 0 | yes |
| 2023-12-01 | bybit_ob/bybit/BTC-USDT/perp | 863,998 | 1.000 | 0.3 | 0 | 0.0 / 0.0 | 0.03 | 194 | 88.5% | 0 | 0 | yes |
| 2023-12-01 | bybit_ob/bybit/DOGE-USDT/perp | 675,549 | 1.000 | 2.0 | 0 | 0.0 / 0.0 | 1.19 | 269 | 90.1% | 1 | 0 | yes |
| 2023-12-01 | bybit_ob/bybit/ETH-USDT/perp | 861,755 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.05 | 224 | 89.0% | 1 | 0 | yes |
| 2023-12-01 | bybit_ob/bybit/SOL-USDT/perp | 857,026 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.17 | 391 | 80.9% | 1 | 0 | yes |
| 2023-12-01 | bybit_ob/bybit/TIA-USDT/perp | 852,984 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 0.79 | 789 | 76.3% | 1 | 20 | yes |
| 2023-12-01 | bybit_ob/bybit/WLD-USDT/perp | 467,987 | 0.997 | 5.9 | 0 | 0.0 / 0.0 | 4.09 | 385 | 96.0% | 1 | 20 | yes |
| 2023-12-01 | bybit_ob/bybit/XRP-USDT/perp | 616,698 | 1.000 | 2.4 | 0 | 0.0 / 0.0 | 1.64 | 158 | 97.1% | 0 | 0 | yes |
| 2023-12-01 | bybit_ob/bybit/ZEC-USDT/perp | 181,618 | 0.832 | 20.0 | 0 | 0.0 / 0.0 | 3.38 | 209 | 95.7% | 1 | 20 | NO |
| 2023-12-02 | binance_bt/binance/AAVE-USDT/perp | 70,364 | 0.966 | 13.6 | 0 | 5.0 / 29.4 | 1.91 | 282 | no trade record | - | - | yes |
| 2023-12-02 | binance_bt/binance/ARB-USDT/perp | 104,988 | 1.000 | 7.2 | 0 | 6.0 / 4982.0 | 0.97 | 328 | no trade record | - | - | yes |
| 2023-12-02 | binance_bt/binance/BTC-USDT/perp | 174,639 | 1.000 | 1.6 | 0 | 8.0 / 5295.0 | 0.05 | 237 | no trade record | - | - | yes |
| 2023-12-02 | binance_bt/binance/DOGE-USDT/perp | 35,447 | 1.000 | 2.7 | 0 | 6.0 / 35.0 | 1.19 | 253 | no trade record | - | - | yes |
| 2023-12-02 | binance_bt/binance/ETH-USDT/perp | 242,614 | 1.000 | 1.7 | 0 | 7.0 / 53.0 | 0.10 | 244 | no trade record | - | - | yes |
| 2023-12-02 | binance_bt/binance/SOL-USDT/perp | 572,857 | 1.000 | 4.1 | 0 | 6.0 / 3653.0 | 0.32 | 359 | no trade record | - | - | yes |
| 2023-12-02 | binance_bt/binance/TIA-USDT/perp | 4,744,947 | 1.000 | 3.7 | 0 | 5.0 / 9.0 | 1.23 | 1142 | no trade record | - | - | yes |
| 2023-12-02 | binance_bt/binance/WLD-USDT/perp | 385,813 | 0.998 | 7.8 | 0 | 5.0 / 16.0 | 0.82 | 466 | no trade record | - | - | yes |
| 2023-12-02 | binance_bt/binance/XRP-USDT/perp | 8,248 | 1.000 | 3.9 | 0 | 7.0 / 60.5 | 1.63 | 130 | no trade record | - | - | yes |
| 2023-12-02 | binance_bt/binance/ZEC-USDT/perp | 16,203 | 0.933 | 16.7 | 0 | 5.0 / 31.0 | 3.31 | 284 | no trade record | - | - | NO |
| 2023-12-02 | bybit_ob/bybit/AAVE-USDT/perp | 444,132 | 0.996 | 4.7 | 0 | 0.0 / 0.0 | 0.98 | 284 | 86.4% | 1 | 0 | yes |
| 2023-12-02 | bybit_ob/bybit/ARB-USDT/perp | 569,641 | 1.000 | 4.1 | 0 | 0.0 / 0.0 | 0.93 | 321 | 92.8% | 1 | 0 | yes |
| 2023-12-02 | bybit_ob/bybit/BTC-USDT/perp | 863,970 | 1.000 | 0.3 | 0 | 0.0 / 0.0 | 0.03 | 219 | 85.0% | 0 | 0 | yes |
| 2023-12-02 | bybit_ob/bybit/DOGE-USDT/perp | 618,244 | 1.000 | 2.6 | 0 | 0.0 / 0.0 | 1.19 | 251 | 89.6% | 1 | 0 | yes |
| 2023-12-02 | bybit_ob/bybit/ETH-USDT/perp | 857,234 | 1.000 | 0.8 | 0 | 0.0 / 0.0 | 0.05 | 248 | 85.0% | 1 | 0 | yes |
| 2023-12-02 | bybit_ob/bybit/SOL-USDT/perp | 850,973 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.16 | 360 | 81.2% | 1 | 0 | yes |
| 2023-12-02 | bybit_ob/bybit/TIA-USDT/perp | 851,564 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 1.23 | 1174 | 73.6% | 2 | 20 | yes |
| 2023-12-02 | bybit_ob/bybit/WLD-USDT/perp | 443,701 | 0.997 | 6.1 | 0 | 0.0 / 0.0 | 4.08 | 459 | 94.6% | 1 | 0 | yes |
| 2023-12-02 | bybit_ob/bybit/XRP-USDT/perp | 552,890 | 1.000 | 2.8 | 0 | 0.0 / 0.0 | 1.63 | 130 | 97.9% | 0 | 0 | yes |
| 2023-12-02 | bybit_ob/bybit/ZEC-USDT/perp | 165,600 | 0.782 | 29.6 | 0 | 0.0 / 0.0 | 3.30 | 267 | 95.4% | 1 | 0 | NO |
| 2023-12-03 | binance_bt/binance/AAVE-USDT/perp | 73,909 | 0.973 | 17.4 | 0 | 5.0 / 27.0 | 0.98 | 273 | no trade record | - | - | yes |
| 2023-12-03 | binance_bt/binance/ARB-USDT/perp | 82,236 | 1.000 | 5.7 | 0 | 6.0 / 546.6 | 0.92 | 298 | no trade record | - | - | yes |
| 2023-12-03 | binance_bt/binance/BTC-USDT/perp | 160,607 | 1.000 | 2.9 | 0 | 7.0 / 2127.0 | 0.05 | 169 | no trade record | - | - | yes |
| 2023-12-03 | binance_bt/binance/DOGE-USDT/perp | 50,200 | 1.000 | 2.1 | 0 | 6.0 / 25.0 | 1.19 | 275 | no trade record | - | - | yes |
| 2023-12-03 | binance_bt/binance/ETH-USDT/perp | 177,606 | 1.000 | 1.2 | 0 | 7.0 / 52.0 | 0.09 | 191 | no trade record | - | - | yes |
| 2023-12-03 | binance_bt/binance/SOL-USDT/perp | 693,055 | 1.000 | 2.6 | 0 | 6.0 / 24.0 | 0.32 | 377 | no trade record | - | - | yes |
| 2023-12-03 | binance_bt/binance/TIA-USDT/perp | 3,453,669 | 1.000 | 3.4 | 0 | 5.0 / 10.0 | 1.14 | 919 | no trade record | - | - | yes |
| 2023-12-03 | binance_bt/binance/WLD-USDT/perp | 407,830 | 0.998 | 8.0 | 0 | 5.0 / 17.0 | 0.81 | 454 | no trade record | - | - | yes |
| 2023-12-03 | binance_bt/binance/XRP-USDT/perp | 19,318 | 1.000 | 2.3 | 0 | 6.0 / 32.0 | 1.61 | 208 | no trade record | - | - | yes |
| 2023-12-03 | binance_bt/binance/ZEC-USDT/perp | 19,901 | 0.943 | 18.6 | 0 | 5.0 / 23.0 | 3.24 | 333 | no trade record | - | - | NO |
| 2023-12-03 | bybit_ob/bybit/AAVE-USDT/perp | 480,238 | 1.000 | 3.9 | 0 | 0.0 / 0.0 | 0.97 | 274 | 89.3% | 1 | 0 | yes |
| 2023-12-03 | bybit_ob/bybit/ARB-USDT/perp | 590,817 | 1.000 | 3.1 | 0 | 0.0 / 0.0 | 0.91 | 296 | 92.0% | 1 | 0 | yes |
| 2023-12-03 | bybit_ob/bybit/BTC-USDT/perp | 863,979 | 1.000 | 0.3 | 0 | 0.0 / 0.0 | 0.03 | 168 | 88.5% | 1 | 0 | yes |
| 2023-12-03 | bybit_ob/bybit/DOGE-USDT/perp | 657,233 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 1.17 | 277 | 88.8% | 1 | 0 | yes |
| 2023-12-03 | bybit_ob/bybit/ETH-USDT/perp | 859,306 | 1.000 | 0.6 | 0 | 0.0 / 0.0 | 0.05 | 189 | 89.5% | 1 | 0 | yes |
| 2023-12-03 | bybit_ob/bybit/SOL-USDT/perp | 853,366 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.16 | 381 | 81.1% | 1 | 0 | yes |
| 2023-12-03 | bybit_ob/bybit/TIA-USDT/perp | 853,449 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 1.20 | 923 | 75.5% | 1 | 20 | yes |
| 2023-12-03 | bybit_ob/bybit/WLD-USDT/perp | 484,603 | 0.999 | 3.3 | 0 | 0.0 / 0.0 | 4.02 | 449 | 97.4% | 1 | 0 | yes |
| 2023-12-03 | bybit_ob/bybit/XRP-USDT/perp | 639,097 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 1.61 | 207 | 96.5% | 1 | 20 | yes |
| 2023-12-03 | bybit_ob/bybit/ZEC-USDT/perp | 191,339 | 0.836 | 21.0 | 0 | 0.0 / 0.0 | 3.23 | 317 | 92.0% | 0 | 20 | NO |
| 2023-12-04 | binance_bt/binance/AAVE-USDT/perp | 225,015 | 0.998 | 9.3 | 0 | 6.0 / 25.0 | 1.95 | 497 | no trade record | - | - | yes |
| 2023-12-04 | binance_bt/binance/ARB-USDT/perp | 294,206 | 1.000 | 4.5 | 0 | 6.0 / 37.0 | 1.79 | 764 | no trade record | - | - | yes |
| 2023-12-04 | binance_bt/binance/BTC-USDT/perp | 593,060 | 1.000 | 1.7 | 0 | 7.0 / 161.0 | 0.05 | 295 | no trade record | - | - | yes |
| 2023-12-04 | binance_bt/binance/DOGE-USDT/perp | 203,994 | 1.000 | 2.6 | 0 | 6.0 / 36.0 | 2.18 | 582 | no trade record | - | - | yes |
| 2023-12-04 | binance_bt/binance/ETH-USDT/perp | 389,420 | 1.000 | 1.0 | 0 | 7.0 / 60.0 | 0.09 | 316 | no trade record | - | - | yes |
| 2023-12-04 | binance_bt/binance/SOL-USDT/perp | 1,114,454 | 1.000 | 2.4 | 0 | 6.0 / 28.0 | 0.33 | 558 | no trade record | - | - | yes |
| 2023-12-04 | binance_bt/binance/TIA-USDT/perp | 6,566,962 | 1.000 | 4.0 | 0 | 5.0 / 11.0 | 1.50 | 1615 | no trade record | - | - | yes |
| 2023-12-04 | binance_bt/binance/WLD-USDT/perp | 680,417 | 1.000 | 8.7 | 0 | 6.0 / 20.0 | 1.19 | 708 | no trade record | - | - | yes |
| 2023-12-04 | binance_bt/binance/XRP-USDT/perp | 92,375 | 1.000 | 3.7 | 0 | 7.0 / 114.0 | 3.16 | 812 | no trade record | - | - | yes |
| 2023-12-04 | binance_bt/binance/ZEC-USDT/perp | 31,976 | 0.991 | 12.5 | 0 | 6.0 / 47.0 | 3.24 | 483 | no trade record | - | - | yes |
| 2023-12-04 | bybit_ob/bybit/AAVE-USDT/perp | 621,210 | 1.000 | 3.2 | 0 | 0.0 / 0.0 | 1.00 | 494 | 88.0% | 1 | 0 | yes |
| 2023-12-04 | bybit_ob/bybit/ARB-USDT/perp | 732,057 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.91 | 817 | 86.7% | 1 | 0 | yes |
| 2023-12-04 | bybit_ob/bybit/BTC-USDT/perp | 864,002 | 1.000 | 0.3 | 0 | 0.0 / 0.0 | 0.02 | 295 | 88.0% | 0 | 0 | yes |
| 2023-12-04 | bybit_ob/bybit/DOGE-USDT/perp | 790,705 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 1.13 | 582 | 87.0% | 1 | 0 | yes |
| 2023-12-04 | bybit_ob/bybit/ETH-USDT/perp | 863,270 | 1.000 | 0.4 | 0 | 0.0 / 0.0 | 0.04 | 317 | 88.6% | 1 | 0 | yes |
| 2023-12-04 | bybit_ob/bybit/SOL-USDT/perp | 859,110 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.16 | 586 | 77.6% | 1 | 0 | yes |
| 2023-12-04 | bybit_ob/bybit/TIA-USDT/perp | 860,721 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 1.74 | 1650 | 75.0% | 1 | 20 | yes |
| 2023-12-04 | bybit_ob/bybit/WLD-USDT/perp | 587,835 | 1.000 | 3.3 | 0 | 0.0 / 0.0 | 4.09 | 707 | 95.5% | 1 | 0 | yes |
| 2023-12-04 | bybit_ob/bybit/XRP-USDT/perp | 749,156 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 1.60 | 882 | 82.8% | 1 | 20 | yes |
| 2023-12-04 | bybit_ob/bybit/ZEC-USDT/perp | 254,194 | 0.930 | 14.2 | 0 | 0.0 / 0.0 | 3.19 | 464 | 93.9% | 1 | 0 | NO |
| 2023-12-05 | binance_bt/binance/AAVE-USDT/perp | 192,322 | 0.995 | 14.6 | 0 | 6.0 / 24.0 | 2.00 | 437 | no trade record | - | - | yes |
| 2023-12-05 | binance_bt/binance/ARB-USDT/perp | 190,465 | 1.000 | 4.0 | 0 | 6.0 / 58.0 | 0.95 | 476 | no trade record | - | - | yes |
| 2023-12-05 | binance_bt/binance/BTC-USDT/perp | 671,115 | 1.000 | 3.0 | 0 | 7.0 / 1027.0 | 0.05 | 320 | no trade record | - | - | yes |
| 2023-12-05 | binance_bt/binance/DOGE-USDT/perp | 201,586 | 1.000 | 3.0 | 0 | 6.0 / 24.0 | 1.14 | 565 | no trade record | - | - | yes |
| 2023-12-05 | binance_bt/binance/ETH-USDT/perp | 453,167 | 1.000 | 1.4 | 0 | 7.0 / 33.0 | 0.09 | 344 | no trade record | - | - | yes |
| 2023-12-05 | binance_bt/binance/SOL-USDT/perp | 984,829 | 1.000 | 3.5 | 0 | 6.0 / 43.0 | 0.33 | 500 | no trade record | - | - | yes |
| 2023-12-05 | binance_bt/binance/TIA-USDT/perp | 5,595,251 | 1.000 | 3.3 | 0 | 5.0 / 10.0 | 1.51 | 1352 | no trade record | - | - | yes |
| 2023-12-05 | binance_bt/binance/WLD-USDT/perp | 612,345 | 0.999 | 6.1 | 0 | 6.0 / 18.0 | 0.84 | 566 | no trade record | - | - | yes |
| 2023-12-05 | binance_bt/binance/XRP-USDT/perp | 35,143 | 1.000 | 2.0 | 0 | 7.0 / 36.6 | 1.63 | 272 | no trade record | - | - | yes |
| 2023-12-05 | binance_bt/binance/ZEC-USDT/perp | 27,470 | 0.988 | 10.7 | 0 | 6.0 / 26.0 | 3.24 | 406 | no trade record | - | - | yes |
| 2023-12-05 | bybit_ob/bybit/AAVE-USDT/perp | 576,709 | 1.000 | 4.0 | 0 | 0.0 / 0.0 | 1.02 | 430 | 87.9% | 1 | 0 | yes |
| 2023-12-05 | bybit_ob/bybit/ARB-USDT/perp | 722,516 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.93 | 481 | 93.0% | 1 | 0 | yes |
| 2023-12-05 | bybit_ob/bybit/BTC-USDT/perp | 864,000 | 1.000 | 0.3 | 0 | 0.0 / 0.0 | 0.02 | 319 | 86.9% | 0 | 0 | yes |
| 2023-12-05 | bybit_ob/bybit/DOGE-USDT/perp | 793,672 | 1.000 | 1.1 | 0 | 0.0 / 0.0 | 1.11 | 568 | 88.3% | 1 | 0 | yes |
| 2023-12-05 | bybit_ob/bybit/ETH-USDT/perp | 863,528 | 1.000 | 0.4 | 0 | 0.0 / 0.0 | 0.04 | 343 | 86.4% | 0 | 0 | yes |
| 2023-12-05 | bybit_ob/bybit/SOL-USDT/perp | 857,688 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.17 | 508 | 79.9% | 1 | 0 | yes |
| 2023-12-05 | bybit_ob/bybit/TIA-USDT/perp | 859,050 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 1.71 | 1359 | 76.1% | 2 | 20 | yes |
| 2023-12-05 | bybit_ob/bybit/WLD-USDT/perp | 558,643 | 1.000 | 3.5 | 0 | 0.0 / 0.0 | 4.09 | 558 | 92.6% | 1 | 0 | yes |
| 2023-12-05 | bybit_ob/bybit/XRP-USDT/perp | 717,872 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 1.62 | 278 | 95.4% | 0 | 20 | yes |
| 2023-12-05 | bybit_ob/bybit/ZEC-USDT/perp | 279,890 | 0.941 | 12.0 | 0 | 0.0 / 0.0 | 3.22 | 396 | 84.8% | 1 | 0 | NO |
| 2023-12-06 | binance_bt/binance/AAVE-USDT/perp | 188,478 | 0.998 | 8.2 | 0 | 6.0 / 20.0 | 2.00 | 440 | no trade record | - | - | yes |
| 2023-12-06 | binance_bt/binance/ARB-USDT/perp | 203,721 | 1.000 | 4.2 | 0 | 6.0 / 21.0 | 0.95 | 468 | no trade record | - | - | yes |
| 2023-12-06 | binance_bt/binance/BTC-USDT/perp | 380,782 | 1.000 | 1.6 | 0 | 7.0 / 28.0 | 0.05 | 266 | no trade record | - | - | yes |
| 2023-12-06 | binance_bt/binance/DOGE-USDT/perp | 707,061 | 1.000 | 1.7 | 0 | 6.0 / 14.0 | 1.93 | 891 | no trade record | - | - | yes |
| 2023-12-06 | binance_bt/binance/ETH-USDT/perp | 357,894 | 1.000 | 1.0 | 0 | 7.0 / 27.0 | 0.04 | 287 | no trade record | - | - | yes |
| 2023-12-06 | binance_bt/binance/SOL-USDT/perp | 1,630,066 | 1.000 | 3.3 | 0 | 6.0 / 15.0 | 0.32 | 672 | no trade record | - | - | yes |
| 2023-12-06 | binance_bt/binance/TIA-USDT/perp | 4,828,183 | 1.000 | 3.8 | 0 | 5.0 / 10.0 | 2.11 | 1568 | no trade record | - | - | yes |
| 2023-12-06 | binance_bt/binance/WLD-USDT/perp | 685,734 | 1.000 | 6.6 | 0 | 6.0 / 16.0 | 1.20 | 684 | no trade record | - | - | yes |
| 2023-12-06 | binance_bt/binance/XRP-USDT/perp | 55,204 | 1.000 | 1.9 | 0 | 6.0 / 25.0 | 1.61 | 379 | no trade record | - | - | yes |
| 2023-12-06 | binance_bt/binance/ZEC-USDT/perp | 28,435 | 0.987 | 16.0 | 0 | 6.0 / 20.7 | 3.23 | 434 | no trade record | - | - | yes |
| 2023-12-06 | bybit_ob/bybit/AAVE-USDT/perp | 583,753 | 1.000 | 3.1 | 0 | 0.0 / 0.0 | 1.02 | 441 | 91.7% | 1 | 0 | yes |
| 2023-12-06 | bybit_ob/bybit/ARB-USDT/perp | 728,473 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.93 | 473 | 90.2% | 1 | 0 | yes |
| 2023-12-06 | bybit_ob/bybit/BTC-USDT/perp | 864,002 | 1.000 | 0.3 | 0 | 0.0 / 0.0 | 0.02 | 266 | 90.4% | 1 | 0 | yes |
| 2023-12-06 | bybit_ob/bybit/DOGE-USDT/perp | 842,980 | 1.000 | 1.0 | 0 | 0.0 / 0.0 | 1.01 | 894 | 85.7% | 1 | 0 | yes |
| 2023-12-06 | bybit_ob/bybit/ETH-USDT/perp | 863,246 | 1.000 | 0.4 | 0 | 0.0 / 0.0 | 0.04 | 288 | 91.7% | 0 | 0 | yes |
| 2023-12-06 | bybit_ob/bybit/SOL-USDT/perp | 860,659 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.16 | 674 | 77.3% | 1 | 0 | yes |
| 2023-12-06 | bybit_ob/bybit/TIA-USDT/perp | 861,704 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 2.30 | 1578 | 76.1% | 1 | 20 | yes |
| 2023-12-06 | bybit_ob/bybit/WLD-USDT/perp | 563,243 | 1.000 | 4.8 | 0 | 0.0 / 0.0 | 4.05 | 685 | 94.6% | 0 | 0 | yes |
| 2023-12-06 | bybit_ob/bybit/XRP-USDT/perp | 755,183 | 1.000 | 1.6 | 0 | 0.0 / 0.0 | 1.60 | 382 | 94.7% | 0 | 0 | yes |
| 2023-12-06 | bybit_ob/bybit/ZEC-USDT/perp | 276,010 | 0.949 | 10.9 | 0 | 0.0 / 0.0 | 3.20 | 425 | 86.8% | 1 | 50 | NO |
| 2023-12-07 | binance_bt/binance/AAVE-USDT/perp | 148,431 | 0.985 | 470.2 | 0 | 6.0 / 22.0 | 1.05 | 391 | no trade record | - | - | yes |
| 2023-12-07 | binance_bt/binance/ARB-USDT/perp | 404,917 | 0.990 | 469.9 | 0 | 6.0 / 19.0 | 1.69 | 616 | no trade record | - | - | yes |
| 2023-12-07 | binance_bt/binance/BTC-USDT/perp | 332,497 | 0.990 | 469.9 | 0 | 7.0 / 45.0 | 0.05 | 239 | no trade record | - | - | yes |
| 2023-12-07 | binance_bt/binance/DOGE-USDT/perp | 202,154 | 0.990 | 469.9 | 0 | 6.0 / 21.0 | 1.07 | 506 | no trade record | - | - | yes |
| 2023-12-07 | binance_bt/binance/ETH-USDT/perp | 386,723 | 0.990 | 469.9 | 0 | 7.0 / 36.0 | 0.08 | 291 | no trade record | - | - | yes |
| 2023-12-07 | binance_bt/binance/SOL-USDT/perp | 1,495,208 | 0.990 | 469.9 | 0 | 6.0 / 17.0 | 0.32 | 667 | no trade record | - | - | yes |
| 2023-12-07 | binance_bt/binance/TIA-USDT/perp | 4,892,619 | 0.990 | 469.9 | 0 | 5.0 / 10.0 | 1.32 | 1053 | no trade record | - | - | yes |
| 2023-12-07 | binance_bt/binance/WLD-USDT/perp | 474,546 | 0.989 | 470.0 | 0 | 6.0 / 17.0 | 0.83 | 492 | no trade record | - | - | yes |
| 2023-12-07 | binance_bt/binance/XRP-USDT/perp | 48,252 | 0.990 | 469.9 | 0 | 6.0 / 27.0 | 1.58 | 352 | no trade record | - | - | yes |
| 2023-12-07 | binance_bt/binance/ZEC-USDT/perp | 28,416 | 0.969 | 471.4 | 0 | 6.0 / 22.0 | 3.19 | 396 | no trade record | - | - | yes |
| 2023-12-07 | bybit_ob/bybit/AAVE-USDT/perp | 553,678 | 1.000 | 3.2 | 0 | 0.0 / 0.0 | 1.02 | 389 | 90.7% | 1 | 0 | yes |
| 2023-12-07 | bybit_ob/bybit/ARB-USDT/perp | 725,250 | 1.000 | 2.7 | 0 | 0.0 / 0.0 | 0.92 | 622 | 86.7% | 1 | 0 | yes |
| 2023-12-07 | bybit_ob/bybit/BTC-USDT/perp | 863,991 | 1.000 | 0.3 | 0 | 0.0 / 0.0 | 0.02 | 243 | 87.2% | 1 | 0 | yes |
| 2023-12-07 | bybit_ob/bybit/DOGE-USDT/perp | 818,945 | 1.000 | 0.9 | 0 | 0.0 / 0.0 | 1.04 | 506 | 92.1% | 1 | 0 | yes |
| 2023-12-07 | bybit_ob/bybit/ETH-USDT/perp | 862,674 | 1.000 | 0.4 | 0 | 0.0 / 0.0 | 0.04 | 290 | 88.8% | 1 | 0 | yes |
| 2023-12-07 | bybit_ob/bybit/SOL-USDT/perp | 857,506 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.16 | 658 | 76.4% | 1 | 0 | yes |
| 2023-12-07 | bybit_ob/bybit/TIA-USDT/perp | 858,384 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 1.51 | 1068 | 78.3% | 1 | 20 | yes |
| 2023-12-07 | bybit_ob/bybit/WLD-USDT/perp | 526,046 | 1.000 | 3.5 | 0 | 0.0 / 0.0 | 4.09 | 485 | 94.0% | 1 | 0 | yes |
| 2023-12-07 | bybit_ob/bybit/XRP-USDT/perp | 743,179 | 1.000 | 1.4 | 0 | 0.0 / 0.0 | 1.56 | 357 | 93.5% | 1 | 0 | yes |
| 2023-12-07 | bybit_ob/bybit/ZEC-USDT/perp | 257,373 | 0.932 | 11.7 | 0 | 0.0 / 0.0 | 3.18 | 389 | 95.9% | 1 | 0 | NO |
| 2023-12-08 | binance_bt/binance/AAVE-USDT/perp | 144,934 | 0.997 | 7.5 | 0 | 6.0 / 19.0 | 1.99 | 381 | no trade record | - | - | yes |
| 2023-12-08 | binance_bt/binance/ARB-USDT/perp | 191,050 | 1.000 | 3.9 | 0 | 6.0 / 22.0 | 0.87 | 425 | no trade record | - | - | yes |
| 2023-12-08 | binance_bt/binance/BTC-USDT/perp | 263,040 | 1.000 | 3.3 | 0 | 7.0 / 36.0 | 0.05 | 203 | no trade record | - | - | yes |
| 2023-12-08 | binance_bt/binance/DOGE-USDT/perp | 135,009 | 1.000 | 3.8 | 0 | 6.0 / 19.0 | 1.04 | 444 | no trade record | - | - | yes |
| 2023-12-08 | binance_bt/binance/ETH-USDT/perp | 294,766 | 1.000 | 2.0 | 0 | 7.0 / 31.0 | 0.08 | 238 | no trade record | - | - | yes |
| 2023-12-08 | binance_bt/binance/SOL-USDT/perp | 1,707,287 | 1.000 | 3.9 | 0 | 5.0 / 15.0 | 0.40 | 661 | no trade record | - | - | yes |
| 2023-12-08 | binance_bt/binance/TIA-USDT/perp | 2,597,258 | 1.000 | 4.0 | 0 | 5.0 / 10.0 | 1.51 | 844 | no trade record | - | - | yes |
| 2023-12-08 | binance_bt/binance/WLD-USDT/perp | 363,554 | 0.999 | 7.1 | 0 | 5.0 / 17.0 | 0.81 | 409 | no trade record | - | - | yes |
| 2023-12-08 | binance_bt/binance/XRP-USDT/perp | 42,956 | 1.000 | 3.8 | 0 | 6.0 / 24.0 | 1.55 | 309 | no trade record | - | - | yes |
| 2023-12-08 | binance_bt/binance/ZEC-USDT/perp | 25,273 | 0.974 | 11.4 | 0 | 6.0 / 22.0 | 3.10 | 369 | no trade record | - | - | yes |
| 2023-12-08 | bybit_ob/bybit/AAVE-USDT/perp | 565,088 | 1.000 | 3.9 | 0 | 0.0 / 0.0 | 1.01 | 374 | 87.3% | 1 | 0 | yes |
| 2023-12-08 | bybit_ob/bybit/ARB-USDT/perp | 763,478 | 1.000 | 1.6 | 0 | 0.0 / 0.0 | 0.86 | 430 | 91.7% | 1 | 0 | yes |
| 2023-12-08 | bybit_ob/bybit/BTC-USDT/perp | 863,998 | 1.000 | 0.3 | 0 | 0.0 / 0.0 | 0.02 | 206 | 88.0% | 1 | 0 | yes |
| 2023-12-08 | bybit_ob/bybit/DOGE-USDT/perp | 800,735 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 1.02 | 446 | 93.0% | 1 | 0 | yes |
| 2023-12-08 | bybit_ob/bybit/ETH-USDT/perp | 863,150 | 1.000 | 0.4 | 0 | 0.0 / 0.0 | 0.04 | 238 | 92.0% | 0 | 0 | yes |
| 2023-12-08 | bybit_ob/bybit/SOL-USDT/perp | 859,184 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.14 | 661 | 77.4% | 1 | 0 | yes |
| 2023-12-08 | bybit_ob/bybit/TIA-USDT/perp | 857,122 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 1.26 | 856 | 76.6% | 1 | 0 | NO |
| 2023-12-08 | bybit_ob/bybit/WLD-USDT/perp | 479,262 | 0.999 | 4.3 | 0 | 0.0 / 0.0 | 4.02 | 402 | 93.9% | 1 | 20 | yes |
| 2023-12-08 | bybit_ob/bybit/XRP-USDT/perp | 723,773 | 1.000 | 2.0 | 0 | 0.0 / 0.0 | 1.54 | 309 | 94.5% | 1 | 0 | yes |
| 2023-12-08 | bybit_ob/bybit/ZEC-USDT/perp | 220,872 | 0.907 | 13.6 | 0 | 0.0 / 0.0 | 3.09 | 365 | 94.5% | 1 | 20 | NO |
| 2023-12-09 | binance_bt/binance/AAVE-USDT/perp | 274,283 | 0.997 | 9.0 | 0 | 6.0 / 18.0 | 1.96 | 575 | no trade record | - | - | yes |
| 2023-12-09 | binance_bt/binance/ARB-USDT/perp | 342,680 | 1.000 | 4.1 | 0 | 6.0 / 20.0 | 1.65 | 621 | no trade record | - | - | yes |
| 2023-12-09 | binance_bt/binance/BTC-USDT/perp | 157,453 | 1.000 | 4.0 | 0 | 8.0 / 36.0 | 0.05 | 156 | no trade record | - | - | yes |
| 2023-12-09 | binance_bt/binance/DOGE-USDT/perp | 162,460 | 1.000 | 3.7 | 0 | 6.0 / 21.0 | 1.02 | 485 | no trade record | - | - | yes |
| 2023-12-09 | binance_bt/binance/ETH-USDT/perp | 272,110 | 1.000 | 2.2 | 0 | 7.0 / 30.0 | 0.08 | 244 | no trade record | - | - | yes |
| 2023-12-09 | binance_bt/binance/SOL-USDT/perp | 1,544,726 | 1.000 | 3.1 | 0 | 6.0 / 15.0 | 0.39 | 608 | no trade record | - | - | yes |
| 2023-12-09 | binance_bt/binance/TIA-USDT/perp | 3,130,501 | 1.000 | 3.7 | 0 | 5.0 / 10.0 | 1.38 | 1023 | no trade record | - | - | yes |
| 2023-12-09 | binance_bt/binance/WLD-USDT/perp | 473,173 | 0.998 | 7.3 | 0 | 6.0 / 16.0 | 0.81 | 528 | no trade record | - | - | yes |
| 2023-12-09 | binance_bt/binance/XRP-USDT/perp | 96,856 | 1.000 | 4.0 | 0 | 6.0 / 26.0 | 1.52 | 469 | no trade record | - | - | yes |
| 2023-12-09 | binance_bt/binance/ZEC-USDT/perp | 33,877 | 0.965 | 14.7 | 0 | 6.0 / 20.0 | 2.96 | 474 | no trade record | - | - | yes |
| 2023-12-09 | bybit_ob/bybit/AAVE-USDT/perp | 584,556 | 1.000 | 3.6 | 0 | 0.0 / 0.0 | 0.99 | 571 | 87.8% | 1 | 0 | yes |
| 2023-12-09 | bybit_ob/bybit/ARB-USDT/perp | 761,115 | 1.000 | 2.0 | 0 | 0.0 / 0.0 | 0.85 | 627 | 85.2% | 1 | 0 | yes |
| 2023-12-09 | bybit_ob/bybit/BTC-USDT/perp | 863,951 | 1.000 | 0.3 | 0 | 0.0 / 0.0 | 0.02 | 159 | 89.5% | 1 | 0 | yes |
| 2023-12-09 | bybit_ob/bybit/DOGE-USDT/perp | 781,256 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.98 | 491 | 91.6% | 1 | 0 | yes |
| 2023-12-09 | bybit_ob/bybit/ETH-USDT/perp | 860,830 | 1.000 | 0.6 | 0 | 0.0 / 0.0 | 0.04 | 244 | 92.1% | 0 | 0 | yes |
| 2023-12-09 | bybit_ob/bybit/SOL-USDT/perp | 857,349 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.13 | 612 | 77.9% | 1 | 0 | yes |
| 2023-12-09 | bybit_ob/bybit/TIA-USDT/perp | 854,029 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 1.47 | 1031 | 76.7% | 2 | 0 | NO |
| 2023-12-09 | bybit_ob/bybit/WLD-USDT/perp | 480,642 | 0.998 | 4.1 | 0 | 0.0 / 0.0 | 3.99 | 527 | 94.1% | 1 | 20 | yes |
| 2023-12-09 | bybit_ob/bybit/XRP-USDT/perp | 736,586 | 1.000 | 1.6 | 0 | 0.0 / 0.0 | 1.47 | 476 | 90.7% | 0 | 0 | yes |
| 2023-12-09 | bybit_ob/bybit/ZEC-USDT/perp | 247,110 | 0.913 | 13.1 | 0 | 0.0 / 0.0 | 2.95 | 460 | 89.9% | 1 | 20 | NO |
| 2023-12-10 | binance_bt/binance/AAVE-USDT/perp | 132,534 | 0.992 | 8.3 | 0 | 6.0 / 22.0 | 2.01 | 358 | no trade record | - | - | yes |
| 2023-12-10 | binance_bt/binance/ARB-USDT/perp | 100,283 | 1.000 | 4.2 | 0 | 6.0 / 24.0 | 0.89 | 335 | no trade record | - | - | yes |
| 2023-12-10 | binance_bt/binance/BTC-USDT/perp | 104,915 | 1.000 | 2.0 | 0 | 8.0 / 37.0 | 0.02 | 123 | no trade record | - | - | yes |
| 2023-12-10 | binance_bt/binance/DOGE-USDT/perp | 98,026 | 1.000 | 3.4 | 0 | 6.0 / 23.0 | 1.02 | 398 | no trade record | - | - | yes |
| 2023-12-10 | binance_bt/binance/ETH-USDT/perp | 155,669 | 1.000 | 4.0 | 0 | 7.0 / 34.0 | 0.04 | 165 | no trade record | - | - | yes |
| 2023-12-10 | binance_bt/binance/SOL-USDT/perp | 1,050,237 | 1.000 | 2.6 | 0 | 6.0 / 16.0 | 0.28 | 435 | no trade record | - | - | yes |
| 2023-12-10 | binance_bt/binance/TIA-USDT/perp | 2,288,004 | 1.000 | 4.3 | 0 | 5.0 / 10.0 | 0.94 | 657 | no trade record | - | - | yes |
| 2023-12-10 | binance_bt/binance/WLD-USDT/perp | 640,794 | 1.000 | 5.5 | 0 | 5.0 / 12.0 | 1.10 | 658 | no trade record | - | - | yes |
| 2023-12-10 | binance_bt/binance/XRP-USDT/perp | 33,201 | 1.000 | 3.8 | 0 | 6.0 / 33.0 | 1.52 | 278 | no trade record | - | - | yes |
| 2023-12-10 | binance_bt/binance/ZEC-USDT/perp | 18,775 | 0.950 | 15.4 | 0 | 5.0 / 20.0 | 3.00 | 345 | no trade record | - | - | yes |
| 2023-12-10 | bybit_ob/bybit/AAVE-USDT/perp | 535,041 | 1.000 | 3.8 | 0 | 0.0 / 0.0 | 1.02 | 353 | 89.6% | 1 | 0 | yes |
| 2023-12-10 | bybit_ob/bybit/ARB-USDT/perp | 719,735 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 0.87 | 334 | 90.9% | 1 | 0 | yes |
| 2023-12-10 | bybit_ob/bybit/BTC-USDT/perp | 863,970 | 1.000 | 0.3 | 0 | 0.0 / 0.0 | 0.02 | 123 | 90.8% | 1 | 0 | yes |
| 2023-12-10 | bybit_ob/bybit/DOGE-USDT/perp | 762,762 | 1.000 | 1.3 | 0 | 0.0 / 0.0 | 1.00 | 402 | 92.7% | 1 | 0 | yes |
| 2023-12-10 | bybit_ob/bybit/ETH-USDT/perp | 859,186 | 1.000 | 0.7 | 0 | 0.0 / 0.0 | 0.04 | 165 | 94.0% | 1 | 0 | yes |
| 2023-12-10 | bybit_ob/bybit/SOL-USDT/perp | 853,039 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.14 | 439 | 80.5% | 1 | 0 | yes |
| 2023-12-10 | bybit_ob/bybit/TIA-USDT/perp | 845,337 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 0.95 | 664 | 76.0% | 2 | 20 | NO |
| 2023-12-10 | bybit_ob/bybit/WLD-USDT/perp | 549,266 | 1.000 | 3.5 | 0 | 0.0 / 0.0 | 3.81 | 647 | 95.1% | 0 | 0 | yes |
| 2023-12-10 | bybit_ob/bybit/XRP-USDT/perp | 682,269 | 1.000 | 2.1 | 0 | 0.0 / 0.0 | 1.51 | 281 | 95.5% | 0 | 0 | yes |
| 2023-12-10 | bybit_ob/bybit/ZEC-USDT/perp | 241,247 | 0.923 | 16.6 | 0 | 0.0 / 0.0 | 2.98 | 339 | 97.1% | 1 | 0 | NO |
| 2023-12-11 | binance_bt/binance/AAVE-USDT/perp | 356,454 | 0.998 | 9.0 | 0 | 6.0 / 26.0 | 2.17 | 808 | no trade record | - | - | yes |
| 2023-12-11 | binance_bt/binance/ARB-USDT/perp | 437,388 | 1.000 | 3.6 | 0 | 6.0 / 34.0 | 1.82 | 927 | no trade record | - | - | yes |
| 2023-12-11 | binance_bt/binance/BTC-USDT/perp | 869,415 | 1.000 | 2.4 | 0 | 7.0 / 56.0 | 0.07 | 512 | no trade record | - | - | yes |
| 2023-12-11 | binance_bt/binance/DOGE-USDT/perp | 615,068 | 1.000 | 3.8 | 0 | 6.0 / 23.0 | 1.98 | 1377 | no trade record | - | - | yes |
| 2023-12-11 | binance_bt/binance/ETH-USDT/perp | 679,046 | 1.000 | 1.6 | 0 | 7.0 / 36.0 | 0.09 | 713 | no trade record | - | - | yes |
| 2023-12-11 | binance_bt/binance/SOL-USDT/perp | 2,340,274 | 1.000 | 2.0 | 0 | 6.0 / 24.0 | 0.44 | 1145 | no trade record | - | - | yes |
| 2023-12-11 | binance_bt/binance/TIA-USDT/perp | 4,920,662 | 1.000 | 4.2 | 0 | 5.0 / 12.0 | 1.53 | 1657 | no trade record | - | - | yes |
| 2023-12-11 | binance_bt/binance/WLD-USDT/perp | 966,707 | 0.999 | 6.9 | 0 | 6.0 / 21.0 | 1.22 | 1056 | no trade record | - | - | yes |
| 2023-12-11 | binance_bt/binance/XRP-USDT/perp | 133,981 | 1.000 | 3.4 | 0 | 7.0 / 35.0 | 1.66 | 659 | no trade record | - | - | yes |
| 2023-12-11 | binance_bt/binance/ZEC-USDT/perp | 53,277 | 0.985 | 12.4 | 0 | 6.0 / 32.0 | 3.36 | 798 | no trade record | - | - | yes |
| 2023-12-11 | bybit_ob/bybit/AAVE-USDT/perp | 651,753 | 1.000 | 3.9 | 0 | 0.0 / 0.0 | 1.10 | 826 | 88.2% | 1 | 0 | yes |
| 2023-12-11 | bybit_ob/bybit/ARB-USDT/perp | 792,078 | 1.000 | 1.5 | 0 | 0.0 / 0.0 | 0.92 | 956 | 88.7% | 1 | 0 | yes |
| 2023-12-11 | bybit_ob/bybit/BTC-USDT/perp | 863,993 | 1.000 | 0.6 | 0 | 0.0 / 0.0 | 0.02 | 550 | 83.3% | 1 | 0 | yes |
| 2023-12-11 | bybit_ob/bybit/DOGE-USDT/perp | 825,806 | 1.000 | 1.1 | 0 | 0.0 / 0.0 | 1.03 | 1222 | 84.0% | 1 | 20 | yes |
| 2023-12-11 | bybit_ob/bybit/ETH-USDT/perp | 862,884 | 1.000 | 0.6 | 0 | 0.0 / 0.0 | 0.04 | 740 | 83.8% | 1 | 0 | yes |
| 2023-12-11 | bybit_ob/bybit/SOL-USDT/perp | 861,551 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 0.14 | 1238 | 74.8% | 1 | 20 | yes |
| 2023-12-11 | bybit_ob/bybit/TIA-USDT/perp | 861,581 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 1.56 | 1711 | 73.6% | 1 | 20 | yes |
| 2023-12-11 | bybit_ob/bybit/WLD-USDT/perp | 629,567 | 1.000 | 5.0 | 0 | 0.0 / 0.0 | 4.05 | 1090 | 91.6% | 1 | 20 | yes |
| 2023-12-11 | bybit_ob/bybit/XRP-USDT/perp | 765,554 | 1.000 | 1.8 | 0 | 0.0 / 0.0 | 1.61 | 695 | 89.2% | 0 | 20 | yes |
| 2023-12-11 | bybit_ob/bybit/ZEC-USDT/perp | 354,983 | 0.970 | 8.5 | 0 | 0.0 / 0.0 | 3.29 | 796 | 95.5% | 1 | 0 | yes |
| 2023-12-12 | binance_bt/binance/AAVE-USDT/perp | 155,657 | 0.997 | 8.8 | 0 | 6.0 / 28.0 | 1.10 | 423 | no trade record | - | - | yes |
| 2023-12-12 | binance_bt/binance/ARB-USDT/perp | 363,616 | 1.000 | 3.8 | 0 | 6.0 / 27.0 | 1.66 | 680 | no trade record | - | - | yes |
| 2023-12-12 | binance_bt/binance/BTC-USDT/perp | 459,458 | 1.000 | 3.6 | 0 | 8.0 / 41.0 | 0.05 | 260 | no trade record | - | - | yes |
| 2023-12-12 | binance_bt/binance/DOGE-USDT/perp | 157,217 | 1.000 | 3.6 | 0 | 6.0 / 29.0 | 1.08 | 455 | no trade record | - | - | yes |
| 2023-12-12 | binance_bt/binance/ETH-USDT/perp | 345,813 | 1.000 | 3.4 | 0 | 7.0 / 42.0 | 0.09 | 268 | no trade record | - | - | yes |
| 2023-12-12 | binance_bt/binance/SOL-USDT/perp | 1,690,585 | 1.000 | 3.6 | 0 | 6.0 / 21.0 | 0.42 | 569 | no trade record | - | - | yes |
| 2023-12-12 | binance_bt/binance/TIA-USDT/perp | 6,812,337 | 1.000 | 3.6 | 0 | 5.0 / 10.0 | 1.19 | 1244 | no trade record | - | - | yes |
| 2023-12-12 | binance_bt/binance/WLD-USDT/perp | 448,546 | 0.998 | 9.0 | 0 | 6.0 / 24.0 | 0.84 | 509 | no trade record | - | - | yes |
| 2023-12-12 | binance_bt/binance/XRP-USDT/perp | 34,348 | 1.000 | 3.4 | 0 | 7.0 / 41.0 | 1.62 | 271 | no trade record | - | - | yes |
| 2023-12-12 | binance_bt/binance/ZEC-USDT/perp | 31,710 | 0.976 | 15.9 | 0 | 6.0 / 28.0 | 3.27 | 444 | no trade record | - | - | yes |
| 2023-12-12 | bybit_ob/bybit/AAVE-USDT/perp | 566,555 | 1.000 | 9.0 | 1 | 0.0 / 0.0 | 1.09 | 417 | 89.5% | 1 | 0 | yes |
| 2023-12-12 | bybit_ob/bybit/ARB-USDT/perp | 787,306 | 1.000 | 10.1 | 1 | 0.0 / 0.0 | 0.87 | 686 | 87.7% | 1 | 0 | yes |
| 2023-12-12 | bybit_ob/bybit/BTC-USDT/perp | 863,920 | 1.000 | 9.4 | 1 | 0.0 / 0.0 | 0.02 | 262 | 88.6% | 1 | 0 | yes |
| 2023-12-12 | bybit_ob/bybit/DOGE-USDT/perp | 798,350 | 1.000 | 10.1 | 1 | 0.0 / 0.0 | 1.05 | 461 | 91.6% | 1 | 0 | yes |
| 2023-12-12 | bybit_ob/bybit/ETH-USDT/perp | 861,183 | 1.000 | 9.3 | 1 | 0.0 / 0.0 | 0.04 | 268 | 91.6% | 0 | 0 | yes |
| 2023-12-12 | bybit_ob/bybit/SOL-USDT/perp | 858,801 | 1.000 | 9.8 | 1 | 0.0 / 0.0 | 0.14 | 577 | 76.5% | 2 | 0 | NO |
| 2023-12-12 | bybit_ob/bybit/TIA-USDT/perp | 862,823 | 1.000 | 9.4 | 1 | 0.0 / 0.0 | 1.49 | 1263 | 73.3% | 1 | 20 | yes |
| 2023-12-12 | bybit_ob/bybit/WLD-USDT/perp | 520,810 | 0.999 | 12.5 | 1 | 0.0 / 0.0 | 4.12 | 504 | 97.0% | 1 | 0 | yes |
| 2023-12-12 | bybit_ob/bybit/XRP-USDT/perp | 705,312 | 1.000 | 8.9 | 1 | 0.0 / 0.0 | 1.61 | 277 | 95.5% | 0 | 20 | yes |
| 2023-12-12 | bybit_ob/bybit/ZEC-USDT/perp | 340,215 | 0.981 | 10.1 | 1 | 0.0 / 0.0 | 3.25 | 434 | 96.9% | 0 | 0 | yes |
| 2023-12-13 | binance_bt/binance/AAVE-USDT/perp | 175,814 | 0.996 | 8.2 | 0 | 6.0 / 31.0 | 2.11 | 477 | no trade record | - | - | yes |
| 2023-12-13 | binance_bt/binance/ARB-USDT/perp | 356,796 | 1.000 | 3.8 | 0 | 6.0 / 30.0 | 1.65 | 621 | no trade record | - | - | yes |
| 2023-12-13 | binance_bt/binance/BTC-USDT/perp | 476,370 | 1.000 | 3.7 | 0 | 8.0 / 47.0 | 0.05 | 274 | no trade record | - | - | yes |
| 2023-12-13 | binance_bt/binance/DOGE-USDT/perp | 154,145 | 1.000 | 3.8 | 0 | 6.0 / 32.0 | 1.10 | 451 | no trade record | - | - | yes |
| 2023-12-13 | binance_bt/binance/ETH-USDT/perp | 400,774 | 1.000 | 3.8 | 0 | 7.0 / 39.0 | 0.09 | 284 | no trade record | - | - | yes |
| 2023-12-13 | binance_bt/binance/SOL-USDT/perp | 1,867,439 | 1.000 | 3.1 | 0 | 6.0 / 23.0 | 0.42 | 601 | no trade record | - | - | yes |
| 2023-12-13 | binance_bt/binance/TIA-USDT/perp | 5,742,296 | 1.000 | 3.6 | 0 | 6.0 / 12.0 | 0.95 | 1105 | no trade record | - | - | yes |
| 2023-12-13 | binance_bt/binance/WLD-USDT/perp | 865,309 | 0.998 | 7.3 | 0 | 6.0 / 21.0 | 1.22 | 820 | no trade record | - | - | yes |
| 2023-12-13 | binance_bt/binance/XRP-USDT/perp | 49,643 | 1.000 | 3.2 | 0 | 7.0 / 43.0 | 1.66 | 307 | no trade record | - | - | yes |
| 2023-12-13 | binance_bt/binance/ZEC-USDT/perp | 33,584 | 0.967 | 13.0 | 0 | 6.0 / 31.0 | 3.33 | 433 | no trade record | - | - | yes |
| 2023-12-13 | bybit_ob/bybit/AAVE-USDT/perp | 573,286 | 1.000 | 4.5 | 0 | 0.0 / 0.0 | 1.10 | 471 | 91.3% | 1 | 0 | yes |
| 2023-12-13 | bybit_ob/bybit/ARB-USDT/perp | 788,862 | 1.000 | 1.2 | 0 | 0.0 / 0.0 | 0.87 | 629 | 87.4% | 1 | 0 | yes |
| 2023-12-13 | bybit_ob/bybit/BTC-USDT/perp | 863,960 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 0.02 | 276 | 87.1% | 1 | 0 | yes |
| 2023-12-13 | bybit_ob/bybit/DOGE-USDT/perp | 784,297 | 1.000 | 1.1 | 0 | 0.0 / 0.0 | 1.08 | 455 | 91.4% | 1 | 0 | yes |
| 2023-12-13 | bybit_ob/bybit/ETH-USDT/perp | 862,892 | 1.000 | 2.0 | 0 | 0.0 / 0.0 | 0.05 | 285 | 89.5% | 0 | 0 | yes |
| 2023-12-13 | bybit_ob/bybit/SOL-USDT/perp | 859,193 | 1.000 | 1.9 | 0 | 0.0 / 0.0 | 0.15 | 604 | 77.4% | 1 | 0 | yes |
| 2023-12-13 | bybit_ob/bybit/TIA-USDT/perp | 861,202 | 1.000 | 0.5 | 0 | 0.0 / 0.0 | 1.08 | 1121 | 72.1% | 1 | 20 | NO |
| 2023-12-13 | bybit_ob/bybit/WLD-USDT/perp | 543,020 | 0.999 | 4.0 | 0 | 0.0 / 0.0 | 4.20 | 808 | 91.7% | 1 | 0 | yes |
| 2023-12-13 | bybit_ob/bybit/XRP-USDT/perp | 719,130 | 1.000 | 1.7 | 0 | 0.0 / 0.0 | 1.64 | 313 | 94.3% | 0 | 20 | yes |
| 2023-12-13 | bybit_ob/bybit/ZEC-USDT/perp | 339,778 | 0.973 | 8.8 | 0 | 0.0 / 0.0 | 3.31 | 433 | 97.9% | 1 | 0 | yes |
| 2023-12-14 | binance_bt/binance/AAVE-USDT/perp | 232,744 | 0.996 | 9.2 | 0 | 6.0 / 19.0 | 1.92 | 527 | no trade record | - | - | yes |
| 2023-12-14 | binance_bt/binance/ARB-USDT/perp | 211,755 | 1.000 | 4.9 | 0 | 6.0 / 29.0 | 1.68 | 484 | no trade record | - | - | yes |
| 2023-12-14 | binance_bt/binance/BTC-USDT/perp | 447,791 | 1.000 | 2.0 | 0 | 8.0 / 73.0 | 0.05 | 284 | no trade record | - | - | yes |
| 2023-12-14 | binance_bt/binance/DOGE-USDT/perp | 120,216 | 1.000 | 3.8 | 0 | 6.0 / 24.0 | 1.05 | 408 | no trade record | - | - | yes |
| 2023-12-14 | binance_bt/binance/ETH-USDT/perp | 337,517 | 1.000 | 3.8 | 0 | 7.0 / 29.0 | 0.09 | 264 | no trade record | - | - | yes |
| 2023-12-14 | binance_bt/binance/SOL-USDT/perp | 1,629,536 | 1.000 | 4.0 | 0 | 6.0 / 18.0 | 0.42 | 606 | no trade record | - | - | yes |
| 2023-12-14 | binance_bt/binance/TIA-USDT/perp | 4,937,567 | 1.000 | 2.9 | 0 | 5.0 / 10.0 | 1.20 | 1149 | no trade record | - | - | yes |
| 2023-12-14 | binance_bt/binance/WLD-USDT/perp | 511,822 | 0.999 | 9.2 | 0 | 6.0 / 17.0 | 1.15 | 583 | no trade record | - | - | yes |
| 2023-12-14 | binance_bt/binance/XRP-USDT/perp | 46,644 | 1.000 | 1.8 | 0 | 7.0 / 35.0 | 1.62 | 285 | no trade record | - | - | yes |
| 2023-12-14 | binance_bt/binance/ZEC-USDT/perp | 36,514 | 0.960 | 17.1 | 0 | 6.0 / 21.0 | 3.31 | 377 | no trade record | - | - | yes |
| 2023-12-14 | bybit_ob/bybit/AAVE-USDT/perp | 588,139 | 0.999 | 9.0 | 1 | 15.0 / 99.0 | 1.03 | 527 | 79.4% | 1 | 0 | yes |
| 2023-12-14 | bybit_ob/bybit/ARB-USDT/perp | 757,088 | 1.000 | 8.9 | 1 | 14.0 / 98.0 | 0.85 | 488 | 88.6% | 1 | 0 | yes |
| 2023-12-14 | bybit_ob/bybit/BTC-USDT/perp | 863,874 | 1.000 | 11.6 | 1 | 3.0 / 8.0 | 0.02 | 286 | 87.2% | 1 | 0 | yes |
| 2023-12-14 | bybit_ob/bybit/DOGE-USDT/perp | 760,751 | 1.000 | 8.9 | 1 | 12.0 / 95.0 | 1.03 | 405 | 88.9% | 1 | 0 | yes |
| 2023-12-14 | bybit_ob/bybit/ETH-USDT/perp | 862,104 | 1.000 | 9.4 | 1 | 4.0 / 16.0 | 0.04 | 267 | 89.4% | 1 | 0 | yes |
| 2023-12-14 | bybit_ob/bybit/SOL-USDT/perp | 856,176 | 1.000 | 11.9 | 1 | 5.0 / 60.0 | 0.14 | 620 | 78.1% | 1 | 0 | yes |
| 2023-12-14 | bybit_ob/bybit/TIA-USDT/perp | 858,471 | 1.000 | 9.8 | 1 | 5.0 / 63.0 | 1.23 | 1163 | 77.3% | 1 | 0 | yes |
| 2023-12-14 | bybit_ob/bybit/WLD-USDT/perp | 523,343 | 0.999 | 9.8 | 1 | 18.0 / 99.0 | 3.88 | 576 | 93.9% | 1 | 0 | yes |
| 2023-12-14 | bybit_ob/bybit/XRP-USDT/perp | 680,952 | 1.000 | 9.0 | 1 | 7.0 / 70.0 | 1.59 | 290 | 91.3% | 0 | 0 | yes |
| 2023-12-14 | bybit_ob/bybit/ZEC-USDT/perp | 328,710 | 0.974 | 9.2 | 1 | 27.0 / 100.0 | 3.28 | 372 | 94.9% | 1 | 0 | yes |
| 2023-12-15 | binance_bt/binance/AAVE-USDT/perp | 455,228 | 1.000 | 6.5 | 0 | 5.0 / 14.0 | 1.73 | 775 | no trade record | - | - | yes |
| 2023-12-15 | binance_bt/binance/ARB-USDT/perp | 133,253 | 1.000 | 5.5 | 0 | 6.0 / 29.0 | 0.91 | 418 | no trade record | - | - | yes |
| 2023-12-15 | binance_bt/binance/BTC-USDT/perp | 274,867 | 1.000 | 3.5 | 0 | 7.0 / 63.0 | 0.05 | 203 | no trade record | - | - | yes |
| 2023-12-15 | binance_bt/binance/DOGE-USDT/perp | 72,789 | 1.000 | 3.6 | 0 | 6.0 / 27.0 | 1.06 | 335 | no trade record | - | - | yes |
| 2023-12-15 | binance_bt/binance/ETH-USDT/perp | 250,379 | 1.000 | 3.5 | 0 | 7.0 / 31.0 | 0.09 | 237 | no trade record | - | - | yes |
| 2023-12-15 | binance_bt/binance/SOL-USDT/perp | 1,904,821 | 1.000 | 3.7 | 0 | 6.0 / 15.0 | 0.39 | 632 | no trade record | - | - | yes |
| 2023-12-15 | binance_bt/binance/TIA-USDT/perp | 3,440,361 | 1.000 | 2.9 | 0 | 5.0 / 10.0 | 1.01 | 1005 | no trade record | - | - | yes |
| 2023-12-15 | binance_bt/binance/WLD-USDT/perp | 503,885 | 1.000 | 5.7 | 0 | 6.0 / 16.0 | 0.79 | 547 | no trade record | - | - | yes |
| 2023-12-15 | binance_bt/binance/XRP-USDT/perp | 31,516 | 1.000 | 3.4 | 0 | 6.0 / 29.8 | 1.61 | 265 | no trade record | - | - | yes |
| 2023-12-15 | binance_bt/binance/ZEC-USDT/perp | 23,071 | 0.941 | 15.9 | 0 | 6.0 / 23.0 | 3.35 | 357 | no trade record | - | - | NO |
| 2023-12-15 | bybit_ob/bybit/AAVE-USDT/perp | 700,625 | 1.000 | 3.4 | 0 | 16.0 / 98.0 | 0.90 | 773 | 84.6% | 1 | 0 | yes |
| 2023-12-15 | bybit_ob/bybit/ARB-USDT/perp | 733,446 | 1.000 | 1.4 | 0 | 19.0 / 99.0 | 0.88 | 418 | 90.6% | 1 | 0 | yes |
| 2023-12-15 | bybit_ob/bybit/BTC-USDT/perp | 863,998 | 1.000 | 0.9 | 0 | 3.0 / 8.0 | 0.02 | 206 | 92.3% | 0 | 0 | yes |
| 2023-12-15 | bybit_ob/bybit/DOGE-USDT/perp | 727,658 | 1.000 | 1.6 | 0 | 14.0 / 95.0 | 1.05 | 339 | 94.7% | 1 | 0 | yes |
| 2023-12-15 | bybit_ob/bybit/ETH-USDT/perp | 862,543 | 1.000 | 0.5 | 0 | 4.0 / 17.0 | 0.04 | 240 | 91.3% | 1 | 0 | yes |
| 2023-12-15 | bybit_ob/bybit/SOL-USDT/perp | 858,281 | 1.000 | 1.4 | 0 | 6.0 / 65.0 | 0.13 | 638 | 77.0% | 1 | 0 | yes |
| 2023-12-15 | bybit_ob/bybit/TIA-USDT/perp | 855,554 | 1.000 | 0.7 | 0 | 6.0 / 76.0 | 0.91 | 1010 | 76.6% | 1 | 0 | NO |
| 2023-12-15 | bybit_ob/bybit/WLD-USDT/perp | 519,324 | 1.000 | 3.8 | 0 | 23.0 / 99.0 | 3.85 | 536 | 95.8% | 0 | 0 | yes |
| 2023-12-15 | bybit_ob/bybit/XRP-USDT/perp | 680,291 | 1.000 | 1.7 | 0 | 9.0 / 72.0 | 1.59 | 269 | 94.7% | 0 | 0 | yes |
| 2023-12-15 | bybit_ob/bybit/ZEC-USDT/perp | 266,086 | 0.942 | 9.6 | 0 | 37.0 / 100.0 | 3.33 | 352 | 97.3% | 1 | 0 | NO |
| 2023-12-16 | binance_bt/binance/AAVE-USDT/perp | 166,194 | 0.998 | 8.0 | 0 | 6.0 / 23.0 | 1.84 | 452 | no trade record | - | - | yes |
| 2023-12-16 | binance_bt/binance/ARB-USDT/perp | 105,829 | 1.000 | 5.7 | 0 | 6.0 / 28.0 | 0.92 | 377 | no trade record | - | - | yes |
| 2023-12-16 | binance_bt/binance/BTC-USDT/perp | 157,128 | 1.000 | 3.8 | 0 | 8.0 / 45.0 | 0.05 | 142 | no trade record | - | - | yes |
| 2023-12-16 | binance_bt/binance/DOGE-USDT/perp | 66,176 | 1.000 | 3.8 | 0 | 6.0 / 33.0 | 1.07 | 334 | no trade record | - | - | yes |
| 2023-12-16 | binance_bt/binance/ETH-USDT/perp | 173,464 | 1.000 | 3.8 | 0 | 7.0 / 34.0 | 0.05 | 175 | no trade record | - | - | yes |
| 2023-12-16 | binance_bt/binance/SOL-USDT/perp | 1,084,686 | 1.000 | 3.8 | 0 | 6.0 / 18.0 | 0.40 | 481 | no trade record | - | - | yes |
| 2023-12-16 | binance_bt/binance/TIA-USDT/perp | 3,551,816 | 1.000 | 3.8 | 0 | 5.0 / 10.0 | 0.90 | 917 | no trade record | - | - | yes |
| 2023-12-16 | binance_bt/binance/WLD-USDT/perp | 3,872,822 | 1.000 | 4.0 | 0 | 5.0 / 10.0 | 1.69 | 1993 | no trade record | - | - | yes |
| 2023-12-16 | binance_bt/binance/XRP-USDT/perp | 12,152 | 1.000 | 3.9 | 0 | 7.0 / 43.0 | 1.62 | 156 | no trade record | - | - | yes |
| 2023-12-16 | binance_bt/binance/ZEC-USDT/perp | 17,174 | 0.909 | 18.2 | 0 | 6.0 / 28.0 | 3.34 | 308 | no trade record | - | - | NO |
| 2023-12-16 | bybit_ob/bybit/AAVE-USDT/perp | 581,577 | 1.000 | 4.2 | 0 | 21.0 / 99.0 | 0.94 | 449 | 82.5% | 1 | 0 | yes |
| 2023-12-16 | bybit_ob/bybit/ARB-USDT/perp | 696,901 | 1.000 | 2.0 | 0 | 21.0 / 99.0 | 0.89 | 380 | 90.8% | 1 | 0 | yes |
| 2023-12-16 | bybit_ob/bybit/BTC-USDT/perp | 863,988 | 1.000 | 0.9 | 0 | 3.0 / 8.0 | 0.02 | 143 | 92.4% | 0 | 0 | yes |
| 2023-12-16 | bybit_ob/bybit/DOGE-USDT/perp | 705,490 | 1.000 | 1.7 | 0 | 15.0 / 96.0 | 1.06 | 337 | 95.9% | 0 | 0 | yes |
| 2023-12-16 | bybit_ob/bybit/ETH-USDT/perp | 860,588 | 1.000 | 0.5 | 0 | 4.0 / 21.0 | 0.04 | 176 | 94.9% | 0 | 0 | yes |
| 2023-12-16 | bybit_ob/bybit/SOL-USDT/perp | 848,670 | 1.000 | 1.4 | 0 | 8.0 / 78.0 | 0.13 | 490 | 77.0% | 1 | 0 | yes |
| 2023-12-16 | bybit_ob/bybit/TIA-USDT/perp | 853,535 | 1.000 | 0.7 | 0 | 6.0 / 81.0 | 1.20 | 914 | 79.3% | 1 | 0 | yes |
| 2023-12-16 | bybit_ob/bybit/WLD-USDT/perp | 701,230 | 1.000 | 4.7 | 0 | 9.0 / 97.0 | 3.23 | 1979 | 84.6% | 0 | 0 | yes |
| 2023-12-16 | bybit_ob/bybit/XRP-USDT/perp | 574,402 | 1.000 | 2.6 | 0 | 10.0 / 72.0 | 1.61 | 157 | 98.2% | 0 | 0 | yes |
| 2023-12-16 | bybit_ob/bybit/ZEC-USDT/perp | 206,363 | 0.889 | 17.0 | 0 | 38.0 / 101.0 | 3.35 | 297 | 97.7% | 1 | 0 | NO |
| 2023-12-17 | binance_bt/binance/AAVE-USDT/perp | 138,401 | 0.995 | 10.1 | 0 | 6.0 / 29.0 | 1.00 | 424 | no trade record | - | - | yes |
| 2023-12-17 | binance_bt/binance/ARB-USDT/perp | 116,586 | 1.000 | 5.0 | 0 | 6.0 / 34.0 | 0.91 | 365 | no trade record | - | - | yes |
| 2023-12-17 | binance_bt/binance/BTC-USDT/perp | 239,124 | 1.000 | 1.4 | 0 | 7.0 / 51.0 | 0.05 | 190 | no trade record | - | - | yes |
| 2023-12-17 | binance_bt/binance/DOGE-USDT/perp | 78,467 | 1.000 | 3.0 | 0 | 6.0 / 30.0 | 1.07 | 330 | no trade record | - | - | yes |
| 2023-12-17 | binance_bt/binance/ETH-USDT/perp | 218,439 | 1.000 | 1.6 | 0 | 7.0 / 37.0 | 0.05 | 195 | no trade record | - | - | yes |
| 2023-12-17 | binance_bt/binance/SOL-USDT/perp | 1,214,912 | 1.000 | 4.0 | 0 | 6.0 / 23.0 | 0.41 | 480 | no trade record | - | - | yes |
| 2023-12-17 | binance_bt/binance/TIA-USDT/perp | 3,105,190 | 1.000 | 4.0 | 0 | 5.0 / 12.0 | 0.98 | 888 | no trade record | - | - | yes |
| 2023-12-17 | binance_bt/binance/WLD-USDT/perp | 4,509,921 | 1.000 | 2.6 | 0 | 5.0 / 11.0 | 1.31 | 1700 | no trade record | - | - | yes |
| 2023-12-17 | binance_bt/binance/XRP-USDT/perp | 20,752 | 1.000 | 2.7 | 0 | 6.0 / 40.0 | 1.62 | 237 | no trade record | - | - | yes |
| 2023-12-17 | binance_bt/binance/ZEC-USDT/perp | 22,503 | 0.928 | 33.7 | 0 | 6.0 / 33.0 | 3.36 | 332 | no trade record | - | - | NO |
| 2023-12-17 | bybit_ob/bybit/AAVE-USDT/perp | 540,768 | 1.000 | 4.2 | 0 | 22.0 / 99.0 | 0.96 | 424 | 87.5% | 1 | 0 | yes |
| 2023-12-17 | bybit_ob/bybit/ARB-USDT/perp | 717,552 | 1.000 | 1.7 | 0 | 19.0 / 99.0 | 0.90 | 367 | 92.0% | 1 | 0 | yes |
| 2023-12-17 | bybit_ob/bybit/BTC-USDT/perp | 863,997 | 1.000 | 0.9 | 0 | 3.0 / 8.0 | 0.02 | 191 | 92.4% | 1 | 0 | yes |
| 2023-12-17 | bybit_ob/bybit/DOGE-USDT/perp | 710,925 | 1.000 | 1.7 | 0 | 15.0 / 97.0 | 1.05 | 334 | 94.5% | 1 | 0 | yes |
| 2023-12-17 | bybit_ob/bybit/ETH-USDT/perp | 861,913 | 1.000 | 0.5 | 0 | 4.0 / 16.0 | 0.05 | 196 | 94.1% | 0 | 0 | yes |
| 2023-12-17 | bybit_ob/bybit/SOL-USDT/perp | 852,265 | 1.000 | 1.4 | 0 | 8.0 / 75.0 | 0.14 | 488 | 80.7% | 1 | 0 | yes |
| 2023-12-17 | bybit_ob/bybit/TIA-USDT/perp | 856,472 | 1.000 | 0.6 | 0 | 6.0 / 78.0 | 1.23 | 886 | 80.9% | 2 | 0 | NO |
| 2023-12-17 | bybit_ob/bybit/WLD-USDT/perp | 837,602 | 1.000 | 1.2 | 0 | 7.0 / 89.0 | 2.43 | 1698 | 86.0% | 0 | 0 | yes |
| 2023-12-17 | bybit_ob/bybit/XRP-USDT/perp | 617,575 | 1.000 | 2.1 | 0 | 10.0 / 71.0 | 1.62 | 234 | 96.5% | 0 | 0 | yes |
| 2023-12-17 | bybit_ob/bybit/ZEC-USDT/perp | 246,293 | 0.929 | 8.7 | 0 | 38.0 / 100.0 | 3.35 | 318 | 98.3% | 0 | 0 | NO |
| 2023-12-18 | binance_bt/binance/AAVE-USDT/perp | 216,710 | 0.994 | 10.0 | 0 | 6.0 / 28.0 | 2.02 | 478 | no trade record | - | - | yes |
| 2023-12-18 | binance_bt/binance/ARB-USDT/perp | 224,963 | 1.000 | 5.2 | 0 | 6.0 / 32.0 | 1.81 | 415 | no trade record | - | - | yes |
| 2023-12-18 | binance_bt/binance/BTC-USDT/perp | 412,504 | 1.000 | 4.1 | 0 | 7.0 / 40.0 | 0.05 | 249 | no trade record | - | - | yes |
| 2023-12-18 | binance_bt/binance/DOGE-USDT/perp | 147,312 | 1.000 | 4.1 | 0 | 6.0 / 31.0 | 1.15 | 399 | no trade record | - | - | yes |
| 2023-12-18 | binance_bt/binance/ETH-USDT/perp | 350,563 | 1.000 | 4.1 | 0 | 7.0 / 35.0 | 0.05 | 252 | no trade record | - | - | yes |
| 2023-12-18 | binance_bt/binance/SOL-USDT/perp | 1,824,992 | 1.000 | 4.1 | 0 | 6.0 / 21.0 | 0.42 | 562 | no trade record | - | - | yes |
| 2023-12-18 | binance_bt/binance/TIA-USDT/perp | 5,256,577 | 1.000 | 4.0 | 0 | 5.0 / 12.0 | 0.99 | 1075 | no trade record | - | - | yes |
| 2023-12-18 | binance_bt/binance/WLD-USDT/perp | 2,822,850 | 1.000 | 4.1 | 0 | 5.0 / 13.0 | 1.21 | 1308 | no trade record | - | - | yes |
| 2023-12-18 | binance_bt/binance/XRP-USDT/perp | 50,132 | 1.000 | 4.1 | 0 | 6.0 / 36.0 | 1.70 | 283 | no trade record | - | - | yes |
| 2023-12-18 | binance_bt/binance/ZEC-USDT/perp | 34,146 | 0.970 | 19.3 | 0 | 6.0 / 29.0 | 3.54 | 470 | no trade record | - | - | yes |
| 2023-12-18 | bybit_ob/bybit/AAVE-USDT/perp | 574,154 | 1.000 | 4.0 | 0 | 20.0 / 99.0 | 1.03 | 472 | 87.4% | 1 | 0 | yes |
| 2023-12-18 | bybit_ob/bybit/ARB-USDT/perp | 737,068 | 1.000 | 1.5 | 0 | 18.0 / 99.0 | 0.93 | 421 | 90.2% | 1 | 0 | yes |
| 2023-12-18 | bybit_ob/bybit/BTC-USDT/perp | 864,000 | 1.000 | 0.9 | 0 | 3.0 / 9.0 | 0.02 | 249 | 92.2% | 0 | 0 | yes |
| 2023-12-18 | bybit_ob/bybit/DOGE-USDT/perp | 738,399 | 1.000 | 1.8 | 0 | 14.0 / 96.0 | 1.10 | 405 | 93.3% | 1 | 0 | yes |
| 2023-12-18 | bybit_ob/bybit/ETH-USDT/perp | 863,175 | 1.000 | 0.5 | 0 | 4.0 / 15.0 | 0.05 | 252 | 92.7% | 1 | 0 | yes |
| 2023-12-18 | bybit_ob/bybit/SOL-USDT/perp | 855,283 | 1.000 | 1.4 | 0 | 7.0 / 71.0 | 0.14 | 572 | 78.0% | 1 | 0 | NO |
| 2023-12-18 | bybit_ob/bybit/TIA-USDT/perp | 857,360 | 1.000 | 0.6 | 0 | 6.0 / 71.0 | 1.67 | 1091 | 77.8% | 1 | 0 | yes |
| 2023-12-18 | bybit_ob/bybit/WLD-USDT/perp | 780,597 | 1.000 | 1.7 | 0 | 10.0 / 95.0 | 2.55 | 1312 | 86.5% | 1 | 0 | yes |
| 2023-12-18 | bybit_ob/bybit/XRP-USDT/perp | 682,116 | 1.000 | 2.6 | 0 | 8.0 / 71.0 | 1.66 | 285 | 96.4% | 0 | 0 | yes |
| 2023-12-18 | bybit_ob/bybit/ZEC-USDT/perp | 282,963 | 0.949 | 19.1 | 0 | 35.0 / 100.0 | 3.50 | 470 | 93.7% | 1 | 0 | NO |
| 2023-12-19 | binance_bt/binance/AAVE-USDT/perp | 223,072 | 0.997 | 8.2 | 0 | 6.0 / 25.0 | 1.89 | 576 | no trade record | - | - | yes |
| 2023-12-19 | binance_bt/binance/ARB-USDT/perp | 131,815 | 1.000 | 5.1 | 0 | 6.0 / 35.0 | 0.93 | 389 | no trade record | - | - | yes |
| 2023-12-19 | binance_bt/binance/BTC-USDT/perp | 360,076 | 1.000 | 4.0 | 0 | 7.0 / 41.0 | 0.05 | 252 | no trade record | - | - | yes |
| 2023-12-19 | binance_bt/binance/DOGE-USDT/perp | 78,411 | 1.000 | 4.0 | 0 | 6.0 / 33.0 | 1.11 | 332 | no trade record | - | - | yes |
| 2023-12-19 | binance_bt/binance/ETH-USDT/perp | 294,845 | 1.000 | 4.0 | 0 | 7.0 / 37.0 | 0.05 | 261 | no trade record | - | - | yes |
| 2023-12-19 | binance_bt/binance/SOL-USDT/perp | 1,404,721 | 1.000 | 2.8 | 0 | 6.0 / 21.0 | 0.40 | 509 | no trade record | - | - | yes |
| 2023-12-19 | binance_bt/binance/TIA-USDT/perp | 3,334,060 | 1.000 | 4.0 | 0 | 5.0 / 12.0 | 0.94 | 933 | no trade record | - | - | yes |
| 2023-12-19 | binance_bt/binance/WLD-USDT/perp | 1,821,573 | 1.000 | 4.0 | 0 | 5.0 / 13.0 | 1.19 | 1075 | no trade record | - | - | yes |
| 2023-12-19 | binance_bt/binance/XRP-USDT/perp | 21,134 | 1.000 | 4.0 | 0 | 7.0 / 66.7 | 1.66 | 218 | no trade record | - | - | yes |
| 2023-12-19 | binance_bt/binance/ZEC-USDT/perp | 24,908 | 0.954 | 26.6 | 0 | 6.0 / 29.0 | 3.59 | 386 | no trade record | - | - | yes |
| 2023-12-19 | bybit_ob/bybit/AAVE-USDT/perp | 591,757 | 1.000 | 3.3 | 0 | 21.0 / 99.0 | 0.97 | 566 | 88.5% | 1 | 0 | yes |
| 2023-12-19 | bybit_ob/bybit/ARB-USDT/perp | 726,170 | 1.000 | 2.1 | 0 | 19.0 / 99.0 | 0.91 | 393 | 92.8% | 1 | 0 | yes |
| 2023-12-19 | bybit_ob/bybit/BTC-USDT/perp | 864,001 | 1.000 | 0.9 | 0 | 3.0 / 8.0 | 0.02 | 251 | 91.7% | 0 | 0 | yes |
| 2023-12-19 | bybit_ob/bybit/DOGE-USDT/perp | 714,176 | 1.000 | 1.8 | 0 | 15.0 / 97.0 | 1.09 | 333 | 93.6% | 1 | 0 | yes |
| 2023-12-19 | bybit_ob/bybit/ETH-USDT/perp | 862,765 | 1.000 | 0.5 | 0 | 4.0 / 15.0 | 0.04 | 263 | 91.2% | 0 | 0 | yes |
| 2023-12-19 | bybit_ob/bybit/SOL-USDT/perp | 854,441 | 1.000 | 1.4 | 0 | 6.0 / 70.0 | 0.13 | 513 | 79.7% | 1 | 0 | yes |
| 2023-12-19 | bybit_ob/bybit/TIA-USDT/perp | 855,018 | 1.000 | 0.6 | 0 | 7.0 / 77.0 | 1.53 | 931 | 77.7% | 1 | 0 | yes |
| 2023-12-19 | bybit_ob/bybit/WLD-USDT/perp | 735,536 | 1.000 | 2.1 | 0 | 14.0 / 98.0 | 2.55 | 1059 | 91.5% | 0 | 0 | yes |
| 2023-12-19 | bybit_ob/bybit/XRP-USDT/perp | 629,282 | 1.000 | 2.4 | 0 | 9.0 / 72.0 | 1.64 | 217 | 96.9% | 0 | 0 | yes |
| 2023-12-19 | bybit_ob/bybit/ZEC-USDT/perp | 251,133 | 0.922 | 9.9 | 0 | 33.0 / 100.0 | 3.54 | 375 | 88.2% | 1 | 0 | NO |
| 2023-12-20 | binance_bt/binance/AAVE-USDT/perp | 176,292 | 0.994 | 8.4 | 0 | 6.0 / 28.0 | 1.91 | 435 | no trade record | - | - | yes |
| 2023-12-20 | binance_bt/binance/ARB-USDT/perp | 149,023 | 1.000 | 4.7 | 0 | 6.0 / 34.0 | 0.93 | 380 | no trade record | - | - | yes |
| 2023-12-20 | binance_bt/binance/BTC-USDT/perp | 424,372 | 1.000 | 3.8 | 0 | 7.0 / 48.0 | 0.05 | 259 | no trade record | - | - | yes |
| 2023-12-20 | binance_bt/binance/DOGE-USDT/perp | 94,861 | 1.000 | 3.8 | 0 | 6.0 / 34.4 | 1.11 | 347 | no trade record | - | - | yes |
| 2023-12-20 | binance_bt/binance/ETH-USDT/perp | 339,589 | 1.000 | 3.7 | 0 | 7.0 / 34.0 | 0.05 | 293 | no trade record | - | - | yes |
| 2023-12-20 | binance_bt/binance/SOL-USDT/perp | 2,261,520 | 1.000 | 4.0 | 0 | 6.0 / 18.0 | 0.39 | 706 | no trade record | - | - | yes |
| 2023-12-20 | binance_bt/binance/TIA-USDT/perp | 3,879,585 | 1.000 | 3.9 | 0 | 5.0 / 11.0 | 0.91 | 1039 | no trade record | - | - | yes |
| 2023-12-20 | binance_bt/binance/WLD-USDT/perp | 1,267,097 | 1.000 | 3.9 | 0 | 5.0 / 14.0 | 1.12 | 973 | no trade record | - | - | yes |
| 2023-12-20 | binance_bt/binance/XRP-USDT/perp | 34,752 | 1.000 | 3.9 | 0 | 6.0 / 40.0 | 1.64 | 283 | no trade record | - | - | yes |
| 2023-12-20 | binance_bt/binance/ZEC-USDT/perp | 23,083 | 0.956 | 19.4 | 0 | 6.0 / 28.0 | 3.53 | 449 | no trade record | - | - | yes |
| 2023-12-20 | bybit_ob/bybit/AAVE-USDT/perp | 581,070 | 1.000 | 3.8 | 0 | 23.0 / 99.0 | 0.98 | 435 | 83.5% | 1 | 0 | yes |
| 2023-12-20 | bybit_ob/bybit/ARB-USDT/perp | 742,797 | 1.000 | 1.5 | 0 | 18.0 / 99.0 | 0.90 | 386 | 90.5% | 1 | 0 | yes |
| 2023-12-20 | bybit_ob/bybit/BTC-USDT/perp | 864,000 | 1.000 | 0.9 | 0 | 3.0 / 8.0 | 0.02 | 261 | 90.3% | 0 | 0 | yes |
| 2023-12-20 | bybit_ob/bybit/DOGE-USDT/perp | 729,293 | 1.000 | 1.9 | 0 | 14.0 / 96.0 | 1.10 | 353 | 93.3% | 1 | 0 | yes |
| 2023-12-20 | bybit_ob/bybit/ETH-USDT/perp | 863,111 | 1.000 | 0.5 | 0 | 4.0 / 15.0 | 0.05 | 293 | 90.7% | 0 | 0 | yes |
| 2023-12-20 | bybit_ob/bybit/SOL-USDT/perp | 856,974 | 1.000 | 1.4 | 0 | 6.0 / 66.0 | 0.13 | 709 | 76.3% | 1 | 0 | yes |
| 2023-12-20 | bybit_ob/bybit/TIA-USDT/perp | 858,395 | 1.000 | 0.5 | 0 | 6.0 / 68.0 | 1.55 | 1049 | 78.5% | 1 | 0 | yes |
| 2023-12-20 | bybit_ob/bybit/WLD-USDT/perp | 716,318 | 1.000 | 2.3 | 0 | 16.0 / 98.0 | 2.80 | 965 | 89.1% | 1 | 0 | yes |
| 2023-12-20 | bybit_ob/bybit/XRP-USDT/perp | 670,453 | 1.000 | 2.6 | 0 | 8.0 / 69.0 | 1.63 | 285 | 94.4% | 0 | 0 | yes |
| 2023-12-20 | bybit_ob/bybit/ZEC-USDT/perp | 242,869 | 0.937 | 8.7 | 0 | 38.0 / 100.0 | 3.50 | 440 | 80.6% | 1 | 20 | NO |
| 2023-12-21 | binance_bt/binance/AAVE-USDT/perp | 140,120 | 0.993 | 10.0 | 0 | 6.0 / 22.0 | 1.96 | 391 | no trade record | - | - | yes |
| 2023-12-21 | binance_bt/binance/ARB-USDT/perp | 170,005 | 1.000 | 4.7 | 0 | 6.0 / 26.0 | 0.91 | 424 | no trade record | - | - | yes |
| 2023-12-21 | binance_bt/binance/BTC-USDT/perp | 343,867 | 1.000 | 2.8 | 0 | 7.0 / 40.0 | 0.02 | 241 | no trade record | - | - | yes |
| 2023-12-21 | binance_bt/binance/DOGE-USDT/perp | 152,945 | 1.000 | 3.9 | 0 | 6.0 / 25.0 | 1.10 | 524 | no trade record | - | - | yes |
| 2023-12-21 | binance_bt/binance/ETH-USDT/perp | 339,012 | 1.000 | 2.5 | 0 | 6.0 / 28.0 | 0.05 | 288 | no trade record | - | - | yes |
| 2023-12-21 | binance_bt/binance/SOL-USDT/perp | 2,904,204 | 1.000 | 3.9 | 0 | 6.0 / 15.0 | 0.46 | 826 | no trade record | - | - | yes |
| 2023-12-21 | binance_bt/binance/TIA-USDT/perp | 2,893,248 | 1.000 | 4.0 | 0 | 5.0 / 10.0 | 0.87 | 872 | no trade record | - | - | yes |
| 2023-12-21 | binance_bt/binance/WLD-USDT/perp | 1,252,401 | 1.000 | 4.1 | 0 | 5.0 / 12.0 | 1.09 | 893 | no trade record | - | - | yes |
| 2023-12-21 | binance_bt/binance/XRP-USDT/perp | 18,689 | 1.000 | 3.9 | 0 | 6.0 / 34.0 | 1.63 | 206 | no trade record | - | - | yes |
| 2023-12-21 | binance_bt/binance/ZEC-USDT/perp | 20,338 | 0.938 | 20.7 | 0 | 6.0 / 26.0 | 3.40 | 347 | no trade record | - | - | NO |
| 2023-12-21 | bybit_ob/bybit/AAVE-USDT/perp | 558,412 | 1.000 | 4.1 | 0 | 23.0 / 99.0 | 1.00 | 389 | 88.1% | 1 | 0 | yes |
| 2023-12-21 | bybit_ob/bybit/ARB-USDT/perp | 748,615 | 1.000 | 2.1 | 0 | 18.0 / 99.0 | 0.89 | 432 | 90.6% | 1 | 0 | yes |
| 2023-12-21 | bybit_ob/bybit/BTC-USDT/perp | 863,995 | 1.000 | 0.9 | 0 | 3.0 / 8.0 | 0.02 | 241 | 92.4% | 1 | 0 | yes |
| 2023-12-21 | bybit_ob/bybit/DOGE-USDT/perp | 721,175 | 1.000 | 1.8 | 0 | 14.0 / 95.0 | 1.09 | 534 | 90.3% | 1 | 0 | yes |
| 2023-12-21 | bybit_ob/bybit/ETH-USDT/perp | 862,993 | 1.000 | 0.5 | 0 | 4.0 / 16.0 | 0.04 | 290 | 91.2% | 1 | 0 | yes |
| 2023-12-21 | bybit_ob/bybit/SOL-USDT/perp | 861,289 | 1.000 | 1.4 | 0 | 6.0 / 55.0 | 0.12 | 831 | 74.9% | 1 | 0 | yes |
| 2023-12-21 | bybit_ob/bybit/TIA-USDT/perp | 858,361 | 1.000 | 0.6 | 0 | 6.0 / 68.0 | 1.53 | 881 | 77.8% | 1 | 0 | yes |
| 2023-12-21 | bybit_ob/bybit/WLD-USDT/perp | 699,464 | 1.000 | 2.9 | 0 | 17.0 / 98.0 | 2.76 | 888 | 90.9% | 1 | 0 | yes |
| 2023-12-21 | bybit_ob/bybit/XRP-USDT/perp | 634,767 | 1.000 | 2.0 | 0 | 7.0 / 66.0 | 1.62 | 209 | 97.8% | 0 | 0 | yes |
| 2023-12-21 | bybit_ob/bybit/ZEC-USDT/perp | 230,539 | 0.928 | 9.9 | 0 | 40.0 / 101.0 | 3.37 | 339 | 93.6% | 1 | 0 | NO |
| 2023-12-22 | binance_bt/binance/AAVE-USDT/perp | 163,392 | 0.995 | 10.2 | 0 | 6.0 / 21.0 | 1.96 | 401 | no trade record | - | - | yes |
| 2023-12-22 | binance_bt/binance/ARB-USDT/perp | 907,193 | 1.000 | 4.2 | 0 | 6.0 / 15.0 | 1.47 | 999 | no trade record | - | - | yes |
| 2023-12-22 | binance_bt/binance/BTC-USDT/perp | 282,235 | 1.000 | 3.6 | 0 | 7.0 / 41.0 | 0.02 | 213 | no trade record | - | - | yes |
| 2023-12-22 | binance_bt/binance/DOGE-USDT/perp | 99,967 | 1.000 | 2.8 | 0 | 6.0 / 22.0 | 1.08 | 357 | no trade record | - | - | yes |
| 2023-12-22 | binance_bt/binance/ETH-USDT/perp | 437,648 | 1.000 | 1.9 | 0 | 6.0 / 25.0 | 0.04 | 352 | no trade record | - | - | yes |
| 2023-12-22 | binance_bt/binance/SOL-USDT/perp | 3,217,981 | 1.000 | 2.8 | 0 | 6.0 / 14.0 | 0.33 | 798 | no trade record | - | - | yes |
| 2023-12-22 | binance_bt/binance/TIA-USDT/perp | 2,547,708 | 1.000 | 4.2 | 0 | 5.0 / 11.0 | 0.90 | 744 | no trade record | - | - | yes |
| 2023-12-22 | binance_bt/binance/WLD-USDT/perp | 1,117,247 | 1.000 | 4.3 | 0 | 5.0 / 12.0 | 1.10 | 806 | no trade record | - | - | yes |
| 2023-12-22 | binance_bt/binance/XRP-USDT/perp | 27,447 | 1.000 | 4.8 | 0 | 6.0 / 24.0 | 1.61 | 309 | no trade record | - | - | yes |
| 2023-12-22 | binance_bt/binance/ZEC-USDT/perp | 25,530 | 0.941 | 28.1 | 0 | 6.0 / 23.0 | 3.35 | 376 | no trade record | - | - | NO |
| 2023-12-22 | bybit_ob/bybit/AAVE-USDT/perp | 589,143 | 1.000 | 3.7 | 0 | 20.0 / 99.0 | 1.00 | 399 | 84.6% | 1 | 0 | yes |
| 2023-12-22 | bybit_ob/bybit/ARB-USDT/perp | 817,117 | 1.000 | 1.2 | 0 | 9.0 / 95.0 | 0.78 | 1015 | 84.4% | 1 | 0 | yes |
| 2023-12-22 | bybit_ob/bybit/BTC-USDT/perp | 863,947 | 1.000 | 0.9 | 0 | 3.0 / 7.0 | 0.02 | 209 | 92.7% | 0 | 0 | yes |
| 2023-12-22 | bybit_ob/bybit/DOGE-USDT/perp | 738,416 | 1.000 | 1.7 | 0 | 14.0 / 95.0 | 1.07 | 360 | 93.7% | 1 | 0 | yes |
| 2023-12-22 | bybit_ob/bybit/ETH-USDT/perp | 863,360 | 1.000 | 0.7 | 0 | 4.0 / 15.0 | 0.04 | 352 | 89.0% | 1 | 0 | yes |
| 2023-12-22 | bybit_ob/bybit/SOL-USDT/perp | 860,722 | 1.000 | 1.4 | 0 | 6.0 / 50.0 | 0.11 | 799 | 75.5% | 1 | 0 | yes |
| 2023-12-22 | bybit_ob/bybit/TIA-USDT/perp | 850,961 | 1.000 | 0.7 | 0 | 8.0 / 65.0 | 0.83 | 750 | 79.9% | 1 | 0 | yes |
| 2023-12-22 | bybit_ob/bybit/WLD-USDT/perp | 705,449 | 1.000 | 3.0 | 0 | 17.0 / 98.0 | 2.77 | 803 | 92.1% | 1 | 0 | yes |
| 2023-12-22 | bybit_ob/bybit/XRP-USDT/perp | 654,970 | 1.000 | 2.3 | 0 | 6.0 / 52.0 | 1.61 | 306 | 96.1% | 2 | 0 | yes |
| 2023-12-22 | bybit_ob/bybit/ZEC-USDT/perp | 248,845 | 0.940 | 18.0 | 0 | 42.0 / 101.0 | 3.32 | 355 | 95.4% | 1 | 0 | NO |
| 2023-12-23 | binance_bt/binance/AAVE-USDT/perp | 143,711 | 0.992 | 13.2 | 0 | 5.0 / 20.0 | 1.97 | 395 | no trade record | - | - | yes |
| 2023-12-23 | binance_bt/binance/ARB-USDT/perp | 451,205 | 1.000 | 4.3 | 0 | 6.0 / 16.0 | 1.44 | 695 | no trade record | - | - | yes |
| 2023-12-23 | binance_bt/binance/BTC-USDT/perp | 116,114 | 1.000 | 2.4 | 0 | 7.0 / 35.0 | 0.02 | 125 | no trade record | - | - | yes |
| 2023-12-23 | binance_bt/binance/DOGE-USDT/perp | 43,760 | 1.000 | 4.7 | 0 | 6.0 / 26.0 | 1.08 | 246 | no trade record | - | - | yes |
| 2023-12-23 | binance_bt/binance/ETH-USDT/perp | 185,074 | 1.000 | 3.8 | 0 | 7.0 / 29.0 | 0.04 | 201 | no trade record | - | - | yes |
| 2023-12-23 | binance_bt/binance/SOL-USDT/perp | 2,356,705 | 1.000 | 4.3 | 0 | 6.0 / 14.0 | 0.32 | 676 | no trade record | - | - | yes |
| 2023-12-23 | binance_bt/binance/TIA-USDT/perp | 1,517,835 | 1.000 | 5.1 | 0 | 5.0 / 11.0 | 0.99 | 572 | no trade record | - | - | yes |
| 2023-12-23 | binance_bt/binance/WLD-USDT/perp | 709,421 | 1.000 | 4.3 | 0 | 5.0 / 12.0 | 1.08 | 590 | no trade record | - | - | yes |
| 2023-12-23 | binance_bt/binance/XRP-USDT/perp | 10,331 | 1.000 | 4.3 | 0 | 6.0 / 35.7 | 1.62 | 158 | no trade record | - | - | yes |
| 2023-12-23 | binance_bt/binance/ZEC-USDT/perp | 13,760 | 0.863 | 25.3 | 0 | 6.0 / 22.0 | 3.33 | 285 | no trade record | - | - | NO |
| 2023-12-23 | bybit_ob/bybit/AAVE-USDT/perp | 525,474 | 0.999 | 4.0 | 0 | 23.0 / 99.0 | 1.02 | 396 | 86.5% | 1 | 0 | yes |
| 2023-12-23 | bybit_ob/bybit/ARB-USDT/perp | 795,467 | 1.000 | 1.0 | 0 | 13.0 / 97.0 | 0.75 | 698 | 84.8% | 1 | 0 | yes |
| 2023-12-23 | bybit_ob/bybit/BTC-USDT/perp | 863,993 | 1.000 | 0.9 | 0 | 3.0 / 7.0 | 0.02 | 124 | 94.1% | 1 | 0 | yes |
| 2023-12-23 | bybit_ob/bybit/DOGE-USDT/perp | 669,593 | 1.000 | 1.7 | 0 | 17.0 / 97.0 | 1.07 | 253 | 94.9% | 1 | 0 | yes |
| 2023-12-23 | bybit_ob/bybit/ETH-USDT/perp | 861,816 | 1.000 | 0.5 | 0 | 4.0 / 18.0 | 0.04 | 202 | 93.8% | 1 | 0 | yes |
| 2023-12-23 | bybit_ob/bybit/SOL-USDT/perp | 858,987 | 1.000 | 1.4 | 0 | 6.0 / 58.0 | 0.10 | 679 | 74.6% | 1 | 0 | yes |
| 2023-12-23 | bybit_ob/bybit/TIA-USDT/perp | 841,895 | 1.000 | 1.0 | 0 | 9.0 / 65.0 | 0.84 | 566 | 87.3% | 1 | 0 | yes |
| 2023-12-23 | bybit_ob/bybit/WLD-USDT/perp | 592,207 | 1.000 | 3.5 | 0 | 22.0 / 99.0 | 2.94 | 584 | 91.1% | 1 | 0 | yes |
| 2023-12-23 | bybit_ob/bybit/XRP-USDT/perp | 593,550 | 1.000 | 1.9 | 0 | 6.0 / 55.0 | 1.62 | 158 | 95.7% | 1 | 0 | yes |
| 2023-12-23 | bybit_ob/bybit/ZEC-USDT/perp | 166,711 | 0.856 | 15.1 | 0 | 45.0 / 101.0 | 3.31 | 272 | 96.1% | 1 | 0 | NO |
| 2023-12-24 | binance_bt/binance/AAVE-USDT/perp | 227,522 | 0.996 | 11.4 | 0 | 6.0 / 21.0 | 1.95 | 522 | no trade record | - | - | yes |
| 2023-12-24 | binance_bt/binance/ARB-USDT/perp | 523,150 | 1.000 | 4.1 | 0 | 6.0 / 21.0 | 1.41 | 709 | no trade record | - | - | yes |
| 2023-12-24 | binance_bt/binance/BTC-USDT/perp | 167,364 | 1.000 | 3.3 | 0 | 7.0 / 89.0 | 0.05 | 199 | no trade record | - | - | yes |
| 2023-12-24 | binance_bt/binance/DOGE-USDT/perp | 86,804 | 1.000 | 3.3 | 0 | 6.0 / 32.0 | 1.09 | 366 | no trade record | - | - | yes |
| 2023-12-24 | binance_bt/binance/ETH-USDT/perp | 228,416 | 1.000 | 4.2 | 0 | 7.0 / 30.0 | 0.04 | 235 | no trade record | - | - | yes |
| 2023-12-24 | binance_bt/binance/SOL-USDT/perp | 3,860,415 | 1.000 | 3.0 | 0 | 6.0 / 15.0 | 0.36 | 981 | no trade record | - | - | yes |
| 2023-12-24 | binance_bt/binance/TIA-USDT/perp | 3,756,687 | 1.000 | 3.8 | 0 | 5.0 / 10.0 | 1.33 | 1153 | no trade record | - | - | yes |
| 2023-12-24 | binance_bt/binance/WLD-USDT/perp | 819,196 | 1.000 | 4.1 | 0 | 5.0 / 15.0 | 0.90 | 688 | no trade record | - | - | yes |
| 2023-12-24 | binance_bt/binance/XRP-USDT/perp | 28,801 | 1.000 | 3.1 | 0 | 6.0 / 36.0 | 1.64 | 257 | no trade record | - | - | yes |
| 2023-12-24 | binance_bt/binance/ZEC-USDT/perp | 29,839 | 0.926 | 20.7 | 0 | 6.0 / 23.0 | 3.34 | 430 | no trade record | - | - | NO |
| 2023-12-24 | bybit_ob/bybit/AAVE-USDT/perp | 590,919 | 1.000 | 2.9 | 0 | 20.0 / 99.0 | 0.99 | 522 | 80.9% | 2 | 0 | NO |
| 2023-12-24 | bybit_ob/bybit/ARB-USDT/perp | 801,267 | 1.000 | 1.0 | 0 | 13.0 / 97.0 | 0.72 | 710 | 85.0% | 1 | 0 | yes |
| 2023-12-24 | bybit_ob/bybit/BTC-USDT/perp | 863,995 | 1.000 | 0.9 | 0 | 3.0 / 7.0 | 0.02 | 198 | 89.9% | 1 | 0 | yes |
| 2023-12-24 | bybit_ob/bybit/DOGE-USDT/perp | 701,362 | 1.000 | 1.8 | 0 | 16.0 / 97.0 | 1.07 | 363 | 90.1% | 2 | 0 | yes |
| 2023-12-24 | bybit_ob/bybit/ETH-USDT/perp | 862,361 | 1.000 | 0.5 | 0 | 4.0 / 18.0 | 0.04 | 237 | 90.3% | 0 | 0 | yes |
| 2023-12-24 | bybit_ob/bybit/SOL-USDT/perp | 862,020 | 1.000 | 1.4 | 0 | 6.0 / 48.0 | 0.09 | 967 | 74.4% | 1 | 0 | yes |
| 2023-12-24 | bybit_ob/bybit/TIA-USDT/perp | 852,506 | 1.000 | 0.8 | 0 | 7.0 / 65.0 | 1.49 | 1152 | 81.4% | 1 | 0 | yes |
| 2023-12-24 | bybit_ob/bybit/WLD-USDT/perp | 619,138 | 1.000 | 3.5 | 0 | 21.0 / 99.0 | 2.91 | 679 | 90.7% | 1 | 0 | yes |
| 2023-12-24 | bybit_ob/bybit/XRP-USDT/perp | 649,015 | 1.000 | 1.7 | 0 | 6.0 / 53.0 | 1.61 | 253 | 94.2% | 0 | 0 | yes |
| 2023-12-24 | bybit_ob/bybit/ZEC-USDT/perp | 242,829 | 0.946 | 10.2 | 0 | 42.0 / 101.0 | 3.30 | 406 | 90.4% | 1 | 0 | NO |
| 2023-12-25 | binance_bt/binance/AAVE-USDT/perp | 225,723 | 0.996 | 10.8 | 0 | 5.0 / 16.0 | 1.92 | 462 | no trade record | - | - | yes |
| 2023-12-25 | binance_bt/binance/ARB-USDT/perp | 272,066 | 1.000 | 4.5 | 0 | 6.0 / 19.0 | 1.44 | 478 | no trade record | - | - | yes |
| 2023-12-25 | binance_bt/binance/BTC-USDT/perp | 193,299 | 1.000 | 2.5 | 0 | 7.0 / 34.0 | 0.02 | 181 | no trade record | - | - | yes |
| 2023-12-25 | binance_bt/binance/DOGE-USDT/perp | 53,245 | 1.000 | 4.1 | 0 | 6.0 / 27.0 | 1.08 | 294 | no trade record | - | - | yes |
| 2023-12-25 | binance_bt/binance/ETH-USDT/perp | 214,536 | 1.000 | 2.8 | 0 | 6.0 / 26.0 | 0.04 | 199 | no trade record | - | - | yes |
| 2023-12-25 | binance_bt/binance/SOL-USDT/perp | 3,764,779 | 1.000 | 1.7 | 0 | 6.0 / 12.0 | 0.34 | 794 | no trade record | - | - | yes |
| 2023-12-25 | binance_bt/binance/TIA-USDT/perp | 2,802,891 | 1.000 | 3.5 | 0 | 5.0 / 10.0 | 1.16 | 833 | no trade record | - | - | yes |
| 2023-12-25 | binance_bt/binance/WLD-USDT/perp | 1,108,340 | 1.000 | 4.9 | 0 | 5.0 / 11.0 | 1.16 | 799 | no trade record | - | - | yes |
| 2023-12-25 | binance_bt/binance/XRP-USDT/perp | 41,862 | 1.000 | 4.1 | 0 | 6.0 / 21.0 | 1.60 | 348 | no trade record | - | - | yes |
| 2023-12-25 | binance_bt/binance/ZEC-USDT/perp | 24,043 | 0.967 | 14.2 | 0 | 6.0 / 21.0 | 3.25 | 375 | no trade record | - | - | yes |
| 2023-12-25 | bybit_ob/bybit/AAVE-USDT/perp | 584,245 | 1.000 | 3.1 | 0 | 21.0 / 99.0 | 0.99 | 455 | 81.3% | 2 | 0 | NO |
| 2023-12-25 | bybit_ob/bybit/ARB-USDT/perp | 787,654 | 1.000 | 1.2 | 0 | 16.0 / 98.0 | 0.73 | 478 | 90.6% | 1 | 0 | yes |
| 2023-12-25 | bybit_ob/bybit/BTC-USDT/perp | 864,002 | 1.000 | 0.9 | 0 | 3.0 / 8.0 | 0.02 | 179 | 92.4% | 0 | 0 | yes |
| 2023-12-25 | bybit_ob/bybit/DOGE-USDT/perp | 664,195 | 1.000 | 2.1 | 0 | 16.0 / 97.0 | 1.07 | 294 | 96.6% | 1 | 0 | yes |
| 2023-12-25 | bybit_ob/bybit/ETH-USDT/perp | 862,489 | 1.000 | 0.5 | 0 | 4.0 / 17.0 | 0.04 | 201 | 91.5% | 0 | 0 | yes |
| 2023-12-25 | bybit_ob/bybit/SOL-USDT/perp | 861,062 | 1.000 | 1.4 | 0 | 6.0 / 50.0 | 0.09 | 805 | 74.1% | 1 | 0 | yes |
| 2023-12-25 | bybit_ob/bybit/TIA-USDT/perp | 848,401 | 1.000 | 0.7 | 0 | 8.0 / 68.0 | 1.38 | 833 | 81.8% | 1 | 0 | yes |
| 2023-12-25 | bybit_ob/bybit/WLD-USDT/perp | 651,692 | 1.000 | 2.9 | 0 | 18.0 / 99.0 | 2.75 | 794 | 89.8% | 1 | 0 | yes |
| 2023-12-25 | bybit_ob/bybit/XRP-USDT/perp | 673,958 | 1.000 | 1.5 | 0 | 6.0 / 52.0 | 1.57 | 348 | 95.8% | 0 | 0 | yes |
| 2023-12-25 | bybit_ob/bybit/ZEC-USDT/perp | 223,882 | 0.934 | 10.0 | 0 | 41.0 / 101.0 | 3.23 | 356 | 96.3% | 1 | 0 | NO |
| 2023-12-26 | binance_bt/binance/AAVE-USDT/perp | 445,071 | 0.996 | 9.6 | 0 | 6.0 / 22.0 | 1.92 | 749 | no trade record | - | - | yes |
| 2023-12-26 | binance_bt/binance/ARB-USDT/perp | 363,939 | 1.000 | 4.5 | 0 | 6.0 / 28.0 | 1.49 | 644 | no trade record | - | - | yes |
| 2023-12-26 | binance_bt/binance/BTC-USDT/perp | 303,234 | 1.000 | 2.2 | 0 | 7.0 / 129.0 | 0.05 | 217 | no trade record | - | - | yes |
| 2023-12-26 | binance_bt/binance/DOGE-USDT/perp | 113,803 | 1.000 | 3.6 | 0 | 6.0 / 34.0 | 2.13 | 636 | no trade record | - | - | yes |
| 2023-12-26 | binance_bt/binance/ETH-USDT/perp | 327,451 | 1.000 | 2.2 | 0 | 7.0 / 33.0 | 0.05 | 236 | no trade record | - | - | yes |
| 2023-12-26 | binance_bt/binance/SOL-USDT/perp | 3,934,155 | 1.000 | 3.0 | 0 | 6.0 / 14.0 | 0.46 | 869 | no trade record | - | - | yes |
| 2023-12-26 | binance_bt/binance/TIA-USDT/perp | 2,786,423 | 1.000 | 4.2 | 0 | 5.0 / 12.0 | 1.19 | 889 | no trade record | - | - | yes |
| 2023-12-26 | binance_bt/binance/WLD-USDT/perp | 1,548,867 | 1.000 | 4.4 | 0 | 5.0 / 14.0 | 1.34 | 1196 | no trade record | - | - | yes |
| 2023-12-26 | binance_bt/binance/XRP-USDT/perp | 61,199 | 1.000 | 1.9 | 0 | 6.0 / 38.0 | 1.64 | 366 | no trade record | - | - | yes |
| 2023-12-26 | binance_bt/binance/ZEC-USDT/perp | 44,644 | 0.974 | 14.6 | 0 | 6.0 / 25.0 | 3.37 | 632 | no trade record | - | - | yes |
| 2023-12-26 | bybit_ob/bybit/AAVE-USDT/perp | 625,053 | 1.000 | 8.0 | 1 | 18.0 / 98.0 | 1.00 | 741 | 81.1% | 2 | 0 | NO |
| 2023-12-26 | bybit_ob/bybit/ARB-USDT/perp | 783,663 | 1.000 | 9.1 | 1 | 15.0 / 98.0 | 0.75 | 644 | 87.3% | 1 | 0 | yes |
| 2023-12-26 | bybit_ob/bybit/BTC-USDT/perp | 863,923 | 1.000 | 7.4 | 1 | 3.0 / 8.0 | 0.02 | 214 | 90.4% | 0 | 0 | yes |
| 2023-12-26 | bybit_ob/bybit/DOGE-USDT/perp | 688,021 | 1.000 | 9.1 | 1 | 15.0 / 96.0 | 1.08 | 566 | 87.4% | 1 | 0 | yes |
| 2023-12-26 | bybit_ob/bybit/ETH-USDT/perp | 862,576 | 1.000 | 7.0 | 1 | 4.0 / 17.0 | 0.04 | 234 | 91.2% | 0 | 0 | yes |
| 2023-12-26 | bybit_ob/bybit/SOL-USDT/perp | 860,915 | 1.000 | 7.9 | 1 | 6.0 / 54.0 | 0.09 | 872 | 73.8% | 1 | 0 | yes |
| 2023-12-26 | bybit_ob/bybit/TIA-USDT/perp | 845,207 | 1.000 | 6.8 | 1 | 8.0 / 72.0 | 0.80 | 866 | 82.7% | 1 | 0 | yes |
| 2023-12-26 | bybit_ob/bybit/WLD-USDT/perp | 699,986 | 1.000 | 7.4 | 1 | 16.0 / 98.0 | 2.67 | 1185 | 89.5% | 1 | 0 | yes |
| 2023-12-26 | bybit_ob/bybit/XRP-USDT/perp | 696,188 | 1.000 | 8.0 | 1 | 5.0 / 51.0 | 1.60 | 366 | 93.0% | 0 | 0 | yes |
| 2023-12-26 | bybit_ob/bybit/ZEC-USDT/perp | 268,581 | 0.951 | 11.6 | 1 | 38.0 / 100.0 | 3.31 | 596 | 92.8% | 1 | 0 | yes |
| 2023-12-27 | binance_bt/binance/AAVE-USDT/perp | 372,132 | 0.999 | 6.4 | 0 | 6.0 / 16.0 | 1.81 | 715 | no trade record | - | - | yes |
| 2023-12-27 | binance_bt/binance/ARB-USDT/perp | 763,174 | 1.000 | 3.5 | 0 | 6.0 / 16.0 | 1.34 | 758 | no trade record | - | - | yes |
| 2023-12-27 | binance_bt/binance/BTC-USDT/perp | 272,420 | 1.000 | 3.8 | 0 | 7.0 / 29.0 | 0.02 | 202 | no trade record | - | - | yes |
| 2023-12-27 | binance_bt/binance/DOGE-USDT/perp | 65,080 | 1.000 | 3.7 | 0 | 6.0 / 25.0 | 1.10 | 306 | no trade record | - | - | yes |
| 2023-12-27 | binance_bt/binance/ETH-USDT/perp | 388,796 | 1.000 | 3.7 | 0 | 6.0 / 25.0 | 0.04 | 286 | no trade record | - | - | yes |
| 2023-12-27 | binance_bt/binance/SOL-USDT/perp | 3,255,102 | 1.000 | 2.4 | 0 | 6.0 / 14.0 | 0.37 | 750 | no trade record | - | - | yes |
| 2023-12-27 | binance_bt/binance/TIA-USDT/perp | 2,648,297 | 1.000 | 4.4 | 0 | 5.0 / 11.0 | 1.03 | 687 | no trade record | - | - | yes |
| 2023-12-27 | binance_bt/binance/WLD-USDT/perp | 920,602 | 1.000 | 4.5 | 0 | 5.0 / 14.0 | 1.11 | 647 | no trade record | - | - | yes |
| 2023-12-27 | binance_bt/binance/XRP-USDT/perp | 35,029 | 1.000 | 3.9 | 0 | 6.0 / 30.0 | 1.61 | 296 | no trade record | - | - | yes |
| 2023-12-27 | binance_bt/binance/ZEC-USDT/perp | 42,586 | 0.988 | 11.3 | 0 | 6.0 / 18.0 | 3.34 | 469 | no trade record | - | - | yes |
| 2023-12-27 | bybit_ob/bybit/AAVE-USDT/perp | 653,131 | 1.000 | 3.7 | 0 | 18.0 / 98.0 | 0.93 | 714 | 79.1% | 1 | 0 | yes |
| 2023-12-27 | bybit_ob/bybit/ARB-USDT/perp | 793,380 | 1.000 | 1.2 | 0 | 12.0 / 98.0 | 0.73 | 761 | 84.2% | 1 | 0 | yes |
| 2023-12-27 | bybit_ob/bybit/BTC-USDT/perp | 864,000 | 1.000 | 0.9 | 0 | 3.0 / 8.0 | 0.02 | 201 | 91.5% | 1 | 0 | yes |
| 2023-12-27 | bybit_ob/bybit/DOGE-USDT/perp | 701,999 | 1.000 | 1.7 | 0 | 14.0 / 95.0 | 1.08 | 306 | 95.7% | 1 | 0 | yes |
| 2023-12-27 | bybit_ob/bybit/ETH-USDT/perp | 863,059 | 1.000 | 0.5 | 0 | 4.0 / 15.0 | 0.04 | 288 | 91.2% | 0 | 0 | yes |
| 2023-12-27 | bybit_ob/bybit/SOL-USDT/perp | 861,191 | 1.000 | 1.4 | 0 | 6.0 / 57.0 | 0.09 | 760 | 75.8% | 1 | 0 | yes |
| 2023-12-27 | bybit_ob/bybit/TIA-USDT/perp | 845,507 | 1.000 | 0.7 | 0 | 8.0 / 68.0 | 0.82 | 688 | 86.0% | 1 | 0 | yes |
| 2023-12-27 | bybit_ob/bybit/WLD-USDT/perp | 653,172 | 1.000 | 2.9 | 0 | 19.0 / 99.0 | 2.77 | 648 | 91.9% | 1 | 0 | yes |
| 2023-12-27 | bybit_ob/bybit/XRP-USDT/perp | 718,875 | 1.000 | 1.5 | 0 | 5.0 / 42.0 | 1.59 | 298 | 97.3% | 0 | 0 | yes |
| 2023-12-27 | bybit_ob/bybit/ZEC-USDT/perp | 308,433 | 0.979 | 7.0 | 0 | 39.0 / 100.0 | 3.32 | 443 | 86.2% | 1 | 0 | yes |
| 2023-12-28 | binance_bt/binance/AAVE-USDT/perp | 844,941 | 1.000 | 4.5 | 0 | 5.0 / 15.0 | 1.64 | 959 | no trade record | - | - | yes |
| 2023-12-28 | binance_bt/binance/ARB-USDT/perp | 991,853 | 1.000 | 4.4 | 0 | 6.0 / 17.0 | 1.26 | 799 | no trade record | - | - | yes |
| 2023-12-28 | binance_bt/binance/BTC-USDT/perp | 292,717 | 1.000 | 3.0 | 0 | 7.0 / 32.0 | 0.02 | 220 | no trade record | - | - | yes |
| 2023-12-28 | binance_bt/binance/DOGE-USDT/perp | 87,921 | 1.000 | 4.9 | 0 | 6.0 / 28.0 | 1.09 | 342 | no trade record | - | - | yes |
| 2023-12-28 | binance_bt/binance/ETH-USDT/perp | 525,925 | 1.000 | 4.4 | 0 | 7.0 / 28.0 | 0.04 | 362 | no trade record | - | - | yes |
| 2023-12-28 | binance_bt/binance/SOL-USDT/perp | 3,354,012 | 1.000 | 2.8 | 0 | 6.0 / 15.0 | 0.38 | 819 | no trade record | - | - | yes |
| 2023-12-28 | binance_bt/binance/TIA-USDT/perp | 2,430,715 | 1.000 | 4.5 | 0 | 5.0 / 12.0 | 0.99 | 654 | no trade record | - | - | yes |
| 2023-12-28 | binance_bt/binance/WLD-USDT/perp | 905,260 | 1.000 | 5.4 | 0 | 6.0 / 15.0 | 1.13 | 635 | no trade record | - | - | yes |
| 2023-12-28 | binance_bt/binance/XRP-USDT/perp | 69,901 | 1.000 | 4.4 | 0 | 6.0 / 24.0 | 1.59 | 402 | no trade record | - | - | yes |
| 2023-12-28 | binance_bt/binance/ZEC-USDT/perp | 58,770 | 0.985 | 11.4 | 0 | 6.0 / 20.0 | 3.14 | 503 | no trade record | - | - | yes |
| 2023-12-28 | bybit_ob/bybit/AAVE-USDT/perp | 743,905 | 1.000 | 9.8 | 1 | 13.0 / 98.0 | 0.84 | 960 | 81.4% | 1 | 0 | yes |
| 2023-12-28 | bybit_ob/bybit/ARB-USDT/perp | 823,262 | 1.000 | 9.2 | 1 | 10.0 / 94.0 | 0.66 | 806 | 85.7% | 1 | 0 | yes |
| 2023-12-28 | bybit_ob/bybit/BTC-USDT/perp | 863,897 | 1.000 | 9.7 | 1 | 3.0 / 8.0 | 0.02 | 218 | 91.9% | 1 | 0 | yes |
| 2023-12-28 | bybit_ob/bybit/DOGE-USDT/perp | 705,392 | 1.000 | 9.2 | 1 | 13.0 / 94.0 | 1.07 | 342 | 93.8% | 1 | 0 | yes |
| 2023-12-28 | bybit_ob/bybit/ETH-USDT/perp | 863,486 | 1.000 | 9.6 | 1 | 4.0 / 15.0 | 0.04 | 365 | 89.1% | 0 | 0 | yes |
| 2023-12-28 | bybit_ob/bybit/SOL-USDT/perp | 861,852 | 1.000 | 9.6 | 1 | 6.0 / 53.0 | 0.10 | 823 | 76.2% | 1 | 0 | yes |
| 2023-12-28 | bybit_ob/bybit/TIA-USDT/perp | 833,351 | 1.000 | 10.2 | 1 | 9.0 / 80.0 | 0.84 | 651 | 85.7% | 0 | 0 | yes |
| 2023-12-28 | bybit_ob/bybit/WLD-USDT/perp | 617,665 | 1.000 | 10.6 | 1 | 19.0 / 99.0 | 2.83 | 635 | 92.1% | 1 | 0 | yes |
| 2023-12-28 | bybit_ob/bybit/XRP-USDT/perp | 744,295 | 1.000 | 9.8 | 1 | 5.0 / 46.0 | 1.57 | 403 | 94.8% | 0 | 0 | yes |
| 2023-12-28 | bybit_ob/bybit/ZEC-USDT/perp | 316,872 | 0.976 | 9.3 | 1 | 37.0 / 100.0 | 3.12 | 476 | 86.1% | 1 | 0 | yes |
| 2023-12-29 | binance_bt/binance/AAVE-USDT/perp | 394,663 | 0.996 | 9.8 | 0 | 6.0 / 22.0 | 1.75 | 674 | no trade record | - | - | yes |
| 2023-12-29 | binance_bt/binance/ARB-USDT/perp | 644,713 | 1.000 | 4.4 | 0 | 6.0 / 22.0 | 1.34 | 633 | no trade record | - | - | yes |
| 2023-12-29 | binance_bt/binance/BTC-USDT/perp | 344,790 | 1.000 | 3.0 | 0 | 7.0 / 51.0 | 0.05 | 253 | no trade record | - | - | yes |
| 2023-12-29 | binance_bt/binance/DOGE-USDT/perp | 81,724 | 1.000 | 1.8 | 0 | 6.0 / 31.0 | 1.11 | 335 | no trade record | - | - | yes |
| 2023-12-29 | binance_bt/binance/ETH-USDT/perp | 442,689 | 1.000 | 2.3 | 0 | 7.0 / 31.0 | 0.08 | 307 | no trade record | - | - | yes |
| 2023-12-29 | binance_bt/binance/SOL-USDT/perp | 3,757,310 | 1.000 | 2.3 | 0 | 6.0 / 15.0 | 0.38 | 775 | no trade record | - | - | yes |
| 2023-12-29 | binance_bt/binance/TIA-USDT/perp | 2,451,277 | 1.000 | 6.2 | 0 | 5.0 / 12.0 | 1.22 | 738 | no trade record | - | - | yes |
| 2023-12-29 | binance_bt/binance/WLD-USDT/perp | 879,090 | 1.000 | 7.7 | 0 | 6.0 / 15.0 | 1.14 | 659 | no trade record | - | - | yes |
| 2023-12-29 | binance_bt/binance/XRP-USDT/perp | 41,721 | 1.000 | 4.3 | 0 | 6.0 / 33.0 | 1.61 | 291 | no trade record | - | - | yes |
| 2023-12-29 | binance_bt/binance/ZEC-USDT/perp | 49,331 | 0.990 | 10.5 | 0 | 6.0 / 21.0 | 3.51 | 629 | no trade record | - | - | yes |
| 2023-12-29 | bybit_ob/bybit/AAVE-USDT/perp | 640,668 | 1.000 | 3.1 | 0 | 18.0 / 98.0 | 0.89 | 674 | 79.8% | 2 | 0 | yes |
| 2023-12-29 | bybit_ob/bybit/ARB-USDT/perp | 795,348 | 1.000 | 1.2 | 0 | 13.0 / 98.0 | 0.68 | 639 | 85.3% | 1 | 0 | yes |
| 2023-12-29 | bybit_ob/bybit/BTC-USDT/perp | 863,988 | 1.000 | 1.1 | 0 | 3.0 / 8.0 | 0.02 | 252 | 89.6% | 0 | 0 | yes |
| 2023-12-29 | bybit_ob/bybit/DOGE-USDT/perp | 679,039 | 1.000 | 1.6 | 0 | 13.0 / 94.0 | 1.09 | 334 | 92.5% | 1 | 0 | yes |
| 2023-12-29 | bybit_ob/bybit/ETH-USDT/perp | 863,116 | 1.000 | 0.6 | 0 | 4.0 / 18.0 | 0.04 | 310 | 86.5% | 0 | 0 | yes |
| 2023-12-29 | bybit_ob/bybit/SOL-USDT/perp | 861,395 | 1.000 | 0.5 | 0 | 6.0 / 55.0 | 0.09 | 786 | 75.7% | 1 | 0 | yes |
| 2023-12-29 | bybit_ob/bybit/TIA-USDT/perp | 835,812 | 1.000 | 0.7 | 0 | 10.0 / 81.0 | 0.84 | 744 | 83.4% | 1 | 0 | yes |
| 2023-12-29 | bybit_ob/bybit/WLD-USDT/perp | 584,506 | 1.000 | 3.3 | 0 | 20.0 / 99.0 | 2.83 | 659 | 91.1% | 1 | 0 | yes |
| 2023-12-29 | bybit_ob/bybit/XRP-USDT/perp | 689,854 | 1.000 | 1.5 | 0 | 5.0 / 49.0 | 1.59 | 295 | 95.5% | 1 | 0 | yes |
| 2023-12-29 | bybit_ob/bybit/ZEC-USDT/perp | 314,412 | 0.977 | 10.1 | 0 | 38.0 / 100.0 | 3.46 | 605 | 91.2% | 0 | 0 | yes |
| 2023-12-30 | binance_bt/binance/AAVE-USDT/perp | 293,650 | 0.995 | 9.1 | 0 | 5.0 / 19.0 | 1.73 | 618 | no trade record | - | - | yes |
| 2023-12-30 | binance_bt/binance/ARB-USDT/perp | 293,993 | 1.000 | 4.3 | 0 | 6.0 / 20.0 | 1.32 | 496 | no trade record | - | - | yes |
| 2023-12-30 | binance_bt/binance/BTC-USDT/perp | 173,424 | 1.000 | 4.3 | 0 | 7.0 / 35.0 | 0.02 | 176 | no trade record | - | - | yes |
| 2023-12-30 | binance_bt/binance/DOGE-USDT/perp | 30,179 | 1.000 | 4.3 | 0 | 6.0 / 32.0 | 1.11 | 222 | no trade record | - | - | yes |
| 2023-12-30 | binance_bt/binance/ETH-USDT/perp | 197,154 | 1.000 | 3.9 | 0 | 7.0 / 30.0 | 0.04 | 211 | no trade record | - | - | yes |
| 2023-12-30 | binance_bt/binance/SOL-USDT/perp | 1,946,943 | 1.000 | 3.8 | 0 | 5.0 / 14.0 | 0.38 | 491 | no trade record | - | - | yes |
| 2023-12-30 | binance_bt/binance/TIA-USDT/perp | 1,666,332 | 1.000 | 7.3 | 0 | 5.0 / 12.0 | 0.99 | 512 | no trade record | - | - | yes |
| 2023-12-30 | binance_bt/binance/WLD-USDT/perp | 1,174,347 | 1.000 | 5.5 | 0 | 5.0 / 11.0 | 1.31 | 830 | no trade record | - | - | yes |
| 2023-12-30 | binance_bt/binance/XRP-USDT/perp | 14,637 | 1.000 | 4.3 | 0 | 6.0 / 34.6 | 1.61 | 189 | no trade record | - | - | yes |
| 2023-12-30 | binance_bt/binance/ZEC-USDT/perp | 17,311 | 0.966 | 13.9 | 0 | 6.0 / 20.0 | 3.51 | 373 | no trade record | - | - | yes |
| 2023-12-30 | bybit_ob/bybit/AAVE-USDT/perp | 587,677 | 1.000 | 3.8 | 0 | 19.0 / 99.0 | 0.89 | 619 | 76.7% | 2 | 0 | NO |
| 2023-12-30 | bybit_ob/bybit/ARB-USDT/perp | 753,665 | 1.000 | 1.6 | 0 | 17.0 / 98.0 | 0.68 | 497 | 81.9% | 1 | 0 | yes |
| 2023-12-30 | bybit_ob/bybit/BTC-USDT/perp | 863,972 | 1.000 | 1.1 | 0 | 3.0 / 8.0 | 0.02 | 175 | 93.6% | 0 | 0 | yes |
| 2023-12-30 | bybit_ob/bybit/DOGE-USDT/perp | 614,870 | 1.000 | 2.4 | 0 | 16.0 / 95.0 | 1.10 | 222 | 96.8% | 1 | 0 | yes |
| 2023-12-30 | bybit_ob/bybit/ETH-USDT/perp | 860,233 | 1.000 | 0.8 | 0 | 4.0 / 19.0 | 0.04 | 212 | 92.7% | 0 | 0 | yes |
| 2023-12-30 | bybit_ob/bybit/SOL-USDT/perp | 853,506 | 1.000 | 0.8 | 0 | 6.0 / 70.0 | 0.10 | 498 | 79.4% | 1 | 0 | yes |
| 2023-12-30 | bybit_ob/bybit/TIA-USDT/perp | 812,630 | 1.000 | 1.0 | 0 | 13.0 / 91.0 | 0.84 | 520 | 88.9% | 1 | 0 | yes |
| 2023-12-30 | bybit_ob/bybit/WLD-USDT/perp | 617,868 | 1.000 | 3.2 | 0 | 18.0 / 99.0 | 2.74 | 825 | 90.6% | 1 | 0 | yes |
| 2023-12-30 | bybit_ob/bybit/XRP-USDT/perp | 630,695 | 1.000 | 2.3 | 0 | 6.0 / 50.0 | 1.60 | 190 | 97.3% | 0 | 0 | yes |
| 2023-12-30 | bybit_ob/bybit/ZEC-USDT/perp | 196,757 | 0.916 | 9.3 | 0 | 44.0 / 101.0 | 3.50 | 360 | 94.6% | 1 | 0 | NO |
| 2023-12-31 | binance_bt/binance/AAVE-USDT/perp | 306,899 | 0.996 | 8.2 | 0 | 5.0 / 16.0 | 1.71 | 635 | no trade record | - | - | yes |
| 2023-12-31 | binance_bt/binance/ARB-USDT/perp | 556,523 | 1.000 | 4.1 | 0 | 6.0 / 16.0 | 1.23 | 632 | no trade record | - | - | yes |
| 2023-12-31 | binance_bt/binance/BTC-USDT/perp | 157,527 | 1.000 | 3.8 | 0 | 7.0 / 36.0 | 0.02 | 180 | no trade record | - | - | yes |
| 2023-12-31 | binance_bt/binance/DOGE-USDT/perp | 27,075 | 1.000 | 4.6 | 0 | 6.0 / 33.3 | 1.12 | 221 | no trade record | - | - | yes |
| 2023-12-31 | binance_bt/binance/ETH-USDT/perp | 177,824 | 1.000 | 4.1 | 0 | 7.0 / 31.0 | 0.04 | 207 | no trade record | - | - | yes |
| 2023-12-31 | binance_bt/binance/SOL-USDT/perp | 1,689,348 | 1.000 | 4.3 | 0 | 5.0 / 14.0 | 0.29 | 449 | no trade record | - | - | yes |
| 2023-12-31 | binance_bt/binance/TIA-USDT/perp | 1,521,890 | 1.000 | 6.1 | 0 | 5.0 / 11.0 | 0.97 | 567 | no trade record | - | - | yes |
| 2023-12-31 | binance_bt/binance/WLD-USDT/perp | 838,092 | 1.000 | 4.7 | 0 | 5.0 / 12.0 | 1.09 | 652 | no trade record | - | - | yes |
| 2023-12-31 | binance_bt/binance/XRP-USDT/perp | 13,565 | 1.000 | 4.6 | 0 | 6.0 / 35.4 | 1.63 | 196 | no trade record | - | - | yes |
| 2023-12-31 | binance_bt/binance/ZEC-USDT/perp | 22,960 | 0.963 | 14.8 | 0 | 6.0 / 18.0 | 3.77 | 594 | no trade record | - | - | yes |
| 2023-12-31 | bybit_ob/bybit/AAVE-USDT/perp | 564,626 | 1.000 | 3.8 | 0 | 19.0 / 99.0 | 0.88 | 637 | 78.2% | 4 | 0 | NO |
| 2023-12-31 | bybit_ob/bybit/ARB-USDT/perp | 780,553 | 1.000 | 1.4 | 0 | 15.0 / 98.0 | 0.65 | 638 | 79.2% | 1 | 0 | yes |
| 2023-12-31 | bybit_ob/bybit/BTC-USDT/perp | 863,996 | 1.000 | 1.1 | 0 | 3.0 / 7.0 | 0.02 | 178 | 92.9% | 0 | 0 | yes |
| 2023-12-31 | bybit_ob/bybit/DOGE-USDT/perp | 585,537 | 1.000 | 2.1 | 0 | 17.0 / 96.0 | 1.11 | 220 | 96.0% | 1 | 0 | yes |
| 2023-12-31 | bybit_ob/bybit/ETH-USDT/perp | 859,831 | 1.000 | 0.6 | 0 | 4.0 / 19.0 | 0.04 | 209 | 93.5% | 0 | 0 | yes |
| 2023-12-31 | bybit_ob/bybit/SOL-USDT/perp | 854,629 | 1.000 | 0.6 | 0 | 6.0 / 71.0 | 0.10 | 451 | 78.7% | 1 | 0 | yes |
| 2023-12-31 | bybit_ob/bybit/TIA-USDT/perp | 810,799 | 1.000 | 0.9 | 0 | 14.0 / 91.0 | 0.83 | 562 | 87.9% | 1 | 0 | yes |
| 2023-12-31 | bybit_ob/bybit/WLD-USDT/perp | 594,133 | 1.000 | 3.4 | 0 | 22.0 / 99.0 | 2.68 | 648 | 89.7% | 1 | 0 | yes |
| 2023-12-31 | bybit_ob/bybit/XRP-USDT/perp | 627,485 | 1.000 | 1.8 | 0 | 6.0 / 59.0 | 1.61 | 193 | 91.6% | 0 | 0 | yes |
| 2023-12-31 | bybit_ob/bybit/ZEC-USDT/perp | 175,825 | 0.891 | 12.1 | 0 | 44.0 / 101.0 | 3.51 | 590 | 85.9% | 0 | 0 | NO |
| 2024-01-01 | binance_bt/binance/BTC-USDT/perp | 206,882 | 1.000 | 3.8 | 0 | 7.0 / 31.0 | 0.02 | 177 | no trade record | - | - | yes |
| 2024-01-01 | bybit_ob/bybit/BTC-USDT/perp | 863,995 | 1.000 | 1.1 | 0 | 3.0 / 8.0 | 0.02 | 176 | 91.0% | 1 | 0 | yes |
| 2024-01-02 | binance_bt/binance/BTC-USDT/perp | 534,249 | 1.000 | 3.1 | 0 | 7.0 / 71.0 | 0.04 | 312 | no trade record | - | - | yes |
| 2024-01-02 | bybit_ob/bybit/BTC-USDT/perp | 864,001 | 1.000 | 1.1 | 0 | 3.0 / 8.0 | 0.02 | 311 | 89.2% | 0 | 0 | yes |
| 2024-01-03 | binance_bt/binance/BTC-USDT/perp | 822,808 | 0.991 | 698.0 | 0 | 7.0 / 42.0 | 0.07 | 513 | no trade record | - | - | yes |
| 2024-01-03 | bybit_ob/bybit/BTC-USDT/perp | 863,996 | 1.000 | 1.1 | 0 | 3.0 / 8.0 | 0.02 | 664 | 77.2% | 1 | 0 | yes |
| 2024-01-04 | binance_bt/binance/BTC-USDT/perp | 479,999 | 1.000 | 3.4 | 0 | 7.0 / 56.0 | 0.05 | 306 | no trade record | - | - | yes |
| 2024-01-04 | bybit_ob/bybit/BTC-USDT/perp | 863,990 | 1.000 | 1.1 | 0 | 3.0 / 8.0 | 0.02 | 307 | 87.8% | 0 | 0 | yes |
| 2024-01-05 | binance_bt/binance/BTC-USDT/perp | 587,037 | 1.000 | 3.6 | 0 | 7.0 / 57.0 | 0.05 | 463 | no trade record | - | - | yes |
| 2024-01-05 | bybit_ob/bybit/BTC-USDT/perp | 863,880 | 1.000 | 1.1 | 0 | 3.0 / 8.0 | 0.02 | 472 | 81.6% | 1 | 0 | yes |
| 2024-01-06 | binance_bt/binance/BTC-USDT/perp | 181,377 | 1.000 | 3.2 | 0 | 7.0 / 35.0 | 0.02 | 160 | no trade record | - | - | yes |
| 2024-01-06 | bybit_ob/bybit/BTC-USDT/perp | 863,992 | 1.000 | 1.1 | 0 | 3.0 / 8.0 | 0.02 | 160 | 92.9% | 1 | 0 | yes |
| 2024-01-07 | binance_bt/binance/BTC-USDT/perp | 223,384 | 1.000 | 1.5 | 0 | 7.0 / 45.0 | 0.02 | 182 | no trade record | - | - | yes |
| 2024-01-07 | bybit_ob/bybit/BTC-USDT/perp | 863,998 | 1.000 | 1.1 | 0 | 3.0 / 8.0 | 0.02 | 181 | 92.6% | 1 | 0 | yes |
| 2024-01-08 | binance_bt/binance/BTC-USDT/perp | 689,757 | 1.000 | 1.8 | 0 | 7.0 / 254.0 | 0.05 | 358 | no trade record | - | - | yes |
| 2024-01-08 | bybit_ob/bybit/BTC-USDT/perp | 863,979 | 1.000 | 1.1 | 0 | 3.0 / 8.0 | 0.02 | 359 | 84.0% | 1 | 0 | yes |
| 2024-01-09 | binance_bt/binance/BTC-USDT/perp | 966,507 | 1.000 | 2.1 | 0 | 8.0 / 27318.0 | 0.11 | 593 | no trade record | - | - | yes |
| 2024-01-09 | bybit_ob/bybit/BTC-USDT/perp | 863,872 | 1.000 | 5.7 | 0 | 3.0 / 8.0 | 0.02 | 586 | 78.1% | 1 | 0 | yes |
| 2024-01-10 | binance_bt/binance/BTC-USDT/perp | 1,436,791 | 1.000 | 2.3 | 0 | 7.0 / 108.0 | 0.11 | 514 | no trade record | - | - | yes |
| 2024-01-10 | bybit_ob/bybit/BTC-USDT/perp | 863,994 | 1.000 | 1.1 | 0 | 3.0 / 9.0 | 0.02 | 522 | 79.4% | 1 | 0 | yes |
| 2024-01-11 | binance_bt/binance/BTC-USDT/perp | 1,208,320 | 1.000 | 3.5 | 0 | 7.0 / 151.0 | 0.06 | 402 | no trade record | - | - | yes |
| 2024-01-11 | bybit_ob/bybit/BTC-USDT/perp | 863,857 | 1.000 | 12.4 | 1 | 3.0 / 9.0 | 0.02 | 403 | 83.8% | 1 | 0 | yes |
| 2024-01-12 | binance_bt/binance/BTC-USDT/perp | 1,063,541 | 1.000 | 1.7 | 0 | 7.0 / 270.0 | 0.06 | 475 | no trade record | - | - | yes |
| 2024-01-12 | bybit_ob/bybit/BTC-USDT/perp | 863,980 | 1.000 | 1.0 | 0 | 3.0 / 9.0 | 0.02 | 471 | 83.5% | 0 | 0 | yes |
| 2024-01-13 | binance_bt/binance/BTC-USDT/perp | 334,207 | 1.000 | 2.5 | 0 | 7.0 / 39.0 | 0.05 | 253 | no trade record | - | - | yes |
| 2024-01-13 | bybit_ob/bybit/BTC-USDT/perp | 863,982 | 1.000 | 1.0 | 0 | 3.0 / 9.0 | 0.02 | 251 | 92.6% | 1 | 0 | yes |
| 2024-01-14 | binance_bt/binance/BTC-USDT/perp | 274,853 | 1.000 | 3.2 | 0 | 7.0 / 40.0 | 0.02 | 236 | no trade record | - | - | yes |
| 2024-01-14 | bybit_ob/bybit/BTC-USDT/perp | 863,956 | 1.000 | 1.0 | 0 | 3.0 / 8.0 | 0.02 | 246 | 89.0% | 1 | 0 | yes |
| 2024-01-15 | binance_bt/binance/BTC-USDT/perp | 383,783 | 1.000 | 3.9 | 0 | 7.0 / 41.0 | 0.05 | 233 | no trade record | - | - | yes |
| 2024-01-15 | bybit_ob/bybit/BTC-USDT/perp | 863,984 | 1.000 | 1.0 | 0 | 3.0 / 9.0 | 0.02 | 234 | 87.9% | 1 | 0 | yes |
| 2024-01-16 | binance_bt/binance/BTC-USDT/perp | 424,296 | 1.000 | 2.9 | 0 | 7.0 / 35.0 | 0.05 | 253 | no trade record | - | - | yes |
| 2024-01-16 | bybit_ob/bybit/BTC-USDT/perp | 863,982 | 1.000 | 1.0 | 0 | 3.0 / 9.0 | 0.02 | 255 | 88.1% | 1 | 0 | yes |
| 2024-01-17 | binance_bt/binance/BTC-USDT/perp | 314,153 | 1.000 | 3.0 | 0 | 7.0 / 41.0 | 0.02 | 217 | no trade record | - | - | yes |
| 2024-01-17 | bybit_ob/bybit/BTC-USDT/perp | 863,975 | 1.000 | 1.0 | 0 | 3.0 / 8.0 | 0.02 | 219 | 91.3% | 1 | 0 | yes |
| 2024-01-18 | binance_bt/binance/BTC-USDT/perp | 478,395 | 1.000 | 4.2 | 0 | 7.0 / 62.0 | 0.05 | 259 | no trade record | - | - | yes |
| 2024-01-18 | bybit_ob/bybit/BTC-USDT/perp | 863,967 | 1.000 | 1.0 | 0 | 3.0 / 9.0 | 0.02 | 261 | 87.4% | 1 | 0 | yes |
| 2024-01-19 | binance_bt/binance/BTC-USDT/perp | 495,091 | 1.000 | 2.3 | 0 | 7.0 / 33.0 | 0.05 | 276 | no trade record | - | - | yes |
| 2024-01-19 | bybit_ob/bybit/BTC-USDT/perp | 863,971 | 1.000 | 1.0 | 0 | 3.0 / 9.0 | 0.02 | 277 | 87.7% | 1 | 0 | yes |
| 2024-01-20 | binance_bt/binance/BTC-USDT/perp | 118,470 | 1.000 | 3.5 | 0 | 7.0 / 37.0 | 0.02 | 129 | no trade record | - | - | yes |
| 2024-01-20 | bybit_ob/bybit/BTC-USDT/perp | 863,821 | 1.000 | 1.0 | 0 | 3.0 / 9.0 | 0.02 | 129 | 94.0% | 1 | 0 | yes |
| 2024-01-21 | binance_bt/binance/BTC-USDT/perp | 68,360 | 1.000 | 4.0 | 0 | 7.0 / 31.0 | 0.02 | 100 | no trade record | - | - | yes |
| 2024-01-21 | bybit_ob/bybit/BTC-USDT/perp | 863,689 | 1.000 | 1.0 | 0 | 3.0 / 10.0 | 0.02 | 100 | 94.5% | 1 | 0 | yes |
| 2024-01-22 | binance_bt/binance/BTC-USDT/perp | 612,447 | 1.000 | 3.7 | 0 | 7.0 / 96.0 | 0.05 | 335 | no trade record | - | - | yes |
| 2024-01-22 | bybit_ob/bybit/BTC-USDT/perp | 863,968 | 1.000 | 1.0 | 0 | 3.0 / 9.0 | 0.02 | 337 | 86.0% | 1 | 0 | yes |
| 2024-01-23 | binance_bt/binance/BTC-USDT/perp | 513,411 | 1.000 | 2.4 | 0 | 7.0 / 34.0 | 0.05 | 320 | no trade record | - | - | yes |
| 2024-01-23 | bybit_ob/bybit/BTC-USDT/perp | 863,983 | 1.000 | 1.0 | 0 | 3.0 / 9.0 | 0.03 | 322 | 88.1% | 1 | 0 | yes |
| 2024-01-24 | binance_bt/binance/BTC-USDT/perp | 338,997 | 1.000 | 3.5 | 0 | 7.0 / 33.0 | 0.03 | 236 | no trade record | - | - | yes |
| 2024-01-24 | bybit_ob/bybit/BTC-USDT/perp | 863,898 | 1.000 | 1.0 | 0 | 3.0 / 10.0 | 0.03 | 237 | 91.8% | 1 | 0 | yes |
| 2024-01-25 | binance_bt/binance/BTC-USDT/perp | 235,059 | 1.000 | 2.6 | 0 | 7.0 / 32.0 | 0.03 | 197 | no trade record | - | - | yes |
| 2024-01-25 | bybit_ob/bybit/BTC-USDT/perp | 863,968 | 1.000 | 1.0 | 0 | 3.0 / 10.0 | 0.03 | 198 | 93.0% | 0 | 0 | yes |
| 2024-01-26 | binance_bt/binance/BTC-USDT/perp | 361,994 | 1.000 | 2.6 | 0 | 7.0 / 76.0 | 0.05 | 255 | no trade record | - | - | yes |
| 2024-01-26 | bybit_ob/bybit/BTC-USDT/perp | 863,959 | 1.000 | 1.0 | 0 | 3.0 / 11.0 | 0.02 | 255 | 90.0% | 1 | 0 | yes |
| 2024-01-27 | binance_bt/binance/BTC-USDT/perp | 99,818 | 1.000 | 1.3 | 0 | 7.0 / 38.0 | 0.02 | 121 | no trade record | - | - | yes |
| 2024-01-27 | bybit_ob/bybit/BTC-USDT/perp | 863,902 | 1.000 | 1.0 | 0 | 3.0 / 9.0 | 0.02 | 123 | 93.5% | 1 | 0 | yes |
| 2024-01-28 | binance_bt/binance/BTC-USDT/perp | 199,245 | 1.000 | 1.5 | 0 | 7.0 / 49.0 | 0.02 | 177 | no trade record | - | - | yes |
| 2024-01-28 | bybit_ob/bybit/BTC-USDT/perp | 863,941 | 1.000 | 1.0 | 0 | 3.0 / 8.0 | 0.02 | 178 | 91.8% | 1 | 0 | yes |
| 2024-01-29 | binance_bt/binance/BTC-USDT/perp | 276,865 | 1.000 | 2.2 | 0 | 7.0 / 45.0 | 0.02 | 206 | no trade record | - | - | yes |
| 2024-01-29 | bybit_ob/bybit/BTC-USDT/perp | 863,965 | 1.000 | 1.0 | 0 | 3.0 / 9.0 | 0.02 | 208 | 90.3% | 0 | 0 | yes |
| 2024-01-30 | binance_bt/binance/BTC-USDT/perp | 282,049 | 1.000 | 2.0 | 0 | 7.0 / 45.0 | 0.02 | 226 | no trade record | - | - | yes |
| 2024-01-30 | bybit_ob/bybit/BTC-USDT/perp | 863,947 | 1.000 | 1.0 | 0 | 3.0 / 9.0 | 0.02 | 227 | 89.1% | 1 | 0 | yes |
| 2024-01-31 | binance_bt/binance/BTC-USDT/perp | 386,013 | 1.000 | 2.4 | 0 | 7.0 / 32.0 | 0.02 | 256 | no trade record | - | - | yes |
| 2024-01-31 | bybit_ob/bybit/BTC-USDT/perp | 863,939 | 1.000 | 1.0 | 0 | 3.0 / 10.0 | 0.02 | 259 | 89.0% | 1 | 0 | yes |
| 2026-09-07 | bybit_ob/bybit/BTC-USDT/perp | 862,255 | 1.000 | 0.6 | 0 | 3.0 / 14.0 | 0.01 | 132 | 92.0% | 1 | 0 | yes |
| 2026-09-07 | bybit_ob/bybit/BTC-USDT/spot | 764,879 | 1.000 | 2.8 | 0 | 5.0 / 36.0 | 0.01 | 127 | 98.7% | 0 | 0 | yes |
| 2026-09-07 | bybit_ob/bybit/ETH-USDT/perp | 838,360 | 1.000 | 1.7 | 0 | 4.0 / 17.0 | 0.04 | 186 | 90.6% | 0 | 0 | yes |
| 2026-09-07 | bybit_ob/bybit/ETH-USDT/spot | 629,760 | 1.000 | 3.2 | 0 | 7.0 / 47.0 | 0.04 | 182 | 95.4% | 1 | 0 | yes |
| 2026-09-08 | bybit_ob/bybit/BTC-USDT/perp | 862,728 | 1.000 | 0.6 | 0 | 3.0 / 10.0 | 0.01 | 159 | 92.5% | 1 | 0 | yes |
| 2026-09-08 | bybit_ob/bybit/BTC-USDT/spot | 796,174 | 1.000 | 2.8 | 0 | 4.0 / 35.0 | 0.01 | 156 | 98.2% | 0 | 0 | yes |
| 2026-09-08 | bybit_ob/bybit/ETH-USDT/perp | 846,887 | 1.000 | 1.7 | 0 | 4.0 / 14.0 | 0.04 | 212 | 91.4% | 0 | 0 | yes |
| 2026-09-08 | bybit_ob/bybit/ETH-USDT/spot | 677,863 | 1.000 | 3.0 | 0 | 7.0 / 48.0 | 0.04 | 209 | 94.9% | 0 | 0 | yes |
| 2026-09-09 | bybit_ob/bybit/BTC-USDT/perp | 862,899 | 1.000 | 0.1 | 0 | 3.0 / 10.0 | 0.01 | 206 | 91.8% | 0 | 0 | yes |
| 2026-09-09 | bybit_ob/bybit/BTC-USDT/spot | 775,703 | 1.000 | 2.8 | 0 | 5.0 / 36.0 | 0.01 | 200 | 98.3% | 0 | 0 | yes |
| 2026-09-09 | bybit_ob/bybit/ETH-USDT/perp | 849,116 | 1.000 | 1.7 | 0 | 3.0 / 12.0 | 0.04 | 249 | 91.2% | 1 | 0 | yes |
| 2026-09-09 | bybit_ob/bybit/ETH-USDT/spot | 664,725 | 1.000 | 3.0 | 0 | 7.0 / 47.0 | 0.04 | 246 | 94.2% | 2 | 0 | yes |
| 2026-09-10 | bybit_ob/bybit/BTC-USDT/perp | 862,836 | 1.000 | 0.6 | 0 | 3.0 / 10.0 | 0.01 | 179 | 91.5% | 0 | 0 | yes |
| 2026-09-10 | bybit_ob/bybit/BTC-USDT/spot | 779,114 | 1.000 | 2.8 | 0 | 5.0 / 35.0 | 0.01 | 174 | 98.4% | 0 | 0 | yes |
| 2026-09-10 | bybit_ob/bybit/ETH-USDT/perp | 848,422 | 1.000 | 1.7 | 0 | 3.0 / 13.0 | 0.04 | 221 | 90.2% | 0 | 0 | yes |
| 2026-09-10 | bybit_ob/bybit/ETH-USDT/spot | 693,725 | 1.000 | 3.0 | 0 | 7.0 / 47.0 | 0.04 | 218 | 93.4% | 1 | 0 | yes |
| 2026-09-11 | bybit_ob/bybit/BTC-USDT/perp | 862,931 | 1.000 | 0.6 | 0 | 3.0 / 10.0 | 0.01 | 264 | 90.0% | 0 | 0 | yes |
| 2026-09-11 | bybit_ob/bybit/BTC-USDT/spot | 765,779 | 1.000 | 2.8 | 0 | 5.0 / 35.0 | 0.01 | 258 | 96.8% | 0 | 0 | yes |
| 2026-09-11 | bybit_ob/bybit/ETH-USDT/perp | 853,349 | 1.000 | 1.7 | 0 | 3.0 / 12.0 | 0.04 | 430 | 86.0% | 1 | 0 | yes |
| 2026-09-11 | bybit_ob/bybit/ETH-USDT/spot | 716,381 | 1.000 | 3.0 | 0 | 6.0 / 45.0 | 0.04 | 424 | 88.3% | 1 | 0 | yes |
| 2026-09-12 | bybit_ob/bybit/BTC-USDT/perp | 858,111 | 1.000 | 0.6 | 0 | 3.0 / 10.0 | 0.01 | 68 | 94.6% | 1 | 0 | yes |
| 2026-09-12 | bybit_ob/bybit/BTC-USDT/spot | 635,522 | 1.000 | 2.8 | 0 | 7.0 / 40.0 | 0.01 | 65 | 97.8% | 0 | 0 | yes |
| 2026-09-12 | bybit_ob/bybit/ETH-USDT/perp | 823,437 | 1.000 | 1.7 | 0 | 4.0 / 10.0 | 0.04 | 122 | 92.6% | 1 | 0 | yes |
| 2026-09-12 | bybit_ob/bybit/ETH-USDT/spot | 669,612 | 1.000 | 3.0 | 0 | 10.0 / 48.0 | 0.04 | 122 | 94.1% | 1 | 0 | yes |
| 2026-09-13 | bybit_ob/bybit/BTC-USDT/perp | 860,064 | 1.000 | 0.5 | 0 | 3.0 / 10.0 | 0.01 | 97 | 92.8% | 2 | 0 | yes |
| 2026-09-13 | bybit_ob/bybit/BTC-USDT/spot | 692,091 | 1.000 | 2.8 | 0 | 7.0 / 38.0 | 0.01 | 94 | 98.3% | 0 | 0 | yes |
| 2026-09-13 | bybit_ob/bybit/ETH-USDT/perp | 829,786 | 1.000 | 1.7 | 0 | 4.0 / 11.0 | 0.04 | 173 | 90.4% | 1 | 0 | yes |
| 2026-09-13 | bybit_ob/bybit/ETH-USDT/spot | 698,700 | 1.000 | 3.0 | 0 | 9.0 / 48.0 | 0.04 | 169 | 93.4% | 0 | 0 | yes |
| 2026-09-14 | bybit_ob/bybit/BTC-USDT/perp | 863,431 | 1.000 | 0.1 | 0 | 3.0 / 10.0 | 0.01 | 199 | 92.7% | 0 | 0 | yes |
| 2026-09-14 | bybit_ob/bybit/BTC-USDT/spot | 803,967 | 1.000 | 2.8 | 0 | 4.0 / 31.0 | 0.01 | 195 | 97.7% | 0 | 0 | yes |
| 2026-09-14 | bybit_ob/bybit/ETH-USDT/perp | 857,362 | 1.000 | 1.7 | 0 | 3.0 / 12.0 | 0.04 | 291 | 89.9% | 0 | 0 | yes |
| 2026-09-14 | bybit_ob/bybit/ETH-USDT/spot | 754,350 | 1.000 | 3.0 | 0 | 5.0 / 45.5 | 0.04 | 285 | 91.5% | 1 | 0 | yes |
| 2026-09-15 | bybit_ob/bybit/BTC-USDT/perp | 863,505 | 1.000 | 0.1 | 0 | 3.0 / 10.0 | 0.01 | 244 | 91.3% | 0 | 0 | yes |
| 2026-09-15 | bybit_ob/bybit/BTC-USDT/spot | 788,465 | 1.000 | 2.8 | 0 | 4.0 / 32.0 | 0.01 | 240 | 96.8% | 0 | 0 | yes |
| 2026-09-15 | bybit_ob/bybit/ETH-USDT/perp | 858,317 | 1.000 | 1.7 | 0 | 3.0 / 12.0 | 0.04 | 330 | 88.8% | 0 | 0 | yes |
| 2026-09-15 | bybit_ob/bybit/ETH-USDT/spot | 698,054 | 1.000 | 3.0 | 0 | 5.0 / 46.0 | 0.04 | 326 | 90.3% | 1 | 0 | yes |
| 2026-09-16 | bybit_ob/bybit/BTC-USDT/perp | 863,122 | 1.000 | 0.1 | 0 | 3.0 / 10.0 | 0.01 | 242 | 92.2% | 0 | 0 | yes |
| 2026-09-16 | bybit_ob/bybit/BTC-USDT/spot | 794,415 | 1.000 | 2.8 | 0 | 4.0 / 31.0 | 0.01 | 239 | 97.8% | 0 | 0 | yes |
| 2026-09-16 | bybit_ob/bybit/ETH-USDT/perp | 855,609 | 1.000 | 1.7 | 0 | 3.0 / 12.0 | 0.04 | 324 | 89.1% | 1 | 0 | yes |
| 2026-09-16 | bybit_ob/bybit/ETH-USDT/spot | 669,487 | 1.000 | 3.0 | 0 | 6.0 / 46.0 | 0.04 | 319 | 92.3% | 1 | 0 | yes |
| 2026-09-17 | bybit_ob/bybit/BTC-USDT/perp | 862,739 | 1.000 | 0.1 | 0 | 3.0 / 10.0 | 0.01 | 175 | 94.5% | 0 | 0 | yes |
| 2026-09-17 | bybit_ob/bybit/BTC-USDT/spot | 783,805 | 1.000 | 2.8 | 0 | 5.0 / 33.0 | 0.01 | 169 | 98.4% | 0 | 0 | yes |
| 2026-09-17 | bybit_ob/bybit/ETH-USDT/perp | 856,225 | 1.000 | 1.7 | 0 | 3.0 / 13.0 | 0.04 | 242 | 91.8% | 0 | 0 | yes |
| 2026-09-17 | bybit_ob/bybit/ETH-USDT/spot | 686,908 | 1.000 | 3.0 | 0 | 6.0 / 45.0 | 0.04 | 237 | 93.4% | 0 | 0 | yes |
| 2026-09-18 | bybit_ob/bybit/BTC-USDT/perp | 863,508 | 1.000 | 0.1 | 0 | 3.0 / 9.0 | 0.01 | 231 | 92.6% | 0 | 0 | yes |
| 2026-09-18 | bybit_ob/bybit/BTC-USDT/spot | 810,317 | 1.000 | 2.9 | 0 | 4.0 / 30.0 | 0.01 | 226 | 97.7% | 0 | 0 | yes |
| 2026-09-18 | bybit_ob/bybit/ETH-USDT/perp | 861,200 | 1.000 | 1.7 | 0 | 3.0 / 11.0 | 0.04 | 327 | 89.0% | 0 | 0 | yes |
| 2026-09-18 | bybit_ob/bybit/ETH-USDT/spot | 751,337 | 1.000 | 3.0 | 0 | 5.0 / 45.0 | 0.04 | 319 | 91.3% | 1 | 0 | yes |
| 2026-09-19 | bybit_ob/bybit/BTC-USDT/perp | 862,773 | 1.000 | 0.5 | 0 | 3.0 / 9.0 | 0.01 | 125 | 93.4% | 0 | 0 | yes |
| 2026-09-19 | bybit_ob/bybit/BTC-USDT/spot | 772,738 | 1.000 | 2.9 | 0 | 5.0 / 33.0 | 0.01 | 119 | 98.2% | 0 | 0 | yes |
| 2026-09-19 | bybit_ob/bybit/ETH-USDT/perp | 851,252 | 1.000 | 1.7 | 0 | 3.0 / 11.0 | 0.04 | 201 | 92.8% | 0 | 0 | yes |
| 2026-09-19 | bybit_ob/bybit/ETH-USDT/spot | 635,691 | 1.000 | 3.0 | 0 | 6.0 / 47.0 | 0.04 | 197 | 94.9% | 0 | 0 | yes |
| 2026-09-20 | bybit_ob/bybit/BTC-USDT/perp | 862,669 | 1.000 | 0.1 | 0 | 3.0 / 9.0 | 0.01 | 158 | 93.8% | 0 | 0 | yes |
| 2026-09-20 | bybit_ob/bybit/BTC-USDT/spot | 786,292 | 1.000 | 2.9 | 0 | 5.0 / 32.0 | 0.01 | 152 | 98.3% | 0 | 0 | yes |
| 2026-09-20 | bybit_ob/bybit/ETH-USDT/perp | 853,116 | 1.000 | 1.7 | 0 | 3.0 / 11.0 | 0.04 | 253 | 91.7% | 0 | 0 | yes |
| 2026-09-20 | bybit_ob/bybit/ETH-USDT/spot | 663,685 | 1.000 | 3.0 | 0 | 7.0 / 48.0 | 0.04 | 247 | 93.4% | 1 | 0 | yes |
| 2026-09-21 | bybit_ob/bybit/BTC-USDT/perp | 863,808 | 1.000 | 0.1 | 0 | 2.0 / 11.0 | 0.01 | 281 | 91.6% | 0 | 0 | yes |
| 2026-09-21 | bybit_ob/bybit/BTC-USDT/spot | 829,316 | 1.000 | 2.9 | 0 | 4.0 / 27.0 | 0.01 | 275 | 96.5% | 0 | 0 | yes |
| 2026-09-21 | bybit_ob/bybit/ETH-USDT/perp | 862,141 | 1.000 | 1.7 | 0 | 3.0 / 15.0 | 0.04 | 365 | 90.6% | 0 | 0 | yes |
| 2026-09-21 | bybit_ob/bybit/ETH-USDT/spot | 769,771 | 1.000 | 3.0 | 0 | 5.0 / 44.0 | 0.04 | 358 | 91.4% | 0 | 0 | yes |
| 2026-09-22 | bybit_ob/bybit/BTC-USDT/perp | 863,769 | 1.000 | 0.1 | 0 | 3.0 / 13.0 | 0.01 | 201 | 94.3% | 0 | 0 | yes |
| 2026-09-22 | bybit_ob/bybit/BTC-USDT/spot | 818,476 | 1.000 | 2.9 | 0 | 3.0 / 27.0 | 0.01 | 196 | 98.7% | 0 | 0 | yes |
| 2026-09-22 | bybit_ob/bybit/ETH-USDT/perp | 860,367 | 1.000 | 1.7 | 0 | 3.0 / 16.0 | 0.04 | 262 | 93.9% | 1 | 0 | yes |
| 2026-09-22 | bybit_ob/bybit/ETH-USDT/spot | 732,641 | 1.000 | 3.0 | 0 | 5.0 / 45.0 | 0.04 | 258 | 95.2% | 0 | 0 | yes |
| 2026-09-23 | bybit_ob/bybit/BTC-USDT/perp | 863,707 | 1.000 | 0.1 | 0 | 3.0 / 13.0 | 0.01 | 197 | 91.8% | 0 | 0 | yes |
| 2026-09-23 | bybit_ob/bybit/BTC-USDT/spot | 818,719 | 1.000 | 1.4 | 0 | 4.0 / 31.0 | 0.01 | 193 | 98.6% | 0 | 0 | yes |
| 2026-09-23 | bybit_ob/bybit/ETH-USDT/perp | 858,204 | 1.000 | 1.7 | 0 | 3.0 / 16.0 | 0.04 | 257 | 91.8% | 1 | 0 | yes |
| 2026-09-23 | bybit_ob/bybit/ETH-USDT/spot | 735,139 | 1.000 | 1.9 | 0 | 5.0 / 44.0 | 0.04 | 254 | 94.3% | 0 | 0 | yes |
| 2026-09-24 | bybit_ob/bybit/BTC-USDT/perp | 863,748 | 1.000 | 0.1 | 0 | 3.0 / 13.0 | 0.01 | 215 | 92.3% | 1 | 0 | yes |
| 2026-09-24 | bybit_ob/bybit/BTC-USDT/spot | 810,884 | 1.000 | 1.5 | 0 | 4.0 / 32.0 | 0.01 | 210 | 98.8% | 0 | 0 | yes |
| 2026-09-24 | bybit_ob/bybit/ETH-USDT/perp | 857,917 | 1.000 | 1.7 | 0 | 3.0 / 16.0 | 0.04 | 254 | 91.9% | 0 | 0 | yes |
| 2026-09-24 | bybit_ob/bybit/ETH-USDT/spot | 731,323 | 1.000 | 2.1 | 0 | 6.0 / 45.0 | 0.04 | 250 | 94.6% | 1 | 0 | yes |
| 2026-09-25 | bybit_ob/bybit/BTC-USDT/perp | 863,488 | 1.000 | 0.1 | 0 | 3.0 / 13.0 | 0.01 | 194 | 92.7% | 0 | 0 | yes |
| 2026-09-25 | bybit_ob/bybit/BTC-USDT/spot | 774,968 | 1.000 | 1.5 | 0 | 4.0 / 32.0 | 0.01 | 190 | 98.6% | 0 | 0 | yes |
| 2026-09-25 | bybit_ob/bybit/ETH-USDT/perp | 854,983 | 1.000 | 1.7 | 0 | 3.0 / 16.0 | 0.04 | 248 | 92.1% | 0 | 0 | yes |
| 2026-09-25 | bybit_ob/bybit/ETH-USDT/spot | 706,876 | 1.000 | 2.7 | 0 | 5.0 / 45.0 | 0.04 | 243 | 95.8% | 0 | 0 | yes |
| 2026-09-26 | bybit_ob/bybit/BTC-USDT/perp | 861,975 | 1.000 | 0.6 | 0 | 3.0 / 15.0 | 0.01 | 82 | 92.8% | 0 | 0 | yes |
| 2026-09-26 | bybit_ob/bybit/BTC-USDT/spot | 693,567 | 1.000 | 2.6 | 0 | 5.0 / 37.0 | 0.01 | 74 | 98.9% | 0 | 0 | yes |
| 2026-09-26 | bybit_ob/bybit/ETH-USDT/perp | 826,734 | 1.000 | 1.7 | 0 | 5.0 / 17.0 | 0.04 | 116 | 93.6% | 1 | 0 | yes |
| 2026-09-26 | bybit_ob/bybit/ETH-USDT/spot | 676,872 | 1.000 | 2.6 | 0 | 9.0 / 49.0 | 0.04 | 110 | 96.6% | 1 | 0 | yes |
| 2026-09-27 | bybit_ob/bybit/BTC-USDT/perp | 861,925 | 1.000 | 0.6 | 0 | 3.0 / 14.0 | 0.01 | 109 | 94.2% | 1 | 0 | yes |
| 2026-09-27 | bybit_ob/bybit/BTC-USDT/spot | 709,262 | 1.000 | 2.1 | 0 | 5.0 / 38.0 | 0.01 | 104 | 98.9% | 0 | 0 | yes |
| 2026-09-27 | bybit_ob/bybit/ETH-USDT/perp | 839,685 | 1.000 | 1.7 | 0 | 4.0 / 16.0 | 0.04 | 141 | 93.3% | 0 | 0 | yes |
| 2026-09-27 | bybit_ob/bybit/ETH-USDT/spot | 708,324 | 1.000 | 3.2 | 0 | 8.0 / 48.0 | 0.04 | 138 | 96.7% | 1 | 0 | yes |
| 2026-09-28 | bybit_ob/bybit/BTC-USDT/perp | 863,452 | 1.000 | 0.6 | 0 | 3.0 / 13.0 | 0.01 | 216 | 94.0% | 0 | 0 | yes |
| 2026-09-28 | bybit_ob/bybit/BTC-USDT/spot | 809,289 | 1.000 | 1.4 | 0 | 4.0 / 31.0 | 0.01 | 211 | 99.2% | 0 | 0 | yes |
| 2026-09-28 | bybit_ob/bybit/ETH-USDT/perp | 858,694 | 1.000 | 1.7 | 0 | 3.0 / 16.0 | 0.04 | 280 | 93.1% | 0 | 0 | yes |
| 2026-09-28 | bybit_ob/bybit/ETH-USDT/spot | 739,203 | 1.000 | 2.0 | 0 | 5.0 / 45.0 | 0.04 | 275 | 95.8% | 1 | 0 | yes |
| 2026-09-29 | bybit_ob/bybit/BTC-USDT/perp | 863,204 | 1.000 | 0.7 | 0 | 3.0 / 12.0 | 0.01 | 174 | 94.6% | 0 | 0 | yes |
| 2026-09-29 | bybit_ob/bybit/BTC-USDT/spot | 806,376 | 1.000 | 1.3 | 0 | 5.0 / 32.0 | 0.01 | 169 | 99.0% | 0 | 0 | yes |
| 2026-09-29 | bybit_ob/bybit/ETH-USDT/perp | 857,203 | 1.000 | 1.7 | 0 | 3.0 / 16.0 | 0.04 | 234 | 93.9% | 0 | 0 | yes |
| 2026-09-29 | bybit_ob/bybit/ETH-USDT/spot | 695,243 | 1.000 | 1.9 | 0 | 6.0 / 47.0 | 0.04 | 229 | 96.5% | 0 | 0 | yes |
| 2026-09-30 | bybit_ob/bybit/BTC-USDT/perp | 863,270 | 1.000 | 0.1 | 0 | 3.0 / 12.0 | 0.01 | 221 | 91.6% | 1 | 0 | yes |
| 2026-09-30 | bybit_ob/bybit/BTC-USDT/spot | 816,206 | 1.000 | 1.4 | 0 | 5.0 / 33.0 | 0.01 | 217 | 98.6% | 0 | 0 | yes |
| 2026-09-30 | bybit_ob/bybit/ETH-USDT/perp | 853,243 | 1.000 | 1.7 | 0 | 3.0 / 16.0 | 0.04 | 230 | 92.9% | 1 | 0 | yes |
| 2026-09-30 | bybit_ob/bybit/ETH-USDT/spot | 656,129 | 1.000 | 2.0 | 0 | 6.0 / 47.0 | 0.04 | 226 | 95.8% | 0 | 0 | yes |
| 2026-10-01 | bybit_ob/bybit/BTC-USDT/perp | 863,390 | 1.000 | 0.1 | 0 | 2.0 / 12.0 | 0.01 | 192 | 92.9% | 0 | 0 | yes |
| 2026-10-01 | bybit_ob/bybit/BTC-USDT/spot | 808,497 | 1.000 | 2.1 | 0 | 5.0 / 34.0 | 0.01 | 186 | 98.8% | 0 | 0 | yes |
| 2026-10-01 | bybit_ob/bybit/ETH-USDT/perp | 852,552 | 1.000 | 1.7 | 0 | 3.0 / 16.0 | 0.04 | 229 | 92.1% | 0 | 0 | yes |
| 2026-10-01 | bybit_ob/bybit/ETH-USDT/spot | 687,773 | 1.000 | 2.8 | 0 | 6.0 / 46.0 | 0.04 | 223 | 96.4% | 1 | 0 | yes |
| 2026-10-02 | bybit_ob/bybit/BTC-USDT/perp | 863,728 | 1.000 | 0.1 | 0 | 2.0 / 12.0 | 0.01 | 222 | 91.3% | 0 | 0 | yes |
| 2026-10-02 | bybit_ob/bybit/BTC-USDT/spot | 826,204 | 1.000 | 1.6 | 0 | 5.0 / 28.0 | 0.01 | 216 | 98.2% | 0 | 0 | yes |
| 2026-10-02 | bybit_ob/bybit/ETH-USDT/perp | 856,238 | 1.000 | 1.7 | 0 | 3.0 / 16.0 | 0.04 | 274 | 88.1% | 0 | 0 | yes |
| 2026-10-02 | bybit_ob/bybit/ETH-USDT/spot | 739,209 | 1.000 | 2.7 | 0 | 6.0 / 45.9 | 0.04 | 265 | 95.0% | 1 | 0 | yes |
| 2026-10-03 | bybit_ob/bybit/BTC-USDT/perp | 859,710 | 1.000 | 0.6 | 0 | 3.0 / 14.0 | 0.01 | 63 | 95.1% | 1 | 0 | yes |
| 2026-10-03 | bybit_ob/bybit/BTC-USDT/spot | 714,128 | 1.000 | 1.9 | 0 | 7.0 / 39.0 | 0.01 | 60 | 98.4% | 0 | 0 | yes |
| 2026-10-03 | bybit_ob/bybit/ETH-USDT/perp | 814,536 | 1.000 | 1.7 | 0 | 5.0 / 17.0 | 0.04 | 85 | 94.2% | 1 | 0 | yes |
| 2026-10-03 | bybit_ob/bybit/ETH-USDT/spot | 555,668 | 1.000 | 2.5 | 0 | 11.0 / 49.0 | 0.04 | 83 | 97.7% | 1 | 0 | yes |
| 2026-10-04 | bybit_ob/bybit/BTC-USDT/perp | 859,966 | 1.000 | 0.6 | 0 | 3.0 / 13.0 | 0.01 | 103 | 92.3% | 1 | 0 | yes |
| 2026-10-04 | bybit_ob/bybit/BTC-USDT/spot | 722,113 | 1.000 | 2.2 | 0 | 6.0 / 42.0 | 0.01 | 99 | 98.8% | 0 | 0 | yes |
| 2026-10-04 | bybit_ob/bybit/ETH-USDT/perp | 817,611 | 1.000 | 1.7 | 0 | 4.0 / 16.0 | 0.04 | 115 | 92.7% | 1 | 0 | yes |
| 2026-10-04 | bybit_ob/bybit/ETH-USDT/spot | 587,827 | 1.000 | 2.0 | 0 | 10.0 / 48.0 | 0.04 | 110 | 96.3% | 1 | 0 | yes |
| 2026-10-05 | bybit_ob/bybit/BTC-USDT/perp | 862,899 | 1.000 | 0.1 | 0 | 3.0 / 14.0 | 0.01 | 185 | 92.3% | 1 | 0 | yes |
| 2026-10-05 | bybit_ob/bybit/BTC-USDT/spot | 803,388 | 1.000 | 1.4 | 0 | 4.0 / 35.0 | 0.01 | 180 | 98.6% | 0 | 0 | yes |
| 2026-10-05 | bybit_ob/bybit/ETH-USDT/perp | 854,955 | 1.000 | 1.7 | 0 | 3.0 / 16.0 | 0.04 | 190 | 91.7% | 0 | 0 | yes |
| 2026-10-05 | bybit_ob/bybit/ETH-USDT/spot | 696,480 | 1.000 | 2.0 | 0 | 7.0 / 46.0 | 0.04 | 185 | 96.5% | 1 | 0 | yes |
| 2026-10-06 | bybit_ob/bybit/BTC-USDT/perp | 862,529 | 1.000 | 0.6 | 0 | 3.0 / 13.0 | 0.01 | 149 | 93.3% | 1 | 0 | yes |
| 2026-10-06 | bybit_ob/bybit/BTC-USDT/spot | 781,636 | 1.000 | 1.3 | 0 | 5.0 / 37.0 | 0.01 | 144 | 99.2% | 0 | 0 | yes |
| 2026-10-06 | bybit_ob/bybit/ETH-USDT/perp | 850,982 | 1.000 | 1.7 | 0 | 4.0 / 26.0 | 0.04 | 149 | 92.7% | 1 | 0 | yes |
| 2026-10-06 | bybit_ob/bybit/ETH-USDT/spot | 673,822 | 1.000 | 1.5 | 0 | 8.0 / 47.0 | 0.04 | 143 | 96.8% | 0 | 0 | yes |
| 2026-10-07 | bybit_ob/bybit/BTC-USDT/perp | 862,910 | 1.000 | 0.1 | 0 | 2.0 / 10.0 | 0.01 | 176 | 92.2% | 1 | 0 | yes |
| 2026-10-07 | bybit_ob/bybit/BTC-USDT/spot | 813,775 | 1.000 | 1.3 | 0 | 5.0 / 33.0 | 0.01 | 172 | 98.7% | 0 | 0 | yes |
| 2026-10-07 | bybit_ob/bybit/ETH-USDT/perp | 857,349 | 1.000 | 1.7 | 0 | 5.0 / 27.0 | 0.04 | 246 | 87.6% | 1 | 0 | yes |
| 2026-10-07 | bybit_ob/bybit/ETH-USDT/spot | 695,437 | 1.000 | 1.9 | 0 | 7.0 / 46.0 | 0.04 | 242 | 94.1% | 0 | 0 | yes |
| 2026-10-08 | bybit_ob/bybit/BTC-USDT/perp | 863,473 | 1.000 | 1.0 | 0 | 2.0 / 4.0 | 0.01 | 230 | 92.3% | 0 | 0 | yes |
| 2026-10-08 | bybit_ob/bybit/BTC-USDT/spot | 819,544 | 1.000 | 1.5 | 0 | 4.0 / 28.0 | 0.01 | 222 | 98.9% | 0 | 0 | yes |
| 2026-10-08 | bybit_ob/bybit/ETH-USDT/perp | 861,322 | 1.000 | 1.7 | 0 | 4.0 / 25.0 | 0.04 | 310 | 89.9% | 0 | 0 | yes |
| 2026-10-08 | bybit_ob/bybit/ETH-USDT/spot | 734,095 | 1.000 | 2.2 | 0 | 6.0 / 61.0 | 0.04 | 305 | 94.2% | 0 | 0 | yes |
| 2026-10-09 | bybit_ob/bybit/BTC-USDT/perp | 862,621 | 1.000 | 0.1 | 0 | 2.0 / 3.0 | 0.01 | 159 | 95.6% | 0 | 0 | yes |
| 2026-10-09 | bybit_ob/bybit/BTC-USDT/spot | 799,890 | 1.000 | 1.9 | 0 | 3.0 / 10.0 | 0.01 | 155 | 99.2% | 0 | 0 | yes |
| 2026-10-09 | bybit_ob/bybit/ETH-USDT/perp | 854,736 | 1.000 | 1.7 | 0 | 4.0 / 28.0 | 0.04 | 203 | 95.1% | 1 | 0 | yes |
| 2026-10-09 | bybit_ob/bybit/ETH-USDT/spot | 702,975 | 1.000 | 2.0 | 0 | 9.0 / 87.0 | 0.04 | 200 | 98.0% | 0 | 0 | yes |
| 2026-10-10 | bybit_ob/bybit/BTC-USDT/perp | 854,316 | 1.000 | 0.9 | 0 | 1.0 / 3.0 | 0.01 | 65 | 94.9% | 0 | 0 | yes |
| 2026-10-10 | bybit_ob/bybit/BTC-USDT/spot | 703,549 | 1.000 | 1.9 | 0 | 4.0 / 10.0 | 0.01 | 60 | 98.9% | 0 | 0 | yes |
| 2026-10-10 | bybit_ob/bybit/ETH-USDT/perp | 822,908 | 1.000 | 1.7 | 0 | 5.0 / 38.0 | 0.04 | 101 | 95.3% | 0 | 0 | yes |
| 2026-10-10 | bybit_ob/bybit/ETH-USDT/spot | 532,459 | 1.000 | 2.4 | 0 | 15.0 / 96.0 | 0.04 | 97 | 98.2% | 0 | 0 | yes |
| 2026-10-11 | bybit_ob/bybit/BTC-USDT/perp | 854,862 | 1.000 | 0.7 | 0 | 1.0 / 3.0 | 0.01 | 100 | 92.3% | 1 | 0 | yes |
| 2026-10-11 | bybit_ob/bybit/BTC-USDT/spot | 710,481 | 1.000 | 2.0 | 0 | 4.0 / 10.0 | 0.01 | 96 | 99.1% | 0 | 0 | yes |
| 2026-10-11 | bybit_ob/bybit/ETH-USDT/perp | 833,925 | 1.000 | 1.7 | 0 | 5.0 / 33.0 | 0.04 | 159 | 92.7% | 0 | 0 | yes |
| 2026-10-11 | bybit_ob/bybit/ETH-USDT/spot | 554,371 | 1.000 | 2.7 | 0 | 12.0 / 93.0 | 0.04 | 155 | 96.9% | 0 | 0 | yes |
| 2026-10-12 | bybit_ob/bybit/BTC-USDT/perp | 862,963 | 1.000 | 0.1 | 0 | 1.0 / 3.0 | 0.01 | 168 | 93.6% | 0 | 0 | yes |
| 2026-10-12 | bybit_ob/bybit/BTC-USDT/spot | 783,071 | 1.000 | 1.6 | 0 | 3.0 / 10.0 | 0.01 | 163 | 99.2% | 0 | 0 | yes |
| 2026-10-12 | bybit_ob/bybit/ETH-USDT/perp | 858,214 | 1.000 | 1.7 | 0 | 4.0 / 28.0 | 0.04 | 243 | 93.0% | 0 | 0 | yes |
| 2026-10-12 | bybit_ob/bybit/ETH-USDT/spot | 716,069 | 1.000 | 1.4 | 0 | 8.0 / 82.0 | 0.04 | 238 | 97.2% | 0 | 0 | yes |
| 2026-10-13 | bybit_ob/bybit/BTC-USDT/perp | 862,460 | 1.000 | 12.7 | 2 | 1.0 / 4.0 | 0.01 | 193 | 93.7% | 1 | 0 | yes |
| 2026-10-13 | bybit_ob/bybit/BTC-USDT/spot | 794,344 | 1.000 | 14.0 | 1 | 3.0 / 10.0 | 0.01 | 189 | 99.2% | 0 | 0 | yes |
| 2026-10-13 | bybit_ob/bybit/ETH-USDT/perp | 858,578 | 1.000 | 12.1 | 2 | 4.0 / 29.0 | 0.04 | 282 | 92.6% | 0 | 0 | yes |
| 2026-10-13 | bybit_ob/bybit/ETH-USDT/spot | 710,243 | 1.000 | 11.1 | 1 | 7.0 / 81.0 | 0.04 | 276 | 96.3% | 0 | 0 | yes |
| 2026-10-14 | bybit_ob/bybit/BTC-USDT/perp | 863,266 | 1.000 | 0.5 | 0 | 2.0 / 4.0 | 0.01 | 217 | 93.1% | 0 | 0 | yes |
| 2026-10-14 | bybit_ob/bybit/BTC-USDT/spot | 802,675 | 1.000 | 1.5 | 0 | 3.0 / 10.0 | 0.01 | 211 | 98.8% | 0 | 0 | yes |
| 2026-10-14 | bybit_ob/bybit/ETH-USDT/perp | 860,799 | 1.000 | 0.6 | 0 | 3.0 / 28.0 | 0.04 | 296 | 92.3% | 0 | 0 | yes |
| 2026-10-14 | bybit_ob/bybit/ETH-USDT/spot | 710,252 | 1.000 | 1.9 | 0 | 6.0 / 78.0 | 0.04 | 290 | 95.6% | 0 | 0 | yes |
| 2026-10-15 | bybit_ob/bybit/BTC-USDT/perp | 863,459 | 1.000 | 0.5 | 0 | 2.0 / 5.0 | 0.01 | 274 | 92.4% | 0 | 0 | yes |
| 2026-10-15 | bybit_ob/bybit/BTC-USDT/spot | 837,207 | 1.000 | 0.9 | 0 | 3.0 / 10.0 | 0.01 | 269 | 98.7% | 0 | 0 | yes |
| 2026-10-15 | bybit_ob/bybit/ETH-USDT/perp | 862,336 | 1.000 | 0.6 | 0 | 3.0 / 26.0 | 0.04 | 425 | 89.8% | 1 | 0 | yes |
| 2026-10-15 | bybit_ob/bybit/ETH-USDT/spot | 767,655 | 1.000 | 1.6 | 0 | 5.0 / 67.0 | 0.04 | 419 | 94.6% | 0 | 0 | yes |
| 2026-10-16 | bybit_ob/bybit/BTC-USDT/perp | 863,006 | 1.000 | 0.6 | 0 | 2.0 / 4.0 | 0.01 | 196 | 94.7% | 0 | 0 | yes |
| 2026-10-16 | bybit_ob/bybit/BTC-USDT/spot | 812,156 | 1.000 | 2.0 | 0 | 3.0 / 10.0 | 0.01 | 190 | 99.3% | 0 | 0 | yes |
| 2026-10-16 | bybit_ob/bybit/ETH-USDT/perp | 860,315 | 1.000 | 0.6 | 0 | 4.0 / 29.0 | 0.04 | 270 | 93.3% | 1 | 0 | yes |
| 2026-10-16 | bybit_ob/bybit/ETH-USDT/spot | 755,144 | 1.000 | 1.6 | 0 | 6.0 / 77.0 | 0.04 | 265 | 96.8% | 0 | 0 | yes |
| 2026-10-17 | bybit_ob/bybit/BTC-USDT/perp | 858,077 | 1.000 | 0.7 | 0 | 1.0 / 3.0 | 0.01 | 102 | 96.3% | 1 | 0 | yes |
| 2026-10-17 | bybit_ob/bybit/BTC-USDT/spot | 745,686 | 1.000 | 2.2 | 0 | 4.0 / 10.0 | 0.01 | 97 | 99.3% | 1 | 0 | yes |
| 2026-10-17 | bybit_ob/bybit/ETH-USDT/perp | 847,610 | 1.000 | 0.8 | 0 | 5.0 / 36.0 | 0.04 | 191 | 94.0% | 0 | 0 | yes |
| 2026-10-17 | bybit_ob/bybit/ETH-USDT/spot | 628,066 | 1.000 | 2.1 | 0 | 11.0 / 94.0 | 0.04 | 186 | 97.4% | 0 | 0 | yes |
| 2026-10-18 | bybit_ob/bybit/BTC-USDT/perp | 861,293 | 1.000 | 0.5 | 0 | 1.0 / 3.0 | 0.01 | 137 | 94.7% | 1 | 0 | yes |
| 2026-10-18 | bybit_ob/bybit/BTC-USDT/spot | 767,062 | 1.000 | 1.6 | 0 | 4.0 / 10.0 | 0.01 | 130 | 99.4% | 0 | 0 | yes |
| 2026-10-18 | bybit_ob/bybit/ETH-USDT/perp | 856,638 | 1.000 | 0.8 | 0 | 4.0 / 33.0 | 0.04 | 242 | 93.8% | 1 | 0 | yes |
| 2026-10-18 | bybit_ob/bybit/ETH-USDT/spot | 702,541 | 1.000 | 1.9 | 0 | 9.0 / 89.0 | 0.04 | 237 | 97.2% | 0 | 0 | yes |
| 2026-10-19 | bybit_ob/bybit/BTC-USDT/perp | 862,962 | 1.000 | 0.5 | 0 | 1.0 / 3.0 | 0.01 | 176 | no trade record | - | - | yes |
| 2026-10-19 | bybit_ob/bybit/BTC-USDT/spot | 788,435 | 1.000 | 1.2 | 0 | 3.0 / 10.0 | 0.01 | 170 | no trade record | - | - | yes |
| 2026-10-19 | bybit_ob/bybit/ETH-USDT/perp | 860,204 | 1.000 | 0.9 | 0 | 4.0 / 30.0 | 0.04 | 250 | no trade record | - | - | yes |
| 2026-10-19 | bybit_ob/bybit/ETH-USDT/spot | 758,334 | 1.000 | 1.3 | 0 | 7.0 / 78.0 | 0.04 | 243 | no trade record | - | - | yes |

## Development data, pooled

Holdout days are excluded. Stale births are dropped. Lifetimes are shown only for episodes longer than the pair's sampling step; shorter ones are known only to within it.

Fresh partner = every sampled leg's quote was less than half a step old at the birth: the cleanest labels.

| Pair | Hurdle | Days | Episodes per day | Shorter than resolution | Resolved life median / p90 (ms) | Fresh-partner births per day | Fresh: shorter than resolution | Fresh: resolved life median (ms) |
|---|---|---|---|---|---|---|---|---|
| aave_perp_binance_bybit | gross>0bps | 81 | 18,993 | 38% | 718 / 7,830 | 12,321.7 | 34% | 854 |
| aave_perp_binance_bybit | gross>1bps | 81 | 18,260 | 38% | 707 / 7,780 | 11,741.9 | 34% | 850 |
| aave_perp_binance_bybit | gross>2bps | 81 | 14,627 | 42% | 638 / 6,885 | 9,165.3 | 37% | 794 |
| aave_perp_binance_bybit | gross>5bps | 81 | 6,045 | 51% | 499 / 4,883 | 3,588.9 | 45% | 605 |
| aave_perp_binance_bybit | retail_taker | 81 | 475 | 82% | 158 / 1,051 | 232.7 | 81% | 213 |
| arb_perp_binance_bybit | gross>0bps | 92 | 15,521 | 36% | 900 / 10,284 | 10,399.8 | 33% | 1,041 |
| arb_perp_binance_bybit | gross>1bps | 92 | 15,304 | 36% | 900 / 9,784 | 10,225.8 | 33% | 1,030 |
| arb_perp_binance_bybit | gross>2bps | 92 | 13,693 | 38% | 793 / 8,005 | 9,044.2 | 35% | 901 |
| arb_perp_binance_bybit | gross>5bps | 92 | 6,797 | 47% | 520 / 4,911 | 4,280.7 | 43% | 631 |
| arb_perp_binance_bybit | retail_taker | 91 | 520 | 78% | 190 / 1,296 | 270.3 | 76% | 242 |
| btc_perp_binance_bybit | gross>0bps | 257 | 7,943 | 29% | 1,477 / 24,993 | 5,463.6 | 27% | 1,700 |
| btc_perp_binance_bybit | gross>1bps | 257 | 7,188 | 33% | 1,081 / 15,979 | 4,744.6 | 32% | 1,290 |
| btc_perp_binance_bybit | gross>2bps | 257 | 5,118 | 39% | 789 / 11,000 | 3,299.8 | 37% | 998 |
| btc_perp_binance_bybit | gross>5bps | 257 | 1,290 | 48% | 718 / 9,733 | 838.2 | 44% | 970 |
| btc_perp_binance_bybit | retail_taker | 241 | 87 | 78% | 226 / 2,407 | 50.0 | 74% | 296 |
| bybit_btc_basis | gross>0bps | 32 | 27,060 | 36% | 1,389 / 11,198 | 15,862.0 | 19% | 1,686 |
| bybit_btc_basis | gross>1bps | 32 | 5,016 | 69% | 586 / 4,300 | 2,188.6 | 39% | 600 |
| bybit_btc_basis | gross>2bps | 32 | 613 | 93% | 200 / 2,418 | 79.2 | 63% | 201 |
| bybit_btc_basis | gross>5bps | 31 | 31 | 95% | 400 / 6,991 | 2.6 | 55% | 693 |
| bybit_eth_basis | gross>0bps | 32 | 40,043 | 31% | 900 / 6,821 | 17,749.9 | 31% | 780 |
| bybit_eth_basis | gross>1bps | 32 | 12,120 | 73% | 300 / 1,824 | 3,070.0 | 64% | 297 |
| bybit_eth_basis | gross>2bps | 32 | 1,703 | 91% | 176 / 499 | 367.0 | 84% | 178 |
| bybit_eth_basis | gross>5bps | 32 | 105 | 98% | 121 / 480 | 13.5 | 95% | 197 |
| bybit_eth_basis | retail_taker | 2 | 4 | 57% | 221 / 284 | 0.0 | - | none resolved |
| bybit_eth_btc_ratio | gross>0bps | 32 | 42,047 | 22% | 1,198 / 3,200 | 28,450.2 | 10% | 1,297 |
| bybit_eth_btc_ratio | gross>1bps | 32 | 11,877 | 52% | 296 / 599 | 8,185.6 | 37% | 297 |
| bybit_eth_btc_ratio | gross>2bps | 32 | 2,028 | 66% | 199 / 597 | 1,269.1 | 50% | 199 |
| bybit_eth_btc_ratio | gross>5bps | 32 | 128 | 73% | 199 / 595 | 78.6 | 60% | 199 |
| bybit_eth_btc_ratio | retail_taker | 11 | 5 | 63% | 198 / 398 | 4.3 | 57% | 198 |
| doge_perp_binance_bybit | gross>0bps | 92 | 11,282 | 35% | 914 / 10,783 | 7,432.2 | 34% | 1,165 |
| doge_perp_binance_bybit | gross>1bps | 92 | 11,212 | 35% | 912 / 10,761 | 7,381.0 | 34% | 1,162 |
| doge_perp_binance_bybit | gross>2bps | 92 | 8,735 | 40% | 785 / 8,881 | 5,618.5 | 38% | 1,020 |
| doge_perp_binance_bybit | gross>5bps | 92 | 3,309 | 52% | 507 / 5,597 | 1,982.8 | 49% | 723 |
| doge_perp_binance_bybit | retail_taker | 91 | 297 | 79% | 190 / 1,057 | 160.6 | 77% | 252 |
| eth_perp_binance_bybit | gross>0bps | 226 | 8,921 | 27% | 1,510 / 22,898 | 6,138.0 | 26% | 1,790 |
| eth_perp_binance_bybit | gross>1bps | 226 | 7,787 | 32% | 1,113 / 15,557 | 5,148.7 | 31% | 1,334 |
| eth_perp_binance_bybit | gross>2bps | 226 | 5,199 | 39% | 821 / 10,963 | 3,313.6 | 37% | 1,038 |
| eth_perp_binance_bybit | gross>5bps | 226 | 965 | 52% | 595 / 7,622 | 614.1 | 48% | 799 |
| eth_perp_binance_bybit | retail_taker | 212 | 77 | 82% | 196 / 881 | 44.9 | 79% | 207 |
| sol_perp_binance_bybit | gross>0bps | 85 | 37,926 | 46% | 585 / 5,893 | 24,641.7 | 42% | 695 |
| sol_perp_binance_bybit | gross>1bps | 85 | 36,638 | 47% | 535 / 5,037 | 23,668.5 | 43% | 648 |
| sol_perp_binance_bybit | gross>2bps | 85 | 33,769 | 48% | 495 / 4,292 | 21,726.4 | 45% | 596 |
| sol_perp_binance_bybit | gross>5bps | 85 | 18,426 | 54% | 399 / 3,082 | 11,536.8 | 50% | 497 |
| sol_perp_binance_bybit | retail_taker | 85 | 1,937 | 71% | 235 / 1,570 | 1,092.8 | 67% | 299 |
| tia_perp_binance_bybit | gross>0bps | 53 | 23,723 | 48% | 718 / 9,500 | 15,736.2 | 42% | 798 |
| tia_perp_binance_bybit | gross>1bps | 53 | 25,976 | 47% | 701 / 8,554 | 17,475.2 | 41% | 774 |
| tia_perp_binance_bybit | gross>2bps | 53 | 29,174 | 46% | 676 / 7,431 | 19,818.1 | 40% | 726 |
| tia_perp_binance_bybit | gross>5bps | 53 | 37,528 | 47% | 545 / 4,701 | 25,456.8 | 41% | 599 |
| tia_perp_binance_bybit | retail_taker | 53 | 23,232 | 56% | 386 / 2,551 | 14,637.5 | 50% | 418 |
| wld_perp_binance_bybit | gross>0bps | 89 | 23,026 | 40% | 684 / 5,868 | 13,704.3 | 37% | 734 |
| wld_perp_binance_bybit | gross>1bps | 89 | 20,622 | 41% | 654 / 5,596 | 12,237.0 | 38% | 701 |
| wld_perp_binance_bybit | gross>2bps | 89 | 17,345 | 43% | 603 / 5,101 | 10,286.2 | 39% | 675 |
| wld_perp_binance_bybit | gross>5bps | 89 | 9,314 | 49% | 497 / 3,694 | 5,468.3 | 44% | 540 |
| wld_perp_binance_bybit | retail_taker | 89 | 1,735 | 69% | 263 / 1,668 | 900.4 | 66% | 311 |
| xrp_perp_binance_bybit | gross>0bps | 92 | 6,624 | 36% | 907 / 12,664 | 4,254.8 | 36% | 1,280 |
| xrp_perp_binance_bybit | gross>1bps | 92 | 6,624 | 36% | 907 / 12,664 | 4,254.8 | 36% | 1,280 |
| xrp_perp_binance_bybit | gross>2bps | 92 | 4,149 | 43% | 705 / 10,441 | 2,558.1 | 42% | 1,066 |
| xrp_perp_binance_bybit | gross>5bps | 92 | 1,313 | 62% | 321 / 5,000 | 750.4 | 61% | 500 |
| xrp_perp_binance_bybit | retail_taker | 92 | 229 | 86% | 170 / 601 | 125.8 | 84% | 191 |
| zec_perp_binance_bybit | gross>0bps | 8 | 9,190 | 23% | 799 / 10,948 | 6,262.0 | 18% | 800 |
| zec_perp_binance_bybit | gross>1bps | 8 | 9,190 | 23% | 799 / 10,948 | 6,262.0 | 18% | 800 |
| zec_perp_binance_bybit | gross>2bps | 8 | 9,190 | 23% | 799 / 10,948 | 6,262.0 | 18% | 800 |
| zec_perp_binance_bybit | gross>5bps | 8 | 4,671 | 30% | 652 / 8,405 | 2,824.1 | 24% | 700 |
| zec_perp_binance_bybit | retail_taker | 8 | 482 | 58% | 353 / 4,103 | 205.8 | 49% | 472 |

## Episodes by day

| Date | Pair | Status | Valid share | Hurdle | Episodes | Observed deaths | Shorter than resolution | Median life, resolved only (ms) | Stale births | Stale partner |
|---|---|---|---|---|---|---|---|---|---|---|
| 2023-05-16 | btc_perp_binance_bybit | excluded: binance_bt/binance/BTC-USDT/perp coverage 0.413 below threshold | | | | | | | | |
| 2023-05-16 | eth_perp_binance_bybit | excluded: binance_bt/binance/ETH-USDT/perp coverage 0.413 below threshold | | | | | | | | |
| 2023-05-17 | btc_perp_binance_bybit | excluded: binance_bt/binance/BTC-USDT/perp coverage 0.627 below threshold | | | | | | | | |
| 2023-05-17 | eth_perp_binance_bybit | excluded: binance_bt/binance/ETH-USDT/perp coverage 0.627 below threshold | | | | | | | | |
| 2023-05-18 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,179 | 100.0% | 25% | 1,474 | 0.0% | 33% |
| 2023-05-18 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,423 | 100.0% | 29% | 1,083 | 0.0% | 38% |
| 2023-05-18 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,378 | 100.0% | 35% | 688 | 0.0% | 42% |
| 2023-05-18 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 550 | 100.0% | 82% | 131 | 0.0% | 49% |
| 2023-05-18 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 69 | 100.0% | 87% | 166 | 0.0% | 48% |
| 2023-05-18 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,473 | 100.0% | 23% | 1,962 | 0.0% | 32% |
| 2023-05-18 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,293 | 100.0% | 28% | 1,234 | 0.0% | 35% |
| 2023-05-18 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,742 | 100.0% | 37% | 766 | 0.0% | 40% |
| 2023-05-18 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 336 | 100.0% | 80% | 137 | 0.0% | 51% |
| 2023-05-18 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 25 | 100.0% | 72% | 118 | 0.0% | 56% |
| 2023-05-19 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,802 | 100.0% | 20% | 2,085 | 0.0% | 34% |
| 2023-05-19 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,853 | 100.0% | 26% | 1,293 | 0.1% | 40% |
| 2023-05-19 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,425 | 100.0% | 36% | 1,284 | 0.1% | 45% |
| 2023-05-19 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 131 | 100.0% | 84% | 121 | 0.0% | 57% |
| 2023-05-19 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2023-05-19 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,250 | 100.0% | 18% | 2,047 | 0.0% | 33% |
| 2023-05-19 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,474 | 100.0% | 28% | 1,038 | 0.0% | 42% |
| 2023-05-19 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,639 | 100.0% | 42% | 674 | 0.1% | 45% |
| 2023-05-19 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 176 | 100.0% | 81% | 145 | 0.0% | 47% |
| 2023-05-19 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 6 | 100.0% | 100% | none resolved | 0.0% | 33% |
| 2023-05-20 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,632 | 99.9% | 12% | 8,537 | 0.0% | 35% |
| 2023-05-20 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,612 | 100.0% | 15% | 4,926 | 0.0% | 35% |
| 2023-05-20 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,163 | 100.0% | 19% | 2,317 | 0.0% | 40% |
| 2023-05-20 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 50 | 100.0% | 66% | 146 | 0.0% | 46% |
| 2023-05-20 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 2 | 100.0% | 50% | 124 | 0.0% | 50% |
| 2023-05-20 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,461 | 100.0% | 12% | 6,700 | 0.0% | 32% |
| 2023-05-20 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,897 | 99.9% | 16% | 4,106 | 0.0% | 39% |
| 2023-05-20 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,141 | 100.0% | 26% | 2,856 | 0.0% | 47% |
| 2023-05-20 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 63 | 100.0% | 89% | 116 | 0.0% | 52% |
| 2023-05-21 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,219 | 100.0% | 19% | 3,860 | 0.0% | 33% |
| 2023-05-21 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,974 | 100.0% | 22% | 2,205 | 0.0% | 35% |
| 2023-05-21 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,905 | 100.0% | 30% | 1,101 | 0.1% | 42% |
| 2023-05-21 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 125 | 100.0% | 73% | 338 | 0.0% | 45% |
| 2023-05-21 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 13 | 100.0% | 77% | 467 | 0.0% | 23% |
| 2023-05-21 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,669 | 100.0% | 18% | 4,792 | 0.1% | 33% |
| 2023-05-21 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,935 | 100.0% | 25% | 2,548 | 0.1% | 40% |
| 2023-05-21 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,550 | 99.9% | 36% | 1,164 | 0.0% | 44% |
| 2023-05-21 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 84 | 100.0% | 90% | 142 | 0.0% | 35% |
| 2023-05-21 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 5 | 100.0% | 100% | none resolved | 0.0% | 40% |
| 2023-05-22 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,600 | 100.0% | 19% | 2,862 | 0.0% | 33% |
| 2023-05-22 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,358 | 100.0% | 21% | 1,976 | 0.0% | 35% |
| 2023-05-22 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,185 | 100.0% | 25% | 1,345 | 0.0% | 39% |
| 2023-05-22 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 212 | 100.0% | 78% | 125 | 0.0% | 50% |
| 2023-05-22 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 15 | 100.0% | 80% | 190 | 0.0% | 47% |
| 2023-05-22 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,090 | 100.0% | 15% | 2,525 | 0.0% | 33% |
| 2023-05-22 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,733 | 100.0% | 27% | 1,474 | 0.0% | 41% |
| 2023-05-22 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,362 | 100.0% | 40% | 942 | 0.1% | 47% |
| 2023-05-22 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 103 | 100.0% | 83% | 111 | 0.0% | 50% |
| 2023-05-22 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 6 | 100.0% | 83% | 119 | 0.0% | 33% |
| 2023-05-23 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,704 | 100.0% | 23% | 2,332 | 0.0% | 33% |
| 2023-05-23 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,304 | 100.0% | 25% | 1,926 | 0.1% | 36% |
| 2023-05-23 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,285 | 100.0% | 27% | 1,651 | 0.0% | 39% |
| 2023-05-23 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 422 | 100.0% | 54% | 289 | 0.0% | 49% |
| 2023-05-23 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 16 | 100.0% | 75% | 157 | 0.0% | 44% |
| 2023-05-23 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,193 | 100.0% | 24% | 2,839 | 0.0% | 33% |
| 2023-05-23 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,716 | 100.0% | 26% | 1,471 | 0.0% | 35% |
| 2023-05-23 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,200 | 100.0% | 34% | 748 | 0.0% | 41% |
| 2023-05-23 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 531 | 100.0% | 82% | 142 | 0.0% | 44% |
| 2023-05-23 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 47 | 100.0% | 96% | 214 | 0.0% | 51% |
| 2023-05-24 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,779 | 100.0% | 28% | 1,401 | 0.1% | 34% |
| 2023-05-24 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,323 | 100.0% | 35% | 862 | 0.1% | 38% |
| 2023-05-24 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,685 | 100.0% | 44% | 495 | 0.0% | 42% |
| 2023-05-24 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 573 | 100.0% | 86% | 160 | 0.0% | 46% |
| 2023-05-24 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 36 | 100.0% | 75% | 163 | 0.0% | 36% |
| 2023-05-24 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,761 | 100.0% | 27% | 1,610 | 0.0% | 34% |
| 2023-05-24 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,467 | 100.0% | 35% | 836 | 0.0% | 40% |
| 2023-05-24 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,063 | 100.0% | 51% | 394 | 0.0% | 47% |
| 2023-05-24 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 388 | 100.0% | 88% | 133 | 0.0% | 48% |
| 2023-05-24 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 41 | 100.0% | 80% | 155 | 0.0% | 49% |
| 2023-05-25 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,835 | 100.0% | 23% | 2,236 | 0.2% | 32% |
| 2023-05-25 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,186 | 100.0% | 27% | 1,502 | 0.2% | 36% |
| 2023-05-25 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,287 | 100.0% | 32% | 951 | 0.1% | 41% |
| 2023-05-25 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 307 | 100.0% | 77% | 158 | 0.3% | 43% |
| 2023-05-25 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 25 | 100.0% | 72% | 268 | 0.0% | 36% |
| 2023-05-25 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,062 | 100.0% | 26% | 2,136 | 0.0% | 33% |
| 2023-05-25 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,892 | 100.0% | 31% | 1,306 | 0.0% | 38% |
| 2023-05-25 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,176 | 100.0% | 41% | 858 | 0.0% | 41% |
| 2023-05-25 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 339 | 100.0% | 82% | 146 | 0.0% | 40% |
| 2023-05-25 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 72 | 100.0% | 90% | 203 | 0.0% | 35% |
| 2023-05-26 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,881 | 100.0% | 19% | 2,470 | 0.0% | 33% |
| 2023-05-26 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,317 | 100.0% | 23% | 2,205 | 0.1% | 38% |
| 2023-05-26 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,837 | 100.0% | 30% | 1,286 | 0.1% | 42% |
| 2023-05-26 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 93 | 100.0% | 82% | 147 | 0.0% | 42% |
| 2023-05-26 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 5 | 100.0% | 20% | 155 | 0.0% | 40% |
| 2023-05-26 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,063 | 100.0% | 18% | 3,236 | 0.1% | 32% |
| 2023-05-26 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,241 | 100.0% | 25% | 2,007 | 0.0% | 38% |
| 2023-05-26 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,722 | 100.0% | 30% | 1,113 | 0.0% | 40% |
| 2023-05-26 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 166 | 100.0% | 73% | 149 | 0.0% | 47% |
| 2023-05-26 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 7 | 100.0% | 57% | 130 | 0.0% | 43% |
| 2023-05-27 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,963 | 99.9% | 16% | 7,026 | 0.0% | 33% |
| 2023-05-27 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,684 | 99.9% | 20% | 4,414 | 0.0% | 38% |
| 2023-05-27 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 976 | 100.0% | 28% | 2,514 | 0.0% | 44% |
| 2023-05-27 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 40 | 100.0% | 65% | 126 | 0.0% | 57% |
| 2023-05-27 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2023-05-27 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,534 | 100.0% | 16% | 7,897 | 0.0% | 34% |
| 2023-05-27 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,121 | 100.0% | 21% | 4,917 | 0.0% | 42% |
| 2023-05-27 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,275 | 100.0% | 29% | 3,589 | 0.0% | 49% |
| 2023-05-27 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 63 | 100.0% | 71% | 130 | 0.0% | 44% |
| 2023-05-27 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 4 | 100.0% | 100% | none resolved | 0.0% | 25% |
| 2023-05-28 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,085 | 100.0% | 26% | 1,946 | 1.4% | 32% |
| 2023-05-28 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,950 | 100.0% | 28% | 1,559 | 1.8% | 33% |
| 2023-05-28 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,156 | 100.0% | 30% | 1,118 | 2.3% | 36% |
| 2023-05-28 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 701 | 100.0% | 68% | 210 | 11.0% | 45% |
| 2023-05-28 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 138 | 100.0% | 83% | 211 | 12.3% | 35% |
| 2023-05-28 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,651 | 100.0% | 28% | 2,097 | 0.0% | 32% |
| 2023-05-28 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,159 | 100.0% | 31% | 1,260 | 0.0% | 36% |
| 2023-05-28 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,711 | 100.0% | 37% | 812 | 0.0% | 38% |
| 2023-05-28 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 671 | 100.0% | 76% | 184 | 0.6% | 41% |
| 2023-05-28 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 129 | 100.0% | 81% | 222 | 3.1% | 40% |
| 2023-05-29 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,248 | 100.0% | 21% | 2,692 | 0.1% | 33% |
| 2023-05-29 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,972 | 100.0% | 22% | 1,890 | 0.0% | 35% |
| 2023-05-29 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,842 | 100.0% | 26% | 1,492 | 0.0% | 37% |
| 2023-05-29 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 377 | 100.0% | 56% | 222 | 0.0% | 45% |
| 2023-05-29 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 13 | 100.0% | 77% | 128 | 0.0% | 54% |
| 2023-05-29 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,583 | 100.0% | 21% | 2,626 | 0.0% | 30% |
| 2023-05-29 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,605 | 100.0% | 22% | 1,804 | 0.0% | 32% |
| 2023-05-29 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,919 | 100.0% | 25% | 1,328 | 0.0% | 36% |
| 2023-05-29 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 409 | 100.0% | 56% | 185 | 0.0% | 49% |
| 2023-05-29 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 17 | 100.0% | 82% | 102 | 0.0% | 41% |
| 2023-05-30 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,240 | 100.0% | 16% | 2,782 | 0.1% | 32% |
| 2023-05-30 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,515 | 100.0% | 22% | 1,656 | 0.0% | 39% |
| 2023-05-30 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,976 | 100.0% | 30% | 1,040 | 0.0% | 43% |
| 2023-05-30 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 84 | 100.0% | 71% | 186 | 0.0% | 50% |
| 2023-05-30 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 5 | 100.0% | 40% | 136 | 0.0% | 60% |
| 2023-05-30 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,844 | 100.0% | 16% | 3,090 | 0.0% | 33% |
| 2023-05-30 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,730 | 100.0% | 22% | 1,589 | 0.0% | 40% |
| 2023-05-30 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,968 | 100.0% | 34% | 947 | 0.0% | 45% |
| 2023-05-30 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 92 | 100.0% | 83% | 148 | 0.0% | 50% |
| 2023-05-30 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 11 | 100.0% | 100% | none resolved | 0.0% | 36% |
| 2023-05-31 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,925 | 100.0% | 20% | 2,306 | 0.0% | 34% |
| 2023-05-31 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,063 | 100.0% | 26% | 1,323 | 0.0% | 40% |
| 2023-05-31 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,399 | 100.0% | 37% | 712 | 0.0% | 43% |
| 2023-05-31 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 407 | 100.0% | 82% | 164 | 0.0% | 44% |
| 2023-05-31 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 65 | 100.0% | 86% | 212 | 0.0% | 42% |
| 2023-05-31 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,289 | 100.0% | 20% | 2,484 | 0.0% | 34% |
| 2023-05-31 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,737 | 100.0% | 27% | 1,192 | 0.0% | 40% |
| 2023-05-31 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,725 | 100.0% | 44% | 508 | 0.0% | 43% |
| 2023-05-31 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 265 | 100.0% | 88% | 187 | 0.0% | 49% |
| 2023-05-31 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 25 | 100.0% | 96% | 110 | 0.0% | 36% |
| 2023-06-01 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,966 | 100.0% | 20% | 2,396 | 0.0% | 32% |
| 2023-06-01 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,104 | 100.0% | 25% | 1,435 | 0.0% | 39% |
| 2023-06-01 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,695 | 100.0% | 36% | 678 | 0.0% | 41% |
| 2023-06-01 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 268 | 100.0% | 80% | 193 | 0.0% | 44% |
| 2023-06-01 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 23 | 100.0% | 65% | 230 | 0.0% | 26% |
| 2023-06-01 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,973 | 100.0% | 22% | 2,270 | 0.0% | 33% |
| 2023-06-01 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,252 | 100.0% | 27% | 1,507 | 0.0% | 36% |
| 2023-06-01 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,104 | 100.0% | 36% | 778 | 0.0% | 40% |
| 2023-06-01 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 262 | 100.0% | 81% | 164 | 0.0% | 50% |
| 2023-06-01 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 23 | 100.0% | 96% | 101 | 0.0% | 48% |
| 2023-06-02 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,933 | 100.0% | 23% | 2,517 | 0.0% | 33% |
| 2023-06-02 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,740 | 100.0% | 26% | 1,344 | 0.0% | 35% |
| 2023-06-02 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,960 | 100.0% | 30% | 942 | 0.0% | 41% |
| 2023-06-02 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 396 | 100.0% | 71% | 138 | 0.0% | 54% |
| 2023-06-02 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 17 | 100.0% | 82% | 652 | 0.0% | 47% |
| 2023-06-02 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 9,165 | 100.0% | 19% | 2,088 | 0.0% | 33% |
| 2023-06-02 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,644 | 100.0% | 30% | 1,213 | 0.0% | 41% |
| 2023-06-02 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,068 | 100.0% | 49% | 572 | 0.0% | 47% |
| 2023-06-02 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 165 | 100.0% | 78% | 135 | 0.0% | 42% |
| 2023-06-02 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 25 | 100.0% | 76% | 356 | 0.0% | 36% |
| 2023-06-03 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,255 | 100.0% | 14% | 6,141 | 0.0% | 33% |
| 2023-06-03 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,852 | 99.9% | 19% | 3,446 | 0.0% | 35% |
| 2023-06-03 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,127 | 100.0% | 28% | 1,792 | 0.2% | 43% |
| 2023-06-03 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 77 | 100.0% | 74% | 142 | 0.0% | 53% |
| 2023-06-03 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 9 | 100.0% | 78% | 270 | 0.0% | 44% |
| 2023-06-03 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,274 | 100.0% | 12% | 5,209 | 0.0% | 33% |
| 2023-06-03 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,429 | 100.0% | 23% | 2,832 | 0.0% | 40% |
| 2023-06-03 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,193 | 100.0% | 36% | 1,133 | 0.0% | 49% |
| 2023-06-03 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 37 | 100.0% | 95% | 114 | 0.0% | 41% |
| 2023-06-03 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 4 | 100.0% | 100% | none resolved | 0.0% | 50% |
| 2023-06-04 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,723 | 100.0% | 15% | 5,121 | 0.0% | 33% |
| 2023-06-04 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,581 | 100.0% | 20% | 2,830 | 0.0% | 39% |
| 2023-06-04 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,752 | 100.0% | 30% | 1,272 | 0.1% | 43% |
| 2023-06-04 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 78 | 100.0% | 81% | 126 | 0.0% | 50% |
| 2023-06-04 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 2 | 100.0% | 100% | none resolved | 0.0% | 0% |
| 2023-06-04 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,596 | 100.0% | 16% | 4,484 | 0.0% | 34% |
| 2023-06-04 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,102 | 100.0% | 22% | 2,140 | 0.0% | 40% |
| 2023-06-04 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,651 | 100.0% | 34% | 890 | 0.0% | 48% |
| 2023-06-04 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 78 | 100.0% | 81% | 138 | 0.0% | 45% |
| 2023-06-04 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 2 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2023-06-05 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,737 | 100.0% | 47% | 1,070 | 0.0% | 37% |
| 2023-06-05 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,903 | 100.0% | 49% | 995 | 0.0% | 39% |
| 2023-06-05 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,855 | 100.0% | 53% | 740 | 0.0% | 40% |
| 2023-06-05 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,426 | 100.0% | 75% | 227 | 0.0% | 45% |
| 2023-06-05 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 1,360 | 100.0% | 89% | 162 | 0.0% | 46% |
| 2023-06-05 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 17,151 | 100.0% | 40% | 1,140 | 0.2% | 37% |
| 2023-06-05 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 14,642 | 100.0% | 49% | 776 | 0.2% | 41% |
| 2023-06-05 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,284 | 100.0% | 61% | 515 | 0.3% | 43% |
| 2023-06-05 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,554 | 100.0% | 86% | 175 | 0.7% | 44% |
| 2023-06-05 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 1,195 | 100.0% | 97% | 136 | 2.7% | 48% |
| 2023-06-06 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,229 | 100.0% | 26% | 1,117 | 0.0% | 33% |
| 2023-06-06 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,803 | 100.0% | 30% | 763 | 0.0% | 37% |
| 2023-06-06 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,693 | 100.0% | 38% | 466 | 0.0% | 42% |
| 2023-06-06 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 933 | 100.0% | 74% | 159 | 0.0% | 50% |
| 2023-06-06 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 44 | 100.0% | 89% | 168 | 0.0% | 45% |
| 2023-06-06 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,004 | 100.0% | 21% | 1,303 | 0.0% | 34% |
| 2023-06-06 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,646 | 100.0% | 31% | 707 | 0.0% | 41% |
| 2023-06-06 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,805 | 100.0% | 48% | 356 | 0.0% | 47% |
| 2023-06-06 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 273 | 100.0% | 81% | 143 | 0.0% | 53% |
| 2023-06-06 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 52 | 100.0% | 73% | 156 | 1.9% | 38% |
| 2023-06-07 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 15,927 | 100.0% | 20% | 1,176 | 0.0% | 33% |
| 2023-06-07 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 13,349 | 100.0% | 28% | 818 | 0.0% | 40% |
| 2023-06-07 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,277 | 100.0% | 39% | 491 | 0.0% | 46% |
| 2023-06-07 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 268 | 100.0% | 77% | 126 | 0.0% | 51% |
| 2023-06-07 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 11 | 100.0% | 91% | 155 | 0.0% | 45% |
| 2023-06-07 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 12,464 | 100.0% | 18% | 1,498 | 0.0% | 34% |
| 2023-06-07 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,837 | 100.0% | 29% | 803 | 0.0% | 41% |
| 2023-06-07 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,858 | 100.0% | 42% | 481 | 0.0% | 46% |
| 2023-06-07 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 155 | 100.0% | 88% | 116 | 0.6% | 42% |
| 2023-06-07 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 14 | 100.0% | 86% | 160 | 0.0% | 50% |
| 2023-06-08 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,734 | 100.0% | 15% | 2,824 | 0.0% | 34% |
| 2023-06-08 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,921 | 100.0% | 21% | 1,589 | 0.0% | 39% |
| 2023-06-08 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,067 | 100.0% | 33% | 756 | 0.0% | 47% |
| 2023-06-08 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 125 | 100.0% | 74% | 115 | 0.0% | 58% |
| 2023-06-08 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 6 | 100.0% | 67% | 154 | 0.0% | 50% |
| 2023-06-08 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,319 | 100.0% | 13% | 3,197 | 0.0% | 35% |
| 2023-06-08 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,723 | 100.0% | 23% | 1,604 | 0.0% | 43% |
| 2023-06-08 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,050 | 100.0% | 39% | 685 | 0.0% | 49% |
| 2023-06-08 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 59 | 100.0% | 88% | 164 | 0.0% | 49% |
| 2023-06-08 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 4 | 100.0% | 100% | none resolved | 0.0% | 50% |
| 2023-06-09 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,900 | 100.0% | 15% | 3,683 | 0.0% | 36% |
| 2023-06-09 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,404 | 100.0% | 21% | 2,682 | 0.0% | 37% |
| 2023-06-09 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,745 | 100.0% | 26% | 1,330 | 0.0% | 44% |
| 2023-06-09 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 85 | 100.0% | 73% | 118 | 0.0% | 49% |
| 2023-06-09 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 8 | 100.0% | 100% | none resolved | 0.0% | 25% |
| 2023-06-09 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,341 | 100.0% | 14% | 4,448 | 0.0% | 35% |
| 2023-06-09 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,178 | 100.0% | 23% | 2,179 | 0.0% | 41% |
| 2023-06-09 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,193 | 100.0% | 36% | 1,026 | 0.0% | 45% |
| 2023-06-09 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 95 | 100.0% | 81% | 123 | 0.0% | 46% |
| 2023-06-09 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 3 | 100.0% | 67% | 154 | 0.0% | 67% |
| 2023-06-10 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,459 | 100.0% | 28% | 1,257 | 0.0% | 33% |
| 2023-06-10 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,266 | 100.0% | 32% | 852 | 0.0% | 37% |
| 2023-06-10 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 9,181 | 100.0% | 37% | 504 | 0.0% | 38% |
| 2023-06-10 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,306 | 100.0% | 64% | 172 | 0.0% | 50% |
| 2023-06-10 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 30 | 100.0% | 80% | 216 | 0.0% | 47% |
| 2023-06-10 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 21,793 | 100.0% | 27% | 943 | 0.1% | 34% |
| 2023-06-10 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 18,069 | 100.0% | 34% | 638 | 0.1% | 38% |
| 2023-06-10 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,736 | 100.0% | 45% | 382 | 0.1% | 43% |
| 2023-06-10 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 943 | 100.0% | 80% | 149 | 0.7% | 51% |
| 2023-06-10 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 80 | 100.0% | 89% | 130 | 1.2% | 48% |
| 2023-06-11 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,966 | 100.0% | 16% | 3,006 | 0.0% | 34% |
| 2023-06-11 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,907 | 100.0% | 24% | 1,490 | 0.0% | 43% |
| 2023-06-11 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,736 | 100.0% | 37% | 722 | 0.0% | 48% |
| 2023-06-11 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 60 | 100.0% | 90% | 130 | 0.0% | 38% |
| 2023-06-11 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 0% |
| 2023-06-11 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,461 | 100.0% | 19% | 3,300 | 0.0% | 32% |
| 2023-06-11 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,774 | 100.0% | 22% | 2,154 | 0.0% | 36% |
| 2023-06-11 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,208 | 100.0% | 31% | 1,364 | 0.0% | 43% |
| 2023-06-11 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 100 | 100.0% | 82% | 112 | 0.0% | 42% |
| 2023-06-11 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 6 | 100.0% | 100% | none resolved | 0.0% | 67% |
| 2023-06-12 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,479 | 100.0% | 17% | 2,659 | 0.0% | 34% |
| 2023-06-12 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,035 | 100.0% | 23% | 1,480 | 0.0% | 42% |
| 2023-06-12 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,564 | 100.0% | 35% | 746 | 0.0% | 48% |
| 2023-06-12 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 52 | 100.0% | 79% | 117 | 0.0% | 58% |
| 2023-06-12 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 0% |
| 2023-06-12 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,605 | 100.0% | 21% | 1,882 | 0.0% | 33% |
| 2023-06-12 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,639 | 100.0% | 28% | 1,162 | 0.0% | 38% |
| 2023-06-12 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,459 | 100.0% | 38% | 659 | 0.0% | 45% |
| 2023-06-12 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 110 | 100.0% | 81% | 117 | 0.0% | 54% |
| 2023-06-12 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 4 | 100.0% | 50% | 124 | 0.0% | 75% |
| 2023-06-13 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 9,451 | 100.0% | 25% | 1,968 | 0.0% | 34% |
| 2023-06-13 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,652 | 100.0% | 27% | 1,286 | 0.0% | 38% |
| 2023-06-13 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,975 | 100.0% | 35% | 727 | 0.0% | 44% |
| 2023-06-13 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 263 | 100.0% | 84% | 122 | 0.0% | 53% |
| 2023-06-13 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 22 | 100.0% | 95% | 171 | 0.0% | 36% |
| 2023-06-13 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,839 | 100.0% | 24% | 1,474 | 0.0% | 33% |
| 2023-06-13 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,864 | 100.0% | 31% | 814 | 0.0% | 36% |
| 2023-06-13 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,527 | 100.0% | 42% | 420 | 0.0% | 42% |
| 2023-06-13 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 280 | 100.0% | 84% | 169 | 0.0% | 45% |
| 2023-06-13 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 32 | 100.0% | 88% | 210 | 0.0% | 38% |
| 2023-06-14 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,775 | 100.0% | 27% | 1,118 | 0.0% | 34% |
| 2023-06-14 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,348 | 100.0% | 35% | 707 | 0.1% | 41% |
| 2023-06-14 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,134 | 100.0% | 46% | 409 | 0.1% | 45% |
| 2023-06-14 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 678 | 100.0% | 82% | 190 | 0.4% | 48% |
| 2023-06-14 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 130 | 100.0% | 88% | 248 | 0.0% | 42% |
| 2023-06-14 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 15,725 | 100.0% | 32% | 885 | 0.0% | 33% |
| 2023-06-14 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,940 | 100.0% | 40% | 550 | 0.0% | 37% |
| 2023-06-14 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,831 | 100.0% | 53% | 308 | 0.0% | 41% |
| 2023-06-14 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,069 | 100.0% | 84% | 168 | 0.0% | 44% |
| 2023-06-14 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 329 | 100.0% | 82% | 216 | 0.6% | 42% |
| 2023-06-15 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,613 | 100.0% | 16% | 2,028 | 0.0% | 35% |
| 2023-06-15 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,917 | 100.0% | 22% | 1,214 | 0.0% | 43% |
| 2023-06-15 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,604 | 100.0% | 32% | 692 | 0.0% | 49% |
| 2023-06-15 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 145 | 100.0% | 79% | 119 | 0.0% | 50% |
| 2023-06-15 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 7 | 100.0% | 100% | none resolved | 0.0% | 29% |
| 2023-06-15 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,672 | 100.0% | 20% | 1,549 | 0.0% | 31% |
| 2023-06-15 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,550 | 100.0% | 26% | 1,023 | 0.0% | 37% |
| 2023-06-15 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,844 | 100.0% | 37% | 696 | 0.0% | 45% |
| 2023-06-15 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 134 | 100.0% | 81% | 122 | 0.0% | 56% |
| 2023-06-15 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 7 | 100.0% | 57% | 134 | 0.0% | 86% |
| 2023-06-16 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,363 | 100.0% | 27% | 1,554 | 0.0% | 35% |
| 2023-06-16 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,820 | 100.0% | 29% | 1,101 | 0.0% | 38% |
| 2023-06-16 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,114 | 100.0% | 35% | 923 | 0.0% | 39% |
| 2023-06-16 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 638 | 100.0% | 70% | 144 | 0.0% | 49% |
| 2023-06-16 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 28 | 100.0% | 82% | 196 | 0.0% | 61% |
| 2023-06-16 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,886 | 100.0% | 26% | 1,387 | 0.0% | 33% |
| 2023-06-16 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,114 | 100.0% | 32% | 1,058 | 0.0% | 38% |
| 2023-06-16 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,137 | 100.0% | 44% | 593 | 0.0% | 42% |
| 2023-06-16 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 245 | 100.0% | 84% | 132 | 0.0% | 46% |
| 2023-06-16 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 12 | 100.0% | 100% | none resolved | 0.0% | 33% |
| 2023-06-17 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,473 | 100.0% | 20% | 2,781 | 0.0% | 35% |
| 2023-06-17 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,876 | 100.0% | 24% | 1,782 | 0.0% | 39% |
| 2023-06-17 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,323 | 100.0% | 32% | 1,454 | 0.0% | 41% |
| 2023-06-17 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 326 | 100.0% | 81% | 135 | 0.0% | 48% |
| 2023-06-17 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 32 | 100.0% | 88% | 274 | 0.0% | 50% |
| 2023-06-17 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,548 | 100.0% | 24% | 2,612 | 0.0% | 33% |
| 2023-06-17 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,410 | 100.0% | 30% | 1,410 | 0.0% | 37% |
| 2023-06-17 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,220 | 100.0% | 45% | 634 | 0.0% | 42% |
| 2023-06-17 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 366 | 100.0% | 81% | 176 | 0.0% | 48% |
| 2023-06-17 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 167 | 100.0% | 84% | 245 | 0.0% | 41% |
| 2023-06-18 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,903 | 100.0% | 18% | 3,238 | 0.0% | 36% |
| 2023-06-18 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,268 | 100.0% | 23% | 2,088 | 0.0% | 42% |
| 2023-06-18 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,394 | 100.0% | 34% | 1,378 | 0.0% | 46% |
| 2023-06-18 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 110 | 100.0% | 86% | 129 | 0.0% | 40% |
| 2023-06-18 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 7 | 100.0% | 100% | none resolved | 0.0% | 43% |
| 2023-06-18 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,788 | 100.0% | 23% | 2,894 | 0.0% | 34% |
| 2023-06-18 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,844 | 100.0% | 30% | 1,922 | 0.0% | 38% |
| 2023-06-18 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,569 | 100.0% | 40% | 1,083 | 0.0% | 45% |
| 2023-06-18 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 108 | 100.0% | 87% | 154 | 0.0% | 38% |
| 2023-06-18 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 9 | 100.0% | 89% | 120 | 0.0% | 33% |
| 2023-06-19 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,866 | 100.0% | 26% | 1,503 | 0.0% | 35% |
| 2023-06-19 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,910 | 100.0% | 30% | 1,076 | 0.0% | 40% |
| 2023-06-19 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,579 | 100.0% | 40% | 723 | 0.0% | 44% |
| 2023-06-19 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 416 | 100.0% | 80% | 137 | 0.0% | 48% |
| 2023-06-19 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 45 | 100.0% | 93% | 240 | 0.0% | 51% |
| 2023-06-19 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 9,398 | 100.0% | 27% | 1,470 | 0.0% | 34% |
| 2023-06-19 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,739 | 100.0% | 35% | 910 | 0.0% | 39% |
| 2023-06-19 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,440 | 100.0% | 49% | 416 | 0.0% | 44% |
| 2023-06-19 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 311 | 100.0% | 90% | 165 | 0.0% | 43% |
| 2023-06-19 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 52 | 100.0% | 81% | 230 | 0.0% | 40% |
| 2023-06-20 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,465 | 100.0% | 29% | 1,064 | 0.0% | 35% |
| 2023-06-20 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,578 | 100.0% | 34% | 789 | 0.0% | 38% |
| 2023-06-20 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,824 | 100.0% | 41% | 623 | 0.0% | 41% |
| 2023-06-20 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,527 | 100.0% | 60% | 294 | 0.0% | 46% |
| 2023-06-20 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 74 | 100.0% | 92% | 121 | 0.0% | 53% |
| 2023-06-20 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,766 | 100.0% | 27% | 1,483 | 0.0% | 33% |
| 2023-06-20 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,555 | 100.0% | 33% | 934 | 0.0% | 37% |
| 2023-06-20 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,165 | 100.0% | 41% | 652 | 0.0% | 40% |
| 2023-06-20 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 425 | 100.0% | 85% | 124 | 0.0% | 48% |
| 2023-06-20 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 13 | 100.0% | 92% | 105 | 0.0% | 31% |
| 2023-06-21 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 23,141 | 100.0% | 32% | 854 | 0.1% | 35% |
| 2023-06-21 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 21,633 | 100.0% | 36% | 610 | 0.1% | 38% |
| 2023-06-21 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 16,475 | 100.0% | 43% | 394 | 0.1% | 40% |
| 2023-06-21 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,498 | 100.0% | 74% | 156 | 0.7% | 44% |
| 2023-06-21 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 261 | 100.0% | 88% | 144 | 3.1% | 42% |
| 2023-06-21 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 16,951 | 100.0% | 29% | 1,043 | 0.0% | 32% |
| 2023-06-21 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 14,983 | 100.0% | 35% | 724 | 0.0% | 36% |
| 2023-06-21 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,953 | 100.0% | 41% | 516 | 0.0% | 37% |
| 2023-06-21 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,535 | 100.0% | 77% | 156 | 0.0% | 48% |
| 2023-06-21 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 90 | 100.0% | 86% | 182 | 0.0% | 54% |
| 2023-06-22 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,483 | 100.0% | 25% | 1,217 | 0.0% | 34% |
| 2023-06-22 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,611 | 100.0% | 30% | 926 | 0.0% | 39% |
| 2023-06-22 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,129 | 100.0% | 38% | 689 | 0.0% | 44% |
| 2023-06-22 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 399 | 100.0% | 82% | 118 | 0.0% | 47% |
| 2023-06-22 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 41 | 100.0% | 95% | 364 | 0.0% | 39% |
| 2023-06-22 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,709 | 100.0% | 25% | 1,416 | 0.0% | 32% |
| 2023-06-22 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,386 | 100.0% | 31% | 1,011 | 0.0% | 35% |
| 2023-06-22 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,722 | 100.0% | 34% | 741 | 0.0% | 37% |
| 2023-06-22 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 537 | 100.0% | 68% | 171 | 0.0% | 45% |
| 2023-06-22 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 16 | 100.0% | 81% | 176 | 0.0% | 25% |
| 2023-06-23 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 17,944 | 100.0% | 30% | 869 | 0.2% | 34% |
| 2023-06-23 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 16,614 | 100.0% | 34% | 707 | 0.2% | 36% |
| 2023-06-23 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,737 | 100.0% | 43% | 499 | 0.3% | 42% |
| 2023-06-23 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,620 | 100.0% | 81% | 148 | 2.5% | 45% |
| 2023-06-23 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 496 | 100.0% | 93% | 137 | 11.3% | 48% |
| 2023-06-23 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,226 | 100.0% | 30% | 1,196 | 0.0% | 30% |
| 2023-06-23 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,267 | 100.0% | 28% | 737 | 0.0% | 31% |
| 2023-06-23 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,991 | 100.0% | 33% | 458 | 0.0% | 37% |
| 2023-06-23 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 813 | 100.0% | 77% | 134 | 0.0% | 48% |
| 2023-06-23 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 37 | 100.0% | 78% | 175 | 0.0% | 24% |
| 2023-06-24 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,770 | 100.0% | 19% | 3,784 | 0.0% | 34% |
| 2023-06-24 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,478 | 100.0% | 22% | 2,224 | 0.0% | 37% |
| 2023-06-24 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,968 | 100.0% | 26% | 1,370 | 0.0% | 40% |
| 2023-06-24 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 213 | 100.0% | 75% | 132 | 0.0% | 53% |
| 2023-06-24 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 6 | 100.0% | 67% | 118 | 0.0% | 50% |
| 2023-06-24 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,091 | 100.0% | 21% | 1,711 | 0.0% | 32% |
| 2023-06-24 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,098 | 100.0% | 26% | 1,609 | 0.0% | 35% |
| 2023-06-24 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,957 | 100.0% | 27% | 1,300 | 0.0% | 33% |
| 2023-06-24 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 245 | 100.0% | 67% | 168 | 0.0% | 48% |
| 2023-06-24 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 7 | 100.0% | 86% | 102 | 0.0% | 57% |
| 2023-06-25 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,399 | 100.0% | 15% | 2,454 | 0.0% | 32% |
| 2023-06-25 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,613 | 100.0% | 22% | 1,815 | 0.0% | 41% |
| 2023-06-25 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,617 | 100.0% | 30% | 1,230 | 0.0% | 46% |
| 2023-06-25 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 93 | 100.0% | 82% | 121 | 0.0% | 40% |
| 2023-06-25 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 6 | 100.0% | 83% | 126 | 0.0% | 67% |
| 2023-06-25 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,015 | 100.0% | 21% | 2,149 | 0.0% | 32% |
| 2023-06-25 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,844 | 100.0% | 23% | 1,419 | 0.0% | 32% |
| 2023-06-25 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,202 | 100.0% | 28% | 938 | 0.0% | 36% |
| 2023-06-25 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 371 | 100.0% | 72% | 161 | 0.0% | 49% |
| 2023-06-25 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 7 | 100.0% | 86% | 121 | 0.0% | 71% |
| 2023-06-26 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,984 | 100.0% | 23% | 1,540 | 0.0% | 33% |
| 2023-06-26 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,193 | 100.0% | 27% | 1,022 | 0.0% | 39% |
| 2023-06-26 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,959 | 100.0% | 35% | 722 | 0.0% | 44% |
| 2023-06-26 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 397 | 100.0% | 79% | 146 | 0.0% | 47% |
| 2023-06-26 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 65 | 100.0% | 94% | 120 | 0.0% | 43% |
| 2023-06-26 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,252 | 100.0% | 29% | 1,448 | 0.0% | 31% |
| 2023-06-26 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,054 | 100.0% | 29% | 973 | 0.0% | 32% |
| 2023-06-26 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,859 | 100.0% | 34% | 588 | 0.0% | 39% |
| 2023-06-26 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 442 | 100.0% | 84% | 132 | 0.0% | 50% |
| 2023-06-26 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 44 | 100.0% | 82% | 128 | 0.0% | 50% |
| 2023-06-27 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,498 | 100.0% | 21% | 1,956 | 0.0% | 35% |
| 2023-06-27 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,555 | 100.0% | 24% | 1,462 | 0.0% | 39% |
| 2023-06-27 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,196 | 100.0% | 30% | 975 | 0.0% | 43% |
| 2023-06-27 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 243 | 100.0% | 74% | 135 | 0.0% | 49% |
| 2023-06-27 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 23 | 100.0% | 83% | 109 | 0.0% | 65% |
| 2023-06-27 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,270 | 100.0% | 19% | 1,964 | 0.0% | 33% |
| 2023-06-27 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,788 | 100.0% | 27% | 1,179 | 0.0% | 36% |
| 2023-06-27 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,279 | 100.0% | 36% | 693 | 0.0% | 40% |
| 2023-06-27 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 132 | 100.0% | 89% | 130 | 0.0% | 52% |
| 2023-06-27 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 3 | 100.0% | 67% | 240 | 0.0% | 33% |
| 2023-06-28 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 9,810 | 100.0% | 20% | 1,892 | 0.0% | 35% |
| 2023-06-28 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,231 | 100.0% | 26% | 1,259 | 0.0% | 39% |
| 2023-06-28 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,992 | 100.0% | 35% | 830 | 0.0% | 45% |
| 2023-06-28 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 298 | 100.0% | 77% | 152 | 0.0% | 45% |
| 2023-06-28 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 15 | 100.0% | 67% | 285 | 0.0% | 33% |
| 2023-06-28 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,745 | 100.0% | 22% | 1,600 | 0.0% | 33% |
| 2023-06-28 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,631 | 100.0% | 32% | 966 | 0.0% | 38% |
| 2023-06-28 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,179 | 100.0% | 47% | 434 | 0.0% | 46% |
| 2023-06-28 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 330 | 100.0% | 80% | 172 | 0.0% | 46% |
| 2023-06-28 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 33 | 100.0% | 85% | 124 | 0.0% | 55% |
| 2023-06-29 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,575 | 100.0% | 17% | 2,336 | 0.0% | 35% |
| 2023-06-29 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,580 | 100.0% | 23% | 1,504 | 0.0% | 40% |
| 2023-06-29 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,124 | 100.0% | 32% | 976 | 0.0% | 47% |
| 2023-06-29 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 127 | 100.0% | 76% | 144 | 0.0% | 47% |
| 2023-06-29 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 9 | 100.0% | 67% | 149 | 0.0% | 56% |
| 2023-06-29 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,128 | 100.0% | 19% | 2,057 | 0.0% | 32% |
| 2023-06-29 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,716 | 100.0% | 28% | 1,149 | 0.0% | 40% |
| 2023-06-29 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,403 | 100.0% | 41% | 555 | 0.0% | 47% |
| 2023-06-29 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 61 | 100.0% | 80% | 126 | 0.0% | 51% |
| 2023-06-29 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 3 | 100.0% | 100% | none resolved | 0.0% | 67% |
| 2023-06-30 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 16,233 | 100.0% | 33% | 886 | 0.0% | 36% |
| 2023-06-30 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 15,006 | 100.0% | 36% | 716 | 0.0% | 38% |
| 2023-06-30 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,589 | 100.0% | 42% | 540 | 0.0% | 41% |
| 2023-06-30 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,058 | 100.0% | 58% | 264 | 0.0% | 43% |
| 2023-06-30 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 475 | 100.0% | 78% | 167 | 0.0% | 42% |
| 2023-06-30 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 25,172 | 100.0% | 31% | 860 | 0.0% | 33% |
| 2023-06-30 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 21,975 | 100.0% | 37% | 576 | 0.0% | 37% |
| 2023-06-30 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 13,964 | 100.0% | 46% | 349 | 0.0% | 40% |
| 2023-06-30 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,225 | 100.0% | 80% | 174 | 0.0% | 45% |
| 2023-06-30 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 130 | 100.0% | 81% | 146 | 0.0% | 48% |
| 2023-07-01 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,372 | 99.8% | 12% | 9,748 | 0.0% | 37% |
| 2023-07-01 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,060 | 99.9% | 18% | 5,930 | 0.1% | 45% |
| 2023-07-01 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,193 | 100.0% | 23% | 2,286 | 0.1% | 48% |
| 2023-07-01 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 29 | 100.0% | 79% | 114 | 0.0% | 55% |
| 2023-07-01 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,093 | 100.0% | 16% | 3,012 | 0.0% | 32% |
| 2023-07-01 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,561 | 100.0% | 23% | 2,062 | 0.0% | 38% |
| 2023-07-01 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,689 | 100.0% | 33% | 922 | 0.0% | 46% |
| 2023-07-01 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 50 | 100.0% | 86% | 112 | 0.0% | 60% |
| 2023-07-02 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,802 | 100.0% | 28% | 3,798 | 0.0% | 34% |
| 2023-07-02 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,807 | 100.0% | 26% | 2,171 | 0.0% | 32% |
| 2023-07-02 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,550 | 100.0% | 28% | 1,294 | 0.0% | 38% |
| 2023-07-02 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 419 | 100.0% | 65% | 169 | 0.0% | 46% |
| 2023-07-02 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 37 | 100.0% | 59% | 185 | 0.0% | 24% |
| 2023-07-02 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,969 | 100.0% | 27% | 1,963 | 0.0% | 32% |
| 2023-07-02 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,728 | 100.0% | 31% | 1,114 | 0.0% | 35% |
| 2023-07-02 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,410 | 100.0% | 39% | 639 | 0.0% | 38% |
| 2023-07-02 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 682 | 100.0% | 77% | 156 | 0.0% | 44% |
| 2023-07-02 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 152 | 100.0% | 86% | 164 | 0.0% | 36% |
| 2023-07-03 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,099 | 100.0% | 26% | 1,771 | 0.0% | 32% |
| 2023-07-03 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,852 | 100.0% | 29% | 1,614 | 0.0% | 34% |
| 2023-07-03 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,039 | 100.0% | 29% | 1,098 | 0.0% | 37% |
| 2023-07-03 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 543 | 100.0% | 52% | 418 | 0.0% | 52% |
| 2023-07-03 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 29 | 100.0% | 86% | 364 | 0.0% | 45% |
| 2023-07-03 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,432 | 100.0% | 21% | 2,946 | 0.0% | 33% |
| 2023-07-03 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,850 | 100.0% | 25% | 1,775 | 0.0% | 36% |
| 2023-07-03 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,133 | 100.0% | 29% | 975 | 0.0% | 35% |
| 2023-07-03 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 714 | 100.0% | 56% | 229 | 0.0% | 48% |
| 2023-07-03 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 34 | 100.0% | 82% | 121 | 0.0% | 65% |
| 2023-07-04 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,015 | 100.0% | 20% | 3,365 | 0.0% | 33% |
| 2023-07-04 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,561 | 100.0% | 24% | 2,397 | 0.0% | 36% |
| 2023-07-04 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,917 | 100.0% | 30% | 1,366 | 0.0% | 43% |
| 2023-07-04 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 157 | 100.0% | 64% | 148 | 0.0% | 53% |
| 2023-07-04 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 16 | 100.0% | 88% | 650 | 0.0% | 50% |
| 2023-07-04 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,230 | 100.0% | 21% | 3,669 | 0.0% | 32% |
| 2023-07-04 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,217 | 100.0% | 22% | 2,415 | 0.0% | 31% |
| 2023-07-04 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,491 | 100.0% | 25% | 1,531 | 0.0% | 34% |
| 2023-07-04 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 312 | 100.0% | 60% | 269 | 0.0% | 45% |
| 2023-07-04 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 12 | 100.0% | 67% | 178 | 0.0% | 25% |
| 2023-07-05 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,258 | 100.0% | 24% | 2,651 | 0.0% | 33% |
| 2023-07-05 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,714 | 100.0% | 24% | 1,858 | 0.0% | 36% |
| 2023-07-05 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,120 | 100.0% | 32% | 1,157 | 0.0% | 41% |
| 2023-07-05 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 135 | 100.0% | 69% | 176 | 0.0% | 45% |
| 2023-07-05 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 8 | 100.0% | 88% | 294 | 0.0% | 38% |
| 2023-07-05 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,677 | 100.0% | 25% | 2,045 | 0.0% | 34% |
| 2023-07-05 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,887 | 100.0% | 28% | 1,363 | 0.0% | 34% |
| 2023-07-05 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,512 | 100.0% | 30% | 918 | 0.0% | 36% |
| 2023-07-05 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 351 | 100.0% | 73% | 204 | 0.0% | 45% |
| 2023-07-05 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 38 | 100.0% | 82% | 140 | 0.0% | 45% |
| 2023-07-06 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,102 | 100.0% | 24% | 1,379 | 0.0% | 33% |
| 2023-07-06 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,404 | 100.0% | 31% | 868 | 0.0% | 38% |
| 2023-07-06 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,570 | 100.0% | 38% | 577 | 0.0% | 43% |
| 2023-07-06 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,262 | 100.0% | 55% | 196 | 0.1% | 41% |
| 2023-07-06 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 57 | 100.0% | 79% | 126 | 0.0% | 44% |
| 2023-07-06 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 12,885 | 100.0% | 26% | 1,432 | 0.0% | 32% |
| 2023-07-06 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,746 | 100.0% | 30% | 1,013 | 0.0% | 34% |
| 2023-07-06 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,219 | 100.0% | 36% | 582 | 0.0% | 38% |
| 2023-07-06 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 800 | 100.0% | 65% | 160 | 0.0% | 47% |
| 2023-07-06 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 18 | 100.0% | 83% | 113 | 0.0% | 56% |
| 2023-07-07 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,136 | 100.0% | 20% | 2,474 | 0.0% | 33% |
| 2023-07-07 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,206 | 100.0% | 25% | 1,474 | 0.0% | 39% |
| 2023-07-07 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,617 | 100.0% | 32% | 959 | 0.0% | 44% |
| 2023-07-07 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 108 | 100.0% | 88% | 121 | 0.0% | 45% |
| 2023-07-07 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 4 | 100.0% | 75% | 122 | 0.0% | 50% |
| 2023-07-07 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,699 | 100.0% | 24% | 1,975 | 0.0% | 31% |
| 2023-07-07 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,608 | 100.0% | 28% | 1,514 | 0.0% | 35% |
| 2023-07-07 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,685 | 100.0% | 41% | 764 | 0.0% | 44% |
| 2023-07-07 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 45 | 100.0% | 91% | 166 | 0.0% | 53% |
| 2023-07-07 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 2 | 100.0% | 100% | none resolved | 0.0% | 50% |
| 2023-07-08 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,867 | 99.9% | 15% | 10,760 | 0.0% | 34% |
| 2023-07-08 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,438 | 100.0% | 18% | 7,465 | 0.0% | 39% |
| 2023-07-08 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 920 | 100.0% | 23% | 3,825 | 0.0% | 44% |
| 2023-07-08 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 39 | 100.0% | 64% | 130 | 0.0% | 46% |
| 2023-07-08 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 3 | 100.0% | 100% | none resolved | 0.0% | 67% |
| 2023-07-08 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,675 | 100.0% | 17% | 5,063 | 0.0% | 32% |
| 2023-07-08 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,001 | 100.0% | 23% | 3,608 | 0.0% | 39% |
| 2023-07-08 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,418 | 100.0% | 35% | 1,914 | 0.0% | 45% |
| 2023-07-08 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 40 | 100.0% | 88% | 117 | 0.0% | 57% |
| 2023-07-08 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 4 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2023-07-09 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,212 | 100.0% | 13% | 8,122 | 0.0% | 31% |
| 2023-07-09 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,982 | 100.0% | 20% | 5,140 | 0.0% | 39% |
| 2023-07-09 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,174 | 100.0% | 28% | 2,832 | 0.0% | 45% |
| 2023-07-09 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 51 | 100.0% | 65% | 118 | 0.0% | 59% |
| 2023-07-09 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2023-07-09 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,884 | 100.0% | 15% | 3,395 | 0.0% | 33% |
| 2023-07-09 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,701 | 100.0% | 25% | 1,918 | 0.0% | 42% |
| 2023-07-09 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,607 | 100.0% | 42% | 1,060 | 0.0% | 48% |
| 2023-07-09 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 36 | 100.0% | 89% | 149 | 0.0% | 44% |
| 2023-07-09 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 0% | 109 | 0.0% | 100% |
| 2023-07-10 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,974 | 100.0% | 20% | 2,816 | 0.0% | 34% |
| 2023-07-10 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,858 | 100.0% | 26% | 1,724 | 0.1% | 39% |
| 2023-07-10 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,627 | 100.0% | 34% | 1,016 | 0.1% | 41% |
| 2023-07-10 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 538 | 100.0% | 42% | 609 | 0.0% | 42% |
| 2023-07-10 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 22 | 100.0% | 68% | 178 | 0.0% | 23% |
| 2023-07-10 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,471 | 100.0% | 20% | 2,569 | 0.0% | 31% |
| 2023-07-10 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,792 | 100.0% | 26% | 1,410 | 0.0% | 38% |
| 2023-07-10 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,564 | 100.0% | 36% | 762 | 0.0% | 43% |
| 2023-07-10 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 60 | 100.0% | 82% | 164 | 0.0% | 42% |
| 2023-07-10 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 0% |
| 2023-07-11 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,670 | 100.0% | 15% | 3,312 | 0.0% | 35% |
| 2023-07-11 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,573 | 100.0% | 20% | 2,383 | 0.0% | 41% |
| 2023-07-11 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,570 | 100.0% | 33% | 1,153 | 0.0% | 47% |
| 2023-07-11 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 90 | 100.0% | 70% | 133 | 0.0% | 33% |
| 2023-07-11 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 3 | 100.0% | 67% | 119 | 0.0% | 67% |
| 2023-07-11 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,049 | 100.0% | 18% | 3,157 | 0.0% | 31% |
| 2023-07-11 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,295 | 100.0% | 21% | 1,685 | 0.0% | 36% |
| 2023-07-11 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,281 | 100.0% | 32% | 1,124 | 0.0% | 42% |
| 2023-07-11 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 47 | 100.0% | 79% | 126 | 0.0% | 57% |
| 2023-07-11 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 6 | 100.0% | 83% | 136 | 0.0% | 83% |
| 2023-07-12 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,291 | 100.0% | 24% | 2,518 | 0.0% | 33% |
| 2023-07-12 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,567 | 100.0% | 27% | 1,493 | 0.1% | 38% |
| 2023-07-12 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,645 | 100.0% | 36% | 704 | 0.0% | 43% |
| 2023-07-12 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 430 | 100.0% | 80% | 158 | 0.0% | 41% |
| 2023-07-12 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 35 | 100.0% | 86% | 144 | 0.0% | 49% |
| 2023-07-12 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,124 | 100.0% | 23% | 2,404 | 0.0% | 31% |
| 2023-07-12 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,696 | 100.0% | 24% | 1,714 | 0.0% | 32% |
| 2023-07-12 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,588 | 100.0% | 28% | 813 | 0.0% | 35% |
| 2023-07-12 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 266 | 100.0% | 78% | 152 | 0.0% | 40% |
| 2023-07-12 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 26 | 100.0% | 81% | 170 | 0.0% | 42% |
| 2023-07-13 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,854 | 100.0% | 27% | 1,145 | 0.0% | 32% |
| 2023-07-13 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,640 | 100.0% | 32% | 867 | 0.0% | 35% |
| 2023-07-13 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,786 | 100.0% | 37% | 563 | 0.0% | 38% |
| 2023-07-13 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,078 | 100.0% | 67% | 230 | 0.0% | 45% |
| 2023-07-13 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 48 | 100.0% | 98% | 102 | 0.0% | 44% |
| 2023-07-13 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,038 | 100.0% | 34% | 944 | 0.0% | 32% |
| 2023-07-13 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,269 | 100.0% | 35% | 844 | 0.0% | 33% |
| 2023-07-13 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,146 | 100.0% | 39% | 788 | 0.0% | 36% |
| 2023-07-13 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,069 | 100.0% | 80% | 148 | 0.8% | 47% |
| 2023-07-13 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 75 | 100.0% | 85% | 261 | 0.0% | 43% |
| 2023-07-14 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,989 | 100.0% | 26% | 1,384 | 0.0% | 33% |
| 2023-07-14 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,281 | 100.0% | 32% | 912 | 0.0% | 37% |
| 2023-07-14 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,413 | 100.0% | 40% | 834 | 0.0% | 42% |
| 2023-07-14 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 361 | 100.0% | 74% | 148 | 0.0% | 37% |
| 2023-07-14 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 22 | 100.0% | 73% | 190 | 0.0% | 45% |
| 2023-07-14 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,955 | 100.0% | 29% | 1,094 | 0.0% | 31% |
| 2023-07-14 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 13,362 | 100.0% | 33% | 734 | 0.0% | 33% |
| 2023-07-14 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,070 | 100.0% | 42% | 798 | 0.0% | 39% |
| 2023-07-14 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 507 | 100.0% | 68% | 319 | 0.0% | 41% |
| 2023-07-14 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 11 | 100.0% | 100% | none resolved | 0.0% | 45% |
| 2023-07-15 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,479 | 99.9% | 9% | 22,277 | 0.0% | 33% |
| 2023-07-15 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,214 | 99.9% | 13% | 9,499 | 0.0% | 41% |
| 2023-07-15 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 625 | 99.8% | 24% | 4,636 | 0.0% | 48% |
| 2023-07-15 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 7 | 100.0% | 86% | 240 | 0.0% | 43% |
| 2023-07-15 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 0% | 206 | 0.0% | 0% |
| 2023-07-15 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,906 | 100.0% | 16% | 8,536 | 0.0% | 30% |
| 2023-07-15 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,512 | 100.0% | 22% | 4,640 | 0.0% | 36% |
| 2023-07-15 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,185 | 100.0% | 33% | 2,265 | 0.0% | 44% |
| 2023-07-15 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 21 | 100.0% | 71% | 109 | 0.0% | 57% |
| 2023-07-16 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,398 | 100.0% | 15% | 5,189 | 0.0% | 32% |
| 2023-07-16 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,478 | 100.0% | 22% | 2,702 | 0.0% | 41% |
| 2023-07-16 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,115 | 100.0% | 41% | 1,088 | 0.0% | 45% |
| 2023-07-16 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 37 | 100.0% | 76% | 256 | 0.0% | 43% |
| 2023-07-16 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 6 | 100.0% | 33% | 211 | 0.0% | 17% |
| 2023-07-16 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,070 | 100.0% | 18% | 4,025 | 0.0% | 31% |
| 2023-07-16 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,496 | 100.0% | 31% | 1,972 | 0.0% | 40% |
| 2023-07-16 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,396 | 100.0% | 46% | 1,052 | 0.0% | 44% |
| 2023-07-16 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 46 | 100.0% | 74% | 144 | 0.0% | 48% |
| 2023-07-16 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 5 | 100.0% | 100% | none resolved | 0.0% | 20% |
| 2023-07-17 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,632 | 100.0% | 22% | 2,567 | 0.0% | 29% |
| 2023-07-17 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,578 | 100.0% | 25% | 1,948 | 0.0% | 35% |
| 2023-07-17 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,602 | 100.0% | 32% | 967 | 0.0% | 42% |
| 2023-07-17 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 144 | 100.0% | 82% | 144 | 0.0% | 47% |
| 2023-07-17 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 15 | 100.0% | 67% | 194 | 0.0% | 20% |
| 2023-07-17 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 9,228 | 100.0% | 23% | 2,066 | 0.0% | 30% |
| 2023-07-17 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,578 | 100.0% | 27% | 1,048 | 0.0% | 35% |
| 2023-07-17 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,607 | 100.0% | 40% | 519 | 0.0% | 43% |
| 2023-07-17 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 130 | 100.0% | 76% | 169 | 0.0% | 31% |
| 2023-07-17 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 18 | 100.0% | 78% | 206 | 0.0% | 33% |
| 2023-07-18 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,890 | 100.0% | 20% | 2,854 | 0.0% | 33% |
| 2023-07-18 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,663 | 100.0% | 25% | 1,943 | 0.0% | 39% |
| 2023-07-18 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,650 | 100.0% | 33% | 1,148 | 0.0% | 45% |
| 2023-07-18 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 130 | 100.0% | 80% | 158 | 0.0% | 45% |
| 2023-07-18 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 42 | 100.0% | 90% | 133 | 0.0% | 40% |
| 2023-07-18 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 9,559 | 100.0% | 18% | 2,478 | 0.0% | 32% |
| 2023-07-18 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,216 | 100.0% | 32% | 1,144 | 0.0% | 42% |
| 2023-07-18 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,012 | 100.0% | 49% | 614 | 0.0% | 45% |
| 2023-07-18 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 52 | 100.0% | 73% | 138 | 0.0% | 37% |
| 2023-07-18 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 4 | 100.0% | 75% | 100 | 0.0% | 0% |
| 2023-07-19 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,630 | 100.0% | 15% | 3,927 | 0.0% | 33% |
| 2023-07-19 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,542 | 100.0% | 22% | 2,319 | 0.0% | 42% |
| 2023-07-19 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,382 | 100.0% | 30% | 1,451 | 0.0% | 46% |
| 2023-07-19 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 26 | 100.0% | 77% | 128 | 0.0% | 31% |
| 2023-07-19 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,933 | 100.0% | 21% | 3,041 | 0.0% | 30% |
| 2023-07-19 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,451 | 100.0% | 27% | 1,731 | 0.0% | 35% |
| 2023-07-19 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,822 | 100.0% | 35% | 966 | 0.0% | 39% |
| 2023-07-19 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 48 | 100.0% | 81% | 122 | 0.0% | 46% |
| 2023-07-19 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 3 | 100.0% | 67% | 100 | 0.0% | 0% |
| 2023-07-20 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,878 | 100.0% | 18% | 3,061 | 0.0% | 33% |
| 2023-07-20 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,830 | 100.0% | 24% | 1,749 | 0.0% | 38% |
| 2023-07-20 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,499 | 100.0% | 35% | 953 | 0.0% | 43% |
| 2023-07-20 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 198 | 100.0% | 71% | 157 | 0.0% | 40% |
| 2023-07-20 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 24 | 100.0% | 83% | 344 | 0.0% | 12% |
| 2023-07-20 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,371 | 100.0% | 22% | 2,128 | 0.0% | 31% |
| 2023-07-20 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,500 | 100.0% | 29% | 1,321 | 0.0% | 35% |
| 2023-07-20 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,483 | 100.0% | 39% | 767 | 0.0% | 39% |
| 2023-07-20 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 116 | 100.0% | 78% | 143 | 0.0% | 41% |
| 2023-07-20 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 2 | 100.0% | 100% | none resolved | 0.0% | 0% |
| 2023-07-21 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,716 | 100.0% | 14% | 5,967 | 0.0% | 32% |
| 2023-07-21 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,002 | 100.0% | 21% | 3,131 | 0.0% | 40% |
| 2023-07-21 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,564 | 100.0% | 30% | 971 | 0.0% | 45% |
| 2023-07-21 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 26 | 100.0% | 62% | 126 | 0.0% | 42% |
| 2023-07-21 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 2 | 100.0% | 100% | none resolved | 0.0% | 50% |
| 2023-07-21 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,155 | 100.0% | 18% | 5,346 | 0.0% | 30% |
| 2023-07-21 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,345 | 100.0% | 23% | 2,773 | 0.0% | 36% |
| 2023-07-21 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,744 | 100.0% | 33% | 992 | 0.0% | 42% |
| 2023-07-21 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 39 | 100.0% | 82% | 128 | 0.0% | 54% |
| 2023-07-21 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 0% | 143 | 0.0% | 100% |
| 2023-07-22 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,582 | 99.9% | 15% | 9,832 | 0.0% | 32% |
| 2023-07-22 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,316 | 99.9% | 18% | 6,322 | 0.0% | 39% |
| 2023-07-22 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 852 | 99.9% | 27% | 2,385 | 0.1% | 45% |
| 2023-07-22 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 33 | 100.0% | 67% | 180 | 0.0% | 42% |
| 2023-07-22 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 6 | 100.0% | 100% | none resolved | 0.0% | 50% |
| 2023-07-22 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,824 | 100.0% | 22% | 5,114 | 0.0% | 31% |
| 2023-07-22 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,258 | 100.0% | 30% | 2,543 | 0.0% | 37% |
| 2023-07-22 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,212 | 99.9% | 47% | 663 | 0.1% | 46% |
| 2023-07-22 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 246 | 100.0% | 85% | 154 | 0.8% | 46% |
| 2023-07-22 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 85 | 100.0% | 85% | 172 | 2.4% | 49% |
| 2023-07-23 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,146 | 99.9% | 19% | 15,360 | 0.1% | 31% |
| 2023-07-23 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,273 | 100.0% | 13% | 7,126 | 0.0% | 30% |
| 2023-07-23 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,385 | 100.0% | 18% | 3,133 | 0.0% | 32% |
| 2023-07-23 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 307 | 100.0% | 49% | 393 | 0.0% | 43% |
| 2023-07-23 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 7 | 100.0% | 71% | 170 | 0.0% | 57% |
| 2023-07-23 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,544 | 100.0% | 20% | 5,423 | 0.0% | 31% |
| 2023-07-23 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,485 | 100.0% | 21% | 3,247 | 0.0% | 33% |
| 2023-07-23 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,946 | 100.0% | 28% | 1,560 | 0.0% | 37% |
| 2023-07-23 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 116 | 100.0% | 63% | 162 | 0.0% | 37% |
| 2023-07-23 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 4 | 100.0% | 75% | 112 | 0.0% | 50% |
| 2023-07-24 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,644 | 100.0% | 25% | 2,963 | 0.0% | 34% |
| 2023-07-24 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,990 | 100.0% | 29% | 1,598 | 0.0% | 38% |
| 2023-07-24 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,002 | 100.0% | 36% | 754 | 0.0% | 43% |
| 2023-07-24 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 367 | 100.0% | 80% | 180 | 0.0% | 41% |
| 2023-07-24 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 168 | 100.0% | 85% | 304 | 0.0% | 46% |
| 2023-07-24 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,001 | 100.0% | 25% | 3,038 | 0.0% | 33% |
| 2023-07-24 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,351 | 100.0% | 28% | 1,330 | 0.0% | 36% |
| 2023-07-24 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,194 | 100.0% | 36% | 757 | 0.0% | 43% |
| 2023-07-24 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 237 | 100.0% | 76% | 231 | 0.0% | 45% |
| 2023-07-24 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 41 | 100.0% | 78% | 214 | 0.0% | 37% |
| 2023-07-25 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,070 | 100.0% | 15% | 11,433 | 0.0% | 33% |
| 2023-07-25 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,816 | 100.0% | 16% | 5,275 | 0.0% | 38% |
| 2023-07-25 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,367 | 100.0% | 22% | 2,049 | 0.1% | 44% |
| 2023-07-25 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 43 | 100.0% | 67% | 120 | 0.0% | 47% |
| 2023-07-25 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2023-07-25 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,939 | 99.9% | 12% | 7,668 | 0.0% | 33% |
| 2023-07-25 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,393 | 99.9% | 16% | 3,617 | 0.0% | 37% |
| 2023-07-25 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,441 | 99.9% | 24% | 1,320 | 0.0% | 45% |
| 2023-07-25 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 15 | 100.0% | 67% | 128 | 0.0% | 47% |
| 2023-07-25 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 2 | 100.0% | 50% | 100 | 0.0% | 0% |
| 2023-07-26 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,015 | 100.0% | 20% | 2,536 | 0.0% | 33% |
| 2023-07-26 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,301 | 100.0% | 27% | 1,668 | 0.0% | 40% |
| 2023-07-26 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,457 | 100.0% | 36% | 813 | 0.0% | 42% |
| 2023-07-26 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 183 | 100.0% | 77% | 235 | 0.0% | 46% |
| 2023-07-26 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 14 | 100.0% | 79% | 253 | 0.0% | 50% |
| 2023-07-26 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,662 | 100.0% | 19% | 3,972 | 0.0% | 33% |
| 2023-07-26 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,160 | 100.0% | 23% | 1,867 | 0.0% | 36% |
| 2023-07-26 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,715 | 100.0% | 28% | 728 | 0.0% | 41% |
| 2023-07-26 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 104 | 100.0% | 72% | 133 | 0.0% | 43% |
| 2023-07-26 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 15 | 100.0% | 87% | 205 | 0.0% | 13% |
| 2023-07-27 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,829 | 100.0% | 11% | 7,596 | 0.0% | 36% |
| 2023-07-27 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,679 | 100.0% | 17% | 3,594 | 0.0% | 43% |
| 2023-07-27 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,320 | 100.0% | 29% | 1,702 | 0.0% | 46% |
| 2023-07-27 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 16 | 100.0% | 88% | 232 | 0.0% | 44% |
| 2023-07-27 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2023-07-27 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,343 | 100.0% | 13% | 6,232 | 0.0% | 35% |
| 2023-07-27 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,722 | 100.0% | 20% | 3,541 | 0.0% | 42% |
| 2023-07-27 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,359 | 100.0% | 33% | 2,180 | 0.0% | 46% |
| 2023-07-27 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 58 | 100.0% | 60% | 770 | 0.0% | 48% |
| 2023-07-27 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 8 | 100.0% | 75% | 598 | 0.0% | 62% |
| 2023-07-28 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,236 | 100.0% | 13% | 8,233 | 0.0% | 35% |
| 2023-07-28 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,235 | 100.0% | 18% | 3,426 | 0.0% | 40% |
| 2023-07-28 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,372 | 100.0% | 25% | 1,832 | 0.1% | 42% |
| 2023-07-28 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 98 | 100.0% | 71% | 125 | 0.0% | 46% |
| 2023-07-28 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 3 | 100.0% | 67% | 121 | 0.0% | 67% |
| 2023-07-28 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,643 | 100.0% | 13% | 6,592 | 0.0% | 34% |
| 2023-07-28 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,119 | 100.0% | 19% | 4,780 | 0.0% | 40% |
| 2023-07-28 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,121 | 100.0% | 27% | 3,398 | 0.0% | 46% |
| 2023-07-28 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 27 | 100.0% | 85% | 184 | 0.0% | 52% |
| 2023-07-28 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 0% |
| 2023-07-29 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 663 | 99.8% | 6% | 49,895 | 0.2% | 35% |
| 2023-07-29 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 650 | 100.0% | 10% | 17,284 | 0.0% | 44% |
| 2023-07-29 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 304 | 100.0% | 24% | 3,233 | 0.0% | 48% |
| 2023-07-29 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 13 | 100.0% | 77% | 176 | 0.0% | 54% |
| 2023-07-29 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2023-07-29 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 971 | 99.8% | 11% | 21,233 | 0.0% | 34% |
| 2023-07-29 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 812 | 99.9% | 15% | 14,970 | 0.0% | 41% |
| 2023-07-29 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 473 | 100.0% | 21% | 11,923 | 0.0% | 45% |
| 2023-07-29 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 18 | 100.0% | 83% | 122 | 0.0% | 44% |
| 2023-07-29 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2023-07-30 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,940 | 99.9% | 21% | 6,064 | 0.1% | 36% |
| 2023-07-30 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,869 | 100.0% | 26% | 3,384 | 0.2% | 42% |
| 2023-07-30 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 944 | 100.0% | 36% | 1,385 | 0.1% | 44% |
| 2023-07-30 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 64 | 100.0% | 75% | 185 | 0.0% | 52% |
| 2023-07-30 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 10 | 100.0% | 70% | 419 | 0.0% | 50% |
| 2023-07-30 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,143 | 100.0% | 23% | 3,925 | 0.0% | 34% |
| 2023-07-30 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,886 | 99.9% | 24% | 2,437 | 0.0% | 34% |
| 2023-07-30 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,408 | 100.0% | 26% | 1,496 | 0.0% | 42% |
| 2023-07-30 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 108 | 100.0% | 72% | 191 | 0.0% | 33% |
| 2023-07-30 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 18 | 100.0% | 78% | 297 | 0.0% | 33% |
| 2023-07-31 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,283 | 100.0% | 17% | 5,528 | 0.0% | 33% |
| 2023-07-31 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,723 | 100.0% | 23% | 3,183 | 0.0% | 40% |
| 2023-07-31 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,367 | 100.0% | 34% | 1,262 | 0.0% | 46% |
| 2023-07-31 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 27 | 100.0% | 89% | 195 | 0.0% | 48% |
| 2023-07-31 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,956 | 99.9% | 17% | 9,142 | 0.0% | 29% |
| 2023-07-31 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,016 | 100.0% | 15% | 3,713 | 0.0% | 30% |
| 2023-07-31 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,562 | 100.0% | 20% | 2,029 | 0.0% | 37% |
| 2023-07-31 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 74 | 100.0% | 74% | 143 | 0.0% | 47% |
| 2023-07-31 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2023-08-01 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,241 | 100.0% | 23% | 2,648 | 0.0% | 35% |
| 2023-08-01 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,174 | 100.0% | 32% | 1,348 | 0.0% | 42% |
| 2023-08-01 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,296 | 100.0% | 47% | 530 | 0.0% | 46% |
| 2023-08-01 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 410 | 100.0% | 82% | 181 | 0.0% | 44% |
| 2023-08-01 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 74 | 100.0% | 80% | 232 | 0.0% | 39% |
| 2023-08-01 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,600 | 100.0% | 22% | 2,422 | 0.0% | 32% |
| 2023-08-01 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,438 | 100.0% | 29% | 1,214 | 0.0% | 37% |
| 2023-08-01 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,990 | 100.0% | 42% | 570 | 0.0% | 42% |
| 2023-08-01 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 378 | 100.0% | 72% | 234 | 0.5% | 37% |
| 2023-08-01 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 140 | 100.0% | 75% | 192 | 0.0% | 36% |
| 2023-08-02 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,608 | 100.0% | 21% | 2,704 | 0.0% | 34% |
| 2023-08-02 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,568 | 100.0% | 27% | 1,482 | 0.0% | 40% |
| 2023-08-02 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,898 | 100.0% | 38% | 836 | 0.0% | 46% |
| 2023-08-02 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 163 | 100.0% | 81% | 177 | 0.0% | 40% |
| 2023-08-02 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 25 | 100.0% | 76% | 190 | 0.0% | 24% |
| 2023-08-02 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,375 | 100.0% | 18% | 2,331 | 0.0% | 35% |
| 2023-08-02 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,212 | 100.0% | 30% | 1,197 | 0.0% | 41% |
| 2023-08-02 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,051 | 100.0% | 47% | 632 | 0.0% | 45% |
| 2023-08-02 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 89 | 100.0% | 63% | 202 | 0.0% | 27% |
| 2023-08-02 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 18 | 100.0% | 61% | 273 | 0.0% | 28% |
| 2023-08-03 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,215 | 100.0% | 15% | 5,334 | 0.0% | 33% |
| 2023-08-03 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,701 | 100.0% | 24% | 2,480 | 0.0% | 43% |
| 2023-08-03 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,616 | 100.0% | 37% | 1,170 | 0.0% | 47% |
| 2023-08-03 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 19 | 100.0% | 79% | 224 | 0.0% | 32% |
| 2023-08-03 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 3 | 100.0% | 67% | 209 | 0.0% | 33% |
| 2023-08-03 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,174 | 100.0% | 20% | 6,228 | 0.0% | 31% |
| 2023-08-03 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,062 | 100.0% | 22% | 2,868 | 0.0% | 31% |
| 2023-08-03 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,024 | 100.0% | 25% | 1,451 | 0.0% | 39% |
| 2023-08-03 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 105 | 100.0% | 64% | 346 | 0.0% | 48% |
| 2023-08-03 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 6 | 100.0% | 100% | none resolved | 0.0% | 17% |
| 2023-08-04 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,493 | 99.9% | 17% | 5,318 | 0.1% | 34% |
| 2023-08-04 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,250 | 100.0% | 24% | 2,318 | 0.1% | 42% |
| 2023-08-04 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,548 | 100.0% | 36% | 874 | 0.1% | 48% |
| 2023-08-04 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 54 | 100.0% | 85% | 485 | 1.9% | 33% |
| 2023-08-04 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 5 | 100.0% | 80% | 237 | 0.0% | 20% |
| 2023-08-04 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,204 | 100.0% | 17% | 3,481 | 0.1% | 32% |
| 2023-08-04 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,621 | 100.0% | 28% | 1,649 | 0.1% | 42% |
| 2023-08-04 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,504 | 100.0% | 44% | 725 | 0.2% | 45% |
| 2023-08-04 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 110 | 100.0% | 68% | 216 | 3.6% | 35% |
| 2023-08-04 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 34 | 100.0% | 74% | 138 | 0.0% | 38% |
| 2023-08-05 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 768 | 99.7% | 8% | 31,081 | 0.0% | 32% |
| 2023-08-05 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 786 | 99.9% | 13% | 8,574 | 0.0% | 47% |
| 2023-08-05 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 267 | 100.0% | 30% | 3,440 | 0.0% | 50% |
| 2023-08-05 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 7 | 100.0% | 86% | 124 | 0.0% | 71% |
| 2023-08-05 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,184 | 99.9% | 12% | 19,668 | 0.0% | 32% |
| 2023-08-05 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 836 | 99.9% | 16% | 10,703 | 0.0% | 45% |
| 2023-08-05 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 343 | 99.7% | 30% | 5,494 | 0.0% | 48% |
| 2023-08-05 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 2 | 100.0% | 100% | none resolved | 0.0% | 50% |
| 2023-08-06 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 957 | 99.7% | 12% | 19,236 | 0.0% | 33% |
| 2023-08-06 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 846 | 99.8% | 19% | 5,712 | 0.0% | 40% |
| 2023-08-06 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 335 | 100.0% | 34% | 1,481 | 0.0% | 48% |
| 2023-08-06 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 3 | 100.0% | 100% | none resolved | 0.0% | 67% |
| 2023-08-06 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,476 | 99.9% | 14% | 15,525 | 0.0% | 32% |
| 2023-08-06 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,032 | 100.0% | 19% | 6,104 | 0.0% | 40% |
| 2023-08-06 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 443 | 100.0% | 39% | 1,255 | 0.0% | 47% |
| 2023-08-06 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 4 | 100.0% | 75% | 231 | 0.0% | 100% |
| 2023-08-06 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2023-08-07 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,811 | 100.0% | 15% | 2,704 | 0.0% | 34% |
| 2023-08-07 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,937 | 100.0% | 26% | 1,475 | 0.0% | 43% |
| 2023-08-07 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,661 | 100.0% | 41% | 852 | 0.0% | 47% |
| 2023-08-07 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 59 | 100.0% | 80% | 314 | 0.0% | 39% |
| 2023-08-07 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 0% |
| 2023-08-07 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,745 | 100.0% | 19% | 3,168 | 0.0% | 32% |
| 2023-08-07 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,815 | 100.0% | 26% | 1,614 | 0.0% | 39% |
| 2023-08-07 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,111 | 100.0% | 36% | 726 | 0.0% | 43% |
| 2023-08-07 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 152 | 100.0% | 76% | 220 | 0.7% | 43% |
| 2023-08-07 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 35 | 100.0% | 69% | 225 | 0.0% | 37% |
| 2023-08-08 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,111 | 100.0% | 21% | 3,601 | 0.0% | 31% |
| 2023-08-08 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,447 | 100.0% | 21% | 1,794 | 0.0% | 37% |
| 2023-08-08 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,469 | 100.0% | 25% | 737 | 0.0% | 42% |
| 2023-08-08 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 296 | 100.0% | 57% | 231 | 0.0% | 42% |
| 2023-08-08 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 9 | 100.0% | 89% | 109 | 0.0% | 67% |
| 2023-08-08 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,133 | 100.0% | 16% | 4,570 | 0.0% | 34% |
| 2023-08-08 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,622 | 100.0% | 22% | 3,222 | 0.0% | 35% |
| 2023-08-08 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,327 | 100.0% | 30% | 2,198 | 0.0% | 39% |
| 2023-08-08 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 108 | 100.0% | 81% | 172 | 0.0% | 48% |
| 2023-08-08 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 18 | 100.0% | 78% | 192 | 0.0% | 39% |
| 2023-08-09 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,827 | 100.0% | 16% | 4,194 | 0.0% | 33% |
| 2023-08-09 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,371 | 100.0% | 22% | 2,098 | 0.0% | 41% |
| 2023-08-09 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,350 | 100.0% | 34% | 787 | 0.0% | 45% |
| 2023-08-09 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 63 | 100.0% | 76% | 173 | 0.0% | 35% |
| 2023-08-09 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 3 | 100.0% | 100% | none resolved | 0.0% | 33% |
| 2023-08-09 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,442 | 100.0% | 15% | 5,170 | 0.0% | 31% |
| 2023-08-09 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,762 | 100.0% | 23% | 2,966 | 0.0% | 39% |
| 2023-08-09 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,212 | 100.0% | 36% | 1,424 | 0.0% | 46% |
| 2023-08-09 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 10 | 100.0% | 90% | 142 | 0.0% | 80% |
| 2023-08-10 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,168 | 100.0% | 17% | 4,894 | 0.0% | 33% |
| 2023-08-10 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,785 | 100.0% | 21% | 2,610 | 0.0% | 42% |
| 2023-08-10 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,410 | 100.0% | 31% | 725 | 0.0% | 48% |
| 2023-08-10 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 33 | 100.0% | 82% | 110 | 0.0% | 52% |
| 2023-08-10 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,697 | 100.0% | 13% | 5,046 | 0.0% | 33% |
| 2023-08-10 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,251 | 100.0% | 19% | 2,354 | 0.0% | 38% |
| 2023-08-10 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,028 | 100.0% | 35% | 686 | 0.0% | 43% |
| 2023-08-10 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 16 | 100.0% | 75% | 106 | 0.0% | 44% |
| 2023-08-11 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,077 | 100.0% | 14% | 7,520 | 0.0% | 33% |
| 2023-08-11 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,848 | 100.0% | 20% | 3,580 | 0.0% | 45% |
| 2023-08-11 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 820 | 100.0% | 33% | 1,038 | 0.0% | 45% |
| 2023-08-11 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 30 | 100.0% | 87% | 114 | 0.0% | 53% |
| 2023-08-11 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,176 | 99.9% | 12% | 7,636 | 0.0% | 34% |
| 2023-08-11 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,517 | 99.9% | 24% | 3,213 | 0.0% | 44% |
| 2023-08-11 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 576 | 100.0% | 43% | 705 | 0.0% | 49% |
| 2023-08-11 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 19 | 100.0% | 68% | 252 | 0.0% | 42% |
| 2023-08-11 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 4 | 100.0% | 100% | none resolved | 0.0% | 50% |
| 2023-08-12 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 267 | 99.6% | 8% | 113,675 | 0.0% | 35% |
| 2023-08-12 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 244 | 100.0% | 12% | 29,851 | 0.0% | 42% |
| 2023-08-12 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 105 | 100.0% | 22% | 23,714 | 0.0% | 47% |
| 2023-08-12 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 4 | 100.0% | 50% | 146 | 0.0% | 50% |
| 2023-08-12 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 295 | 100.0% | 10% | 87,979 | 0.0% | 32% |
| 2023-08-12 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 275 | 100.0% | 12% | 34,458 | 0.0% | 32% |
| 2023-08-12 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 186 | 100.0% | 17% | 24,887 | 0.0% | 44% |
| 2023-08-12 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 2 | 100.0% | 50% | 103 | 0.0% | 0% |
| 2023-08-13 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 351 | 99.7% | 14% | 34,269 | 0.0% | 34% |
| 2023-08-13 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 319 | 99.7% | 9% | 14,771 | 0.0% | 24% |
| 2023-08-13 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 237 | 99.6% | 19% | 4,414 | 0.0% | 42% |
| 2023-08-13 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 6 | 100.0% | 67% | 342 | 0.0% | 67% |
| 2023-08-13 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 5 | 100.0% | 100% | none resolved | 0.0% | 60% |
| 2023-08-13 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,071 | 99.9% | 13% | 6,480 | 0.0% | 35% |
| 2023-08-13 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 840 | 99.9% | 23% | 2,480 | 0.0% | 44% |
| 2023-08-13 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 353 | 99.7% | 40% | 1,771 | 0.0% | 44% |
| 2023-08-13 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 8 | 100.0% | 88% | 157 | 0.0% | 62% |
| 2023-08-14 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,155 | 100.0% | 17% | 4,190 | 0.0% | 33% |
| 2023-08-14 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,560 | 100.0% | 20% | 3,443 | 0.0% | 40% |
| 2023-08-14 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,726 | 100.0% | 32% | 1,633 | 0.0% | 44% |
| 2023-08-14 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 46 | 100.0% | 85% | 202 | 0.0% | 59% |
| 2023-08-14 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 0% | 131 | 0.0% | 100% |
| 2023-08-14 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,851 | 99.9% | 14% | 7,920 | 0.0% | 33% |
| 2023-08-14 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,569 | 99.9% | 18% | 5,017 | 0.0% | 35% |
| 2023-08-14 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 959 | 99.9% | 25% | 2,544 | 0.0% | 45% |
| 2023-08-14 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 10 | 100.0% | 80% | 12,992 | 0.0% | 70% |
| 2023-08-15 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,581 | 99.9% | 29% | 6,523 | 0.0% | 35% |
| 2023-08-15 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,705 | 99.9% | 28% | 2,525 | 0.0% | 35% |
| 2023-08-15 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,255 | 100.0% | 29% | 1,383 | 0.0% | 39% |
| 2023-08-15 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 94 | 100.0% | 71% | 257 | 0.0% | 48% |
| 2023-08-15 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 5 | 100.0% | 40% | 138 | 0.0% | 0% |
| 2023-08-15 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,314 | 99.8% | 31% | 4,793 | 0.0% | 31% |
| 2023-08-15 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,494 | 100.0% | 28% | 2,034 | 0.1% | 30% |
| 2023-08-15 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,386 | 100.0% | 31% | 979 | 0.1% | 36% |
| 2023-08-15 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 339 | 100.0% | 67% | 341 | 0.3% | 40% |
| 2023-08-15 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 118 | 100.0% | 86% | 238 | 0.8% | 47% |
| 2023-08-16 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,333 | 100.0% | 21% | 4,041 | 0.0% | 33% |
| 2023-08-16 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,328 | 100.0% | 21% | 1,846 | 0.0% | 37% |
| 2023-08-16 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,765 | 99.9% | 25% | 1,290 | 0.0% | 35% |
| 2023-08-16 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 615 | 100.0% | 37% | 965 | 0.0% | 39% |
| 2023-08-16 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 9 | 100.0% | 89% | 201 | 0.0% | 56% |
| 2023-08-16 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,244 | 99.9% | 24% | 5,955 | 0.0% | 30% |
| 2023-08-16 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,657 | 99.9% | 17% | 3,148 | 0.0% | 25% |
| 2023-08-16 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,078 | 100.0% | 19% | 1,852 | 0.0% | 30% |
| 2023-08-16 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 305 | 100.0% | 55% | 385 | 0.0% | 48% |
| 2023-08-16 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 37 | 100.0% | 73% | 125 | 0.0% | 38% |
| 2023-08-17 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 9,909 | 100.0% | 40% | 638 | 0.0% | 34% |
| 2023-08-17 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,656 | 100.0% | 39% | 617 | 0.0% | 32% |
| 2023-08-17 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,486 | 100.0% | 40% | 678 | 0.0% | 33% |
| 2023-08-17 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,591 | 100.0% | 61% | 382 | 0.0% | 41% |
| 2023-08-17 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 656 | 100.0% | 73% | 256 | 0.0% | 36% |
| 2023-08-17 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 12,014 | 100.0% | 54% | 464 | 0.4% | 32% |
| 2023-08-17 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 13,540 | 100.0% | 45% | 747 | 0.4% | 29% |
| 2023-08-17 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 16,428 | 100.0% | 40% | 706 | 0.3% | 28% |
| 2023-08-17 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 5,243 | 100.0% | 73% | 201 | 0.7% | 43% |
| 2023-08-17 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 968 | 100.0% | 73% | 212 | 2.4% | 39% |
| 2023-08-18 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,687 | 100.0% | 22% | 1,813 | 0.0% | 33% |
| 2023-08-18 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,306 | 100.0% | 28% | 863 | 0.0% | 40% |
| 2023-08-18 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,972 | 100.0% | 39% | 401 | 0.0% | 44% |
| 2023-08-18 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 307 | 100.0% | 75% | 138 | 0.0% | 46% |
| 2023-08-18 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 30 | 100.0% | 83% | 195 | 0.0% | 40% |
| 2023-08-18 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,089 | 100.0% | 23% | 1,719 | 0.0% | 31% |
| 2023-08-18 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,757 | 100.0% | 29% | 819 | 0.0% | 33% |
| 2023-08-18 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,344 | 100.0% | 38% | 528 | 0.0% | 37% |
| 2023-08-18 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 730 | 100.0% | 66% | 168 | 0.0% | 46% |
| 2023-08-18 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 60 | 100.0% | 80% | 268 | 0.0% | 32% |
| 2023-08-19 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,847 | 100.0% | 16% | 4,435 | 0.0% | 34% |
| 2023-08-19 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,305 | 100.0% | 22% | 1,727 | 0.0% | 45% |
| 2023-08-19 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,726 | 100.0% | 37% | 660 | 0.0% | 49% |
| 2023-08-19 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 35 | 100.0% | 83% | 132 | 0.0% | 46% |
| 2023-08-19 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2023-08-19 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,275 | 100.0% | 18% | 2,895 | 0.0% | 34% |
| 2023-08-19 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,539 | 100.0% | 29% | 1,699 | 0.0% | 45% |
| 2023-08-19 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,918 | 99.9% | 47% | 790 | 0.0% | 48% |
| 2023-08-19 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 67 | 100.0% | 85% | 135 | 0.0% | 46% |
| 2023-08-19 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 6 | 100.0% | 67% | 150 | 0.0% | 50% |
| 2023-08-20 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,767 | 100.0% | 13% | 7,839 | 0.0% | 34% |
| 2023-08-20 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,522 | 100.0% | 22% | 2,597 | 0.0% | 46% |
| 2023-08-20 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,060 | 100.0% | 39% | 506 | 0.0% | 51% |
| 2023-08-20 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 28 | 100.0% | 82% | 121 | 0.0% | 46% |
| 2023-08-20 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 0% | 110 | 0.0% | 0% |
| 2023-08-20 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,408 | 100.0% | 18% | 5,788 | 0.0% | 32% |
| 2023-08-20 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,515 | 100.0% | 25% | 2,743 | 0.0% | 39% |
| 2023-08-20 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,807 | 100.0% | 42% | 777 | 0.0% | 46% |
| 2023-08-20 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 56 | 100.0% | 79% | 156 | 0.0% | 50% |
| 2023-08-20 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 6 | 100.0% | 67% | 198 | 0.0% | 67% |
| 2023-08-21 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,912 | 100.0% | 19% | 2,815 | 0.0% | 34% |
| 2023-08-21 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,047 | 100.0% | 29% | 1,297 | 0.0% | 45% |
| 2023-08-21 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,917 | 100.0% | 48% | 420 | 0.0% | 48% |
| 2023-08-21 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 48 | 100.0% | 69% | 165 | 0.0% | 42% |
| 2023-08-21 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 5 | 100.0% | 60% | 244 | 0.0% | 0% |
| 2023-08-21 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,889 | 100.0% | 23% | 2,266 | 0.0% | 31% |
| 2023-08-21 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,954 | 100.0% | 28% | 1,396 | 0.0% | 35% |
| 2023-08-21 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,034 | 100.0% | 42% | 915 | 0.0% | 43% |
| 2023-08-21 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 141 | 100.0% | 77% | 155 | 0.0% | 37% |
| 2023-08-21 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 14 | 100.0% | 79% | 215 | 0.0% | 43% |
| 2023-08-22 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,964 | 100.0% | 21% | 1,970 | 0.0% | 33% |
| 2023-08-22 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,781 | 100.0% | 31% | 953 | 0.0% | 43% |
| 2023-08-22 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,939 | 100.0% | 45% | 399 | 0.0% | 44% |
| 2023-08-22 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 291 | 100.0% | 79% | 176 | 0.0% | 38% |
| 2023-08-22 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 92 | 100.0% | 84% | 145 | 0.0% | 49% |
| 2023-08-22 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,035 | 100.0% | 27% | 1,136 | 0.0% | 31% |
| 2023-08-22 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,544 | 100.0% | 36% | 612 | 0.0% | 36% |
| 2023-08-22 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,090 | 100.0% | 52% | 295 | 0.0% | 44% |
| 2023-08-22 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 415 | 100.0% | 76% | 245 | 0.0% | 32% |
| 2023-08-22 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 176 | 100.0% | 77% | 242 | 0.0% | 33% |
| 2023-08-23 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,000 | 100.0% | 20% | 1,978 | 0.0% | 34% |
| 2023-08-23 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,680 | 100.0% | 29% | 964 | 0.0% | 42% |
| 2023-08-23 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,946 | 100.0% | 46% | 382 | 0.0% | 48% |
| 2023-08-23 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 168 | 100.0% | 81% | 168 | 0.0% | 40% |
| 2023-08-23 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 21 | 100.0% | 81% | 171 | 0.0% | 43% |
| 2023-08-23 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,693 | 100.0% | 24% | 1,790 | 0.0% | 33% |
| 2023-08-23 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,182 | 100.0% | 31% | 1,074 | 0.0% | 38% |
| 2023-08-23 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,729 | 100.0% | 43% | 529 | 0.0% | 43% |
| 2023-08-23 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 371 | 100.0% | 78% | 210 | 0.0% | 42% |
| 2023-08-23 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 52 | 100.0% | 83% | 134 | 0.0% | 46% |
| 2023-08-24 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,422 | 100.0% | 15% | 3,159 | 0.0% | 35% |
| 2023-08-24 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,717 | 100.0% | 26% | 1,503 | 0.0% | 45% |
| 2023-08-24 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,436 | 100.0% | 39% | 581 | 0.0% | 48% |
| 2023-08-24 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 77 | 100.0% | 73% | 145 | 0.0% | 42% |
| 2023-08-24 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 12 | 100.0% | 92% | 294 | 0.0% | 42% |
| 2023-08-24 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,387 | 100.0% | 22% | 3,193 | 0.0% | 31% |
| 2023-08-24 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,357 | 100.0% | 23% | 1,366 | 0.0% | 30% |
| 2023-08-24 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,637 | 100.0% | 32% | 621 | 0.0% | 40% |
| 2023-08-24 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 130 | 100.0% | 81% | 236 | 0.0% | 39% |
| 2023-08-24 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 11 | 100.0% | 64% | 152 | 0.0% | 18% |
| 2023-08-25 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,073 | 100.0% | 18% | 2,872 | 0.0% | 35% |
| 2023-08-25 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,528 | 100.0% | 24% | 1,482 | 0.0% | 41% |
| 2023-08-25 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,046 | 100.0% | 34% | 528 | 0.0% | 44% |
| 2023-08-25 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 60 | 100.0% | 78% | 129 | 0.0% | 38% |
| 2023-08-25 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 0% |
| 2023-08-25 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,172 | 100.0% | 22% | 1,584 | 0.0% | 32% |
| 2023-08-25 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,823 | 100.0% | 31% | 867 | 0.0% | 39% |
| 2023-08-25 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,404 | 100.0% | 49% | 395 | 0.0% | 46% |
| 2023-08-25 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 113 | 100.0% | 78% | 133 | 0.0% | 39% |
| 2023-08-25 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 31 | 100.0% | 100% | none resolved | 0.0% | 45% |
| 2023-08-26 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 653 | 99.8% | 7% | 43,660 | 0.0% | 35% |
| 2023-08-26 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 665 | 99.8% | 12% | 18,900 | 0.2% | 44% |
| 2023-08-26 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 354 | 100.0% | 22% | 6,828 | 0.3% | 46% |
| 2023-08-26 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 6 | 100.0% | 67% | 221 | 0.0% | 33% |
| 2023-08-26 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 0% |
| 2023-08-26 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,272 | 100.0% | 10% | 18,628 | 0.0% | 34% |
| 2023-08-26 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,105 | 100.0% | 17% | 9,183 | 0.0% | 42% |
| 2023-08-26 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 544 | 100.0% | 32% | 3,308 | 0.0% | 46% |
| 2023-08-26 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 19 | 100.0% | 74% | 132 | 0.0% | 74% |
| 2023-08-26 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 6 | 100.0% | 67% | 126 | 0.0% | 67% |
| 2023-08-27 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,140 | 99.9% | 6% | 15,766 | 0.0% | 34% |
| 2023-08-27 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,169 | 100.0% | 16% | 5,469 | 0.0% | 43% |
| 2023-08-27 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 426 | 100.0% | 34% | 2,938 | 0.0% | 48% |
| 2023-08-27 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 1 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2023-08-27 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,022 | 100.0% | 12% | 9,878 | 0.0% | 34% |
| 2023-08-27 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,605 | 100.0% | 19% | 4,806 | 0.0% | 42% |
| 2023-08-27 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 765 | 100.0% | 33% | 3,324 | 0.0% | 48% |
| 2023-08-27 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 10 | 100.0% | 100% | none resolved | 0.0% | 30% |
| 2023-08-28 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,376 | 100.0% | 16% | 4,088 | 0.0% | 37% |
| 2023-08-28 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,831 | 100.0% | 22% | 2,192 | 0.0% | 43% |
| 2023-08-28 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,995 | 100.0% | 36% | 972 | 0.0% | 49% |
| 2023-08-28 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 42 | 100.0% | 76% | 134 | 0.0% | 38% |
| 2023-08-28 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 4 | 100.0% | 75% | 143 | 0.0% | 50% |
| 2023-08-28 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,050 | 100.0% | 21% | 2,478 | 0.0% | 33% |
| 2023-08-28 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,713 | 100.0% | 29% | 1,406 | 0.0% | 39% |
| 2023-08-28 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,793 | 100.0% | 43% | 610 | 0.0% | 43% |
| 2023-08-28 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 231 | 100.0% | 89% | 165 | 0.0% | 43% |
| 2023-08-28 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 38 | 100.0% | 82% | 296 | 0.0% | 32% |
| 2023-08-29 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 20,294 | 100.0% | 37% | 604 | 0.0% | 35% |
| 2023-08-29 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 17,804 | 100.0% | 46% | 434 | 0.0% | 41% |
| 2023-08-29 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,179 | 100.0% | 58% | 290 | 0.0% | 44% |
| 2023-08-29 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,633 | 100.0% | 86% | 162 | 0.0% | 46% |
| 2023-08-29 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 230 | 100.0% | 87% | 190 | 0.0% | 45% |
| 2023-08-29 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,485 | 100.0% | 41% | 918 | 0.0% | 35% |
| 2023-08-29 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 13,940 | 100.0% | 42% | 604 | 0.0% | 34% |
| 2023-08-29 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,681 | 100.0% | 46% | 366 | 0.0% | 37% |
| 2023-08-29 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,867 | 100.0% | 76% | 185 | 0.0% | 45% |
| 2023-08-29 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 238 | 100.0% | 82% | 180 | 0.0% | 39% |
| 2023-08-30 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,770 | 100.0% | 18% | 2,516 | 0.0% | 35% |
| 2023-08-30 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,721 | 100.0% | 26% | 1,359 | 0.0% | 43% |
| 2023-08-30 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,493 | 100.0% | 38% | 540 | 0.0% | 47% |
| 2023-08-30 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 198 | 100.0% | 82% | 171 | 0.0% | 45% |
| 2023-08-30 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 42 | 100.0% | 83% | 152 | 0.0% | 57% |
| 2023-08-30 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,778 | 100.0% | 22% | 2,454 | 0.0% | 30% |
| 2023-08-30 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,245 | 100.0% | 24% | 954 | 0.0% | 32% |
| 2023-08-30 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,718 | 100.0% | 36% | 480 | 0.0% | 40% |
| 2023-08-30 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 187 | 100.0% | 87% | 182 | 0.0% | 48% |
| 2023-08-30 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 26 | 100.0% | 85% | 170 | 0.0% | 50% |
| 2023-08-31 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,789 | 100.0% | 32% | 976 | 0.0% | 33% |
| 2023-08-31 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,785 | 100.0% | 39% | 581 | 0.0% | 39% |
| 2023-08-31 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,352 | 100.0% | 53% | 259 | 0.0% | 45% |
| 2023-08-31 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 760 | 100.0% | 83% | 176 | 0.0% | 44% |
| 2023-08-31 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 134 | 100.0% | 81% | 176 | 0.0% | 37% |
| 2023-08-31 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,028 | 100.0% | 32% | 1,138 | 0.0% | 31% |
| 2023-08-31 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,626 | 100.0% | 34% | 622 | 0.0% | 32% |
| 2023-08-31 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,094 | 100.0% | 43% | 354 | 0.0% | 38% |
| 2023-08-31 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 608 | 100.0% | 80% | 174 | 0.0% | 40% |
| 2023-08-31 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 86 | 100.0% | 81% | 205 | 0.0% | 37% |
| 2023-09-01 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,063 | 100.0% | 24% | 1,158 | 0.0% | 32% |
| 2023-09-01 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,967 | 100.0% | 38% | 444 | 0.0% | 43% |
| 2023-09-01 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,467 | 100.0% | 61% | 198 | 0.0% | 50% |
| 2023-09-01 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 191 | 100.0% | 82% | 134 | 0.0% | 38% |
| 2023-09-01 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 36 | 100.0% | 83% | 160 | 0.0% | 44% |
| 2023-09-01 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,432 | 100.0% | 29% | 1,420 | 0.0% | 30% |
| 2023-09-01 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,087 | 100.0% | 30% | 691 | 0.0% | 29% |
| 2023-09-01 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,700 | 100.0% | 42% | 314 | 0.0% | 36% |
| 2023-09-01 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 238 | 100.0% | 83% | 166 | 0.0% | 33% |
| 2023-09-01 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 22 | 100.0% | 91% | 164 | 0.0% | 27% |
| 2023-09-02 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,612 | 100.0% | 9% | 10,044 | 0.0% | 37% |
| 2023-09-02 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,004 | 100.0% | 23% | 2,420 | 0.0% | 50% |
| 2023-09-02 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 580 | 100.0% | 46% | 266 | 0.0% | 53% |
| 2023-09-02 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 11 | 100.0% | 100% | none resolved | 0.0% | 45% |
| 2023-09-02 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,424 | 100.0% | 16% | 6,821 | 0.0% | 31% |
| 2023-09-02 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,372 | 100.0% | 27% | 2,978 | 0.0% | 40% |
| 2023-09-02 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 828 | 100.0% | 49% | 907 | 0.0% | 46% |
| 2023-09-02 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 23 | 100.0% | 91% | 127 | 0.0% | 35% |
| 2023-09-02 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 2 | 100.0% | 50% | 118 | 0.0% | 100% |
| 2023-09-03 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,077 | 100.0% | 17% | 4,300 | 0.0% | 35% |
| 2023-09-03 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,042 | 100.0% | 29% | 1,534 | 0.0% | 44% |
| 2023-09-03 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,047 | 100.0% | 53% | 222 | 0.0% | 49% |
| 2023-09-03 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 47 | 100.0% | 85% | 162 | 0.0% | 57% |
| 2023-09-03 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 4 | 100.0% | 50% | 148 | 0.0% | 50% |
| 2023-09-03 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,996 | 100.0% | 21% | 3,070 | 0.0% | 31% |
| 2023-09-03 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,877 | 100.0% | 32% | 1,918 | 0.0% | 38% |
| 2023-09-03 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,128 | 100.0% | 44% | 1,138 | 0.0% | 51% |
| 2023-09-03 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 39 | 100.0% | 82% | 158 | 0.0% | 41% |
| 2023-09-03 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 3 | 100.0% | 100% | none resolved | 0.0% | 67% |
| 2023-09-04 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,198 | 100.0% | 17% | 3,533 | 0.0% | 34% |
| 2023-09-04 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,938 | 100.0% | 25% | 1,738 | 0.0% | 42% |
| 2023-09-04 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,548 | 100.0% | 41% | 750 | 0.0% | 48% |
| 2023-09-04 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 72 | 100.0% | 75% | 180 | 0.0% | 40% |
| 2023-09-04 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 9 | 100.0% | 89% | 393 | 0.0% | 33% |
| 2023-09-04 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,437 | 100.0% | 21% | 2,926 | 0.0% | 31% |
| 2023-09-04 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,144 | 100.0% | 30% | 1,535 | 0.0% | 37% |
| 2023-09-04 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,642 | 100.0% | 44% | 586 | 0.0% | 44% |
| 2023-09-04 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 55 | 100.0% | 95% | 562 | 0.0% | 38% |
| 2023-09-04 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 11 | 100.0% | 91% | 170 | 0.0% | 36% |
| 2023-09-05 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,492 | 100.0% | 16% | 3,556 | 0.0% | 33% |
| 2023-09-05 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,142 | 100.0% | 25% | 1,743 | 0.0% | 41% |
| 2023-09-05 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,572 | 100.0% | 40% | 909 | 0.0% | 48% |
| 2023-09-05 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 42 | 100.0% | 83% | 159 | 0.0% | 48% |
| 2023-09-05 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 3 | 100.0% | 67% | 107 | 0.0% | 33% |
| 2023-09-05 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,620 | 100.0% | 22% | 3,656 | 0.0% | 30% |
| 2023-09-05 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,016 | 100.0% | 25% | 1,732 | 0.0% | 34% |
| 2023-09-05 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,523 | 100.0% | 43% | 540 | 0.0% | 43% |
| 2023-09-05 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 68 | 100.0% | 84% | 163 | 0.0% | 40% |
| 2023-09-05 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 7 | 100.0% | 71% | 154 | 0.0% | 14% |
| 2023-09-06 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,753 | 100.0% | 24% | 1,893 | 0.0% | 32% |
| 2023-09-06 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,035 | 100.0% | 32% | 1,078 | 0.0% | 40% |
| 2023-09-06 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,832 | 100.0% | 49% | 383 | 0.0% | 44% |
| 2023-09-06 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 221 | 100.0% | 86% | 216 | 0.0% | 44% |
| 2023-09-06 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 35 | 100.0% | 83% | 123 | 0.0% | 43% |
| 2023-09-06 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 9,483 | 100.0% | 30% | 1,080 | 0.0% | 31% |
| 2023-09-06 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,248 | 100.0% | 41% | 600 | 0.0% | 37% |
| 2023-09-06 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,470 | 100.0% | 57% | 333 | 0.0% | 42% |
| 2023-09-06 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 309 | 100.0% | 82% | 209 | 0.0% | 42% |
| 2023-09-06 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 120 | 100.0% | 88% | 141 | 0.0% | 40% |
| 2023-09-07 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,898 | 99.9% | 23% | 2,182 | 0.1% | 31% |
| 2023-09-07 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,526 | 99.9% | 31% | 1,146 | 0.1% | 37% |
| 2023-09-07 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,465 | 100.0% | 49% | 408 | 0.0% | 43% |
| 2023-09-07 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 207 | 100.0% | 79% | 192 | 0.0% | 49% |
| 2023-09-07 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 50 | 100.0% | 82% | 155 | 0.0% | 48% |
| 2023-09-07 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,448 | 99.9% | 24% | 3,436 | 0.0% | 32% |
| 2023-09-07 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,129 | 99.9% | 27% | 1,550 | 0.0% | 32% |
| 2023-09-07 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,434 | 99.9% | 35% | 548 | 0.0% | 39% |
| 2023-09-07 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 144 | 100.0% | 85% | 315 | 0.0% | 49% |
| 2023-09-07 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 11 | 100.0% | 82% | 232 | 0.0% | 45% |
| 2023-09-08 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,628 | 100.0% | 26% | 2,594 | 0.0% | 31% |
| 2023-09-08 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,164 | 100.0% | 35% | 1,293 | 0.0% | 38% |
| 2023-09-08 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,410 | 100.0% | 53% | 453 | 0.0% | 45% |
| 2023-09-08 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 76 | 100.0% | 88% | 132 | 0.0% | 45% |
| 2023-09-08 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 6 | 100.0% | 83% | 139 | 0.0% | 50% |
| 2023-09-08 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,821 | 100.0% | 27% | 2,220 | 0.0% | 32% |
| 2023-09-08 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,282 | 100.0% | 31% | 1,180 | 0.0% | 34% |
| 2023-09-08 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,811 | 100.0% | 43% | 558 | 0.0% | 44% |
| 2023-09-08 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 50 | 100.0% | 98% | 329 | 0.0% | 62% |
| 2023-09-08 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 2 | 100.0% | 100% | none resolved | 0.0% | 0% |
| 2023-09-09 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,087 | 99.8% | 11% | 19,382 | 0.0% | 28% |
| 2023-09-09 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 789 | 99.9% | 26% | 4,577 | 0.1% | 43% |
| 2023-09-09 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 276 | 100.0% | 51% | 488 | 0.4% | 47% |
| 2023-09-09 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 12 | 100.0% | 67% | 119 | 0.0% | 67% |
| 2023-09-09 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2023-09-09 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,103 | 99.8% | 13% | 24,735 | 0.0% | 32% |
| 2023-09-09 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 943 | 99.9% | 19% | 8,056 | 0.2% | 41% |
| 2023-09-09 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 378 | 100.0% | 34% | 2,376 | 0.3% | 51% |
| 2023-09-09 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 3 | 100.0% | 100% | none resolved | 0.0% | 67% |
| 2023-09-10 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,772 | 100.0% | 21% | 2,782 | 0.0% | 32% |
| 2023-09-10 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,162 | 100.0% | 37% | 1,074 | 0.0% | 41% |
| 2023-09-10 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 972 | 100.0% | 61% | 290 | 0.0% | 46% |
| 2023-09-10 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 79 | 100.0% | 77% | 172 | 0.0% | 35% |
| 2023-09-10 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 15 | 100.0% | 87% | 202 | 0.0% | 40% |
| 2023-09-10 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,578 | 100.0% | 26% | 1,709 | 0.0% | 30% |
| 2023-09-10 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,387 | 100.0% | 38% | 881 | 0.0% | 38% |
| 2023-09-10 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,261 | 100.0% | 56% | 302 | 0.0% | 48% |
| 2023-09-10 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 165 | 100.0% | 80% | 214 | 0.0% | 35% |
| 2023-09-10 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 41 | 100.0% | 90% | 363 | 0.0% | 34% |
| 2023-09-11 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 15,185 | 100.0% | 31% | 1,018 | 0.2% | 32% |
| 2023-09-11 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,737 | 100.0% | 43% | 549 | 0.2% | 39% |
| 2023-09-11 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,655 | 100.0% | 60% | 230 | 0.2% | 43% |
| 2023-09-11 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 406 | 100.0% | 82% | 142 | 0.0% | 43% |
| 2023-09-11 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 65 | 100.0% | 78% | 203 | 3.1% | 37% |
| 2023-09-11 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,527 | 100.0% | 37% | 1,171 | 0.1% | 31% |
| 2023-09-11 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 14,638 | 100.0% | 37% | 585 | 0.0% | 31% |
| 2023-09-11 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 9,664 | 100.0% | 49% | 326 | 0.0% | 38% |
| 2023-09-11 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 674 | 100.0% | 84% | 164 | 0.0% | 41% |
| 2023-09-11 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 152 | 100.0% | 89% | 248 | 0.0% | 40% |
| 2023-09-12 | btc_perp_binance_bybit | ok | 0.990 | gross>0bps | 19,085 | 100.0% | 31% | 972 | 0.3% | 31% |
| 2023-09-12 | btc_perp_binance_bybit | ok | 0.990 | gross>1bps | 15,233 | 100.0% | 39% | 746 | 0.3% | 36% |
| 2023-09-12 | btc_perp_binance_bybit | ok | 0.990 | gross>2bps | 8,837 | 100.0% | 50% | 426 | 0.6% | 42% |
| 2023-09-12 | btc_perp_binance_bybit | ok | 0.990 | gross>5bps | 587 | 100.0% | 82% | 170 | 5.6% | 38% |
| 2023-09-12 | btc_perp_binance_bybit | ok | 0.990 | retail_taker | 104 | 100.0% | 81% | 162 | 0.0% | 38% |
| 2023-09-12 | eth_perp_binance_bybit | ok | 0.989 | gross>0bps | 17,945 | 100.0% | 31% | 1,146 | 0.5% | 31% |
| 2023-09-12 | eth_perp_binance_bybit | ok | 0.989 | gross>1bps | 14,787 | 100.0% | 38% | 581 | 0.5% | 35% |
| 2023-09-12 | eth_perp_binance_bybit | ok | 0.989 | gross>2bps | 7,223 | 100.0% | 53% | 314 | 1.1% | 41% |
| 2023-09-12 | eth_perp_binance_bybit | ok | 0.989 | gross>5bps | 383 | 100.0% | 81% | 178 | 15.1% | 37% |
| 2023-09-12 | eth_perp_binance_bybit | ok | 0.989 | retail_taker | 108 | 100.0% | 81% | 224 | 4.6% | 37% |
| 2023-09-13 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,059 | 100.0% | 27% | 1,419 | 0.0% | 31% |
| 2023-09-13 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,805 | 100.0% | 34% | 872 | 0.0% | 34% |
| 2023-09-13 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,886 | 100.0% | 44% | 522 | 0.0% | 40% |
| 2023-09-13 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 242 | 100.0% | 78% | 192 | 0.0% | 44% |
| 2023-09-13 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 4 | 100.0% | 100% | none resolved | 0.0% | 75% |
| 2023-09-13 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,443 | 100.0% | 28% | 1,526 | 0.0% | 30% |
| 2023-09-13 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,543 | 100.0% | 34% | 914 | 0.0% | 33% |
| 2023-09-13 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,047 | 100.0% | 44% | 528 | 0.0% | 37% |
| 2023-09-13 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 197 | 100.0% | 78% | 177 | 0.0% | 39% |
| 2023-09-13 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 38 | 100.0% | 66% | 343 | 0.0% | 18% |
| 2023-09-14 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 12,009 | 100.0% | 24% | 1,555 | 0.1% | 30% |
| 2023-09-14 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,434 | 100.0% | 34% | 831 | 0.1% | 37% |
| 2023-09-14 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,384 | 100.0% | 53% | 317 | 0.1% | 42% |
| 2023-09-14 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 226 | 100.0% | 85% | 132 | 0.0% | 45% |
| 2023-09-14 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 36 | 100.0% | 78% | 210 | 0.0% | 33% |
| 2023-09-14 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,668 | 100.0% | 29% | 1,600 | 0.1% | 29% |
| 2023-09-14 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,880 | 100.0% | 31% | 980 | 0.1% | 31% |
| 2023-09-14 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,880 | 100.0% | 40% | 734 | 0.1% | 37% |
| 2023-09-14 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 345 | 100.0% | 79% | 180 | 0.3% | 44% |
| 2023-09-14 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 51 | 100.0% | 78% | 155 | 0.0% | 37% |
| 2023-09-15 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,557 | 100.0% | 25% | 3,840 | 0.0% | 30% |
| 2023-09-15 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,756 | 100.0% | 25% | 2,535 | 0.0% | 33% |
| 2023-09-15 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,067 | 100.0% | 36% | 764 | 0.0% | 42% |
| 2023-09-15 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 132 | 100.0% | 86% | 223 | 0.0% | 40% |
| 2023-09-15 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 5 | 100.0% | 60% | 206 | 0.0% | 40% |
| 2023-09-15 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,372 | 100.0% | 24% | 3,504 | 0.0% | 31% |
| 2023-09-15 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,267 | 100.0% | 27% | 2,078 | 0.1% | 32% |
| 2023-09-15 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,526 | 100.0% | 31% | 838 | 0.0% | 34% |
| 2023-09-15 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 151 | 100.0% | 78% | 118 | 0.0% | 48% |
| 2023-09-15 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 10 | 100.0% | 100% | none resolved | 0.0% | 30% |
| 2023-09-16 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,950 | 100.0% | 15% | 8,338 | 0.0% | 33% |
| 2023-09-16 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,186 | 100.0% | 27% | 3,469 | 0.0% | 45% |
| 2023-09-16 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 836 | 100.0% | 45% | 547 | 0.0% | 49% |
| 2023-09-16 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 29 | 100.0% | 86% | 118 | 0.0% | 62% |
| 2023-09-16 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 2 | 100.0% | 100% | none resolved | 0.0% | 50% |
| 2023-09-16 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,681 | 100.0% | 20% | 8,033 | 0.1% | 34% |
| 2023-09-16 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,524 | 100.0% | 20% | 4,016 | 0.0% | 36% |
| 2023-09-16 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,292 | 99.9% | 36% | 1,410 | 0.0% | 46% |
| 2023-09-16 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 12 | 100.0% | 75% | 103 | 0.0% | 58% |
| 2023-09-16 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 0% |
| 2023-09-17 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,218 | 100.0% | 15% | 11,567 | 0.0% | 32% |
| 2023-09-17 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,583 | 100.0% | 31% | 3,285 | 0.0% | 43% |
| 2023-09-17 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 506 | 100.0% | 52% | 538 | 0.0% | 46% |
| 2023-09-17 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 20 | 100.0% | 75% | 300 | 0.0% | 50% |
| 2023-09-17 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 2 | 100.0% | 100% | none resolved | 0.0% | 50% |
| 2023-09-17 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,491 | 100.0% | 23% | 9,880 | 0.2% | 34% |
| 2023-09-17 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,497 | 100.0% | 24% | 3,729 | 0.0% | 33% |
| 2023-09-17 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,815 | 99.9% | 30% | 1,141 | 0.0% | 39% |
| 2023-09-17 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 59 | 100.0% | 81% | 196 | 0.0% | 53% |
| 2023-09-17 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 8 | 100.0% | 88% | 374 | 0.0% | 25% |
| 2023-09-18 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,040 | 100.0% | 25% | 1,540 | 0.1% | 32% |
| 2023-09-18 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,327 | 100.0% | 36% | 812 | 0.0% | 40% |
| 2023-09-18 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,904 | 100.0% | 50% | 430 | 0.0% | 45% |
| 2023-09-18 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 176 | 100.0% | 85% | 131 | 0.0% | 42% |
| 2023-09-18 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 5 | 100.0% | 100% | none resolved | 0.0% | 20% |
| 2023-09-18 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,769 | 100.0% | 24% | 1,590 | 0.1% | 31% |
| 2023-09-18 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,178 | 100.0% | 33% | 806 | 0.0% | 37% |
| 2023-09-18 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,393 | 100.0% | 49% | 394 | 0.0% | 44% |
| 2023-09-18 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 158 | 100.0% | 87% | 144 | 0.0% | 47% |
| 2023-09-18 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 26 | 100.0% | 73% | 222 | 0.0% | 38% |
| 2023-09-19 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 12,218 | 100.0% | 25% | 1,435 | 0.0% | 32% |
| 2023-09-19 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,598 | 100.0% | 34% | 811 | 0.0% | 40% |
| 2023-09-19 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,249 | 100.0% | 49% | 322 | 0.0% | 46% |
| 2023-09-19 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 114 | 100.0% | 90% | 115 | 0.0% | 55% |
| 2023-09-19 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 4 | 100.0% | 100% | none resolved | 0.0% | 75% |
| 2023-09-19 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,914 | 100.0% | 23% | 1,975 | 0.0% | 32% |
| 2023-09-19 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,254 | 100.0% | 29% | 1,166 | 0.0% | 35% |
| 2023-09-19 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,058 | 100.0% | 40% | 523 | 0.0% | 42% |
| 2023-09-19 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 66 | 100.0% | 85% | 143 | 0.0% | 45% |
| 2023-09-19 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 10 | 100.0% | 90% | 112 | 0.0% | 40% |
| 2023-09-20 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,863 | 100.0% | 22% | 1,848 | 0.0% | 32% |
| 2023-09-20 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,976 | 100.0% | 38% | 946 | 0.0% | 42% |
| 2023-09-20 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,261 | 100.0% | 58% | 322 | 0.0% | 48% |
| 2023-09-20 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 177 | 100.0% | 81% | 136 | 0.0% | 44% |
| 2023-09-20 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 33 | 100.0% | 91% | 112 | 0.0% | 48% |
| 2023-09-20 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,814 | 100.0% | 26% | 2,420 | 0.0% | 32% |
| 2023-09-20 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,828 | 100.0% | 30% | 1,212 | 0.0% | 35% |
| 2023-09-20 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,232 | 100.0% | 39% | 580 | 0.0% | 42% |
| 2023-09-20 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 210 | 100.0% | 84% | 168 | 0.0% | 48% |
| 2023-09-20 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 46 | 100.0% | 89% | 248 | 0.0% | 43% |
| 2023-09-21 | btc_perp_binance_bybit | excluded: binance_bt/binance/BTC-USDT/perp coverage 0.924 below threshold | | | | | | | | |
| 2023-09-21 | eth_perp_binance_bybit | excluded: binance_bt/binance/ETH-USDT/perp coverage 0.924 below threshold | | | | | | | | |
| 2023-09-22 | btc_perp_binance_bybit | excluded: binance_bt/binance/BTC-USDT/perp coverage 0.778 below threshold | | | | | | | | |
| 2023-09-22 | eth_perp_binance_bybit | excluded: binance_bt/binance/ETH-USDT/perp coverage 0.778 below threshold | | | | | | | | |
| 2023-09-23 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 803 | 99.9% | 10% | 37,794 | 0.0% | 33% |
| 2023-09-23 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 668 | 100.0% | 24% | 14,640 | 0.0% | 44% |
| 2023-09-23 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 219 | 100.0% | 40% | 2,322 | 0.0% | 51% |
| 2023-09-23 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 4 | 100.0% | 100% | none resolved | 0.0% | 50% |
| 2023-09-23 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,021 | 100.0% | 12% | 25,446 | 0.0% | 34% |
| 2023-09-23 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 921 | 100.0% | 19% | 10,212 | 0.0% | 42% |
| 2023-09-23 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 463 | 100.0% | 31% | 2,932 | 0.0% | 51% |
| 2023-09-23 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 10 | 100.0% | 70% | 104 | 0.0% | 40% |
| 2023-09-23 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2023-09-24 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,000 | 100.0% | 22% | 3,264 | 0.0% | 32% |
| 2023-09-24 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,515 | 100.0% | 32% | 1,326 | 0.0% | 39% |
| 2023-09-24 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,272 | 100.0% | 51% | 376 | 0.0% | 41% |
| 2023-09-24 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 228 | 100.0% | 84% | 167 | 0.0% | 43% |
| 2023-09-24 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 35 | 100.0% | 94% | 136 | 0.0% | 51% |
| 2023-09-24 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,013 | 100.0% | 28% | 3,020 | 0.0% | 31% |
| 2023-09-24 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,757 | 100.0% | 28% | 1,248 | 0.0% | 35% |
| 2023-09-24 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,633 | 100.0% | 44% | 372 | 0.0% | 47% |
| 2023-09-24 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 74 | 100.0% | 76% | 210 | 0.0% | 38% |
| 2023-09-24 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 12 | 100.0% | 83% | 308 | 0.0% | 25% |
| 2023-09-25 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,798 | 100.0% | 19% | 2,900 | 0.0% | 32% |
| 2023-09-25 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,486 | 100.0% | 29% | 1,511 | 0.0% | 39% |
| 2023-09-25 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,548 | 100.0% | 46% | 602 | 0.0% | 46% |
| 2023-09-25 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 45 | 100.0% | 93% | 118 | 0.0% | 38% |
| 2023-09-25 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,749 | 100.0% | 23% | 2,902 | 0.0% | 33% |
| 2023-09-25 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,054 | 100.0% | 27% | 1,632 | 0.0% | 36% |
| 2023-09-25 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,997 | 100.0% | 37% | 762 | 0.0% | 44% |
| 2023-09-25 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 78 | 100.0% | 91% | 170 | 0.0% | 32% |
| 2023-09-25 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 7 | 100.0% | 43% | 205 | 0.0% | 43% |
| 2023-09-26 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,724 | 100.0% | 15% | 7,120 | 0.0% | 33% |
| 2023-09-26 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,017 | 100.0% | 24% | 2,946 | 0.0% | 41% |
| 2023-09-26 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,495 | 100.0% | 36% | 1,316 | 0.1% | 43% |
| 2023-09-26 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 38 | 100.0% | 61% | 117 | 0.0% | 47% |
| 2023-09-26 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2023-09-26 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,498 | 100.0% | 15% | 5,002 | 0.0% | 35% |
| 2023-09-26 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,658 | 100.0% | 24% | 2,412 | 0.0% | 41% |
| 2023-09-26 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,722 | 100.0% | 37% | 930 | 0.0% | 50% |
| 2023-09-26 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 28 | 100.0% | 93% | 114 | 0.0% | 64% |
| 2023-09-27 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,148 | 100.0% | 22% | 2,450 | 0.0% | 33% |
| 2023-09-27 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,483 | 100.0% | 26% | 1,189 | 0.0% | 38% |
| 2023-09-27 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,468 | 100.0% | 37% | 614 | 0.0% | 40% |
| 2023-09-27 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 296 | 100.0% | 82% | 178 | 0.0% | 46% |
| 2023-09-27 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 43 | 100.0% | 74% | 310 | 0.0% | 56% |
| 2023-09-27 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,557 | 100.0% | 22% | 2,044 | 0.0% | 33% |
| 2023-09-27 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,218 | 100.0% | 31% | 1,061 | 0.0% | 41% |
| 2023-09-27 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,630 | 100.0% | 41% | 534 | 0.0% | 42% |
| 2023-09-27 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 206 | 100.0% | 81% | 164 | 0.0% | 48% |
| 2023-09-27 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 24 | 100.0% | 92% | 142 | 0.0% | 50% |
| 2023-09-28 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,867 | 100.0% | 22% | 1,793 | 0.0% | 34% |
| 2023-09-28 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,934 | 100.0% | 32% | 926 | 0.0% | 39% |
| 2023-09-28 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,583 | 100.0% | 48% | 317 | 0.0% | 45% |
| 2023-09-28 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 193 | 100.0% | 85% | 138 | 0.0% | 48% |
| 2023-09-28 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 12 | 100.0% | 92% | 100 | 0.0% | 67% |
| 2023-09-28 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,452 | 100.0% | 22% | 2,752 | 0.0% | 34% |
| 2023-09-28 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,248 | 100.0% | 25% | 1,420 | 0.0% | 35% |
| 2023-09-28 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,088 | 100.0% | 33% | 610 | 0.0% | 41% |
| 2023-09-28 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 333 | 100.0% | 88% | 119 | 0.0% | 47% |
| 2023-09-28 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 16 | 100.0% | 81% | 130 | 0.0% | 62% |
| 2023-09-29 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,379 | 100.0% | 23% | 3,102 | 0.0% | 33% |
| 2023-09-29 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,177 | 100.0% | 29% | 1,496 | 0.0% | 40% |
| 2023-09-29 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,290 | 100.0% | 44% | 402 | 0.0% | 44% |
| 2023-09-29 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 113 | 100.0% | 88% | 142 | 0.0% | 42% |
| 2023-09-29 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 10 | 100.0% | 80% | 547 | 0.0% | 30% |
| 2023-09-29 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,148 | 100.0% | 24% | 2,077 | 0.0% | 33% |
| 2023-09-29 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,797 | 100.0% | 31% | 1,422 | 0.0% | 40% |
| 2023-09-29 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,729 | 100.0% | 43% | 802 | 0.0% | 44% |
| 2023-09-29 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 165 | 100.0% | 88% | 110 | 0.0% | 38% |
| 2023-09-29 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 22 | 100.0% | 82% | 223 | 0.0% | 50% |
| 2023-09-30 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,960 | 99.9% | 9% | 13,098 | 0.1% | 35% |
| 2023-09-30 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,500 | 100.0% | 21% | 5,086 | 0.1% | 45% |
| 2023-09-30 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 533 | 100.0% | 40% | 1,236 | 0.0% | 46% |
| 2023-09-30 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 2 | 100.0% | 50% | 140 | 0.0% | 100% |
| 2023-09-30 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,722 | 100.0% | 15% | 9,363 | 0.1% | 35% |
| 2023-09-30 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,550 | 100.0% | 16% | 4,998 | 0.0% | 40% |
| 2023-09-30 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,739 | 100.0% | 25% | 1,769 | 0.0% | 44% |
| 2023-09-30 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 61 | 100.0% | 87% | 146 | 0.0% | 39% |
| 2023-09-30 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 10 | 100.0% | 100% | none resolved | 0.0% | 30% |
| 2023-10-01 | aave_perp_binance_bybit | excluded: binance_bt/binance/AAVE-USDT/perp coverage 0.948 below threshold | | | | | | | | |
| 2023-10-01 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,868 | 100.0% | 37% | 934 | 0.0% | 40% |
| 2023-10-01 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 13,868 | 100.0% | 37% | 934 | 0.0% | 40% |
| 2023-10-01 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,030 | 100.0% | 46% | 630 | 0.0% | 44% |
| 2023-10-01 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,983 | 100.0% | 80% | 149 | 0.0% | 52% |
| 2023-10-01 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 185 | 100.0% | 85% | 143 | 0.0% | 50% |
| 2023-10-01 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,091 | 100.0% | 31% | 3,326 | 0.0% | 34% |
| 2023-10-01 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,704 | 100.0% | 32% | 2,394 | 0.0% | 35% |
| 2023-10-01 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,487 | 100.0% | 42% | 1,158 | 0.0% | 41% |
| 2023-10-01 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 701 | 100.0% | 84% | 230 | 0.0% | 45% |
| 2023-10-01 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 283 | 100.0% | 86% | 184 | 0.0% | 51% |
| 2023-10-01 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,089 | 100.0% | 34% | 1,030 | 0.0% | 52% |
| 2023-10-01 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,089 | 100.0% | 34% | 1,030 | 0.0% | 52% |
| 2023-10-01 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 821 | 100.0% | 55% | 231 | 0.0% | 52% |
| 2023-10-01 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 122 | 100.0% | 82% | 212 | 0.0% | 45% |
| 2023-10-01 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 16 | 100.0% | 81% | 301 | 0.0% | 38% |
| 2023-10-01 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,384 | 100.0% | 31% | 1,376 | 0.0% | 36% |
| 2023-10-01 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,854 | 100.0% | 36% | 1,158 | 0.0% | 38% |
| 2023-10-01 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,625 | 100.0% | 43% | 839 | 0.0% | 41% |
| 2023-10-01 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 767 | 100.0% | 83% | 201 | 0.0% | 49% |
| 2023-10-01 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 203 | 100.0% | 83% | 223 | 0.5% | 46% |
| 2023-10-01 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 28,048 | 100.0% | 36% | 752 | 0.0% | 37% |
| 2023-10-01 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 24,053 | 100.0% | 43% | 524 | 0.0% | 41% |
| 2023-10-01 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 18,550 | 100.0% | 52% | 370 | 0.0% | 43% |
| 2023-10-01 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,308 | 100.0% | 82% | 159 | 0.0% | 49% |
| 2023-10-01 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 992 | 100.0% | 89% | 166 | 0.0% | 46% |
| 2023-10-01 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,628 | 100.0% | 36% | 914 | 0.0% | 51% |
| 2023-10-01 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,601 | 100.0% | 36% | 831 | 0.0% | 52% |
| 2023-10-01 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,594 | 100.0% | 39% | 639 | 0.0% | 55% |
| 2023-10-01 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,815 | 100.0% | 62% | 262 | 0.0% | 60% |
| 2023-10-01 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 198 | 100.0% | 84% | 129 | 0.0% | 60% |
| 2023-10-01 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,481 | 100.0% | 41% | 660 | 0.0% | 45% |
| 2023-10-01 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,481 | 100.0% | 41% | 660 | 0.0% | 45% |
| 2023-10-01 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 393 | 100.0% | 62% | 165 | 0.0% | 50% |
| 2023-10-01 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 133 | 100.0% | 71% | 172 | 0.0% | 40% |
| 2023-10-01 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 14 | 100.0% | 100% | none resolved | 0.0% | 57% |
| 2023-10-01 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.792 below threshold | | | | | | | | |
| 2023-10-02 | aave_perp_binance_bybit | ok | 0.998 | gross>0bps | 11,149 | 98.9% | 28% | 708 | 0.0% | 37% |
| 2023-10-02 | aave_perp_binance_bybit | ok | 0.998 | gross>1bps | 11,149 | 98.9% | 28% | 708 | 0.0% | 37% |
| 2023-10-02 | aave_perp_binance_bybit | ok | 0.998 | gross>2bps | 7,270 | 99.3% | 35% | 598 | 0.0% | 42% |
| 2023-10-02 | aave_perp_binance_bybit | ok | 0.998 | gross>5bps | 1,044 | 100.0% | 67% | 246 | 0.3% | 59% |
| 2023-10-02 | aave_perp_binance_bybit | ok | 0.998 | retail_taker | 112 | 100.0% | 79% | 196 | 0.0% | 45% |
| 2023-10-02 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,384 | 100.0% | 28% | 1,144 | 0.0% | 38% |
| 2023-10-02 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 14,384 | 100.0% | 28% | 1,144 | 0.0% | 38% |
| 2023-10-02 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,597 | 100.0% | 33% | 766 | 0.0% | 39% |
| 2023-10-02 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,271 | 100.0% | 55% | 242 | 0.1% | 44% |
| 2023-10-02 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 227 | 100.0% | 75% | 153 | 0.0% | 48% |
| 2023-10-02 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 16,562 | 100.0% | 25% | 1,430 | 0.0% | 31% |
| 2023-10-02 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 13,383 | 100.0% | 32% | 848 | 0.0% | 38% |
| 2023-10-02 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,155 | 100.0% | 46% | 442 | 0.3% | 42% |
| 2023-10-02 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 454 | 100.0% | 82% | 160 | 0.0% | 41% |
| 2023-10-02 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 55 | 100.0% | 76% | 192 | 0.0% | 33% |
| 2023-10-02 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,584 | 100.0% | 32% | 1,421 | 0.0% | 50% |
| 2023-10-02 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,584 | 100.0% | 32% | 1,421 | 0.0% | 50% |
| 2023-10-02 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,654 | 100.0% | 50% | 308 | 0.0% | 54% |
| 2023-10-02 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 297 | 100.0% | 73% | 197 | 0.0% | 43% |
| 2023-10-02 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 171 | 100.0% | 79% | 207 | 0.0% | 48% |
| 2023-10-02 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 9,217 | 100.0% | 25% | 1,636 | 0.1% | 34% |
| 2023-10-02 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,828 | 100.0% | 27% | 1,124 | 0.0% | 34% |
| 2023-10-02 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,550 | 100.0% | 30% | 917 | 0.1% | 35% |
| 2023-10-02 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,648 | 100.0% | 55% | 332 | 0.1% | 46% |
| 2023-10-02 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 156 | 100.0% | 84% | 208 | 0.0% | 46% |
| 2023-10-02 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 30,391 | 100.0% | 31% | 862 | 0.0% | 36% |
| 2023-10-02 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 27,872 | 100.0% | 35% | 660 | 0.0% | 39% |
| 2023-10-02 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 22,417 | 100.0% | 41% | 509 | 0.0% | 42% |
| 2023-10-02 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,980 | 100.0% | 66% | 188 | 0.0% | 48% |
| 2023-10-02 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 531 | 100.0% | 85% | 216 | 0.0% | 47% |
| 2023-10-02 | wld_perp_binance_bybit | excluded: bybit_ob/bybit/WLD-USDT/perp coverage 0.999 below threshold | | | | | | | | |
| 2023-10-02 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,815 | 100.0% | 41% | 446 | 0.0% | 45% |
| 2023-10-02 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,815 | 100.0% | 41% | 446 | 0.0% | 45% |
| 2023-10-02 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 978 | 100.0% | 67% | 199 | 0.0% | 44% |
| 2023-10-02 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 472 | 100.0% | 79% | 208 | 0.0% | 43% |
| 2023-10-02 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 210 | 100.0% | 82% | 214 | 0.0% | 43% |
| 2023-10-02 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.821 below threshold | | | | | | | | |
| 2023-10-03 | aave_perp_binance_bybit | ok | 0.997 | gross>0bps | 9,617 | 99.0% | 32% | 1,121 | 0.0% | 41% |
| 2023-10-03 | aave_perp_binance_bybit | ok | 0.997 | gross>1bps | 9,617 | 99.0% | 32% | 1,121 | 0.0% | 41% |
| 2023-10-03 | aave_perp_binance_bybit | ok | 0.997 | gross>2bps | 5,536 | 99.7% | 41% | 761 | 0.0% | 46% |
| 2023-10-03 | aave_perp_binance_bybit | ok | 0.997 | gross>5bps | 1,157 | 100.0% | 74% | 153 | 0.0% | 52% |
| 2023-10-03 | aave_perp_binance_bybit | ok | 0.997 | retail_taker | 272 | 100.0% | 92% | 134 | 0.0% | 51% |
| 2023-10-03 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,201 | 100.0% | 25% | 1,424 | 0.0% | 39% |
| 2023-10-03 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,201 | 100.0% | 25% | 1,424 | 0.0% | 39% |
| 2023-10-03 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,831 | 100.0% | 32% | 936 | 0.0% | 43% |
| 2023-10-03 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,008 | 100.0% | 59% | 373 | 0.0% | 56% |
| 2023-10-03 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 12 | 100.0% | 100% | none resolved | 0.0% | 75% |
| 2023-10-03 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,472 | 100.0% | 17% | 2,812 | 0.0% | 32% |
| 2023-10-03 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,734 | 100.0% | 27% | 1,620 | 0.0% | 41% |
| 2023-10-03 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,897 | 100.0% | 39% | 738 | 0.0% | 46% |
| 2023-10-03 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 61 | 100.0% | 82% | 139 | 0.0% | 43% |
| 2023-10-03 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 5 | 100.0% | 80% | 103 | 0.0% | 40% |
| 2023-10-03 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,807 | 99.9% | 23% | 2,254 | 0.0% | 55% |
| 2023-10-03 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,807 | 99.9% | 23% | 2,254 | 0.0% | 55% |
| 2023-10-03 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 744 | 100.0% | 45% | 404 | 0.0% | 54% |
| 2023-10-03 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 42 | 100.0% | 98% | 116 | 0.0% | 67% |
| 2023-10-03 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 11 | 100.0% | 100% | none resolved | 0.0% | 64% |
| 2023-10-03 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,718 | 100.0% | 15% | 3,850 | 0.0% | 35% |
| 2023-10-03 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,422 | 100.0% | 19% | 2,528 | 0.0% | 42% |
| 2023-10-03 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,316 | 100.0% | 28% | 1,119 | 0.0% | 48% |
| 2023-10-03 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 71 | 100.0% | 83% | 162 | 0.0% | 55% |
| 2023-10-03 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 2 | 100.0% | 100% | none resolved | 0.0% | 50% |
| 2023-10-03 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 32,062 | 100.0% | 32% | 830 | 0.0% | 37% |
| 2023-10-03 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 27,821 | 100.0% | 38% | 575 | 0.0% | 41% |
| 2023-10-03 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 21,273 | 100.0% | 47% | 390 | 0.0% | 44% |
| 2023-10-03 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,243 | 100.0% | 77% | 164 | 0.0% | 52% |
| 2023-10-03 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 225 | 100.0% | 91% | 164 | 0.0% | 52% |
| 2023-10-03 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 9,520 | 100.0% | 27% | 1,298 | 0.0% | 54% |
| 2023-10-03 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,229 | 100.0% | 25% | 1,150 | 0.0% | 53% |
| 2023-10-03 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,355 | 100.0% | 28% | 862 | 0.0% | 56% |
| 2023-10-03 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,480 | 100.0% | 51% | 436 | 0.0% | 64% |
| 2023-10-03 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 128 | 100.0% | 90% | 118 | 0.0% | 67% |
| 2023-10-03 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,834 | 100.0% | 50% | 250 | 0.0% | 46% |
| 2023-10-03 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,834 | 100.0% | 50% | 250 | 0.0% | 46% |
| 2023-10-03 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,042 | 100.0% | 72% | 150 | 0.0% | 46% |
| 2023-10-03 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 946 | 100.0% | 83% | 125 | 0.0% | 48% |
| 2023-10-03 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 189 | 100.0% | 95% | 118 | 0.0% | 54% |
| 2023-10-03 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.822 below threshold | | | | | | | | |
| 2023-10-04 | aave_perp_binance_bybit | ok | 0.997 | gross>0bps | 9,034 | 98.9% | 26% | 1,036 | 0.0% | 40% |
| 2023-10-04 | aave_perp_binance_bybit | ok | 0.997 | gross>1bps | 9,034 | 98.9% | 26% | 1,036 | 0.0% | 40% |
| 2023-10-04 | aave_perp_binance_bybit | ok | 0.997 | gross>2bps | 5,024 | 99.2% | 35% | 650 | 0.0% | 45% |
| 2023-10-04 | aave_perp_binance_bybit | ok | 0.997 | gross>5bps | 824 | 100.0% | 69% | 178 | 0.0% | 54% |
| 2023-10-04 | aave_perp_binance_bybit | ok | 0.997 | retail_taker | 116 | 100.0% | 89% | 109 | 0.0% | 49% |
| 2023-10-04 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,091 | 100.0% | 28% | 1,216 | 0.0% | 35% |
| 2023-10-04 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,091 | 100.0% | 28% | 1,216 | 0.0% | 35% |
| 2023-10-04 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 9,349 | 100.0% | 32% | 888 | 0.0% | 38% |
| 2023-10-04 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,951 | 100.0% | 63% | 290 | 0.0% | 51% |
| 2023-10-04 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 172 | 100.0% | 85% | 218 | 0.0% | 48% |
| 2023-10-04 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,453 | 100.0% | 20% | 2,575 | 0.0% | 32% |
| 2023-10-04 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,110 | 100.0% | 25% | 2,047 | 0.0% | 37% |
| 2023-10-04 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,485 | 100.0% | 35% | 1,013 | 0.0% | 43% |
| 2023-10-04 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 70 | 100.0% | 77% | 256 | 0.0% | 39% |
| 2023-10-04 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 16 | 100.0% | 75% | 215 | 0.0% | 25% |
| 2023-10-04 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,115 | 100.0% | 25% | 2,262 | 0.0% | 53% |
| 2023-10-04 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,115 | 100.0% | 25% | 2,262 | 0.0% | 53% |
| 2023-10-04 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 994 | 100.0% | 47% | 455 | 0.0% | 56% |
| 2023-10-04 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 141 | 100.0% | 81% | 256 | 0.0% | 44% |
| 2023-10-04 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 69 | 100.0% | 80% | 144 | 0.0% | 41% |
| 2023-10-04 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,836 | 100.0% | 20% | 2,987 | 0.0% | 34% |
| 2023-10-04 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,445 | 100.0% | 23% | 1,792 | 0.0% | 36% |
| 2023-10-04 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,517 | 100.0% | 28% | 926 | 0.0% | 43% |
| 2023-10-04 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 205 | 100.0% | 80% | 158 | 0.0% | 45% |
| 2023-10-04 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 49 | 100.0% | 82% | 626 | 0.0% | 45% |
| 2023-10-04 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 30,139 | 100.0% | 29% | 902 | 0.0% | 38% |
| 2023-10-04 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 25,180 | 100.0% | 38% | 577 | 0.0% | 42% |
| 2023-10-04 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 17,291 | 100.0% | 48% | 352 | 0.0% | 46% |
| 2023-10-04 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,506 | 100.0% | 86% | 127 | 0.0% | 56% |
| 2023-10-04 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 183 | 100.0% | 87% | 286 | 0.0% | 45% |
| 2023-10-04 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,369 | 100.0% | 34% | 936 | 0.0% | 55% |
| 2023-10-04 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,595 | 100.0% | 33% | 814 | 0.0% | 56% |
| 2023-10-04 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,284 | 100.0% | 41% | 582 | 0.0% | 58% |
| 2023-10-04 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,192 | 100.0% | 61% | 376 | 0.0% | 61% |
| 2023-10-04 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 199 | 100.0% | 84% | 134 | 0.0% | 59% |
| 2023-10-04 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,063 | 100.0% | 40% | 413 | 0.0% | 46% |
| 2023-10-04 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,063 | 100.0% | 40% | 413 | 0.0% | 46% |
| 2023-10-04 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,130 | 100.0% | 64% | 153 | 0.0% | 51% |
| 2023-10-04 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 654 | 100.0% | 83% | 130 | 0.0% | 50% |
| 2023-10-04 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 116 | 100.0% | 86% | 160 | 0.0% | 41% |
| 2023-10-04 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.817 below threshold | | | | | | | | |
| 2023-10-05 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 16,749 | 100.0% | 36% | 586 | 0.0% | 40% |
| 2023-10-05 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 16,749 | 100.0% | 36% | 586 | 0.0% | 40% |
| 2023-10-05 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,144 | 100.0% | 46% | 377 | 0.0% | 44% |
| 2023-10-05 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,026 | 100.0% | 72% | 160 | 0.0% | 49% |
| 2023-10-05 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 366 | 100.0% | 90% | 124 | 0.0% | 57% |
| 2023-10-05 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,752 | 100.0% | 24% | 1,513 | 0.0% | 39% |
| 2023-10-05 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,752 | 100.0% | 24% | 1,513 | 0.0% | 39% |
| 2023-10-05 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,057 | 100.0% | 32% | 854 | 0.0% | 42% |
| 2023-10-05 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 500 | 100.0% | 68% | 162 | 0.0% | 53% |
| 2023-10-05 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 12 | 100.0% | 92% | 115 | 0.0% | 67% |
| 2023-10-05 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,385 | 100.0% | 22% | 1,579 | 0.0% | 32% |
| 2023-10-05 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,690 | 100.0% | 32% | 962 | 0.0% | 40% |
| 2023-10-05 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,388 | 100.0% | 47% | 686 | 0.0% | 45% |
| 2023-10-05 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 114 | 100.0% | 83% | 135 | 0.0% | 35% |
| 2023-10-05 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 9 | 100.0% | 89% | 132 | 0.0% | 33% |
| 2023-10-05 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,353 | 100.0% | 20% | 3,869 | 0.0% | 54% |
| 2023-10-05 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,353 | 100.0% | 20% | 3,869 | 0.0% | 54% |
| 2023-10-05 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 580 | 100.0% | 38% | 2,078 | 0.0% | 58% |
| 2023-10-05 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 29 | 100.0% | 72% | 769 | 0.0% | 62% |
| 2023-10-05 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 10 | 100.0% | 80% | 232 | 0.0% | 40% |
| 2023-10-05 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,139 | 100.0% | 26% | 2,464 | 0.0% | 33% |
| 2023-10-05 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,804 | 100.0% | 20% | 1,444 | 0.0% | 33% |
| 2023-10-05 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,151 | 100.0% | 25% | 679 | 0.0% | 41% |
| 2023-10-05 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 198 | 100.0% | 78% | 207 | 0.0% | 47% |
| 2023-10-05 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 46 | 100.0% | 83% | 286 | 0.0% | 33% |
| 2023-10-05 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 23,002 | 100.0% | 27% | 1,078 | 0.0% | 36% |
| 2023-10-05 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 20,028 | 100.0% | 33% | 758 | 0.0% | 39% |
| 2023-10-05 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 14,308 | 100.0% | 41% | 482 | 0.0% | 44% |
| 2023-10-05 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,386 | 100.0% | 80% | 127 | 0.0% | 53% |
| 2023-10-05 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 79 | 100.0% | 91% | 125 | 0.0% | 42% |
| 2023-10-05 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 9,755 | 99.9% | 30% | 1,186 | 0.0% | 56% |
| 2023-10-05 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,135 | 99.9% | 29% | 1,094 | 0.0% | 56% |
| 2023-10-05 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,884 | 99.9% | 33% | 807 | 0.0% | 59% |
| 2023-10-05 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,244 | 99.9% | 49% | 447 | 0.0% | 64% |
| 2023-10-05 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 65 | 100.0% | 97% | 195 | 0.0% | 45% |
| 2023-10-05 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,167 | 100.0% | 45% | 334 | 0.0% | 48% |
| 2023-10-05 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,167 | 100.0% | 45% | 334 | 0.0% | 48% |
| 2023-10-05 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 405 | 100.0% | 69% | 138 | 0.0% | 49% |
| 2023-10-05 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 139 | 100.0% | 85% | 154 | 0.0% | 48% |
| 2023-10-05 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 23 | 100.0% | 91% | 128 | 0.0% | 57% |
| 2023-10-05 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.755 below threshold | | | | | | | | |
| 2023-10-06 | aave_perp_binance_bybit | ok | 0.999 | gross>0bps | 5,792 | 99.4% | 27% | 1,614 | 0.0% | 45% |
| 2023-10-06 | aave_perp_binance_bybit | ok | 0.999 | gross>1bps | 5,792 | 99.4% | 27% | 1,614 | 0.0% | 45% |
| 2023-10-06 | aave_perp_binance_bybit | ok | 0.999 | gross>2bps | 3,364 | 99.6% | 34% | 904 | 0.0% | 47% |
| 2023-10-06 | aave_perp_binance_bybit | ok | 0.999 | gross>5bps | 627 | 100.0% | 63% | 154 | 0.0% | 55% |
| 2023-10-06 | aave_perp_binance_bybit | ok | 0.999 | retail_taker | 84 | 100.0% | 90% | 110 | 0.0% | 38% |
| 2023-10-06 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,780 | 99.9% | 23% | 1,700 | 0.0% | 38% |
| 2023-10-06 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,780 | 99.9% | 23% | 1,700 | 0.0% | 38% |
| 2023-10-06 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,262 | 99.9% | 30% | 1,243 | 0.0% | 43% |
| 2023-10-06 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 466 | 100.0% | 69% | 182 | 0.0% | 53% |
| 2023-10-06 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 15 | 100.0% | 87% | 156 | 0.0% | 53% |
| 2023-10-06 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 12,607 | 100.0% | 21% | 1,572 | 0.0% | 32% |
| 2023-10-06 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,178 | 100.0% | 33% | 924 | 0.0% | 40% |
| 2023-10-06 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,422 | 100.0% | 47% | 480 | 0.0% | 43% |
| 2023-10-06 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 238 | 100.0% | 85% | 162 | 0.0% | 48% |
| 2023-10-06 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 73 | 100.0% | 92% | 282 | 0.0% | 36% |
| 2023-10-06 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,195 | 99.9% | 23% | 4,114 | 0.0% | 57% |
| 2023-10-06 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,195 | 99.9% | 23% | 4,114 | 0.0% | 57% |
| 2023-10-06 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 454 | 100.0% | 48% | 395 | 0.0% | 56% |
| 2023-10-06 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 11 | 100.0% | 82% | 264 | 0.0% | 45% |
| 2023-10-06 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 0% | 115 | 0.0% | 100% |
| 2023-10-06 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,746 | 100.0% | 20% | 2,499 | 0.0% | 34% |
| 2023-10-06 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,978 | 100.0% | 22% | 1,617 | 0.0% | 36% |
| 2023-10-06 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,840 | 100.0% | 30% | 789 | 0.1% | 42% |
| 2023-10-06 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 192 | 100.0% | 71% | 150 | 0.0% | 42% |
| 2023-10-06 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 31 | 100.0% | 77% | 214 | 0.0% | 35% |
| 2023-10-06 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 24,063 | 100.0% | 26% | 1,054 | 0.0% | 36% |
| 2023-10-06 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 20,490 | 100.0% | 33% | 712 | 0.0% | 41% |
| 2023-10-06 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 14,042 | 100.0% | 42% | 514 | 0.0% | 45% |
| 2023-10-06 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,193 | 100.0% | 80% | 127 | 0.0% | 52% |
| 2023-10-06 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 59 | 100.0% | 93% | 132 | 0.0% | 54% |
| 2023-10-06 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,650 | 99.9% | 31% | 1,028 | 0.0% | 54% |
| 2023-10-06 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,969 | 99.9% | 31% | 898 | 0.0% | 54% |
| 2023-10-06 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,451 | 100.0% | 37% | 657 | 0.0% | 57% |
| 2023-10-06 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,400 | 100.0% | 58% | 274 | 0.0% | 62% |
| 2023-10-06 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 142 | 100.0% | 94% | 129 | 0.0% | 65% |
| 2023-10-06 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,411 | 99.9% | 36% | 746 | 0.0% | 50% |
| 2023-10-06 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,411 | 99.9% | 36% | 746 | 0.0% | 50% |
| 2023-10-06 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 323 | 100.0% | 59% | 392 | 0.0% | 50% |
| 2023-10-06 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 85 | 100.0% | 79% | 186 | 0.0% | 39% |
| 2023-10-06 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 13 | 100.0% | 85% | 198 | 0.0% | 38% |
| 2023-10-06 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.761 below threshold | | | | | | | | |
| 2023-10-07 | aave_perp_binance_bybit | ok | 0.998 | gross>0bps | 4,222 | 99.0% | 25% | 2,698 | 0.0% | 46% |
| 2023-10-07 | aave_perp_binance_bybit | ok | 0.998 | gross>1bps | 4,222 | 99.0% | 25% | 2,698 | 0.0% | 46% |
| 2023-10-07 | aave_perp_binance_bybit | ok | 0.998 | gross>2bps | 3,052 | 99.8% | 31% | 1,227 | 0.0% | 48% |
| 2023-10-07 | aave_perp_binance_bybit | ok | 0.998 | gross>5bps | 623 | 100.0% | 64% | 134 | 0.0% | 61% |
| 2023-10-07 | aave_perp_binance_bybit | ok | 0.998 | retail_taker | 96 | 100.0% | 81% | 116 | 0.0% | 68% |
| 2023-10-07 | arb_perp_binance_bybit | ok | 0.999 | gross>0bps | 4,114 | 99.6% | 22% | 3,577 | 0.0% | 41% |
| 2023-10-07 | arb_perp_binance_bybit | ok | 0.999 | gross>1bps | 4,114 | 99.6% | 22% | 3,577 | 0.0% | 41% |
| 2023-10-07 | arb_perp_binance_bybit | ok | 0.999 | gross>2bps | 2,657 | 99.8% | 30% | 2,279 | 0.0% | 49% |
| 2023-10-07 | arb_perp_binance_bybit | ok | 0.999 | gross>5bps | 144 | 100.0% | 78% | 131 | 0.0% | 58% |
| 2023-10-07 | arb_perp_binance_bybit | ok | 0.999 | retail_taker | 9 | 100.0% | 89% | 119 | 0.0% | 67% |
| 2023-10-07 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,513 | 100.0% | 14% | 9,392 | 0.0% | 31% |
| 2023-10-07 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,899 | 100.0% | 19% | 5,917 | 0.0% | 40% |
| 2023-10-07 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 993 | 100.0% | 26% | 2,622 | 0.0% | 44% |
| 2023-10-07 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 5 | 100.0% | 100% | none resolved | 0.0% | 40% |
| 2023-10-07 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 526 | 100.0% | 13% | 14,416 | 0.0% | 56% |
| 2023-10-07 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 526 | 100.0% | 13% | 14,416 | 0.0% | 56% |
| 2023-10-07 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 254 | 100.0% | 24% | 5,670 | 0.0% | 59% |
| 2023-10-07 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 6 | 100.0% | 100% | none resolved | 0.0% | 50% |
| 2023-10-07 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,437 | 100.0% | 10% | 11,290 | 0.0% | 37% |
| 2023-10-07 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,831 | 100.0% | 16% | 6,466 | 0.0% | 46% |
| 2023-10-07 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 969 | 100.0% | 25% | 2,614 | 0.0% | 51% |
| 2023-10-07 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 11 | 100.0% | 73% | 117 | 0.0% | 64% |
| 2023-10-07 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2023-10-07 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,230 | 100.0% | 26% | 1,721 | 0.0% | 37% |
| 2023-10-07 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,496 | 100.0% | 32% | 1,132 | 0.0% | 42% |
| 2023-10-07 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,317 | 100.0% | 40% | 772 | 0.0% | 45% |
| 2023-10-07 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,031 | 100.0% | 77% | 131 | 0.0% | 57% |
| 2023-10-07 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 44 | 100.0% | 93% | 118 | 0.0% | 64% |
| 2023-10-07 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,707 | 99.9% | 26% | 1,370 | 0.0% | 55% |
| 2023-10-07 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,669 | 99.9% | 27% | 1,218 | 0.0% | 56% |
| 2023-10-07 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,843 | 99.9% | 30% | 943 | 0.0% | 59% |
| 2023-10-07 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,954 | 100.0% | 51% | 470 | 0.0% | 65% |
| 2023-10-07 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 52 | 100.0% | 75% | 121 | 0.0% | 79% |
| 2023-10-07 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 595 | 99.8% | 29% | 5,363 | 0.0% | 51% |
| 2023-10-07 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 595 | 99.8% | 29% | 5,363 | 0.0% | 51% |
| 2023-10-07 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 115 | 100.0% | 59% | 3,344 | 0.0% | 56% |
| 2023-10-07 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 12 | 100.0% | 75% | 121 | 0.0% | 75% |
| 2023-10-07 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 2 | 100.0% | 100% | none resolved | 0.0% | 50% |
| 2023-10-07 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.780 below threshold | | | | | | | | |
| 2023-10-08 | aave_perp_binance_bybit | ok | 0.997 | gross>0bps | 3,950 | 98.3% | 26% | 1,760 | 0.0% | 51% |
| 2023-10-08 | aave_perp_binance_bybit | ok | 0.997 | gross>1bps | 3,950 | 98.3% | 26% | 1,760 | 0.0% | 51% |
| 2023-10-08 | aave_perp_binance_bybit | ok | 0.997 | gross>2bps | 1,513 | 98.9% | 43% | 1,114 | 0.0% | 67% |
| 2023-10-08 | aave_perp_binance_bybit | ok | 0.997 | gross>5bps | 92 | 100.0% | 87% | 116 | 0.0% | 84% |
| 2023-10-08 | aave_perp_binance_bybit | ok | 0.997 | retail_taker | 3 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2023-10-08 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,294 | 99.9% | 28% | 2,198 | 0.0% | 43% |
| 2023-10-08 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,294 | 99.9% | 28% | 2,198 | 0.0% | 43% |
| 2023-10-08 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,373 | 99.9% | 36% | 1,210 | 0.0% | 46% |
| 2023-10-08 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 386 | 100.0% | 71% | 362 | 0.0% | 54% |
| 2023-10-08 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 40 | 100.0% | 98% | 151 | 0.0% | 68% |
| 2023-10-08 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,177 | 100.0% | 16% | 5,012 | 0.0% | 32% |
| 2023-10-08 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,170 | 100.0% | 22% | 2,800 | 0.0% | 37% |
| 2023-10-08 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,566 | 100.0% | 34% | 994 | 0.0% | 46% |
| 2023-10-08 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 24 | 100.0% | 67% | 128 | 0.0% | 58% |
| 2023-10-08 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 2 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2023-10-08 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 613 | 99.8% | 29% | 3,617 | 0.0% | 59% |
| 2023-10-08 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 613 | 99.8% | 29% | 3,617 | 0.0% | 59% |
| 2023-10-08 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 152 | 100.0% | 60% | 284 | 0.0% | 61% |
| 2023-10-08 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 5 | 100.0% | 80% | 131 | 0.0% | 100% |
| 2023-10-08 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 2 | 100.0% | 100% | none resolved | 0.0% | 50% |
| 2023-10-08 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,199 | 100.0% | 19% | 6,048 | 0.0% | 32% |
| 2023-10-08 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,343 | 100.0% | 17% | 3,041 | 0.0% | 33% |
| 2023-10-08 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,570 | 100.0% | 22% | 1,345 | 0.0% | 42% |
| 2023-10-08 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 54 | 100.0% | 80% | 260 | 0.0% | 61% |
| 2023-10-08 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 10 | 100.0% | 80% | 102 | 0.0% | 40% |
| 2023-10-08 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,607 | 100.0% | 22% | 2,038 | 0.0% | 36% |
| 2023-10-08 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,642 | 100.0% | 27% | 1,260 | 0.0% | 40% |
| 2023-10-08 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,174 | 100.0% | 33% | 853 | 0.0% | 43% |
| 2023-10-08 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 892 | 100.0% | 66% | 158 | 0.0% | 58% |
| 2023-10-08 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 18 | 100.0% | 89% | 134 | 0.0% | 67% |
| 2023-10-08 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,740 | 99.6% | 22% | 1,924 | 0.0% | 57% |
| 2023-10-08 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,078 | 99.7% | 21% | 1,765 | 0.0% | 57% |
| 2023-10-08 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,970 | 99.7% | 25% | 1,363 | 0.0% | 60% |
| 2023-10-08 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,552 | 100.0% | 36% | 725 | 0.0% | 65% |
| 2023-10-08 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 27 | 100.0% | 81% | 123 | 0.0% | 70% |
| 2023-10-08 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 564 | 100.0% | 34% | 1,456 | 0.0% | 53% |
| 2023-10-08 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 564 | 100.0% | 34% | 1,456 | 0.0% | 53% |
| 2023-10-08 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 109 | 100.0% | 60% | 132 | 0.0% | 59% |
| 2023-10-08 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 21 | 100.0% | 71% | 122 | 0.0% | 71% |
| 2023-10-08 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2023-10-08 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.737 below threshold | | | | | | | | |
| 2023-10-09 | aave_perp_binance_bybit | ok | 0.998 | gross>0bps | 8,889 | 99.5% | 33% | 1,001 | 0.0% | 45% |
| 2023-10-09 | aave_perp_binance_bybit | ok | 0.998 | gross>1bps | 8,889 | 99.5% | 33% | 1,001 | 0.0% | 45% |
| 2023-10-09 | aave_perp_binance_bybit | ok | 0.998 | gross>2bps | 3,843 | 99.7% | 48% | 400 | 0.0% | 55% |
| 2023-10-09 | aave_perp_binance_bybit | ok | 0.998 | gross>5bps | 552 | 100.0% | 78% | 180 | 0.0% | 49% |
| 2023-10-09 | aave_perp_binance_bybit | ok | 0.998 | retail_taker | 139 | 100.0% | 76% | 236 | 0.0% | 46% |
| 2023-10-09 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,417 | 100.0% | 28% | 1,136 | 0.0% | 37% |
| 2023-10-09 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,417 | 100.0% | 28% | 1,136 | 0.0% | 37% |
| 2023-10-09 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,389 | 100.0% | 34% | 658 | 0.0% | 41% |
| 2023-10-09 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,585 | 100.0% | 74% | 186 | 0.0% | 49% |
| 2023-10-09 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 362 | 100.0% | 81% | 180 | 0.0% | 48% |
| 2023-10-09 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,133 | 100.0% | 23% | 2,339 | 0.0% | 31% |
| 2023-10-09 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,403 | 100.0% | 28% | 1,432 | 0.0% | 38% |
| 2023-10-09 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,559 | 100.0% | 41% | 630 | 0.0% | 43% |
| 2023-10-09 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 177 | 100.0% | 72% | 202 | 0.0% | 29% |
| 2023-10-09 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 23 | 100.0% | 65% | 489 | 0.0% | 26% |
| 2023-10-09 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,642 | 100.0% | 35% | 1,191 | 0.0% | 48% |
| 2023-10-09 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,642 | 100.0% | 35% | 1,191 | 0.0% | 48% |
| 2023-10-09 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,249 | 100.0% | 48% | 344 | 0.0% | 47% |
| 2023-10-09 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 611 | 100.0% | 55% | 295 | 0.0% | 43% |
| 2023-10-09 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 202 | 100.0% | 64% | 246 | 0.0% | 40% |
| 2023-10-09 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,962 | 100.0% | 27% | 1,726 | 0.0% | 35% |
| 2023-10-09 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,457 | 100.0% | 36% | 1,025 | 0.0% | 39% |
| 2023-10-09 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,445 | 100.0% | 44% | 648 | 0.0% | 44% |
| 2023-10-09 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 727 | 100.0% | 80% | 190 | 0.0% | 40% |
| 2023-10-09 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 241 | 100.0% | 84% | 408 | 0.0% | 39% |
| 2023-10-09 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 21,398 | 100.0% | 29% | 1,158 | 0.0% | 38% |
| 2023-10-09 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 17,267 | 100.0% | 38% | 728 | 0.0% | 43% |
| 2023-10-09 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,196 | 100.0% | 50% | 448 | 0.0% | 46% |
| 2023-10-09 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,096 | 100.0% | 82% | 164 | 0.0% | 48% |
| 2023-10-09 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 383 | 100.0% | 79% | 200 | 0.0% | 37% |
| 2023-10-09 | wld_perp_binance_bybit | excluded: bybit_ob/bybit/WLD-USDT/perp coverage 0.993 below threshold | | | | | | | | |
| 2023-10-09 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,011 | 100.0% | 49% | 377 | 0.0% | 46% |
| 2023-10-09 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,011 | 100.0% | 49% | 377 | 0.0% | 46% |
| 2023-10-09 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,111 | 100.0% | 56% | 277 | 0.0% | 44% |
| 2023-10-09 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 612 | 100.0% | 82% | 168 | 0.0% | 39% |
| 2023-10-09 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 353 | 100.0% | 80% | 170 | 0.0% | 40% |
| 2023-10-09 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.795 below threshold | | | | | | | | |
| 2023-10-10 | aave_perp_binance_bybit | ok | 0.997 | gross>0bps | 5,734 | 99.5% | 36% | 1,078 | 0.0% | 54% |
| 2023-10-10 | aave_perp_binance_bybit | ok | 0.997 | gross>1bps | 5,734 | 99.5% | 36% | 1,078 | 0.0% | 54% |
| 2023-10-10 | aave_perp_binance_bybit | ok | 0.997 | gross>2bps | 2,075 | 99.9% | 55% | 316 | 0.0% | 62% |
| 2023-10-10 | aave_perp_binance_bybit | ok | 0.997 | gross>5bps | 247 | 100.0% | 85% | 110 | 0.0% | 65% |
| 2023-10-10 | aave_perp_binance_bybit | ok | 0.997 | retail_taker | 68 | 100.0% | 85% | 104 | 0.0% | 51% |
| 2023-10-10 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,147 | 99.9% | 26% | 1,642 | 0.0% | 43% |
| 2023-10-10 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,147 | 99.9% | 26% | 1,642 | 0.0% | 43% |
| 2023-10-10 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,345 | 100.0% | 36% | 1,115 | 0.0% | 47% |
| 2023-10-10 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 238 | 100.0% | 79% | 146 | 0.0% | 55% |
| 2023-10-10 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 11 | 100.0% | 64% | 169 | 0.0% | 36% |
| 2023-10-10 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,764 | 100.0% | 16% | 3,031 | 0.0% | 33% |
| 2023-10-10 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,195 | 100.0% | 29% | 1,289 | 0.0% | 41% |
| 2023-10-10 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,940 | 100.0% | 43% | 492 | 0.0% | 47% |
| 2023-10-10 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 18 | 100.0% | 72% | 139 | 0.0% | 44% |
| 2023-10-10 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2023-10-10 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,423 | 99.9% | 24% | 3,175 | 0.0% | 56% |
| 2023-10-10 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,423 | 99.9% | 24% | 3,175 | 0.0% | 56% |
| 2023-10-10 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 500 | 100.0% | 54% | 333 | 0.0% | 58% |
| 2023-10-10 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 86 | 100.0% | 81% | 208 | 0.0% | 53% |
| 2023-10-10 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 5 | 100.0% | 100% | none resolved | 0.0% | 60% |
| 2023-10-10 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,575 | 100.0% | 18% | 2,056 | 0.0% | 33% |
| 2023-10-10 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,611 | 100.0% | 28% | 1,033 | 0.0% | 43% |
| 2023-10-10 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,959 | 100.0% | 48% | 471 | 0.0% | 48% |
| 2023-10-10 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 91 | 100.0% | 73% | 199 | 0.0% | 29% |
| 2023-10-10 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 36 | 100.0% | 75% | 276 | 0.0% | 47% |
| 2023-10-10 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 16,317 | 100.0% | 24% | 1,318 | 0.0% | 38% |
| 2023-10-10 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 13,125 | 100.0% | 33% | 987 | 0.0% | 43% |
| 2023-10-10 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,234 | 100.0% | 42% | 687 | 0.0% | 48% |
| 2023-10-10 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 315 | 100.0% | 89% | 116 | 0.0% | 49% |
| 2023-10-10 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 24 | 100.0% | 92% | 127 | 0.0% | 62% |
| 2023-10-10 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,458 | 99.9% | 29% | 1,263 | 0.0% | 59% |
| 2023-10-10 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,188 | 99.8% | 29% | 1,044 | 0.0% | 59% |
| 2023-10-10 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,374 | 99.9% | 31% | 767 | 0.0% | 61% |
| 2023-10-10 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,018 | 99.9% | 55% | 392 | 0.0% | 64% |
| 2023-10-10 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 25 | 100.0% | 88% | 111 | 0.0% | 60% |
| 2023-10-10 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,443 | 99.9% | 33% | 1,439 | 0.0% | 49% |
| 2023-10-10 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,443 | 99.9% | 33% | 1,439 | 0.0% | 49% |
| 2023-10-10 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,342 | 99.9% | 33% | 1,453 | 0.0% | 48% |
| 2023-10-10 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 102 | 100.0% | 75% | 263 | 0.0% | 36% |
| 2023-10-10 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 13 | 100.0% | 100% | none resolved | 0.0% | 69% |
| 2023-10-10 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.769 below threshold | | | | | | | | |
| 2023-10-11 | aave_perp_binance_bybit | ok | 0.997 | gross>0bps | 6,792 | 98.9% | 30% | 1,326 | 0.0% | 47% |
| 2023-10-11 | aave_perp_binance_bybit | ok | 0.997 | gross>1bps | 6,792 | 98.9% | 30% | 1,326 | 0.0% | 47% |
| 2023-10-11 | aave_perp_binance_bybit | ok | 0.997 | gross>2bps | 2,774 | 99.5% | 41% | 710 | 0.0% | 53% |
| 2023-10-11 | aave_perp_binance_bybit | ok | 0.997 | gross>5bps | 232 | 100.0% | 84% | 158 | 0.0% | 56% |
| 2023-10-11 | aave_perp_binance_bybit | ok | 0.997 | retail_taker | 49 | 100.0% | 86% | 264 | 0.0% | 63% |
| 2023-10-11 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,752 | 100.0% | 27% | 1,740 | 0.0% | 41% |
| 2023-10-11 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,752 | 100.0% | 27% | 1,740 | 0.0% | 41% |
| 2023-10-11 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,501 | 100.0% | 34% | 1,099 | 0.0% | 46% |
| 2023-10-11 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 378 | 100.0% | 83% | 170 | 0.0% | 50% |
| 2023-10-11 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 29 | 100.0% | 69% | 209 | 0.0% | 45% |
| 2023-10-11 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 9,570 | 100.0% | 23% | 2,181 | 0.0% | 33% |
| 2023-10-11 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,831 | 100.0% | 30% | 1,542 | 0.0% | 37% |
| 2023-10-11 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,893 | 100.0% | 42% | 732 | 0.0% | 42% |
| 2023-10-11 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 272 | 100.0% | 86% | 172 | 0.0% | 41% |
| 2023-10-11 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 41 | 100.0% | 93% | 158 | 0.0% | 39% |
| 2023-10-11 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,133 | 100.0% | 26% | 3,812 | 0.0% | 46% |
| 2023-10-11 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,133 | 100.0% | 26% | 3,812 | 0.0% | 46% |
| 2023-10-11 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,241 | 100.0% | 37% | 1,363 | 0.0% | 51% |
| 2023-10-11 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 384 | 100.0% | 66% | 176 | 0.0% | 52% |
| 2023-10-11 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 35 | 100.0% | 71% | 212 | 0.0% | 37% |
| 2023-10-11 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,200 | 100.0% | 22% | 2,044 | 0.0% | 33% |
| 2023-10-11 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,963 | 100.0% | 25% | 1,126 | 0.0% | 36% |
| 2023-10-11 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,205 | 100.0% | 33% | 565 | 0.0% | 47% |
| 2023-10-11 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 179 | 100.0% | 79% | 178 | 0.0% | 36% |
| 2023-10-11 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 24 | 100.0% | 92% | 738 | 0.0% | 38% |
| 2023-10-11 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 17,554 | 100.0% | 25% | 1,428 | 0.0% | 37% |
| 2023-10-11 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 15,065 | 100.0% | 30% | 1,012 | 0.0% | 41% |
| 2023-10-11 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,506 | 100.0% | 37% | 709 | 0.0% | 45% |
| 2023-10-11 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 839 | 100.0% | 82% | 139 | 0.0% | 53% |
| 2023-10-11 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 80 | 100.0% | 89% | 446 | 0.0% | 46% |
| 2023-10-11 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,181 | 100.0% | 42% | 634 | 0.0% | 54% |
| 2023-10-11 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,144 | 100.0% | 44% | 523 | 0.0% | 55% |
| 2023-10-11 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,223 | 100.0% | 53% | 378 | 0.0% | 57% |
| 2023-10-11 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,670 | 100.0% | 74% | 241 | 0.0% | 62% |
| 2023-10-11 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 194 | 100.0% | 86% | 127 | 0.0% | 62% |
| 2023-10-11 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,118 | 100.0% | 47% | 390 | 0.0% | 48% |
| 2023-10-11 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,118 | 100.0% | 47% | 390 | 0.0% | 48% |
| 2023-10-11 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,118 | 100.0% | 47% | 390 | 0.0% | 48% |
| 2023-10-11 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 193 | 100.0% | 83% | 158 | 0.0% | 43% |
| 2023-10-11 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 51 | 100.0% | 88% | 528 | 0.0% | 39% |
| 2023-10-11 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.807 below threshold | | | | | | | | |
| 2023-10-12 | aave_perp_binance_bybit | ok | 0.996 | gross>0bps | 5,215 | 98.6% | 32% | 1,350 | 0.0% | 52% |
| 2023-10-12 | aave_perp_binance_bybit | ok | 0.996 | gross>1bps | 5,215 | 98.6% | 32% | 1,350 | 0.0% | 52% |
| 2023-10-12 | aave_perp_binance_bybit | ok | 0.996 | gross>2bps | 1,610 | 99.5% | 50% | 450 | 0.0% | 62% |
| 2023-10-12 | aave_perp_binance_bybit | ok | 0.996 | gross>5bps | 117 | 100.0% | 78% | 131 | 0.0% | 55% |
| 2023-10-12 | aave_perp_binance_bybit | ok | 0.996 | retail_taker | 46 | 100.0% | 78% | 169 | 0.0% | 35% |
| 2023-10-12 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,474 | 99.9% | 33% | 1,184 | 0.0% | 45% |
| 2023-10-12 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,474 | 99.9% | 33% | 1,184 | 0.0% | 45% |
| 2023-10-12 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,053 | 99.9% | 47% | 547 | 0.0% | 48% |
| 2023-10-12 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 574 | 100.0% | 75% | 192 | 0.0% | 47% |
| 2023-10-12 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 72 | 100.0% | 75% | 168 | 0.0% | 44% |
| 2023-10-12 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,646 | 100.0% | 16% | 3,366 | 0.0% | 32% |
| 2023-10-12 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,733 | 100.0% | 29% | 1,532 | 0.0% | 42% |
| 2023-10-12 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,585 | 100.0% | 43% | 753 | 0.0% | 45% |
| 2023-10-12 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 45 | 100.0% | 76% | 204 | 0.0% | 49% |
| 2023-10-12 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 4 | 100.0% | 75% | 194 | 0.0% | 50% |
| 2023-10-12 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,444 | 100.0% | 32% | 1,915 | 0.0% | 50% |
| 2023-10-12 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,444 | 100.0% | 32% | 1,915 | 0.0% | 50% |
| 2023-10-12 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 432 | 100.0% | 61% | 228 | 0.0% | 51% |
| 2023-10-12 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 130 | 100.0% | 70% | 204 | 0.0% | 42% |
| 2023-10-12 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 43 | 100.0% | 77% | 208 | 0.0% | 35% |
| 2023-10-12 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,145 | 100.0% | 24% | 2,566 | 0.0% | 32% |
| 2023-10-12 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,379 | 100.0% | 28% | 1,322 | 0.0% | 35% |
| 2023-10-12 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,184 | 100.0% | 34% | 569 | 0.0% | 39% |
| 2023-10-12 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 271 | 100.0% | 82% | 170 | 0.0% | 42% |
| 2023-10-12 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 122 | 100.0% | 84% | 187 | 0.0% | 39% |
| 2023-10-12 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 17,659 | 100.0% | 26% | 1,294 | 0.0% | 39% |
| 2023-10-12 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 13,409 | 100.0% | 37% | 756 | 0.0% | 45% |
| 2023-10-12 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,461 | 100.0% | 51% | 435 | 0.0% | 49% |
| 2023-10-12 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 616 | 100.0% | 83% | 137 | 0.0% | 51% |
| 2023-10-12 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 137 | 100.0% | 83% | 190 | 0.0% | 44% |
| 2023-10-12 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 9,657 | 100.0% | 30% | 951 | 0.0% | 53% |
| 2023-10-12 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,140 | 100.0% | 29% | 819 | 0.0% | 54% |
| 2023-10-12 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,723 | 100.0% | 35% | 635 | 0.0% | 55% |
| 2023-10-12 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,019 | 100.0% | 59% | 285 | 0.0% | 60% |
| 2023-10-12 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 113 | 100.0% | 90% | 129 | 0.0% | 65% |
| 2023-10-12 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,647 | 100.0% | 55% | 175 | 0.0% | 50% |
| 2023-10-12 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,647 | 100.0% | 55% | 175 | 0.0% | 50% |
| 2023-10-12 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,647 | 100.0% | 55% | 175 | 0.0% | 50% |
| 2023-10-12 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 133 | 100.0% | 84% | 208 | 0.0% | 48% |
| 2023-10-12 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 65 | 100.0% | 86% | 522 | 0.0% | 29% |
| 2023-10-12 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.771 below threshold | | | | | | | | |
| 2023-10-13 | aave_perp_binance_bybit | excluded: binance_bt/binance/AAVE-USDT/perp coverage 0.935 below threshold | | | | | | | | |
| 2023-10-13 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,793 | 99.9% | 34% | 1,623 | 0.0% | 44% |
| 2023-10-13 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,793 | 99.9% | 34% | 1,623 | 0.0% | 44% |
| 2023-10-13 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,859 | 99.9% | 50% | 1,100 | 0.0% | 48% |
| 2023-10-13 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 281 | 100.0% | 80% | 163 | 0.0% | 51% |
| 2023-10-13 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 37 | 100.0% | 97% | 165 | 0.0% | 57% |
| 2023-10-13 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,466 | 100.0% | 18% | 3,060 | 0.0% | 32% |
| 2023-10-13 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,666 | 100.0% | 30% | 1,550 | 0.0% | 40% |
| 2023-10-13 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,935 | 100.0% | 44% | 610 | 0.1% | 41% |
| 2023-10-13 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 57 | 100.0% | 74% | 288 | 0.0% | 35% |
| 2023-10-13 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 2 | 100.0% | 50% | 684 | 0.0% | 50% |
| 2023-10-13 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,464 | 100.0% | 35% | 2,374 | 0.0% | 48% |
| 2023-10-13 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,464 | 100.0% | 35% | 2,374 | 0.0% | 48% |
| 2023-10-13 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 680 | 100.0% | 55% | 752 | 0.0% | 53% |
| 2023-10-13 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 245 | 100.0% | 79% | 133 | 0.0% | 49% |
| 2023-10-13 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 56 | 100.0% | 91% | 164 | 0.0% | 54% |
| 2023-10-13 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,868 | 100.0% | 21% | 2,027 | 0.0% | 34% |
| 2023-10-13 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,609 | 100.0% | 33% | 1,269 | 0.0% | 42% |
| 2023-10-13 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,853 | 100.0% | 46% | 967 | 0.0% | 44% |
| 2023-10-13 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 116 | 100.0% | 76% | 196 | 0.0% | 36% |
| 2023-10-13 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 26 | 100.0% | 73% | 278 | 0.0% | 42% |
| 2023-10-13 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,297 | 100.0% | 27% | 1,905 | 0.0% | 37% |
| 2023-10-13 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,070 | 100.0% | 33% | 1,192 | 0.0% | 41% |
| 2023-10-13 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,183 | 100.0% | 43% | 653 | 0.0% | 43% |
| 2023-10-13 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,205 | 100.0% | 69% | 166 | 0.0% | 48% |
| 2023-10-13 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 54 | 100.0% | 78% | 210 | 0.0% | 39% |
| 2023-10-13 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,414 | 100.0% | 32% | 1,293 | 0.0% | 60% |
| 2023-10-13 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,443 | 99.9% | 35% | 984 | 0.0% | 60% |
| 2023-10-13 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,576 | 100.0% | 39% | 742 | 0.0% | 60% |
| 2023-10-13 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,129 | 100.0% | 62% | 253 | 0.0% | 62% |
| 2023-10-13 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 66 | 100.0% | 86% | 137 | 0.0% | 55% |
| 2023-10-13 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,203 | 100.0% | 44% | 424 | 0.0% | 46% |
| 2023-10-13 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,203 | 100.0% | 44% | 424 | 0.0% | 46% |
| 2023-10-13 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,203 | 100.0% | 44% | 424 | 0.0% | 46% |
| 2023-10-13 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 123 | 100.0% | 87% | 184 | 0.0% | 46% |
| 2023-10-13 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 18 | 100.0% | 83% | 128 | 0.0% | 67% |
| 2023-10-13 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.761 below threshold | | | | | | | | |
| 2023-10-14 | aave_perp_binance_bybit | excluded: binance_bt/binance/AAVE-USDT/perp coverage 0.871 below threshold | | | | | | | | |
| 2023-10-14 | arb_perp_binance_bybit | ok | 0.999 | gross>0bps | 1,819 | 99.2% | 31% | 5,098 | 0.0% | 50% |
| 2023-10-14 | arb_perp_binance_bybit | ok | 0.999 | gross>1bps | 1,819 | 99.2% | 31% | 5,098 | 0.0% | 50% |
| 2023-10-14 | arb_perp_binance_bybit | ok | 0.999 | gross>2bps | 773 | 100.0% | 46% | 1,723 | 0.0% | 53% |
| 2023-10-14 | arb_perp_binance_bybit | ok | 0.999 | gross>5bps | 9 | 100.0% | 100% | none resolved | 0.0% | 44% |
| 2023-10-14 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,317 | 99.9% | 14% | 21,779 | 0.0% | 33% |
| 2023-10-14 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 894 | 99.9% | 21% | 9,613 | 0.0% | 43% |
| 2023-10-14 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 416 | 100.0% | 33% | 2,835 | 0.0% | 44% |
| 2023-10-14 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 3 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2023-10-14 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 727 | 100.0% | 20% | 12,834 | 0.0% | 44% |
| 2023-10-14 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 727 | 100.0% | 20% | 12,834 | 0.0% | 44% |
| 2023-10-14 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 517 | 100.0% | 30% | 5,516 | 0.0% | 52% |
| 2023-10-14 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 268 | 100.0% | 46% | 604 | 0.0% | 55% |
| 2023-10-14 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 5 | 100.0% | 100% | none resolved | 0.0% | 40% |
| 2023-10-14 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,812 | 100.0% | 14% | 9,334 | 0.0% | 38% |
| 2023-10-14 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,981 | 99.9% | 21% | 5,394 | 0.0% | 48% |
| 2023-10-14 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 722 | 100.0% | 41% | 1,337 | 0.0% | 52% |
| 2023-10-14 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 15 | 100.0% | 53% | 162 | 0.0% | 73% |
| 2023-10-14 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 3 | 100.0% | 100% | none resolved | 0.0% | 67% |
| 2023-10-14 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,802 | 100.0% | 25% | 3,271 | 0.0% | 39% |
| 2023-10-14 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,615 | 100.0% | 29% | 2,028 | 0.0% | 44% |
| 2023-10-14 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,233 | 100.0% | 41% | 962 | 0.0% | 51% |
| 2023-10-14 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 235 | 100.0% | 90% | 115 | 0.0% | 60% |
| 2023-10-14 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 32 | 100.0% | 84% | 108 | 0.0% | 72% |
| 2023-10-14 | wld_perp_binance_bybit | ok | 0.999 | gross>0bps | 3,184 | 99.1% | 28% | 2,878 | 0.0% | 63% |
| 2023-10-14 | wld_perp_binance_bybit | ok | 0.999 | gross>1bps | 2,539 | 99.3% | 29% | 2,401 | 0.0% | 62% |
| 2023-10-14 | wld_perp_binance_bybit | ok | 0.999 | gross>2bps | 2,040 | 99.6% | 33% | 1,925 | 0.0% | 66% |
| 2023-10-14 | wld_perp_binance_bybit | ok | 0.999 | gross>5bps | 338 | 100.0% | 59% | 489 | 0.0% | 69% |
| 2023-10-14 | wld_perp_binance_bybit | ok | 0.999 | retail_taker | 11 | 100.0% | 100% | none resolved | 0.0% | 73% |
| 2023-10-14 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 308 | 100.0% | 56% | 243 | 0.0% | 57% |
| 2023-10-14 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 308 | 100.0% | 56% | 243 | 0.0% | 57% |
| 2023-10-14 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 308 | 100.0% | 56% | 243 | 0.0% | 57% |
| 2023-10-14 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 10 | 100.0% | 100% | none resolved | 0.0% | 20% |
| 2023-10-14 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 2 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2023-10-14 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.653 below threshold | | | | | | | | |
| 2023-10-15 | aave_perp_binance_bybit | excluded: binance_bt/binance/AAVE-USDT/perp coverage 0.914 below threshold | | | | | | | | |
| 2023-10-15 | arb_perp_binance_bybit | ok | 0.998 | gross>0bps | 2,844 | 99.2% | 29% | 3,200 | 0.0% | 47% |
| 2023-10-15 | arb_perp_binance_bybit | ok | 0.998 | gross>1bps | 2,844 | 99.2% | 29% | 3,200 | 0.0% | 47% |
| 2023-10-15 | arb_perp_binance_bybit | ok | 0.998 | gross>2bps | 1,316 | 99.6% | 46% | 1,248 | 0.0% | 52% |
| 2023-10-15 | arb_perp_binance_bybit | ok | 0.998 | gross>5bps | 34 | 100.0% | 91% | 302 | 0.0% | 56% |
| 2023-10-15 | arb_perp_binance_bybit | ok | 0.998 | retail_taker | 11 | 100.0% | 82% | 300 | 0.0% | 64% |
| 2023-10-15 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,213 | 99.9% | 17% | 5,400 | 0.0% | 31% |
| 2023-10-15 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,822 | 99.9% | 19% | 4,230 | 0.0% | 37% |
| 2023-10-15 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,077 | 99.9% | 30% | 1,978 | 0.0% | 36% |
| 2023-10-15 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 88 | 100.0% | 69% | 232 | 0.0% | 41% |
| 2023-10-15 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 25 | 100.0% | 80% | 727 | 0.0% | 40% |
| 2023-10-15 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 726 | 100.0% | 21% | 10,702 | 0.0% | 46% |
| 2023-10-15 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 726 | 100.0% | 21% | 10,702 | 0.0% | 46% |
| 2023-10-15 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 417 | 100.0% | 29% | 3,310 | 0.0% | 53% |
| 2023-10-15 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 150 | 100.0% | 45% | 908 | 0.0% | 57% |
| 2023-10-15 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 4 | 100.0% | 50% | 371 | 0.0% | 75% |
| 2023-10-15 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,215 | 100.0% | 17% | 3,996 | 0.0% | 36% |
| 2023-10-15 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,101 | 100.0% | 28% | 2,110 | 0.0% | 45% |
| 2023-10-15 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,299 | 100.0% | 40% | 1,028 | 0.0% | 48% |
| 2023-10-15 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 38 | 100.0% | 79% | 162 | 0.0% | 37% |
| 2023-10-15 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 6 | 100.0% | 83% | 497 | 0.0% | 17% |
| 2023-10-15 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,686 | 99.9% | 25% | 2,234 | 0.0% | 40% |
| 2023-10-15 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,625 | 100.0% | 34% | 1,481 | 0.0% | 47% |
| 2023-10-15 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,797 | 100.0% | 45% | 692 | 0.0% | 52% |
| 2023-10-15 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 198 | 100.0% | 81% | 139 | 0.0% | 58% |
| 2023-10-15 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 33 | 100.0% | 91% | 323 | 0.0% | 64% |
| 2023-10-15 | wld_perp_binance_bybit | ok | 0.999 | gross>0bps | 4,966 | 99.5% | 35% | 2,152 | 0.0% | 60% |
| 2023-10-15 | wld_perp_binance_bybit | ok | 0.999 | gross>1bps | 4,314 | 99.6% | 36% | 1,658 | 0.0% | 61% |
| 2023-10-15 | wld_perp_binance_bybit | ok | 0.999 | gross>2bps | 3,135 | 99.7% | 42% | 1,234 | 0.0% | 62% |
| 2023-10-15 | wld_perp_binance_bybit | ok | 0.999 | gross>5bps | 887 | 100.0% | 64% | 436 | 0.0% | 65% |
| 2023-10-15 | wld_perp_binance_bybit | ok | 0.999 | retail_taker | 74 | 100.0% | 76% | 214 | 0.0% | 47% |
| 2023-10-15 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 477 | 100.0% | 40% | 1,197 | 0.0% | 52% |
| 2023-10-15 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 477 | 100.0% | 40% | 1,197 | 0.0% | 52% |
| 2023-10-15 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 477 | 100.0% | 40% | 1,197 | 0.0% | 52% |
| 2023-10-15 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 16 | 100.0% | 69% | 199 | 0.0% | 50% |
| 2023-10-15 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 6 | 100.0% | 50% | 154 | 0.0% | 50% |
| 2023-10-15 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.751 below threshold | | | | | | | | |
| 2023-10-16 | aave_perp_binance_bybit | ok | 0.997 | gross>0bps | 8,083 | 99.0% | 40% | 695 | 0.0% | 42% |
| 2023-10-16 | aave_perp_binance_bybit | ok | 0.997 | gross>1bps | 8,083 | 99.0% | 40% | 695 | 0.0% | 42% |
| 2023-10-16 | aave_perp_binance_bybit | ok | 0.997 | gross>2bps | 3,114 | 99.5% | 55% | 434 | 0.0% | 49% |
| 2023-10-16 | aave_perp_binance_bybit | ok | 0.997 | gross>5bps | 552 | 100.0% | 75% | 188 | 0.0% | 41% |
| 2023-10-16 | aave_perp_binance_bybit | ok | 0.997 | retail_taker | 170 | 100.0% | 72% | 154 | 0.0% | 35% |
| 2023-10-16 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,340 | 100.0% | 34% | 1,456 | 0.1% | 39% |
| 2023-10-16 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,340 | 100.0% | 34% | 1,456 | 0.1% | 39% |
| 2023-10-16 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,618 | 100.0% | 41% | 825 | 0.2% | 38% |
| 2023-10-16 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,702 | 100.0% | 69% | 206 | 1.0% | 42% |
| 2023-10-16 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 234 | 100.0% | 77% | 222 | 10.7% | 35% |
| 2023-10-16 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 24,497 | 100.0% | 45% | 880 | 0.2% | 33% |
| 2023-10-16 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 21,377 | 100.0% | 51% | 539 | 0.2% | 36% |
| 2023-10-16 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 15,490 | 100.0% | 60% | 300 | 0.3% | 39% |
| 2023-10-16 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,329 | 100.0% | 83% | 187 | 1.2% | 41% |
| 2023-10-16 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 1,241 | 100.0% | 85% | 213 | 3.5% | 41% |
| 2023-10-16 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,538 | 100.0% | 35% | 623 | 0.0% | 38% |
| 2023-10-16 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,538 | 100.0% | 35% | 623 | 0.0% | 38% |
| 2023-10-16 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,973 | 100.0% | 48% | 314 | 0.0% | 42% |
| 2023-10-16 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 684 | 100.0% | 65% | 222 | 0.0% | 37% |
| 2023-10-16 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 159 | 100.0% | 85% | 191 | 0.0% | 36% |
| 2023-10-16 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 15,245 | 100.0% | 42% | 886 | 0.0% | 34% |
| 2023-10-16 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 15,122 | 100.0% | 43% | 503 | 0.0% | 33% |
| 2023-10-16 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,137 | 100.0% | 54% | 285 | 0.0% | 38% |
| 2023-10-16 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,349 | 100.0% | 83% | 211 | 0.0% | 38% |
| 2023-10-16 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 327 | 100.0% | 81% | 227 | 0.0% | 32% |
| 2023-10-16 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 28,189 | 100.0% | 36% | 980 | 0.2% | 36% |
| 2023-10-16 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 26,231 | 100.0% | 41% | 739 | 0.2% | 38% |
| 2023-10-16 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 21,220 | 100.0% | 46% | 541 | 0.2% | 41% |
| 2023-10-16 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 5,407 | 100.0% | 77% | 170 | 1.1% | 44% |
| 2023-10-16 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 877 | 100.0% | 85% | 188 | 4.3% | 43% |
| 2023-10-16 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 12,532 | 99.9% | 43% | 730 | 0.0% | 53% |
| 2023-10-16 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,808 | 99.9% | 47% | 578 | 0.0% | 53% |
| 2023-10-16 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,258 | 100.0% | 51% | 372 | 0.0% | 53% |
| 2023-10-16 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,687 | 100.0% | 64% | 240 | 0.0% | 50% |
| 2023-10-16 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 426 | 100.0% | 82% | 141 | 0.0% | 44% |
| 2023-10-16 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,852 | 100.0% | 40% | 632 | 0.0% | 39% |
| 2023-10-16 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,852 | 100.0% | 40% | 632 | 0.0% | 39% |
| 2023-10-16 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,484 | 100.0% | 40% | 645 | 0.0% | 40% |
| 2023-10-16 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 695 | 100.0% | 74% | 180 | 0.0% | 39% |
| 2023-10-16 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 134 | 100.0% | 75% | 172 | 0.0% | 33% |
| 2023-10-16 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.802 below threshold | | | | | | | | |
| 2023-10-17 | aave_perp_binance_bybit | ok | 0.995 | gross>0bps | 4,606 | 98.6% | 28% | 1,394 | 0.0% | 42% |
| 2023-10-17 | aave_perp_binance_bybit | ok | 0.995 | gross>1bps | 4,606 | 98.6% | 28% | 1,394 | 0.0% | 42% |
| 2023-10-17 | aave_perp_binance_bybit | ok | 0.995 | gross>2bps | 1,903 | 99.4% | 40% | 597 | 0.0% | 53% |
| 2023-10-17 | aave_perp_binance_bybit | ok | 0.995 | gross>5bps | 310 | 100.0% | 76% | 182 | 0.0% | 48% |
| 2023-10-17 | aave_perp_binance_bybit | ok | 0.995 | retail_taker | 120 | 100.0% | 83% | 170 | 0.0% | 46% |
| 2023-10-17 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,931 | 99.9% | 35% | 1,624 | 0.0% | 45% |
| 2023-10-17 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,931 | 99.9% | 35% | 1,624 | 0.0% | 45% |
| 2023-10-17 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,815 | 100.0% | 45% | 1,039 | 0.0% | 52% |
| 2023-10-17 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 306 | 100.0% | 79% | 258 | 0.0% | 47% |
| 2023-10-17 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 94 | 100.0% | 79% | 145 | 0.0% | 40% |
| 2023-10-17 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 12,838 | 100.0% | 21% | 2,040 | 0.0% | 30% |
| 2023-10-17 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,771 | 100.0% | 35% | 904 | 0.0% | 41% |
| 2023-10-17 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,671 | 100.0% | 58% | 314 | 0.0% | 48% |
| 2023-10-17 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 88 | 100.0% | 73% | 160 | 0.0% | 38% |
| 2023-10-17 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 14 | 100.0% | 86% | 243 | 0.0% | 36% |
| 2023-10-17 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,826 | 100.0% | 25% | 2,453 | 0.0% | 40% |
| 2023-10-17 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,826 | 100.0% | 25% | 2,453 | 0.0% | 40% |
| 2023-10-17 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,035 | 100.0% | 40% | 1,593 | 0.0% | 50% |
| 2023-10-17 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 386 | 100.0% | 61% | 409 | 0.0% | 45% |
| 2023-10-17 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 67 | 100.0% | 72% | 180 | 0.0% | 45% |
| 2023-10-17 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,488 | 100.0% | 25% | 4,749 | 0.0% | 31% |
| 2023-10-17 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,938 | 100.0% | 22% | 2,274 | 0.0% | 28% |
| 2023-10-17 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,518 | 100.0% | 24% | 966 | 0.0% | 35% |
| 2023-10-17 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 224 | 100.0% | 77% | 278 | 0.0% | 44% |
| 2023-10-17 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 42 | 100.0% | 81% | 194 | 0.0% | 43% |
| 2023-10-17 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 26,698 | 100.0% | 28% | 1,050 | 0.0% | 38% |
| 2023-10-17 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 22,178 | 100.0% | 36% | 716 | 0.0% | 42% |
| 2023-10-17 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 15,235 | 100.0% | 46% | 504 | 0.0% | 45% |
| 2023-10-17 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,261 | 100.0% | 83% | 147 | 0.0% | 53% |
| 2023-10-17 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 155 | 100.0% | 85% | 163 | 0.0% | 48% |
| 2023-10-17 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,806 | 99.9% | 38% | 914 | 0.0% | 56% |
| 2023-10-17 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,912 | 99.9% | 39% | 797 | 0.0% | 57% |
| 2023-10-17 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,695 | 100.0% | 47% | 535 | 0.0% | 59% |
| 2023-10-17 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,153 | 100.0% | 74% | 218 | 0.0% | 63% |
| 2023-10-17 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 159 | 100.0% | 79% | 186 | 0.0% | 47% |
| 2023-10-17 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,126 | 100.0% | 53% | 350 | 0.0% | 48% |
| 2023-10-17 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,126 | 100.0% | 53% | 350 | 0.0% | 48% |
| 2023-10-17 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,126 | 100.0% | 53% | 350 | 0.0% | 48% |
| 2023-10-17 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 162 | 100.0% | 76% | 155 | 0.0% | 45% |
| 2023-10-17 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 51 | 100.0% | 86% | 249 | 0.0% | 51% |
| 2023-10-17 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.802 below threshold | | | | | | | | |
| 2023-10-18 | aave_perp_binance_bybit | excluded: binance_bt/binance/AAVE-USDT/perp coverage 0.946 below threshold | | | | | | | | |
| 2023-10-18 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,087 | 99.9% | 31% | 1,952 | 0.0% | 46% |
| 2023-10-18 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,087 | 99.9% | 31% | 1,952 | 0.0% | 46% |
| 2023-10-18 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,366 | 99.9% | 41% | 1,447 | 0.0% | 48% |
| 2023-10-18 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 319 | 100.0% | 71% | 272 | 0.0% | 54% |
| 2023-10-18 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 21 | 100.0% | 86% | 834 | 0.0% | 43% |
| 2023-10-18 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 9,968 | 100.0% | 22% | 2,382 | 0.0% | 30% |
| 2023-10-18 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,433 | 100.0% | 32% | 1,248 | 0.0% | 38% |
| 2023-10-18 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,374 | 100.0% | 50% | 396 | 0.0% | 41% |
| 2023-10-18 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 252 | 100.0% | 82% | 146 | 0.0% | 42% |
| 2023-10-18 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 38 | 100.0% | 89% | 788 | 0.0% | 61% |
| 2023-10-18 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,235 | 99.9% | 26% | 2,844 | 0.0% | 49% |
| 2023-10-18 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,235 | 99.9% | 26% | 2,844 | 0.0% | 49% |
| 2023-10-18 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 485 | 99.8% | 43% | 2,292 | 0.0% | 47% |
| 2023-10-18 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 212 | 100.0% | 49% | 873 | 0.0% | 50% |
| 2023-10-18 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 45 | 100.0% | 76% | 201 | 0.0% | 20% |
| 2023-10-18 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,044 | 100.0% | 25% | 4,304 | 0.0% | 31% |
| 2023-10-18 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,549 | 100.0% | 20% | 2,075 | 0.0% | 27% |
| 2023-10-18 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,991 | 100.0% | 26% | 1,043 | 0.0% | 36% |
| 2023-10-18 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 350 | 100.0% | 52% | 612 | 0.0% | 46% |
| 2023-10-18 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 21 | 100.0% | 81% | 903 | 0.0% | 43% |
| 2023-10-18 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 19,278 | 100.0% | 27% | 1,348 | 0.0% | 37% |
| 2023-10-18 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 15,486 | 100.0% | 35% | 914 | 0.0% | 42% |
| 2023-10-18 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 9,672 | 100.0% | 44% | 595 | 0.0% | 47% |
| 2023-10-18 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 441 | 100.0% | 85% | 122 | 0.0% | 53% |
| 2023-10-18 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 67 | 100.0% | 84% | 149 | 0.0% | 43% |
| 2023-10-18 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,202 | 100.0% | 36% | 1,090 | 0.0% | 56% |
| 2023-10-18 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,635 | 100.0% | 37% | 910 | 0.0% | 57% |
| 2023-10-18 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,866 | 100.0% | 45% | 652 | 0.0% | 60% |
| 2023-10-18 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,540 | 100.0% | 68% | 232 | 0.0% | 66% |
| 2023-10-18 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 104 | 100.0% | 92% | 131 | 0.0% | 73% |
| 2023-10-18 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 884 | 100.0% | 46% | 554 | 0.0% | 49% |
| 2023-10-18 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 884 | 100.0% | 46% | 554 | 0.0% | 49% |
| 2023-10-18 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 884 | 100.0% | 46% | 554 | 0.0% | 49% |
| 2023-10-18 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 59 | 100.0% | 80% | 139 | 0.0% | 44% |
| 2023-10-18 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 22 | 100.0% | 95% | 1,261 | 0.0% | 32% |
| 2023-10-18 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.769 below threshold | | | | | | | | |
| 2023-10-19 | aave_perp_binance_bybit | excluded: binance_bt/binance/AAVE-USDT/perp coverage 0.945 below threshold | | | | | | | | |
| 2023-10-19 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,609 | 99.8% | 35% | 1,626 | 0.0% | 49% |
| 2023-10-19 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,609 | 99.8% | 35% | 1,626 | 0.0% | 49% |
| 2023-10-19 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,368 | 99.9% | 49% | 1,047 | 0.0% | 53% |
| 2023-10-19 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 351 | 100.0% | 75% | 190 | 0.0% | 47% |
| 2023-10-19 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 72 | 100.0% | 76% | 152 | 0.0% | 39% |
| 2023-10-19 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,475 | 100.0% | 23% | 1,920 | 0.0% | 30% |
| 2023-10-19 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,626 | 100.0% | 28% | 1,056 | 0.0% | 34% |
| 2023-10-19 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,460 | 100.0% | 45% | 408 | 0.0% | 44% |
| 2023-10-19 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 111 | 100.0% | 82% | 174 | 0.0% | 45% |
| 2023-10-19 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 10 | 100.0% | 80% | 102 | 0.0% | 50% |
| 2023-10-19 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,433 | 100.0% | 21% | 4,139 | 0.0% | 38% |
| 2023-10-19 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,433 | 100.0% | 21% | 4,139 | 0.0% | 38% |
| 2023-10-19 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,074 | 100.0% | 29% | 1,612 | 0.0% | 39% |
| 2023-10-19 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 615 | 100.0% | 36% | 431 | 0.0% | 47% |
| 2023-10-19 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 49 | 100.0% | 80% | 298 | 0.0% | 33% |
| 2023-10-19 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,095 | 100.0% | 24% | 2,762 | 0.0% | 32% |
| 2023-10-19 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,534 | 100.0% | 30% | 1,154 | 0.0% | 35% |
| 2023-10-19 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,846 | 100.0% | 36% | 756 | 0.0% | 38% |
| 2023-10-19 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 168 | 100.0% | 83% | 164 | 0.0% | 37% |
| 2023-10-19 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 19 | 100.0% | 89% | 208 | 0.0% | 53% |
| 2023-10-19 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 30,638 | 100.0% | 31% | 805 | 0.0% | 36% |
| 2023-10-19 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 25,216 | 100.0% | 39% | 502 | 0.0% | 42% |
| 2023-10-19 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 16,041 | 100.0% | 51% | 307 | 0.0% | 46% |
| 2023-10-19 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,383 | 100.0% | 88% | 119 | 0.0% | 51% |
| 2023-10-19 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 307 | 100.0% | 88% | 158 | 0.0% | 53% |
| 2023-10-19 | wld_perp_binance_bybit | excluded: bybit_ob/bybit/WLD-USDT/perp coverage 0.993 below threshold | | | | | | | | |
| 2023-10-19 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,818 | 100.0% | 50% | 318 | 0.0% | 41% |
| 2023-10-19 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,818 | 100.0% | 50% | 318 | 0.0% | 41% |
| 2023-10-19 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,044 | 100.0% | 58% | 252 | 0.0% | 44% |
| 2023-10-19 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,332 | 100.0% | 78% | 129 | 0.0% | 46% |
| 2023-10-19 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 201 | 100.0% | 95% | 194 | 0.0% | 45% |
| 2023-10-19 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.768 below threshold | | | | | | | | |
| 2023-10-20 | aave_perp_binance_bybit | ok | 0.999 | gross>0bps | 13,041 | 99.7% | 36% | 483 | 0.0% | 36% |
| 2023-10-20 | aave_perp_binance_bybit | ok | 0.999 | gross>1bps | 13,041 | 99.7% | 36% | 483 | 0.0% | 36% |
| 2023-10-20 | aave_perp_binance_bybit | ok | 0.999 | gross>2bps | 7,905 | 99.8% | 45% | 322 | 0.0% | 40% |
| 2023-10-20 | aave_perp_binance_bybit | ok | 0.999 | gross>5bps | 2,736 | 100.0% | 64% | 170 | 0.0% | 44% |
| 2023-10-20 | aave_perp_binance_bybit | ok | 0.999 | retail_taker | 495 | 100.0% | 89% | 121 | 0.0% | 52% |
| 2023-10-20 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,737 | 99.9% | 26% | 1,498 | 0.0% | 39% |
| 2023-10-20 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,737 | 99.9% | 26% | 1,498 | 0.0% | 39% |
| 2023-10-20 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,954 | 100.0% | 36% | 1,002 | 0.0% | 45% |
| 2023-10-20 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 565 | 100.0% | 72% | 226 | 0.0% | 53% |
| 2023-10-20 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 15 | 100.0% | 93% | 114 | 0.0% | 60% |
| 2023-10-20 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 16,946 | 100.0% | 29% | 1,280 | 0.0% | 30% |
| 2023-10-20 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 14,957 | 100.0% | 29% | 1,067 | 0.0% | 32% |
| 2023-10-20 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,050 | 100.0% | 40% | 462 | 0.0% | 39% |
| 2023-10-20 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 643 | 100.0% | 88% | 146 | 0.2% | 47% |
| 2023-10-20 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 48 | 100.0% | 81% | 423 | 0.0% | 50% |
| 2023-10-20 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,917 | 99.9% | 25% | 1,968 | 0.0% | 43% |
| 2023-10-20 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,917 | 99.9% | 25% | 1,968 | 0.0% | 43% |
| 2023-10-20 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 876 | 100.0% | 31% | 614 | 0.0% | 47% |
| 2023-10-20 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 198 | 100.0% | 54% | 344 | 0.0% | 41% |
| 2023-10-20 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 8 | 100.0% | 88% | 134 | 0.0% | 50% |
| 2023-10-20 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 15,496 | 100.0% | 23% | 1,537 | 0.0% | 31% |
| 2023-10-20 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,364 | 100.0% | 34% | 639 | 0.0% | 39% |
| 2023-10-20 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,804 | 100.0% | 58% | 233 | 0.0% | 45% |
| 2023-10-20 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 116 | 100.0% | 78% | 158 | 0.0% | 47% |
| 2023-10-20 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 11 | 100.0% | 82% | 230 | 0.0% | 55% |
| 2023-10-20 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 41,344 | 100.0% | 33% | 717 | 0.0% | 34% |
| 2023-10-20 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 36,743 | 100.0% | 38% | 568 | 0.0% | 38% |
| 2023-10-20 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 24,444 | 100.0% | 49% | 388 | 0.0% | 43% |
| 2023-10-20 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,555 | 100.0% | 84% | 133 | 0.0% | 53% |
| 2023-10-20 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 235 | 100.0% | 93% | 142 | 0.0% | 54% |
| 2023-10-20 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,677 | 100.0% | 40% | 728 | 0.0% | 56% |
| 2023-10-20 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,395 | 99.9% | 42% | 647 | 0.1% | 56% |
| 2023-10-20 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,427 | 100.0% | 50% | 472 | 0.1% | 59% |
| 2023-10-20 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,163 | 100.0% | 76% | 196 | 0.2% | 66% |
| 2023-10-20 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 79 | 100.0% | 90% | 121 | 0.0% | 71% |
| 2023-10-20 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,214 | 100.0% | 42% | 475 | 0.0% | 46% |
| 2023-10-20 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,214 | 100.0% | 42% | 475 | 0.0% | 46% |
| 2023-10-20 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,316 | 100.0% | 66% | 169 | 0.0% | 51% |
| 2023-10-20 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 305 | 100.0% | 77% | 131 | 0.0% | 50% |
| 2023-10-20 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 51 | 100.0% | 86% | 130 | 0.0% | 41% |
| 2023-10-20 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.861 below threshold | | | | | | | | |
| 2023-10-21 | aave_perp_binance_bybit | ok | 0.998 | gross>0bps | 8,241 | 99.4% | 31% | 846 | 0.0% | 42% |
| 2023-10-21 | aave_perp_binance_bybit | ok | 0.998 | gross>1bps | 8,241 | 99.4% | 31% | 846 | 0.0% | 42% |
| 2023-10-21 | aave_perp_binance_bybit | ok | 0.998 | gross>2bps | 4,427 | 99.7% | 42% | 455 | 0.0% | 50% |
| 2023-10-21 | aave_perp_binance_bybit | ok | 0.998 | gross>5bps | 928 | 99.9% | 77% | 160 | 0.0% | 59% |
| 2023-10-21 | aave_perp_binance_bybit | ok | 0.998 | retail_taker | 95 | 100.0% | 83% | 114 | 0.0% | 58% |
| 2023-10-21 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,060 | 99.9% | 27% | 1,634 | 0.0% | 41% |
| 2023-10-21 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,060 | 99.9% | 27% | 1,634 | 0.0% | 41% |
| 2023-10-21 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,849 | 99.8% | 36% | 1,228 | 0.0% | 47% |
| 2023-10-21 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 281 | 100.0% | 84% | 207 | 0.0% | 55% |
| 2023-10-21 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 46 | 100.0% | 83% | 357 | 0.0% | 41% |
| 2023-10-21 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,798 | 100.0% | 21% | 1,918 | 0.0% | 30% |
| 2023-10-21 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,277 | 100.0% | 30% | 1,116 | 0.0% | 36% |
| 2023-10-21 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,454 | 100.0% | 38% | 1,010 | 0.0% | 43% |
| 2023-10-21 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 118 | 100.0% | 80% | 126 | 0.0% | 42% |
| 2023-10-21 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 5 | 100.0% | 60% | 157 | 0.0% | 40% |
| 2023-10-21 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,692 | 100.0% | 32% | 1,650 | 0.0% | 48% |
| 2023-10-21 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,692 | 100.0% | 32% | 1,650 | 0.0% | 48% |
| 2023-10-21 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 608 | 100.0% | 48% | 453 | 0.0% | 52% |
| 2023-10-21 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 50 | 100.0% | 74% | 213 | 0.0% | 44% |
| 2023-10-21 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 16 | 100.0% | 75% | 295 | 0.0% | 44% |
| 2023-10-21 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,842 | 100.0% | 21% | 2,208 | 0.0% | 32% |
| 2023-10-21 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,540 | 100.0% | 29% | 1,410 | 0.0% | 40% |
| 2023-10-21 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,556 | 100.0% | 41% | 558 | 0.0% | 44% |
| 2023-10-21 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 47 | 100.0% | 85% | 145 | 0.0% | 55% |
| 2023-10-21 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 2 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2023-10-21 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 44,883 | 100.0% | 36% | 699 | 0.0% | 35% |
| 2023-10-21 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 40,976 | 100.0% | 41% | 609 | 0.0% | 38% |
| 2023-10-21 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 31,412 | 100.0% | 50% | 407 | 0.0% | 43% |
| 2023-10-21 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 5,786 | 100.0% | 84% | 141 | 0.0% | 51% |
| 2023-10-21 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 942 | 100.0% | 91% | 156 | 0.0% | 49% |
| 2023-10-21 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,731 | 99.9% | 42% | 782 | 0.0% | 55% |
| 2023-10-21 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,964 | 99.9% | 44% | 661 | 0.0% | 56% |
| 2023-10-21 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,009 | 100.0% | 52% | 448 | 0.0% | 59% |
| 2023-10-21 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,830 | 100.0% | 70% | 198 | 0.0% | 62% |
| 2023-10-21 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 173 | 100.0% | 90% | 126 | 0.0% | 69% |
| 2023-10-21 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,325 | 100.0% | 38% | 624 | 0.0% | 42% |
| 2023-10-21 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,325 | 100.0% | 38% | 624 | 0.0% | 42% |
| 2023-10-21 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 751 | 100.0% | 60% | 178 | 0.0% | 45% |
| 2023-10-21 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 298 | 100.0% | 83% | 120 | 0.0% | 49% |
| 2023-10-21 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 37 | 100.0% | 97% | 126 | 0.0% | 46% |
| 2023-10-21 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.783 below threshold | | | | | | | | |
| 2023-10-22 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 28,069 | 100.0% | 39% | 518 | 0.0% | 37% |
| 2023-10-22 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 28,069 | 100.0% | 39% | 518 | 0.0% | 37% |
| 2023-10-22 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 20,455 | 100.0% | 47% | 323 | 0.0% | 42% |
| 2023-10-22 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 6,189 | 100.0% | 76% | 133 | 0.1% | 52% |
| 2023-10-22 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 695 | 100.0% | 89% | 116 | 0.0% | 54% |
| 2023-10-22 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,995 | 100.0% | 30% | 1,253 | 0.0% | 43% |
| 2023-10-22 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,995 | 100.0% | 30% | 1,253 | 0.0% | 43% |
| 2023-10-22 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,516 | 100.0% | 41% | 810 | 0.0% | 47% |
| 2023-10-22 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 353 | 100.0% | 76% | 176 | 0.0% | 48% |
| 2023-10-22 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 126 | 100.0% | 81% | 220 | 0.0% | 40% |
| 2023-10-22 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,005 | 100.0% | 19% | 2,733 | 0.0% | 31% |
| 2023-10-22 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,280 | 100.0% | 27% | 1,523 | 0.0% | 39% |
| 2023-10-22 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,235 | 100.0% | 45% | 661 | 0.0% | 48% |
| 2023-10-22 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 157 | 100.0% | 77% | 222 | 0.0% | 37% |
| 2023-10-22 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 19 | 100.0% | 63% | 607 | 0.0% | 26% |
| 2023-10-22 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,229 | 100.0% | 24% | 1,630 | 0.0% | 39% |
| 2023-10-22 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,229 | 100.0% | 24% | 1,630 | 0.0% | 39% |
| 2023-10-22 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,256 | 100.0% | 33% | 939 | 0.0% | 45% |
| 2023-10-22 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 225 | 100.0% | 63% | 188 | 0.0% | 42% |
| 2023-10-22 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 95 | 100.0% | 74% | 289 | 0.0% | 31% |
| 2023-10-22 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,786 | 100.0% | 21% | 2,330 | 0.0% | 32% |
| 2023-10-22 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,405 | 100.0% | 32% | 1,189 | 0.0% | 42% |
| 2023-10-22 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,915 | 100.0% | 50% | 543 | 0.0% | 47% |
| 2023-10-22 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 253 | 100.0% | 85% | 206 | 0.0% | 45% |
| 2023-10-22 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 37 | 100.0% | 86% | 254 | 0.0% | 35% |
| 2023-10-22 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 35,713 | 100.0% | 30% | 890 | 0.0% | 37% |
| 2023-10-22 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 31,612 | 100.0% | 37% | 694 | 0.0% | 40% |
| 2023-10-22 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 21,492 | 100.0% | 48% | 423 | 0.0% | 45% |
| 2023-10-22 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,941 | 100.0% | 83% | 129 | 0.0% | 51% |
| 2023-10-22 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 269 | 100.0% | 86% | 208 | 0.0% | 43% |
| 2023-10-22 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,844 | 100.0% | 40% | 769 | 0.0% | 53% |
| 2023-10-22 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,696 | 100.0% | 41% | 672 | 0.0% | 54% |
| 2023-10-22 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,813 | 100.0% | 48% | 511 | 0.0% | 58% |
| 2023-10-22 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,051 | 100.0% | 72% | 210 | 0.0% | 61% |
| 2023-10-22 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 276 | 100.0% | 79% | 137 | 0.0% | 50% |
| 2023-10-22 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,850 | 99.9% | 39% | 612 | 0.0% | 48% |
| 2023-10-22 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,850 | 99.9% | 39% | 612 | 0.0% | 48% |
| 2023-10-22 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 413 | 100.0% | 67% | 150 | 0.0% | 48% |
| 2023-10-22 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 162 | 100.0% | 80% | 230 | 0.0% | 44% |
| 2023-10-22 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 64 | 100.0% | 86% | 221 | 0.0% | 42% |
| 2023-10-22 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.769 below threshold | | | | | | | | |
| 2023-10-23 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 36,107 | 100.0% | 37% | 514 | 0.0% | 32% |
| 2023-10-23 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 36,107 | 100.0% | 37% | 514 | 0.0% | 32% |
| 2023-10-23 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 33,533 | 100.0% | 40% | 358 | 0.0% | 34% |
| 2023-10-23 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 8,947 | 100.0% | 69% | 160 | 0.0% | 48% |
| 2023-10-23 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 1,035 | 100.0% | 86% | 142 | 0.0% | 50% |
| 2023-10-23 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 16,450 | 100.0% | 33% | 884 | 0.5% | 38% |
| 2023-10-23 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 16,450 | 100.0% | 33% | 884 | 0.5% | 38% |
| 2023-10-23 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 12,526 | 100.0% | 37% | 628 | 0.7% | 41% |
| 2023-10-23 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,217 | 100.0% | 68% | 249 | 4.5% | 47% |
| 2023-10-23 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 266 | 100.0% | 74% | 238 | 35.7% | 39% |
| 2023-10-23 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 28,678 | 100.0% | 39% | 950 | 0.6% | 33% |
| 2023-10-23 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 26,694 | 100.0% | 41% | 713 | 0.7% | 34% |
| 2023-10-23 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 21,084 | 100.0% | 49% | 391 | 0.9% | 37% |
| 2023-10-23 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 8,826 | 100.0% | 69% | 222 | 1.7% | 40% |
| 2023-10-23 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 1,693 | 100.0% | 86% | 187 | 7.2% | 45% |
| 2023-10-23 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,126 | 100.0% | 25% | 1,076 | 0.0% | 31% |
| 2023-10-23 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,126 | 100.0% | 25% | 1,076 | 0.0% | 31% |
| 2023-10-23 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,747 | 100.0% | 29% | 696 | 0.0% | 34% |
| 2023-10-23 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 5,111 | 100.0% | 36% | 517 | 0.0% | 33% |
| 2023-10-23 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 1,592 | 100.0% | 63% | 175 | 0.0% | 43% |
| 2023-10-23 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 36,717 | 100.0% | 34% | 749 | 0.0% | 32% |
| 2023-10-23 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 28,963 | 100.0% | 44% | 476 | 0.0% | 38% |
| 2023-10-23 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 14,896 | 100.0% | 61% | 266 | 0.0% | 43% |
| 2023-10-23 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,669 | 100.0% | 83% | 195 | 0.0% | 40% |
| 2023-10-23 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 876 | 100.0% | 86% | 215 | 0.3% | 41% |
| 2023-10-23 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 88,013 | 100.0% | 46% | 503 | 0.2% | 37% |
| 2023-10-23 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 77,170 | 100.0% | 51% | 418 | 0.3% | 40% |
| 2023-10-23 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 56,172 | 100.0% | 59% | 305 | 0.3% | 43% |
| 2023-10-23 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 10,851 | 100.0% | 85% | 170 | 1.6% | 48% |
| 2023-10-23 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 1,552 | 100.0% | 83% | 193 | 12.2% | 45% |
| 2023-10-23 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 21,953 | 100.0% | 46% | 502 | 0.0% | 52% |
| 2023-10-23 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 17,823 | 100.0% | 50% | 432 | 0.0% | 52% |
| 2023-10-23 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,987 | 100.0% | 59% | 334 | 0.0% | 53% |
| 2023-10-23 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,233 | 100.0% | 74% | 190 | 0.0% | 50% |
| 2023-10-23 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 828 | 100.0% | 77% | 178 | 0.0% | 44% |
| 2023-10-23 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,090 | 100.0% | 36% | 643 | 0.0% | 35% |
| 2023-10-23 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,090 | 100.0% | 36% | 643 | 0.0% | 35% |
| 2023-10-23 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,752 | 100.0% | 56% | 245 | 0.0% | 43% |
| 2023-10-23 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,340 | 100.0% | 77% | 170 | 0.0% | 44% |
| 2023-10-23 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 402 | 100.0% | 80% | 223 | 0.0% | 42% |
| 2023-10-23 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.932 below threshold | | | | | | | | |
| 2023-10-24 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 26,157 | 100.0% | 33% | 543 | 0.0% | 30% |
| 2023-10-24 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 26,157 | 100.0% | 33% | 543 | 0.0% | 30% |
| 2023-10-24 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 26,326 | 100.0% | 33% | 428 | 0.0% | 31% |
| 2023-10-24 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 9,128 | 100.0% | 59% | 213 | 0.0% | 47% |
| 2023-10-24 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 666 | 100.0% | 89% | 180 | 0.0% | 53% |
| 2023-10-24 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 24,551 | 100.0% | 33% | 683 | 0.0% | 35% |
| 2023-10-24 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 24,551 | 100.0% | 33% | 683 | 0.0% | 35% |
| 2023-10-24 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 20,654 | 100.0% | 37% | 526 | 0.0% | 37% |
| 2023-10-24 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 6,405 | 100.0% | 56% | 263 | 0.0% | 45% |
| 2023-10-24 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 327 | 100.0% | 80% | 195 | 0.0% | 45% |
| 2023-10-24 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 37,049 | 100.0% | 42% | 552 | 0.0% | 33% |
| 2023-10-24 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 35,941 | 100.0% | 43% | 460 | 0.0% | 33% |
| 2023-10-24 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 31,278 | 100.0% | 44% | 385 | 0.0% | 34% |
| 2023-10-24 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 6,028 | 100.0% | 66% | 190 | 0.0% | 45% |
| 2023-10-24 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 141 | 100.0% | 75% | 125 | 0.0% | 48% |
| 2023-10-24 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,729 | 100.0% | 32% | 868 | 0.0% | 33% |
| 2023-10-24 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,729 | 100.0% | 32% | 868 | 0.0% | 33% |
| 2023-10-24 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,370 | 100.0% | 32% | 731 | 0.0% | 33% |
| 2023-10-24 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 7,375 | 100.0% | 33% | 554 | 0.0% | 33% |
| 2023-10-24 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 805 | 100.0% | 81% | 195 | 0.0% | 46% |
| 2023-10-24 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 37,491 | 100.0% | 31% | 783 | 0.0% | 31% |
| 2023-10-24 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 32,630 | 100.0% | 36% | 533 | 0.0% | 34% |
| 2023-10-24 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 22,471 | 100.0% | 45% | 362 | 0.0% | 38% |
| 2023-10-24 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,911 | 100.0% | 82% | 137 | 0.0% | 47% |
| 2023-10-24 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 97 | 100.0% | 79% | 132 | 0.0% | 41% |
| 2023-10-24 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 79,513 | 100.0% | 52% | 492 | 0.0% | 38% |
| 2023-10-24 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 76,714 | 100.0% | 54% | 439 | 0.0% | 39% |
| 2023-10-24 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 68,825 | 100.0% | 57% | 393 | 0.0% | 40% |
| 2023-10-24 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 27,845 | 100.0% | 68% | 248 | 0.0% | 45% |
| 2023-10-24 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 973 | 100.0% | 88% | 168 | 0.0% | 50% |
| 2023-10-24 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 35,686 | 100.0% | 41% | 434 | 0.0% | 46% |
| 2023-10-24 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 30,283 | 100.0% | 44% | 386 | 0.0% | 47% |
| 2023-10-24 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 19,719 | 100.0% | 51% | 330 | 0.0% | 49% |
| 2023-10-24 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,757 | 100.0% | 69% | 217 | 0.0% | 51% |
| 2023-10-24 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 481 | 100.0% | 84% | 142 | 0.2% | 47% |
| 2023-10-24 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 18,771 | 100.0% | 38% | 508 | 0.0% | 33% |
| 2023-10-24 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 18,771 | 100.0% | 38% | 508 | 0.0% | 33% |
| 2023-10-24 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 13,301 | 100.0% | 45% | 332 | 0.0% | 37% |
| 2023-10-24 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 7,457 | 100.0% | 60% | 222 | 0.0% | 43% |
| 2023-10-24 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 1,228 | 100.0% | 86% | 156 | 0.0% | 45% |
| 2023-10-24 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.855 below threshold | | | | | | | | |
| 2023-10-25 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 28,735 | 100.0% | 39% | 480 | 0.0% | 39% |
| 2023-10-25 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 28,735 | 100.0% | 39% | 480 | 0.0% | 39% |
| 2023-10-25 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 15,594 | 100.0% | 46% | 373 | 0.0% | 45% |
| 2023-10-25 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,644 | 100.0% | 77% | 157 | 0.0% | 55% |
| 2023-10-25 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 238 | 100.0% | 91% | 106 | 0.0% | 58% |
| 2023-10-25 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,150 | 100.0% | 26% | 1,029 | 0.0% | 35% |
| 2023-10-25 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 14,150 | 100.0% | 26% | 1,029 | 0.0% | 35% |
| 2023-10-25 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,622 | 100.0% | 29% | 756 | 0.0% | 39% |
| 2023-10-25 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,652 | 100.0% | 35% | 518 | 0.0% | 42% |
| 2023-10-25 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 85 | 100.0% | 85% | 120 | 0.0% | 62% |
| 2023-10-25 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 402 | 99.5% | 53% | 9,274 | 0.0% | 42% |
| 2023-10-25 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 669 | 99.7% | 35% | 4,468 | 0.0% | 31% |
| 2023-10-25 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,828 | 99.9% | 25% | 1,977 | 0.0% | 26% |
| 2023-10-25 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 12,790 | 100.0% | 25% | 567 | 0.0% | 27% |
| 2023-10-25 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 224 | 100.0% | 82% | 166 | 0.0% | 44% |
| 2023-10-25 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 9,884 | 100.0% | 27% | 900 | 0.1% | 33% |
| 2023-10-25 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,884 | 100.0% | 27% | 900 | 0.1% | 33% |
| 2023-10-25 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 9,010 | 100.0% | 31% | 653 | 0.0% | 33% |
| 2023-10-25 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 6,272 | 100.0% | 37% | 410 | 0.0% | 35% |
| 2023-10-25 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 674 | 100.0% | 82% | 139 | 0.0% | 50% |
| 2023-10-25 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 25,842 | 100.0% | 22% | 1,188 | 0.0% | 31% |
| 2023-10-25 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 19,779 | 100.0% | 33% | 682 | 0.0% | 39% |
| 2023-10-25 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,935 | 100.0% | 51% | 391 | 0.0% | 46% |
| 2023-10-25 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 157 | 100.0% | 88% | 120 | 0.0% | 49% |
| 2023-10-25 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 9 | 100.0% | 89% | 104 | 0.0% | 33% |
| 2023-10-25 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 68,197 | 100.0% | 48% | 556 | 0.0% | 37% |
| 2023-10-25 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 66,042 | 100.0% | 49% | 480 | 0.0% | 37% |
| 2023-10-25 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 60,539 | 100.0% | 51% | 414 | 0.0% | 39% |
| 2023-10-25 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 22,846 | 100.0% | 67% | 210 | 0.0% | 46% |
| 2023-10-25 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 827 | 100.0% | 93% | 120 | 0.0% | 53% |
| 2023-10-25 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 27,180 | 100.0% | 38% | 500 | 0.0% | 48% |
| 2023-10-25 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 22,362 | 100.0% | 41% | 464 | 0.0% | 49% |
| 2023-10-25 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 13,757 | 100.0% | 48% | 398 | 0.0% | 52% |
| 2023-10-25 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,712 | 100.0% | 73% | 192 | 0.0% | 58% |
| 2023-10-25 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 171 | 100.0% | 91% | 118 | 0.0% | 60% |
| 2023-10-25 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,563 | 100.0% | 20% | 1,243 | 0.0% | 29% |
| 2023-10-25 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,563 | 100.0% | 20% | 1,243 | 0.0% | 29% |
| 2023-10-25 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,009 | 100.0% | 22% | 1,045 | 0.0% | 32% |
| 2023-10-25 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,866 | 100.0% | 25% | 720 | 0.0% | 34% |
| 2023-10-25 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 160 | 100.0% | 74% | 135 | 0.0% | 58% |
| 2023-10-25 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.851 below threshold | | | | | | | | |
| 2023-10-26 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 31,684 | 100.0% | 35% | 518 | 0.0% | 33% |
| 2023-10-26 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 31,684 | 100.0% | 35% | 518 | 0.0% | 33% |
| 2023-10-26 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 22,742 | 100.0% | 41% | 423 | 0.0% | 38% |
| 2023-10-26 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,401 | 100.0% | 69% | 187 | 0.0% | 49% |
| 2023-10-26 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 369 | 100.0% | 83% | 150 | 0.0% | 52% |
| 2023-10-26 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 32,960 | 100.0% | 39% | 654 | 0.0% | 38% |
| 2023-10-26 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 32,960 | 100.0% | 39% | 654 | 0.0% | 38% |
| 2023-10-26 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 25,326 | 100.0% | 45% | 613 | 0.0% | 41% |
| 2023-10-26 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 6,773 | 100.0% | 64% | 318 | 0.0% | 47% |
| 2023-10-26 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 434 | 100.0% | 83% | 155 | 0.0% | 47% |
| 2023-10-26 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,134 | 99.9% | 37% | 5,592 | 0.0% | 31% |
| 2023-10-26 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,255 | 100.0% | 20% | 1,890 | 0.0% | 19% |
| 2023-10-26 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,938 | 100.0% | 20% | 885 | 0.0% | 25% |
| 2023-10-26 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 6,902 | 100.0% | 26% | 724 | 0.0% | 29% |
| 2023-10-26 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 34 | 100.0% | 94% | 130 | 0.0% | 35% |
| 2023-10-26 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 27,150 | 100.0% | 40% | 534 | 0.0% | 36% |
| 2023-10-26 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 27,150 | 100.0% | 40% | 534 | 0.0% | 36% |
| 2023-10-26 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 20,432 | 100.0% | 45% | 406 | 0.0% | 39% |
| 2023-10-26 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 8,648 | 100.0% | 56% | 305 | 0.0% | 41% |
| 2023-10-26 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 756 | 100.0% | 85% | 149 | 0.0% | 52% |
| 2023-10-26 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,859 | 100.0% | 32% | 987 | 0.0% | 32% |
| 2023-10-26 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,743 | 100.0% | 31% | 720 | 0.0% | 31% |
| 2023-10-26 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 12,808 | 100.0% | 31% | 638 | 0.0% | 30% |
| 2023-10-26 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 6,542 | 100.0% | 44% | 374 | 0.0% | 38% |
| 2023-10-26 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 100 | 100.0% | 82% | 168 | 0.0% | 38% |
| 2023-10-26 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 24,851 | 100.0% | 43% | 712 | 0.0% | 35% |
| 2023-10-26 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 27,764 | 100.0% | 40% | 574 | 0.0% | 33% |
| 2023-10-26 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 30,427 | 100.0% | 41% | 446 | 0.0% | 35% |
| 2023-10-26 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 22,447 | 100.0% | 47% | 450 | 0.0% | 38% |
| 2023-10-26 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 2,469 | 100.0% | 73% | 174 | 0.0% | 47% |
| 2023-10-26 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 29,726 | 100.0% | 37% | 565 | 0.0% | 46% |
| 2023-10-26 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 25,421 | 100.0% | 39% | 524 | 0.0% | 47% |
| 2023-10-26 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 17,128 | 100.0% | 45% | 437 | 0.0% | 50% |
| 2023-10-26 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,141 | 100.0% | 68% | 224 | 0.0% | 53% |
| 2023-10-26 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 438 | 100.0% | 88% | 139 | 0.0% | 53% |
| 2023-10-26 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,762 | 100.0% | 26% | 819 | 0.0% | 30% |
| 2023-10-26 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,762 | 100.0% | 26% | 819 | 0.0% | 30% |
| 2023-10-26 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,299 | 100.0% | 22% | 980 | 0.0% | 30% |
| 2023-10-26 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,576 | 100.0% | 32% | 626 | 0.0% | 39% |
| 2023-10-26 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 170 | 100.0% | 81% | 140 | 0.0% | 45% |
| 2023-10-26 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.868 below threshold | | | | | | | | |
| 2023-10-27 | aave_perp_binance_bybit | ok | 0.999 | gross>0bps | 20,856 | 99.8% | 36% | 633 | 0.0% | 39% |
| 2023-10-27 | aave_perp_binance_bybit | ok | 0.999 | gross>1bps | 20,856 | 99.8% | 36% | 633 | 0.0% | 39% |
| 2023-10-27 | aave_perp_binance_bybit | ok | 0.999 | gross>2bps | 10,302 | 99.8% | 44% | 514 | 0.0% | 49% |
| 2023-10-27 | aave_perp_binance_bybit | ok | 0.999 | gross>5bps | 1,708 | 100.0% | 72% | 185 | 0.0% | 60% |
| 2023-10-27 | aave_perp_binance_bybit | ok | 0.999 | retail_taker | 157 | 100.0% | 82% | 234 | 0.0% | 55% |
| 2023-10-27 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 17,708 | 100.0% | 33% | 1,002 | 0.0% | 39% |
| 2023-10-27 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 17,708 | 100.0% | 33% | 1,002 | 0.0% | 39% |
| 2023-10-27 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,811 | 100.0% | 40% | 721 | 0.0% | 43% |
| 2023-10-27 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,228 | 100.0% | 74% | 203 | 0.0% | 52% |
| 2023-10-27 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 113 | 100.0% | 77% | 224 | 0.0% | 52% |
| 2023-10-27 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,606 | 100.0% | 30% | 1,374 | 0.1% | 29% |
| 2023-10-27 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,341 | 100.0% | 28% | 1,258 | 0.0% | 25% |
| 2023-10-27 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,904 | 100.0% | 26% | 898 | 0.0% | 30% |
| 2023-10-27 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,044 | 99.9% | 41% | 980 | 0.0% | 39% |
| 2023-10-27 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 72 | 100.0% | 83% | 185 | 0.0% | 43% |
| 2023-10-27 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,481 | 100.0% | 32% | 960 | 0.0% | 36% |
| 2023-10-27 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,481 | 100.0% | 32% | 960 | 0.0% | 36% |
| 2023-10-27 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,627 | 100.0% | 38% | 642 | 0.0% | 39% |
| 2023-10-27 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,835 | 100.0% | 70% | 204 | 0.1% | 53% |
| 2023-10-27 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 155 | 100.0% | 83% | 176 | 0.0% | 46% |
| 2023-10-27 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 9,562 | 100.0% | 27% | 2,055 | 0.0% | 30% |
| 2023-10-27 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,037 | 100.0% | 25% | 1,818 | 0.0% | 29% |
| 2023-10-27 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,669 | 100.0% | 32% | 956 | 0.0% | 36% |
| 2023-10-27 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,113 | 100.0% | 68% | 197 | 0.0% | 52% |
| 2023-10-27 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 110 | 100.0% | 85% | 150 | 0.0% | 44% |
| 2023-10-27 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 47,664 | 100.0% | 40% | 720 | 0.0% | 37% |
| 2023-10-27 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 42,569 | 100.0% | 44% | 538 | 0.0% | 39% |
| 2023-10-27 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 33,443 | 100.0% | 50% | 414 | 0.0% | 41% |
| 2023-10-27 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 9,551 | 100.0% | 62% | 263 | 0.0% | 44% |
| 2023-10-27 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 407 | 100.0% | 89% | 150 | 0.0% | 50% |
| 2023-10-27 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 25,981 | 100.0% | 40% | 595 | 0.0% | 47% |
| 2023-10-27 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 22,360 | 100.0% | 42% | 570 | 0.0% | 48% |
| 2023-10-27 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 16,182 | 100.0% | 45% | 509 | 0.0% | 49% |
| 2023-10-27 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 6,191 | 100.0% | 50% | 310 | 0.0% | 49% |
| 2023-10-27 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 905 | 100.0% | 74% | 244 | 0.0% | 48% |
| 2023-10-27 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,856 | 100.0% | 32% | 1,048 | 0.0% | 39% |
| 2023-10-27 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,856 | 100.0% | 32% | 1,048 | 0.0% | 39% |
| 2023-10-27 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,101 | 100.0% | 50% | 430 | 0.0% | 50% |
| 2023-10-27 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 668 | 100.0% | 75% | 188 | 0.0% | 53% |
| 2023-10-27 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 199 | 100.0% | 85% | 220 | 0.0% | 46% |
| 2023-10-27 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.834 below threshold | | | | | | | | |
| 2023-10-28 | aave_perp_binance_bybit | ok | 0.997 | gross>0bps | 8,985 | 99.0% | 31% | 1,308 | 0.0% | 42% |
| 2023-10-28 | aave_perp_binance_bybit | ok | 0.997 | gross>1bps | 8,985 | 99.0% | 31% | 1,308 | 0.0% | 42% |
| 2023-10-28 | aave_perp_binance_bybit | ok | 0.997 | gross>2bps | 5,031 | 99.5% | 41% | 1,001 | 0.0% | 49% |
| 2023-10-28 | aave_perp_binance_bybit | ok | 0.997 | gross>5bps | 507 | 100.0% | 77% | 170 | 0.0% | 63% |
| 2023-10-28 | aave_perp_binance_bybit | ok | 0.997 | retail_taker | 45 | 100.0% | 89% | 364 | 0.0% | 71% |
| 2023-10-28 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,754 | 99.9% | 24% | 2,833 | 0.0% | 39% |
| 2023-10-28 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,754 | 99.9% | 24% | 2,833 | 0.0% | 39% |
| 2023-10-28 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,571 | 100.0% | 29% | 1,950 | 0.0% | 43% |
| 2023-10-28 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 705 | 100.0% | 67% | 193 | 0.0% | 50% |
| 2023-10-28 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 54 | 100.0% | 80% | 206 | 0.0% | 44% |
| 2023-10-28 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 514 | 99.8% | 40% | 6,890 | 0.0% | 28% |
| 2023-10-28 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 829 | 99.9% | 25% | 2,935 | 0.0% | 21% |
| 2023-10-28 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,326 | 99.9% | 20% | 2,060 | 0.0% | 22% |
| 2023-10-28 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,679 | 100.0% | 29% | 1,352 | 0.0% | 28% |
| 2023-10-28 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 67 | 100.0% | 70% | 272 | 0.0% | 43% |
| 2023-10-28 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,583 | 100.0% | 28% | 2,694 | 0.0% | 37% |
| 2023-10-28 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,583 | 100.0% | 28% | 2,694 | 0.0% | 37% |
| 2023-10-28 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,613 | 100.0% | 32% | 1,682 | 0.0% | 37% |
| 2023-10-28 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 656 | 100.0% | 55% | 222 | 0.0% | 51% |
| 2023-10-28 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 50 | 100.0% | 78% | 171 | 0.0% | 46% |
| 2023-10-28 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,113 | 100.0% | 26% | 4,027 | 0.0% | 31% |
| 2023-10-28 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,160 | 100.0% | 24% | 1,979 | 0.0% | 29% |
| 2023-10-28 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,129 | 100.0% | 31% | 829 | 0.0% | 40% |
| 2023-10-28 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 178 | 100.0% | 71% | 185 | 0.0% | 50% |
| 2023-10-28 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 14 | 100.0% | 71% | 295 | 0.0% | 36% |
| 2023-10-28 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,044 | 100.0% | 32% | 1,844 | 0.0% | 34% |
| 2023-10-28 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,185 | 100.0% | 28% | 1,378 | 0.0% | 32% |
| 2023-10-28 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,489 | 100.0% | 29% | 1,035 | 0.0% | 32% |
| 2023-10-28 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 7,832 | 100.0% | 44% | 420 | 0.0% | 42% |
| 2023-10-28 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 103 | 100.0% | 84% | 113 | 0.0% | 47% |
| 2023-10-28 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 15,967 | 100.0% | 40% | 964 | 0.0% | 50% |
| 2023-10-28 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 14,154 | 100.0% | 42% | 868 | 0.0% | 52% |
| 2023-10-28 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,361 | 100.0% | 48% | 740 | 0.0% | 54% |
| 2023-10-28 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,061 | 100.0% | 56% | 454 | 0.0% | 52% |
| 2023-10-28 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 1,183 | 100.0% | 53% | 250 | 0.0% | 48% |
| 2023-10-28 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 931 | 100.0% | 36% | 1,002 | 0.0% | 51% |
| 2023-10-28 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 931 | 100.0% | 36% | 1,002 | 0.0% | 51% |
| 2023-10-28 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 159 | 100.0% | 67% | 143 | 0.0% | 58% |
| 2023-10-28 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 43 | 100.0% | 77% | 180 | 0.0% | 58% |
| 2023-10-28 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 5 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2023-10-28 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.881 below threshold | | | | | | | | |
| 2023-10-29 | aave_perp_binance_bybit | ok | 0.999 | gross>0bps | 10,609 | 99.3% | 31% | 1,120 | 0.0% | 39% |
| 2023-10-29 | aave_perp_binance_bybit | ok | 0.999 | gross>1bps | 10,609 | 99.3% | 31% | 1,120 | 0.0% | 39% |
| 2023-10-29 | aave_perp_binance_bybit | ok | 0.999 | gross>2bps | 8,328 | 99.6% | 36% | 810 | 0.0% | 42% |
| 2023-10-29 | aave_perp_binance_bybit | ok | 0.999 | gross>5bps | 1,823 | 99.9% | 60% | 226 | 0.1% | 57% |
| 2023-10-29 | aave_perp_binance_bybit | ok | 0.999 | retail_taker | 132 | 100.0% | 92% | 111 | 0.0% | 67% |
| 2023-10-29 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,788 | 99.9% | 27% | 1,788 | 0.0% | 40% |
| 2023-10-29 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,788 | 99.9% | 27% | 1,788 | 0.0% | 40% |
| 2023-10-29 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,401 | 100.0% | 31% | 1,364 | 0.0% | 41% |
| 2023-10-29 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,659 | 100.0% | 45% | 516 | 0.1% | 49% |
| 2023-10-29 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 67 | 100.0% | 84% | 118 | 0.0% | 60% |
| 2023-10-29 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,465 | 99.9% | 30% | 2,649 | 0.0% | 28% |
| 2023-10-29 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,723 | 99.9% | 25% | 1,557 | 0.1% | 26% |
| 2023-10-29 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,551 | 100.0% | 24% | 1,217 | 0.0% | 31% |
| 2023-10-29 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 160 | 100.0% | 69% | 190 | 0.0% | 47% |
| 2023-10-29 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 23 | 100.0% | 96% | 573 | 0.0% | 26% |
| 2023-10-29 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,045 | 100.0% | 29% | 1,527 | 0.0% | 41% |
| 2023-10-29 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,045 | 100.0% | 29% | 1,527 | 0.0% | 41% |
| 2023-10-29 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,952 | 100.0% | 36% | 1,174 | 0.0% | 44% |
| 2023-10-29 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 424 | 100.0% | 75% | 144 | 0.0% | 57% |
| 2023-10-29 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 43 | 100.0% | 91% | 128 | 0.0% | 40% |
| 2023-10-29 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,177 | 100.0% | 22% | 2,814 | 0.0% | 32% |
| 2023-10-29 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,050 | 100.0% | 30% | 1,832 | 0.0% | 38% |
| 2023-10-29 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,827 | 100.0% | 41% | 826 | 0.0% | 47% |
| 2023-10-29 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 55 | 100.0% | 85% | 162 | 0.0% | 60% |
| 2023-10-29 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,319 | 100.0% | 37% | 1,950 | 0.0% | 33% |
| 2023-10-29 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,326 | 100.0% | 27% | 1,388 | 0.0% | 30% |
| 2023-10-29 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,473 | 100.0% | 25% | 1,073 | 0.0% | 30% |
| 2023-10-29 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 10,673 | 100.0% | 42% | 464 | 0.0% | 41% |
| 2023-10-29 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 248 | 100.0% | 89% | 130 | 0.4% | 52% |
| 2023-10-29 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 12,555 | 100.0% | 39% | 928 | 0.0% | 55% |
| 2023-10-29 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,651 | 100.0% | 43% | 821 | 0.0% | 56% |
| 2023-10-29 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,992 | 100.0% | 50% | 573 | 0.0% | 59% |
| 2023-10-29 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 855 | 100.0% | 81% | 141 | 0.0% | 67% |
| 2023-10-29 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 83 | 100.0% | 90% | 123 | 0.0% | 64% |
| 2023-10-29 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,328 | 100.0% | 26% | 1,939 | 0.0% | 44% |
| 2023-10-29 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,328 | 100.0% | 26% | 1,939 | 0.0% | 44% |
| 2023-10-29 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 574 | 100.0% | 48% | 190 | 0.0% | 54% |
| 2023-10-29 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 84 | 100.0% | 65% | 113 | 0.0% | 60% |
| 2023-10-29 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 7 | 100.0% | 71% | 122 | 0.0% | 29% |
| 2023-10-29 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.903 below threshold | | | | | | | | |
| 2023-10-30 | aave_perp_binance_bybit | ok | 0.999 | gross>0bps | 14,564 | 99.7% | 35% | 831 | 0.0% | 42% |
| 2023-10-30 | aave_perp_binance_bybit | ok | 0.999 | gross>1bps | 14,564 | 99.7% | 35% | 831 | 0.0% | 42% |
| 2023-10-30 | aave_perp_binance_bybit | ok | 0.999 | gross>2bps | 9,486 | 99.7% | 40% | 705 | 0.0% | 45% |
| 2023-10-30 | aave_perp_binance_bybit | ok | 0.999 | gross>5bps | 1,908 | 99.9% | 67% | 208 | 0.0% | 55% |
| 2023-10-30 | aave_perp_binance_bybit | ok | 0.999 | retail_taker | 246 | 100.0% | 79% | 170 | 0.0% | 57% |
| 2023-10-30 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,651 | 100.0% | 29% | 1,415 | 0.0% | 40% |
| 2023-10-30 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,651 | 100.0% | 29% | 1,415 | 0.0% | 40% |
| 2023-10-30 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,599 | 100.0% | 35% | 1,096 | 0.0% | 43% |
| 2023-10-30 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,627 | 100.0% | 56% | 402 | 0.0% | 49% |
| 2023-10-30 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 100 | 100.0% | 68% | 158 | 0.0% | 43% |
| 2023-10-30 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 525 | 99.8% | 47% | 4,110 | 0.0% | 32% |
| 2023-10-30 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,067 | 99.9% | 28% | 2,465 | 0.0% | 20% |
| 2023-10-30 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,479 | 100.0% | 21% | 1,738 | 0.0% | 19% |
| 2023-10-30 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,283 | 100.0% | 30% | 786 | 0.0% | 32% |
| 2023-10-30 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 25 | 100.0% | 76% | 138 | 0.0% | 52% |
| 2023-10-30 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,815 | 100.0% | 34% | 1,084 | 0.0% | 44% |
| 2023-10-30 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,815 | 100.0% | 34% | 1,084 | 0.0% | 44% |
| 2023-10-30 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,010 | 100.0% | 50% | 435 | 0.0% | 49% |
| 2023-10-30 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 371 | 100.0% | 75% | 262 | 0.0% | 47% |
| 2023-10-30 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 71 | 100.0% | 73% | 295 | 0.0% | 31% |
| 2023-10-30 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,378 | 100.0% | 25% | 1,684 | 0.0% | 32% |
| 2023-10-30 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,049 | 100.0% | 34% | 972 | 0.0% | 39% |
| 2023-10-30 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,101 | 100.0% | 50% | 447 | 0.0% | 45% |
| 2023-10-30 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 215 | 100.0% | 79% | 178 | 0.0% | 43% |
| 2023-10-30 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 52 | 100.0% | 75% | 175 | 0.0% | 44% |
| 2023-10-30 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,624 | 100.0% | 44% | 713 | 0.0% | 37% |
| 2023-10-30 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,095 | 100.0% | 40% | 612 | 0.0% | 34% |
| 2023-10-30 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 14,915 | 100.0% | 38% | 560 | 0.0% | 33% |
| 2023-10-30 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 19,957 | 100.0% | 42% | 428 | 0.0% | 38% |
| 2023-10-30 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 1,734 | 100.0% | 81% | 189 | 0.0% | 49% |
| 2023-10-30 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 17,924 | 100.0% | 39% | 749 | 0.0% | 52% |
| 2023-10-30 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 15,251 | 100.0% | 42% | 660 | 0.0% | 54% |
| 2023-10-30 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,206 | 100.0% | 50% | 507 | 0.0% | 56% |
| 2023-10-30 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,562 | 100.0% | 79% | 192 | 0.0% | 59% |
| 2023-10-30 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 195 | 100.0% | 80% | 139 | 0.0% | 56% |
| 2023-10-30 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,340 | 100.0% | 30% | 698 | 0.0% | 38% |
| 2023-10-30 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,340 | 100.0% | 30% | 698 | 0.0% | 38% |
| 2023-10-30 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,801 | 100.0% | 43% | 522 | 0.0% | 39% |
| 2023-10-30 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,293 | 100.0% | 49% | 258 | 0.0% | 38% |
| 2023-10-30 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 93 | 100.0% | 81% | 172 | 0.0% | 43% |
| 2023-10-30 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.810 below threshold | | | | | | | | |
| 2023-10-31 | aave_perp_binance_bybit | ok | 0.999 | gross>0bps | 17,637 | 99.5% | 33% | 776 | 0.0% | 39% |
| 2023-10-31 | aave_perp_binance_bybit | ok | 0.999 | gross>1bps | 17,637 | 99.5% | 33% | 776 | 0.0% | 39% |
| 2023-10-31 | aave_perp_binance_bybit | ok | 0.999 | gross>2bps | 12,330 | 99.6% | 39% | 550 | 0.0% | 44% |
| 2023-10-31 | aave_perp_binance_bybit | ok | 0.999 | gross>5bps | 1,474 | 99.9% | 75% | 186 | 0.0% | 58% |
| 2023-10-31 | aave_perp_binance_bybit | ok | 0.999 | retail_taker | 209 | 100.0% | 69% | 190 | 0.0% | 47% |
| 2023-10-31 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 15,604 | 100.0% | 30% | 1,169 | 0.0% | 41% |
| 2023-10-31 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 15,604 | 100.0% | 30% | 1,169 | 0.0% | 41% |
| 2023-10-31 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,128 | 100.0% | 38% | 857 | 0.0% | 44% |
| 2023-10-31 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,678 | 100.0% | 70% | 202 | 0.1% | 52% |
| 2023-10-31 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 296 | 100.0% | 74% | 204 | 0.0% | 37% |
| 2023-10-31 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,923 | 99.9% | 27% | 2,472 | 0.1% | 30% |
| 2023-10-31 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,935 | 99.9% | 24% | 1,727 | 0.0% | 29% |
| 2023-10-31 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,138 | 100.0% | 21% | 1,510 | 0.0% | 28% |
| 2023-10-31 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,435 | 100.0% | 38% | 883 | 0.0% | 38% |
| 2023-10-31 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 9 | 100.0% | 100% | none resolved | 0.0% | 56% |
| 2023-10-31 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,187 | 100.0% | 35% | 878 | 0.0% | 40% |
| 2023-10-31 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,187 | 100.0% | 35% | 878 | 0.0% | 40% |
| 2023-10-31 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,997 | 100.0% | 50% | 428 | 0.0% | 45% |
| 2023-10-31 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 799 | 100.0% | 80% | 196 | 0.0% | 46% |
| 2023-10-31 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 224 | 100.0% | 83% | 176 | 0.0% | 46% |
| 2023-10-31 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,422 | 100.0% | 22% | 1,898 | 0.0% | 33% |
| 2023-10-31 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,659 | 100.0% | 31% | 1,048 | 0.0% | 40% |
| 2023-10-31 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,916 | 100.0% | 37% | 818 | 0.1% | 38% |
| 2023-10-31 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 442 | 100.0% | 69% | 159 | 0.0% | 50% |
| 2023-10-31 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 5 | 100.0% | 80% | 123 | 0.0% | 40% |
| 2023-10-31 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 31,712 | 100.0% | 42% | 749 | 0.0% | 37% |
| 2023-10-31 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 31,837 | 100.0% | 42% | 629 | 0.0% | 37% |
| 2023-10-31 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 30,989 | 100.0% | 43% | 464 | 0.0% | 37% |
| 2023-10-31 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 17,912 | 100.0% | 52% | 318 | 0.0% | 42% |
| 2023-10-31 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 896 | 100.0% | 86% | 133 | 0.0% | 49% |
| 2023-10-31 | tia_perp_binance_bybit | excluded: binance_bt/binance/TIA-USDT/perp coverage 0.250 below threshold | | | | | | | | |
| 2023-10-31 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 25,099 | 100.0% | 40% | 498 | 0.0% | 50% |
| 2023-10-31 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 19,391 | 100.0% | 44% | 434 | 0.0% | 52% |
| 2023-10-31 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,776 | 100.0% | 54% | 340 | 0.0% | 55% |
| 2023-10-31 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,910 | 100.0% | 79% | 139 | 0.0% | 61% |
| 2023-10-31 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 286 | 100.0% | 85% | 128 | 0.0% | 59% |
| 2023-10-31 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,332 | 100.0% | 41% | 455 | 0.0% | 37% |
| 2023-10-31 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,332 | 100.0% | 41% | 455 | 0.0% | 37% |
| 2023-10-31 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,189 | 100.0% | 52% | 246 | 0.0% | 39% |
| 2023-10-31 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,070 | 100.0% | 73% | 162 | 0.0% | 45% |
| 2023-10-31 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 502 | 100.0% | 90% | 142 | 0.0% | 51% |
| 2023-10-31 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.813 below threshold | | | | | | | | |
| 2023-11-01 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 39,860 | 99.9% | 44% | 452 | 0.0% | 34% |
| 2023-11-01 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 39,860 | 99.9% | 44% | 452 | 0.0% | 34% |
| 2023-11-01 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 30,015 | 100.0% | 50% | 373 | 0.0% | 38% |
| 2023-11-01 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 5,286 | 100.0% | 78% | 159 | 0.0% | 51% |
| 2023-11-01 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 540 | 100.0% | 92% | 113 | 0.0% | 58% |
| 2023-11-01 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 23,945 | 100.0% | 36% | 811 | 0.0% | 36% |
| 2023-11-01 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 23,016 | 100.0% | 37% | 802 | 0.0% | 36% |
| 2023-11-01 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 19,294 | 100.0% | 40% | 706 | 0.0% | 39% |
| 2023-11-01 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 6,053 | 100.0% | 59% | 306 | 0.0% | 46% |
| 2023-11-01 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 413 | 100.0% | 87% | 130 | 0.0% | 53% |
| 2023-11-01 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,832 | 100.0% | 43% | 604 | 0.0% | 30% |
| 2023-11-01 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,162 | 100.0% | 38% | 544 | 0.0% | 26% |
| 2023-11-01 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 9,876 | 100.0% | 37% | 531 | 0.0% | 28% |
| 2023-11-01 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,980 | 100.0% | 50% | 285 | 0.0% | 34% |
| 2023-11-01 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 81 | 100.0% | 86% | 246 | 0.0% | 56% |
| 2023-11-01 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,646 | 100.0% | 28% | 976 | 0.0% | 32% |
| 2023-11-01 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,646 | 100.0% | 28% | 976 | 0.0% | 32% |
| 2023-11-01 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,518 | 100.0% | 31% | 658 | 0.0% | 34% |
| 2023-11-01 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,575 | 100.0% | 55% | 182 | 0.0% | 47% |
| 2023-11-01 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 52 | 100.0% | 92% | 117 | 0.0% | 54% |
| 2023-11-01 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 20,651 | 100.0% | 32% | 867 | 0.0% | 29% |
| 2023-11-01 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 16,903 | 100.0% | 38% | 624 | 0.0% | 33% |
| 2023-11-01 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,342 | 100.0% | 44% | 480 | 0.0% | 35% |
| 2023-11-01 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 774 | 100.0% | 77% | 144 | 0.0% | 47% |
| 2023-11-01 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 45 | 100.0% | 78% | 158 | 0.0% | 29% |
| 2023-11-01 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 137,020 | 100.0% | 56% | 369 | 0.0% | 36% |
| 2023-11-01 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 125,886 | 100.0% | 59% | 327 | 0.0% | 37% |
| 2023-11-01 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 104,563 | 100.0% | 63% | 282 | 0.0% | 39% |
| 2023-11-01 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 35,809 | 100.0% | 76% | 196 | 0.0% | 44% |
| 2023-11-01 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 3,072 | 100.0% | 92% | 124 | 0.0% | 53% |
| 2023-11-01 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 24,273 | 100.0% | 42% | 632 | 0.0% | 33% |
| 2023-11-01 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 25,032 | 100.0% | 42% | 627 | 0.0% | 33% |
| 2023-11-01 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 25,933 | 100.0% | 42% | 568 | 0.0% | 33% |
| 2023-11-01 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 29,394 | 100.0% | 42% | 463 | 0.0% | 33% |
| 2023-11-01 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 25,679 | 100.0% | 44% | 372 | 0.0% | 35% |
| 2023-11-01 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 22,926 | 100.0% | 40% | 521 | 0.0% | 49% |
| 2023-11-01 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 18,738 | 100.0% | 44% | 468 | 0.0% | 51% |
| 2023-11-01 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,823 | 100.0% | 51% | 370 | 0.0% | 53% |
| 2023-11-01 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,873 | 100.0% | 78% | 153 | 0.0% | 59% |
| 2023-11-01 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 212 | 100.0% | 91% | 114 | 0.0% | 64% |
| 2023-11-01 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,605 | 100.0% | 25% | 688 | 0.0% | 29% |
| 2023-11-01 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,605 | 100.0% | 25% | 688 | 0.0% | 29% |
| 2023-11-01 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,782 | 100.0% | 31% | 498 | 0.0% | 31% |
| 2023-11-01 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,334 | 100.0% | 36% | 444 | 0.0% | 34% |
| 2023-11-01 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 161 | 100.0% | 90% | 148 | 0.0% | 50% |
| 2023-11-01 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.850 below threshold | | | | | | | | |
| 2023-11-02 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 49,505 | 100.0% | 50% | 394 | 0.0% | 37% |
| 2023-11-02 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 50,104 | 100.0% | 49% | 393 | 0.0% | 37% |
| 2023-11-02 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 37,546 | 100.0% | 54% | 313 | 0.0% | 39% |
| 2023-11-02 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 19,205 | 100.0% | 60% | 218 | 0.0% | 38% |
| 2023-11-02 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 4,825 | 100.0% | 84% | 134 | 0.1% | 46% |
| 2023-11-02 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 26,362 | 100.0% | 34% | 909 | 0.0% | 34% |
| 2023-11-02 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 24,492 | 100.0% | 36% | 838 | 0.0% | 35% |
| 2023-11-02 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 19,728 | 100.0% | 40% | 646 | 0.0% | 38% |
| 2023-11-02 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,962 | 100.0% | 68% | 205 | 0.1% | 49% |
| 2023-11-02 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 198 | 100.0% | 84% | 206 | 0.5% | 44% |
| 2023-11-02 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 874 | 99.9% | 49% | 2,942 | 0.2% | 30% |
| 2023-11-02 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,702 | 99.9% | 29% | 1,224 | 0.2% | 21% |
| 2023-11-02 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,003 | 100.0% | 27% | 874 | 0.1% | 22% |
| 2023-11-02 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 6,815 | 100.0% | 34% | 729 | 0.0% | 27% |
| 2023-11-02 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 135 | 100.0% | 82% | 202 | 0.0% | 42% |
| 2023-11-02 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 15,282 | 100.0% | 30% | 790 | 0.0% | 32% |
| 2023-11-02 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 15,282 | 100.0% | 30% | 790 | 0.0% | 32% |
| 2023-11-02 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,103 | 100.0% | 43% | 482 | 0.1% | 38% |
| 2023-11-02 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 813 | 100.0% | 76% | 162 | 0.1% | 47% |
| 2023-11-02 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 109 | 100.0% | 86% | 148 | 0.0% | 38% |
| 2023-11-02 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 19,913 | 100.0% | 30% | 1,158 | 0.0% | 29% |
| 2023-11-02 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 17,175 | 100.0% | 35% | 851 | 0.0% | 33% |
| 2023-11-02 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,811 | 100.0% | 45% | 488 | 0.1% | 37% |
| 2023-11-02 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 236 | 100.0% | 84% | 145 | 0.0% | 39% |
| 2023-11-02 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 33 | 100.0% | 79% | 164 | 0.0% | 36% |
| 2023-11-02 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 105,211 | 100.0% | 52% | 444 | 0.0% | 34% |
| 2023-11-02 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 100,248 | 100.0% | 54% | 387 | 0.0% | 35% |
| 2023-11-02 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 87,527 | 100.0% | 57% | 332 | 0.0% | 37% |
| 2023-11-02 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 29,094 | 100.0% | 71% | 216 | 0.1% | 45% |
| 2023-11-02 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 1,579 | 100.0% | 91% | 124 | 2.0% | 52% |
| 2023-11-02 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 59,524 | 100.0% | 48% | 454 | 0.0% | 35% |
| 2023-11-02 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 54,011 | 100.0% | 49% | 428 | 0.0% | 36% |
| 2023-11-02 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 47,773 | 100.0% | 52% | 400 | 0.0% | 38% |
| 2023-11-02 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 27,992 | 100.0% | 60% | 308 | 0.0% | 41% |
| 2023-11-02 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 8,361 | 100.0% | 74% | 194 | 0.0% | 46% |
| 2023-11-02 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 20,032 | 100.0% | 42% | 534 | 0.0% | 49% |
| 2023-11-02 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 15,467 | 100.0% | 46% | 471 | 0.1% | 51% |
| 2023-11-02 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,233 | 100.0% | 55% | 366 | 0.1% | 54% |
| 2023-11-02 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 992 | 100.0% | 81% | 148 | 0.9% | 52% |
| 2023-11-02 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 132 | 100.0% | 86% | 126 | 0.0% | 45% |
| 2023-11-02 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,568 | 100.0% | 33% | 756 | 0.0% | 32% |
| 2023-11-02 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,568 | 100.0% | 33% | 756 | 0.0% | 32% |
| 2023-11-02 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,276 | 100.0% | 44% | 420 | 0.0% | 36% |
| 2023-11-02 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,161 | 100.0% | 76% | 170 | 0.1% | 47% |
| 2023-11-02 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 130 | 100.0% | 93% | 332 | 1.5% | 48% |
| 2023-11-02 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.880 below threshold | | | | | | | | |
| 2023-11-03 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 25,994 | 99.8% | 36% | 560 | 0.0% | 35% |
| 2023-11-03 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 25,994 | 99.8% | 36% | 560 | 0.0% | 35% |
| 2023-11-03 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 25,432 | 99.9% | 38% | 442 | 0.0% | 36% |
| 2023-11-03 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 9,890 | 99.9% | 55% | 235 | 0.0% | 43% |
| 2023-11-03 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 292 | 100.0% | 86% | 113 | 0.0% | 59% |
| 2023-11-03 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 37,958 | 100.0% | 46% | 559 | 0.0% | 40% |
| 2023-11-03 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 34,707 | 100.0% | 47% | 569 | 0.0% | 40% |
| 2023-11-03 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 26,401 | 100.0% | 51% | 470 | 0.0% | 41% |
| 2023-11-03 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 6,766 | 100.0% | 67% | 242 | 0.0% | 47% |
| 2023-11-03 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 429 | 100.0% | 90% | 126 | 0.0% | 61% |
| 2023-11-03 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,379 | 100.0% | 29% | 1,628 | 0.0% | 29% |
| 2023-11-03 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,452 | 100.0% | 29% | 820 | 0.0% | 29% |
| 2023-11-03 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,020 | 100.0% | 33% | 548 | 0.0% | 31% |
| 2023-11-03 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,003 | 100.0% | 33% | 794 | 0.0% | 31% |
| 2023-11-03 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 19 | 100.0% | 68% | 138 | 0.0% | 42% |
| 2023-11-03 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,416 | 100.0% | 31% | 1,010 | 0.0% | 36% |
| 2023-11-03 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,416 | 100.0% | 31% | 1,010 | 0.0% | 36% |
| 2023-11-03 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,157 | 100.0% | 46% | 432 | 0.0% | 46% |
| 2023-11-03 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 117 | 100.0% | 84% | 227 | 0.0% | 52% |
| 2023-11-03 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 5 | 100.0% | 100% | none resolved | 0.0% | 40% |
| 2023-11-03 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 19,669 | 100.0% | 25% | 1,356 | 0.0% | 30% |
| 2023-11-03 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 13,928 | 100.0% | 35% | 858 | 0.0% | 35% |
| 2023-11-03 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,144 | 100.0% | 44% | 638 | 0.1% | 38% |
| 2023-11-03 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 132 | 100.0% | 73% | 117 | 0.0% | 42% |
| 2023-11-03 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 13 | 100.0% | 85% | 103 | 0.0% | 62% |
| 2023-11-03 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 118,504 | 100.0% | 51% | 381 | 0.0% | 37% |
| 2023-11-03 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 101,794 | 100.0% | 55% | 336 | 0.0% | 39% |
| 2023-11-03 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 69,788 | 100.0% | 60% | 282 | 0.0% | 41% |
| 2023-11-03 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 9,276 | 100.0% | 80% | 158 | 0.0% | 50% |
| 2023-11-03 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 396 | 100.0% | 93% | 121 | 0.0% | 59% |
| 2023-11-03 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 52,300 | 100.0% | 48% | 537 | 0.0% | 34% |
| 2023-11-03 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 47,324 | 100.0% | 49% | 500 | 0.0% | 35% |
| 2023-11-03 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 41,669 | 100.0% | 51% | 490 | 0.0% | 36% |
| 2023-11-03 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 23,276 | 100.0% | 55% | 370 | 0.0% | 39% |
| 2023-11-03 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 5,838 | 100.0% | 68% | 210 | 0.0% | 47% |
| 2023-11-03 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,919 | 100.0% | 30% | 761 | 0.0% | 46% |
| 2023-11-03 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,757 | 100.0% | 32% | 646 | 0.0% | 47% |
| 2023-11-03 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,190 | 100.0% | 39% | 559 | 0.0% | 49% |
| 2023-11-03 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,299 | 100.0% | 65% | 282 | 0.0% | 55% |
| 2023-11-03 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 43 | 100.0% | 98% | 103 | 0.0% | 63% |
| 2023-11-03 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,514 | 100.0% | 28% | 1,186 | 0.0% | 32% |
| 2023-11-03 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,514 | 100.0% | 28% | 1,186 | 0.0% | 32% |
| 2023-11-03 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,789 | 100.0% | 43% | 466 | 0.0% | 39% |
| 2023-11-03 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 443 | 100.0% | 76% | 138 | 0.0% | 51% |
| 2023-11-03 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 47 | 100.0% | 96% | 252 | 0.0% | 60% |
| 2023-11-03 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.823 below threshold | | | | | | | | |
| 2023-11-04 | aave_perp_binance_bybit | ok | 0.999 | gross>0bps | 11,241 | 99.1% | 34% | 882 | 0.1% | 38% |
| 2023-11-04 | aave_perp_binance_bybit | ok | 0.999 | gross>1bps | 11,241 | 99.1% | 34% | 882 | 0.1% | 38% |
| 2023-11-04 | aave_perp_binance_bybit | ok | 0.999 | gross>2bps | 12,423 | 99.4% | 34% | 704 | 0.1% | 38% |
| 2023-11-04 | aave_perp_binance_bybit | ok | 0.999 | gross>5bps | 8,529 | 99.7% | 43% | 496 | 0.1% | 43% |
| 2023-11-04 | aave_perp_binance_bybit | ok | 0.999 | retail_taker | 1,499 | 100.0% | 64% | 264 | 0.4% | 48% |
| 2023-11-04 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 23,926 | 100.0% | 41% | 766 | 0.0% | 38% |
| 2023-11-04 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 21,566 | 100.0% | 43% | 632 | 0.0% | 39% |
| 2023-11-04 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 18,699 | 100.0% | 45% | 512 | 0.0% | 41% |
| 2023-11-04 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 6,216 | 100.0% | 62% | 258 | 0.0% | 46% |
| 2023-11-04 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 152 | 100.0% | 92% | 128 | 0.0% | 54% |
| 2023-11-04 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,328 | 99.9% | 32% | 1,255 | 0.0% | 33% |
| 2023-11-04 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,256 | 99.9% | 30% | 1,256 | 0.0% | 31% |
| 2023-11-04 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,102 | 100.0% | 32% | 1,363 | 0.1% | 31% |
| 2023-11-04 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,635 | 100.0% | 20% | 2,164 | 0.0% | 28% |
| 2023-11-04 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 22 | 100.0% | 68% | 306 | 0.0% | 41% |
| 2023-11-04 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,489 | 100.0% | 17% | 2,352 | 0.0% | 31% |
| 2023-11-04 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,489 | 100.0% | 17% | 2,352 | 0.0% | 31% |
| 2023-11-04 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,856 | 100.0% | 21% | 1,559 | 0.0% | 36% |
| 2023-11-04 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 581 | 100.0% | 43% | 243 | 0.0% | 54% |
| 2023-11-04 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 15 | 100.0% | 73% | 130 | 0.0% | 67% |
| 2023-11-04 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,029 | 99.9% | 40% | 3,056 | 0.0% | 33% |
| 2023-11-04 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,857 | 99.9% | 18% | 1,268 | 0.1% | 22% |
| 2023-11-04 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,747 | 100.0% | 22% | 1,281 | 0.1% | 27% |
| 2023-11-04 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,431 | 100.0% | 27% | 1,036 | 0.0% | 34% |
| 2023-11-04 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 26 | 100.0% | 46% | 940 | 0.0% | 42% |
| 2023-11-04 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 75,388 | 100.0% | 51% | 478 | 0.0% | 37% |
| 2023-11-04 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 63,565 | 100.0% | 54% | 411 | 0.0% | 38% |
| 2023-11-04 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 47,148 | 100.0% | 56% | 372 | 0.0% | 39% |
| 2023-11-04 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 10,349 | 100.0% | 69% | 256 | 0.0% | 46% |
| 2023-11-04 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 263 | 100.0% | 93% | 107 | 0.0% | 52% |
| 2023-11-04 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 26,935 | 99.8% | 47% | 887 | 0.0% | 42% |
| 2023-11-04 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 24,076 | 99.8% | 49% | 848 | 0.0% | 42% |
| 2023-11-04 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 20,527 | 99.8% | 49% | 855 | 0.0% | 44% |
| 2023-11-04 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 10,992 | 99.8% | 61% | 658 | 0.1% | 47% |
| 2023-11-04 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 2,625 | 99.8% | 68% | 524 | 0.1% | 55% |
| 2023-11-04 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,550 | 99.7% | 33% | 1,029 | 0.0% | 51% |
| 2023-11-04 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,635 | 99.7% | 37% | 950 | 0.0% | 52% |
| 2023-11-04 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,578 | 99.7% | 43% | 715 | 0.0% | 55% |
| 2023-11-04 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 294 | 100.0% | 77% | 165 | 0.0% | 59% |
| 2023-11-04 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 29 | 100.0% | 90% | 134 | 0.0% | 72% |
| 2023-11-04 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,927 | 100.0% | 23% | 2,467 | 0.1% | 36% |
| 2023-11-04 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,927 | 100.0% | 23% | 2,467 | 0.1% | 36% |
| 2023-11-04 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,546 | 100.0% | 32% | 1,098 | 0.0% | 41% |
| 2023-11-04 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 83 | 100.0% | 87% | 124 | 0.0% | 67% |
| 2023-11-04 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 10 | 100.0% | 100% | none resolved | 0.0% | 80% |
| 2023-11-04 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.904 below threshold | | | | | | | | |
| 2023-11-05 | aave_perp_binance_bybit | ok | 0.999 | gross>0bps | 18,287 | 99.6% | 33% | 728 | 0.0% | 35% |
| 2023-11-05 | aave_perp_binance_bybit | ok | 0.999 | gross>1bps | 18,287 | 99.6% | 33% | 728 | 0.0% | 35% |
| 2023-11-05 | aave_perp_binance_bybit | ok | 0.999 | gross>2bps | 21,204 | 99.8% | 35% | 557 | 0.0% | 36% |
| 2023-11-05 | aave_perp_binance_bybit | ok | 0.999 | gross>5bps | 13,565 | 99.9% | 46% | 345 | 0.0% | 43% |
| 2023-11-05 | aave_perp_binance_bybit | ok | 0.999 | retail_taker | 1,371 | 100.0% | 76% | 154 | 0.0% | 56% |
| 2023-11-05 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,107 | 100.0% | 34% | 1,122 | 0.0% | 32% |
| 2023-11-05 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 16,365 | 100.0% | 34% | 800 | 0.0% | 33% |
| 2023-11-05 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 18,493 | 100.0% | 35% | 614 | 0.0% | 35% |
| 2023-11-05 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 13,747 | 100.0% | 47% | 374 | 0.0% | 40% |
| 2023-11-05 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 408 | 100.0% | 82% | 228 | 0.0% | 50% |
| 2023-11-05 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,926 | 99.9% | 36% | 3,399 | 0.0% | 33% |
| 2023-11-05 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,623 | 100.0% | 19% | 2,484 | 0.0% | 23% |
| 2023-11-05 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,359 | 100.0% | 22% | 1,320 | 0.0% | 28% |
| 2023-11-05 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 863 | 100.0% | 63% | 182 | 0.0% | 35% |
| 2023-11-05 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 38 | 100.0% | 79% | 1,008 | 0.0% | 29% |
| 2023-11-05 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,292 | 100.0% | 29% | 823 | 0.0% | 35% |
| 2023-11-05 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,292 | 100.0% | 29% | 823 | 0.0% | 35% |
| 2023-11-05 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,777 | 100.0% | 35% | 612 | 0.0% | 38% |
| 2023-11-05 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,590 | 100.0% | 50% | 294 | 0.0% | 44% |
| 2023-11-05 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 93 | 100.0% | 88% | 147 | 0.0% | 53% |
| 2023-11-05 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,684 | 100.0% | 32% | 1,374 | 0.1% | 31% |
| 2023-11-05 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,981 | 100.0% | 26% | 834 | 0.1% | 28% |
| 2023-11-05 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,298 | 100.0% | 30% | 566 | 0.0% | 29% |
| 2023-11-05 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,323 | 100.0% | 42% | 446 | 0.0% | 36% |
| 2023-11-05 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 58 | 100.0% | 83% | 148 | 0.0% | 45% |
| 2023-11-05 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 60,702 | 100.0% | 46% | 668 | 0.0% | 36% |
| 2023-11-05 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 49,136 | 100.0% | 50% | 522 | 0.0% | 39% |
| 2023-11-05 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 31,848 | 100.0% | 58% | 380 | 0.0% | 41% |
| 2023-11-05 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,375 | 100.0% | 81% | 168 | 0.0% | 47% |
| 2023-11-05 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 159 | 100.0% | 89% | 136 | 0.0% | 48% |
| 2023-11-05 | tia_perp_binance_bybit | ok | 0.999 | gross>0bps | 27,394 | 99.7% | 42% | 829 | 0.0% | 35% |
| 2023-11-05 | tia_perp_binance_bybit | ok | 0.999 | gross>1bps | 23,717 | 99.7% | 43% | 767 | 0.0% | 35% |
| 2023-11-05 | tia_perp_binance_bybit | ok | 0.999 | gross>2bps | 20,215 | 99.7% | 45% | 727 | 0.0% | 37% |
| 2023-11-05 | tia_perp_binance_bybit | ok | 0.999 | gross>5bps | 8,991 | 99.8% | 59% | 547 | 0.0% | 44% |
| 2023-11-05 | tia_perp_binance_bybit | ok | 0.999 | retail_taker | 1,079 | 100.0% | 77% | 187 | 0.0% | 57% |
| 2023-11-05 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,485 | 99.9% | 36% | 898 | 0.0% | 49% |
| 2023-11-05 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,008 | 99.9% | 39% | 810 | 0.0% | 50% |
| 2023-11-05 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,123 | 100.0% | 49% | 542 | 0.0% | 53% |
| 2023-11-05 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 380 | 100.0% | 77% | 157 | 0.0% | 53% |
| 2023-11-05 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 47 | 100.0% | 81% | 141 | 0.0% | 40% |
| 2023-11-05 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,369 | 100.0% | 35% | 599 | 0.0% | 32% |
| 2023-11-05 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 14,369 | 100.0% | 35% | 599 | 0.0% | 32% |
| 2023-11-05 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 9,320 | 100.0% | 44% | 331 | 0.0% | 36% |
| 2023-11-05 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,105 | 100.0% | 74% | 146 | 0.0% | 47% |
| 2023-11-05 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 273 | 100.0% | 89% | 114 | 0.0% | 52% |
| 2023-11-05 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.843 below threshold | | | | | | | | |
| 2023-11-06 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 30,782 | 99.9% | 40% | 496 | 0.0% | 36% |
| 2023-11-06 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 30,788 | 99.9% | 40% | 497 | 0.0% | 36% |
| 2023-11-06 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 26,204 | 99.9% | 43% | 380 | 0.0% | 38% |
| 2023-11-06 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 12,413 | 100.0% | 54% | 274 | 0.0% | 42% |
| 2023-11-06 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 2,240 | 100.0% | 73% | 159 | 0.0% | 45% |
| 2023-11-06 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,245 | 100.0% | 30% | 1,002 | 0.0% | 30% |
| 2023-11-06 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,951 | 100.0% | 29% | 778 | 0.0% | 31% |
| 2023-11-06 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 15,757 | 100.0% | 30% | 644 | 0.0% | 32% |
| 2023-11-06 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 18,440 | 100.0% | 39% | 406 | 0.0% | 34% |
| 2023-11-06 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 1,024 | 100.0% | 78% | 199 | 0.0% | 48% |
| 2023-11-06 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,724 | 99.9% | 29% | 8,440 | 0.0% | 29% |
| 2023-11-06 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,477 | 99.9% | 14% | 3,066 | 0.0% | 20% |
| 2023-11-06 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,472 | 100.0% | 20% | 1,264 | 0.0% | 28% |
| 2023-11-06 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,511 | 100.0% | 30% | 996 | 0.0% | 32% |
| 2023-11-06 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 6 | 100.0% | 100% | none resolved | 0.0% | 67% |
| 2023-11-06 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,333 | 100.0% | 24% | 1,232 | 0.0% | 28% |
| 2023-11-06 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,333 | 100.0% | 24% | 1,232 | 0.0% | 28% |
| 2023-11-06 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,433 | 100.0% | 25% | 735 | 0.0% | 28% |
| 2023-11-06 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 10,382 | 100.0% | 35% | 422 | 0.0% | 32% |
| 2023-11-06 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 837 | 100.0% | 81% | 141 | 0.0% | 49% |
| 2023-11-06 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,502 | 100.0% | 24% | 2,603 | 0.0% | 30% |
| 2023-11-06 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,983 | 100.0% | 19% | 2,119 | 0.0% | 26% |
| 2023-11-06 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,422 | 100.0% | 23% | 1,096 | 0.0% | 28% |
| 2023-11-06 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 848 | 100.0% | 72% | 130 | 0.0% | 47% |
| 2023-11-06 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 7 | 100.0% | 100% | none resolved | 0.0% | 43% |
| 2023-11-06 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 57,898 | 100.0% | 45% | 630 | 0.0% | 37% |
| 2023-11-06 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 46,883 | 100.0% | 50% | 530 | 0.0% | 38% |
| 2023-11-06 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 29,563 | 100.0% | 56% | 450 | 0.0% | 41% |
| 2023-11-06 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,588 | 100.0% | 64% | 262 | 0.0% | 42% |
| 2023-11-06 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 396 | 100.0% | 75% | 149 | 0.0% | 41% |
| 2023-11-06 | tia_perp_binance_bybit | ok | 0.998 | gross>0bps | 22,457 | 99.2% | 47% | 1,035 | 0.0% | 40% |
| 2023-11-06 | tia_perp_binance_bybit | ok | 0.998 | gross>1bps | 20,712 | 99.3% | 51% | 946 | 0.0% | 42% |
| 2023-11-06 | tia_perp_binance_bybit | ok | 0.998 | gross>2bps | 17,400 | 99.2% | 51% | 948 | 0.0% | 42% |
| 2023-11-06 | tia_perp_binance_bybit | ok | 0.998 | gross>5bps | 8,980 | 99.1% | 56% | 789 | 0.0% | 45% |
| 2023-11-06 | tia_perp_binance_bybit | ok | 0.998 | retail_taker | 1,163 | 99.7% | 76% | 262 | 0.0% | 52% |
| 2023-11-06 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 9,657 | 99.8% | 33% | 937 | 0.0% | 52% |
| 2023-11-06 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,454 | 99.9% | 36% | 843 | 0.0% | 53% |
| 2023-11-06 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,111 | 99.9% | 45% | 692 | 0.0% | 56% |
| 2023-11-06 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 424 | 100.0% | 66% | 338 | 0.0% | 64% |
| 2023-11-06 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 29 | 100.0% | 97% | 124 | 0.0% | 55% |
| 2023-11-06 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 22,811 | 100.0% | 36% | 499 | 0.0% | 32% |
| 2023-11-06 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 22,811 | 100.0% | 36% | 499 | 0.0% | 32% |
| 2023-11-06 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 20,387 | 100.0% | 38% | 348 | 0.0% | 32% |
| 2023-11-06 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 10,925 | 100.0% | 50% | 236 | 0.0% | 37% |
| 2023-11-06 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 861 | 100.0% | 91% | 116 | 0.0% | 52% |
| 2023-11-06 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.895 below threshold | | | | | | | | |
| 2023-11-07 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 49,521 | 100.0% | 43% | 473 | 0.0% | 36% |
| 2023-11-07 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 48,952 | 100.0% | 44% | 453 | 0.0% | 37% |
| 2023-11-07 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 37,620 | 100.0% | 49% | 367 | 0.0% | 40% |
| 2023-11-07 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 9,679 | 100.0% | 64% | 238 | 0.0% | 47% |
| 2023-11-07 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 684 | 100.0% | 91% | 119 | 0.0% | 49% |
| 2023-11-07 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,423 | 100.0% | 39% | 830 | 0.0% | 36% |
| 2023-11-07 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,730 | 100.0% | 37% | 715 | 0.0% | 34% |
| 2023-11-07 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 15,215 | 100.0% | 36% | 597 | 0.0% | 34% |
| 2023-11-07 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 15,731 | 100.0% | 41% | 552 | 0.0% | 37% |
| 2023-11-07 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 1,717 | 100.0% | 75% | 194 | 0.0% | 50% |
| 2023-11-07 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,191 | 99.9% | 47% | 3,876 | 0.0% | 37% |
| 2023-11-07 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,435 | 100.0% | 23% | 1,682 | 0.0% | 26% |
| 2023-11-07 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,432 | 100.0% | 20% | 908 | 0.0% | 24% |
| 2023-11-07 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,551 | 100.0% | 39% | 488 | 0.0% | 35% |
| 2023-11-07 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 32 | 100.0% | 72% | 226 | 0.0% | 38% |
| 2023-11-07 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 21,030 | 100.0% | 38% | 611 | 0.0% | 37% |
| 2023-11-07 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 21,030 | 100.0% | 38% | 611 | 0.0% | 37% |
| 2023-11-07 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 13,486 | 100.0% | 47% | 393 | 0.0% | 40% |
| 2023-11-07 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,621 | 100.0% | 75% | 154 | 0.0% | 51% |
| 2023-11-07 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 153 | 100.0% | 99% | 100 | 0.0% | 59% |
| 2023-11-07 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 21,567 | 100.0% | 23% | 1,209 | 0.0% | 30% |
| 2023-11-07 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 15,621 | 100.0% | 32% | 811 | 0.0% | 34% |
| 2023-11-07 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,435 | 100.0% | 44% | 409 | 0.0% | 38% |
| 2023-11-07 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 164 | 100.0% | 80% | 128 | 0.0% | 55% |
| 2023-11-07 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 15 | 100.0% | 67% | 114 | 0.0% | 53% |
| 2023-11-07 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 66,923 | 100.0% | 46% | 496 | 0.0% | 36% |
| 2023-11-07 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 56,555 | 100.0% | 51% | 388 | 0.0% | 39% |
| 2023-11-07 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 44,614 | 100.0% | 54% | 337 | 0.0% | 40% |
| 2023-11-07 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 22,182 | 100.0% | 58% | 248 | 0.0% | 39% |
| 2023-11-07 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 1,234 | 100.0% | 85% | 138 | 0.0% | 49% |
| 2023-11-07 | tia_perp_binance_bybit | ok | 0.999 | gross>0bps | 15,384 | 99.6% | 42% | 1,150 | 0.0% | 36% |
| 2023-11-07 | tia_perp_binance_bybit | ok | 0.999 | gross>1bps | 15,544 | 99.6% | 42% | 1,074 | 0.0% | 36% |
| 2023-11-07 | tia_perp_binance_bybit | ok | 0.999 | gross>2bps | 15,517 | 99.6% | 42% | 1,008 | 0.0% | 37% |
| 2023-11-07 | tia_perp_binance_bybit | ok | 0.999 | gross>5bps | 14,537 | 99.6% | 42% | 804 | 0.0% | 38% |
| 2023-11-07 | tia_perp_binance_bybit | ok | 0.999 | retail_taker | 8,905 | 99.9% | 48% | 486 | 0.0% | 42% |
| 2023-11-07 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 15,266 | 99.9% | 36% | 862 | 0.0% | 48% |
| 2023-11-07 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,249 | 99.9% | 38% | 788 | 0.0% | 49% |
| 2023-11-07 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,348 | 99.9% | 44% | 640 | 0.0% | 52% |
| 2023-11-07 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 923 | 100.0% | 75% | 213 | 0.0% | 60% |
| 2023-11-07 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 105 | 100.0% | 85% | 115 | 0.0% | 60% |
| 2023-11-07 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 24,380 | 100.0% | 45% | 494 | 0.0% | 37% |
| 2023-11-07 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 24,380 | 100.0% | 45% | 494 | 0.0% | 37% |
| 2023-11-07 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 13,503 | 100.0% | 55% | 330 | 0.0% | 40% |
| 2023-11-07 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,464 | 100.0% | 76% | 178 | 0.0% | 45% |
| 2023-11-07 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 593 | 100.0% | 91% | 160 | 0.0% | 45% |
| 2023-11-07 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.906 below threshold | | | | | | | | |
| 2023-11-08 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,841 | 99.8% | 36% | 997 | 0.0% | 42% |
| 2023-11-08 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 13,972 | 99.8% | 37% | 943 | 0.0% | 42% |
| 2023-11-08 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,726 | 99.8% | 39% | 800 | 0.0% | 43% |
| 2023-11-08 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 8,696 | 99.9% | 37% | 574 | 0.0% | 38% |
| 2023-11-08 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 325 | 100.0% | 91% | 108 | 0.0% | 60% |
| 2023-11-08 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,816 | 100.0% | 37% | 1,295 | 0.0% | 35% |
| 2023-11-08 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,387 | 100.0% | 36% | 1,146 | 0.1% | 35% |
| 2023-11-08 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,135 | 100.0% | 35% | 1,076 | 0.0% | 36% |
| 2023-11-08 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 8,987 | 100.0% | 40% | 658 | 0.0% | 38% |
| 2023-11-08 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 404 | 100.0% | 84% | 134 | 0.0% | 53% |
| 2023-11-08 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 572 | 99.8% | 49% | 8,100 | 4.7% | 41% |
| 2023-11-08 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,085 | 99.9% | 27% | 2,882 | 2.4% | 26% |
| 2023-11-08 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,176 | 100.0% | 18% | 1,392 | 0.9% | 22% |
| 2023-11-08 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 7,335 | 100.0% | 36% | 437 | 0.1% | 34% |
| 2023-11-08 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 61 | 100.0% | 80% | 136 | 6.6% | 48% |
| 2023-11-08 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,961 | 100.0% | 36% | 841 | 0.0% | 38% |
| 2023-11-08 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,961 | 100.0% | 36% | 841 | 0.0% | 38% |
| 2023-11-08 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,853 | 100.0% | 39% | 773 | 0.0% | 37% |
| 2023-11-08 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,336 | 100.0% | 46% | 514 | 0.0% | 39% |
| 2023-11-08 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 282 | 100.0% | 93% | 115 | 0.0% | 60% |
| 2023-11-08 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,813 | 100.0% | 20% | 3,372 | 0.0% | 30% |
| 2023-11-08 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,293 | 100.0% | 21% | 1,904 | 0.0% | 31% |
| 2023-11-08 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,257 | 100.0% | 22% | 868 | 0.0% | 29% |
| 2023-11-08 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,360 | 100.0% | 29% | 462 | 0.0% | 31% |
| 2023-11-08 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 5 | 100.0% | 80% | 256 | 0.0% | 40% |
| 2023-11-08 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 24,704 | 100.0% | 45% | 760 | 0.0% | 36% |
| 2023-11-08 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 25,373 | 100.0% | 44% | 652 | 0.0% | 36% |
| 2023-11-08 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 24,964 | 100.0% | 44% | 570 | 0.0% | 36% |
| 2023-11-08 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 14,467 | 100.0% | 49% | 379 | 0.0% | 38% |
| 2023-11-08 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 231 | 100.0% | 90% | 115 | 0.0% | 57% |
| 2023-11-08 | tia_perp_binance_bybit | ok | 0.996 | gross>0bps | 13,656 | 97.7% | 45% | 1,200 | 0.0% | 38% |
| 2023-11-08 | tia_perp_binance_bybit | ok | 0.996 | gross>1bps | 12,753 | 97.7% | 45% | 1,213 | 0.0% | 39% |
| 2023-11-08 | tia_perp_binance_bybit | ok | 0.996 | gross>2bps | 13,246 | 97.9% | 48% | 1,076 | 0.0% | 40% |
| 2023-11-08 | tia_perp_binance_bybit | ok | 0.996 | gross>5bps | 9,916 | 98.3% | 53% | 792 | 0.0% | 43% |
| 2023-11-08 | tia_perp_binance_bybit | ok | 0.996 | retail_taker | 1,702 | 99.4% | 67% | 286 | 0.0% | 49% |
| 2023-11-08 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,873 | 99.9% | 31% | 1,286 | 0.0% | 53% |
| 2023-11-08 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,168 | 99.9% | 33% | 1,200 | 0.0% | 53% |
| 2023-11-08 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,657 | 99.9% | 38% | 955 | 0.0% | 55% |
| 2023-11-08 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 353 | 100.0% | 71% | 399 | 0.0% | 59% |
| 2023-11-08 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 56 | 100.0% | 95% | 214 | 0.0% | 55% |
| 2023-11-08 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,857 | 100.0% | 34% | 912 | 0.0% | 35% |
| 2023-11-08 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,857 | 100.0% | 34% | 912 | 0.0% | 35% |
| 2023-11-08 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,909 | 100.0% | 40% | 696 | 0.0% | 39% |
| 2023-11-08 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,079 | 100.0% | 47% | 607 | 0.0% | 43% |
| 2023-11-08 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 147 | 100.0% | 68% | 176 | 0.0% | 46% |
| 2023-11-08 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.930 below threshold | | | | | | | | |
| 2023-11-09 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 56,031 | 100.0% | 47% | 468 | 0.0% | 35% |
| 2023-11-09 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 52,203 | 100.0% | 48% | 437 | 0.0% | 36% |
| 2023-11-09 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 43,331 | 100.0% | 52% | 377 | 0.0% | 37% |
| 2023-11-09 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 20,088 | 100.0% | 58% | 330 | 0.0% | 38% |
| 2023-11-09 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 2,994 | 100.0% | 84% | 142 | 0.2% | 49% |
| 2023-11-09 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 46,761 | 100.0% | 50% | 448 | 0.1% | 33% |
| 2023-11-09 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 42,977 | 100.0% | 52% | 412 | 0.1% | 34% |
| 2023-11-09 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 38,369 | 100.0% | 53% | 382 | 0.1% | 35% |
| 2023-11-09 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 24,022 | 100.0% | 59% | 284 | 0.1% | 36% |
| 2023-11-09 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 5,185 | 100.0% | 73% | 210 | 0.2% | 41% |
| 2023-11-09 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 23,100 | 100.0% | 44% | 440 | 0.2% | 31% |
| 2023-11-09 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 21,679 | 100.0% | 47% | 440 | 0.3% | 31% |
| 2023-11-09 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 19,352 | 100.0% | 45% | 466 | 0.2% | 30% |
| 2023-11-09 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 9,022 | 100.0% | 49% | 444 | 0.5% | 33% |
| 2023-11-09 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 467 | 100.0% | 81% | 206 | 7.7% | 44% |
| 2023-11-09 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 20,769 | 100.0% | 42% | 647 | 0.0% | 33% |
| 2023-11-09 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 20,769 | 100.0% | 42% | 647 | 0.0% | 33% |
| 2023-11-09 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 18,319 | 100.0% | 43% | 579 | 0.0% | 34% |
| 2023-11-09 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 13,508 | 100.0% | 44% | 452 | 0.0% | 34% |
| 2023-11-09 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 1,734 | 100.0% | 76% | 203 | 0.0% | 40% |
| 2023-11-09 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 21,688 | 100.0% | 53% | 474 | 0.1% | 34% |
| 2023-11-09 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 22,128 | 100.0% | 51% | 416 | 0.2% | 34% |
| 2023-11-09 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 23,830 | 100.0% | 47% | 384 | 0.2% | 32% |
| 2023-11-09 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 18,206 | 100.0% | 52% | 277 | 0.1% | 36% |
| 2023-11-09 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 2,541 | 100.0% | 71% | 197 | 0.2% | 37% |
| 2023-11-09 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 76,709 | 100.0% | 56% | 413 | 0.0% | 37% |
| 2023-11-09 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 77,866 | 100.0% | 55% | 362 | 0.0% | 36% |
| 2023-11-09 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 78,771 | 100.0% | 55% | 322 | 0.0% | 36% |
| 2023-11-09 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 52,350 | 100.0% | 63% | 248 | 0.0% | 40% |
| 2023-11-09 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 3,761 | 100.0% | 85% | 159 | 0.6% | 46% |
| 2023-11-09 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 23,330 | 99.8% | 39% | 754 | 0.0% | 33% |
| 2023-11-09 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 23,856 | 99.8% | 39% | 678 | 0.0% | 33% |
| 2023-11-09 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 23,740 | 99.8% | 38% | 592 | 0.0% | 33% |
| 2023-11-09 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 20,525 | 99.9% | 43% | 456 | 0.0% | 34% |
| 2023-11-09 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 9,515 | 100.0% | 48% | 400 | 0.0% | 37% |
| 2023-11-09 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 19,384 | 100.0% | 37% | 613 | 0.0% | 40% |
| 2023-11-09 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 16,552 | 100.0% | 40% | 561 | 0.0% | 40% |
| 2023-11-09 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 12,121 | 100.0% | 45% | 428 | 0.0% | 39% |
| 2023-11-09 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 5,322 | 100.0% | 54% | 278 | 0.0% | 37% |
| 2023-11-09 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 1,016 | 100.0% | 75% | 184 | 0.5% | 39% |
| 2023-11-09 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 29,631 | 100.0% | 51% | 384 | 0.0% | 36% |
| 2023-11-09 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 29,631 | 100.0% | 51% | 384 | 0.0% | 36% |
| 2023-11-09 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 19,210 | 100.0% | 57% | 370 | 0.0% | 38% |
| 2023-11-09 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 7,724 | 100.0% | 69% | 264 | 0.0% | 42% |
| 2023-11-09 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 2,288 | 100.0% | 81% | 187 | 0.0% | 42% |
| 2023-11-09 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.914 below threshold | | | | | | | | |
| 2023-11-10 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 24,817 | 100.0% | 37% | 591 | 0.0% | 34% |
| 2023-11-10 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 24,381 | 100.0% | 37% | 556 | 0.0% | 34% |
| 2023-11-10 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 24,537 | 100.0% | 39% | 481 | 0.0% | 36% |
| 2023-11-10 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 11,666 | 100.0% | 50% | 307 | 0.0% | 42% |
| 2023-11-10 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 278 | 100.0% | 82% | 134 | 0.0% | 52% |
| 2023-11-10 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 26,868 | 100.0% | 40% | 628 | 0.0% | 32% |
| 2023-11-10 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 25,416 | 100.0% | 40% | 544 | 0.0% | 32% |
| 2023-11-10 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 24,249 | 100.0% | 41% | 479 | 0.0% | 33% |
| 2023-11-10 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 16,783 | 100.0% | 44% | 362 | 0.0% | 33% |
| 2023-11-10 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 694 | 100.0% | 84% | 128 | 0.0% | 53% |
| 2023-11-10 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,424 | 100.0% | 29% | 829 | 0.0% | 27% |
| 2023-11-10 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,773 | 100.0% | 26% | 1,392 | 0.0% | 25% |
| 2023-11-10 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,526 | 100.0% | 21% | 876 | 0.0% | 25% |
| 2023-11-10 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 7,911 | 100.0% | 27% | 1,123 | 0.0% | 26% |
| 2023-11-10 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 40 | 100.0% | 80% | 124 | 0.0% | 42% |
| 2023-11-10 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,790 | 100.0% | 29% | 974 | 0.0% | 32% |
| 2023-11-10 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,790 | 100.0% | 29% | 974 | 0.0% | 32% |
| 2023-11-10 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,768 | 100.0% | 28% | 842 | 0.0% | 32% |
| 2023-11-10 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 6,157 | 100.0% | 35% | 592 | 0.0% | 38% |
| 2023-11-10 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 104 | 100.0% | 95% | 114 | 0.0% | 44% |
| 2023-11-10 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,941 | 100.0% | 30% | 1,052 | 0.0% | 32% |
| 2023-11-10 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,840 | 100.0% | 27% | 1,126 | 0.0% | 27% |
| 2023-11-10 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 12,473 | 100.0% | 24% | 727 | 0.0% | 26% |
| 2023-11-10 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 6,429 | 100.0% | 33% | 498 | 0.0% | 31% |
| 2023-11-10 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 109 | 100.0% | 85% | 128 | 0.0% | 50% |
| 2023-11-10 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 52,066 | 100.0% | 55% | 404 | 0.0% | 36% |
| 2023-11-10 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 55,415 | 100.0% | 53% | 354 | 0.0% | 36% |
| 2023-11-10 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 60,614 | 100.0% | 52% | 311 | 0.0% | 35% |
| 2023-11-10 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 54,010 | 100.0% | 56% | 236 | 0.0% | 38% |
| 2023-11-10 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 23,146 | 100.0% | 58% | 202 | 0.0% | 37% |
| 2023-11-10 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 26,784 | 99.7% | 42% | 606 | 0.0% | 33% |
| 2023-11-10 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 27,534 | 99.7% | 43% | 569 | 0.0% | 32% |
| 2023-11-10 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 27,579 | 99.7% | 43% | 504 | 0.0% | 31% |
| 2023-11-10 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 27,292 | 99.8% | 43% | 398 | 0.0% | 31% |
| 2023-11-10 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 14,409 | 99.9% | 53% | 288 | 0.0% | 36% |
| 2023-11-10 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,622 | 100.0% | 32% | 745 | 0.0% | 41% |
| 2023-11-10 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,321 | 100.0% | 35% | 675 | 0.0% | 42% |
| 2023-11-10 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,134 | 100.0% | 39% | 556 | 0.0% | 42% |
| 2023-11-10 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,633 | 100.0% | 43% | 406 | 0.0% | 39% |
| 2023-11-10 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 672 | 100.0% | 63% | 248 | 0.0% | 46% |
| 2023-11-10 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 12,895 | 100.0% | 34% | 986 | 0.0% | 33% |
| 2023-11-10 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,895 | 100.0% | 34% | 986 | 0.0% | 33% |
| 2023-11-10 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,341 | 100.0% | 38% | 622 | 0.0% | 35% |
| 2023-11-10 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,352 | 100.0% | 74% | 130 | 0.0% | 44% |
| 2023-11-10 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 163 | 100.0% | 91% | 133 | 0.0% | 48% |
| 2023-11-10 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.887 below threshold | | | | | | | | |
| 2023-11-11 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 25,360 | 99.9% | 34% | 570 | 0.0% | 33% |
| 2023-11-11 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 25,452 | 99.9% | 35% | 572 | 0.0% | 33% |
| 2023-11-11 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 26,472 | 99.9% | 37% | 522 | 0.0% | 34% |
| 2023-11-11 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 13,060 | 100.0% | 46% | 386 | 0.0% | 42% |
| 2023-11-11 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 323 | 100.0% | 90% | 137 | 0.0% | 51% |
| 2023-11-11 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 17,015 | 100.0% | 40% | 690 | 0.0% | 32% |
| 2023-11-11 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 16,816 | 100.0% | 39% | 632 | 0.0% | 31% |
| 2023-11-11 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 16,825 | 100.0% | 39% | 584 | 0.0% | 32% |
| 2023-11-11 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 13,418 | 100.0% | 42% | 505 | 0.0% | 34% |
| 2023-11-11 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 951 | 100.0% | 82% | 177 | 0.0% | 48% |
| 2023-11-11 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,195 | 100.0% | 24% | 3,103 | 0.0% | 27% |
| 2023-11-11 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,915 | 100.0% | 22% | 1,728 | 0.0% | 24% |
| 2023-11-11 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,134 | 100.0% | 27% | 1,134 | 0.0% | 30% |
| 2023-11-11 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 114 | 100.0% | 83% | 260 | 0.0% | 41% |
| 2023-11-11 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 18 | 100.0% | 72% | 343 | 0.0% | 50% |
| 2023-11-11 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 37,091 | 100.0% | 40% | 528 | 0.0% | 34% |
| 2023-11-11 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 37,091 | 100.0% | 40% | 528 | 0.0% | 34% |
| 2023-11-11 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 28,447 | 100.0% | 45% | 395 | 0.0% | 37% |
| 2023-11-11 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 8,651 | 100.0% | 64% | 224 | 0.0% | 43% |
| 2023-11-11 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 447 | 100.0% | 90% | 132 | 0.0% | 54% |
| 2023-11-11 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,268 | 100.0% | 28% | 1,612 | 0.0% | 29% |
| 2023-11-11 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,728 | 100.0% | 26% | 1,554 | 0.0% | 27% |
| 2023-11-11 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 9,616 | 100.0% | 26% | 1,024 | 0.0% | 29% |
| 2023-11-11 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,125 | 100.0% | 53% | 287 | 0.0% | 36% |
| 2023-11-11 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 78 | 100.0% | 79% | 215 | 0.0% | 44% |
| 2023-11-11 | sol_perp_binance_bybit | excluded: bybit_ob/bybit/SOL-USDT/perp coverage 1.000 below threshold | | | | | | | | |
| 2023-11-11 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 30,800 | 100.0% | 46% | 477 | 0.0% | 31% |
| 2023-11-11 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 33,633 | 100.0% | 45% | 452 | 0.0% | 30% |
| 2023-11-11 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 37,070 | 100.0% | 44% | 423 | 0.0% | 30% |
| 2023-11-11 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 50,162 | 100.0% | 42% | 330 | 0.0% | 28% |
| 2023-11-11 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 56,645 | 100.0% | 46% | 259 | 0.0% | 30% |
| 2023-11-11 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 29,598 | 100.0% | 42% | 544 | 0.0% | 39% |
| 2023-11-11 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 23,755 | 100.0% | 44% | 505 | 0.0% | 40% |
| 2023-11-11 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 16,696 | 100.0% | 47% | 420 | 0.0% | 42% |
| 2023-11-11 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,305 | 100.0% | 65% | 276 | 0.0% | 47% |
| 2023-11-11 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 440 | 100.0% | 91% | 123 | 0.0% | 62% |
| 2023-11-11 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,550 | 100.0% | 34% | 684 | 0.0% | 33% |
| 2023-11-11 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 13,550 | 100.0% | 34% | 684 | 0.0% | 33% |
| 2023-11-11 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 9,298 | 100.0% | 39% | 477 | 0.0% | 37% |
| 2023-11-11 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,114 | 100.0% | 69% | 174 | 0.0% | 46% |
| 2023-11-11 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 250 | 100.0% | 90% | 153 | 0.0% | 47% |
| 2023-11-11 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.872 below threshold | | | | | | | | |
| 2023-11-12 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,464 | 99.7% | 30% | 788 | 0.0% | 30% |
| 2023-11-12 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,464 | 99.7% | 30% | 788 | 0.0% | 30% |
| 2023-11-12 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 15,157 | 99.8% | 33% | 660 | 0.0% | 32% |
| 2023-11-12 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 19,703 | 99.9% | 38% | 424 | 0.0% | 36% |
| 2023-11-12 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 339 | 100.0% | 85% | 133 | 0.0% | 58% |
| 2023-11-12 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 19,819 | 100.0% | 37% | 638 | 0.0% | 32% |
| 2023-11-12 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 18,614 | 100.0% | 38% | 568 | 0.0% | 32% |
| 2023-11-12 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 17,375 | 100.0% | 38% | 577 | 0.0% | 32% |
| 2023-11-12 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 10,887 | 100.0% | 45% | 427 | 0.0% | 36% |
| 2023-11-12 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 316 | 100.0% | 88% | 214 | 0.0% | 57% |
| 2023-11-12 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,670 | 100.0% | 19% | 3,262 | 0.0% | 27% |
| 2023-11-12 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,990 | 100.0% | 28% | 1,637 | 0.0% | 32% |
| 2023-11-12 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,193 | 100.0% | 39% | 572 | 0.0% | 36% |
| 2023-11-12 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 21 | 100.0% | 76% | 125 | 0.0% | 62% |
| 2023-11-12 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 0% |
| 2023-11-12 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 19,191 | 100.0% | 39% | 680 | 0.0% | 36% |
| 2023-11-12 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 19,191 | 100.0% | 39% | 680 | 0.0% | 36% |
| 2023-11-12 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 13,403 | 100.0% | 44% | 550 | 0.0% | 39% |
| 2023-11-12 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 5,877 | 100.0% | 44% | 439 | 0.0% | 38% |
| 2023-11-12 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 217 | 100.0% | 94% | 112 | 0.0% | 55% |
| 2023-11-12 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,711 | 100.0% | 28% | 1,074 | 0.0% | 30% |
| 2023-11-12 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,498 | 100.0% | 27% | 1,130 | 0.0% | 27% |
| 2023-11-12 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,971 | 100.0% | 25% | 1,050 | 0.0% | 26% |
| 2023-11-12 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,293 | 100.0% | 46% | 332 | 0.1% | 41% |
| 2023-11-12 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 24 | 100.0% | 83% | 166 | 0.0% | 50% |
| 2023-11-12 | sol_perp_binance_bybit | excluded: bybit_ob/bybit/SOL-USDT/perp coverage 1.000 below threshold | | | | | | | | |
| 2023-11-12 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 19,173 | 100.0% | 44% | 676 | 0.0% | 33% |
| 2023-11-12 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 20,756 | 100.0% | 43% | 618 | 0.0% | 32% |
| 2023-11-12 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 22,683 | 100.0% | 42% | 570 | 0.0% | 31% |
| 2023-11-12 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 30,268 | 100.0% | 40% | 469 | 0.0% | 30% |
| 2023-11-12 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 38,741 | 100.0% | 43% | 334 | 0.0% | 31% |
| 2023-11-12 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,206 | 99.9% | 40% | 750 | 0.0% | 44% |
| 2023-11-12 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,127 | 99.9% | 44% | 696 | 0.0% | 45% |
| 2023-11-12 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,331 | 100.0% | 51% | 592 | 0.0% | 47% |
| 2023-11-12 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 789 | 99.9% | 75% | 416 | 0.0% | 56% |
| 2023-11-12 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 46 | 100.0% | 93% | 107 | 0.0% | 70% |
| 2023-11-12 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,833 | 100.0% | 33% | 1,019 | 0.0% | 37% |
| 2023-11-12 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,833 | 100.0% | 33% | 1,019 | 0.0% | 37% |
| 2023-11-12 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,932 | 100.0% | 42% | 630 | 0.0% | 45% |
| 2023-11-12 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 220 | 100.0% | 84% | 181 | 0.0% | 58% |
| 2023-11-12 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 11 | 100.0% | 91% | 103 | 0.0% | 27% |
| 2023-11-12 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.863 below threshold | | | | | | | | |
| 2023-11-13 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 17,550 | 99.9% | 32% | 468 | 0.0% | 29% |
| 2023-11-13 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 18,560 | 100.0% | 33% | 436 | 0.0% | 30% |
| 2023-11-13 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 21,906 | 100.0% | 34% | 414 | 0.0% | 30% |
| 2023-11-13 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 21,305 | 100.0% | 38% | 372 | 0.0% | 35% |
| 2023-11-13 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 1,311 | 100.0% | 72% | 260 | 0.0% | 51% |
| 2023-11-13 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 40,962 | 100.0% | 43% | 526 | 0.0% | 32% |
| 2023-11-13 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 35,667 | 100.0% | 44% | 486 | 0.0% | 34% |
| 2023-11-13 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 29,309 | 100.0% | 46% | 418 | 0.0% | 35% |
| 2023-11-13 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 10,596 | 100.0% | 59% | 290 | 0.0% | 40% |
| 2023-11-13 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 438 | 100.0% | 88% | 166 | 0.0% | 47% |
| 2023-11-13 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,199 | 100.0% | 26% | 1,269 | 0.0% | 27% |
| 2023-11-13 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,651 | 100.0% | 28% | 1,061 | 0.0% | 26% |
| 2023-11-13 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,060 | 100.0% | 28% | 1,138 | 0.1% | 25% |
| 2023-11-13 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 572 | 100.0% | 62% | 209 | 0.2% | 38% |
| 2023-11-13 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 12 | 100.0% | 75% | 312 | 0.0% | 17% |
| 2023-11-13 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 29,224 | 100.0% | 40% | 535 | 0.0% | 37% |
| 2023-11-13 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 29,224 | 100.0% | 40% | 535 | 0.0% | 37% |
| 2023-11-13 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 17,860 | 100.0% | 51% | 364 | 0.0% | 42% |
| 2023-11-13 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,036 | 100.0% | 74% | 186 | 0.0% | 47% |
| 2023-11-13 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 220 | 100.0% | 88% | 162 | 0.0% | 40% |
| 2023-11-13 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 20,164 | 100.0% | 34% | 900 | 0.0% | 30% |
| 2023-11-13 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 21,814 | 100.0% | 31% | 608 | 0.0% | 28% |
| 2023-11-13 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 17,753 | 100.0% | 37% | 438 | 0.0% | 32% |
| 2023-11-13 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,380 | 100.0% | 68% | 166 | 0.1% | 47% |
| 2023-11-13 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 32 | 100.0% | 75% | 157 | 0.0% | 44% |
| 2023-11-13 | sol_perp_binance_bybit | excluded: bybit_ob/bybit/SOL-USDT/perp coverage 1.000 below threshold | | | | | | | | |
| 2023-11-13 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 30,146 | 100.0% | 51% | 574 | 0.0% | 35% |
| 2023-11-13 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 31,794 | 100.0% | 50% | 568 | 0.0% | 34% |
| 2023-11-13 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 33,983 | 100.0% | 48% | 554 | 0.0% | 34% |
| 2023-11-13 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 44,480 | 100.0% | 45% | 446 | 0.0% | 32% |
| 2023-11-13 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 62,091 | 100.0% | 47% | 292 | 0.0% | 33% |
| 2023-11-13 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 72,562 | 100.0% | 57% | 338 | 0.0% | 39% |
| 2023-11-13 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 63,847 | 100.0% | 59% | 318 | 0.0% | 39% |
| 2023-11-13 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 53,667 | 100.0% | 61% | 304 | 0.0% | 39% |
| 2023-11-13 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 28,394 | 100.0% | 68% | 252 | 0.0% | 41% |
| 2023-11-13 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 6,026 | 100.0% | 88% | 138 | 0.0% | 50% |
| 2023-11-13 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 29,380 | 100.0% | 57% | 434 | 0.0% | 37% |
| 2023-11-13 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 29,380 | 100.0% | 57% | 434 | 0.0% | 37% |
| 2023-11-13 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 21,261 | 100.0% | 67% | 276 | 0.0% | 39% |
| 2023-11-13 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 12,363 | 100.0% | 79% | 180 | 0.0% | 40% |
| 2023-11-13 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 6,291 | 100.0% | 86% | 164 | 0.0% | 43% |
| 2023-11-13 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.924 below threshold | | | | | | | | |
| 2023-11-14 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 20,110 | 99.9% | 35% | 622 | 0.0% | 31% |
| 2023-11-14 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 20,110 | 99.9% | 35% | 622 | 0.0% | 31% |
| 2023-11-14 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 22,726 | 99.9% | 35% | 522 | 0.1% | 31% |
| 2023-11-14 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 16,252 | 100.0% | 45% | 310 | 0.0% | 40% |
| 2023-11-14 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 539 | 100.0% | 82% | 190 | 0.0% | 47% |
| 2023-11-14 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 29,217 | 100.0% | 42% | 661 | 0.1% | 33% |
| 2023-11-14 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 24,927 | 100.0% | 44% | 646 | 0.0% | 34% |
| 2023-11-14 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 20,561 | 100.0% | 46% | 628 | 0.0% | 36% |
| 2023-11-14 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 5,846 | 100.0% | 66% | 290 | 0.1% | 45% |
| 2023-11-14 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 537 | 100.0% | 81% | 206 | 0.0% | 37% |
| 2023-11-14 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 20,617 | 100.0% | 32% | 948 | 0.1% | 28% |
| 2023-11-14 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 17,896 | 100.0% | 36% | 712 | 0.1% | 29% |
| 2023-11-14 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,068 | 100.0% | 47% | 399 | 0.1% | 32% |
| 2023-11-14 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 962 | 100.0% | 82% | 173 | 0.1% | 42% |
| 2023-11-14 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 232 | 100.0% | 85% | 190 | 0.0% | 44% |
| 2023-11-14 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 24,154 | 100.0% | 41% | 631 | 0.1% | 36% |
| 2023-11-14 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 24,154 | 100.0% | 41% | 631 | 0.1% | 36% |
| 2023-11-14 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 15,245 | 100.0% | 50% | 426 | 0.1% | 41% |
| 2023-11-14 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,742 | 100.0% | 79% | 166 | 0.0% | 48% |
| 2023-11-14 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 456 | 100.0% | 80% | 166 | 0.0% | 37% |
| 2023-11-14 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 31,930 | 100.0% | 35% | 718 | 0.1% | 30% |
| 2023-11-14 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 25,249 | 100.0% | 42% | 499 | 0.1% | 33% |
| 2023-11-14 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 12,026 | 100.0% | 55% | 385 | 0.2% | 38% |
| 2023-11-14 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,121 | 100.0% | 75% | 216 | 0.4% | 45% |
| 2023-11-14 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 317 | 100.0% | 87% | 152 | 0.9% | 41% |
| 2023-11-14 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 103,612 | 100.0% | 55% | 334 | 0.0% | 34% |
| 2023-11-14 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 99,697 | 100.0% | 56% | 304 | 0.0% | 35% |
| 2023-11-14 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 90,224 | 100.0% | 57% | 290 | 0.0% | 35% |
| 2023-11-14 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 46,662 | 100.0% | 61% | 213 | 0.0% | 38% |
| 2023-11-14 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 3,268 | 100.0% | 87% | 131 | 0.0% | 51% |
| 2023-11-14 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 50,482 | 100.0% | 58% | 387 | 0.0% | 35% |
| 2023-11-14 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 55,220 | 100.0% | 57% | 372 | 0.0% | 35% |
| 2023-11-14 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 61,202 | 100.0% | 56% | 345 | 0.0% | 35% |
| 2023-11-14 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 79,415 | 100.0% | 56% | 298 | 0.0% | 34% |
| 2023-11-14 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 84,492 | 100.0% | 61% | 229 | 0.0% | 36% |
| 2023-11-14 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 62,783 | 100.0% | 52% | 428 | 0.0% | 39% |
| 2023-11-14 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 54,707 | 100.0% | 53% | 380 | 0.0% | 40% |
| 2023-11-14 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 46,295 | 100.0% | 55% | 351 | 0.0% | 41% |
| 2023-11-14 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 20,710 | 100.0% | 65% | 244 | 0.0% | 46% |
| 2023-11-14 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 2,213 | 100.0% | 89% | 144 | 0.1% | 56% |
| 2023-11-14 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 20,665 | 100.0% | 44% | 542 | 0.0% | 35% |
| 2023-11-14 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 20,665 | 100.0% | 44% | 542 | 0.0% | 35% |
| 2023-11-14 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 12,325 | 100.0% | 56% | 356 | 0.1% | 39% |
| 2023-11-14 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,938 | 100.0% | 83% | 169 | 0.0% | 45% |
| 2023-11-14 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 1,048 | 100.0% | 85% | 192 | 0.0% | 44% |
| 2023-11-14 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.901 below threshold | | | | | | | | |
| 2023-11-15 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 25,463 | 99.9% | 37% | 519 | 0.2% | 37% |
| 2023-11-15 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 25,463 | 99.9% | 37% | 519 | 0.2% | 37% |
| 2023-11-15 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 18,628 | 99.9% | 41% | 424 | 0.3% | 39% |
| 2023-11-15 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,992 | 100.0% | 56% | 272 | 1.1% | 49% |
| 2023-11-15 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 120 | 100.0% | 85% | 139 | 10.0% | 60% |
| 2023-11-15 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 17,898 | 100.0% | 31% | 812 | 0.3% | 31% |
| 2023-11-15 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 15,046 | 100.0% | 33% | 650 | 0.4% | 32% |
| 2023-11-15 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 12,363 | 100.0% | 34% | 520 | 0.4% | 32% |
| 2023-11-15 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,165 | 100.0% | 59% | 222 | 0.9% | 40% |
| 2023-11-15 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 157 | 100.0% | 87% | 120 | 15.3% | 53% |
| 2023-11-15 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,942 | 100.0% | 35% | 1,037 | 0.6% | 28% |
| 2023-11-15 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 15,262 | 100.0% | 35% | 730 | 0.6% | 27% |
| 2023-11-15 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 14,569 | 100.0% | 37% | 486 | 0.7% | 28% |
| 2023-11-15 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,568 | 100.0% | 78% | 148 | 5.4% | 43% |
| 2023-11-15 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 182 | 100.0% | 82% | 222 | 48.4% | 38% |
| 2023-11-15 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,196 | 100.0% | 25% | 1,272 | 0.2% | 33% |
| 2023-11-15 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 14,196 | 100.0% | 25% | 1,272 | 0.2% | 33% |
| 2023-11-15 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,149 | 100.0% | 35% | 567 | 0.5% | 41% |
| 2023-11-15 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 678 | 100.0% | 74% | 160 | 4.0% | 46% |
| 2023-11-15 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 59 | 100.0% | 83% | 176 | 30.5% | 36% |
| 2023-11-15 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 20,924 | 100.0% | 29% | 1,042 | 0.4% | 29% |
| 2023-11-15 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 15,793 | 100.0% | 36% | 690 | 0.4% | 32% |
| 2023-11-15 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 9,587 | 100.0% | 40% | 446 | 0.6% | 32% |
| 2023-11-15 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 589 | 100.0% | 78% | 172 | 9.0% | 44% |
| 2023-11-15 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 36 | 100.0% | 67% | 138 | 41.7% | 42% |
| 2023-11-15 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 118,369 | 100.0% | 54% | 348 | 0.1% | 35% |
| 2023-11-15 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 108,400 | 100.0% | 56% | 308 | 0.1% | 36% |
| 2023-11-15 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 89,409 | 100.0% | 59% | 269 | 0.1% | 38% |
| 2023-11-15 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 35,022 | 100.0% | 64% | 208 | 0.2% | 41% |
| 2023-11-15 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 2,717 | 100.0% | 88% | 128 | 1.9% | 51% |
| 2023-11-15 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 34,985 | 100.0% | 53% | 470 | 0.2% | 34% |
| 2023-11-15 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 38,201 | 100.0% | 53% | 425 | 0.2% | 34% |
| 2023-11-15 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 41,389 | 100.0% | 52% | 395 | 0.1% | 34% |
| 2023-11-15 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 53,893 | 100.0% | 52% | 318 | 0.1% | 33% |
| 2023-11-15 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 59,579 | 100.0% | 59% | 242 | 0.0% | 37% |
| 2023-11-15 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 35,923 | 100.0% | 39% | 542 | 0.2% | 36% |
| 2023-11-15 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 32,806 | 100.0% | 41% | 487 | 0.2% | 36% |
| 2023-11-15 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 29,550 | 100.0% | 42% | 434 | 0.2% | 37% |
| 2023-11-15 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 15,625 | 100.0% | 49% | 314 | 0.2% | 42% |
| 2023-11-15 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 1,317 | 100.0% | 85% | 146 | 1.0% | 58% |
| 2023-11-15 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,608 | 100.0% | 29% | 1,149 | 0.6% | 35% |
| 2023-11-15 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,608 | 100.0% | 29% | 1,149 | 0.6% | 35% |
| 2023-11-15 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,470 | 100.0% | 32% | 626 | 0.9% | 36% |
| 2023-11-15 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 839 | 100.0% | 66% | 161 | 3.8% | 44% |
| 2023-11-15 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 108 | 100.0% | 81% | 187 | 24.1% | 45% |
| 2023-11-15 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.861 below threshold | | | | | | | | |
| 2023-11-16 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 18,725 | 100.0% | 32% | 798 | 0.0% | 30% |
| 2023-11-16 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 18,725 | 100.0% | 32% | 798 | 0.0% | 30% |
| 2023-11-16 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 23,565 | 100.0% | 31% | 600 | 0.1% | 29% |
| 2023-11-16 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 20,645 | 100.0% | 44% | 312 | 0.0% | 34% |
| 2023-11-16 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 1,373 | 100.0% | 81% | 133 | 0.3% | 45% |
| 2023-11-16 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 23,810 | 100.0% | 38% | 665 | 0.0% | 29% |
| 2023-11-16 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 22,640 | 100.0% | 40% | 566 | 0.0% | 30% |
| 2023-11-16 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 19,612 | 100.0% | 42% | 585 | 0.0% | 31% |
| 2023-11-16 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 9,983 | 100.0% | 48% | 392 | 0.1% | 35% |
| 2023-11-16 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 406 | 100.0% | 86% | 166 | 0.2% | 48% |
| 2023-11-16 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 21,206 | 100.0% | 31% | 968 | 0.0% | 27% |
| 2023-11-16 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 20,620 | 100.0% | 31% | 550 | 0.0% | 28% |
| 2023-11-16 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 12,168 | 100.0% | 42% | 317 | 0.0% | 33% |
| 2023-11-16 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 519 | 100.0% | 82% | 144 | 0.0% | 45% |
| 2023-11-16 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 31 | 100.0% | 77% | 416 | 0.0% | 35% |
| 2023-11-16 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 54,105 | 100.0% | 48% | 394 | 0.0% | 34% |
| 2023-11-16 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 54,105 | 100.0% | 48% | 394 | 0.0% | 34% |
| 2023-11-16 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 40,486 | 100.0% | 53% | 326 | 0.1% | 36% |
| 2023-11-16 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 12,488 | 100.0% | 70% | 190 | 0.1% | 43% |
| 2023-11-16 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 573 | 100.0% | 88% | 129 | 0.0% | 47% |
| 2023-11-16 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 20,249 | 100.0% | 37% | 652 | 0.1% | 29% |
| 2023-11-16 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 20,387 | 100.0% | 37% | 668 | 0.1% | 28% |
| 2023-11-16 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 18,904 | 100.0% | 38% | 643 | 0.1% | 28% |
| 2023-11-16 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,217 | 100.0% | 68% | 270 | 0.0% | 39% |
| 2023-11-16 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 121 | 100.0% | 82% | 171 | 0.0% | 40% |
| 2023-11-16 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 75,135 | 100.0% | 54% | 401 | 0.0% | 35% |
| 2023-11-16 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 74,612 | 100.0% | 53% | 368 | 0.0% | 35% |
| 2023-11-16 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 74,770 | 100.0% | 52% | 321 | 0.0% | 34% |
| 2023-11-16 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 48,199 | 100.0% | 59% | 214 | 0.0% | 37% |
| 2023-11-16 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 3,457 | 100.0% | 85% | 123 | 0.0% | 52% |
| 2023-11-16 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 35,644 | 100.0% | 55% | 520 | 0.1% | 35% |
| 2023-11-16 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 37,242 | 100.0% | 54% | 488 | 0.1% | 34% |
| 2023-11-16 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 39,524 | 100.0% | 52% | 478 | 0.1% | 33% |
| 2023-11-16 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 49,295 | 100.0% | 51% | 368 | 0.0% | 33% |
| 2023-11-16 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 33,699 | 100.0% | 58% | 276 | 0.1% | 37% |
| 2023-11-16 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 40,853 | 100.0% | 44% | 420 | 0.0% | 38% |
| 2023-11-16 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 29,603 | 100.0% | 50% | 365 | 0.0% | 40% |
| 2023-11-16 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 20,203 | 100.0% | 57% | 306 | 0.0% | 43% |
| 2023-11-16 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,899 | 100.0% | 80% | 163 | 0.1% | 51% |
| 2023-11-16 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 532 | 100.0% | 90% | 125 | 0.0% | 52% |
| 2023-11-16 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,642 | 100.0% | 35% | 696 | 0.1% | 32% |
| 2023-11-16 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 14,642 | 100.0% | 35% | 696 | 0.1% | 32% |
| 2023-11-16 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,775 | 100.0% | 44% | 517 | 0.1% | 37% |
| 2023-11-16 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,165 | 100.0% | 80% | 142 | 0.2% | 46% |
| 2023-11-16 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 301 | 100.0% | 84% | 162 | 0.0% | 42% |
| 2023-11-17 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 17,645 | 99.9% | 29% | 668 | 0.2% | 32% |
| 2023-11-17 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 17,645 | 99.9% | 29% | 668 | 0.2% | 32% |
| 2023-11-17 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 19,043 | 100.0% | 30% | 559 | 0.1% | 32% |
| 2023-11-17 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 16,466 | 100.0% | 42% | 270 | 0.2% | 34% |
| 2023-11-17 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 382 | 100.0% | 86% | 174 | 1.6% | 53% |
| 2023-11-17 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 24,778 | 100.0% | 33% | 808 | 0.2% | 29% |
| 2023-11-17 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 24,928 | 100.0% | 34% | 652 | 0.2% | 30% |
| 2023-11-17 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 21,420 | 100.0% | 39% | 506 | 0.2% | 32% |
| 2023-11-17 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,782 | 100.0% | 74% | 228 | 0.7% | 51% |
| 2023-11-17 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 160 | 100.0% | 89% | 130 | 5.6% | 51% |
| 2023-11-17 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,074 | 100.0% | 37% | 816 | 1.4% | 30% |
| 2023-11-17 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,237 | 100.0% | 35% | 553 | 1.1% | 27% |
| 2023-11-17 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 9,384 | 100.0% | 34% | 518 | 0.9% | 28% |
| 2023-11-17 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,226 | 100.0% | 44% | 588 | 3.1% | 34% |
| 2023-11-17 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 82 | 100.0% | 78% | 266 | 31.7% | 39% |
| 2023-11-17 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 50,424 | 100.0% | 42% | 492 | 0.1% | 30% |
| 2023-11-17 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 50,424 | 100.0% | 42% | 492 | 0.1% | 30% |
| 2023-11-17 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 42,558 | 100.0% | 46% | 416 | 0.1% | 32% |
| 2023-11-17 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 14,003 | 100.0% | 63% | 222 | 0.1% | 40% |
| 2023-11-17 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 1,057 | 100.0% | 88% | 118 | 0.9% | 49% |
| 2023-11-17 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,609 | 100.0% | 29% | 1,312 | 0.2% | 29% |
| 2023-11-17 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,446 | 100.0% | 32% | 828 | 0.3% | 29% |
| 2023-11-17 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,198 | 100.0% | 28% | 648 | 0.2% | 27% |
| 2023-11-17 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,584 | 100.0% | 62% | 202 | 0.9% | 41% |
| 2023-11-17 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 63 | 100.0% | 84% | 296 | 1.6% | 22% |
| 2023-11-17 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 30,937 | 100.0% | 51% | 539 | 0.4% | 36% |
| 2023-11-17 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 37,749 | 100.0% | 46% | 408 | 0.4% | 33% |
| 2023-11-17 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 48,950 | 100.0% | 44% | 326 | 0.3% | 32% |
| 2023-11-17 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 58,584 | 100.0% | 51% | 248 | 0.1% | 36% |
| 2023-11-17 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 7,422 | 100.0% | 75% | 134 | 0.4% | 48% |
| 2023-11-17 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 56,178 | 100.0% | 56% | 418 | 0.1% | 35% |
| 2023-11-17 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 62,211 | 100.0% | 55% | 366 | 0.1% | 35% |
| 2023-11-17 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 69,590 | 100.0% | 56% | 330 | 0.0% | 35% |
| 2023-11-17 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 81,520 | 100.0% | 58% | 264 | 0.0% | 35% |
| 2023-11-17 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 48,999 | 100.0% | 67% | 207 | 0.0% | 40% |
| 2023-11-17 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 29,681 | 100.0% | 32% | 672 | 0.1% | 35% |
| 2023-11-17 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 28,348 | 100.0% | 33% | 628 | 0.1% | 35% |
| 2023-11-17 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 26,405 | 100.0% | 34% | 553 | 0.1% | 36% |
| 2023-11-17 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 17,465 | 100.0% | 43% | 326 | 0.1% | 37% |
| 2023-11-17 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 2,666 | 100.0% | 74% | 157 | 0.4% | 47% |
| 2023-11-17 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,499 | 100.0% | 29% | 526 | 0.3% | 30% |
| 2023-11-17 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 13,499 | 100.0% | 29% | 526 | 0.3% | 30% |
| 2023-11-17 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,471 | 100.0% | 45% | 321 | 0.6% | 37% |
| 2023-11-17 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 833 | 100.0% | 78% | 138 | 2.5% | 49% |
| 2023-11-17 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 45 | 100.0% | 84% | 265 | 17.8% | 47% |
| 2023-11-17 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.882 below threshold | | | | | | | | |
| 2023-11-18 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 15,820 | 99.6% | 33% | 879 | 0.0% | 32% |
| 2023-11-18 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 15,820 | 99.6% | 33% | 879 | 0.0% | 32% |
| 2023-11-18 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 12,906 | 99.7% | 36% | 766 | 0.0% | 35% |
| 2023-11-18 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,501 | 100.0% | 58% | 316 | 0.0% | 52% |
| 2023-11-18 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 92 | 100.0% | 98% | 170 | 0.0% | 72% |
| 2023-11-18 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,862 | 100.0% | 31% | 1,132 | 0.0% | 30% |
| 2023-11-18 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,833 | 100.0% | 32% | 963 | 0.0% | 32% |
| 2023-11-18 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,736 | 100.0% | 36% | 818 | 0.0% | 33% |
| 2023-11-18 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,685 | 100.0% | 64% | 300 | 0.0% | 50% |
| 2023-11-18 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 64 | 100.0% | 94% | 123 | 0.0% | 66% |
| 2023-11-18 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,301 | 99.9% | 29% | 2,296 | 0.0% | 25% |
| 2023-11-18 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,097 | 100.0% | 19% | 1,662 | 0.0% | 23% |
| 2023-11-18 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,078 | 100.0% | 24% | 1,458 | 0.0% | 26% |
| 2023-11-18 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,042 | 100.0% | 30% | 1,309 | 0.0% | 31% |
| 2023-11-18 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 2 | 100.0% | 50% | 164 | 0.0% | 0% |
| 2023-11-18 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 25,521 | 100.0% | 40% | 800 | 0.0% | 29% |
| 2023-11-18 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 25,521 | 100.0% | 40% | 800 | 0.0% | 29% |
| 2023-11-18 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 25,205 | 100.0% | 40% | 640 | 0.0% | 29% |
| 2023-11-18 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 11,928 | 100.0% | 57% | 299 | 0.0% | 41% |
| 2023-11-18 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 1,362 | 100.0% | 86% | 133 | 0.0% | 48% |
| 2023-11-18 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,756 | 100.0% | 25% | 2,074 | 0.0% | 29% |
| 2023-11-18 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,237 | 100.0% | 26% | 1,620 | 0.0% | 29% |
| 2023-11-18 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,672 | 100.0% | 31% | 763 | 0.0% | 31% |
| 2023-11-18 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 76 | 100.0% | 91% | 114 | 0.0% | 61% |
| 2023-11-18 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 0% |
| 2023-11-18 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 36,575 | 100.0% | 41% | 668 | 0.0% | 33% |
| 2023-11-18 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 39,743 | 100.0% | 38% | 503 | 0.0% | 31% |
| 2023-11-18 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 42,988 | 100.0% | 38% | 383 | 0.0% | 31% |
| 2023-11-18 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 17,750 | 100.0% | 59% | 200 | 0.0% | 43% |
| 2023-11-18 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 517 | 100.0% | 89% | 114 | 0.0% | 56% |
| 2023-11-18 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 25,820 | 100.0% | 53% | 524 | 0.0% | 35% |
| 2023-11-18 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 31,989 | 100.0% | 52% | 434 | 0.0% | 34% |
| 2023-11-18 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 41,075 | 100.0% | 51% | 368 | 0.0% | 34% |
| 2023-11-18 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 66,051 | 100.0% | 54% | 293 | 0.0% | 34% |
| 2023-11-18 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 57,389 | 100.0% | 62% | 216 | 0.0% | 38% |
| 2023-11-18 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 28,347 | 100.0% | 44% | 552 | 0.0% | 43% |
| 2023-11-18 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 23,300 | 100.0% | 46% | 536 | 0.0% | 43% |
| 2023-11-18 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 16,078 | 100.0% | 53% | 449 | 0.0% | 48% |
| 2023-11-18 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,117 | 100.0% | 67% | 342 | 0.0% | 54% |
| 2023-11-18 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 474 | 100.0% | 91% | 120 | 0.0% | 58% |
| 2023-11-18 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,984 | 100.0% | 47% | 599 | 0.0% | 46% |
| 2023-11-18 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,984 | 100.0% | 47% | 599 | 0.0% | 46% |
| 2023-11-18 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 912 | 100.0% | 57% | 322 | 0.0% | 44% |
| 2023-11-18 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 272 | 100.0% | 60% | 193 | 0.0% | 41% |
| 2023-11-18 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 3 | 100.0% | 33% | 111 | 0.0% | 100% |
| 2023-11-18 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.775 below threshold | | | | | | | | |
| 2023-11-19 | aave_perp_binance_bybit | ok | 0.999 | gross>0bps | 11,501 | 99.5% | 35% | 1,027 | 0.0% | 37% |
| 2023-11-19 | aave_perp_binance_bybit | ok | 0.999 | gross>1bps | 11,501 | 99.5% | 35% | 1,027 | 0.0% | 37% |
| 2023-11-19 | aave_perp_binance_bybit | ok | 0.999 | gross>2bps | 6,843 | 99.4% | 38% | 834 | 0.0% | 42% |
| 2023-11-19 | aave_perp_binance_bybit | ok | 0.999 | gross>5bps | 1,790 | 99.7% | 40% | 357 | 0.0% | 42% |
| 2023-11-19 | aave_perp_binance_bybit | ok | 0.999 | retail_taker | 14 | 100.0% | 93% | 199 | 0.0% | 79% |
| 2023-11-19 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,313 | 99.8% | 18% | 1,882 | 0.0% | 22% |
| 2023-11-19 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,402 | 99.9% | 21% | 1,249 | 0.0% | 26% |
| 2023-11-19 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,195 | 100.0% | 26% | 836 | 0.0% | 30% |
| 2023-11-19 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,030 | 100.0% | 61% | 600 | 0.0% | 49% |
| 2023-11-19 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 97 | 100.0% | 91% | 127 | 0.0% | 65% |
| 2023-11-19 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,995 | 100.0% | 29% | 1,274 | 0.0% | 28% |
| 2023-11-19 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,596 | 100.0% | 35% | 1,040 | 0.0% | 31% |
| 2023-11-19 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,072 | 100.0% | 30% | 1,046 | 0.0% | 29% |
| 2023-11-19 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 761 | 100.0% | 32% | 1,832 | 0.1% | 36% |
| 2023-11-19 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 6 | 100.0% | 50% | 208 | 0.0% | 50% |
| 2023-11-19 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 9,075 | 100.0% | 31% | 1,280 | 0.0% | 31% |
| 2023-11-19 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,075 | 100.0% | 31% | 1,280 | 0.0% | 31% |
| 2023-11-19 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,683 | 100.0% | 34% | 926 | 0.1% | 31% |
| 2023-11-19 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,440 | 100.0% | 40% | 828 | 0.0% | 36% |
| 2023-11-19 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 244 | 100.0% | 77% | 129 | 0.0% | 50% |
| 2023-11-19 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,060 | 100.0% | 28% | 2,834 | 0.1% | 30% |
| 2023-11-19 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,023 | 100.0% | 25% | 1,511 | 0.0% | 28% |
| 2023-11-19 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,820 | 100.0% | 30% | 691 | 0.0% | 29% |
| 2023-11-19 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 200 | 100.0% | 86% | 133 | 0.0% | 50% |
| 2023-11-19 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 21 | 100.0% | 81% | 231 | 0.0% | 48% |
| 2023-11-19 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 17,971 | 100.0% | 40% | 1,130 | 0.0% | 33% |
| 2023-11-19 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 23,592 | 100.0% | 31% | 668 | 0.0% | 29% |
| 2023-11-19 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 31,672 | 100.0% | 32% | 457 | 0.0% | 29% |
| 2023-11-19 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 23,199 | 100.0% | 49% | 264 | 0.0% | 37% |
| 2023-11-19 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 632 | 100.0% | 87% | 120 | 0.2% | 57% |
| 2023-11-19 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 20,719 | 100.0% | 49% | 590 | 0.0% | 35% |
| 2023-11-19 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 25,645 | 100.0% | 47% | 486 | 0.0% | 33% |
| 2023-11-19 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 32,426 | 100.0% | 48% | 414 | 0.0% | 33% |
| 2023-11-19 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 46,824 | 100.0% | 50% | 318 | 0.0% | 33% |
| 2023-11-19 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 33,126 | 100.0% | 59% | 246 | 0.0% | 38% |
| 2023-11-19 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 77,648 | 100.0% | 48% | 365 | 0.0% | 38% |
| 2023-11-19 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 65,749 | 100.0% | 51% | 340 | 0.0% | 39% |
| 2023-11-19 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 52,564 | 100.0% | 55% | 314 | 0.0% | 40% |
| 2023-11-19 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 18,065 | 100.0% | 69% | 259 | 0.0% | 46% |
| 2023-11-19 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 2,764 | 100.0% | 84% | 144 | 0.3% | 53% |
| 2023-11-19 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,774 | 100.0% | 23% | 2,094 | 0.1% | 29% |
| 2023-11-19 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,774 | 100.0% | 23% | 2,094 | 0.1% | 29% |
| 2023-11-19 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,633 | 100.0% | 21% | 1,620 | 0.0% | 25% |
| 2023-11-19 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,905 | 100.0% | 49% | 400 | 0.0% | 41% |
| 2023-11-19 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 92 | 100.0% | 95% | 119 | 0.0% | 59% |
| 2023-11-19 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.918 below threshold | | | | | | | | |
| 2023-11-20 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 17,832 | 99.9% | 32% | 652 | 0.0% | 34% |
| 2023-11-20 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 17,832 | 99.9% | 32% | 652 | 0.0% | 34% |
| 2023-11-20 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 16,786 | 99.9% | 32% | 565 | 0.0% | 35% |
| 2023-11-20 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 5,064 | 100.0% | 54% | 224 | 0.0% | 47% |
| 2023-11-20 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 109 | 100.0% | 94% | 120 | 0.0% | 48% |
| 2023-11-20 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 20,877 | 100.0% | 35% | 689 | 0.5% | 33% |
| 2023-11-20 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 17,077 | 100.0% | 38% | 611 | 0.5% | 34% |
| 2023-11-20 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 13,641 | 100.0% | 40% | 527 | 0.7% | 35% |
| 2023-11-20 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 5,906 | 100.0% | 43% | 387 | 1.3% | 37% |
| 2023-11-20 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 129 | 100.0% | 86% | 200 | 38.0% | 44% |
| 2023-11-20 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,065 | 100.0% | 33% | 1,524 | 0.9% | 27% |
| 2023-11-20 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,864 | 100.0% | 29% | 818 | 0.7% | 25% |
| 2023-11-20 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 9,773 | 100.0% | 32% | 543 | 0.7% | 27% |
| 2023-11-20 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,487 | 100.0% | 54% | 312 | 5.3% | 36% |
| 2023-11-20 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 121 | 100.0% | 78% | 165 | 55.4% | 38% |
| 2023-11-20 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 18,712 | 100.0% | 35% | 700 | 0.0% | 35% |
| 2023-11-20 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 18,712 | 100.0% | 35% | 700 | 0.0% | 35% |
| 2023-11-20 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,644 | 100.0% | 42% | 562 | 0.0% | 37% |
| 2023-11-20 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,624 | 100.0% | 66% | 187 | 0.1% | 42% |
| 2023-11-20 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 370 | 100.0% | 88% | 172 | 0.0% | 46% |
| 2023-11-20 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,082 | 100.0% | 33% | 887 | 0.0% | 29% |
| 2023-11-20 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 13,067 | 100.0% | 35% | 570 | 0.0% | 30% |
| 2023-11-20 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 12,186 | 100.0% | 32% | 576 | 0.0% | 28% |
| 2023-11-20 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,203 | 99.9% | 73% | 137 | 0.2% | 47% |
| 2023-11-20 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 97 | 100.0% | 88% | 252 | 0.0% | 40% |
| 2023-11-20 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 56,302 | 100.0% | 44% | 526 | 0.5% | 36% |
| 2023-11-20 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 55,441 | 100.0% | 44% | 398 | 0.4% | 35% |
| 2023-11-20 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 51,488 | 100.0% | 45% | 310 | 0.5% | 36% |
| 2023-11-20 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 16,902 | 100.0% | 64% | 198 | 1.2% | 44% |
| 2023-11-20 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 608 | 100.0% | 88% | 177 | 33.2% | 54% |
| 2023-11-20 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 19,739 | 100.0% | 54% | 510 | 0.0% | 34% |
| 2023-11-20 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 22,530 | 100.0% | 51% | 503 | 0.0% | 33% |
| 2023-11-20 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 27,817 | 100.0% | 51% | 450 | 0.0% | 33% |
| 2023-11-20 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 42,513 | 100.0% | 51% | 372 | 0.0% | 34% |
| 2023-11-20 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 37,237 | 100.0% | 59% | 259 | 0.0% | 38% |
| 2023-11-20 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 74,503 | 100.0% | 51% | 350 | 0.0% | 40% |
| 2023-11-20 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 60,769 | 100.0% | 55% | 308 | 0.0% | 41% |
| 2023-11-20 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 46,431 | 100.0% | 60% | 273 | 0.1% | 43% |
| 2023-11-20 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 15,193 | 100.0% | 77% | 168 | 0.2% | 47% |
| 2023-11-20 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 3,221 | 100.0% | 90% | 118 | 0.5% | 50% |
| 2023-11-20 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,737 | 100.0% | 33% | 786 | 0.0% | 36% |
| 2023-11-20 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,737 | 100.0% | 33% | 786 | 0.0% | 36% |
| 2023-11-20 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,484 | 100.0% | 45% | 560 | 0.0% | 43% |
| 2023-11-20 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 338 | 100.0% | 86% | 246 | 0.0% | 52% |
| 2023-11-20 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 57 | 100.0% | 93% | 246 | 0.0% | 47% |
| 2023-11-20 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.738 below threshold | | | | | | | | |
| 2023-11-21 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 32,692 | 99.9% | 44% | 465 | 0.0% | 35% |
| 2023-11-21 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 32,692 | 99.9% | 44% | 465 | 0.0% | 35% |
| 2023-11-21 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 21,342 | 99.9% | 48% | 448 | 0.0% | 37% |
| 2023-11-21 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,393 | 100.0% | 66% | 303 | 0.0% | 51% |
| 2023-11-21 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 96 | 100.0% | 98% | 120 | 0.0% | 50% |
| 2023-11-21 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 39,988 | 100.0% | 49% | 502 | 0.0% | 36% |
| 2023-11-21 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 36,137 | 100.0% | 50% | 462 | 0.0% | 37% |
| 2023-11-21 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 25,984 | 100.0% | 56% | 378 | 0.0% | 41% |
| 2023-11-21 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,439 | 100.0% | 86% | 136 | 0.1% | 55% |
| 2023-11-21 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 200 | 100.0% | 94% | 122 | 0.0% | 56% |
| 2023-11-21 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 19,706 | 100.0% | 31% | 844 | 0.0% | 28% |
| 2023-11-21 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 15,937 | 100.0% | 36% | 548 | 0.0% | 30% |
| 2023-11-21 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,719 | 100.0% | 40% | 365 | 0.0% | 30% |
| 2023-11-21 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,323 | 100.0% | 61% | 225 | 0.1% | 34% |
| 2023-11-21 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 170 | 100.0% | 91% | 182 | 0.0% | 51% |
| 2023-11-21 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 30,008 | 100.0% | 41% | 598 | 0.0% | 34% |
| 2023-11-21 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 30,008 | 100.0% | 41% | 598 | 0.0% | 34% |
| 2023-11-21 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 22,203 | 100.0% | 47% | 414 | 0.0% | 38% |
| 2023-11-21 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 5,111 | 100.0% | 78% | 160 | 0.0% | 50% |
| 2023-11-21 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 285 | 100.0% | 95% | 124 | 0.0% | 54% |
| 2023-11-21 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 31,289 | 100.0% | 36% | 661 | 0.0% | 30% |
| 2023-11-21 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 26,320 | 100.0% | 40% | 568 | 0.0% | 32% |
| 2023-11-21 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 15,313 | 100.0% | 48% | 390 | 0.0% | 36% |
| 2023-11-21 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,571 | 100.0% | 86% | 125 | 0.0% | 47% |
| 2023-11-21 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 135 | 100.0% | 92% | 164 | 0.0% | 41% |
| 2023-11-21 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 125,200 | 100.0% | 50% | 368 | 0.0% | 35% |
| 2023-11-21 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 106,958 | 100.0% | 55% | 300 | 0.0% | 38% |
| 2023-11-21 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 75,463 | 100.0% | 61% | 240 | 0.0% | 40% |
| 2023-11-21 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 10,812 | 100.0% | 83% | 130 | 0.0% | 52% |
| 2023-11-21 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 605 | 100.0% | 96% | 114 | 0.0% | 54% |
| 2023-11-21 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 58,838 | 100.0% | 56% | 416 | 0.0% | 35% |
| 2023-11-21 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 62,891 | 100.0% | 55% | 371 | 0.0% | 35% |
| 2023-11-21 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 68,868 | 100.0% | 56% | 342 | 0.0% | 35% |
| 2023-11-21 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 73,060 | 100.0% | 59% | 278 | 0.0% | 36% |
| 2023-11-21 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 30,359 | 100.0% | 67% | 217 | 0.0% | 41% |
| 2023-11-21 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 70,175 | 100.0% | 53% | 336 | 0.0% | 41% |
| 2023-11-21 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 51,761 | 100.0% | 58% | 301 | 0.0% | 43% |
| 2023-11-21 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 36,526 | 100.0% | 64% | 267 | 0.0% | 46% |
| 2023-11-21 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 7,986 | 100.0% | 80% | 184 | 0.0% | 53% |
| 2023-11-21 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 907 | 100.0% | 91% | 130 | 0.0% | 57% |
| 2023-11-21 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,485 | 100.0% | 44% | 523 | 0.0% | 40% |
| 2023-11-21 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 14,485 | 100.0% | 44% | 523 | 0.0% | 40% |
| 2023-11-21 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,320 | 100.0% | 60% | 290 | 0.0% | 45% |
| 2023-11-21 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,950 | 100.0% | 78% | 172 | 0.0% | 49% |
| 2023-11-21 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 106 | 100.0% | 96% | 125 | 0.0% | 44% |
| 2023-11-21 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.811 below threshold | | | | | | | | |
| 2023-11-22 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 29,133 | 100.0% | 41% | 644 | 0.0% | 37% |
| 2023-11-22 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 29,133 | 100.0% | 41% | 644 | 0.0% | 37% |
| 2023-11-22 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 18,457 | 100.0% | 47% | 479 | 0.0% | 40% |
| 2023-11-22 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,136 | 100.0% | 80% | 166 | 0.0% | 52% |
| 2023-11-22 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 188 | 100.0% | 93% | 141 | 0.0% | 57% |
| 2023-11-22 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 17,033 | 100.0% | 29% | 940 | 0.3% | 33% |
| 2023-11-22 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 16,357 | 100.0% | 31% | 876 | 0.3% | 34% |
| 2023-11-22 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,879 | 100.0% | 36% | 739 | 0.4% | 36% |
| 2023-11-22 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,090 | 100.0% | 73% | 212 | 2.6% | 54% |
| 2023-11-22 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 94 | 100.0% | 91% | 160 | 21.3% | 57% |
| 2023-11-22 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,951 | 100.0% | 37% | 1,276 | 1.7% | 30% |
| 2023-11-22 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,307 | 100.0% | 26% | 662 | 0.9% | 25% |
| 2023-11-22 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,996 | 100.0% | 28% | 497 | 0.8% | 27% |
| 2023-11-22 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,840 | 100.0% | 31% | 1,236 | 2.1% | 31% |
| 2023-11-22 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 38 | 100.0% | 63% | 511 | 63.2% | 26% |
| 2023-11-22 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 9,734 | 100.0% | 28% | 1,069 | 0.0% | 37% |
| 2023-11-22 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,734 | 100.0% | 28% | 1,069 | 0.0% | 37% |
| 2023-11-22 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,497 | 100.0% | 33% | 946 | 0.0% | 39% |
| 2023-11-22 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,207 | 100.0% | 47% | 320 | 0.1% | 45% |
| 2023-11-22 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 40 | 100.0% | 85% | 158 | 0.0% | 48% |
| 2023-11-22 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 16,576 | 100.0% | 32% | 995 | 0.0% | 30% |
| 2023-11-22 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 16,646 | 100.0% | 31% | 972 | 0.0% | 29% |
| 2023-11-22 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 15,255 | 100.0% | 33% | 1,423 | 0.0% | 32% |
| 2023-11-22 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 465 | 100.0% | 87% | 116 | 0.0% | 49% |
| 2023-11-22 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 61 | 100.0% | 95% | 170 | 0.0% | 48% |
| 2023-11-22 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 68,216 | 100.0% | 40% | 522 | 0.1% | 34% |
| 2023-11-22 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 61,582 | 100.0% | 43% | 422 | 0.1% | 35% |
| 2023-11-22 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 47,428 | 100.0% | 47% | 314 | 0.2% | 37% |
| 2023-11-22 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 5,056 | 100.0% | 80% | 126 | 1.0% | 53% |
| 2023-11-22 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 161 | 100.0% | 88% | 155 | 32.9% | 54% |
| 2023-11-22 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 19,157 | 100.0% | 49% | 638 | 0.0% | 33% |
| 2023-11-22 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 24,264 | 100.0% | 45% | 540 | 0.0% | 30% |
| 2023-11-22 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 32,637 | 100.0% | 44% | 460 | 0.0% | 29% |
| 2023-11-22 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 57,021 | 100.0% | 46% | 324 | 0.0% | 31% |
| 2023-11-22 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 28,482 | 100.0% | 60% | 219 | 0.0% | 39% |
| 2023-11-22 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 50,023 | 100.0% | 42% | 479 | 0.0% | 38% |
| 2023-11-22 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 41,236 | 100.0% | 46% | 418 | 0.0% | 40% |
| 2023-11-22 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 30,607 | 100.0% | 51% | 357 | 0.0% | 42% |
| 2023-11-22 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 8,795 | 100.0% | 70% | 210 | 0.1% | 50% |
| 2023-11-22 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 993 | 100.0% | 91% | 118 | 0.1% | 57% |
| 2023-11-22 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,874 | 100.0% | 26% | 1,111 | 0.0% | 34% |
| 2023-11-22 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,874 | 100.0% | 26% | 1,111 | 0.0% | 34% |
| 2023-11-22 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,731 | 100.0% | 38% | 540 | 0.0% | 41% |
| 2023-11-22 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 393 | 100.0% | 79% | 121 | 0.0% | 53% |
| 2023-11-22 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 30 | 100.0% | 97% | 117 | 0.0% | 50% |
| 2023-11-22 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.903 below threshold | | | | | | | | |
| 2023-11-23 | aave_perp_binance_bybit | ok | 0.999 | gross>0bps | 18,775 | 99.9% | 38% | 784 | 0.0% | 39% |
| 2023-11-23 | aave_perp_binance_bybit | ok | 0.999 | gross>1bps | 18,796 | 99.9% | 38% | 784 | 0.0% | 39% |
| 2023-11-23 | aave_perp_binance_bybit | ok | 0.999 | gross>2bps | 11,987 | 99.9% | 45% | 600 | 0.0% | 43% |
| 2023-11-23 | aave_perp_binance_bybit | ok | 0.999 | gross>5bps | 1,987 | 100.0% | 69% | 162 | 0.0% | 49% |
| 2023-11-23 | aave_perp_binance_bybit | ok | 0.999 | retail_taker | 188 | 100.0% | 91% | 128 | 0.0% | 53% |
| 2023-11-23 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,438 | 99.9% | 28% | 1,426 | 0.0% | 34% |
| 2023-11-23 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,237 | 100.0% | 30% | 1,100 | 0.0% | 37% |
| 2023-11-23 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,347 | 100.0% | 35% | 768 | 0.0% | 38% |
| 2023-11-23 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 534 | 100.0% | 74% | 214 | 0.0% | 56% |
| 2023-11-23 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 36 | 100.0% | 92% | 117 | 0.0% | 67% |
| 2023-11-23 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,264 | 100.0% | 26% | 1,568 | 0.0% | 27% |
| 2023-11-23 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,973 | 100.0% | 25% | 1,784 | 0.0% | 26% |
| 2023-11-23 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,921 | 100.0% | 25% | 1,216 | 0.1% | 27% |
| 2023-11-23 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 816 | 100.0% | 32% | 554 | 0.0% | 39% |
| 2023-11-23 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 6 | 100.0% | 67% | 142 | 0.0% | 33% |
| 2023-11-23 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,129 | 100.0% | 21% | 2,252 | 0.0% | 39% |
| 2023-11-23 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,129 | 100.0% | 21% | 2,252 | 0.0% | 39% |
| 2023-11-23 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,655 | 100.0% | 22% | 2,526 | 0.0% | 41% |
| 2023-11-23 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,058 | 100.0% | 39% | 476 | 0.0% | 50% |
| 2023-11-23 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 20 | 100.0% | 95% | 134 | 0.0% | 45% |
| 2023-11-23 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 16,153 | 100.0% | 25% | 1,171 | 0.0% | 30% |
| 2023-11-23 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,902 | 100.0% | 34% | 890 | 0.0% | 34% |
| 2023-11-23 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,618 | 100.0% | 42% | 690 | 0.0% | 36% |
| 2023-11-23 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 563 | 100.0% | 64% | 183 | 0.0% | 44% |
| 2023-11-23 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 26 | 100.0% | 92% | 123 | 0.0% | 38% |
| 2023-11-23 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 40,584 | 100.0% | 39% | 593 | 0.0% | 34% |
| 2023-11-23 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 39,583 | 100.0% | 40% | 434 | 0.0% | 34% |
| 2023-11-23 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 34,797 | 100.0% | 42% | 332 | 0.0% | 36% |
| 2023-11-23 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 7,292 | 100.0% | 67% | 154 | 0.0% | 49% |
| 2023-11-23 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 199 | 100.0% | 92% | 112 | 0.0% | 61% |
| 2023-11-23 | tia_perp_binance_bybit | excluded: bybit_ob/bybit/TIA-USDT/perp coverage 1.000 below threshold | | | | | | | | |
| 2023-11-23 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 21,526 | 100.0% | 37% | 660 | 0.0% | 42% |
| 2023-11-23 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 15,280 | 100.0% | 42% | 590 | 0.0% | 45% |
| 2023-11-23 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 9,814 | 100.0% | 48% | 504 | 0.0% | 46% |
| 2023-11-23 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,388 | 100.0% | 78% | 214 | 0.0% | 58% |
| 2023-11-23 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 221 | 100.0% | 85% | 120 | 0.0% | 66% |
| 2023-11-23 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,867 | 100.0% | 25% | 1,327 | 0.0% | 30% |
| 2023-11-23 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,867 | 100.0% | 25% | 1,327 | 0.0% | 30% |
| 2023-11-23 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,655 | 100.0% | 29% | 838 | 0.0% | 34% |
| 2023-11-23 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 418 | 100.0% | 74% | 112 | 0.0% | 57% |
| 2023-11-23 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 25 | 100.0% | 100% | none resolved | 0.0% | 44% |
| 2023-11-23 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.944 below threshold | | | | | | | | |
| 2023-11-24 | aave_perp_binance_bybit | ok | 0.999 | gross>0bps | 14,737 | 99.6% | 41% | 801 | 0.0% | 40% |
| 2023-11-24 | aave_perp_binance_bybit | ok | 0.999 | gross>1bps | 14,737 | 99.6% | 41% | 801 | 0.0% | 40% |
| 2023-11-24 | aave_perp_binance_bybit | ok | 0.999 | gross>2bps | 12,024 | 99.5% | 39% | 723 | 0.0% | 39% |
| 2023-11-24 | aave_perp_binance_bybit | ok | 0.999 | gross>5bps | 5,961 | 99.9% | 44% | 322 | 0.0% | 40% |
| 2023-11-24 | aave_perp_binance_bybit | ok | 0.999 | retail_taker | 123 | 100.0% | 80% | 136 | 0.0% | 63% |
| 2023-11-24 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,862 | 100.0% | 32% | 1,378 | 0.6% | 36% |
| 2023-11-24 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,038 | 100.0% | 28% | 1,329 | 0.4% | 32% |
| 2023-11-24 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 9,115 | 100.0% | 26% | 1,014 | 0.4% | 32% |
| 2023-11-24 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,937 | 100.0% | 45% | 340 | 0.4% | 40% |
| 2023-11-24 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 85 | 100.0% | 95% | 163 | 2.4% | 46% |
| 2023-11-24 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,773 | 100.0% | 34% | 1,747 | 1.3% | 30% |
| 2023-11-24 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,353 | 100.0% | 33% | 1,006 | 1.3% | 28% |
| 2023-11-24 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,067 | 100.0% | 32% | 616 | 0.9% | 26% |
| 2023-11-24 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,779 | 100.0% | 47% | 421 | 1.4% | 33% |
| 2023-11-24 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 106 | 100.0% | 87% | 246 | 39.6% | 40% |
| 2023-11-24 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,872 | 100.0% | 21% | 1,970 | 0.0% | 34% |
| 2023-11-24 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,872 | 100.0% | 21% | 1,970 | 0.0% | 34% |
| 2023-11-24 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,416 | 100.0% | 22% | 1,322 | 0.0% | 33% |
| 2023-11-24 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,024 | 100.0% | 35% | 655 | 0.0% | 45% |
| 2023-11-24 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 18 | 100.0% | 94% | 198 | 0.0% | 72% |
| 2023-11-24 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 19,594 | 100.0% | 32% | 820 | 0.0% | 29% |
| 2023-11-24 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 15,154 | 100.0% | 41% | 518 | 0.0% | 33% |
| 2023-11-24 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,935 | 100.0% | 42% | 596 | 0.0% | 33% |
| 2023-11-24 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 537 | 100.0% | 85% | 162 | 0.0% | 49% |
| 2023-11-24 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 66 | 100.0% | 85% | 258 | 0.0% | 36% |
| 2023-11-24 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 42,132 | 100.0% | 39% | 549 | 0.1% | 33% |
| 2023-11-24 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 38,566 | 100.0% | 41% | 492 | 0.1% | 34% |
| 2023-11-24 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 30,279 | 100.0% | 44% | 416 | 0.2% | 36% |
| 2023-11-24 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,182 | 100.0% | 67% | 192 | 1.6% | 49% |
| 2023-11-24 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 88 | 100.0% | 92% | 119 | 2.3% | 61% |
| 2023-11-24 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,590 | 100.0% | 38% | 1,129 | 0.0% | 28% |
| 2023-11-24 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,271 | 100.0% | 33% | 784 | 0.0% | 24% |
| 2023-11-24 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 13,371 | 100.0% | 32% | 628 | 0.0% | 25% |
| 2023-11-24 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 27,605 | 100.0% | 35% | 434 | 0.0% | 26% |
| 2023-11-24 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 13,855 | 100.0% | 50% | 279 | 0.0% | 36% |
| 2023-11-24 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 26,534 | 100.0% | 39% | 536 | 0.0% | 39% |
| 2023-11-24 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 18,892 | 100.0% | 45% | 478 | 0.0% | 42% |
| 2023-11-24 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 12,055 | 100.0% | 51% | 400 | 0.0% | 44% |
| 2023-11-24 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,566 | 100.0% | 72% | 214 | 0.1% | 51% |
| 2023-11-24 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 333 | 100.0% | 86% | 124 | 0.0% | 57% |
| 2023-11-24 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,417 | 100.0% | 28% | 1,104 | 0.0% | 35% |
| 2023-11-24 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,417 | 100.0% | 28% | 1,104 | 0.0% | 35% |
| 2023-11-24 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,036 | 100.0% | 44% | 618 | 0.0% | 43% |
| 2023-11-24 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 129 | 100.0% | 84% | 109 | 0.0% | 60% |
| 2023-11-24 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 19 | 100.0% | 95% | 112 | 0.0% | 79% |
| 2023-11-24 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.810 below threshold | | | | | | | | |
| 2023-11-25 | aave_perp_binance_bybit | ok | 0.997 | gross>0bps | 12,991 | 99.2% | 40% | 995 | 0.0% | 44% |
| 2023-11-25 | aave_perp_binance_bybit | ok | 0.997 | gross>1bps | 13,454 | 99.2% | 40% | 866 | 0.0% | 44% |
| 2023-11-25 | aave_perp_binance_bybit | ok | 0.997 | gross>2bps | 9,542 | 99.5% | 44% | 626 | 0.0% | 45% |
| 2023-11-25 | aave_perp_binance_bybit | ok | 0.997 | gross>5bps | 937 | 99.9% | 75% | 156 | 0.0% | 62% |
| 2023-11-25 | aave_perp_binance_bybit | ok | 0.997 | retail_taker | 56 | 100.0% | 88% | 118 | 0.0% | 79% |
| 2023-11-25 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,274 | 99.9% | 24% | 1,819 | 0.0% | 33% |
| 2023-11-25 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,075 | 99.9% | 25% | 1,343 | 0.0% | 34% |
| 2023-11-25 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,158 | 99.9% | 26% | 1,132 | 0.0% | 37% |
| 2023-11-25 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,452 | 99.9% | 41% | 1,146 | 0.0% | 48% |
| 2023-11-25 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 12 | 100.0% | 92% | 111 | 0.0% | 83% |
| 2023-11-25 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 32 | 96.9% | 50% | 714,030 | 0.0% | 31% |
| 2023-11-25 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 76 | 98.7% | 22% | 120,902 | 0.0% | 21% |
| 2023-11-25 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 329 | 99.7% | 18% | 29,598 | 0.0% | 19% |
| 2023-11-25 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,175 | 99.9% | 27% | 3,789 | 0.0% | 27% |
| 2023-11-25 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 7 | 100.0% | 71% | 121 | 0.0% | 43% |
| 2023-11-25 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,451 | 100.0% | 28% | 2,110 | 0.0% | 42% |
| 2023-11-25 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,451 | 100.0% | 28% | 2,110 | 0.0% | 42% |
| 2023-11-25 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,302 | 100.0% | 37% | 1,220 | 0.0% | 47% |
| 2023-11-25 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 260 | 100.0% | 73% | 192 | 0.0% | 60% |
| 2023-11-25 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 15 | 100.0% | 87% | 112 | 0.0% | 53% |
| 2023-11-25 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,013 | 99.9% | 28% | 7,434 | 0.0% | 29% |
| 2023-11-25 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,760 | 99.9% | 16% | 2,784 | 0.0% | 21% |
| 2023-11-25 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,562 | 100.0% | 23% | 2,876 | 0.0% | 27% |
| 2023-11-25 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,039 | 99.9% | 36% | 1,939 | 0.0% | 40% |
| 2023-11-25 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 0% |
| 2023-11-25 | sol_perp_binance_bybit | excluded: bybit_ob/bybit/SOL-USDT/perp coverage 1.000 below threshold | | | | | | | | |
| 2023-11-25 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,149 | 100.0% | 38% | 1,240 | 0.0% | 29% |
| 2023-11-25 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,386 | 100.0% | 33% | 983 | 0.0% | 26% |
| 2023-11-25 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,501 | 100.0% | 30% | 880 | 0.0% | 25% |
| 2023-11-25 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 17,485 | 100.0% | 29% | 647 | 0.0% | 24% |
| 2023-11-25 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 11,778 | 100.0% | 46% | 561 | 0.0% | 34% |
| 2023-11-25 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 36,556 | 100.0% | 36% | 567 | 0.0% | 35% |
| 2023-11-25 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 31,326 | 100.0% | 39% | 526 | 0.0% | 36% |
| 2023-11-25 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 23,412 | 100.0% | 43% | 450 | 0.0% | 39% |
| 2023-11-25 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 8,220 | 100.0% | 54% | 313 | 0.0% | 43% |
| 2023-11-25 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 650 | 100.0% | 86% | 140 | 0.0% | 55% |
| 2023-11-25 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,570 | 99.9% | 28% | 3,171 | 0.0% | 42% |
| 2023-11-25 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,570 | 99.9% | 28% | 3,171 | 0.0% | 42% |
| 2023-11-25 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 520 | 99.8% | 43% | 1,025 | 0.0% | 56% |
| 2023-11-25 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 20 | 100.0% | 80% | 110 | 0.0% | 65% |
| 2023-11-25 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 0% |
| 2023-11-25 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.919 below threshold | | | | | | | | |
| 2023-11-26 | aave_perp_binance_bybit | ok | 0.999 | gross>0bps | 14,783 | 99.5% | 39% | 932 | 0.0% | 40% |
| 2023-11-26 | aave_perp_binance_bybit | ok | 0.999 | gross>1bps | 12,008 | 99.5% | 40% | 958 | 0.0% | 40% |
| 2023-11-26 | aave_perp_binance_bybit | ok | 0.999 | gross>2bps | 10,483 | 99.6% | 43% | 822 | 0.0% | 40% |
| 2023-11-26 | aave_perp_binance_bybit | ok | 0.999 | gross>5bps | 4,828 | 99.8% | 53% | 356 | 0.0% | 44% |
| 2023-11-26 | aave_perp_binance_bybit | ok | 0.999 | retail_taker | 163 | 100.0% | 91% | 117 | 0.0% | 62% |
| 2023-11-26 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,291 | 99.8% | 25% | 1,146 | 0.5% | 27% |
| 2023-11-26 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,930 | 99.9% | 24% | 954 | 0.2% | 29% |
| 2023-11-26 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,827 | 99.9% | 27% | 814 | 0.1% | 31% |
| 2023-11-26 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,752 | 99.9% | 41% | 589 | 0.1% | 40% |
| 2023-11-26 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 126 | 100.0% | 96% | 107 | 0.0% | 58% |
| 2023-11-26 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 71 | 98.6% | 72% | 328,336 | 42.3% | 23% |
| 2023-11-26 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 67 | 98.5% | 66% | 152,693 | 37.3% | 31% |
| 2023-11-26 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 92 | 98.9% | 64% | 32,589 | 38.0% | 37% |
| 2023-11-26 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 971 | 100.0% | 18% | 2,565 | 1.2% | 22% |
| 2023-11-26 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 2,071 | 100.0% | 37% | 899 | 0.8% | 33% |
| 2023-11-26 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,642 | 100.0% | 26% | 1,747 | 0.0% | 40% |
| 2023-11-26 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,642 | 100.0% | 26% | 1,747 | 0.0% | 40% |
| 2023-11-26 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,105 | 100.0% | 33% | 1,518 | 0.0% | 40% |
| 2023-11-26 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,617 | 100.0% | 53% | 279 | 0.0% | 43% |
| 2023-11-26 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 64 | 100.0% | 94% | 152 | 0.0% | 41% |
| 2023-11-26 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 220 | 99.5% | 53% | 10,195 | 0.0% | 44% |
| 2023-11-26 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 368 | 99.7% | 50% | 13,976 | 0.0% | 38% |
| 2023-11-26 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 894 | 99.9% | 29% | 9,132 | 0.0% | 27% |
| 2023-11-26 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 8,391 | 100.0% | 29% | 626 | 0.0% | 28% |
| 2023-11-26 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 70 | 100.0% | 87% | 124 | 0.0% | 53% |
| 2023-11-26 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,907 | 100.0% | 43% | 1,002 | 0.2% | 35% |
| 2023-11-26 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,871 | 100.0% | 36% | 694 | 0.2% | 31% |
| 2023-11-26 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 16,470 | 100.0% | 33% | 542 | 0.2% | 30% |
| 2023-11-26 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 13,662 | 100.0% | 45% | 300 | 0.2% | 38% |
| 2023-11-26 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 127 | 100.0% | 95% | 113 | 0.8% | 58% |
| 2023-11-26 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,825 | 99.5% | 41% | 1,742 | 0.2% | 30% |
| 2023-11-26 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,615 | 99.7% | 34% | 1,212 | 0.2% | 26% |
| 2023-11-26 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,978 | 99.8% | 32% | 1,162 | 0.1% | 26% |
| 2023-11-26 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 14,236 | 99.9% | 27% | 706 | 0.0% | 24% |
| 2023-11-26 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 12,836 | 100.0% | 40% | 442 | 0.0% | 31% |
| 2023-11-26 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 21,834 | 100.0% | 35% | 666 | 0.0% | 35% |
| 2023-11-26 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 21,082 | 100.0% | 35% | 648 | 0.0% | 35% |
| 2023-11-26 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 19,827 | 100.0% | 33% | 590 | 0.0% | 34% |
| 2023-11-26 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 14,662 | 100.0% | 38% | 347 | 0.0% | 38% |
| 2023-11-26 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 1,081 | 100.0% | 82% | 158 | 0.0% | 57% |
| 2023-11-26 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,281 | 100.0% | 37% | 1,357 | 0.0% | 31% |
| 2023-11-26 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,281 | 100.0% | 37% | 1,357 | 0.0% | 31% |
| 2023-11-26 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,563 | 100.0% | 34% | 947 | 0.0% | 37% |
| 2023-11-26 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 700 | 100.0% | 76% | 150 | 0.0% | 56% |
| 2023-11-26 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 86 | 100.0% | 95% | 260 | 0.0% | 48% |
| 2023-11-26 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.927 below threshold | | | | | | | | |
| 2023-11-27 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 16,696 | 99.6% | 39% | 844 | 0.0% | 37% |
| 2023-11-27 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 16,696 | 99.6% | 39% | 844 | 0.0% | 37% |
| 2023-11-27 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 13,938 | 99.7% | 40% | 667 | 0.0% | 38% |
| 2023-11-27 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,227 | 99.9% | 64% | 321 | 0.0% | 54% |
| 2023-11-27 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 8 | 100.0% | 100% | none resolved | 0.0% | 62% |
| 2023-11-27 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,811 | 99.9% | 25% | 916 | 0.0% | 29% |
| 2023-11-27 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,688 | 99.9% | 25% | 762 | 0.0% | 30% |
| 2023-11-27 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,411 | 100.0% | 27% | 655 | 0.0% | 31% |
| 2023-11-27 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 6,944 | 100.0% | 32% | 549 | 0.1% | 35% |
| 2023-11-27 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 121 | 100.0% | 93% | 110 | 0.0% | 62% |
| 2023-11-27 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 144 | 99.3% | 58% | 131,450 | 0.0% | 31% |
| 2023-11-27 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 252 | 99.6% | 35% | 24,696 | 0.0% | 29% |
| 2023-11-27 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 979 | 99.9% | 20% | 4,838 | 0.0% | 17% |
| 2023-11-27 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 8,060 | 100.0% | 29% | 648 | 0.0% | 27% |
| 2023-11-27 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 39 | 100.0% | 90% | 172 | 0.0% | 46% |
| 2023-11-27 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 15,949 | 100.0% | 32% | 706 | 0.0% | 34% |
| 2023-11-27 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 15,949 | 100.0% | 32% | 706 | 0.0% | 34% |
| 2023-11-27 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,536 | 100.0% | 38% | 487 | 0.0% | 38% |
| 2023-11-27 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,055 | 100.0% | 50% | 361 | 0.0% | 42% |
| 2023-11-27 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 99 | 100.0% | 98% | 110 | 0.0% | 54% |
| 2023-11-27 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 339 | 99.7% | 53% | 30,735 | 0.0% | 34% |
| 2023-11-27 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 561 | 99.8% | 37% | 14,570 | 0.0% | 25% |
| 2023-11-27 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,535 | 99.9% | 24% | 4,300 | 0.0% | 19% |
| 2023-11-27 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 9,538 | 100.0% | 34% | 547 | 0.0% | 32% |
| 2023-11-27 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 63 | 100.0% | 94% | 118 | 0.0% | 52% |
| 2023-11-27 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,683 | 100.0% | 43% | 1,489 | 0.0% | 34% |
| 2023-11-27 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,969 | 100.0% | 32% | 832 | 0.0% | 28% |
| 2023-11-27 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 14,099 | 100.0% | 34% | 576 | 0.0% | 31% |
| 2023-11-27 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 24,820 | 100.0% | 38% | 402 | 0.0% | 32% |
| 2023-11-27 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 1,514 | 100.0% | 70% | 199 | 0.0% | 47% |
| 2023-11-27 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 12,833 | 100.0% | 39% | 848 | 0.0% | 28% |
| 2023-11-27 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 16,693 | 100.0% | 36% | 682 | 0.0% | 26% |
| 2023-11-27 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 20,912 | 100.0% | 34% | 576 | 0.0% | 26% |
| 2023-11-27 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 30,336 | 100.0% | 36% | 426 | 0.0% | 27% |
| 2023-11-27 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 10,369 | 100.0% | 53% | 257 | 0.0% | 39% |
| 2023-11-27 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 33,617 | 100.0% | 38% | 538 | 0.0% | 36% |
| 2023-11-27 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 28,253 | 100.0% | 40% | 498 | 0.0% | 37% |
| 2023-11-27 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 21,524 | 100.0% | 44% | 387 | 0.0% | 39% |
| 2023-11-27 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 7,131 | 100.0% | 60% | 207 | 0.0% | 46% |
| 2023-11-27 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 1,033 | 100.0% | 78% | 141 | 0.0% | 52% |
| 2023-11-27 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,378 | 100.0% | 13% | 3,279 | 0.0% | 18% |
| 2023-11-27 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,378 | 100.0% | 13% | 3,279 | 0.0% | 18% |
| 2023-11-27 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,678 | 100.0% | 14% | 1,589 | 0.1% | 27% |
| 2023-11-27 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,586 | 100.0% | 32% | 895 | 0.0% | 38% |
| 2023-11-27 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 72 | 100.0% | 75% | 123 | 0.0% | 46% |
| 2023-11-27 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.887 below threshold | | | | | | | | |
| 2023-11-28 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 12,109 | 99.8% | 44% | 1,075 | 0.0% | 42% |
| 2023-11-28 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,109 | 99.8% | 44% | 1,075 | 0.0% | 42% |
| 2023-11-28 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,202 | 99.9% | 46% | 934 | 0.0% | 43% |
| 2023-11-28 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 8,771 | 100.0% | 45% | 480 | 0.0% | 36% |
| 2023-11-28 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 387 | 100.0% | 89% | 120 | 0.0% | 53% |
| 2023-11-28 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,233 | 99.9% | 22% | 1,114 | 0.0% | 27% |
| 2023-11-28 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,361 | 99.9% | 21% | 798 | 0.0% | 28% |
| 2023-11-28 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 9,136 | 99.9% | 22% | 646 | 0.0% | 30% |
| 2023-11-28 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 7,071 | 99.9% | 32% | 879 | 0.0% | 37% |
| 2023-11-28 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 63 | 100.0% | 94% | 106 | 0.0% | 57% |
| 2023-11-28 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 155 | 98.7% | 50% | 6,644 | 0.0% | 31% |
| 2023-11-28 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 226 | 99.1% | 31% | 4,696 | 0.0% | 27% |
| 2023-11-28 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 616 | 99.7% | 18% | 3,048 | 0.0% | 19% |
| 2023-11-28 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,710 | 100.0% | 21% | 1,103 | 0.0% | 25% |
| 2023-11-28 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 182 | 100.0% | 79% | 127 | 0.0% | 46% |
| 2023-11-28 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,149 | 100.0% | 29% | 1,361 | 0.0% | 31% |
| 2023-11-28 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,149 | 100.0% | 29% | 1,361 | 0.0% | 31% |
| 2023-11-28 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,283 | 100.0% | 33% | 1,140 | 0.0% | 34% |
| 2023-11-28 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,340 | 100.0% | 52% | 380 | 0.0% | 46% |
| 2023-11-28 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 108 | 100.0% | 88% | 117 | 0.0% | 57% |
| 2023-11-28 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 369 | 99.5% | 43% | 10,288 | 0.0% | 28% |
| 2023-11-28 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 749 | 99.7% | 18% | 3,186 | 0.0% | 19% |
| 2023-11-28 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,061 | 99.9% | 15% | 5,038 | 0.1% | 16% |
| 2023-11-28 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 7,446 | 100.0% | 34% | 730 | 0.0% | 29% |
| 2023-11-28 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 26 | 100.0% | 85% | 116 | 0.0% | 62% |
| 2023-11-28 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,318 | 100.0% | 43% | 1,674 | 0.0% | 32% |
| 2023-11-28 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,294 | 100.0% | 29% | 882 | 0.0% | 25% |
| 2023-11-28 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 17,673 | 100.0% | 28% | 589 | 0.0% | 25% |
| 2023-11-28 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 18,600 | 100.0% | 40% | 337 | 0.0% | 36% |
| 2023-11-28 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 761 | 99.9% | 54% | 334 | 0.0% | 48% |
| 2023-11-28 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 25,370 | 100.0% | 42% | 566 | 0.0% | 29% |
| 2023-11-28 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 28,500 | 100.0% | 39% | 503 | 0.0% | 28% |
| 2023-11-28 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 33,406 | 100.0% | 37% | 434 | 0.0% | 28% |
| 2023-11-28 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 33,567 | 100.0% | 41% | 324 | 0.0% | 31% |
| 2023-11-28 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 4,386 | 100.0% | 71% | 188 | 0.0% | 47% |
| 2023-11-28 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 19,742 | 100.0% | 24% | 723 | 0.0% | 33% |
| 2023-11-28 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 19,918 | 100.0% | 25% | 617 | 0.0% | 34% |
| 2023-11-28 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 19,268 | 100.0% | 27% | 526 | 0.0% | 36% |
| 2023-11-28 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 8,192 | 100.0% | 42% | 334 | 0.0% | 45% |
| 2023-11-28 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 481 | 100.0% | 71% | 162 | 0.0% | 55% |
| 2023-11-28 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,708 | 100.0% | 17% | 1,824 | 0.0% | 31% |
| 2023-11-28 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,708 | 100.0% | 17% | 1,824 | 0.0% | 31% |
| 2023-11-28 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,079 | 100.0% | 25% | 2,153 | 0.0% | 36% |
| 2023-11-28 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 656 | 100.0% | 45% | 1,992 | 0.0% | 49% |
| 2023-11-28 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 30 | 100.0% | 100% | none resolved | 0.0% | 57% |
| 2023-11-28 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.878 below threshold | | | | | | | | |
| 2023-11-29 | aave_perp_binance_bybit | ok | 0.999 | gross>0bps | 10,673 | 99.6% | 24% | 1,108 | 0.0% | 28% |
| 2023-11-29 | aave_perp_binance_bybit | ok | 0.999 | gross>1bps | 10,673 | 99.6% | 24% | 1,108 | 0.0% | 28% |
| 2023-11-29 | aave_perp_binance_bybit | ok | 0.999 | gross>2bps | 10,931 | 99.8% | 27% | 673 | 0.0% | 30% |
| 2023-11-29 | aave_perp_binance_bybit | ok | 0.999 | gross>5bps | 2,636 | 100.0% | 56% | 262 | 0.0% | 48% |
| 2023-11-29 | aave_perp_binance_bybit | ok | 0.999 | retail_taker | 61 | 100.0% | 95% | 115 | 0.0% | 59% |
| 2023-11-29 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,121 | 99.6% | 13% | 1,909 | 0.0% | 20% |
| 2023-11-29 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,821 | 99.7% | 15% | 1,179 | 0.0% | 22% |
| 2023-11-29 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,820 | 99.8% | 17% | 1,041 | 0.0% | 24% |
| 2023-11-29 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 6,522 | 99.9% | 27% | 556 | 0.0% | 34% |
| 2023-11-29 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 100 | 100.0% | 89% | 127 | 0.0% | 63% |
| 2023-11-29 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 417 | 99.8% | 46% | 5,062 | 0.0% | 32% |
| 2023-11-29 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,049 | 99.9% | 22% | 2,442 | 0.0% | 18% |
| 2023-11-29 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,042 | 100.0% | 21% | 1,585 | 0.0% | 19% |
| 2023-11-29 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,732 | 100.0% | 34% | 1,035 | 0.0% | 29% |
| 2023-11-29 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 17 | 100.0% | 94% | 100 | 0.0% | 65% |
| 2023-11-29 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,257 | 100.0% | 25% | 1,074 | 0.0% | 29% |
| 2023-11-29 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,257 | 100.0% | 25% | 1,074 | 0.0% | 29% |
| 2023-11-29 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,233 | 100.0% | 27% | 944 | 0.0% | 33% |
| 2023-11-29 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,258 | 100.0% | 36% | 358 | 0.0% | 37% |
| 2023-11-29 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 189 | 100.0% | 83% | 126 | 0.0% | 51% |
| 2023-11-29 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,705 | 100.0% | 28% | 1,128 | 0.0% | 27% |
| 2023-11-29 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,132 | 100.0% | 33% | 644 | 0.0% | 29% |
| 2023-11-29 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,307 | 100.0% | 31% | 2,779 | 0.0% | 23% |
| 2023-11-29 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,851 | 100.0% | 42% | 402 | 0.0% | 35% |
| 2023-11-29 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 13 | 100.0% | 100% | none resolved | 0.0% | 15% |
| 2023-11-29 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,721 | 100.0% | 44% | 2,218 | 0.0% | 33% |
| 2023-11-29 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,789 | 100.0% | 30% | 978 | 0.0% | 26% |
| 2023-11-29 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 14,346 | 100.0% | 29% | 597 | 0.0% | 26% |
| 2023-11-29 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 24,456 | 100.0% | 38% | 354 | 0.0% | 32% |
| 2023-11-29 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 666 | 100.0% | 86% | 122 | 0.0% | 56% |
| 2023-11-29 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,461 | 99.9% | 40% | 1,202 | 0.0% | 31% |
| 2023-11-29 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,535 | 100.0% | 37% | 877 | 0.0% | 30% |
| 2023-11-29 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,054 | 100.0% | 36% | 758 | 0.0% | 29% |
| 2023-11-29 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 19,047 | 100.0% | 36% | 562 | 0.0% | 31% |
| 2023-11-29 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 14,096 | 100.0% | 47% | 314 | 0.0% | 37% |
| 2023-11-29 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,708 | 100.0% | 26% | 1,088 | 0.0% | 37% |
| 2023-11-29 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 15,314 | 100.0% | 25% | 869 | 0.0% | 36% |
| 2023-11-29 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 15,548 | 100.0% | 27% | 666 | 0.0% | 38% |
| 2023-11-29 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 9,369 | 100.0% | 34% | 472 | 0.0% | 40% |
| 2023-11-29 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 886 | 100.0% | 74% | 212 | 0.0% | 61% |
| 2023-11-29 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,514 | 100.0% | 13% | 3,504 | 0.0% | 25% |
| 2023-11-29 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,514 | 100.0% | 13% | 3,504 | 0.0% | 25% |
| 2023-11-29 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,865 | 100.0% | 18% | 4,184 | 0.0% | 35% |
| 2023-11-29 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 574 | 100.0% | 56% | 256 | 0.0% | 52% |
| 2023-11-29 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 35 | 100.0% | 97% | 118 | 0.0% | 51% |
| 2023-11-29 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.854 below threshold | | | | | | | | |
| 2023-11-30 | aave_perp_binance_bybit | ok | 0.999 | gross>0bps | 9,321 | 99.5% | 32% | 1,336 | 0.0% | 39% |
| 2023-11-30 | aave_perp_binance_bybit | ok | 0.999 | gross>1bps | 9,321 | 99.5% | 32% | 1,336 | 0.0% | 39% |
| 2023-11-30 | aave_perp_binance_bybit | ok | 0.999 | gross>2bps | 5,634 | 99.8% | 37% | 965 | 0.0% | 41% |
| 2023-11-30 | aave_perp_binance_bybit | ok | 0.999 | gross>5bps | 318 | 100.0% | 80% | 467 | 0.6% | 60% |
| 2023-11-30 | aave_perp_binance_bybit | ok | 0.999 | retail_taker | 20 | 100.0% | 85% | 119 | 0.0% | 75% |
| 2023-11-30 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 668 | 99.6% | 19% | 4,007 | 0.0% | 24% |
| 2023-11-30 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,343 | 99.7% | 13% | 1,810 | 0.0% | 23% |
| 2023-11-30 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,082 | 99.8% | 15% | 1,398 | 0.0% | 28% |
| 2023-11-30 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,918 | 99.9% | 17% | 2,498 | 0.0% | 29% |
| 2023-11-30 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 264 | 100.0% | 74% | 138 | 0.0% | 57% |
| 2023-11-30 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 189 | 99.5% | 59% | 30,468 | 0.0% | 38% |
| 2023-11-30 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 447 | 99.8% | 28% | 10,245 | 0.0% | 20% |
| 2023-11-30 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,300 | 100.0% | 15% | 1,756 | 0.0% | 17% |
| 2023-11-30 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,590 | 100.0% | 28% | 1,342 | 0.0% | 27% |
| 2023-11-30 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 5 | 100.0% | 60% | 201 | 0.0% | 40% |
| 2023-11-30 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,802 | 100.0% | 22% | 1,172 | 0.0% | 24% |
| 2023-11-30 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,802 | 100.0% | 22% | 1,172 | 0.0% | 24% |
| 2023-11-30 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,140 | 100.0% | 22% | 1,067 | 0.0% | 26% |
| 2023-11-30 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,992 | 100.0% | 32% | 728 | 0.0% | 37% |
| 2023-11-30 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 250 | 100.0% | 82% | 117 | 0.0% | 52% |
| 2023-11-30 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 95 | 98.9% | 45% | 88,064 | 0.0% | 24% |
| 2023-11-30 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 304 | 99.7% | 19% | 17,899 | 0.0% | 13% |
| 2023-11-30 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,562 | 99.9% | 9% | 3,573 | 0.1% | 13% |
| 2023-11-30 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,012 | 100.0% | 30% | 784 | 0.0% | 31% |
| 2023-11-30 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 3 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2023-11-30 | sol_perp_binance_bybit | excluded: bybit_ob/bybit/SOL-USDT/perp coverage 1.000 below threshold | | | | | | | | |
| 2023-11-30 | tia_perp_binance_bybit | excluded: bybit_ob/bybit/TIA-USDT/perp coverage 1.000 below threshold | | | | | | | | |
| 2023-11-30 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 9,393 | 99.8% | 20% | 1,464 | 0.0% | 34% |
| 2023-11-30 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,937 | 99.8% | 20% | 1,093 | 0.0% | 36% |
| 2023-11-30 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,620 | 99.9% | 22% | 940 | 0.0% | 38% |
| 2023-11-30 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 8,220 | 99.9% | 36% | 604 | 0.0% | 47% |
| 2023-11-30 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 362 | 100.0% | 77% | 147 | 0.6% | 69% |
| 2023-11-30 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,249 | 100.0% | 22% | 5,185 | 0.0% | 27% |
| 2023-11-30 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,249 | 100.0% | 22% | 5,185 | 0.0% | 27% |
| 2023-11-30 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,739 | 100.0% | 16% | 4,355 | 0.0% | 28% |
| 2023-11-30 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 996 | 100.0% | 35% | 1,012 | 0.0% | 45% |
| 2023-11-30 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 70 | 100.0% | 96% | 146 | 0.0% | 51% |
| 2023-11-30 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.858 below threshold | | | | | | | | |
| 2023-12-01 | aave_perp_binance_bybit | ok | 0.999 | gross>0bps | 3,661 | 97.0% | 20% | 3,092 | 0.0% | 28% |
| 2023-12-01 | aave_perp_binance_bybit | ok | 0.999 | gross>1bps | 4,877 | 97.9% | 21% | 2,209 | 0.0% | 27% |
| 2023-12-01 | aave_perp_binance_bybit | ok | 0.999 | gross>2bps | 7,235 | 99.1% | 21% | 1,402 | 0.0% | 28% |
| 2023-12-01 | aave_perp_binance_bybit | ok | 0.999 | gross>5bps | 4,612 | 99.9% | 42% | 695 | 0.0% | 43% |
| 2023-12-01 | aave_perp_binance_bybit | ok | 0.999 | retail_taker | 97 | 100.0% | 94% | 116 | 0.0% | 63% |
| 2023-12-01 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 247 | 98.4% | 28% | 43,634 | 0.0% | 27% |
| 2023-12-01 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 611 | 99.3% | 18% | 9,495 | 0.2% | 19% |
| 2023-12-01 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,390 | 99.7% | 11% | 4,330 | 0.1% | 22% |
| 2023-12-01 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 5,435 | 100.0% | 18% | 1,119 | 0.1% | 28% |
| 2023-12-01 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 1,842 | 100.0% | 41% | 699 | 0.0% | 42% |
| 2023-12-01 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 268 | 99.6% | 71% | 360 | 4.5% | 42% |
| 2023-12-01 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 350 | 99.7% | 51% | 1,054 | 6.0% | 32% |
| 2023-12-01 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 821 | 99.9% | 29% | 3,311 | 3.9% | 23% |
| 2023-12-01 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 6,429 | 100.0% | 24% | 1,034 | 0.6% | 25% |
| 2023-12-01 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 83 | 100.0% | 67% | 176 | 1.2% | 33% |
| 2023-12-01 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,234 | 100.0% | 21% | 1,410 | 0.0% | 28% |
| 2023-12-01 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,234 | 100.0% | 21% | 1,410 | 0.0% | 28% |
| 2023-12-01 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,001 | 100.0% | 24% | 1,041 | 0.0% | 33% |
| 2023-12-01 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,508 | 100.0% | 49% | 308 | 0.0% | 47% |
| 2023-12-01 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 36 | 100.0% | 94% | 115 | 0.0% | 67% |
| 2023-12-01 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 115 | 99.1% | 52% | 185,550 | 0.0% | 33% |
| 2023-12-01 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 159 | 99.4% | 45% | 103,068 | 0.0% | 29% |
| 2023-12-01 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 306 | 99.7% | 30% | 17,942 | 0.0% | 22% |
| 2023-12-01 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 6,507 | 100.0% | 21% | 1,898 | 0.0% | 21% |
| 2023-12-01 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 187 | 100.0% | 88% | 118 | 0.0% | 48% |
| 2023-12-01 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 623 | 99.8% | 44% | 25,650 | 0.0% | 34% |
| 2023-12-01 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,396 | 99.9% | 26% | 5,786 | 0.1% | 24% |
| 2023-12-01 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,013 | 100.0% | 19% | 1,566 | 0.1% | 19% |
| 2023-12-01 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 14,791 | 100.0% | 29% | 574 | 0.0% | 28% |
| 2023-12-01 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 1,829 | 100.0% | 64% | 253 | 0.3% | 46% |
| 2023-12-01 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 19,976 | 100.0% | 40% | 561 | 0.0% | 30% |
| 2023-12-01 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 24,999 | 100.0% | 37% | 455 | 0.0% | 29% |
| 2023-12-01 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 30,890 | 100.0% | 36% | 374 | 0.0% | 30% |
| 2023-12-01 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 34,784 | 100.0% | 40% | 288 | 0.0% | 33% |
| 2023-12-01 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 7,169 | 100.0% | 61% | 198 | 0.0% | 45% |
| 2023-12-01 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 12,386 | 99.9% | 31% | 1,094 | 0.0% | 43% |
| 2023-12-01 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,443 | 99.9% | 33% | 834 | 0.0% | 45% |
| 2023-12-01 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,449 | 100.0% | 36% | 683 | 0.0% | 47% |
| 2023-12-01 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,206 | 100.0% | 52% | 484 | 0.0% | 53% |
| 2023-12-01 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 85 | 100.0% | 87% | 107 | 0.0% | 61% |
| 2023-12-01 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,217 | 100.0% | 22% | 3,239 | 0.0% | 38% |
| 2023-12-01 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,217 | 100.0% | 22% | 3,239 | 0.0% | 38% |
| 2023-12-01 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 795 | 100.0% | 38% | 1,198 | 0.0% | 45% |
| 2023-12-01 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 18 | 100.0% | 72% | 110 | 0.0% | 50% |
| 2023-12-01 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 5 | 100.0% | 80% | 101 | 0.0% | 20% |
| 2023-12-01 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.832 below threshold | | | | | | | | |
| 2023-12-02 | aave_perp_binance_bybit | ok | 0.996 | gross>0bps | 2,364 | 92.0% | 25% | 4,792 | 0.0% | 28% |
| 2023-12-02 | aave_perp_binance_bybit | ok | 0.996 | gross>1bps | 4,464 | 95.6% | 22% | 2,424 | 0.0% | 27% |
| 2023-12-02 | aave_perp_binance_bybit | ok | 0.996 | gross>2bps | 6,648 | 97.4% | 25% | 1,255 | 0.0% | 30% |
| 2023-12-02 | aave_perp_binance_bybit | ok | 0.996 | gross>5bps | 3,536 | 99.0% | 47% | 778 | 0.0% | 45% |
| 2023-12-02 | aave_perp_binance_bybit | ok | 0.996 | retail_taker | 92 | 100.0% | 90% | 173 | 0.0% | 58% |
| 2023-12-02 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,886 | 99.9% | 28% | 712 | 5.6% | 27% |
| 2023-12-02 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,862 | 99.9% | 28% | 728 | 4.3% | 29% |
| 2023-12-02 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,638 | 99.9% | 29% | 654 | 3.5% | 30% |
| 2023-12-02 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,430 | 99.9% | 35% | 794 | 3.7% | 36% |
| 2023-12-02 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 629 | 100.0% | 53% | 512 | 8.7% | 52% |
| 2023-12-02 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 495 | 99.8% | 68% | 703 | 63.4% | 45% |
| 2023-12-02 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 593 | 99.8% | 61% | 1,078 | 48.9% | 38% |
| 2023-12-02 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 907 | 99.9% | 50% | 1,044 | 32.0% | 30% |
| 2023-12-02 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,291 | 100.0% | 36% | 642 | 5.8% | 28% |
| 2023-12-02 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 238 | 100.0% | 77% | 345 | 71.4% | 45% |
| 2023-12-02 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,692 | 99.9% | 22% | 2,580 | 0.0% | 26% |
| 2023-12-02 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,692 | 99.9% | 22% | 2,580 | 0.0% | 26% |
| 2023-12-02 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,550 | 100.0% | 17% | 2,096 | 0.0% | 23% |
| 2023-12-02 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,423 | 100.0% | 25% | 2,028 | 0.0% | 33% |
| 2023-12-02 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 104 | 100.0% | 82% | 165 | 0.0% | 54% |
| 2023-12-02 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 863 | 99.9% | 77% | 451 | 0.0% | 40% |
| 2023-12-02 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 985 | 99.9% | 72% | 463 | 0.0% | 40% |
| 2023-12-02 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,202 | 99.9% | 64% | 525 | 0.0% | 39% |
| 2023-12-02 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 6,574 | 100.0% | 28% | 1,344 | 0.0% | 21% |
| 2023-12-02 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 439 | 100.0% | 88% | 149 | 0.0% | 46% |
| 2023-12-02 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,285 | 100.0% | 40% | 1,044 | 2.7% | 32% |
| 2023-12-02 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,477 | 100.0% | 32% | 694 | 2.2% | 27% |
| 2023-12-02 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 12,559 | 100.0% | 30% | 617 | 1.8% | 28% |
| 2023-12-02 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 9,771 | 100.0% | 35% | 512 | 2.1% | 32% |
| 2023-12-02 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 247 | 100.0% | 77% | 224 | 59.1% | 43% |
| 2023-12-02 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 22,588 | 100.0% | 54% | 489 | 0.0% | 34% |
| 2023-12-02 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 26,254 | 100.0% | 51% | 417 | 0.0% | 33% |
| 2023-12-02 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 31,699 | 100.0% | 49% | 362 | 0.0% | 32% |
| 2023-12-02 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 49,197 | 100.0% | 48% | 310 | 0.0% | 32% |
| 2023-12-02 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 29,260 | 100.0% | 57% | 229 | 0.0% | 38% |
| 2023-12-02 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,753 | 99.9% | 31% | 1,021 | 0.0% | 43% |
| 2023-12-02 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,522 | 99.9% | 33% | 924 | 0.0% | 44% |
| 2023-12-02 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 9,475 | 99.9% | 36% | 767 | 0.0% | 48% |
| 2023-12-02 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,861 | 100.0% | 67% | 228 | 0.0% | 63% |
| 2023-12-02 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 135 | 100.0% | 88% | 113 | 0.0% | 70% |
| 2023-12-02 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,565 | 99.9% | 29% | 3,560 | 0.0% | 37% |
| 2023-12-02 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,565 | 99.9% | 29% | 3,560 | 0.0% | 37% |
| 2023-12-02 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 664 | 100.0% | 45% | 1,123 | 0.0% | 43% |
| 2023-12-02 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 43 | 100.0% | 95% | 278 | 0.0% | 40% |
| 2023-12-02 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 4 | 100.0% | 75% | 267 | 0.0% | 50% |
| 2023-12-02 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.933 below threshold | | | | | | | | |
| 2023-12-03 | aave_perp_binance_bybit | ok | 0.997 | gross>0bps | 7,773 | 97.8% | 28% | 1,662 | 0.0% | 34% |
| 2023-12-03 | aave_perp_binance_bybit | ok | 0.997 | gross>1bps | 7,336 | 98.5% | 32% | 1,028 | 0.1% | 37% |
| 2023-12-03 | aave_perp_binance_bybit | ok | 0.997 | gross>2bps | 5,306 | 99.1% | 36% | 798 | 0.0% | 40% |
| 2023-12-03 | aave_perp_binance_bybit | ok | 0.997 | gross>5bps | 1,009 | 100.0% | 53% | 276 | 0.0% | 53% |
| 2023-12-03 | aave_perp_binance_bybit | ok | 0.997 | retail_taker | 40 | 100.0% | 82% | 107 | 0.0% | 70% |
| 2023-12-03 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,696 | 99.9% | 26% | 1,021 | 0.7% | 29% |
| 2023-12-03 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,948 | 100.0% | 25% | 926 | 0.6% | 29% |
| 2023-12-03 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,444 | 100.0% | 27% | 936 | 0.6% | 32% |
| 2023-12-03 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,276 | 100.0% | 45% | 650 | 1.0% | 45% |
| 2023-12-03 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 42 | 100.0% | 86% | 110 | 2.4% | 67% |
| 2023-12-03 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 187 | 99.5% | 60% | 1,822 | 43.3% | 39% |
| 2023-12-03 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 240 | 99.6% | 49% | 2,242 | 34.2% | 36% |
| 2023-12-03 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 458 | 99.8% | 34% | 1,614 | 17.2% | 27% |
| 2023-12-03 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,177 | 100.0% | 25% | 1,134 | 2.3% | 24% |
| 2023-12-03 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 120 | 100.0% | 77% | 263 | 42.5% | 41% |
| 2023-12-03 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,698 | 100.0% | 19% | 1,971 | 0.0% | 24% |
| 2023-12-03 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,698 | 100.0% | 19% | 1,971 | 0.0% | 24% |
| 2023-12-03 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,847 | 100.0% | 18% | 1,426 | 0.0% | 27% |
| 2023-12-03 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,163 | 100.0% | 30% | 664 | 0.0% | 40% |
| 2023-12-03 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 58 | 100.0% | 86% | 110 | 0.0% | 57% |
| 2023-12-03 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 164 | 99.4% | 57% | 73,112 | 0.0% | 32% |
| 2023-12-03 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 251 | 99.6% | 39% | 31,048 | 0.0% | 26% |
| 2023-12-03 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 692 | 99.9% | 19% | 7,273 | 0.0% | 19% |
| 2023-12-03 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,497 | 100.0% | 23% | 1,835 | 0.0% | 22% |
| 2023-12-03 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 381 | 100.0% | 78% | 146 | 0.0% | 48% |
| 2023-12-03 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,069 | 100.0% | 33% | 1,142 | 0.3% | 30% |
| 2023-12-03 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 15,834 | 100.0% | 31% | 730 | 0.2% | 28% |
| 2023-12-03 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 17,594 | 100.0% | 30% | 534 | 0.2% | 29% |
| 2023-12-03 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 7,198 | 100.0% | 48% | 269 | 0.4% | 40% |
| 2023-12-03 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 83 | 100.0% | 87% | 112 | 3.6% | 55% |
| 2023-12-03 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 9,244 | 100.0% | 49% | 1,178 | 0.0% | 34% |
| 2023-12-03 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,774 | 100.0% | 44% | 818 | 0.0% | 31% |
| 2023-12-03 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 19,271 | 100.0% | 40% | 571 | 0.0% | 28% |
| 2023-12-03 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 39,781 | 100.0% | 43% | 357 | 0.0% | 31% |
| 2023-12-03 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 21,188 | 100.0% | 55% | 244 | 0.0% | 37% |
| 2023-12-03 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 16,340 | 100.0% | 37% | 904 | 0.0% | 47% |
| 2023-12-03 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,059 | 100.0% | 44% | 712 | 0.0% | 51% |
| 2023-12-03 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,316 | 100.0% | 53% | 501 | 0.0% | 55% |
| 2023-12-03 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,033 | 100.0% | 84% | 134 | 0.0% | 66% |
| 2023-12-03 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 112 | 100.0% | 90% | 110 | 0.0% | 69% |
| 2023-12-03 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,611 | 100.0% | 32% | 1,457 | 0.0% | 39% |
| 2023-12-03 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,611 | 100.0% | 32% | 1,457 | 0.0% | 39% |
| 2023-12-03 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,449 | 100.0% | 51% | 522 | 0.1% | 50% |
| 2023-12-03 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 64 | 100.0% | 95% | 113 | 0.0% | 55% |
| 2023-12-03 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 9 | 100.0% | 100% | none resolved | 0.0% | 89% |
| 2023-12-03 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.943 below threshold | | | | | | | | |
| 2023-12-04 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 24,892 | 100.0% | 36% | 766 | 0.0% | 34% |
| 2023-12-04 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 22,348 | 100.0% | 39% | 644 | 0.0% | 37% |
| 2023-12-04 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 14,950 | 100.0% | 48% | 464 | 0.0% | 42% |
| 2023-12-04 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,796 | 100.0% | 70% | 204 | 0.3% | 44% |
| 2023-12-04 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 521 | 100.0% | 84% | 155 | 0.0% | 49% |
| 2023-12-04 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 22,747 | 100.0% | 44% | 569 | 0.0% | 35% |
| 2023-12-04 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 18,448 | 100.0% | 48% | 608 | 0.1% | 37% |
| 2023-12-04 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 15,220 | 100.0% | 48% | 636 | 0.1% | 36% |
| 2023-12-04 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 8,337 | 100.0% | 45% | 476 | 0.1% | 37% |
| 2023-12-04 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 1,226 | 100.0% | 78% | 206 | 0.7% | 46% |
| 2023-12-04 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,239 | 100.0% | 44% | 2,084 | 2.9% | 34% |
| 2023-12-04 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,129 | 100.0% | 28% | 983 | 1.9% | 24% |
| 2023-12-04 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,428 | 100.0% | 29% | 664 | 1.0% | 24% |
| 2023-12-04 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 9,552 | 100.0% | 33% | 558 | 0.4% | 28% |
| 2023-12-04 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 135 | 100.0% | 90% | 122 | 14.8% | 42% |
| 2023-12-04 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,367 | 100.0% | 38% | 742 | 0.0% | 31% |
| 2023-12-04 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 14,367 | 100.0% | 38% | 742 | 0.0% | 31% |
| 2023-12-04 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 13,473 | 100.0% | 38% | 684 | 0.1% | 33% |
| 2023-12-04 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 8,519 | 100.0% | 40% | 606 | 0.2% | 32% |
| 2023-12-04 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 2,722 | 100.0% | 58% | 250 | 0.6% | 39% |
| 2023-12-04 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,193 | 99.9% | 48% | 3,644 | 0.7% | 29% |
| 2023-12-04 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,610 | 100.0% | 24% | 1,333 | 0.5% | 22% |
| 2023-12-04 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,691 | 100.0% | 25% | 840 | 0.2% | 22% |
| 2023-12-04 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 8,282 | 100.0% | 34% | 1,058 | 0.1% | 27% |
| 2023-12-04 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 224 | 100.0% | 80% | 132 | 1.3% | 48% |
| 2023-12-04 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 17,688 | 100.0% | 49% | 779 | 0.2% | 32% |
| 2023-12-04 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 21,166 | 100.0% | 41% | 603 | 0.2% | 28% |
| 2023-12-04 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 26,134 | 100.0% | 38% | 505 | 0.1% | 28% |
| 2023-12-04 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 17,884 | 100.0% | 46% | 402 | 0.1% | 34% |
| 2023-12-04 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 954 | 100.0% | 83% | 168 | 1.2% | 49% |
| 2023-12-04 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 21,918 | 100.0% | 55% | 616 | 0.0% | 35% |
| 2023-12-04 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 26,523 | 100.0% | 53% | 527 | 0.0% | 33% |
| 2023-12-04 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 32,763 | 100.0% | 51% | 448 | 0.0% | 32% |
| 2023-12-04 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 56,970 | 100.0% | 52% | 350 | 0.0% | 33% |
| 2023-12-04 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 49,907 | 100.0% | 60% | 289 | 0.0% | 38% |
| 2023-12-04 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 26,776 | 100.0% | 37% | 578 | 0.0% | 41% |
| 2023-12-04 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 20,219 | 100.0% | 41% | 528 | 0.1% | 43% |
| 2023-12-04 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 13,450 | 100.0% | 47% | 450 | 0.1% | 46% |
| 2023-12-04 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,821 | 100.0% | 76% | 211 | 0.2% | 51% |
| 2023-12-04 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 622 | 100.0% | 86% | 142 | 0.8% | 43% |
| 2023-12-04 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,315 | 100.0% | 32% | 1,314 | 0.0% | 30% |
| 2023-12-04 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,315 | 100.0% | 32% | 1,314 | 0.0% | 30% |
| 2023-12-04 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,296 | 100.0% | 32% | 974 | 0.0% | 33% |
| 2023-12-04 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,239 | 100.0% | 62% | 264 | 0.1% | 47% |
| 2023-12-04 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 431 | 100.0% | 81% | 222 | 0.5% | 46% |
| 2023-12-04 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.930 below threshold | | | | | | | | |
| 2023-12-05 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 20,173 | 99.9% | 35% | 892 | 0.0% | 36% |
| 2023-12-05 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 19,650 | 99.9% | 35% | 891 | 0.0% | 36% |
| 2023-12-05 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 15,401 | 99.9% | 40% | 742 | 0.0% | 40% |
| 2023-12-05 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,777 | 100.0% | 56% | 360 | 0.0% | 48% |
| 2023-12-05 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 266 | 100.0% | 76% | 146 | 0.0% | 47% |
| 2023-12-05 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 22,743 | 100.0% | 32% | 617 | 0.4% | 29% |
| 2023-12-05 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 19,075 | 100.0% | 34% | 510 | 0.4% | 32% |
| 2023-12-05 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 13,864 | 100.0% | 38% | 398 | 0.6% | 34% |
| 2023-12-05 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,473 | 100.0% | 52% | 257 | 0.8% | 40% |
| 2023-12-05 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 95 | 100.0% | 96% | 125 | 0.0% | 54% |
| 2023-12-05 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,542 | 100.0% | 58% | 1,237 | 10.0% | 38% |
| 2023-12-05 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,741 | 100.0% | 42% | 834 | 6.2% | 29% |
| 2023-12-05 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,162 | 100.0% | 35% | 688 | 3.3% | 26% |
| 2023-12-05 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 13,553 | 100.0% | 39% | 419 | 1.4% | 28% |
| 2023-12-05 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 270 | 100.0% | 91% | 168 | 38.9% | 52% |
| 2023-12-05 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,042 | 100.0% | 34% | 885 | 0.0% | 31% |
| 2023-12-05 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,042 | 100.0% | 34% | 885 | 0.0% | 31% |
| 2023-12-05 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,687 | 100.0% | 34% | 862 | 0.0% | 30% |
| 2023-12-05 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 10,659 | 100.0% | 36% | 453 | 0.0% | 32% |
| 2023-12-05 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 1,959 | 100.0% | 71% | 161 | 0.0% | 41% |
| 2023-12-05 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 12,591 | 100.0% | 38% | 958 | 0.0% | 27% |
| 2023-12-05 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 14,277 | 100.0% | 33% | 553 | 0.0% | 24% |
| 2023-12-05 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 14,582 | 100.0% | 38% | 388 | 0.0% | 26% |
| 2023-12-05 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,236 | 100.0% | 41% | 734 | 0.0% | 35% |
| 2023-12-05 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 40 | 100.0% | 92% | 153 | 0.0% | 62% |
| 2023-12-05 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,805 | 100.0% | 43% | 1,262 | 2.2% | 31% |
| 2023-12-05 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,250 | 100.0% | 32% | 825 | 1.4% | 25% |
| 2023-12-05 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 17,869 | 100.0% | 28% | 590 | 0.6% | 23% |
| 2023-12-05 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 24,067 | 100.0% | 41% | 298 | 0.3% | 32% |
| 2023-12-05 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 312 | 100.0% | 87% | 137 | 13.1% | 56% |
| 2023-12-05 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 37,217 | 100.0% | 56% | 548 | 0.0% | 34% |
| 2023-12-05 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 46,637 | 100.0% | 53% | 460 | 0.0% | 33% |
| 2023-12-05 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 57,665 | 100.0% | 52% | 394 | 0.0% | 33% |
| 2023-12-05 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 71,849 | 100.0% | 58% | 284 | 0.0% | 36% |
| 2023-12-05 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 28,539 | 100.0% | 69% | 218 | 0.0% | 42% |
| 2023-12-05 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 23,085 | 100.0% | 32% | 650 | 0.0% | 43% |
| 2023-12-05 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 17,334 | 100.0% | 35% | 587 | 0.0% | 45% |
| 2023-12-05 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 12,269 | 100.0% | 39% | 548 | 0.0% | 48% |
| 2023-12-05 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,069 | 100.0% | 59% | 374 | 0.0% | 59% |
| 2023-12-05 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 147 | 100.0% | 93% | 117 | 0.0% | 56% |
| 2023-12-05 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,540 | 100.0% | 15% | 2,083 | 0.0% | 22% |
| 2023-12-05 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,540 | 100.0% | 15% | 2,083 | 0.0% | 22% |
| 2023-12-05 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,365 | 100.0% | 18% | 1,254 | 0.0% | 29% |
| 2023-12-05 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,542 | 100.0% | 35% | 1,148 | 0.0% | 45% |
| 2023-12-05 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 34 | 100.0% | 97% | 114 | 0.0% | 50% |
| 2023-12-05 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.941 below threshold | | | | | | | | |
| 2023-12-06 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 25,965 | 100.0% | 39% | 700 | 0.0% | 38% |
| 2023-12-06 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 25,750 | 100.0% | 39% | 700 | 0.0% | 38% |
| 2023-12-06 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 14,915 | 100.0% | 48% | 500 | 0.0% | 45% |
| 2023-12-06 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,374 | 100.0% | 78% | 250 | 0.0% | 56% |
| 2023-12-06 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 80 | 100.0% | 96% | 107 | 0.0% | 56% |
| 2023-12-06 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,802 | 100.0% | 29% | 750 | 0.0% | 26% |
| 2023-12-06 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 17,523 | 100.0% | 27% | 602 | 0.0% | 25% |
| 2023-12-06 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 19,417 | 100.0% | 27% | 473 | 0.0% | 27% |
| 2023-12-06 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 8,476 | 100.0% | 43% | 432 | 0.0% | 37% |
| 2023-12-06 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 117 | 100.0% | 96% | 116 | 0.0% | 63% |
| 2023-12-06 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,542 | 100.0% | 36% | 3,541 | 0.1% | 30% |
| 2023-12-06 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,721 | 100.0% | 19% | 1,146 | 0.0% | 20% |
| 2023-12-06 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 12,382 | 100.0% | 25% | 731 | 0.0% | 24% |
| 2023-12-06 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,064 | 100.0% | 66% | 199 | 0.0% | 47% |
| 2023-12-06 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 13 | 100.0% | 92% | 121 | 0.0% | 54% |
| 2023-12-06 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 51,819 | 100.0% | 48% | 432 | 0.0% | 35% |
| 2023-12-06 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 48,163 | 100.0% | 50% | 400 | 0.0% | 35% |
| 2023-12-06 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 42,854 | 100.0% | 53% | 323 | 0.0% | 36% |
| 2023-12-06 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 21,790 | 100.0% | 62% | 212 | 0.0% | 41% |
| 2023-12-06 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 1,717 | 100.0% | 90% | 116 | 0.0% | 57% |
| 2023-12-06 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 22,711 | 100.0% | 28% | 1,293 | 0.0% | 27% |
| 2023-12-06 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 18,037 | 100.0% | 36% | 745 | 0.0% | 30% |
| 2023-12-06 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,410 | 100.0% | 47% | 446 | 0.0% | 35% |
| 2023-12-06 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 201 | 100.0% | 91% | 122 | 0.0% | 49% |
| 2023-12-06 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 8 | 100.0% | 100% | none resolved | 0.0% | 50% |
| 2023-12-06 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 65,838 | 100.0% | 40% | 548 | 0.0% | 31% |
| 2023-12-06 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 59,474 | 100.0% | 44% | 450 | 0.0% | 33% |
| 2023-12-06 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 45,900 | 100.0% | 48% | 338 | 0.0% | 36% |
| 2023-12-06 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 7,164 | 100.0% | 77% | 143 | 0.0% | 49% |
| 2023-12-06 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 372 | 100.0% | 92% | 116 | 0.0% | 58% |
| 2023-12-06 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 32,970 | 100.0% | 46% | 543 | 0.0% | 30% |
| 2023-12-06 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 39,951 | 100.0% | 43% | 460 | 0.0% | 29% |
| 2023-12-06 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 48,364 | 100.0% | 42% | 394 | 0.0% | 28% |
| 2023-12-06 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 65,602 | 100.0% | 44% | 300 | 0.0% | 30% |
| 2023-12-06 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 30,788 | 100.0% | 62% | 186 | 0.0% | 41% |
| 2023-12-06 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 26,241 | 100.0% | 33% | 626 | 0.0% | 40% |
| 2023-12-06 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 21,298 | 100.0% | 37% | 542 | 0.0% | 42% |
| 2023-12-06 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 16,238 | 100.0% | 41% | 491 | 0.0% | 44% |
| 2023-12-06 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,695 | 99.9% | 65% | 246 | 0.0% | 56% |
| 2023-12-06 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 369 | 100.0% | 91% | 116 | 0.0% | 63% |
| 2023-12-06 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,884 | 100.0% | 28% | 1,213 | 0.0% | 31% |
| 2023-12-06 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,884 | 100.0% | 28% | 1,213 | 0.0% | 31% |
| 2023-12-06 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,036 | 100.0% | 35% | 636 | 0.0% | 37% |
| 2023-12-06 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 942 | 100.0% | 75% | 136 | 0.2% | 54% |
| 2023-12-06 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 34 | 100.0% | 97% | 114 | 5.9% | 44% |
| 2023-12-06 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.949 below threshold | | | | | | | | |
| 2023-12-07 | aave_perp_binance_bybit | ok | 0.990 | gross>0bps | 19,038 | 99.9% | 37% | 764 | 0.0% | 37% |
| 2023-12-07 | aave_perp_binance_bybit | ok | 0.990 | gross>1bps | 19,038 | 99.9% | 37% | 764 | 0.0% | 37% |
| 2023-12-07 | aave_perp_binance_bybit | ok | 0.990 | gross>2bps | 12,536 | 99.9% | 43% | 670 | 0.0% | 42% |
| 2023-12-07 | aave_perp_binance_bybit | ok | 0.990 | gross>5bps | 1,335 | 100.0% | 75% | 196 | 0.0% | 55% |
| 2023-12-07 | aave_perp_binance_bybit | ok | 0.990 | retail_taker | 99 | 100.0% | 96% | 116 | 0.0% | 54% |
| 2023-12-07 | arb_perp_binance_bybit | ok | 0.993 | gross>0bps | 20,840 | 100.0% | 43% | 536 | 0.0% | 30% |
| 2023-12-07 | arb_perp_binance_bybit | ok | 0.993 | gross>1bps | 21,769 | 100.0% | 41% | 508 | 0.0% | 30% |
| 2023-12-07 | arb_perp_binance_bybit | ok | 0.993 | gross>2bps | 22,743 | 100.0% | 39% | 469 | 0.0% | 30% |
| 2023-12-07 | arb_perp_binance_bybit | ok | 0.993 | gross>5bps | 16,767 | 100.0% | 48% | 355 | 0.0% | 36% |
| 2023-12-07 | arb_perp_binance_bybit | ok | 0.993 | retail_taker | 1,052 | 100.0% | 94% | 113 | 0.0% | 57% |
| 2023-12-07 | btc_perp_binance_bybit | ok | 0.992 | gross>0bps | 3,598 | 99.9% | 36% | 2,000 | 0.0% | 28% |
| 2023-12-07 | btc_perp_binance_bybit | ok | 0.992 | gross>1bps | 4,883 | 100.0% | 29% | 962 | 0.0% | 23% |
| 2023-12-07 | btc_perp_binance_bybit | ok | 0.992 | gross>2bps | 6,081 | 100.0% | 30% | 768 | 0.0% | 24% |
| 2023-12-07 | btc_perp_binance_bybit | ok | 0.992 | gross>5bps | 3,865 | 100.0% | 40% | 398 | 0.0% | 33% |
| 2023-12-07 | btc_perp_binance_bybit | ok | 0.992 | retail_taker | 21 | 100.0% | 81% | 302 | 0.0% | 33% |
| 2023-12-07 | doge_perp_binance_bybit | ok | 0.991 | gross>0bps | 21,501 | 100.0% | 36% | 725 | 0.0% | 32% |
| 2023-12-07 | doge_perp_binance_bybit | ok | 0.991 | gross>1bps | 21,501 | 100.0% | 36% | 725 | 0.0% | 32% |
| 2023-12-07 | doge_perp_binance_bybit | ok | 0.991 | gross>2bps | 18,178 | 100.0% | 38% | 640 | 0.0% | 33% |
| 2023-12-07 | doge_perp_binance_bybit | ok | 0.991 | gross>5bps | 6,441 | 100.0% | 54% | 261 | 0.0% | 42% |
| 2023-12-07 | doge_perp_binance_bybit | ok | 0.991 | retail_taker | 147 | 100.0% | 90% | 121 | 0.0% | 58% |
| 2023-12-07 | eth_perp_binance_bybit | ok | 0.992 | gross>0bps | 6,687 | 100.0% | 34% | 2,344 | 0.1% | 29% |
| 2023-12-07 | eth_perp_binance_bybit | ok | 0.992 | gross>1bps | 9,702 | 100.0% | 23% | 1,124 | 0.0% | 23% |
| 2023-12-07 | eth_perp_binance_bybit | ok | 0.992 | gross>2bps | 11,872 | 100.0% | 28% | 564 | 0.0% | 26% |
| 2023-12-07 | eth_perp_binance_bybit | ok | 0.992 | gross>5bps | 2,950 | 100.0% | 58% | 194 | 0.1% | 40% |
| 2023-12-07 | eth_perp_binance_bybit | ok | 0.992 | retail_taker | 14 | 100.0% | 86% | 104 | 0.0% | 50% |
| 2023-12-07 | sol_perp_binance_bybit | ok | 0.995 | gross>0bps | 43,750 | 100.0% | 44% | 482 | 0.0% | 32% |
| 2023-12-07 | sol_perp_binance_bybit | ok | 0.995 | gross>1bps | 41,555 | 100.0% | 45% | 418 | 0.0% | 33% |
| 2023-12-07 | sol_perp_binance_bybit | ok | 0.995 | gross>2bps | 36,708 | 100.0% | 45% | 385 | 0.0% | 34% |
| 2023-12-07 | sol_perp_binance_bybit | ok | 0.995 | gross>5bps | 15,757 | 100.0% | 55% | 232 | 0.0% | 41% |
| 2023-12-07 | sol_perp_binance_bybit | ok | 0.995 | retail_taker | 416 | 100.0% | 86% | 122 | 0.0% | 57% |
| 2023-12-07 | tia_perp_binance_bybit | ok | 0.998 | gross>0bps | 23,681 | 100.0% | 55% | 581 | 0.0% | 34% |
| 2023-12-07 | tia_perp_binance_bybit | ok | 0.998 | gross>1bps | 31,487 | 100.0% | 53% | 497 | 0.0% | 33% |
| 2023-12-07 | tia_perp_binance_bybit | ok | 0.998 | gross>2bps | 42,497 | 100.0% | 53% | 410 | 0.0% | 32% |
| 2023-12-07 | tia_perp_binance_bybit | ok | 0.998 | gross>5bps | 66,452 | 100.0% | 58% | 310 | 0.0% | 35% |
| 2023-12-07 | tia_perp_binance_bybit | ok | 0.998 | retail_taker | 26,285 | 100.0% | 72% | 206 | 0.0% | 43% |
| 2023-12-07 | wld_perp_binance_bybit | ok | 0.994 | gross>0bps | 16,754 | 99.9% | 26% | 740 | 0.0% | 40% |
| 2023-12-07 | wld_perp_binance_bybit | ok | 0.994 | gross>1bps | 15,434 | 99.9% | 28% | 647 | 0.0% | 41% |
| 2023-12-07 | wld_perp_binance_bybit | ok | 0.994 | gross>2bps | 13,294 | 100.0% | 30% | 546 | 0.0% | 42% |
| 2023-12-07 | wld_perp_binance_bybit | ok | 0.994 | gross>5bps | 4,411 | 100.0% | 44% | 359 | 0.0% | 49% |
| 2023-12-07 | wld_perp_binance_bybit | ok | 0.994 | retail_taker | 171 | 100.0% | 89% | 114 | 0.0% | 70% |
| 2023-12-07 | xrp_perp_binance_bybit | ok | 0.990 | gross>0bps | 8,361 | 100.0% | 36% | 835 | 0.0% | 38% |
| 2023-12-07 | xrp_perp_binance_bybit | ok | 0.990 | gross>1bps | 8,361 | 100.0% | 36% | 835 | 0.0% | 38% |
| 2023-12-07 | xrp_perp_binance_bybit | ok | 0.990 | gross>2bps | 3,567 | 100.0% | 49% | 346 | 0.0% | 44% |
| 2023-12-07 | xrp_perp_binance_bybit | ok | 0.990 | gross>5bps | 337 | 100.0% | 86% | 117 | 0.0% | 56% |
| 2023-12-07 | xrp_perp_binance_bybit | ok | 0.990 | retail_taker | 39 | 100.0% | 100% | none resolved | 0.0% | 38% |
| 2023-12-07 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.932 below threshold | | | | | | | | |
| 2023-12-08 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 12,431 | 99.8% | 29% | 1,318 | 0.0% | 31% |
| 2023-12-08 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,986 | 99.8% | 30% | 1,294 | 0.0% | 32% |
| 2023-12-08 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,935 | 99.9% | 32% | 950 | 0.0% | 35% |
| 2023-12-08 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 5,576 | 99.9% | 43% | 435 | 0.0% | 39% |
| 2023-12-08 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 327 | 100.0% | 90% | 118 | 0.0% | 58% |
| 2023-12-08 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,540 | 100.0% | 27% | 1,036 | 0.0% | 27% |
| 2023-12-08 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,316 | 100.0% | 25% | 815 | 0.0% | 27% |
| 2023-12-08 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 13,662 | 100.0% | 26% | 656 | 0.0% | 28% |
| 2023-12-08 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 9,632 | 100.0% | 36% | 382 | 0.0% | 34% |
| 2023-12-08 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 359 | 100.0% | 73% | 241 | 0.0% | 48% |
| 2023-12-08 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,276 | 100.0% | 29% | 1,745 | 0.0% | 28% |
| 2023-12-08 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,398 | 100.0% | 29% | 1,076 | 0.0% | 25% |
| 2023-12-08 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,176 | 100.0% | 30% | 764 | 0.0% | 27% |
| 2023-12-08 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 735 | 100.0% | 58% | 250 | 0.0% | 43% |
| 2023-12-08 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 9 | 100.0% | 56% | 156 | 0.0% | 44% |
| 2023-12-08 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,979 | 100.0% | 24% | 996 | 0.0% | 25% |
| 2023-12-08 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,988 | 100.0% | 25% | 862 | 0.0% | 25% |
| 2023-12-08 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 13,104 | 100.0% | 25% | 693 | 0.0% | 26% |
| 2023-12-08 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 6,216 | 100.0% | 43% | 305 | 0.0% | 38% |
| 2023-12-08 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 200 | 100.0% | 89% | 114 | 0.0% | 52% |
| 2023-12-08 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,392 | 100.0% | 28% | 1,407 | 0.0% | 27% |
| 2023-12-08 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,295 | 100.0% | 30% | 1,669 | 0.0% | 27% |
| 2023-12-08 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,441 | 100.0% | 28% | 933 | 0.0% | 28% |
| 2023-12-08 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,637 | 100.0% | 54% | 322 | 0.0% | 39% |
| 2023-12-08 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 27 | 100.0% | 89% | 112 | 0.0% | 56% |
| 2023-12-08 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 34,746 | 100.0% | 42% | 621 | 0.0% | 32% |
| 2023-12-08 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 37,830 | 100.0% | 40% | 474 | 0.0% | 30% |
| 2023-12-08 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 41,084 | 100.0% | 39% | 379 | 0.0% | 30% |
| 2023-12-08 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 22,680 | 100.0% | 51% | 234 | 0.0% | 37% |
| 2023-12-08 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 480 | 100.0% | 89% | 111 | 0.0% | 56% |
| 2023-12-08 | tia_perp_binance_bybit | excluded: bybit_ob/bybit/TIA-USDT/perp coverage 1.000 below threshold | | | | | | | | |
| 2023-12-08 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,429 | 99.9% | 30% | 942 | 0.0% | 45% |
| 2023-12-08 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,791 | 100.0% | 34% | 778 | 0.0% | 47% |
| 2023-12-08 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,753 | 100.0% | 36% | 676 | 0.0% | 48% |
| 2023-12-08 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,240 | 100.0% | 49% | 332 | 0.0% | 51% |
| 2023-12-08 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 157 | 100.0% | 85% | 118 | 0.0% | 58% |
| 2023-12-08 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,432 | 100.0% | 26% | 1,370 | 0.0% | 33% |
| 2023-12-08 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,432 | 100.0% | 26% | 1,370 | 0.0% | 33% |
| 2023-12-08 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,626 | 100.0% | 37% | 610 | 0.0% | 39% |
| 2023-12-08 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 611 | 100.0% | 77% | 120 | 0.0% | 51% |
| 2023-12-08 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 58 | 100.0% | 98% | 104 | 0.0% | 45% |
| 2023-12-08 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.907 below threshold | | | | | | | | |
| 2023-12-09 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 18,790 | 99.9% | 38% | 622 | 0.0% | 30% |
| 2023-12-09 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 18,452 | 99.9% | 39% | 538 | 0.0% | 32% |
| 2023-12-09 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 17,344 | 99.9% | 42% | 460 | 0.0% | 35% |
| 2023-12-09 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 9,081 | 99.8% | 49% | 532 | 0.0% | 41% |
| 2023-12-09 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 530 | 100.0% | 84% | 166 | 0.0% | 58% |
| 2023-12-09 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 18,605 | 100.0% | 45% | 602 | 0.0% | 32% |
| 2023-12-09 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 18,472 | 100.0% | 43% | 558 | 0.0% | 31% |
| 2023-12-09 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 18,211 | 100.0% | 41% | 534 | 0.0% | 31% |
| 2023-12-09 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 14,660 | 100.0% | 40% | 487 | 0.0% | 33% |
| 2023-12-09 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 1,011 | 100.0% | 85% | 156 | 0.0% | 51% |
| 2023-12-09 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,800 | 100.0% | 27% | 2,691 | 0.0% | 28% |
| 2023-12-09 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,839 | 100.0% | 27% | 2,495 | 0.0% | 27% |
| 2023-12-09 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,030 | 100.0% | 30% | 1,899 | 0.0% | 28% |
| 2023-12-09 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,128 | 100.0% | 37% | 839 | 0.0% | 33% |
| 2023-12-09 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 5 | 100.0% | 40% | 514 | 0.0% | 40% |
| 2023-12-09 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 16,635 | 100.0% | 36% | 700 | 0.0% | 33% |
| 2023-12-09 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 15,325 | 100.0% | 39% | 616 | 0.0% | 34% |
| 2023-12-09 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,916 | 100.0% | 41% | 584 | 0.0% | 35% |
| 2023-12-09 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,073 | 100.0% | 47% | 541 | 0.0% | 39% |
| 2023-12-09 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 371 | 100.0% | 77% | 168 | 0.0% | 51% |
| 2023-12-09 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,904 | 100.0% | 31% | 2,534 | 0.0% | 28% |
| 2023-12-09 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,980 | 100.0% | 26% | 2,126 | 0.0% | 27% |
| 2023-12-09 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,943 | 100.0% | 34% | 1,089 | 0.0% | 31% |
| 2023-12-09 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 883 | 100.0% | 76% | 154 | 0.1% | 46% |
| 2023-12-09 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 21 | 100.0% | 90% | 109 | 0.0% | 62% |
| 2023-12-09 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,569 | 100.0% | 47% | 976 | 0.0% | 34% |
| 2023-12-09 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 17,797 | 100.0% | 39% | 665 | 0.0% | 29% |
| 2023-12-09 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 25,380 | 100.0% | 36% | 510 | 0.0% | 29% |
| 2023-12-09 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 29,804 | 100.0% | 44% | 302 | 0.0% | 33% |
| 2023-12-09 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 1,332 | 100.0% | 82% | 144 | 0.0% | 49% |
| 2023-12-09 | tia_perp_binance_bybit | excluded: bybit_ob/bybit/TIA-USDT/perp coverage 1.000 below threshold | | | | | | | | |
| 2023-12-09 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 15,484 | 99.9% | 29% | 810 | 0.0% | 41% |
| 2023-12-09 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 14,129 | 99.9% | 31% | 753 | 0.0% | 43% |
| 2023-12-09 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,829 | 99.9% | 33% | 658 | 0.0% | 45% |
| 2023-12-09 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 5,117 | 99.9% | 41% | 494 | 0.0% | 50% |
| 2023-12-09 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 409 | 100.0% | 79% | 159 | 0.0% | 57% |
| 2023-12-09 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 12,155 | 100.0% | 42% | 586 | 0.0% | 36% |
| 2023-12-09 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,155 | 100.0% | 42% | 586 | 0.0% | 36% |
| 2023-12-09 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,566 | 100.0% | 51% | 505 | 0.0% | 38% |
| 2023-12-09 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,442 | 100.0% | 53% | 310 | 0.0% | 40% |
| 2023-12-09 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 260 | 100.0% | 90% | 132 | 0.0% | 53% |
| 2023-12-09 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.913 below threshold | | | | | | | | |
| 2023-12-10 | aave_perp_binance_bybit | ok | 0.999 | gross>0bps | 3,375 | 98.0% | 23% | 2,806 | 0.0% | 25% |
| 2023-12-10 | aave_perp_binance_bybit | ok | 0.999 | gross>1bps | 3,375 | 98.0% | 23% | 2,806 | 0.0% | 25% |
| 2023-12-10 | aave_perp_binance_bybit | ok | 0.999 | gross>2bps | 6,386 | 99.0% | 21% | 1,456 | 0.0% | 26% |
| 2023-12-10 | aave_perp_binance_bybit | ok | 0.999 | gross>5bps | 10,151 | 99.6% | 36% | 622 | 0.0% | 35% |
| 2023-12-10 | aave_perp_binance_bybit | ok | 0.999 | retail_taker | 158 | 100.0% | 94% | 124 | 0.0% | 69% |
| 2023-12-10 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,735 | 100.0% | 23% | 1,483 | 0.0% | 28% |
| 2023-12-10 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,189 | 100.0% | 22% | 1,131 | 0.0% | 28% |
| 2023-12-10 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,579 | 100.0% | 23% | 1,002 | 0.0% | 30% |
| 2023-12-10 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 5,021 | 100.0% | 35% | 492 | 0.0% | 36% |
| 2023-12-10 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 93 | 100.0% | 95% | 105 | 0.0% | 65% |
| 2023-12-10 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 996 | 99.9% | 30% | 11,685 | 0.1% | 29% |
| 2023-12-10 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,592 | 99.9% | 17% | 3,812 | 0.1% | 21% |
| 2023-12-10 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,197 | 100.0% | 23% | 2,459 | 0.0% | 25% |
| 2023-12-10 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 604 | 100.0% | 36% | 1,249 | 0.0% | 34% |
| 2023-12-10 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 5 | 100.0% | 80% | 123 | 0.0% | 80% |
| 2023-12-10 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,926 | 100.0% | 29% | 1,140 | 0.0% | 32% |
| 2023-12-10 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,649 | 100.0% | 30% | 1,005 | 0.0% | 33% |
| 2023-12-10 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,921 | 100.0% | 35% | 698 | 0.0% | 37% |
| 2023-12-10 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,494 | 100.0% | 62% | 314 | 0.0% | 50% |
| 2023-12-10 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 56 | 100.0% | 86% | 139 | 0.0% | 64% |
| 2023-12-10 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,453 | 100.0% | 24% | 2,976 | 0.0% | 28% |
| 2023-12-10 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,571 | 100.0% | 28% | 3,043 | 0.0% | 31% |
| 2023-12-10 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,260 | 100.0% | 34% | 1,460 | 0.0% | 36% |
| 2023-12-10 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 81 | 100.0% | 85% | 119 | 0.0% | 54% |
| 2023-12-10 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2023-12-10 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 25,511 | 100.0% | 38% | 847 | 0.0% | 32% |
| 2023-12-10 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 27,205 | 100.0% | 35% | 554 | 0.0% | 30% |
| 2023-12-10 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 26,888 | 100.0% | 37% | 452 | 0.0% | 31% |
| 2023-12-10 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 7,564 | 100.0% | 59% | 218 | 0.0% | 44% |
| 2023-12-10 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 106 | 100.0% | 90% | 111 | 0.0% | 50% |
| 2023-12-10 | tia_perp_binance_bybit | excluded: bybit_ob/bybit/TIA-USDT/perp coverage 1.000 below threshold | | | | | | | | |
| 2023-12-10 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 18,087 | 100.0% | 28% | 851 | 0.0% | 39% |
| 2023-12-10 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 17,318 | 100.0% | 28% | 744 | 0.0% | 40% |
| 2023-12-10 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 15,518 | 100.0% | 29% | 635 | 0.0% | 42% |
| 2023-12-10 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 9,251 | 100.0% | 36% | 458 | 0.0% | 45% |
| 2023-12-10 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 1,585 | 100.0% | 54% | 288 | 0.0% | 51% |
| 2023-12-10 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,228 | 100.0% | 30% | 1,054 | 0.0% | 39% |
| 2023-12-10 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,228 | 100.0% | 30% | 1,054 | 0.0% | 39% |
| 2023-12-10 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,522 | 100.0% | 39% | 556 | 0.0% | 44% |
| 2023-12-10 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 426 | 100.0% | 66% | 217 | 0.0% | 45% |
| 2023-12-10 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 33 | 100.0% | 94% | 104 | 0.0% | 42% |
| 2023-12-10 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.923 below threshold | | | | | | | | |
| 2023-12-11 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 12,112 | 99.9% | 36% | 849 | 0.0% | 24% |
| 2023-12-11 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,112 | 99.9% | 36% | 849 | 0.0% | 24% |
| 2023-12-11 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 18,149 | 99.9% | 35% | 620 | 0.0% | 25% |
| 2023-12-11 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 25,779 | 100.0% | 41% | 436 | 0.0% | 31% |
| 2023-12-11 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 1,558 | 100.0% | 79% | 188 | 0.0% | 50% |
| 2023-12-11 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 36,479 | 100.0% | 44% | 503 | 0.1% | 32% |
| 2023-12-11 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 32,218 | 100.0% | 45% | 458 | 0.1% | 33% |
| 2023-12-11 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 27,793 | 100.0% | 45% | 408 | 0.1% | 35% |
| 2023-12-11 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 10,511 | 100.0% | 62% | 253 | 0.1% | 44% |
| 2023-12-11 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 784 | 100.0% | 82% | 228 | 0.4% | 44% |
| 2023-12-11 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,744 | 100.0% | 48% | 520 | 0.2% | 30% |
| 2023-12-11 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,020 | 100.0% | 46% | 483 | 0.3% | 29% |
| 2023-12-11 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 12,824 | 100.0% | 42% | 541 | 0.3% | 28% |
| 2023-12-11 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 7,717 | 100.0% | 46% | 449 | 0.4% | 32% |
| 2023-12-11 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 1,821 | 100.0% | 63% | 298 | 1.2% | 42% |
| 2023-12-11 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 46,951 | 100.0% | 49% | 434 | 0.0% | 32% |
| 2023-12-11 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 45,767 | 100.0% | 49% | 424 | 0.0% | 32% |
| 2023-12-11 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 42,672 | 100.0% | 50% | 370 | 0.0% | 34% |
| 2023-12-11 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 18,249 | 100.0% | 64% | 267 | 0.0% | 42% |
| 2023-12-11 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 1,724 | 100.0% | 84% | 160 | 0.0% | 46% |
| 2023-12-11 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,987 | 100.0% | 44% | 1,081 | 0.0% | 30% |
| 2023-12-11 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,121 | 100.0% | 34% | 1,004 | 0.0% | 24% |
| 2023-12-11 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 16,176 | 100.0% | 30% | 682 | 0.0% | 23% |
| 2023-12-11 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 11,413 | 100.0% | 48% | 363 | 0.0% | 33% |
| 2023-12-11 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 1,069 | 100.0% | 80% | 164 | 0.0% | 40% |
| 2023-12-11 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 47,323 | 100.0% | 52% | 444 | 0.1% | 32% |
| 2023-12-11 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 53,639 | 100.0% | 47% | 388 | 0.1% | 30% |
| 2023-12-11 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 62,287 | 100.0% | 44% | 335 | 0.1% | 29% |
| 2023-12-11 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 34,478 | 100.0% | 55% | 238 | 0.1% | 39% |
| 2023-12-11 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 1,469 | 100.0% | 85% | 162 | 0.4% | 51% |
| 2023-12-11 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 15,413 | 100.0% | 47% | 906 | 0.0% | 32% |
| 2023-12-11 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 20,164 | 100.0% | 43% | 691 | 0.0% | 29% |
| 2023-12-11 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 27,397 | 100.0% | 40% | 538 | 0.0% | 27% |
| 2023-12-11 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 54,128 | 100.0% | 41% | 338 | 0.0% | 27% |
| 2023-12-11 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 47,418 | 100.0% | 51% | 254 | 0.0% | 34% |
| 2023-12-11 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 31,131 | 100.0% | 34% | 430 | 0.0% | 37% |
| 2023-12-11 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 27,989 | 100.0% | 36% | 374 | 0.0% | 37% |
| 2023-12-11 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 24,464 | 100.0% | 38% | 338 | 0.0% | 38% |
| 2023-12-11 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 13,294 | 100.0% | 46% | 297 | 0.0% | 40% |
| 2023-12-11 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 1,847 | 100.0% | 75% | 198 | 0.0% | 45% |
| 2023-12-11 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,929 | 100.0% | 33% | 726 | 0.0% | 28% |
| 2023-12-11 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 14,929 | 100.0% | 33% | 726 | 0.0% | 28% |
| 2023-12-11 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 14,470 | 100.0% | 36% | 554 | 0.0% | 35% |
| 2023-12-11 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,848 | 100.0% | 69% | 259 | 0.0% | 46% |
| 2023-12-11 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 885 | 100.0% | 76% | 186 | 0.0% | 40% |
| 2023-12-11 | zec_perp_binance_bybit | ok | 0.999 | gross>0bps | 12,999 | 99.5% | 24% | 437 | 0.0% | 30% |
| 2023-12-11 | zec_perp_binance_bybit | ok | 0.999 | gross>1bps | 12,999 | 99.5% | 24% | 437 | 0.0% | 30% |
| 2023-12-11 | zec_perp_binance_bybit | ok | 0.999 | gross>2bps | 12,999 | 99.5% | 24% | 437 | 0.0% | 30% |
| 2023-12-11 | zec_perp_binance_bybit | ok | 0.999 | gross>5bps | 5,615 | 99.5% | 33% | 450 | 0.0% | 37% |
| 2023-12-11 | zec_perp_binance_bybit | ok | 0.999 | retail_taker | 453 | 99.8% | 64% | 250 | 0.0% | 52% |
| 2023-12-12 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,348 | 98.9% | 17% | 2,714 | 0.0% | 21% |
| 2023-12-12 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,348 | 98.9% | 17% | 2,714 | 0.0% | 21% |
| 2023-12-12 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,703 | 99.5% | 16% | 1,206 | 0.0% | 21% |
| 2023-12-12 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 14,304 | 99.9% | 32% | 468 | 0.0% | 31% |
| 2023-12-12 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 1,086 | 99.9% | 55% | 604 | 0.0% | 47% |
| 2023-12-12 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 25,448 | 100.0% | 38% | 580 | 0.0% | 31% |
| 2023-12-12 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 24,219 | 100.0% | 38% | 481 | 0.0% | 31% |
| 2023-12-12 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 22,591 | 100.0% | 40% | 417 | 0.0% | 32% |
| 2023-12-12 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 13,190 | 100.0% | 48% | 311 | 0.0% | 36% |
| 2023-12-12 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 1,016 | 100.0% | 77% | 193 | 0.0% | 48% |
| 2023-12-12 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 9,899 | 100.0% | 32% | 1,356 | 0.0% | 29% |
| 2023-12-12 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,093 | 100.0% | 33% | 1,130 | 0.0% | 27% |
| 2023-12-12 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 9,760 | 100.0% | 32% | 1,045 | 0.0% | 27% |
| 2023-12-12 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,189 | 100.0% | 62% | 287 | 0.0% | 44% |
| 2023-12-12 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 16 | 100.0% | 94% | 123 | 0.0% | 44% |
| 2023-12-12 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 15,057 | 100.0% | 28% | 1,011 | 0.0% | 29% |
| 2023-12-12 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 15,057 | 100.0% | 28% | 1,011 | 0.0% | 29% |
| 2023-12-12 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 15,253 | 100.0% | 28% | 804 | 0.0% | 30% |
| 2023-12-12 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 6,308 | 100.0% | 49% | 332 | 0.0% | 45% |
| 2023-12-12 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 153 | 100.0% | 97% | 164 | 0.0% | 56% |
| 2023-12-12 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 16,575 | 100.0% | 29% | 914 | 0.0% | 28% |
| 2023-12-12 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,002 | 100.0% | 40% | 694 | 0.0% | 33% |
| 2023-12-12 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,347 | 100.0% | 40% | 1,312 | 0.0% | 31% |
| 2023-12-12 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 921 | 100.0% | 71% | 200 | 0.0% | 51% |
| 2023-12-12 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 12 | 100.0% | 83% | 129 | 0.0% | 67% |
| 2023-12-12 | sol_perp_binance_bybit | excluded: bybit_ob/bybit/SOL-USDT/perp coverage 1.000 below threshold | | | | | | | | |
| 2023-12-12 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 23,737 | 100.0% | 46% | 518 | 0.0% | 31% |
| 2023-12-12 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 31,101 | 100.0% | 43% | 405 | 0.0% | 29% |
| 2023-12-12 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 40,705 | 100.0% | 41% | 337 | 0.0% | 28% |
| 2023-12-12 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 61,990 | 100.0% | 47% | 258 | 0.0% | 31% |
| 2023-12-12 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 44,579 | 100.0% | 56% | 218 | 0.0% | 35% |
| 2023-12-12 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,763 | 99.8% | 22% | 847 | 0.0% | 35% |
| 2023-12-12 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,866 | 99.8% | 23% | 750 | 0.0% | 36% |
| 2023-12-12 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 13,397 | 99.8% | 23% | 709 | 0.0% | 37% |
| 2023-12-12 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 8,815 | 99.9% | 30% | 559 | 0.0% | 44% |
| 2023-12-12 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 510 | 100.0% | 71% | 190 | 0.0% | 65% |
| 2023-12-12 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,037 | 100.0% | 21% | 1,524 | 0.0% | 29% |
| 2023-12-12 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,037 | 100.0% | 21% | 1,524 | 0.0% | 29% |
| 2023-12-12 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,696 | 100.0% | 18% | 1,902 | 0.0% | 28% |
| 2023-12-12 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,923 | 100.0% | 43% | 456 | 0.0% | 49% |
| 2023-12-12 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 26 | 100.0% | 88% | 105 | 0.0% | 58% |
| 2023-12-12 | zec_perp_binance_bybit | ok | 0.998 | gross>0bps | 9,673 | 98.9% | 20% | 601 | 0.0% | 26% |
| 2023-12-12 | zec_perp_binance_bybit | ok | 0.998 | gross>1bps | 9,673 | 98.9% | 20% | 601 | 0.0% | 26% |
| 2023-12-12 | zec_perp_binance_bybit | ok | 0.998 | gross>2bps | 9,673 | 98.9% | 20% | 601 | 0.0% | 26% |
| 2023-12-12 | zec_perp_binance_bybit | ok | 0.998 | gross>5bps | 4,142 | 99.6% | 34% | 262 | 0.0% | 38% |
| 2023-12-12 | zec_perp_binance_bybit | ok | 0.998 | retail_taker | 99 | 100.0% | 85% | 136 | 0.0% | 69% |
| 2023-12-13 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,954 | 99.5% | 23% | 1,007 | 0.0% | 21% |
| 2023-12-13 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,954 | 99.5% | 23% | 1,007 | 0.0% | 21% |
| 2023-12-13 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 15,853 | 99.7% | 25% | 568 | 0.0% | 25% |
| 2023-12-13 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 11,015 | 99.9% | 41% | 432 | 0.0% | 39% |
| 2023-12-13 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 226 | 100.0% | 93% | 114 | 0.0% | 69% |
| 2023-12-13 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 25,617 | 100.0% | 37% | 624 | 0.0% | 31% |
| 2023-12-13 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 25,213 | 100.0% | 38% | 515 | 0.0% | 31% |
| 2023-12-13 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 23,107 | 100.0% | 40% | 413 | 0.0% | 33% |
| 2023-12-13 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 12,971 | 100.0% | 48% | 280 | 0.1% | 39% |
| 2023-12-13 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 639 | 100.0% | 89% | 120 | 0.0% | 58% |
| 2023-12-13 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,150 | 100.0% | 31% | 1,456 | 0.1% | 29% |
| 2023-12-13 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,458 | 100.0% | 37% | 893 | 0.0% | 31% |
| 2023-12-13 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,264 | 100.0% | 37% | 779 | 0.0% | 31% |
| 2023-12-13 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 5,176 | 100.0% | 42% | 355 | 0.0% | 34% |
| 2023-12-13 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 54 | 100.0% | 81% | 138 | 1.9% | 43% |
| 2023-12-13 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,502 | 100.0% | 33% | 991 | 0.0% | 32% |
| 2023-12-13 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 14,502 | 100.0% | 33% | 991 | 0.0% | 32% |
| 2023-12-13 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 13,244 | 100.0% | 33% | 935 | 0.0% | 33% |
| 2023-12-13 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 6,275 | 100.0% | 44% | 438 | 0.0% | 40% |
| 2023-12-13 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 177 | 100.0% | 90% | 114 | 0.0% | 57% |
| 2023-12-13 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 15,591 | 100.0% | 32% | 1,460 | 0.0% | 29% |
| 2023-12-13 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 15,706 | 100.0% | 33% | 1,038 | 0.0% | 29% |
| 2023-12-13 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,060 | 100.0% | 39% | 590 | 0.0% | 32% |
| 2023-12-13 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 992 | 100.0% | 79% | 129 | 0.0% | 47% |
| 2023-12-13 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 31 | 100.0% | 97% | 137 | 0.0% | 32% |
| 2023-12-13 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,396 | 100.0% | 47% | 881 | 0.0% | 33% |
| 2023-12-13 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 18,173 | 100.0% | 40% | 718 | 0.0% | 29% |
| 2023-12-13 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 25,697 | 100.0% | 38% | 531 | 0.0% | 28% |
| 2023-12-13 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 31,337 | 100.0% | 48% | 287 | 0.0% | 34% |
| 2023-12-13 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 5,535 | 100.0% | 55% | 260 | 0.2% | 37% |
| 2023-12-13 | tia_perp_binance_bybit | excluded: bybit_ob/bybit/TIA-USDT/perp coverage 1.000 below threshold | | | | | | | | |
| 2023-12-13 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 22,087 | 99.9% | 37% | 634 | 0.0% | 39% |
| 2023-12-13 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 22,999 | 99.9% | 37% | 537 | 0.0% | 39% |
| 2023-12-13 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 22,495 | 99.9% | 37% | 459 | 0.0% | 40% |
| 2023-12-13 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 13,978 | 100.0% | 47% | 336 | 0.0% | 45% |
| 2023-12-13 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 1,777 | 100.0% | 83% | 142 | 0.0% | 57% |
| 2023-12-13 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,918 | 100.0% | 29% | 1,041 | 0.0% | 34% |
| 2023-12-13 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,918 | 100.0% | 29% | 1,041 | 0.0% | 34% |
| 2023-12-13 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,847 | 100.0% | 34% | 902 | 0.0% | 39% |
| 2023-12-13 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,570 | 100.0% | 39% | 626 | 0.0% | 39% |
| 2023-12-13 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 61 | 100.0% | 97% | 372 | 0.0% | 57% |
| 2023-12-13 | zec_perp_binance_bybit | ok | 0.997 | gross>0bps | 11,615 | 98.9% | 22% | 352 | 0.0% | 24% |
| 2023-12-13 | zec_perp_binance_bybit | ok | 0.997 | gross>1bps | 11,615 | 98.9% | 22% | 352 | 0.0% | 24% |
| 2023-12-13 | zec_perp_binance_bybit | ok | 0.997 | gross>2bps | 11,615 | 98.9% | 22% | 352 | 0.0% | 24% |
| 2023-12-13 | zec_perp_binance_bybit | ok | 0.997 | gross>5bps | 3,704 | 99.4% | 36% | 258 | 0.2% | 35% |
| 2023-12-13 | zec_perp_binance_bybit | ok | 0.997 | retail_taker | 59 | 100.0% | 90% | 125 | 0.0% | 81% |
| 2023-12-14 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,964 | 99.8% | 34% | 580 | 0.0% | 27% |
| 2023-12-14 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 15,634 | 99.8% | 35% | 524 | 0.0% | 27% |
| 2023-12-14 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 17,137 | 99.8% | 36% | 426 | 0.0% | 29% |
| 2023-12-14 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 10,550 | 99.9% | 41% | 440 | 0.0% | 33% |
| 2023-12-14 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 990 | 100.0% | 76% | 262 | 0.0% | 48% |
| 2023-12-14 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 18,232 | 100.0% | 34% | 752 | 0.0% | 29% |
| 2023-12-14 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 17,651 | 100.0% | 35% | 632 | 0.0% | 29% |
| 2023-12-14 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 16,300 | 100.0% | 35% | 514 | 0.0% | 31% |
| 2023-12-14 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 6,035 | 100.0% | 54% | 347 | 0.0% | 40% |
| 2023-12-14 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 376 | 100.0% | 80% | 203 | 0.0% | 42% |
| 2023-12-14 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,176 | 99.9% | 51% | 1,252 | 0.1% | 35% |
| 2023-12-14 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,711 | 99.9% | 40% | 806 | 0.1% | 29% |
| 2023-12-14 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,272 | 99.9% | 41% | 901 | 0.1% | 28% |
| 2023-12-14 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 9,416 | 100.0% | 33% | 742 | 0.0% | 27% |
| 2023-12-14 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 619 | 100.0% | 86% | 197 | 0.5% | 45% |
| 2023-12-14 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,714 | 100.0% | 30% | 1,163 | 0.0% | 25% |
| 2023-12-14 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,714 | 100.0% | 30% | 1,163 | 0.0% | 25% |
| 2023-12-14 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,766 | 100.0% | 26% | 1,026 | 0.0% | 24% |
| 2023-12-14 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 9,204 | 100.0% | 30% | 773 | 0.0% | 32% |
| 2023-12-14 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 328 | 100.0% | 82% | 168 | 0.0% | 45% |
| 2023-12-14 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 794 | 99.7% | 54% | 5,953 | 0.1% | 39% |
| 2023-12-14 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,430 | 99.9% | 32% | 5,952 | 0.1% | 21% |
| 2023-12-14 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,003 | 100.0% | 22% | 2,020 | 0.0% | 21% |
| 2023-12-14 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 10,209 | 100.0% | 34% | 630 | 0.0% | 27% |
| 2023-12-14 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 290 | 100.0% | 83% | 220 | 0.3% | 45% |
| 2023-12-14 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,295 | 100.0% | 60% | 1,962 | 0.0% | 36% |
| 2023-12-14 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,977 | 100.0% | 47% | 1,392 | 0.1% | 31% |
| 2023-12-14 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,223 | 100.0% | 37% | 943 | 0.0% | 28% |
| 2023-12-14 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 30,978 | 100.0% | 39% | 422 | 0.0% | 30% |
| 2023-12-14 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 10,625 | 100.0% | 58% | 262 | 0.0% | 37% |
| 2023-12-14 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,064 | 100.0% | 46% | 938 | 0.0% | 33% |
| 2023-12-14 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 17,658 | 100.0% | 41% | 650 | 0.0% | 29% |
| 2023-12-14 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 24,954 | 100.0% | 38% | 512 | 0.0% | 27% |
| 2023-12-14 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 49,959 | 100.0% | 40% | 324 | 0.0% | 28% |
| 2023-12-14 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 30,346 | 100.0% | 54% | 231 | 0.0% | 36% |
| 2023-12-14 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,577 | 99.9% | 29% | 811 | 0.0% | 40% |
| 2023-12-14 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 14,202 | 99.9% | 30% | 681 | 0.0% | 40% |
| 2023-12-14 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 13,244 | 99.9% | 31% | 590 | 0.0% | 40% |
| 2023-12-14 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 8,807 | 100.0% | 37% | 441 | 0.0% | 41% |
| 2023-12-14 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 910 | 100.0% | 74% | 211 | 0.0% | 51% |
| 2023-12-14 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,707 | 100.0% | 33% | 1,885 | 0.0% | 31% |
| 2023-12-14 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,707 | 100.0% | 33% | 1,885 | 0.0% | 31% |
| 2023-12-14 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,217 | 100.0% | 33% | 1,445 | 0.0% | 35% |
| 2023-12-14 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,570 | 100.0% | 62% | 298 | 0.0% | 44% |
| 2023-12-14 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 321 | 100.0% | 79% | 216 | 0.0% | 43% |
| 2023-12-14 | zec_perp_binance_bybit | ok | 0.996 | gross>0bps | 9,171 | 97.9% | 21% | 590 | 0.0% | 28% |
| 2023-12-14 | zec_perp_binance_bybit | ok | 0.996 | gross>1bps | 9,171 | 97.9% | 21% | 590 | 0.0% | 28% |
| 2023-12-14 | zec_perp_binance_bybit | ok | 0.996 | gross>2bps | 9,171 | 97.9% | 21% | 590 | 0.0% | 28% |
| 2023-12-14 | zec_perp_binance_bybit | ok | 0.996 | gross>5bps | 5,533 | 98.6% | 27% | 632 | 0.0% | 35% |
| 2023-12-14 | zec_perp_binance_bybit | ok | 0.996 | retail_taker | 307 | 100.0% | 62% | 240 | 0.0% | 61% |
| 2023-12-15 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 39,392 | 100.0% | 44% | 438 | 0.0% | 31% |
| 2023-12-15 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 33,532 | 100.0% | 47% | 362 | 0.0% | 33% |
| 2023-12-15 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 26,740 | 100.0% | 51% | 327 | 0.0% | 36% |
| 2023-12-15 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 11,561 | 100.0% | 55% | 312 | 0.0% | 37% |
| 2023-12-15 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 1,362 | 100.0% | 82% | 131 | 0.0% | 50% |
| 2023-12-15 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,852 | 100.0% | 26% | 1,158 | 0.1% | 28% |
| 2023-12-15 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,704 | 100.0% | 26% | 842 | 0.1% | 28% |
| 2023-12-15 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,838 | 100.0% | 28% | 670 | 0.1% | 28% |
| 2023-12-15 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,363 | 100.0% | 49% | 345 | 0.2% | 41% |
| 2023-12-15 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 103 | 100.0% | 89% | 198 | 1.9% | 51% |
| 2023-12-15 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 9,297 | 100.0% | 30% | 1,228 | 0.2% | 28% |
| 2023-12-15 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,110 | 100.0% | 37% | 987 | 0.4% | 33% |
| 2023-12-15 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,182 | 100.0% | 36% | 1,277 | 0.5% | 31% |
| 2023-12-15 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,555 | 100.0% | 41% | 664 | 0.5% | 38% |
| 2023-12-15 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 20 | 100.0% | 75% | 444 | 5.0% | 40% |
| 2023-12-15 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 9,741 | 100.0% | 26% | 1,192 | 0.0% | 31% |
| 2023-12-15 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,741 | 100.0% | 26% | 1,192 | 0.0% | 31% |
| 2023-12-15 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,509 | 100.0% | 28% | 865 | 0.0% | 32% |
| 2023-12-15 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,756 | 100.0% | 53% | 364 | 0.0% | 46% |
| 2023-12-15 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 44 | 100.0% | 86% | 126 | 0.0% | 59% |
| 2023-12-15 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 9,420 | 100.0% | 31% | 1,010 | 0.0% | 28% |
| 2023-12-15 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,333 | 100.0% | 31% | 777 | 0.0% | 27% |
| 2023-12-15 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,365 | 100.0% | 34% | 913 | 0.0% | 29% |
| 2023-12-15 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,203 | 100.0% | 71% | 234 | 0.0% | 45% |
| 2023-12-15 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 37 | 100.0% | 81% | 311 | 0.0% | 43% |
| 2023-12-15 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 12,821 | 100.0% | 47% | 786 | 0.1% | 33% |
| 2023-12-15 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 18,340 | 100.0% | 39% | 480 | 0.1% | 28% |
| 2023-12-15 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 25,311 | 100.0% | 40% | 391 | 0.1% | 28% |
| 2023-12-15 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 33,558 | 100.0% | 43% | 334 | 0.1% | 30% |
| 2023-12-15 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 2,105 | 100.0% | 78% | 138 | 0.1% | 48% |
| 2023-12-15 | tia_perp_binance_bybit | excluded: bybit_ob/bybit/TIA-USDT/perp coverage 1.000 below threshold | | | | | | | | |
| 2023-12-15 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 12,598 | 100.0% | 26% | 944 | 0.0% | 39% |
| 2023-12-15 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,887 | 100.0% | 26% | 795 | 0.0% | 40% |
| 2023-12-15 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 12,575 | 100.0% | 27% | 664 | 0.0% | 42% |
| 2023-12-15 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 8,507 | 100.0% | 33% | 560 | 0.0% | 45% |
| 2023-12-15 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 1,091 | 100.0% | 57% | 251 | 0.0% | 57% |
| 2023-12-15 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,257 | 100.0% | 18% | 1,627 | 0.0% | 29% |
| 2023-12-15 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,257 | 100.0% | 18% | 1,627 | 0.0% | 29% |
| 2023-12-15 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,683 | 100.0% | 28% | 1,012 | 0.0% | 38% |
| 2023-12-15 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 648 | 100.0% | 68% | 207 | 0.0% | 53% |
| 2023-12-15 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 37 | 100.0% | 100% | none resolved | 0.0% | 54% |
| 2023-12-15 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.941 below threshold | | | | | | | | |
| 2023-12-16 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,433 | 99.8% | 30% | 922 | 0.0% | 27% |
| 2023-12-16 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,514 | 99.9% | 30% | 634 | 0.0% | 27% |
| 2023-12-16 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 12,778 | 99.9% | 33% | 617 | 0.0% | 31% |
| 2023-12-16 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 7,774 | 100.0% | 38% | 461 | 0.0% | 34% |
| 2023-12-16 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 307 | 100.0% | 89% | 130 | 0.0% | 63% |
| 2023-12-16 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,771 | 100.0% | 24% | 2,197 | 0.1% | 27% |
| 2023-12-16 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,542 | 100.0% | 21% | 1,560 | 0.0% | 28% |
| 2023-12-16 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,313 | 100.0% | 23% | 1,154 | 0.0% | 29% |
| 2023-12-16 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 5,243 | 100.0% | 37% | 637 | 0.0% | 36% |
| 2023-12-16 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 226 | 100.0% | 92% | 200 | 0.0% | 47% |
| 2023-12-16 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,095 | 99.9% | 37% | 6,604 | 0.0% | 30% |
| 2023-12-16 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,349 | 100.0% | 19% | 2,686 | 0.0% | 21% |
| 2023-12-16 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,001 | 100.0% | 23% | 1,919 | 0.0% | 24% |
| 2023-12-16 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 966 | 100.0% | 43% | 490 | 0.1% | 35% |
| 2023-12-16 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 7 | 100.0% | 86% | 117 | 0.0% | 43% |
| 2023-12-16 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,013 | 100.0% | 34% | 928 | 0.0% | 35% |
| 2023-12-16 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,013 | 100.0% | 34% | 928 | 0.0% | 35% |
| 2023-12-16 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,458 | 100.0% | 36% | 978 | 0.0% | 38% |
| 2023-12-16 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 883 | 100.0% | 61% | 231 | 0.0% | 53% |
| 2023-12-16 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 21 | 100.0% | 90% | 124 | 0.0% | 67% |
| 2023-12-16 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,582 | 100.0% | 28% | 2,406 | 0.0% | 27% |
| 2023-12-16 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,692 | 100.0% | 27% | 1,412 | 0.0% | 27% |
| 2023-12-16 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,092 | 100.0% | 30% | 961 | 0.0% | 32% |
| 2023-12-16 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 113 | 100.0% | 89% | 110 | 0.0% | 58% |
| 2023-12-16 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2023-12-16 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,719 | 100.0% | 39% | 979 | 0.0% | 32% |
| 2023-12-16 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,416 | 100.0% | 36% | 737 | 0.0% | 30% |
| 2023-12-16 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 9,679 | 100.0% | 34% | 634 | 0.0% | 28% |
| 2023-12-16 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 14,862 | 100.0% | 38% | 457 | 0.0% | 30% |
| 2023-12-16 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 7,451 | 100.0% | 41% | 738 | 0.0% | 32% |
| 2023-12-16 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,764 | 100.0% | 44% | 678 | 0.0% | 32% |
| 2023-12-16 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,828 | 100.0% | 42% | 612 | 0.0% | 30% |
| 2023-12-16 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 15,545 | 100.0% | 40% | 624 | 0.0% | 29% |
| 2023-12-16 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 32,062 | 100.0% | 37% | 454 | 0.0% | 28% |
| 2023-12-16 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 24,607 | 100.0% | 52% | 273 | 0.0% | 38% |
| 2023-12-16 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 83,598 | 100.0% | 59% | 294 | 0.0% | 35% |
| 2023-12-16 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 81,132 | 100.0% | 58% | 286 | 0.0% | 36% |
| 2023-12-16 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 78,065 | 100.0% | 59% | 270 | 0.0% | 36% |
| 2023-12-16 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 60,385 | 100.0% | 60% | 248 | 0.0% | 39% |
| 2023-12-16 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 22,660 | 100.0% | 73% | 173 | 0.0% | 45% |
| 2023-12-16 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,283 | 100.0% | 22% | 3,129 | 0.0% | 39% |
| 2023-12-16 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,283 | 100.0% | 22% | 3,129 | 0.0% | 39% |
| 2023-12-16 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,143 | 100.0% | 30% | 1,197 | 0.0% | 48% |
| 2023-12-16 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 96 | 100.0% | 65% | 452 | 0.0% | 56% |
| 2023-12-16 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 0% |
| 2023-12-16 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.909 below threshold | | | | | | | | |
| 2023-12-17 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 17,529 | 99.8% | 34% | 944 | 0.0% | 31% |
| 2023-12-17 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 14,856 | 99.8% | 36% | 744 | 0.0% | 34% |
| 2023-12-17 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,479 | 99.8% | 41% | 600 | 0.0% | 38% |
| 2023-12-17 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,270 | 100.0% | 71% | 214 | 0.0% | 57% |
| 2023-12-17 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 89 | 100.0% | 98% | 117 | 0.0% | 66% |
| 2023-12-17 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,006 | 100.0% | 24% | 1,400 | 0.0% | 28% |
| 2023-12-17 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,980 | 100.0% | 24% | 1,081 | 0.0% | 27% |
| 2023-12-17 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,159 | 100.0% | 25% | 861 | 0.0% | 30% |
| 2023-12-17 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,396 | 100.0% | 51% | 306 | 0.0% | 44% |
| 2023-12-17 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 26 | 100.0% | 88% | 103 | 0.0% | 73% |
| 2023-12-17 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,352 | 100.0% | 27% | 1,584 | 0.0% | 28% |
| 2023-12-17 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,988 | 100.0% | 31% | 1,349 | 0.0% | 30% |
| 2023-12-17 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,502 | 100.0% | 36% | 814 | 0.0% | 34% |
| 2023-12-17 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 161 | 100.0% | 82% | 142 | 0.0% | 57% |
| 2023-12-17 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 9 | 100.0% | 100% | none resolved | 0.0% | 56% |
| 2023-12-17 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,041 | 100.0% | 30% | 1,062 | 0.0% | 38% |
| 2023-12-17 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 13,041 | 100.0% | 30% | 1,062 | 0.0% | 38% |
| 2023-12-17 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,892 | 100.0% | 43% | 572 | 0.0% | 46% |
| 2023-12-17 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 280 | 100.0% | 92% | 110 | 0.0% | 58% |
| 2023-12-17 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 15 | 100.0% | 100% | none resolved | 0.0% | 53% |
| 2023-12-17 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 12,643 | 100.0% | 24% | 1,697 | 0.0% | 28% |
| 2023-12-17 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,703 | 100.0% | 30% | 1,002 | 0.0% | 30% |
| 2023-12-17 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,808 | 100.0% | 40% | 571 | 0.0% | 35% |
| 2023-12-17 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 179 | 100.0% | 75% | 255 | 0.0% | 52% |
| 2023-12-17 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 6 | 100.0% | 100% | none resolved | 0.0% | 50% |
| 2023-12-17 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,700 | 100.0% | 43% | 1,312 | 0.0% | 33% |
| 2023-12-17 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,063 | 100.0% | 33% | 858 | 0.0% | 27% |
| 2023-12-17 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 17,730 | 100.0% | 32% | 592 | 0.0% | 27% |
| 2023-12-17 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 22,738 | 100.0% | 41% | 391 | 0.0% | 32% |
| 2023-12-17 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 883 | 100.0% | 85% | 122 | 0.2% | 56% |
| 2023-12-17 | tia_perp_binance_bybit | excluded: bybit_ob/bybit/TIA-USDT/perp coverage 1.000 below threshold | | | | | | | | |
| 2023-12-17 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 89,020 | 100.0% | 51% | 324 | 0.0% | 33% |
| 2023-12-17 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 90,341 | 100.0% | 50% | 298 | 0.0% | 32% |
| 2023-12-17 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 90,857 | 100.0% | 49% | 269 | 0.0% | 32% |
| 2023-12-17 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 76,328 | 100.0% | 53% | 212 | 0.0% | 35% |
| 2023-12-17 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 17,230 | 100.0% | 74% | 158 | 0.0% | 47% |
| 2023-12-17 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,970 | 100.0% | 36% | 1,854 | 0.0% | 47% |
| 2023-12-17 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,970 | 100.0% | 36% | 1,854 | 0.0% | 47% |
| 2023-12-17 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,160 | 100.0% | 42% | 1,437 | 0.0% | 48% |
| 2023-12-17 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 113 | 100.0% | 91% | 118 | 0.0% | 54% |
| 2023-12-17 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 15 | 100.0% | 93% | 115 | 0.0% | 80% |
| 2023-12-17 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.928 below threshold | | | | | | | | |
| 2023-12-18 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 26,285 | 99.9% | 43% | 592 | 0.0% | 36% |
| 2023-12-18 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 25,779 | 99.9% | 43% | 576 | 0.0% | 36% |
| 2023-12-18 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 16,110 | 99.9% | 49% | 550 | 0.0% | 40% |
| 2023-12-18 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,856 | 99.9% | 57% | 350 | 0.0% | 46% |
| 2023-12-18 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 161 | 100.0% | 89% | 126 | 0.0% | 58% |
| 2023-12-18 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 20,867 | 100.0% | 35% | 657 | 0.0% | 30% |
| 2023-12-18 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 20,251 | 100.0% | 35% | 547 | 0.0% | 30% |
| 2023-12-18 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 17,457 | 100.0% | 37% | 454 | 0.0% | 33% |
| 2023-12-18 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,078 | 100.0% | 66% | 226 | 0.1% | 48% |
| 2023-12-18 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 102 | 100.0% | 90% | 116 | 0.0% | 43% |
| 2023-12-18 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 20,503 | 100.0% | 29% | 1,100 | 0.0% | 27% |
| 2023-12-18 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 15,319 | 100.0% | 37% | 884 | 0.0% | 30% |
| 2023-12-18 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,706 | 100.0% | 44% | 642 | 0.0% | 33% |
| 2023-12-18 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 291 | 100.0% | 83% | 137 | 0.0% | 50% |
| 2023-12-18 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 19 | 100.0% | 89% | 120 | 0.0% | 37% |
| 2023-12-18 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 18,283 | 100.0% | 35% | 873 | 0.0% | 34% |
| 2023-12-18 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 18,283 | 100.0% | 35% | 873 | 0.0% | 34% |
| 2023-12-18 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 13,861 | 100.0% | 41% | 593 | 0.0% | 39% |
| 2023-12-18 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,138 | 100.0% | 83% | 126 | 0.0% | 51% |
| 2023-12-18 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 164 | 100.0% | 91% | 150 | 0.0% | 44% |
| 2023-12-18 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,445 | 100.0% | 32% | 1,033 | 0.0% | 29% |
| 2023-12-18 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 14,008 | 100.0% | 34% | 666 | 0.0% | 29% |
| 2023-12-18 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,112 | 100.0% | 36% | 613 | 0.0% | 30% |
| 2023-12-18 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,430 | 100.0% | 52% | 265 | 0.0% | 43% |
| 2023-12-18 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 34 | 100.0% | 97% | 200 | 0.0% | 32% |
| 2023-12-18 | sol_perp_binance_bybit | excluded: bybit_ob/bybit/SOL-USDT/perp coverage 1.000 below threshold | | | | | | | | |
| 2023-12-18 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 85,975 | 100.0% | 53% | 446 | 0.0% | 36% |
| 2023-12-18 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 79,145 | 100.0% | 54% | 422 | 0.0% | 36% |
| 2023-12-18 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 69,563 | 100.0% | 56% | 386 | 0.0% | 37% |
| 2023-12-18 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 35,779 | 100.0% | 61% | 316 | 0.0% | 41% |
| 2023-12-18 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 7,661 | 100.0% | 67% | 248 | 0.0% | 45% |
| 2023-12-18 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 67,357 | 100.0% | 47% | 354 | 0.0% | 34% |
| 2023-12-18 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 62,372 | 100.0% | 49% | 323 | 0.0% | 35% |
| 2023-12-18 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 56,387 | 100.0% | 50% | 284 | 0.0% | 36% |
| 2023-12-18 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 36,413 | 100.0% | 56% | 247 | 0.0% | 38% |
| 2023-12-18 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 9,991 | 100.0% | 65% | 208 | 0.0% | 46% |
| 2023-12-18 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,740 | 100.0% | 30% | 792 | 0.0% | 35% |
| 2023-12-18 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,740 | 100.0% | 30% | 792 | 0.0% | 35% |
| 2023-12-18 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,671 | 100.0% | 43% | 380 | 0.0% | 42% |
| 2023-12-18 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,227 | 100.0% | 78% | 144 | 0.0% | 49% |
| 2023-12-18 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 87 | 100.0% | 91% | 136 | 0.0% | 41% |
| 2023-12-18 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.949 below threshold | | | | | | | | |
| 2023-12-19 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 26,826 | 99.9% | 35% | 714 | 0.0% | 30% |
| 2023-12-19 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 21,366 | 99.9% | 40% | 585 | 0.0% | 34% |
| 2023-12-19 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 14,685 | 100.0% | 46% | 453 | 0.0% | 37% |
| 2023-12-19 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,975 | 100.0% | 71% | 164 | 0.0% | 46% |
| 2023-12-19 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 425 | 100.0% | 88% | 112 | 0.0% | 51% |
| 2023-12-19 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 12,596 | 100.0% | 30% | 824 | 0.0% | 28% |
| 2023-12-19 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,666 | 100.0% | 29% | 819 | 0.0% | 29% |
| 2023-12-19 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,168 | 100.0% | 29% | 687 | 0.0% | 29% |
| 2023-12-19 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 4,377 | 100.0% | 38% | 470 | 0.0% | 36% |
| 2023-12-19 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 89 | 100.0% | 91% | 120 | 0.0% | 55% |
| 2023-12-19 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,881 | 100.0% | 30% | 1,359 | 0.0% | 26% |
| 2023-12-19 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,650 | 100.0% | 34% | 962 | 0.1% | 28% |
| 2023-12-19 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,441 | 100.0% | 40% | 578 | 0.0% | 33% |
| 2023-12-19 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 450 | 100.0% | 77% | 148 | 0.0% | 45% |
| 2023-12-19 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 20 | 100.0% | 90% | 114 | 0.0% | 40% |
| 2023-12-19 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,196 | 100.0% | 28% | 1,195 | 0.0% | 36% |
| 2023-12-19 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,196 | 100.0% | 28% | 1,195 | 0.0% | 36% |
| 2023-12-19 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,572 | 100.0% | 33% | 885 | 0.0% | 40% |
| 2023-12-19 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,136 | 100.0% | 54% | 333 | 0.1% | 54% |
| 2023-12-19 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 20 | 100.0% | 100% | none resolved | 0.0% | 50% |
| 2023-12-19 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 17,694 | 100.0% | 30% | 923 | 0.0% | 29% |
| 2023-12-19 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 14,116 | 100.0% | 38% | 719 | 0.0% | 32% |
| 2023-12-19 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,958 | 100.0% | 41% | 823 | 0.0% | 33% |
| 2023-12-19 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 431 | 100.0% | 79% | 130 | 0.0% | 50% |
| 2023-12-19 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 16 | 100.0% | 94% | 100 | 0.0% | 38% |
| 2023-12-19 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 19,991 | 100.0% | 44% | 604 | 0.0% | 30% |
| 2023-12-19 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 21,558 | 100.0% | 39% | 487 | 0.0% | 29% |
| 2023-12-19 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 23,903 | 100.0% | 39% | 398 | 0.0% | 29% |
| 2023-12-19 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 18,499 | 100.0% | 42% | 361 | 0.0% | 32% |
| 2023-12-19 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 3,429 | 100.0% | 55% | 223 | 0.0% | 40% |
| 2023-12-19 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 32,775 | 100.0% | 42% | 511 | 0.0% | 33% |
| 2023-12-19 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 30,738 | 100.0% | 43% | 475 | 0.0% | 33% |
| 2023-12-19 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 29,548 | 100.0% | 43% | 451 | 0.0% | 33% |
| 2023-12-19 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 29,464 | 100.0% | 41% | 368 | 0.0% | 32% |
| 2023-12-19 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 13,286 | 100.0% | 55% | 226 | 0.0% | 41% |
| 2023-12-19 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 28,027 | 100.0% | 38% | 606 | 0.0% | 32% |
| 2023-12-19 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 31,130 | 100.0% | 36% | 526 | 0.0% | 32% |
| 2023-12-19 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 34,189 | 100.0% | 35% | 456 | 0.0% | 32% |
| 2023-12-19 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 32,507 | 100.0% | 41% | 334 | 0.0% | 36% |
| 2023-12-19 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 9,870 | 100.0% | 64% | 212 | 0.0% | 44% |
| 2023-12-19 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,556 | 100.0% | 21% | 1,872 | 0.0% | 34% |
| 2023-12-19 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,556 | 100.0% | 21% | 1,872 | 0.0% | 34% |
| 2023-12-19 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,388 | 100.0% | 26% | 2,004 | 0.0% | 38% |
| 2023-12-19 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 416 | 100.0% | 52% | 520 | 0.0% | 50% |
| 2023-12-19 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 17 | 100.0% | 94% | 131 | 0.0% | 35% |
| 2023-12-19 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.922 below threshold | | | | | | | | |
| 2023-12-20 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 21,726 | 99.8% | 36% | 690 | 0.0% | 36% |
| 2023-12-20 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 15,749 | 99.9% | 40% | 601 | 0.0% | 39% |
| 2023-12-20 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 9,372 | 99.9% | 47% | 493 | 0.0% | 45% |
| 2023-12-20 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,064 | 100.0% | 75% | 142 | 0.0% | 59% |
| 2023-12-20 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 111 | 100.0% | 87% | 110 | 0.0% | 60% |
| 2023-12-20 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 21,300 | 100.0% | 29% | 641 | 0.0% | 28% |
| 2023-12-20 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 16,085 | 100.0% | 33% | 512 | 0.0% | 30% |
| 2023-12-20 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,749 | 100.0% | 36% | 420 | 0.0% | 32% |
| 2023-12-20 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,636 | 100.0% | 57% | 297 | 0.1% | 43% |
| 2023-12-20 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 81 | 100.0% | 90% | 116 | 0.0% | 58% |
| 2023-12-20 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 17,612 | 100.0% | 29% | 1,196 | 0.0% | 27% |
| 2023-12-20 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 16,589 | 100.0% | 32% | 942 | 0.0% | 28% |
| 2023-12-20 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 9,542 | 100.0% | 42% | 899 | 0.0% | 33% |
| 2023-12-20 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 306 | 100.0% | 84% | 118 | 0.0% | 56% |
| 2023-12-20 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 27 | 100.0% | 85% | 145 | 0.0% | 56% |
| 2023-12-20 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,155 | 100.0% | 27% | 1,320 | 0.0% | 33% |
| 2023-12-20 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,155 | 100.0% | 27% | 1,320 | 0.0% | 33% |
| 2023-12-20 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,036 | 100.0% | 28% | 1,020 | 0.0% | 35% |
| 2023-12-20 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,000 | 100.0% | 55% | 240 | 0.0% | 47% |
| 2023-12-20 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 35 | 100.0% | 83% | 120 | 0.0% | 57% |
| 2023-12-20 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 20,256 | 100.0% | 30% | 912 | 0.0% | 29% |
| 2023-12-20 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 18,882 | 100.0% | 33% | 672 | 0.0% | 29% |
| 2023-12-20 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 12,147 | 100.0% | 41% | 433 | 0.0% | 33% |
| 2023-12-20 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 311 | 100.0% | 94% | 112 | 0.0% | 47% |
| 2023-12-20 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 33 | 100.0% | 100% | none resolved | 0.0% | 52% |
| 2023-12-20 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 53,118 | 100.0% | 47% | 491 | 0.0% | 32% |
| 2023-12-20 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 52,346 | 100.0% | 46% | 402 | 0.0% | 31% |
| 2023-12-20 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 50,214 | 100.0% | 46% | 340 | 0.0% | 32% |
| 2023-12-20 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 22,042 | 100.0% | 56% | 234 | 0.0% | 38% |
| 2023-12-20 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 615 | 100.0% | 89% | 120 | 0.0% | 53% |
| 2023-12-20 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 41,517 | 100.0% | 42% | 580 | 0.0% | 32% |
| 2023-12-20 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 44,766 | 100.0% | 42% | 484 | 0.0% | 31% |
| 2023-12-20 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 46,652 | 100.0% | 43% | 401 | 0.0% | 31% |
| 2023-12-20 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 42,224 | 100.0% | 45% | 295 | 0.0% | 34% |
| 2023-12-20 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 11,452 | 100.0% | 59% | 216 | 0.0% | 41% |
| 2023-12-20 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 25,871 | 100.0% | 30% | 646 | 0.0% | 32% |
| 2023-12-20 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 28,352 | 100.0% | 30% | 556 | 0.0% | 32% |
| 2023-12-20 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 30,168 | 100.0% | 30% | 472 | 0.0% | 32% |
| 2023-12-20 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 22,620 | 100.0% | 39% | 325 | 0.0% | 38% |
| 2023-12-20 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 4,487 | 100.0% | 60% | 204 | 0.0% | 42% |
| 2023-12-20 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,320 | 100.0% | 40% | 884 | 0.0% | 43% |
| 2023-12-20 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,320 | 100.0% | 40% | 884 | 0.0% | 43% |
| 2023-12-20 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,032 | 100.0% | 57% | 563 | 0.0% | 47% |
| 2023-12-20 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 227 | 100.0% | 93% | 120 | 0.0% | 45% |
| 2023-12-20 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 33 | 100.0% | 94% | 194 | 0.0% | 42% |
| 2023-12-20 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.937 below threshold | | | | | | | | |
| 2023-12-21 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 21,412 | 99.8% | 31% | 724 | 0.0% | 30% |
| 2023-12-21 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 19,706 | 99.8% | 33% | 650 | 0.0% | 31% |
| 2023-12-21 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 12,077 | 99.9% | 39% | 578 | 0.0% | 36% |
| 2023-12-21 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 938 | 100.0% | 78% | 155 | 0.0% | 59% |
| 2023-12-21 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 87 | 100.0% | 92% | 108 | 0.0% | 67% |
| 2023-12-21 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 17,526 | 100.0% | 26% | 718 | 0.0% | 26% |
| 2023-12-21 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 16,343 | 100.0% | 27% | 554 | 0.0% | 27% |
| 2023-12-21 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 14,064 | 100.0% | 31% | 396 | 0.0% | 28% |
| 2023-12-21 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 5,999 | 100.0% | 39% | 305 | 0.0% | 34% |
| 2023-12-21 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 111 | 100.0% | 97% | 133 | 0.0% | 50% |
| 2023-12-21 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,571 | 100.0% | 26% | 1,608 | 0.0% | 27% |
| 2023-12-21 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,911 | 100.0% | 30% | 1,247 | 0.0% | 27% |
| 2023-12-21 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,021 | 100.0% | 37% | 812 | 0.0% | 32% |
| 2023-12-21 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 140 | 100.0% | 85% | 123 | 0.0% | 49% |
| 2023-12-21 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 14 | 100.0% | 100% | none resolved | 0.0% | 57% |
| 2023-12-21 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,822 | 100.0% | 31% | 936 | 0.0% | 35% |
| 2023-12-21 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 13,822 | 100.0% | 31% | 936 | 0.0% | 35% |
| 2023-12-21 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 9,863 | 100.0% | 39% | 584 | 0.0% | 37% |
| 2023-12-21 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,912 | 100.0% | 47% | 368 | 0.0% | 31% |
| 2023-12-21 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 1,203 | 100.0% | 70% | 173 | 0.0% | 41% |
| 2023-12-21 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 18,036 | 100.0% | 26% | 1,336 | 0.0% | 29% |
| 2023-12-21 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 14,187 | 100.0% | 33% | 796 | 0.0% | 30% |
| 2023-12-21 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,671 | 100.0% | 41% | 455 | 0.0% | 32% |
| 2023-12-21 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,314 | 100.0% | 64% | 190 | 0.0% | 46% |
| 2023-12-21 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 14 | 100.0% | 93% | 120 | 0.0% | 50% |
| 2023-12-21 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 25,255 | 100.0% | 53% | 517 | 0.0% | 34% |
| 2023-12-21 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 30,448 | 100.0% | 46% | 406 | 0.0% | 31% |
| 2023-12-21 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 38,738 | 100.0% | 44% | 364 | 0.0% | 30% |
| 2023-12-21 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 47,762 | 100.0% | 47% | 281 | 0.0% | 32% |
| 2023-12-21 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 3,893 | 100.0% | 82% | 130 | 0.2% | 50% |
| 2023-12-21 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 27,231 | 100.0% | 39% | 549 | 0.0% | 29% |
| 2023-12-21 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 27,969 | 100.0% | 39% | 468 | 0.0% | 29% |
| 2023-12-21 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 28,390 | 100.0% | 39% | 429 | 0.0% | 30% |
| 2023-12-21 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 28,253 | 100.0% | 39% | 365 | 0.0% | 30% |
| 2023-12-21 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 11,718 | 100.0% | 52% | 312 | 0.0% | 38% |
| 2023-12-21 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 21,413 | 100.0% | 30% | 783 | 0.0% | 31% |
| 2023-12-21 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 24,641 | 100.0% | 28% | 634 | 0.0% | 31% |
| 2023-12-21 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 28,356 | 100.0% | 28% | 519 | 0.0% | 31% |
| 2023-12-21 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 24,802 | 100.0% | 36% | 329 | 0.0% | 37% |
| 2023-12-21 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 2,684 | 100.0% | 73% | 162 | 0.0% | 56% |
| 2023-12-21 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,969 | 100.0% | 34% | 1,099 | 0.0% | 49% |
| 2023-12-21 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,969 | 100.0% | 34% | 1,099 | 0.0% | 49% |
| 2023-12-21 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 714 | 100.0% | 57% | 323 | 0.0% | 53% |
| 2023-12-21 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 33 | 100.0% | 97% | 100 | 0.0% | 76% |
| 2023-12-21 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 4 | 100.0% | 100% | none resolved | 0.0% | 75% |
| 2023-12-21 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.938 below threshold | | | | | | | | |
| 2023-12-22 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 26,348 | 99.9% | 36% | 550 | 0.0% | 33% |
| 2023-12-22 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 21,285 | 99.9% | 38% | 500 | 0.0% | 34% |
| 2023-12-22 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 12,017 | 99.9% | 46% | 450 | 0.0% | 39% |
| 2023-12-22 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 850 | 100.0% | 81% | 185 | 0.1% | 58% |
| 2023-12-22 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 30 | 100.0% | 90% | 117 | 0.0% | 73% |
| 2023-12-22 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 55,977 | 100.0% | 44% | 371 | 0.0% | 30% |
| 2023-12-22 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 51,462 | 100.0% | 46% | 315 | 0.0% | 31% |
| 2023-12-22 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 46,831 | 100.0% | 48% | 281 | 0.0% | 32% |
| 2023-12-22 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 26,502 | 100.0% | 55% | 216 | 0.0% | 35% |
| 2023-12-22 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 3,416 | 100.0% | 74% | 152 | 0.0% | 46% |
| 2023-12-22 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,476 | 100.0% | 25% | 1,679 | 0.0% | 27% |
| 2023-12-22 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,022 | 100.0% | 30% | 1,118 | 0.0% | 31% |
| 2023-12-22 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,293 | 100.0% | 35% | 945 | 0.0% | 32% |
| 2023-12-22 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 130 | 100.0% | 82% | 124 | 0.8% | 46% |
| 2023-12-22 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 4 | 100.0% | 50% | 168 | 0.0% | 50% |
| 2023-12-22 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,380 | 100.0% | 26% | 1,074 | 0.1% | 31% |
| 2023-12-22 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,380 | 100.0% | 26% | 1,074 | 0.1% | 31% |
| 2023-12-22 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,242 | 100.0% | 27% | 857 | 0.0% | 32% |
| 2023-12-22 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,202 | 100.0% | 43% | 362 | 0.0% | 45% |
| 2023-12-22 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 48 | 100.0% | 96% | 118 | 0.0% | 56% |
| 2023-12-22 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,880 | 100.0% | 32% | 1,482 | 0.1% | 28% |
| 2023-12-22 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 14,355 | 100.0% | 27% | 1,094 | 0.0% | 25% |
| 2023-12-22 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 14,551 | 100.0% | 31% | 678 | 0.0% | 27% |
| 2023-12-22 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,447 | 100.0% | 55% | 234 | 0.1% | 39% |
| 2023-12-22 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 40 | 100.0% | 90% | 122 | 2.5% | 50% |
| 2023-12-22 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 42,489 | 100.0% | 51% | 459 | 0.0% | 34% |
| 2023-12-22 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 45,000 | 100.0% | 48% | 375 | 0.0% | 33% |
| 2023-12-22 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 49,246 | 100.0% | 46% | 347 | 0.0% | 32% |
| 2023-12-22 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 43,666 | 100.0% | 51% | 244 | 0.0% | 35% |
| 2023-12-22 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 6,683 | 100.0% | 65% | 164 | 0.0% | 41% |
| 2023-12-22 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,016 | 100.0% | 41% | 691 | 0.0% | 34% |
| 2023-12-22 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 16,932 | 100.0% | 38% | 580 | 0.0% | 31% |
| 2023-12-22 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 20,831 | 100.0% | 36% | 523 | 0.0% | 30% |
| 2023-12-22 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 31,596 | 100.0% | 37% | 377 | 0.0% | 32% |
| 2023-12-22 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 11,103 | 100.0% | 52% | 300 | 0.0% | 41% |
| 2023-12-22 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 15,901 | 100.0% | 29% | 806 | 0.0% | 31% |
| 2023-12-22 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 18,418 | 100.0% | 27% | 712 | 0.0% | 30% |
| 2023-12-22 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 22,162 | 100.0% | 26% | 568 | 0.0% | 31% |
| 2023-12-22 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 23,155 | 100.0% | 30% | 410 | 0.0% | 35% |
| 2023-12-22 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 4,762 | 100.0% | 50% | 256 | 0.0% | 48% |
| 2023-12-22 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,658 | 100.0% | 30% | 1,133 | 0.0% | 43% |
| 2023-12-22 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,658 | 100.0% | 30% | 1,133 | 0.0% | 43% |
| 2023-12-22 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,646 | 100.0% | 50% | 373 | 0.0% | 50% |
| 2023-12-22 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 147 | 100.0% | 93% | 115 | 0.0% | 50% |
| 2023-12-22 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 9 | 100.0% | 100% | none resolved | 0.0% | 67% |
| 2023-12-22 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.941 below threshold | | | | | | | | |
| 2023-12-23 | aave_perp_binance_bybit | ok | 0.999 | gross>0bps | 11,671 | 99.6% | 33% | 810 | 0.0% | 30% |
| 2023-12-23 | aave_perp_binance_bybit | ok | 0.999 | gross>1bps | 10,628 | 99.5% | 34% | 886 | 0.0% | 31% |
| 2023-12-23 | aave_perp_binance_bybit | ok | 0.999 | gross>2bps | 10,332 | 99.5% | 36% | 706 | 0.0% | 31% |
| 2023-12-23 | aave_perp_binance_bybit | ok | 0.999 | gross>5bps | 6,939 | 99.4% | 35% | 631 | 0.0% | 32% |
| 2023-12-23 | aave_perp_binance_bybit | ok | 0.999 | retail_taker | 394 | 100.0% | 78% | 141 | 0.0% | 50% |
| 2023-12-23 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,845 | 100.0% | 30% | 738 | 0.1% | 26% |
| 2023-12-23 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 17,850 | 100.0% | 28% | 564 | 0.0% | 24% |
| 2023-12-23 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 20,804 | 100.0% | 29% | 481 | 0.0% | 24% |
| 2023-12-23 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 21,629 | 100.0% | 38% | 313 | 0.0% | 28% |
| 2023-12-23 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 3,079 | 100.0% | 72% | 142 | 0.0% | 44% |
| 2023-12-23 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,739 | 100.0% | 23% | 3,229 | 0.0% | 28% |
| 2023-12-23 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,061 | 100.0% | 28% | 2,466 | 0.0% | 29% |
| 2023-12-23 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,918 | 99.9% | 33% | 2,181 | 0.0% | 31% |
| 2023-12-23 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 36 | 100.0% | 78% | 150 | 0.0% | 47% |
| 2023-12-23 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 7 | 100.0% | 57% | 104 | 0.0% | 43% |
| 2023-12-23 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,920 | 100.0% | 27% | 1,708 | 0.0% | 36% |
| 2023-12-23 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,920 | 100.0% | 27% | 1,708 | 0.0% | 36% |
| 2023-12-23 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,438 | 100.0% | 32% | 1,273 | 0.0% | 40% |
| 2023-12-23 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 326 | 100.0% | 71% | 133 | 0.0% | 59% |
| 2023-12-23 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 20 | 100.0% | 95% | 108 | 0.0% | 55% |
| 2023-12-23 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 9,175 | 100.0% | 24% | 2,235 | 0.0% | 29% |
| 2023-12-23 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,109 | 100.0% | 28% | 1,490 | 0.0% | 30% |
| 2023-12-23 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,199 | 100.0% | 37% | 934 | 0.0% | 33% |
| 2023-12-23 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 139 | 100.0% | 91% | 124 | 0.0% | 42% |
| 2023-12-23 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 38,952 | 100.0% | 47% | 498 | 0.0% | 33% |
| 2023-12-23 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 40,536 | 100.0% | 47% | 380 | 0.0% | 33% |
| 2023-12-23 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 40,815 | 100.0% | 47% | 327 | 0.0% | 32% |
| 2023-12-23 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 26,915 | 100.0% | 53% | 260 | 0.0% | 36% |
| 2023-12-23 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 2,019 | 100.0% | 80% | 148 | 0.1% | 49% |
| 2023-12-23 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,747 | 100.0% | 33% | 1,212 | 0.0% | 27% |
| 2023-12-23 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,790 | 100.0% | 27% | 750 | 0.0% | 24% |
| 2023-12-23 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 12,478 | 100.0% | 27% | 592 | 0.0% | 23% |
| 2023-12-23 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 25,661 | 100.0% | 32% | 433 | 0.0% | 28% |
| 2023-12-23 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 8,134 | 100.0% | 50% | 356 | 0.0% | 40% |
| 2023-12-23 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 9,551 | 100.0% | 24% | 1,132 | 0.0% | 32% |
| 2023-12-23 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,855 | 100.0% | 22% | 922 | 0.0% | 31% |
| 2023-12-23 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 14,392 | 100.0% | 22% | 762 | 0.0% | 32% |
| 2023-12-23 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 16,305 | 100.0% | 28% | 476 | 0.0% | 37% |
| 2023-12-23 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 2,373 | 100.0% | 60% | 306 | 0.0% | 57% |
| 2023-12-23 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,526 | 100.0% | 39% | 1,593 | 0.0% | 51% |
| 2023-12-23 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,526 | 100.0% | 39% | 1,593 | 0.0% | 51% |
| 2023-12-23 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 346 | 100.0% | 43% | 1,226 | 0.0% | 55% |
| 2023-12-23 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 15 | 100.0% | 87% | 123 | 0.0% | 80% |
| 2023-12-23 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 6 | 100.0% | 100% | none resolved | 0.0% | 67% |
| 2023-12-23 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.863 below threshold | | | | | | | | |
| 2023-12-24 | aave_perp_binance_bybit | excluded: bybit_ob/bybit/AAVE-USDT/perp coverage 1.000 below threshold | | | | | | | | |
| 2023-12-24 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 23,918 | 100.0% | 37% | 626 | 0.0% | 28% |
| 2023-12-24 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 25,836 | 100.0% | 37% | 546 | 0.0% | 27% |
| 2023-12-24 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 27,672 | 100.0% | 36% | 483 | 0.0% | 27% |
| 2023-12-24 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 20,026 | 100.0% | 43% | 312 | 0.0% | 33% |
| 2023-12-24 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 1,374 | 100.0% | 84% | 125 | 0.0% | 48% |
| 2023-12-24 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,369 | 100.0% | 26% | 2,373 | 0.0% | 28% |
| 2023-12-24 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,131 | 100.0% | 31% | 1,717 | 0.0% | 29% |
| 2023-12-24 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,048 | 100.0% | 46% | 851 | 0.0% | 35% |
| 2023-12-24 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 266 | 100.0% | 85% | 169 | 0.0% | 43% |
| 2023-12-24 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 54 | 100.0% | 80% | 165 | 0.0% | 39% |
| 2023-12-24 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 12,247 | 100.0% | 33% | 1,200 | 0.0% | 37% |
| 2023-12-24 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,247 | 100.0% | 33% | 1,200 | 0.0% | 37% |
| 2023-12-24 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,822 | 100.0% | 43% | 949 | 0.0% | 42% |
| 2023-12-24 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,004 | 100.0% | 78% | 150 | 0.0% | 50% |
| 2023-12-24 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 199 | 100.0% | 84% | 121 | 0.0% | 37% |
| 2023-12-24 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 15,147 | 100.0% | 27% | 1,478 | 0.0% | 28% |
| 2023-12-24 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,726 | 100.0% | 33% | 970 | 0.0% | 31% |
| 2023-12-24 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,777 | 100.0% | 40% | 643 | 0.0% | 33% |
| 2023-12-24 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 191 | 100.0% | 83% | 185 | 0.0% | 50% |
| 2023-12-24 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 35 | 100.0% | 94% | 256 | 0.0% | 20% |
| 2023-12-24 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 40,847 | 100.0% | 52% | 520 | 0.0% | 34% |
| 2023-12-24 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 44,877 | 100.0% | 49% | 398 | 0.0% | 32% |
| 2023-12-24 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 51,592 | 100.0% | 47% | 324 | 0.0% | 31% |
| 2023-12-24 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 57,930 | 100.0% | 51% | 246 | 0.0% | 33% |
| 2023-12-24 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 6,956 | 100.0% | 78% | 137 | 0.1% | 47% |
| 2023-12-24 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,893 | 100.0% | 47% | 952 | 0.0% | 32% |
| 2023-12-24 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,160 | 100.0% | 42% | 668 | 0.0% | 29% |
| 2023-12-24 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 13,223 | 100.0% | 39% | 520 | 0.0% | 27% |
| 2023-12-24 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 25,308 | 100.0% | 38% | 400 | 0.0% | 27% |
| 2023-12-24 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 34,453 | 100.0% | 41% | 353 | 0.0% | 30% |
| 2023-12-24 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,732 | 100.0% | 28% | 1,044 | 0.0% | 32% |
| 2023-12-24 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,044 | 100.0% | 25% | 966 | 0.0% | 30% |
| 2023-12-24 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 14,348 | 100.0% | 23% | 849 | 0.0% | 30% |
| 2023-12-24 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 21,275 | 100.0% | 25% | 535 | 0.0% | 34% |
| 2023-12-24 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 3,753 | 100.0% | 56% | 241 | 0.0% | 52% |
| 2023-12-24 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,517 | 100.0% | 37% | 1,206 | 0.0% | 41% |
| 2023-12-24 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,517 | 100.0% | 37% | 1,206 | 0.0% | 41% |
| 2023-12-24 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,770 | 100.0% | 53% | 383 | 0.0% | 47% |
| 2023-12-24 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 368 | 100.0% | 84% | 176 | 0.0% | 44% |
| 2023-12-24 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 185 | 100.0% | 85% | 157 | 0.0% | 42% |
| 2023-12-24 | zec_perp_binance_bybit | excluded: binance_bt/binance/ZEC-USDT/perp coverage 0.926 below threshold | | | | | | | | |
| 2023-12-25 | aave_perp_binance_bybit | excluded: bybit_ob/bybit/AAVE-USDT/perp coverage 1.000 below threshold | | | | | | | | |
| 2023-12-25 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 20,818 | 100.0% | 33% | 702 | 0.0% | 30% |
| 2023-12-25 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 19,004 | 100.0% | 33% | 638 | 0.0% | 31% |
| 2023-12-25 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 17,553 | 100.0% | 34% | 566 | 0.0% | 31% |
| 2023-12-25 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 8,254 | 100.0% | 43% | 328 | 0.0% | 37% |
| 2023-12-25 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 192 | 100.0% | 89% | 112 | 0.0% | 58% |
| 2023-12-25 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,733 | 100.0% | 22% | 2,521 | 0.0% | 27% |
| 2023-12-25 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,029 | 100.0% | 27% | 1,764 | 0.0% | 28% |
| 2023-12-25 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,746 | 100.0% | 31% | 1,756 | 0.0% | 28% |
| 2023-12-25 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 248 | 100.0% | 79% | 122 | 0.0% | 46% |
| 2023-12-25 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 23 | 100.0% | 78% | 118 | 0.0% | 70% |
| 2023-12-25 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,168 | 100.0% | 26% | 1,632 | 0.0% | 37% |
| 2023-12-25 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,168 | 100.0% | 26% | 1,632 | 0.0% | 37% |
| 2023-12-25 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,305 | 100.0% | 29% | 1,183 | 0.0% | 38% |
| 2023-12-25 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 840 | 100.0% | 54% | 358 | 0.0% | 49% |
| 2023-12-25 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 35 | 100.0% | 89% | 146 | 0.0% | 46% |
| 2023-12-25 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,544 | 100.0% | 23% | 1,812 | 0.0% | 29% |
| 2023-12-25 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,027 | 100.0% | 31% | 1,034 | 0.0% | 32% |
| 2023-12-25 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,084 | 100.0% | 47% | 656 | 0.0% | 38% |
| 2023-12-25 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 78 | 100.0% | 87% | 350 | 0.0% | 49% |
| 2023-12-25 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 2 | 100.0% | 100% | none resolved | 0.0% | 50% |
| 2023-12-25 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 25,702 | 100.0% | 52% | 707 | 0.0% | 34% |
| 2023-12-25 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 29,728 | 100.0% | 45% | 520 | 0.0% | 31% |
| 2023-12-25 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 37,553 | 100.0% | 43% | 408 | 0.0% | 30% |
| 2023-12-25 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 43,106 | 100.0% | 49% | 268 | 0.0% | 33% |
| 2023-12-25 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 13,325 | 100.0% | 65% | 191 | 0.0% | 37% |
| 2023-12-25 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,735 | 100.0% | 42% | 1,332 | 0.0% | 31% |
| 2023-12-25 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,828 | 100.0% | 36% | 932 | 0.0% | 28% |
| 2023-12-25 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,751 | 100.0% | 33% | 715 | 0.0% | 25% |
| 2023-12-25 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 27,491 | 100.0% | 33% | 410 | 0.0% | 26% |
| 2023-12-25 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 15,908 | 100.0% | 46% | 302 | 0.0% | 35% |
| 2023-12-25 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,061 | 100.0% | 26% | 980 | 0.0% | 32% |
| 2023-12-25 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 15,917 | 100.0% | 23% | 812 | 0.0% | 30% |
| 2023-12-25 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 19,276 | 100.0% | 24% | 677 | 0.0% | 30% |
| 2023-12-25 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 22,267 | 100.0% | 30% | 416 | 0.0% | 33% |
| 2023-12-25 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 8,897 | 100.0% | 44% | 256 | 0.0% | 39% |
| 2023-12-25 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,069 | 100.0% | 35% | 896 | 0.0% | 38% |
| 2023-12-25 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,069 | 100.0% | 35% | 896 | 0.0% | 38% |
| 2023-12-25 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,244 | 100.0% | 52% | 394 | 0.0% | 45% |
| 2023-12-25 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 442 | 100.0% | 80% | 117 | 0.0% | 57% |
| 2023-12-25 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 60 | 100.0% | 92% | 125 | 0.0% | 53% |
| 2023-12-25 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.934 below threshold | | | | | | | | |
| 2023-12-26 | aave_perp_binance_bybit | excluded: bybit_ob/bybit/AAVE-USDT/perp coverage 1.000 below threshold | | | | | | | | |
| 2023-12-26 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 27,877 | 100.0% | 37% | 561 | 0.1% | 29% |
| 2023-12-26 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 26,872 | 100.0% | 38% | 500 | 0.1% | 30% |
| 2023-12-26 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 25,352 | 100.0% | 39% | 420 | 0.1% | 32% |
| 2023-12-26 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 7,904 | 100.0% | 62% | 229 | 0.1% | 42% |
| 2023-12-26 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 410 | 100.0% | 81% | 190 | 2.0% | 45% |
| 2023-12-26 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,612 | 100.0% | 29% | 1,416 | 0.7% | 28% |
| 2023-12-26 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,430 | 100.0% | 32% | 1,124 | 0.6% | 28% |
| 2023-12-26 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,575 | 100.0% | 36% | 636 | 0.8% | 31% |
| 2023-12-26 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 678 | 100.0% | 78% | 158 | 10.0% | 44% |
| 2023-12-26 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 146 | 100.0% | 86% | 240 | 25.3% | 47% |
| 2023-12-26 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,011 | 100.0% | 32% | 984 | 0.0% | 36% |
| 2023-12-26 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,011 | 100.0% | 32% | 984 | 0.0% | 36% |
| 2023-12-26 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,950 | 100.0% | 35% | 684 | 0.0% | 37% |
| 2023-12-26 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,421 | 100.0% | 55% | 245 | 0.0% | 40% |
| 2023-12-26 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 414 | 100.0% | 76% | 206 | 0.0% | 41% |
| 2023-12-26 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 16,021 | 100.0% | 35% | 875 | 0.0% | 29% |
| 2023-12-26 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 15,672 | 100.0% | 36% | 957 | 0.0% | 30% |
| 2023-12-26 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,519 | 100.0% | 42% | 712 | 0.0% | 34% |
| 2023-12-26 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 484 | 100.0% | 84% | 145 | 0.0% | 43% |
| 2023-12-26 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 83 | 100.0% | 90% | 174 | 0.0% | 41% |
| 2023-12-26 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 48,664 | 100.0% | 59% | 392 | 0.0% | 34% |
| 2023-12-26 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 49,708 | 100.0% | 57% | 355 | 0.1% | 34% |
| 2023-12-26 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 50,152 | 100.0% | 57% | 336 | 0.1% | 33% |
| 2023-12-26 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 47,077 | 100.0% | 53% | 326 | 0.0% | 33% |
| 2023-12-26 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 9,304 | 100.0% | 75% | 179 | 0.2% | 44% |
| 2023-12-26 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 22,663 | 100.0% | 43% | 486 | 0.0% | 30% |
| 2023-12-26 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 24,676 | 100.0% | 41% | 470 | 0.0% | 29% |
| 2023-12-26 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 28,050 | 100.0% | 38% | 435 | 0.0% | 28% |
| 2023-12-26 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 32,264 | 100.0% | 40% | 373 | 0.0% | 29% |
| 2023-12-26 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 10,105 | 100.0% | 53% | 276 | 0.0% | 37% |
| 2023-12-26 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 25,591 | 100.0% | 33% | 692 | 0.0% | 31% |
| 2023-12-26 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 29,317 | 100.0% | 31% | 562 | 0.0% | 30% |
| 2023-12-26 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 33,108 | 100.0% | 32% | 432 | 0.0% | 30% |
| 2023-12-26 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 30,939 | 100.0% | 40% | 331 | 0.0% | 34% |
| 2023-12-26 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 7,354 | 100.0% | 59% | 221 | 0.0% | 45% |
| 2023-12-26 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 9,130 | 100.0% | 33% | 775 | 0.0% | 34% |
| 2023-12-26 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,130 | 100.0% | 33% | 775 | 0.0% | 34% |
| 2023-12-26 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,405 | 100.0% | 47% | 327 | 0.0% | 40% |
| 2023-12-26 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,273 | 100.0% | 79% | 174 | 0.0% | 46% |
| 2023-12-26 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 442 | 100.0% | 82% | 193 | 0.0% | 39% |
| 2023-12-26 | zec_perp_binance_bybit | ok | 0.997 | gross>0bps | 6,179 | 98.4% | 24% | 713 | 0.0% | 43% |
| 2023-12-26 | zec_perp_binance_bybit | ok | 0.997 | gross>1bps | 6,179 | 98.4% | 24% | 713 | 0.0% | 43% |
| 2023-12-26 | zec_perp_binance_bybit | ok | 0.997 | gross>2bps | 6,179 | 98.4% | 24% | 713 | 0.0% | 43% |
| 2023-12-26 | zec_perp_binance_bybit | ok | 0.997 | gross>5bps | 3,952 | 98.4% | 26% | 510 | 0.0% | 43% |
| 2023-12-26 | zec_perp_binance_bybit | ok | 0.997 | retail_taker | 510 | 99.6% | 63% | 262 | 0.0% | 58% |
| 2023-12-27 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 34,594 | 100.0% | 41% | 564 | 0.0% | 31% |
| 2023-12-27 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 29,068 | 100.0% | 44% | 574 | 0.0% | 34% |
| 2023-12-27 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 22,366 | 100.0% | 46% | 544 | 0.0% | 35% |
| 2023-12-27 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 6,978 | 100.0% | 61% | 332 | 0.0% | 41% |
| 2023-12-27 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 747 | 100.0% | 91% | 121 | 0.0% | 52% |
| 2023-12-27 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 29,918 | 100.0% | 40% | 512 | 0.0% | 29% |
| 2023-12-27 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 32,273 | 100.0% | 38% | 420 | 0.0% | 28% |
| 2023-12-27 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 34,397 | 100.0% | 39% | 364 | 0.0% | 28% |
| 2023-12-27 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 25,531 | 100.0% | 47% | 261 | 0.0% | 32% |
| 2023-12-27 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 2,111 | 100.0% | 85% | 122 | 0.0% | 51% |
| 2023-12-27 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,962 | 100.0% | 27% | 1,799 | 0.0% | 27% |
| 2023-12-27 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,837 | 100.0% | 27% | 1,074 | 0.0% | 26% |
| 2023-12-27 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,789 | 100.0% | 31% | 732 | 0.0% | 28% |
| 2023-12-27 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 256 | 100.0% | 70% | 130 | 0.0% | 51% |
| 2023-12-27 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 6 | 100.0% | 83% | 129 | 0.0% | 50% |
| 2023-12-27 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,714 | 100.0% | 22% | 1,774 | 0.0% | 34% |
| 2023-12-27 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,714 | 100.0% | 22% | 1,774 | 0.0% | 34% |
| 2023-12-27 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,631 | 100.0% | 23% | 1,451 | 0.0% | 36% |
| 2023-12-27 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,709 | 100.0% | 44% | 462 | 0.0% | 46% |
| 2023-12-27 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 39 | 100.0% | 100% | none resolved | 0.0% | 51% |
| 2023-12-27 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,110 | 100.0% | 27% | 1,431 | 0.0% | 29% |
| 2023-12-27 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,295 | 100.0% | 31% | 752 | 0.0% | 29% |
| 2023-12-27 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,396 | 100.0% | 31% | 562 | 0.0% | 28% |
| 2023-12-27 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,153 | 100.0% | 58% | 208 | 0.0% | 44% |
| 2023-12-27 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 18 | 100.0% | 89% | 154 | 0.0% | 56% |
| 2023-12-27 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 25,161 | 100.0% | 47% | 680 | 0.0% | 32% |
| 2023-12-27 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 28,162 | 100.0% | 44% | 569 | 0.0% | 30% |
| 2023-12-27 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 35,329 | 100.0% | 41% | 422 | 0.0% | 29% |
| 2023-12-27 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 46,787 | 100.0% | 49% | 265 | 0.0% | 32% |
| 2023-12-27 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 9,476 | 100.0% | 65% | 193 | 0.0% | 40% |
| 2023-12-27 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,918 | 100.0% | 36% | 913 | 0.0% | 29% |
| 2023-12-27 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,019 | 100.0% | 33% | 740 | 0.0% | 27% |
| 2023-12-27 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 10,137 | 100.0% | 31% | 712 | 0.0% | 26% |
| 2023-12-27 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 27,470 | 100.0% | 31% | 416 | 0.0% | 25% |
| 2023-12-27 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 19,813 | 100.0% | 47% | 256 | 0.0% | 36% |
| 2023-12-27 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 21,850 | 100.0% | 26% | 740 | 0.0% | 31% |
| 2023-12-27 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 23,533 | 100.0% | 25% | 606 | 0.0% | 32% |
| 2023-12-27 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 23,247 | 100.0% | 27% | 479 | 0.0% | 34% |
| 2023-12-27 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 12,935 | 100.0% | 39% | 356 | 0.0% | 39% |
| 2023-12-27 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 1,900 | 100.0% | 53% | 251 | 0.1% | 50% |
| 2023-12-27 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,201 | 100.0% | 29% | 1,282 | 0.0% | 40% |
| 2023-12-27 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 6,201 | 100.0% | 29% | 1,282 | 0.0% | 40% |
| 2023-12-27 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,044 | 100.0% | 46% | 592 | 0.0% | 47% |
| 2023-12-27 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 149 | 100.0% | 91% | 110 | 0.0% | 55% |
| 2023-12-27 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 33 | 100.0% | 100% | none resolved | 0.0% | 42% |
| 2023-12-27 | zec_perp_binance_bybit | ok | 0.999 | gross>0bps | 6,558 | 99.7% | 25% | 638 | 0.0% | 38% |
| 2023-12-27 | zec_perp_binance_bybit | ok | 0.999 | gross>1bps | 6,558 | 99.7% | 25% | 638 | 0.0% | 38% |
| 2023-12-27 | zec_perp_binance_bybit | ok | 0.999 | gross>2bps | 6,558 | 99.7% | 25% | 638 | 0.0% | 38% |
| 2023-12-27 | zec_perp_binance_bybit | ok | 0.999 | gross>5bps | 2,825 | 99.9% | 32% | 448 | 0.0% | 42% |
| 2023-12-27 | zec_perp_binance_bybit | ok | 0.999 | retail_taker | 509 | 100.0% | 54% | 328 | 0.0% | 54% |
| 2023-12-28 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 70,364 | 100.0% | 46% | 380 | 0.0% | 33% |
| 2023-12-28 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 56,048 | 100.0% | 50% | 350 | 0.0% | 36% |
| 2023-12-28 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 42,270 | 100.0% | 54% | 310 | 0.0% | 38% |
| 2023-12-28 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 12,660 | 100.0% | 64% | 212 | 0.0% | 44% |
| 2023-12-28 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 1,454 | 100.0% | 87% | 118 | 0.0% | 55% |
| 2023-12-28 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 27,370 | 100.0% | 39% | 480 | 0.0% | 27% |
| 2023-12-28 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 31,468 | 100.0% | 36% | 418 | 0.0% | 27% |
| 2023-12-28 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 38,808 | 100.0% | 37% | 350 | 0.0% | 27% |
| 2023-12-28 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 36,602 | 100.0% | 45% | 260 | 0.0% | 32% |
| 2023-12-28 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 3,152 | 100.0% | 82% | 126 | 0.0% | 50% |
| 2023-12-28 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 9,719 | 100.0% | 28% | 1,633 | 0.1% | 28% |
| 2023-12-28 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,013 | 100.0% | 29% | 996 | 0.0% | 27% |
| 2023-12-28 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,089 | 100.0% | 33% | 659 | 0.0% | 30% |
| 2023-12-28 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 186 | 100.0% | 82% | 142 | 0.0% | 48% |
| 2023-12-28 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 12 | 100.0% | 67% | 122 | 0.0% | 50% |
| 2023-12-28 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,966 | 100.0% | 27% | 1,101 | 0.0% | 35% |
| 2023-12-28 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,966 | 100.0% | 27% | 1,101 | 0.0% | 35% |
| 2023-12-28 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 9,034 | 100.0% | 31% | 891 | 0.0% | 37% |
| 2023-12-28 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,733 | 100.0% | 54% | 329 | 0.1% | 53% |
| 2023-12-28 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 46 | 100.0% | 80% | 270 | 0.0% | 48% |
| 2023-12-28 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 20,800 | 100.0% | 34% | 970 | 0.0% | 28% |
| 2023-12-28 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 21,925 | 100.0% | 34% | 609 | 0.0% | 27% |
| 2023-12-28 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 18,172 | 100.0% | 40% | 415 | 0.0% | 31% |
| 2023-12-28 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,362 | 100.0% | 74% | 191 | 0.0% | 48% |
| 2023-12-28 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 151 | 100.0% | 90% | 137 | 0.0% | 44% |
| 2023-12-28 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 71,675 | 100.0% | 50% | 450 | 0.0% | 32% |
| 2023-12-28 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 73,452 | 100.0% | 48% | 346 | 0.0% | 31% |
| 2023-12-28 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 74,552 | 100.0% | 49% | 268 | 0.0% | 31% |
| 2023-12-28 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 30,242 | 100.0% | 62% | 205 | 0.0% | 39% |
| 2023-12-28 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 1,148 | 100.0% | 87% | 124 | 0.0% | 55% |
| 2023-12-28 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,405 | 100.0% | 36% | 600 | 0.0% | 27% |
| 2023-12-28 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,826 | 100.0% | 33% | 526 | 0.0% | 26% |
| 2023-12-28 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 14,747 | 100.0% | 32% | 544 | 0.0% | 26% |
| 2023-12-28 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 33,722 | 100.0% | 33% | 400 | 0.0% | 26% |
| 2023-12-28 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 9,599 | 100.0% | 53% | 373 | 0.0% | 41% |
| 2023-12-28 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 17,948 | 100.0% | 27% | 637 | 0.0% | 31% |
| 2023-12-28 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 21,733 | 100.0% | 26% | 554 | 0.0% | 32% |
| 2023-12-28 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 24,836 | 100.0% | 28% | 486 | 0.0% | 34% |
| 2023-12-28 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 17,128 | 100.0% | 37% | 406 | 0.0% | 41% |
| 2023-12-28 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 1,294 | 100.0% | 66% | 269 | 0.0% | 48% |
| 2023-12-28 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,274 | 100.0% | 37% | 660 | 0.0% | 40% |
| 2023-12-28 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,274 | 100.0% | 37% | 660 | 0.0% | 40% |
| 2023-12-28 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,484 | 100.0% | 53% | 342 | 0.0% | 47% |
| 2023-12-28 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 585 | 100.0% | 85% | 125 | 0.0% | 55% |
| 2023-12-28 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 109 | 100.0% | 98% | 110 | 0.0% | 55% |
| 2023-12-28 | zec_perp_binance_bybit | ok | 0.999 | gross>0bps | 9,264 | 99.3% | 25% | 678 | 0.0% | 38% |
| 2023-12-28 | zec_perp_binance_bybit | ok | 0.999 | gross>1bps | 9,264 | 99.3% | 25% | 678 | 0.0% | 38% |
| 2023-12-28 | zec_perp_binance_bybit | ok | 0.999 | gross>2bps | 9,264 | 99.3% | 25% | 678 | 0.0% | 38% |
| 2023-12-28 | zec_perp_binance_bybit | ok | 0.999 | gross>5bps | 5,986 | 99.6% | 29% | 497 | 0.0% | 42% |
| 2023-12-28 | zec_perp_binance_bybit | ok | 0.999 | retail_taker | 662 | 99.8% | 57% | 211 | 0.0% | 60% |
| 2023-12-29 | aave_perp_binance_bybit | ok | 1.000 | gross>0bps | 38,452 | 99.9% | 42% | 531 | 0.0% | 35% |
| 2023-12-29 | aave_perp_binance_bybit | ok | 1.000 | gross>1bps | 30,951 | 100.0% | 46% | 500 | 0.0% | 37% |
| 2023-12-29 | aave_perp_binance_bybit | ok | 1.000 | gross>2bps | 22,977 | 100.0% | 50% | 452 | 0.0% | 40% |
| 2023-12-29 | aave_perp_binance_bybit | ok | 1.000 | gross>5bps | 5,211 | 100.0% | 67% | 254 | 0.1% | 48% |
| 2023-12-29 | aave_perp_binance_bybit | ok | 1.000 | retail_taker | 320 | 100.0% | 88% | 137 | 0.0% | 57% |
| 2023-12-29 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 15,058 | 100.0% | 37% | 658 | 0.0% | 29% |
| 2023-12-29 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 18,189 | 100.0% | 35% | 560 | 0.0% | 28% |
| 2023-12-29 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 22,058 | 100.0% | 34% | 465 | 0.0% | 28% |
| 2023-12-29 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 27,623 | 100.0% | 42% | 316 | 0.0% | 33% |
| 2023-12-29 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 1,734 | 100.0% | 81% | 152 | 0.0% | 52% |
| 2023-12-29 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 16,772 | 100.0% | 31% | 1,055 | 0.0% | 28% |
| 2023-12-29 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 14,115 | 100.0% | 34% | 826 | 0.0% | 31% |
| 2023-12-29 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,738 | 100.0% | 44% | 702 | 0.0% | 36% |
| 2023-12-29 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 310 | 100.0% | 81% | 191 | 2.3% | 45% |
| 2023-12-29 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 64 | 100.0% | 84% | 264 | 0.0% | 38% |
| 2023-12-29 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,654 | 100.0% | 30% | 962 | 0.0% | 38% |
| 2023-12-29 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,654 | 100.0% | 30% | 962 | 0.0% | 38% |
| 2023-12-29 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,359 | 100.0% | 36% | 816 | 0.0% | 43% |
| 2023-12-29 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,027 | 100.0% | 72% | 183 | 0.0% | 52% |
| 2023-12-29 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 128 | 100.0% | 89% | 144 | 0.0% | 38% |
| 2023-12-29 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 23,621 | 100.0% | 34% | 788 | 0.0% | 30% |
| 2023-12-29 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 22,318 | 100.0% | 37% | 691 | 0.0% | 30% |
| 2023-12-29 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 14,135 | 100.0% | 43% | 516 | 0.0% | 33% |
| 2023-12-29 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 798 | 100.0% | 88% | 136 | 0.0% | 45% |
| 2023-12-29 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 70 | 100.0% | 84% | 151 | 0.0% | 41% |
| 2023-12-29 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 75,801 | 100.0% | 52% | 388 | 0.0% | 33% |
| 2023-12-29 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 72,840 | 100.0% | 52% | 334 | 0.0% | 34% |
| 2023-12-29 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 67,400 | 100.0% | 52% | 291 | 0.0% | 35% |
| 2023-12-29 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 31,584 | 100.0% | 58% | 220 | 0.0% | 38% |
| 2023-12-29 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 1,585 | 100.0% | 85% | 122 | 0.0% | 53% |
| 2023-12-29 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 11,640 | 100.0% | 41% | 469 | 0.0% | 29% |
| 2023-12-29 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 13,131 | 100.0% | 40% | 445 | 0.0% | 29% |
| 2023-12-29 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 15,438 | 100.0% | 38% | 441 | 0.0% | 28% |
| 2023-12-29 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 25,288 | 100.0% | 36% | 424 | 0.0% | 28% |
| 2023-12-29 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 12,741 | 100.0% | 49% | 339 | 0.0% | 36% |
| 2023-12-29 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 12,606 | 100.0% | 26% | 932 | 0.0% | 29% |
| 2023-12-29 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 17,385 | 100.0% | 24% | 725 | 0.0% | 29% |
| 2023-12-29 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 23,195 | 100.0% | 25% | 584 | 0.0% | 31% |
| 2023-12-29 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 20,680 | 100.0% | 36% | 366 | 0.0% | 40% |
| 2023-12-29 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 2,400 | 100.0% | 59% | 283 | 0.0% | 50% |
| 2023-12-29 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,038 | 100.0% | 34% | 741 | 0.0% | 41% |
| 2023-12-29 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,038 | 100.0% | 34% | 741 | 0.0% | 41% |
| 2023-12-29 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,686 | 100.0% | 49% | 396 | 0.0% | 48% |
| 2023-12-29 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 200 | 100.0% | 93% | 148 | 0.0% | 53% |
| 2023-12-29 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 31 | 100.0% | 97% | 186 | 0.0% | 55% |
| 2023-12-29 | zec_perp_binance_bybit | ok | 0.999 | gross>0bps | 8,069 | 99.6% | 23% | 964 | 0.0% | 39% |
| 2023-12-29 | zec_perp_binance_bybit | ok | 0.999 | gross>1bps | 8,069 | 99.6% | 23% | 964 | 0.0% | 39% |
| 2023-12-29 | zec_perp_binance_bybit | ok | 0.999 | gross>2bps | 8,069 | 99.6% | 23% | 964 | 0.0% | 39% |
| 2023-12-29 | zec_perp_binance_bybit | ok | 0.999 | gross>5bps | 5,619 | 99.9% | 28% | 564 | 0.0% | 44% |
| 2023-12-29 | zec_perp_binance_bybit | ok | 0.999 | retail_taker | 1,253 | 100.0% | 51% | 359 | 0.0% | 56% |
| 2023-12-30 | aave_perp_binance_bybit | excluded: bybit_ob/bybit/AAVE-USDT/perp coverage 1.000 below threshold | | | | | | | | |
| 2023-12-30 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,551 | 100.0% | 28% | 929 | 0.0% | 27% |
| 2023-12-30 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,578 | 100.0% | 26% | 721 | 0.0% | 27% |
| 2023-12-30 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 14,049 | 100.0% | 26% | 672 | 0.0% | 28% |
| 2023-12-30 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 11,195 | 100.0% | 35% | 435 | 0.0% | 36% |
| 2023-12-30 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 558 | 100.0% | 75% | 140 | 0.0% | 56% |
| 2023-12-30 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,208 | 100.0% | 26% | 2,877 | 0.0% | 27% |
| 2023-12-30 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,843 | 100.0% | 28% | 1,655 | 0.0% | 31% |
| 2023-12-30 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,836 | 100.0% | 47% | 492 | 0.0% | 43% |
| 2023-12-30 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 50 | 100.0% | 76% | 119 | 0.0% | 54% |
| 2023-12-30 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 5 | 100.0% | 80% | 132 | 0.0% | 60% |
| 2023-12-30 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,841 | 100.0% | 21% | 2,947 | 0.0% | 37% |
| 2023-12-30 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,841 | 100.0% | 21% | 2,947 | 0.0% | 37% |
| 2023-12-30 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,508 | 100.0% | 25% | 2,062 | 0.0% | 42% |
| 2023-12-30 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 176 | 100.0% | 80% | 150 | 0.0% | 49% |
| 2023-12-30 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 8 | 100.0% | 88% | 111 | 0.0% | 50% |
| 2023-12-30 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,203 | 100.0% | 23% | 1,937 | 0.0% | 29% |
| 2023-12-30 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,905 | 100.0% | 31% | 1,358 | 0.0% | 30% |
| 2023-12-30 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,774 | 100.0% | 40% | 642 | 0.0% | 35% |
| 2023-12-30 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 91 | 100.0% | 86% | 118 | 0.0% | 45% |
| 2023-12-30 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 8 | 100.0% | 75% | 148 | 0.0% | 75% |
| 2023-12-30 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 22,093 | 100.0% | 45% | 743 | 0.0% | 34% |
| 2023-12-30 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 27,177 | 100.0% | 39% | 506 | 0.0% | 31% |
| 2023-12-30 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 33,241 | 100.0% | 38% | 406 | 0.0% | 31% |
| 2023-12-30 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 23,146 | 100.0% | 48% | 259 | 0.0% | 35% |
| 2023-12-30 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 388 | 100.0% | 87% | 116 | 0.0% | 56% |
| 2023-12-30 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,879 | 99.8% | 37% | 1,909 | 0.0% | 31% |
| 2023-12-30 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,988 | 99.9% | 31% | 1,274 | 0.0% | 29% |
| 2023-12-30 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 9,373 | 99.9% | 30% | 980 | 0.0% | 26% |
| 2023-12-30 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 22,242 | 100.0% | 32% | 486 | 0.0% | 28% |
| 2023-12-30 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 4,875 | 100.0% | 56% | 400 | 0.0% | 42% |
| 2023-12-30 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 19,469 | 100.0% | 31% | 693 | 0.0% | 31% |
| 2023-12-30 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 23,096 | 100.0% | 30% | 560 | 0.0% | 30% |
| 2023-12-30 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 26,423 | 100.0% | 30% | 467 | 0.0% | 32% |
| 2023-12-30 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 22,920 | 100.0% | 38% | 344 | 0.0% | 37% |
| 2023-12-30 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 4,369 | 100.0% | 65% | 194 | 0.0% | 48% |
| 2023-12-30 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 2,429 | 100.0% | 25% | 2,154 | 0.1% | 43% |
| 2023-12-30 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,429 | 100.0% | 25% | 2,154 | 0.1% | 43% |
| 2023-12-30 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,043 | 100.0% | 30% | 1,273 | 0.0% | 45% |
| 2023-12-30 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 52 | 100.0% | 88% | 112 | 0.0% | 48% |
| 2023-12-30 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 13 | 100.0% | 100% | none resolved | 0.0% | 54% |
| 2023-12-30 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.916 below threshold | | | | | | | | |
| 2023-12-31 | aave_perp_binance_bybit | excluded: bybit_ob/bybit/AAVE-USDT/perp coverage 1.000 below threshold | | | | | | | | |
| 2023-12-31 | arb_perp_binance_bybit | ok | 1.000 | gross>0bps | 15,375 | 100.0% | 33% | 804 | 0.0% | 30% |
| 2023-12-31 | arb_perp_binance_bybit | ok | 1.000 | gross>1bps | 17,731 | 100.0% | 30% | 648 | 0.0% | 28% |
| 2023-12-31 | arb_perp_binance_bybit | ok | 1.000 | gross>2bps | 21,831 | 100.0% | 31% | 472 | 0.0% | 28% |
| 2023-12-31 | arb_perp_binance_bybit | ok | 1.000 | gross>5bps | 18,085 | 100.0% | 39% | 390 | 0.0% | 33% |
| 2023-12-31 | arb_perp_binance_bybit | ok | 1.000 | retail_taker | 3,036 | 100.0% | 72% | 137 | 0.0% | 47% |
| 2023-12-31 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,306 | 100.0% | 25% | 2,371 | 0.1% | 28% |
| 2023-12-31 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,845 | 100.0% | 23% | 2,418 | 0.0% | 26% |
| 2023-12-31 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,581 | 100.0% | 27% | 1,194 | 0.0% | 28% |
| 2023-12-31 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 157 | 100.0% | 73% | 114 | 0.0% | 55% |
| 2023-12-31 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 3 | 100.0% | 100% | none resolved | 0.0% | 33% |
| 2023-12-31 | doge_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,440 | 100.0% | 24% | 2,651 | 0.0% | 39% |
| 2023-12-31 | doge_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,440 | 100.0% | 24% | 2,651 | 0.0% | 39% |
| 2023-12-31 | doge_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,767 | 100.0% | 28% | 1,973 | 0.0% | 45% |
| 2023-12-31 | doge_perp_binance_bybit | ok | 1.000 | gross>5bps | 165 | 100.0% | 72% | 190 | 0.0% | 48% |
| 2023-12-31 | doge_perp_binance_bybit | ok | 1.000 | retail_taker | 3 | 100.0% | 67% | 110 | 0.0% | 100% |
| 2023-12-31 | eth_perp_binance_bybit | ok | 1.000 | gross>0bps | 15,198 | 100.0% | 21% | 1,871 | 0.0% | 28% |
| 2023-12-31 | eth_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,678 | 100.0% | 38% | 981 | 0.0% | 36% |
| 2023-12-31 | eth_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,123 | 100.0% | 49% | 526 | 0.0% | 40% |
| 2023-12-31 | eth_perp_binance_bybit | ok | 1.000 | gross>5bps | 58 | 100.0% | 81% | 119 | 0.0% | 47% |
| 2023-12-31 | eth_perp_binance_bybit | ok | 1.000 | retail_taker | 9 | 100.0% | 100% | none resolved | 0.0% | 33% |
| 2023-12-31 | sol_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,786 | 100.0% | 43% | 1,072 | 0.0% | 34% |
| 2023-12-31 | sol_perp_binance_bybit | ok | 1.000 | gross>1bps | 16,036 | 100.0% | 35% | 613 | 0.0% | 30% |
| 2023-12-31 | sol_perp_binance_bybit | ok | 1.000 | gross>2bps | 22,973 | 100.0% | 36% | 456 | 0.0% | 30% |
| 2023-12-31 | sol_perp_binance_bybit | ok | 1.000 | gross>5bps | 23,705 | 100.0% | 42% | 342 | 0.0% | 34% |
| 2023-12-31 | sol_perp_binance_bybit | ok | 1.000 | retail_taker | 561 | 100.0% | 86% | 115 | 0.0% | 60% |
| 2023-12-31 | tia_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,675 | 99.9% | 33% | 1,536 | 0.0% | 28% |
| 2023-12-31 | tia_perp_binance_bybit | ok | 1.000 | gross>1bps | 7,716 | 99.9% | 27% | 1,097 | 0.0% | 24% |
| 2023-12-31 | tia_perp_binance_bybit | ok | 1.000 | gross>2bps | 12,444 | 100.0% | 26% | 809 | 0.0% | 24% |
| 2023-12-31 | tia_perp_binance_bybit | ok | 1.000 | gross>5bps | 20,971 | 100.0% | 35% | 480 | 0.0% | 31% |
| 2023-12-31 | tia_perp_binance_bybit | ok | 1.000 | retail_taker | 3,063 | 100.0% | 59% | 288 | 0.0% | 46% |
| 2023-12-31 | wld_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,136 | 100.0% | 30% | 1,428 | 0.0% | 32% |
| 2023-12-31 | wld_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,397 | 100.0% | 27% | 1,106 | 0.0% | 31% |
| 2023-12-31 | wld_perp_binance_bybit | ok | 1.000 | gross>2bps | 13,856 | 100.0% | 25% | 886 | 0.0% | 31% |
| 2023-12-31 | wld_perp_binance_bybit | ok | 1.000 | gross>5bps | 19,266 | 100.0% | 28% | 573 | 0.0% | 35% |
| 2023-12-31 | wld_perp_binance_bybit | ok | 1.000 | retail_taker | 4,446 | 100.0% | 57% | 284 | 0.0% | 50% |
| 2023-12-31 | xrp_perp_binance_bybit | ok | 1.000 | gross>0bps | 1,946 | 100.0% | 36% | 985 | 0.0% | 47% |
| 2023-12-31 | xrp_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,946 | 100.0% | 36% | 985 | 0.0% | 47% |
| 2023-12-31 | xrp_perp_binance_bybit | ok | 1.000 | gross>2bps | 585 | 100.0% | 47% | 662 | 0.0% | 42% |
| 2023-12-31 | xrp_perp_binance_bybit | ok | 1.000 | gross>5bps | 108 | 100.0% | 77% | 152 | 0.0% | 44% |
| 2023-12-31 | xrp_perp_binance_bybit | ok | 1.000 | retail_taker | 27 | 100.0% | 81% | 253 | 0.0% | 56% |
| 2023-12-31 | zec_perp_binance_bybit | excluded: bybit_ob/bybit/ZEC-USDT/perp coverage 0.891 below threshold | | | | | | | | |
| 2024-01-01 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 5,412 | 100.0% | 27% | 1,990 | 0.0% | 29% |
| 2024-01-01 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 5,283 | 100.0% | 26% | 1,628 | 0.0% | 30% |
| 2024-01-01 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,153 | 100.0% | 29% | 1,658 | 0.0% | 30% |
| 2024-01-01 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 284 | 100.0% | 71% | 127 | 0.0% | 46% |
| 2024-01-01 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 3 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2024-01-02 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 16,531 | 100.0% | 32% | 919 | 0.4% | 28% |
| 2024-01-02 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 16,492 | 100.0% | 34% | 597 | 0.5% | 29% |
| 2024-01-02 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 13,014 | 100.0% | 37% | 481 | 0.4% | 32% |
| 2024-01-02 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,610 | 100.0% | 64% | 170 | 2.5% | 48% |
| 2024-01-02 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 45 | 100.0% | 80% | 210 | 28.9% | 44% |
| 2024-01-03 | btc_perp_binance_bybit | ok | 0.995 | gross>0bps | 23,042 | 100.0% | 54% | 392 | 0.0% | 33% |
| 2024-01-03 | btc_perp_binance_bybit | ok | 0.995 | gross>1bps | 21,141 | 100.0% | 54% | 418 | 0.0% | 33% |
| 2024-01-03 | btc_perp_binance_bybit | ok | 0.995 | gross>2bps | 19,130 | 100.0% | 50% | 419 | 0.1% | 33% |
| 2024-01-03 | btc_perp_binance_bybit | ok | 0.995 | gross>5bps | 9,212 | 100.0% | 52% | 358 | 0.0% | 35% |
| 2024-01-03 | btc_perp_binance_bybit | ok | 0.995 | retail_taker | 524 | 99.8% | 83% | 205 | 0.0% | 44% |
| 2024-01-04 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 369 | 99.7% | 55% | 13,339 | 0.0% | 41% |
| 2024-01-04 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 677 | 99.9% | 38% | 7,712 | 0.0% | 34% |
| 2024-01-04 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,826 | 99.9% | 24% | 3,036 | 0.0% | 20% |
| 2024-01-04 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 10,728 | 100.0% | 27% | 664 | 0.0% | 26% |
| 2024-01-04 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 419 | 100.0% | 81% | 142 | 0.0% | 51% |
| 2024-01-05 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 8,455 | 100.0% | 43% | 982 | 0.1% | 33% |
| 2024-01-05 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,893 | 100.0% | 41% | 798 | 0.1% | 30% |
| 2024-01-05 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,610 | 100.0% | 36% | 678 | 0.0% | 28% |
| 2024-01-05 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 7,483 | 100.0% | 42% | 541 | 0.1% | 34% |
| 2024-01-05 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 413 | 100.0% | 84% | 236 | 1.0% | 43% |
| 2024-01-06 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 428 | 99.8% | 44% | 27,927 | 0.0% | 33% |
| 2024-01-06 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 1,270 | 99.9% | 16% | 5,006 | 0.0% | 17% |
| 2024-01-06 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,935 | 100.0% | 16% | 2,174 | 0.0% | 21% |
| 2024-01-06 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,262 | 100.0% | 45% | 480 | 0.1% | 42% |
| 2024-01-06 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 5 | 100.0% | 60% | 166 | 0.0% | 20% |
| 2024-01-07 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 383 | 99.7% | 45% | 12,240 | 0.0% | 31% |
| 2024-01-07 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 812 | 99.9% | 27% | 3,794 | 0.0% | 22% |
| 2024-01-07 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,299 | 100.0% | 16% | 2,482 | 0.0% | 18% |
| 2024-01-07 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,612 | 100.0% | 30% | 760 | 0.0% | 31% |
| 2024-01-07 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 12 | 100.0% | 67% | 118 | 0.0% | 67% |
| 2024-01-08 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 18,169 | 100.0% | 39% | 678 | 0.8% | 29% |
| 2024-01-08 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 17,848 | 100.0% | 40% | 520 | 0.9% | 30% |
| 2024-01-08 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 15,354 | 100.0% | 43% | 375 | 1.0% | 31% |
| 2024-01-08 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 6,901 | 100.0% | 45% | 370 | 1.5% | 35% |
| 2024-01-08 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 251 | 100.0% | 80% | 252 | 15.5% | 46% |
| 2024-01-09 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 17,589 | 100.0% | 52% | 732 | 5.6% | 34% |
| 2024-01-09 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 20,534 | 100.0% | 45% | 558 | 5.1% | 30% |
| 2024-01-09 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 22,289 | 100.0% | 46% | 390 | 4.5% | 31% |
| 2024-01-09 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 8,564 | 100.0% | 67% | 250 | 10.5% | 40% |
| 2024-01-09 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 1,226 | 100.0% | 80% | 253 | 53.8% | 42% |
| 2024-01-10 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 32,020 | 100.0% | 51% | 480 | 0.3% | 34% |
| 2024-01-10 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 35,201 | 100.0% | 48% | 376 | 0.3% | 31% |
| 2024-01-10 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 38,629 | 100.0% | 48% | 336 | 0.2% | 31% |
| 2024-01-10 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 11,179 | 100.0% | 77% | 172 | 1.1% | 45% |
| 2024-01-10 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 882 | 100.0% | 88% | 170 | 10.2% | 47% |
| 2024-01-11 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 47,688 | 100.0% | 47% | 452 | 0.4% | 30% |
| 2024-01-11 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 42,977 | 100.0% | 51% | 358 | 0.4% | 32% |
| 2024-01-11 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 28,866 | 100.0% | 59% | 301 | 0.5% | 36% |
| 2024-01-11 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 2,604 | 100.0% | 80% | 164 | 3.4% | 49% |
| 2024-01-11 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 169 | 100.0% | 88% | 137 | 8.3% | 39% |
| 2024-01-12 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 31,507 | 100.0% | 49% | 471 | 0.7% | 31% |
| 2024-01-12 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 30,991 | 100.0% | 48% | 556 | 0.7% | 30% |
| 2024-01-12 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 28,719 | 100.0% | 46% | 419 | 0.7% | 31% |
| 2024-01-12 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 3,913 | 100.0% | 72% | 198 | 3.7% | 44% |
| 2024-01-12 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 271 | 100.0% | 80% | 192 | 45.4% | 42% |
| 2024-01-13 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 12,283 | 100.0% | 28% | 1,598 | 0.0% | 28% |
| 2024-01-13 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,046 | 100.0% | 29% | 904 | 0.0% | 29% |
| 2024-01-13 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,905 | 100.0% | 32% | 662 | 0.0% | 32% |
| 2024-01-13 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 288 | 100.0% | 86% | 116 | 0.0% | 56% |
| 2024-01-13 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 18 | 100.0% | 78% | 117 | 0.0% | 67% |
| 2024-01-14 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,364 | 100.0% | 29% | 1,300 | 0.0% | 28% |
| 2024-01-14 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,032 | 100.0% | 31% | 1,130 | 0.0% | 27% |
| 2024-01-14 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 6,770 | 100.0% | 39% | 1,499 | 0.0% | 30% |
| 2024-01-14 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 558 | 100.0% | 63% | 263 | 0.0% | 47% |
| 2024-01-14 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 30 | 100.0% | 83% | 502 | 3.3% | 37% |
| 2024-01-15 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,670 | 100.0% | 28% | 1,421 | 0.0% | 28% |
| 2024-01-15 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 12,075 | 100.0% | 33% | 1,030 | 0.0% | 29% |
| 2024-01-15 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 7,662 | 100.0% | 36% | 892 | 0.0% | 32% |
| 2024-01-15 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 475 | 100.0% | 83% | 124 | 0.2% | 49% |
| 2024-01-15 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 19 | 100.0% | 89% | 360 | 0.0% | 37% |
| 2024-01-16 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 18,100 | 100.0% | 28% | 1,212 | 0.0% | 27% |
| 2024-01-16 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 15,275 | 100.0% | 34% | 842 | 0.0% | 30% |
| 2024-01-16 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,447 | 100.0% | 45% | 521 | 0.0% | 34% |
| 2024-01-16 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 644 | 100.0% | 84% | 138 | 0.3% | 49% |
| 2024-01-16 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 13 | 100.0% | 92% | 111 | 0.0% | 62% |
| 2024-01-17 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 15,103 | 100.0% | 26% | 1,413 | 0.0% | 28% |
| 2024-01-17 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,979 | 100.0% | 33% | 1,048 | 0.0% | 31% |
| 2024-01-17 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,806 | 100.0% | 41% | 718 | 0.0% | 36% |
| 2024-01-17 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 173 | 100.0% | 88% | 121 | 0.0% | 55% |
| 2024-01-17 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 17 | 100.0% | 88% | 108 | 0.0% | 41% |
| 2024-01-18 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,031 | 100.0% | 32% | 1,350 | 0.1% | 29% |
| 2024-01-18 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 13,920 | 100.0% | 33% | 1,017 | 0.1% | 27% |
| 2024-01-18 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 12,896 | 100.0% | 36% | 416 | 0.1% | 29% |
| 2024-01-18 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,000 | 100.0% | 80% | 211 | 0.7% | 50% |
| 2024-01-18 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 44 | 100.0% | 89% | 160 | 34.1% | 55% |
| 2024-01-19 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 18,229 | 100.0% | 35% | 1,037 | 0.0% | 28% |
| 2024-01-19 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 18,670 | 100.0% | 35% | 660 | 0.0% | 28% |
| 2024-01-19 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,204 | 100.0% | 43% | 392 | 0.0% | 34% |
| 2024-01-19 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 687 | 100.0% | 83% | 162 | 0.0% | 50% |
| 2024-01-19 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 30 | 100.0% | 80% | 139 | 0.0% | 27% |
| 2024-01-20 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 6,391 | 100.0% | 21% | 4,307 | 0.0% | 30% |
| 2024-01-20 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 4,709 | 100.0% | 28% | 2,399 | 0.0% | 33% |
| 2024-01-20 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 1,891 | 100.0% | 41% | 1,002 | 0.0% | 41% |
| 2024-01-20 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 34 | 100.0% | 85% | 125 | 0.0% | 50% |
| 2024-01-20 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 2 | 100.0% | 100% | none resolved | 0.0% | 0% |
| 2024-01-21 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 3,581 | 100.0% | 20% | 5,900 | 0.0% | 28% |
| 2024-01-21 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 2,841 | 100.0% | 26% | 2,727 | 0.0% | 34% |
| 2024-01-21 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 899 | 100.0% | 45% | 916 | 0.0% | 43% |
| 2024-01-21 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 15 | 100.0% | 87% | 156 | 0.0% | 40% |
| 2024-01-21 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 0% |
| 2024-01-22 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 27,404 | 100.0% | 36% | 798 | 0.5% | 27% |
| 2024-01-22 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 25,445 | 100.0% | 38% | 700 | 0.5% | 28% |
| 2024-01-22 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 18,119 | 100.0% | 45% | 498 | 0.6% | 32% |
| 2024-01-22 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 1,010 | 100.0% | 90% | 124 | 5.9% | 47% |
| 2024-01-22 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 70 | 100.0% | 89% | 620 | 32.9% | 47% |
| 2024-01-23 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 21,843 | 100.0% | 29% | 1,030 | 0.1% | 27% |
| 2024-01-23 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 19,719 | 100.0% | 33% | 688 | 0.1% | 28% |
| 2024-01-23 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 15,222 | 100.0% | 36% | 482 | 0.0% | 29% |
| 2024-01-23 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 594 | 100.0% | 85% | 114 | 0.7% | 49% |
| 2024-01-23 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 8 | 100.0% | 100% | none resolved | 0.0% | 12% |
| 2024-01-24 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,473 | 100.0% | 26% | 1,440 | 0.0% | 28% |
| 2024-01-24 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 13,901 | 100.0% | 29% | 962 | 0.0% | 29% |
| 2024-01-24 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 8,390 | 100.0% | 37% | 745 | 0.0% | 33% |
| 2024-01-24 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 221 | 100.0% | 86% | 116 | 0.0% | 49% |
| 2024-01-24 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 0% |
| 2024-01-25 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 13,381 | 100.0% | 23% | 1,600 | 0.0% | 27% |
| 2024-01-25 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 10,195 | 100.0% | 32% | 1,000 | 0.0% | 32% |
| 2024-01-25 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 4,203 | 100.0% | 43% | 756 | 0.0% | 36% |
| 2024-01-25 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 68 | 100.0% | 87% | 123 | 0.0% | 51% |
| 2024-01-25 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 6 | 100.0% | 83% | 102 | 0.0% | 33% |
| 2024-01-26 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 15,139 | 100.0% | 27% | 1,304 | 0.1% | 28% |
| 2024-01-26 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 13,672 | 100.0% | 31% | 826 | 0.1% | 28% |
| 2024-01-26 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 9,316 | 100.0% | 39% | 394 | 0.2% | 32% |
| 2024-01-26 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 535 | 100.0% | 86% | 127 | 4.7% | 49% |
| 2024-01-26 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 26 | 100.0% | 69% | 249 | 7.7% | 42% |
| 2024-01-27 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 4,522 | 100.0% | 19% | 3,939 | 0.1% | 29% |
| 2024-01-27 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 3,528 | 100.0% | 22% | 2,560 | 0.1% | 32% |
| 2024-01-27 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 2,011 | 100.0% | 32% | 1,600 | 0.0% | 34% |
| 2024-01-27 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 56 | 100.0% | 95% | 102 | 0.0% | 52% |
| 2024-01-28 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 10,627 | 100.0% | 21% | 2,118 | 0.1% | 27% |
| 2024-01-28 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 8,130 | 100.0% | 29% | 1,155 | 0.1% | 32% |
| 2024-01-28 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 3,762 | 100.0% | 39% | 649 | 0.1% | 36% |
| 2024-01-28 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 114 | 100.0% | 83% | 130 | 1.8% | 53% |
| 2024-01-28 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 5 | 100.0% | 80% | 197 | 0.0% | 60% |
| 2024-01-29 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 14,505 | 100.0% | 25% | 1,188 | 0.0% | 29% |
| 2024-01-29 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,175 | 100.0% | 32% | 956 | 0.0% | 31% |
| 2024-01-29 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,966 | 100.0% | 39% | 568 | 0.1% | 34% |
| 2024-01-29 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 102 | 100.0% | 88% | 350 | 1.0% | 63% |
| 2024-01-29 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 4 | 100.0% | 50% | 176 | 0.0% | 50% |
| 2024-01-30 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 12,353 | 100.0% | 26% | 1,541 | 0.0% | 29% |
| 2024-01-30 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 11,492 | 100.0% | 28% | 1,113 | 0.0% | 30% |
| 2024-01-30 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 5,958 | 100.0% | 41% | 538 | 0.1% | 34% |
| 2024-01-30 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 191 | 100.0% | 85% | 129 | 0.0% | 46% |
| 2024-01-30 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 6 | 100.0% | 100% | none resolved | 0.0% | 83% |
| 2024-01-31 | btc_perp_binance_bybit | ok | 1.000 | gross>0bps | 7,160 | 100.0% | 30% | 1,918 | 0.0% | 28% |
| 2024-01-31 | btc_perp_binance_bybit | ok | 1.000 | gross>1bps | 9,240 | 100.0% | 23% | 950 | 0.0% | 24% |
| 2024-01-31 | btc_perp_binance_bybit | ok | 1.000 | gross>2bps | 11,041 | 100.0% | 27% | 531 | 0.0% | 25% |
| 2024-01-31 | btc_perp_binance_bybit | ok | 1.000 | gross>5bps | 894 | 100.0% | 72% | 120 | 0.0% | 47% |
| 2024-01-31 | btc_perp_binance_bybit | ok | 1.000 | retail_taker | 8 | 100.0% | 88% | 105 | 0.0% | 50% |
| 2026-09-07 | bybit_btc_basis | ok | 1.000 | gross>0bps | 15,099 | 100.0% | 34% | 2,994 | 0.0% | 41% |
| 2026-09-07 | bybit_btc_basis | ok | 1.000 | gross>1bps | 2,606 | 100.0% | 70% | 1,042 | 0.0% | 56% |
| 2026-09-07 | bybit_btc_basis | ok | 1.000 | gross>2bps | 293 | 100.0% | 98% | 1,171 | 0.0% | 92% |
| 2026-09-07 | bybit_btc_basis | ok | 1.000 | gross>5bps | 15 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2026-09-07 | bybit_eth_basis | ok | 1.000 | gross>0bps | 29,122 | 100.0% | 27% | 1,450 | 0.0% | 56% |
| 2026-09-07 | bybit_eth_basis | ok | 1.000 | gross>1bps | 7,638 | 100.0% | 75% | 410 | 0.0% | 75% |
| 2026-09-07 | bybit_eth_basis | ok | 1.000 | gross>2bps | 883 | 100.0% | 96% | 141 | 0.0% | 80% |
| 2026-09-07 | bybit_eth_basis | ok | 1.000 | gross>5bps | 69 | 100.0% | 100% | none resolved | 0.0% | 91% |
| 2026-09-07 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 29,308 | 100.0% | 16% | 1,700 | 0.0% | 27% |
| 2026-09-07 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 8,298 | 100.0% | 45% | 298 | 0.0% | 24% |
| 2026-09-07 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 1,205 | 100.0% | 65% | 200 | 0.0% | 32% |
| 2026-09-07 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 40 | 100.0% | 90% | 249 | 0.0% | 40% |
| 2026-09-08 | bybit_btc_basis | ok | 1.000 | gross>0bps | 23,286 | 100.0% | 34% | 2,088 | 0.0% | 40% |
| 2026-09-08 | bybit_btc_basis | ok | 1.000 | gross>1bps | 3,993 | 100.0% | 66% | 992 | 0.0% | 51% |
| 2026-09-08 | bybit_btc_basis | ok | 1.000 | gross>2bps | 425 | 100.0% | 93% | 1,186 | 0.0% | 90% |
| 2026-09-08 | bybit_btc_basis | ok | 1.000 | gross>5bps | 42 | 100.0% | 60% | 2,223 | 0.0% | 67% |
| 2026-09-08 | bybit_eth_basis | ok | 1.000 | gross>0bps | 36,126 | 100.0% | 29% | 1,190 | 0.0% | 58% |
| 2026-09-08 | bybit_eth_basis | ok | 1.000 | gross>1bps | 10,009 | 100.0% | 75% | 362 | 0.0% | 78% |
| 2026-09-08 | bybit_eth_basis | ok | 1.000 | gross>2bps | 1,122 | 100.0% | 96% | 194 | 0.0% | 78% |
| 2026-09-08 | bybit_eth_basis | ok | 1.000 | gross>5bps | 92 | 100.0% | 100% | none resolved | 0.0% | 91% |
| 2026-09-08 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 41,319 | 100.0% | 20% | 1,342 | 0.0% | 32% |
| 2026-09-08 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 9,882 | 100.0% | 51% | 296 | 0.0% | 31% |
| 2026-09-08 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 1,384 | 100.0% | 65% | 200 | 0.0% | 34% |
| 2026-09-08 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 59 | 100.0% | 78% | 247 | 0.0% | 46% |
| 2026-09-09 | bybit_btc_basis | ok | 1.000 | gross>0bps | 26,011 | 100.0% | 35% | 1,794 | 0.0% | 39% |
| 2026-09-09 | bybit_btc_basis | ok | 1.000 | gross>1bps | 5,511 | 100.0% | 63% | 693 | 0.0% | 47% |
| 2026-09-09 | bybit_btc_basis | ok | 1.000 | gross>2bps | 616 | 100.0% | 94% | 204 | 0.0% | 88% |
| 2026-09-09 | bybit_btc_basis | ok | 1.000 | gross>5bps | 35 | 100.0% | 100% | none resolved | 0.0% | 97% |
| 2026-09-09 | bybit_eth_basis | ok | 1.000 | gross>0bps | 39,588 | 100.0% | 31% | 1,079 | 0.0% | 58% |
| 2026-09-09 | bybit_eth_basis | ok | 1.000 | gross>1bps | 10,586 | 100.0% | 77% | 360 | 0.0% | 80% |
| 2026-09-09 | bybit_eth_basis | ok | 1.000 | gross>2bps | 1,245 | 100.0% | 96% | 110 | 0.0% | 80% |
| 2026-09-09 | bybit_eth_basis | ok | 1.000 | gross>5bps | 74 | 100.0% | 99% | 100 | 0.0% | 93% |
| 2026-09-09 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 43,995 | 100.0% | 22% | 1,298 | 0.0% | 34% |
| 2026-09-09 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 10,869 | 100.0% | 54% | 296 | 0.0% | 33% |
| 2026-09-09 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 1,576 | 100.0% | 65% | 199 | 0.0% | 35% |
| 2026-09-09 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 56 | 100.0% | 80% | 148 | 0.0% | 46% |
| 2026-09-10 | bybit_btc_basis | ok | 1.000 | gross>0bps | 26,316 | 100.0% | 34% | 1,736 | 0.0% | 37% |
| 2026-09-10 | bybit_btc_basis | ok | 1.000 | gross>1bps | 5,519 | 100.0% | 61% | 644 | 0.0% | 45% |
| 2026-09-10 | bybit_btc_basis | ok | 1.000 | gross>2bps | 615 | 100.0% | 94% | 550 | 0.0% | 86% |
| 2026-09-10 | bybit_btc_basis | ok | 1.000 | gross>5bps | 46 | 100.0% | 89% | 186 | 0.0% | 85% |
| 2026-09-10 | bybit_eth_basis | ok | 1.000 | gross>0bps | 41,491 | 100.0% | 30% | 939 | 0.0% | 56% |
| 2026-09-10 | bybit_eth_basis | ok | 1.000 | gross>1bps | 11,041 | 100.0% | 76% | 306 | 0.0% | 74% |
| 2026-09-10 | bybit_eth_basis | ok | 1.000 | gross>2bps | 1,488 | 100.0% | 91% | 200 | 0.0% | 76% |
| 2026-09-10 | bybit_eth_basis | ok | 1.000 | gross>5bps | 139 | 100.0% | 98% | 120 | 0.0% | 88% |
| 2026-09-10 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 45,831 | 100.0% | 21% | 1,151 | 0.0% | 34% |
| 2026-09-10 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 10,920 | 100.0% | 53% | 249 | 0.0% | 34% |
| 2026-09-10 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 1,785 | 100.0% | 66% | 200 | 0.0% | 37% |
| 2026-09-10 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 141 | 100.0% | 80% | 150 | 0.0% | 40% |
| 2026-09-10 | bybit_eth_btc_ratio | ok | 1.000 | retail_taker | 1 | 100.0% | 0% | 102 | 0.0% | 0% |
| 2026-09-11 | bybit_btc_basis | ok | 1.000 | gross>0bps | 37,350 | 100.0% | 39% | 899 | 0.0% | 41% |
| 2026-09-11 | bybit_btc_basis | ok | 1.000 | gross>1bps | 9,901 | 100.0% | 72% | 387 | 0.0% | 58% |
| 2026-09-11 | bybit_btc_basis | ok | 1.000 | gross>2bps | 1,696 | 100.0% | 91% | 186 | 0.0% | 84% |
| 2026-09-11 | bybit_btc_basis | ok | 1.000 | gross>5bps | 102 | 100.0% | 90% | 100 | 0.0% | 88% |
| 2026-09-11 | bybit_eth_basis | ok | 1.000 | gross>0bps | 60,257 | 100.0% | 39% | 590 | 0.0% | 55% |
| 2026-09-11 | bybit_eth_basis | ok | 1.000 | gross>1bps | 24,535 | 100.0% | 72% | 221 | 0.0% | 71% |
| 2026-09-11 | bybit_eth_basis | ok | 1.000 | gross>2bps | 6,144 | 100.0% | 86% | 122 | 0.0% | 76% |
| 2026-09-11 | bybit_eth_basis | ok | 1.000 | gross>5bps | 429 | 100.0% | 95% | 120 | 0.0% | 86% |
| 2026-09-11 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 54,107 | 100.0% | 25% | 901 | 0.0% | 34% |
| 2026-09-11 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 23,151 | 100.0% | 51% | 297 | 0.0% | 34% |
| 2026-09-11 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 7,218 | 100.0% | 62% | 200 | 0.0% | 37% |
| 2026-09-11 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 772 | 100.0% | 68% | 200 | 0.0% | 37% |
| 2026-09-11 | bybit_eth_btc_ratio | ok | 1.000 | retail_taker | 16 | 100.0% | 75% | 242 | 0.0% | 19% |
| 2026-09-12 | bybit_btc_basis | ok | 1.000 | gross>0bps | 3,338 | 100.0% | 30% | 12,900 | 0.0% | 45% |
| 2026-09-12 | bybit_btc_basis | ok | 1.000 | gross>1bps | 697 | 100.0% | 70% | 4,336 | 0.0% | 65% |
| 2026-09-12 | bybit_btc_basis | ok | 1.000 | gross>2bps | 160 | 100.0% | 99% | 2,144 | 0.0% | 95% |
| 2026-09-12 | bybit_btc_basis | ok | 1.000 | gross>5bps | 6 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2026-09-12 | bybit_eth_basis | ok | 1.000 | gross>0bps | 10,053 | 100.0% | 27% | 3,600 | 0.0% | 56% |
| 2026-09-12 | bybit_eth_basis | ok | 1.000 | gross>1bps | 2,561 | 100.0% | 78% | 922 | 0.0% | 78% |
| 2026-09-12 | bybit_eth_basis | ok | 1.000 | gross>2bps | 376 | 100.0% | 98% | 207 | 0.0% | 81% |
| 2026-09-12 | bybit_eth_basis | ok | 1.000 | gross>5bps | 61 | 100.0% | 100% | none resolved | 0.0% | 79% |
| 2026-09-12 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 10,040 | 100.0% | 9% | 2,549 | 0.0% | 23% |
| 2026-09-12 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 3,130 | 100.0% | 33% | 300 | 0.0% | 20% |
| 2026-09-12 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 674 | 100.0% | 57% | 296 | 0.0% | 27% |
| 2026-09-12 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 35 | 100.0% | 83% | 272 | 0.0% | 49% |
| 2026-09-13 | bybit_btc_basis | ok | 1.000 | gross>0bps | 8,676 | 100.0% | 32% | 3,493 | 0.0% | 42% |
| 2026-09-13 | bybit_btc_basis | ok | 1.000 | gross>1bps | 1,598 | 99.9% | 66% | 1,042 | 0.0% | 55% |
| 2026-09-13 | bybit_btc_basis | ok | 1.000 | gross>2bps | 170 | 99.4% | 99% | 942 | 0.0% | 95% |
| 2026-09-13 | bybit_btc_basis | ok | 1.000 | gross>5bps | 6 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2026-09-13 | bybit_eth_basis | ok | 1.000 | gross>0bps | 18,631 | 100.0% | 30% | 1,589 | 0.0% | 55% |
| 2026-09-13 | bybit_eth_basis | ok | 1.000 | gross>1bps | 5,640 | 100.0% | 72% | 438 | 0.0% | 75% |
| 2026-09-13 | bybit_eth_basis | ok | 1.000 | gross>2bps | 868 | 100.0% | 93% | 239 | 0.0% | 75% |
| 2026-09-13 | bybit_eth_basis | ok | 1.000 | gross>5bps | 62 | 100.0% | 97% | 409 | 0.0% | 81% |
| 2026-09-13 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 17,949 | 100.0% | 15% | 1,950 | 0.0% | 29% |
| 2026-09-13 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 6,127 | 100.0% | 40% | 299 | 0.0% | 25% |
| 2026-09-13 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 1,303 | 100.0% | 58% | 201 | 0.0% | 30% |
| 2026-09-13 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 81 | 100.0% | 68% | 150 | 0.0% | 32% |
| 2026-09-13 | bybit_eth_btc_ratio | ok | 1.000 | retail_taker | 3 | 100.0% | 67% | 396 | 0.0% | 33% |
| 2026-09-14 | bybit_btc_basis | ok | 1.000 | gross>0bps | 32,104 | 100.0% | 35% | 1,500 | 0.0% | 40% |
| 2026-09-14 | bybit_btc_basis | ok | 1.000 | gross>1bps | 5,595 | 100.0% | 70% | 693 | 0.0% | 54% |
| 2026-09-14 | bybit_btc_basis | ok | 1.000 | gross>2bps | 637 | 100.0% | 99% | 192 | 0.0% | 94% |
| 2026-09-14 | bybit_btc_basis | ok | 1.000 | gross>5bps | 36 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2026-09-14 | bybit_eth_basis | ok | 1.000 | gross>0bps | 52,169 | 100.0% | 32% | 812 | 0.0% | 55% |
| 2026-09-14 | bybit_eth_basis | ok | 1.000 | gross>1bps | 16,311 | 100.0% | 74% | 320 | 0.0% | 74% |
| 2026-09-14 | bybit_eth_basis | ok | 1.000 | gross>2bps | 2,558 | 100.0% | 91% | 150 | 0.0% | 78% |
| 2026-09-14 | bybit_eth_basis | ok | 1.000 | gross>5bps | 171 | 100.0% | 100% | none resolved | 0.0% | 83% |
| 2026-09-14 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 51,810 | 100.0% | 22% | 1,100 | 0.0% | 33% |
| 2026-09-14 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 16,417 | 100.0% | 50% | 297 | 0.0% | 31% |
| 2026-09-14 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 3,287 | 100.0% | 64% | 200 | 0.0% | 33% |
| 2026-09-14 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 148 | 100.0% | 79% | 198 | 0.0% | 43% |
| 2026-09-15 | bybit_btc_basis | ok | 1.000 | gross>0bps | 39,524 | 100.0% | 39% | 996 | 0.0% | 42% |
| 2026-09-15 | bybit_btc_basis | ok | 1.000 | gross>1bps | 9,631 | 100.0% | 76% | 393 | 0.0% | 64% |
| 2026-09-15 | bybit_btc_basis | ok | 1.000 | gross>2bps | 1,664 | 100.0% | 97% | 144 | 0.0% | 89% |
| 2026-09-15 | bybit_btc_basis | ok | 1.000 | gross>5bps | 89 | 100.0% | 100% | none resolved | 0.0% | 98% |
| 2026-09-15 | bybit_eth_basis | ok | 1.000 | gross>0bps | 61,995 | 100.0% | 35% | 602 | 0.0% | 54% |
| 2026-09-15 | bybit_eth_basis | ok | 1.000 | gross>1bps | 20,184 | 100.0% | 76% | 200 | 0.0% | 71% |
| 2026-09-15 | bybit_eth_basis | ok | 1.000 | gross>2bps | 4,262 | 100.0% | 91% | 121 | 0.0% | 77% |
| 2026-09-15 | bybit_eth_basis | ok | 1.000 | gross>5bps | 326 | 100.0% | 98% | 189 | 0.0% | 87% |
| 2026-09-15 | bybit_eth_basis | ok | 1.000 | retail_taker | 6 | 100.0% | 50% | 221 | 0.0% | 100% |
| 2026-09-15 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 57,547 | 100.0% | 26% | 998 | 0.0% | 35% |
| 2026-09-15 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 20,248 | 100.0% | 56% | 200 | 0.0% | 39% |
| 2026-09-15 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 5,449 | 100.0% | 70% | 199 | 0.0% | 48% |
| 2026-09-15 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 458 | 100.0% | 79% | 198 | 0.0% | 59% |
| 2026-09-15 | bybit_eth_btc_ratio | ok | 1.000 | retail_taker | 7 | 100.0% | 57% | 196 | 0.0% | 0% |
| 2026-09-16 | bybit_btc_basis | ok | 1.000 | gross>0bps | 41,235 | 100.0% | 38% | 895 | 0.0% | 41% |
| 2026-09-16 | bybit_btc_basis | ok | 1.000 | gross>1bps | 9,103 | 100.0% | 75% | 394 | 0.0% | 62% |
| 2026-09-16 | bybit_btc_basis | ok | 1.000 | gross>2bps | 1,355 | 100.0% | 96% | 149 | 0.0% | 90% |
| 2026-09-16 | bybit_btc_basis | ok | 1.000 | gross>5bps | 68 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2026-09-16 | bybit_eth_basis | ok | 1.000 | gross>0bps | 63,838 | 100.0% | 36% | 600 | 0.0% | 55% |
| 2026-09-16 | bybit_eth_basis | ok | 1.000 | gross>1bps | 22,609 | 100.0% | 78% | 211 | 0.0% | 75% |
| 2026-09-16 | bybit_eth_basis | ok | 1.000 | gross>2bps | 3,802 | 100.0% | 95% | 116 | 0.0% | 83% |
| 2026-09-16 | bybit_eth_basis | ok | 1.000 | gross>5bps | 233 | 100.0% | 100% | 278 | 0.0% | 87% |
| 2026-09-16 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 63,582 | 100.0% | 28% | 850 | 0.0% | 35% |
| 2026-09-16 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 21,425 | 100.0% | 59% | 200 | 0.0% | 39% |
| 2026-09-16 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 4,951 | 100.0% | 73% | 198 | 0.0% | 51% |
| 2026-09-16 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 286 | 100.0% | 84% | 196 | 0.0% | 55% |
| 2026-09-17 | bybit_btc_basis | ok | 1.000 | gross>0bps | 24,518 | 100.0% | 33% | 1,800 | 0.0% | 38% |
| 2026-09-17 | bybit_btc_basis | ok | 1.000 | gross>1bps | 4,091 | 100.0% | 61% | 744 | 0.0% | 44% |
| 2026-09-17 | bybit_btc_basis | ok | 1.000 | gross>2bps | 360 | 100.0% | 99% | 522 | 0.0% | 94% |
| 2026-09-17 | bybit_btc_basis | ok | 1.000 | gross>5bps | 18 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2026-09-17 | bybit_eth_basis | ok | 1.000 | gross>0bps | 40,679 | 100.0% | 29% | 1,000 | 0.0% | 58% |
| 2026-09-17 | bybit_eth_basis | ok | 1.000 | gross>1bps | 12,531 | 100.0% | 73% | 322 | 0.0% | 78% |
| 2026-09-17 | bybit_eth_basis | ok | 1.000 | gross>2bps | 1,375 | 100.0% | 97% | 151 | 0.0% | 82% |
| 2026-09-17 | bybit_eth_basis | ok | 1.000 | gross>5bps | 103 | 100.0% | 100% | none resolved | 0.0% | 84% |
| 2026-09-17 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 45,900 | 100.0% | 22% | 1,199 | 0.0% | 32% |
| 2026-09-17 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 11,836 | 100.0% | 53% | 248 | 0.0% | 32% |
| 2026-09-17 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 1,685 | 100.0% | 69% | 199 | 0.0% | 37% |
| 2026-09-17 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 74 | 100.0% | 82% | 198 | 0.0% | 43% |
| 2026-09-18 | bybit_btc_basis | ok | 1.000 | gross>0bps | 33,648 | 100.0% | 36% | 1,336 | 0.0% | 40% |
| 2026-09-18 | bybit_btc_basis | ok | 1.000 | gross>1bps | 8,048 | 100.0% | 65% | 456 | 0.0% | 52% |
| 2026-09-18 | bybit_btc_basis | ok | 1.000 | gross>2bps | 1,110 | 100.0% | 93% | 199 | 0.0% | 83% |
| 2026-09-18 | bybit_btc_basis | ok | 1.000 | gross>5bps | 42 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2026-09-18 | bybit_eth_basis | ok | 1.000 | gross>0bps | 61,461 | 100.0% | 32% | 700 | 0.0% | 55% |
| 2026-09-18 | bybit_eth_basis | ok | 1.000 | gross>1bps | 21,517 | 100.0% | 70% | 300 | 0.0% | 71% |
| 2026-09-18 | bybit_eth_basis | ok | 1.000 | gross>2bps | 3,265 | 100.0% | 91% | 160 | 0.0% | 78% |
| 2026-09-18 | bybit_eth_basis | ok | 1.000 | gross>5bps | 206 | 100.0% | 100% | 101 | 0.0% | 85% |
| 2026-09-18 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 61,072 | 100.0% | 23% | 901 | 0.0% | 32% |
| 2026-09-18 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 20,443 | 100.0% | 56% | 200 | 0.0% | 32% |
| 2026-09-18 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 3,507 | 100.0% | 70% | 199 | 0.0% | 39% |
| 2026-09-18 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 149 | 100.0% | 85% | 198 | 0.0% | 44% |
| 2026-09-19 | bybit_btc_basis | ok | 1.000 | gross>0bps | 10,986 | 100.0% | 32% | 3,857 | 0.0% | 41% |
| 2026-09-19 | bybit_btc_basis | ok | 1.000 | gross>1bps | 2,569 | 100.0% | 58% | 1,550 | 0.0% | 45% |
| 2026-09-19 | bybit_btc_basis | ok | 1.000 | gross>2bps | 263 | 100.0% | 98% | 200 | 0.0% | 92% |
| 2026-09-19 | bybit_btc_basis | ok | 1.000 | gross>5bps | 18 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2026-09-19 | bybit_eth_basis | ok | 1.000 | gross>0bps | 25,556 | 100.0% | 26% | 1,688 | 0.0% | 55% |
| 2026-09-19 | bybit_eth_basis | ok | 1.000 | gross>1bps | 6,968 | 100.0% | 66% | 528 | 0.0% | 76% |
| 2026-09-19 | bybit_eth_basis | ok | 1.000 | gross>2bps | 1,074 | 100.0% | 90% | 240 | 0.0% | 76% |
| 2026-09-19 | bybit_eth_basis | ok | 1.000 | gross>5bps | 111 | 100.0% | 100% | none resolved | 0.0% | 87% |
| 2026-09-19 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 24,873 | 100.0% | 13% | 2,000 | 0.0% | 26% |
| 2026-09-19 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 7,558 | 100.0% | 39% | 298 | 0.0% | 22% |
| 2026-09-19 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 1,270 | 100.0% | 56% | 248 | 0.0% | 26% |
| 2026-09-19 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 105 | 100.0% | 59% | 198 | 0.0% | 28% |
| 2026-09-19 | bybit_eth_btc_ratio | ok | 1.000 | retail_taker | 2 | 100.0% | 50% | 396 | 0.0% | 0% |
| 2026-09-20 | bybit_btc_basis | ok | 1.000 | gross>0bps | 16,963 | 100.0% | 32% | 2,400 | 0.0% | 40% |
| 2026-09-20 | bybit_btc_basis | ok | 1.000 | gross>1bps | 3,282 | 100.0% | 60% | 1,037 | 0.0% | 46% |
| 2026-09-20 | bybit_btc_basis | ok | 1.000 | gross>2bps | 347 | 100.0% | 93% | 521 | 0.0% | 86% |
| 2026-09-20 | bybit_btc_basis | ok | 1.000 | gross>5bps | 17 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2026-09-20 | bybit_eth_basis | ok | 1.000 | gross>0bps | 35,931 | 100.0% | 28% | 1,100 | 0.0% | 55% |
| 2026-09-20 | bybit_eth_basis | ok | 1.000 | gross>1bps | 12,043 | 100.0% | 67% | 389 | 0.0% | 72% |
| 2026-09-20 | bybit_eth_basis | ok | 1.000 | gross>2bps | 1,874 | 100.0% | 87% | 179 | 0.0% | 74% |
| 2026-09-20 | bybit_eth_basis | ok | 1.000 | gross>5bps | 105 | 100.0% | 100% | none resolved | 0.0% | 89% |
| 2026-09-20 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 33,805 | 100.0% | 16% | 1,648 | 0.0% | 27% |
| 2026-09-20 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 12,021 | 100.0% | 42% | 298 | 0.0% | 22% |
| 2026-09-20 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 2,175 | 100.0% | 58% | 200 | 0.0% | 26% |
| 2026-09-20 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 112 | 100.0% | 71% | 199 | 0.0% | 27% |
| 2026-09-21 | bybit_btc_basis | ok | 1.000 | gross>0bps | 47,566 | 100.0% | 37% | 1,000 | 0.0% | 43% |
| 2026-09-21 | bybit_btc_basis | ok | 1.000 | gross>1bps | 12,340 | 100.0% | 67% | 438 | 0.0% | 59% |
| 2026-09-21 | bybit_btc_basis | ok | 1.000 | gross>2bps | 2,085 | 100.0% | 88% | 242 | 0.0% | 82% |
| 2026-09-21 | bybit_btc_basis | ok | 1.000 | gross>5bps | 108 | 100.0% | 96% | 102 | 0.0% | 87% |
| 2026-09-21 | bybit_eth_basis | ok | 1.000 | gross>0bps | 83,689 | 100.0% | 35% | 600 | 0.0% | 51% |
| 2026-09-21 | bybit_eth_basis | ok | 1.000 | gross>1bps | 28,438 | 100.0% | 71% | 289 | 0.0% | 65% |
| 2026-09-21 | bybit_eth_basis | ok | 1.000 | gross>2bps | 4,343 | 100.0% | 90% | 150 | 0.0% | 72% |
| 2026-09-21 | bybit_eth_basis | ok | 1.000 | gross>5bps | 209 | 100.0% | 100% | 179 | 0.0% | 87% |
| 2026-09-21 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 73,034 | 100.0% | 25% | 898 | 0.0% | 33% |
| 2026-09-21 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 27,065 | 100.0% | 53% | 201 | 0.0% | 30% |
| 2026-09-21 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 5,081 | 100.0% | 64% | 200 | 0.0% | 34% |
| 2026-09-21 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 323 | 100.0% | 71% | 199 | 0.0% | 33% |
| 2026-09-21 | bybit_eth_btc_ratio | ok | 1.000 | retail_taker | 2 | 100.0% | 50% | 100 | 0.0% | 0% |
| 2026-09-22 | bybit_btc_basis | ok | 1.000 | gross>0bps | 37,630 | 100.0% | 35% | 1,401 | 0.0% | 40% |
| 2026-09-22 | bybit_btc_basis | ok | 1.000 | gross>1bps | 5,326 | 100.0% | 64% | 643 | 0.0% | 48% |
| 2026-09-22 | bybit_btc_basis | ok | 1.000 | gross>2bps | 590 | 100.0% | 97% | 196 | 0.0% | 91% |
| 2026-09-22 | bybit_btc_basis | ok | 1.000 | gross>5bps | 27 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2026-09-22 | bybit_eth_basis | ok | 1.000 | gross>0bps | 57,953 | 100.0% | 29% | 849 | 0.0% | 53% |
| 2026-09-22 | bybit_eth_basis | ok | 1.000 | gross>1bps | 15,466 | 100.0% | 74% | 322 | 0.0% | 72% |
| 2026-09-22 | bybit_eth_basis | ok | 1.000 | gross>2bps | 1,570 | 100.0% | 93% | 113 | 0.0% | 80% |
| 2026-09-22 | bybit_eth_basis | ok | 1.000 | gross>5bps | 104 | 100.0% | 100% | none resolved | 0.0% | 90% |
| 2026-09-22 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 58,446 | 100.0% | 23% | 1,050 | 0.0% | 34% |
| 2026-09-22 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 14,731 | 100.0% | 52% | 248 | 0.0% | 31% |
| 2026-09-22 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 1,760 | 100.0% | 70% | 199 | 0.0% | 41% |
| 2026-09-22 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 87 | 100.0% | 87% | 648 | 0.0% | 44% |
| 2026-09-23 | bybit_btc_basis | ok | 1.000 | gross>0bps | 34,269 | 100.0% | 36% | 1,287 | 0.0% | 42% |
| 2026-09-23 | bybit_btc_basis | ok | 1.000 | gross>1bps | 5,815 | 100.0% | 71% | 544 | 0.0% | 58% |
| 2026-09-23 | bybit_btc_basis | ok | 1.000 | gross>2bps | 630 | 100.0% | 91% | 716 | 0.0% | 87% |
| 2026-09-23 | bybit_btc_basis | ok | 1.000 | gross>5bps | 20 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2026-09-23 | bybit_eth_basis | ok | 1.000 | gross>0bps | 53,759 | 100.0% | 31% | 800 | 0.0% | 53% |
| 2026-09-23 | bybit_eth_basis | ok | 1.000 | gross>1bps | 14,654 | 100.0% | 75% | 310 | 0.0% | 73% |
| 2026-09-23 | bybit_eth_basis | ok | 1.000 | gross>2bps | 1,790 | 100.0% | 91% | 164 | 0.0% | 78% |
| 2026-09-23 | bybit_eth_basis | ok | 1.000 | gross>5bps | 108 | 100.0% | 98% | 150 | 0.0% | 90% |
| 2026-09-23 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 51,014 | 100.0% | 22% | 1,100 | 0.0% | 34% |
| 2026-09-23 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 15,177 | 100.0% | 52% | 202 | 0.0% | 32% |
| 2026-09-23 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 2,342 | 100.0% | 67% | 199 | 0.0% | 40% |
| 2026-09-23 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 127 | 100.0% | 70% | 199 | 0.0% | 31% |
| 2026-09-23 | bybit_eth_btc_ratio | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 0% |
| 2026-09-24 | bybit_btc_basis | ok | 1.000 | gross>0bps | 37,260 | 100.0% | 36% | 1,300 | 0.0% | 42% |
| 2026-09-24 | bybit_btc_basis | ok | 1.000 | gross>1bps | 5,942 | 100.0% | 71% | 543 | 0.0% | 58% |
| 2026-09-24 | bybit_btc_basis | ok | 1.000 | gross>2bps | 579 | 100.0% | 97% | 192 | 0.0% | 87% |
| 2026-09-24 | bybit_btc_basis | ok | 1.000 | gross>5bps | 16 | 100.0% | 100% | none resolved | 0.0% | 88% |
| 2026-09-24 | bybit_eth_basis | ok | 1.000 | gross>0bps | 52,425 | 100.0% | 30% | 899 | 0.0% | 54% |
| 2026-09-24 | bybit_eth_basis | ok | 1.000 | gross>1bps | 13,669 | 100.0% | 76% | 310 | 0.0% | 75% |
| 2026-09-24 | bybit_eth_basis | ok | 1.000 | gross>2bps | 1,356 | 100.0% | 96% | 122 | 0.0% | 81% |
| 2026-09-24 | bybit_eth_basis | ok | 1.000 | gross>5bps | 45 | 100.0% | 100% | none resolved | 0.0% | 80% |
| 2026-09-24 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 53,376 | 100.0% | 23% | 1,100 | 0.0% | 34% |
| 2026-09-24 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 13,660 | 100.0% | 53% | 248 | 0.0% | 32% |
| 2026-09-24 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 1,615 | 100.0% | 69% | 199 | 0.0% | 35% |
| 2026-09-24 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 68 | 100.0% | 59% | 197 | 0.0% | 25% |
| 2026-09-25 | bybit_btc_basis | ok | 1.000 | gross>0bps | 28,560 | 100.0% | 35% | 1,386 | 0.0% | 41% |
| 2026-09-25 | bybit_btc_basis | ok | 1.000 | gross>1bps | 4,865 | 100.0% | 66% | 544 | 0.0% | 50% |
| 2026-09-25 | bybit_btc_basis | ok | 1.000 | gross>2bps | 450 | 100.0% | 98% | 151 | 0.0% | 88% |
| 2026-09-25 | bybit_btc_basis | ok | 1.000 | gross>5bps | 14 | 100.0% | 100% | none resolved | 0.0% | 93% |
| 2026-09-25 | bybit_eth_basis | ok | 1.000 | gross>0bps | 42,041 | 100.0% | 29% | 900 | 0.0% | 56% |
| 2026-09-25 | bybit_eth_basis | ok | 1.000 | gross>1bps | 12,233 | 100.0% | 72% | 310 | 0.0% | 79% |
| 2026-09-25 | bybit_eth_basis | ok | 1.000 | gross>2bps | 1,463 | 100.0% | 94% | 160 | 0.0% | 85% |
| 2026-09-25 | bybit_eth_basis | ok | 1.000 | gross>5bps | 56 | 100.0% | 100% | none resolved | 0.0% | 98% |
| 2026-09-25 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 44,227 | 100.0% | 21% | 1,102 | 0.0% | 32% |
| 2026-09-25 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 12,211 | 100.0% | 51% | 202 | 0.0% | 29% |
| 2026-09-25 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 1,520 | 100.0% | 66% | 200 | 0.0% | 36% |
| 2026-09-25 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 58 | 100.0% | 72% | 224 | 0.0% | 31% |
| 2026-09-26 | bybit_btc_basis | ok | 1.000 | gross>0bps | 4,619 | 100.0% | 30% | 9,500 | 0.0% | 41% |
| 2026-09-26 | bybit_btc_basis | ok | 1.000 | gross>1bps | 1,006 | 100.0% | 56% | 3,492 | 0.0% | 42% |
| 2026-09-26 | bybit_btc_basis | ok | 1.000 | gross>2bps | 99 | 100.0% | 87% | 324 | 0.0% | 77% |
| 2026-09-26 | bybit_btc_basis | ok | 1.000 | gross>5bps | 2 | 100.0% | 100% | none resolved | 0.0% | 50% |
| 2026-09-26 | bybit_eth_basis | ok | 1.000 | gross>0bps | 9,475 | 100.0% | 25% | 3,740 | 0.0% | 54% |
| 2026-09-26 | bybit_eth_basis | ok | 1.000 | gross>1bps | 1,762 | 100.0% | 73% | 838 | 0.0% | 74% |
| 2026-09-26 | bybit_eth_basis | ok | 1.000 | gross>2bps | 237 | 100.0% | 97% | 124 | 0.0% | 84% |
| 2026-09-26 | bybit_eth_basis | ok | 1.000 | gross>5bps | 17 | 100.0% | 100% | none resolved | 0.0% | 94% |
| 2026-09-26 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 11,134 | 100.0% | 10% | 2,349 | 0.0% | 31% |
| 2026-09-26 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 2,078 | 100.0% | 38% | 298 | 0.0% | 21% |
| 2026-09-26 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 294 | 100.0% | 55% | 248 | 0.0% | 18% |
| 2026-09-26 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 9 | 100.0% | 78% | 895 | 0.0% | 22% |
| 2026-09-27 | bybit_btc_basis | ok | 1.000 | gross>0bps | 10,039 | 100.0% | 32% | 3,901 | 0.0% | 41% |
| 2026-09-27 | bybit_btc_basis | ok | 1.000 | gross>1bps | 1,846 | 100.0% | 63% | 1,718 | 0.0% | 50% |
| 2026-09-27 | bybit_btc_basis | ok | 1.000 | gross>2bps | 175 | 100.0% | 98% | 4,256 | 0.0% | 95% |
| 2026-09-27 | bybit_btc_basis | ok | 1.000 | gross>5bps | 6 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2026-09-27 | bybit_eth_basis | ok | 1.000 | gross>0bps | 17,646 | 100.0% | 26% | 1,922 | 0.0% | 56% |
| 2026-09-27 | bybit_eth_basis | ok | 1.000 | gross>1bps | 4,001 | 100.0% | 75% | 550 | 0.0% | 77% |
| 2026-09-27 | bybit_eth_basis | ok | 1.000 | gross>2bps | 434 | 99.8% | 97% | 157 | 0.0% | 79% |
| 2026-09-27 | bybit_eth_basis | ok | 1.000 | gross>5bps | 14 | 100.0% | 100% | none resolved | 0.0% | 79% |
| 2026-09-27 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 19,099 | 100.0% | 14% | 2,000 | 0.0% | 31% |
| 2026-09-27 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 4,457 | 100.0% | 43% | 298 | 0.0% | 21% |
| 2026-09-27 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 584 | 100.0% | 55% | 298 | 0.0% | 27% |
| 2026-09-27 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 24 | 100.0% | 50% | 372 | 0.0% | 25% |
| 2026-09-28 | bybit_btc_basis | ok | 1.000 | gross>0bps | 42,552 | 100.0% | 36% | 1,186 | 0.0% | 42% |
| 2026-09-28 | bybit_btc_basis | ok | 1.000 | gross>1bps | 5,561 | 100.0% | 72% | 542 | 0.0% | 58% |
| 2026-09-28 | bybit_btc_basis | ok | 1.000 | gross>2bps | 424 | 100.0% | 97% | 464 | 0.0% | 89% |
| 2026-09-28 | bybit_btc_basis | ok | 1.000 | gross>5bps | 18 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2026-09-28 | bybit_eth_basis | ok | 1.000 | gross>0bps | 52,068 | 100.0% | 30% | 851 | 0.0% | 54% |
| 2026-09-28 | bybit_eth_basis | ok | 1.000 | gross>1bps | 15,369 | 100.0% | 70% | 382 | 0.0% | 74% |
| 2026-09-28 | bybit_eth_basis | ok | 1.000 | gross>2bps | 1,511 | 99.9% | 93% | 205 | 0.0% | 79% |
| 2026-09-28 | bybit_eth_basis | ok | 1.000 | gross>5bps | 34 | 100.0% | 100% | none resolved | 0.0% | 85% |
| 2026-09-28 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 57,606 | 100.0% | 24% | 1,000 | 0.0% | 35% |
| 2026-09-28 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 14,239 | 100.0% | 54% | 200 | 0.0% | 32% |
| 2026-09-28 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 1,466 | 99.9% | 69% | 199 | 0.0% | 38% |
| 2026-09-28 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 43 | 100.0% | 81% | 271 | 0.0% | 42% |
| 2026-09-29 | bybit_btc_basis | ok | 1.000 | gross>0bps | 33,907 | 100.0% | 37% | 1,500 | 0.0% | 43% |
| 2026-09-29 | bybit_btc_basis | ok | 1.000 | gross>1bps | 3,467 | 100.0% | 76% | 644 | 0.0% | 62% |
| 2026-09-29 | bybit_btc_basis | ok | 1.000 | gross>2bps | 219 | 100.0% | 100% | 2,386 | 0.0% | 97% |
| 2026-09-29 | bybit_eth_basis | ok | 1.000 | gross>0bps | 46,911 | 100.0% | 30% | 1,000 | 0.0% | 55% |
| 2026-09-29 | bybit_eth_basis | ok | 1.000 | gross>1bps | 12,431 | 100.0% | 75% | 399 | 0.0% | 75% |
| 2026-09-29 | bybit_eth_basis | ok | 1.000 | gross>2bps | 951 | 100.0% | 96% | 202 | 0.0% | 83% |
| 2026-09-29 | bybit_eth_basis | ok | 1.000 | gross>5bps | 25 | 100.0% | 100% | none resolved | 0.0% | 92% |
| 2026-09-29 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 48,101 | 100.0% | 22% | 1,200 | 0.0% | 30% |
| 2026-09-29 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 12,089 | 100.0% | 50% | 250 | 0.0% | 24% |
| 2026-09-29 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 1,143 | 100.0% | 69% | 199 | 0.0% | 32% |
| 2026-09-29 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 42 | 100.0% | 69% | 271 | 0.0% | 14% |
| 2026-09-30 | bybit_btc_basis | ok | 1.000 | gross>0bps | 37,545 | 100.0% | 38% | 1,144 | 0.0% | 46% |
| 2026-09-30 | bybit_btc_basis | ok | 1.000 | gross>1bps | 6,260 | 100.0% | 79% | 386 | 0.0% | 73% |
| 2026-09-30 | bybit_btc_basis | ok | 1.000 | gross>2bps | 818 | 100.0% | 92% | 200 | 0.0% | 86% |
| 2026-09-30 | bybit_btc_basis | ok | 1.000 | gross>5bps | 28 | 100.0% | 96% | 101 | 0.0% | 82% |
| 2026-09-30 | bybit_eth_basis | ok | 1.000 | gross>0bps | 40,856 | 100.0% | 32% | 989 | 0.0% | 56% |
| 2026-09-30 | bybit_eth_basis | ok | 1.000 | gross>1bps | 10,689 | 100.0% | 77% | 300 | 0.0% | 76% |
| 2026-09-30 | bybit_eth_basis | ok | 1.000 | gross>2bps | 1,240 | 100.0% | 91% | 154 | 0.0% | 80% |
| 2026-09-30 | bybit_eth_basis | ok | 1.000 | gross>5bps | 37 | 100.0% | 100% | none resolved | 0.0% | 92% |
| 2026-09-30 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 45,435 | 100.0% | 23% | 1,199 | 0.0% | 30% |
| 2026-09-30 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 10,650 | 100.0% | 54% | 200 | 0.0% | 32% |
| 2026-09-30 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 1,410 | 100.0% | 68% | 199 | 0.0% | 39% |
| 2026-09-30 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 59 | 100.0% | 75% | 174 | 0.0% | 51% |
| 2026-10-01 | bybit_btc_basis | ok | 1.000 | gross>0bps | 35,320 | 100.0% | 36% | 1,192 | 0.0% | 42% |
| 2026-10-01 | bybit_btc_basis | ok | 1.000 | gross>1bps | 4,962 | 100.0% | 72% | 600 | 0.0% | 59% |
| 2026-10-01 | bybit_btc_basis | ok | 1.000 | gross>2bps | 468 | 100.0% | 85% | 2,618 | 0.0% | 84% |
| 2026-10-01 | bybit_btc_basis | ok | 1.000 | gross>5bps | 15 | 100.0% | 80% | 599 | 0.0% | 80% |
| 2026-10-01 | bybit_eth_basis | ok | 1.000 | gross>0bps | 38,783 | 100.0% | 29% | 1,022 | 0.0% | 58% |
| 2026-10-01 | bybit_eth_basis | ok | 1.000 | gross>1bps | 12,486 | 100.0% | 70% | 399 | 0.0% | 80% |
| 2026-10-01 | bybit_eth_basis | ok | 1.000 | gross>2bps | 1,195 | 100.0% | 91% | 254 | 0.0% | 83% |
| 2026-10-01 | bybit_eth_basis | ok | 1.000 | gross>5bps | 25 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2026-10-01 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 47,581 | 100.0% | 21% | 1,050 | 0.0% | 29% |
| 2026-10-01 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 11,161 | 100.0% | 53% | 248 | 0.0% | 30% |
| 2026-10-01 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 1,087 | 100.0% | 68% | 198 | 0.0% | 34% |
| 2026-10-01 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 39 | 100.0% | 72% | 148 | 0.0% | 36% |
| 2026-10-02 | bybit_btc_basis | ok | 1.000 | gross>0bps | 41,820 | 100.0% | 36% | 1,101 | 0.0% | 45% |
| 2026-10-02 | bybit_btc_basis | ok | 1.000 | gross>1bps | 7,415 | 100.0% | 75% | 394 | 0.0% | 68% |
| 2026-10-02 | bybit_btc_basis | ok | 1.000 | gross>2bps | 1,226 | 100.0% | 82% | 204 | 0.0% | 81% |
| 2026-10-02 | bybit_btc_basis | ok | 1.000 | gross>5bps | 53 | 100.0% | 100% | none resolved | 0.0% | 94% |
| 2026-10-02 | bybit_eth_basis | ok | 1.000 | gross>0bps | 46,514 | 100.0% | 30% | 940 | 0.0% | 59% |
| 2026-10-02 | bybit_eth_basis | ok | 1.000 | gross>1bps | 15,658 | 100.0% | 67% | 350 | 0.0% | 77% |
| 2026-10-02 | bybit_eth_basis | ok | 1.000 | gross>2bps | 2,353 | 100.0% | 81% | 190 | 0.0% | 77% |
| 2026-10-02 | bybit_eth_basis | ok | 1.000 | gross>5bps | 82 | 100.0% | 96% | 100 | 0.0% | 87% |
| 2026-10-02 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 55,172 | 100.0% | 22% | 999 | 0.0% | 29% |
| 2026-10-02 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 14,209 | 100.0% | 52% | 200 | 0.0% | 29% |
| 2026-10-02 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 1,931 | 100.0% | 65% | 199 | 0.0% | 35% |
| 2026-10-02 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 158 | 100.0% | 61% | 150 | 0.0% | 23% |
| 2026-10-02 | bybit_eth_btc_ratio | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2026-10-03 | bybit_btc_basis | ok | 1.000 | gross>0bps | 4,373 | 100.0% | 29% | 7,654 | 0.0% | 45% |
| 2026-10-03 | bybit_btc_basis | ok | 1.000 | gross>1bps | 524 | 100.0% | 75% | 1,743 | 0.0% | 71% |
| 2026-10-03 | bybit_btc_basis | ok | 1.000 | gross>2bps | 73 | 100.0% | 100% | none resolved | 0.0% | 90% |
| 2026-10-03 | bybit_btc_basis | ok | 1.000 | gross>5bps | 3 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2026-10-03 | bybit_eth_basis | ok | 1.000 | gross>0bps | 7,417 | 100.0% | 23% | 5,111 | 0.0% | 62% |
| 2026-10-03 | bybit_eth_basis | ok | 1.000 | gross>1bps | 1,334 | 100.0% | 77% | 1,042 | 0.0% | 84% |
| 2026-10-03 | bybit_eth_basis | ok | 1.000 | gross>2bps | 120 | 100.0% | 99% | 522 | 0.0% | 86% |
| 2026-10-03 | bybit_eth_basis | ok | 1.000 | gross>5bps | 8 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2026-10-03 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 9,756 | 100.0% | 8% | 2,449 | 0.0% | 24% |
| 2026-10-03 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 1,454 | 100.0% | 39% | 298 | 0.0% | 11% |
| 2026-10-03 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 172 | 100.0% | 53% | 249 | 0.0% | 17% |
| 2026-10-03 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 7 | 100.0% | 71% | 298 | 0.0% | 14% |
| 2026-10-04 | bybit_btc_basis | ok | 1.000 | gross>0bps | 8,536 | 100.0% | 33% | 3,093 | 0.0% | 42% |
| 2026-10-04 | bybit_btc_basis | ok | 1.000 | gross>1bps | 1,629 | 100.0% | 67% | 1,190 | 0.0% | 53% |
| 2026-10-04 | bybit_btc_basis | ok | 1.000 | gross>2bps | 199 | 100.0% | 93% | 7,664 | 0.0% | 88% |
| 2026-10-04 | bybit_btc_basis | ok | 1.000 | gross>5bps | 11 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2026-10-04 | bybit_eth_basis | ok | 1.000 | gross>0bps | 11,623 | 100.0% | 27% | 2,264 | 0.0% | 60% |
| 2026-10-04 | bybit_eth_basis | ok | 1.000 | gross>1bps | 2,704 | 100.0% | 74% | 650 | 0.0% | 85% |
| 2026-10-04 | bybit_eth_basis | ok | 1.000 | gross>2bps | 300 | 100.0% | 96% | 181 | 0.0% | 87% |
| 2026-10-04 | bybit_eth_basis | ok | 1.000 | gross>5bps | 7 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2026-10-04 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 15,318 | 100.0% | 12% | 1,901 | 0.0% | 28% |
| 2026-10-04 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 2,908 | 100.0% | 44% | 297 | 0.0% | 22% |
| 2026-10-04 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 398 | 100.0% | 54% | 200 | 0.0% | 23% |
| 2026-10-04 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 15 | 100.0% | 33% | 248 | 0.0% | 27% |
| 2026-10-05 | bybit_btc_basis | ok | 1.000 | gross>0bps | 29,102 | 100.0% | 35% | 1,502 | 0.0% | 41% |
| 2026-10-05 | bybit_btc_basis | ok | 1.000 | gross>1bps | 4,553 | 100.0% | 71% | 650 | 0.0% | 57% |
| 2026-10-05 | bybit_btc_basis | ok | 1.000 | gross>2bps | 406 | 100.0% | 89% | 1,949 | 0.0% | 85% |
| 2026-10-05 | bybit_btc_basis | ok | 1.000 | gross>5bps | 22 | 100.0% | 77% | 1,784 | 0.0% | 82% |
| 2026-10-05 | bybit_eth_basis | ok | 1.000 | gross>0bps | 30,751 | 100.0% | 26% | 1,310 | 0.0% | 61% |
| 2026-10-05 | bybit_eth_basis | ok | 1.000 | gross>1bps | 7,509 | 100.0% | 75% | 394 | 0.0% | 84% |
| 2026-10-05 | bybit_eth_basis | ok | 1.000 | gross>2bps | 664 | 100.0% | 95% | 194 | 0.0% | 81% |
| 2026-10-05 | bybit_eth_basis | ok | 1.000 | gross>5bps | 32 | 100.0% | 100% | none resolved | 0.0% | 69% |
| 2026-10-05 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 41,120 | 100.0% | 20% | 1,298 | 0.0% | 33% |
| 2026-10-05 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 6,916 | 100.0% | 55% | 200 | 0.0% | 32% |
| 2026-10-05 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 698 | 100.0% | 62% | 200 | 0.0% | 32% |
| 2026-10-05 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 47 | 100.0% | 60% | 223 | 0.0% | 19% |
| 2026-10-06 | bybit_btc_basis | ok | 1.000 | gross>0bps | 21,083 | 100.0% | 34% | 1,943 | 0.0% | 40% |
| 2026-10-06 | bybit_btc_basis | ok | 1.000 | gross>1bps | 3,290 | 100.0% | 69% | 793 | 0.0% | 54% |
| 2026-10-06 | bybit_btc_basis | ok | 1.000 | gross>2bps | 232 | 100.0% | 99% | 3,643 | 0.0% | 96% |
| 2026-10-06 | bybit_btc_basis | ok | 1.000 | gross>5bps | 3 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2026-10-06 | bybit_eth_basis | ok | 1.000 | gross>0bps | 20,252 | 100.0% | 25% | 1,822 | 0.0% | 62% |
| 2026-10-06 | bybit_eth_basis | ok | 1.000 | gross>1bps | 4,428 | 100.0% | 74% | 411 | 0.0% | 85% |
| 2026-10-06 | bybit_eth_basis | ok | 1.000 | gross>2bps | 384 | 100.0% | 91% | 265 | 0.0% | 82% |
| 2026-10-06 | bybit_eth_basis | ok | 1.000 | gross>5bps | 24 | 100.0% | 96% | 100 | 0.0% | 96% |
| 2026-10-06 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 29,919 | 100.0% | 18% | 1,500 | 0.0% | 34% |
| 2026-10-06 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 4,169 | 100.0% | 54% | 201 | 0.0% | 31% |
| 2026-10-06 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 393 | 100.0% | 61% | 248 | 0.0% | 34% |
| 2026-10-06 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 22 | 100.0% | 68% | 548 | 0.0% | 18% |
| 2026-10-06 | bybit_eth_btc_ratio | ok | 1.000 | retail_taker | 2 | 100.0% | 100% | none resolved | 0.0% | 0% |
| 2026-10-07 | bybit_btc_basis | ok | 1.000 | gross>0bps | 27,447 | 100.0% | 36% | 1,443 | 0.0% | 40% |
| 2026-10-07 | bybit_btc_basis | ok | 1.000 | gross>1bps | 4,969 | 100.0% | 68% | 594 | 0.0% | 54% |
| 2026-10-07 | bybit_btc_basis | ok | 1.000 | gross>2bps | 471 | 100.0% | 91% | 4,453 | 0.0% | 85% |
| 2026-10-07 | bybit_btc_basis | ok | 1.000 | gross>5bps | 26 | 100.0% | 85% | 4,438 | 0.0% | 65% |
| 2026-10-07 | bybit_eth_basis | ok | 1.000 | gross>0bps | 33,874 | 100.0% | 28% | 1,011 | 0.0% | 60% |
| 2026-10-07 | bybit_eth_basis | ok | 1.000 | gross>1bps | 10,895 | 100.0% | 74% | 300 | 0.0% | 82% |
| 2026-10-07 | bybit_eth_basis | ok | 1.000 | gross>2bps | 1,475 | 100.0% | 90% | 145 | 0.0% | 81% |
| 2026-10-07 | bybit_eth_basis | ok | 1.000 | gross>5bps | 162 | 100.0% | 85% | 197 | 0.0% | 80% |
| 2026-10-07 | bybit_eth_basis | ok | 1.000 | retail_taker | 1 | 100.0% | 100% | none resolved | 0.0% | 100% |
| 2026-10-07 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 40,774 | 100.0% | 21% | 1,200 | 0.0% | 34% |
| 2026-10-07 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 10,591 | 100.0% | 51% | 202 | 0.0% | 31% |
| 2026-10-07 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 1,967 | 100.0% | 62% | 199 | 0.0% | 34% |
| 2026-10-07 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 183 | 100.0% | 68% | 249 | 0.0% | 23% |
| 2026-10-07 | bybit_eth_btc_ratio | ok | 1.000 | retail_taker | 16 | 100.0% | 56% | 296 | 0.0% | 12% |
| 2026-10-08 | bybit_btc_basis | ok | 1.000 | gross>0bps | 45,222 | 100.0% | 36% | 956 | 0.0% | 41% |
| 2026-10-08 | bybit_btc_basis | ok | 1.000 | gross>1bps | 8,602 | 100.0% | 71% | 456 | 0.0% | 57% |
| 2026-10-08 | bybit_btc_basis | ok | 1.000 | gross>2bps | 753 | 100.0% | 96% | 196 | 0.0% | 90% |
| 2026-10-08 | bybit_btc_basis | ok | 1.000 | gross>5bps | 34 | 100.0% | 100% | none resolved | 0.0% | 94% |
| 2026-10-08 | bybit_eth_basis | ok | 1.000 | gross>0bps | 58,443 | 100.0% | 33% | 710 | 0.0% | 58% |
| 2026-10-08 | bybit_eth_basis | ok | 1.000 | gross>1bps | 19,939 | 100.0% | 75% | 288 | 0.0% | 80% |
| 2026-10-08 | bybit_eth_basis | ok | 1.000 | gross>2bps | 2,760 | 100.0% | 92% | 122 | 0.0% | 83% |
| 2026-10-08 | bybit_eth_basis | ok | 1.000 | gross>5bps | 177 | 100.0% | 99% | 100 | 0.0% | 94% |
| 2026-10-08 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 63,247 | 100.0% | 25% | 898 | 0.0% | 36% |
| 2026-10-08 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 19,989 | 100.0% | 56% | 200 | 0.0% | 37% |
| 2026-10-08 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 3,555 | 100.0% | 67% | 199 | 0.0% | 43% |
| 2026-10-08 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 266 | 100.0% | 71% | 199 | 0.0% | 32% |
| 2026-10-08 | bybit_eth_btc_ratio | ok | 1.000 | retail_taker | 3 | 100.0% | 33% | 150 | 0.0% | 0% |
| 2026-10-09 | bybit_btc_basis | ok | 1.000 | gross>0bps | 23,097 | 100.0% | 34% | 1,857 | 0.0% | 38% |
| 2026-10-09 | bybit_btc_basis | ok | 1.000 | gross>1bps | 3,306 | 100.0% | 65% | 650 | 0.0% | 49% |
| 2026-10-09 | bybit_btc_basis | ok | 1.000 | gross>2bps | 229 | 100.0% | 90% | 694 | 0.0% | 90% |
| 2026-10-09 | bybit_btc_basis | ok | 1.000 | gross>5bps | 10 | 100.0% | 90% | 2,814 | 0.0% | 90% |
| 2026-10-09 | bybit_eth_basis | ok | 1.000 | gross>0bps | 28,618 | 100.0% | 26% | 1,340 | 0.0% | 63% |
| 2026-10-09 | bybit_eth_basis | ok | 1.000 | gross>1bps | 8,362 | 100.0% | 77% | 412 | 0.0% | 86% |
| 2026-10-09 | bybit_eth_basis | ok | 1.000 | gross>2bps | 572 | 100.0% | 97% | 239 | 0.0% | 83% |
| 2026-10-09 | bybit_eth_basis | ok | 1.000 | gross>5bps | 18 | 100.0% | 100% | none resolved | 0.0% | 83% |
| 2026-10-09 | bybit_eth_btc_ratio | ok | 1.000 | gross>0bps | 39,222 | 100.0% | 22% | 1,250 | 0.0% | 35% |
| 2026-10-09 | bybit_eth_btc_ratio | ok | 1.000 | gross>1bps | 7,294 | 100.0% | 56% | 200 | 0.0% | 31% |
| 2026-10-09 | bybit_eth_btc_ratio | ok | 1.000 | gross>2bps | 698 | 100.0% | 68% | 200 | 0.0% | 33% |
| 2026-10-09 | bybit_eth_btc_ratio | ok | 1.000 | gross>5bps | 40 | 100.0% | 65% | 174 | 0.0% | 18% |
| 2026-10-10 | bybit_btc_basis | holdout: label statistics hidden | | | | | | | | |
| 2026-10-10 | bybit_eth_basis | holdout: label statistics hidden | | | | | | | | |
| 2026-10-10 | bybit_eth_btc_ratio | holdout: label statistics hidden | | | | | | | | |
| 2026-10-11 | bybit_btc_basis | holdout: label statistics hidden | | | | | | | | |
| 2026-10-11 | bybit_eth_basis | holdout: label statistics hidden | | | | | | | | |
| 2026-10-11 | bybit_eth_btc_ratio | holdout: label statistics hidden | | | | | | | | |
| 2026-10-12 | bybit_btc_basis | holdout: label statistics hidden | | | | | | | | |
| 2026-10-12 | bybit_eth_basis | holdout: label statistics hidden | | | | | | | | |
| 2026-10-12 | bybit_eth_btc_ratio | holdout: label statistics hidden | | | | | | | | |
| 2026-10-13 | bybit_btc_basis | holdout: label statistics hidden | | | | | | | | |
| 2026-10-13 | bybit_eth_basis | holdout: label statistics hidden | | | | | | | | |
| 2026-10-13 | bybit_eth_btc_ratio | holdout: label statistics hidden | | | | | | | | |
| 2026-10-14 | bybit_btc_basis | holdout: label statistics hidden | | | | | | | | |
| 2026-10-14 | bybit_eth_basis | holdout: label statistics hidden | | | | | | | | |
| 2026-10-14 | bybit_eth_btc_ratio | holdout: label statistics hidden | | | | | | | | |
| 2026-10-15 | bybit_btc_basis | holdout: label statistics hidden | | | | | | | | |
| 2026-10-15 | bybit_eth_basis | holdout: label statistics hidden | | | | | | | | |
| 2026-10-15 | bybit_eth_btc_ratio | holdout: label statistics hidden | | | | | | | | |
| 2026-10-16 | bybit_btc_basis | holdout: label statistics hidden | | | | | | | | |
| 2026-10-16 | bybit_eth_basis | holdout: label statistics hidden | | | | | | | | |
| 2026-10-16 | bybit_eth_btc_ratio | holdout: label statistics hidden | | | | | | | | |
| 2026-10-17 | bybit_btc_basis | holdout: label statistics hidden | | | | | | | | |
| 2026-10-17 | bybit_eth_basis | holdout: label statistics hidden | | | | | | | | |
| 2026-10-17 | bybit_eth_btc_ratio | holdout: label statistics hidden | | | | | | | | |
| 2026-10-18 | bybit_btc_basis | holdout: label statistics hidden | | | | | | | | |
| 2026-10-18 | bybit_eth_basis | holdout: label statistics hidden | | | | | | | | |
| 2026-10-18 | bybit_eth_btc_ratio | holdout: label statistics hidden | | | | | | | | |

## Splits

Holdout window 2026-10-10 to 2026-10-18, frozen 2026-10-19T13:19:24+00:00 (fingerprint f16868b266a6c9e2). Embargo from 2026-10-09.

| Split | Dates | Range | Daily RV of BTC perp, min / median / max (bps) |
|---|---|---|---|
| development | 289 | 2023-05-18 to 2026-10-08 | 25 / 184 / 935 |
| embargo | 1 | 2026-10-09 to 2026-10-09 | 159 / 159 / 159 |
| holdout | 9 | 2026-10-10 to 2026-10-18 | 65 / 168 / 274 |

4 walk-forward folds inside development.
