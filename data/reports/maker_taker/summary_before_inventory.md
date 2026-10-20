# Maker-taker prototype, January 2024 (Bybit maker, Binance taker hedge)

31 days. Margin chosen on the first 20 days; P&L reported on the last 11.
Bybit latency 8 ms; one order per quoting spell; queue cancellations ignored (pessimistic).

| Fees (bps) | Binance latency | Chosen margin | Fills per day | Mean P&L per fill (bps) | Adverse selection per fill (bps) | Net P&L per day, reporting days | 95% interval |
|---|---|---|---|---|---|---|---|
| base tier (2, 5) | co-located (5 ms) | 2 | 3 | +4.47 | -1.15 | $13 | [4, 25] |
| base tier (2, 5) | from here (50 ms) | 2 | 3 | +2.22 | -3.40 | $7 | [2, 11] |
| mid tier (1, 3) | co-located (5 ms) | 2 | 11 | +3.15 | -0.97 | $33 | [16, 54] |
| mid tier (1, 3) | from here (50 ms) | 2 | 11 | +1.50 | -2.61 | $16 | [7, 25] |
| top tier (maker 0, taker 1.7) | co-located (5 ms) | 2 | 134 | +2.01 | -0.70 | $260 | [110, 443] |
| top tier (maker 0, taker 1.7) | from here (50 ms) | 2 | 134 | +1.57 | -1.13 | $202 | [84, 357] |

Adverse selection = how far Binance's hedge price moved against us between the quote decision and the hedge (negative hurts).
Full grid: `by_day.csv`.
