# Decay models: all births vs clean births, and isotonic calibration

Walk-forward folds on the development days, births above 1 bps gross. AUC of P(gap still open after tau).
Clean = both legs' quotes fresh at birth (no stale partner), the labels the 100 ms archive can be trusted on.
Calibrated = boosted model fitted on the first 70% of each fold's training days, isotonic map on the last 30%.

| Pair | Births | tau (ms) | Validation births | Boosted AUC | Boosted + isotonic AUC | Logistic AUC | Gap size alone | ECE boosted | ECE boosted + isotonic | ECE logistic |
|---|---|---|---|---|---|---|---|---|---|---|
| btc_perp_binance_bybit | all | 500 | 354,202 | 0.847 | 0.840 | 0.783 | 0.574 | 0.028 | 0.033 | 0.051 |
| btc_perp_binance_bybit | all | 1000 | 364,128 | 0.847 | 0.840 | 0.791 | 0.568 | 0.029 | 0.027 | 0.044 |
| btc_perp_binance_bybit | clean | 500 | 247,582 | 0.832 | 0.825 | 0.778 | 0.578 | 0.030 | 0.036 | 0.049 |
| btc_perp_binance_bybit | clean | 1000 | 255,131 | 0.833 | 0.826 | 0.787 | 0.573 | 0.030 | 0.027 | 0.044 |
| bybit_btc_basis | all | 500 | 126,433 | 0.908 | 0.903 | 0.882 | 0.602 | 0.019 | 0.015 | 0.018 |
| bybit_btc_basis | all | 1000 | 128,860 | 0.905 | 0.900 | 0.887 | 0.597 | 0.015 | 0.013 | 0.015 |
| bybit_btc_basis | clean | 500 | 52,069 | 0.780 | 0.774 | 0.746 | 0.488 | 0.032 | 0.030 | 0.034 |
| bybit_btc_basis | clean | 1000 | 54,145 | 0.791 | 0.785 | 0.771 | 0.488 | 0.031 | 0.026 | 0.029 |
| bybit_eth_basis | all | 500 | 305,900 | 0.850 | 0.845 | 0.749 | 0.562 | 0.015 | 0.008 | 0.009 |
| bybit_eth_basis | all | 1000 | 312,320 | 0.857 | 0.849 | 0.776 | 0.566 | 0.008 | 0.006 | 0.006 |
| bybit_eth_basis | clean | 500 | 76,728 | 0.842 | 0.828 | 0.790 | 0.567 | 0.016 | 0.010 | 0.020 |
| bybit_eth_basis | clean | 1000 | 78,966 | 0.852 | 0.839 | 0.814 | 0.577 | 0.011 | 0.007 | 0.014 |
| bybit_eth_btc_ratio | all | 500 | 289,751 | 0.919 | 0.917 | 0.871 | 0.838 | 0.007 | 0.007 | 0.018 |
| bybit_eth_btc_ratio | all | 1000 | 305,457 | 0.927 | 0.920 | 0.890 | 0.881 | 0.002 | 0.002 | 0.004 |
| bybit_eth_btc_ratio | clean | 500 | 195,204 | 0.909 | 0.906 | 0.858 | 0.866 | 0.010 | 0.009 | 0.019 |
| bybit_eth_btc_ratio | clean | 1000 | 209,861 | 0.920 | 0.912 | 0.888 | 0.897 | 0.002 | 0.003 | 0.005 |

Full grid (both hurdles, Brier skill, fold spread): `summary_v2.csv`, `fold_results_v2.csv`.
