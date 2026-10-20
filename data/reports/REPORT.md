# Dataset report

## Stream quality

Trade check: Bybit's independent trade record against the reconstructed book. In band = share of trades printing between the bracketing snapshots' quotes; sweeps beyond the band are normal on volatile days. A day fails on persistence (5+ consecutive minutes where most trades miss the book) or a clock offset over 20 ms.

| Date | Stream | Rows | Coverage | Longest raw silence (s) | Resyncs | Feed lag p50/p99 (ms) | Spread p50 (bps) | Daily RV (bps) | Trades in band | Longest anomaly (min) | Clock offset (ms) | Passes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
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

## Development data, pooled

Holdout days are excluded. Stale births are dropped. Lifetimes are shown only for episodes longer than the pair's sampling step; shorter ones are known only to within it.

Fresh partner = every sampled leg's quote was less than half a step old at the birth: the cleanest labels.

| Pair | Hurdle | Days | Episodes per day | Shorter than resolution | Resolved life median / p90 (ms) | Fresh-partner births per day | Fresh: shorter than resolution | Fresh: resolved life median (ms) |
|---|---|---|---|---|---|---|---|---|
| btc_perp_binance_bybit | gross>0bps | 31 | 14,575 | 36% | 945 / 13,479 | 10,293.0 | 33% | 1,178 |
| btc_perp_binance_bybit | gross>1bps | 31 | 13,813 | 38% | 797 / 9,499 | 9,694.5 | 35% | 976 |
| btc_perp_binance_bybit | gross>2bps | 31 | 10,854 | 42% | 637 / 7,703 | 7,432.5 | 39% | 799 |
| btc_perp_binance_bybit | gross>5bps | 31 | 2,371 | 56% | 528 / 6,699 | 1,460.8 | 51% | 753 |
| btc_perp_binance_bybit | retail_taker | 30 | 118 | 84% | 171 / 617 | 64.2 | 81% | 188 |
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

## Episodes by day

| Date | Pair | Status | Valid share | Hurdle | Episodes | Observed deaths | Shorter than resolution | Median life, resolved only (ms) | Stale births | Stale partner |
|---|---|---|---|---|---|---|---|---|---|---|
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
| development | 63 | 2024-01-01 to 2026-10-08 | 63 / 215 / 664 |
| embargo | 1 | 2026-10-09 to 2026-10-09 | 159 / 159 / 159 |
| holdout | 9 | 2026-10-10 to 2026-10-18 | 65 / 168 / 274 |

4 walk-forward folds inside development.
