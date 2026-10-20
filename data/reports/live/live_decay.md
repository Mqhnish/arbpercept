# Decay models on our 10 ms recordings (preliminary)

Hour-based split: train on the first hours, one-hour embargo, test on the last hours. AUC of P(still open after tau) on the test hours.

| Pair | Births above 1 bps | Hours (train / test) | tau (ms) | Open after tau (test) | Boosted AUC | Logistic AUC | Gap size alone |
|---|---|---|---|---|---|---|---|
| live_btc_basis | 1,234 | 5 / 3 | 50 | 46% | 0.66 | 0.58 | 0.55 |
| live_btc_basis | 1,234 | 5 / 3 | 100 | 36% | 0.66 | 0.56 | 0.53 |
| live_btc_basis | 1,234 | 5 / 3 | 250 | 28% | 0.64 | 0.55 | 0.53 |
| live_btc_basis | 1,234 | 5 / 3 | 500 | 20% | 0.65 | 0.57 | 0.55 |
| live_eth_basis | 3,005 | 5 / 3 | 50 | 45% | 0.71 | 0.62 | 0.49 |
| live_eth_basis | 3,005 | 5 / 3 | 100 | 35% | 0.70 | 0.61 | 0.48 |
| live_eth_basis | 3,005 | 5 / 3 | 250 | 23% | 0.69 | 0.61 | 0.47 |
| live_eth_basis | 3,005 | 5 / 3 | 500 | 15% | 0.70 | 0.60 | 0.49 |
| live_btc_perp_binance_bybit | 1,686 | 4 / 2 | 50 | 61% | 0.74 | 0.64 | 0.55 |
| live_btc_perp_binance_bybit | 1,686 | 4 / 2 | 100 | 51% | 0.69 | 0.61 | 0.55 |
| live_btc_perp_binance_bybit | 1,686 | 4 / 2 | 250 | 40% | 0.67 | 0.61 | 0.54 |
| live_btc_perp_binance_bybit | 1,686 | 4 / 2 | 500 | 31% | 0.65 | 0.60 | 0.55 |
| live_eth_perp_binance_bybit | 3,045 | 4 / 2 | 50 | 56% | 0.74 | 0.52 | 0.65 |
| live_eth_perp_binance_bybit | 3,045 | 4 / 2 | 100 | 48% | 0.70 | 0.54 | 0.61 |
| live_eth_perp_binance_bybit | 3,045 | 4 / 2 | 250 | 38% | 0.70 | 0.61 | 0.59 |
| live_eth_perp_binance_bybit | 3,045 | 4 / 2 | 500 | 29% | 0.70 | 0.53 | 0.41 |
