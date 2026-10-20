# Maker-taker prototype, January 2024 (Bybit maker, Binance taker hedge), with inventory

31 days. Margin chosen on the first 20 days by capped realised P&L; everything below is the last 11 days.
Bybit latency 8 ms; one order per quoting spell; queue cancellations ignored (pessimistic); each partial fill hedged on its own.
Old accounting: each fill credited with the whole gap. Realised: positions tracked, funding paid or received, no new fills in the day's last 60 s while the position is closed with taker orders, never taking more than both books show. Capped: no fill that would take the position past $50,000 at the price of that fill.

| Fees (bps) | Binance latency | Quoting rule | Margin | Fills per day | Fills going one way | Old accounting | Realised, no cap | Realised, capped | 95% interval (capped) | Marked, capped |
|---|---|---|---|---|---|---|---|---|---|---|
| top tier (maker 0, taker 1.7) | co-located (5 ms) | vs zero | 5 | 7 | 88% | $45 | $34 | $32 | [10, 61] | $41 |
| top tier (maker 0, taker 1.7) | co-located (5 ms) | vs trailing offset | 3 | 13 | 74% | $51 | $42 | $37 | [16, 63] | $44 |
| top tier (maker 0, taker 1.7) | from here (50 ms) | vs zero | 5 | 7 | 88% | $30 | $20 | $19 | [5, 36] | $28 |
| top tier (maker 0, taker 1.7) | from here (50 ms) | vs trailing offset | 5 | 5 | 81% | $24 | $18 | $17 | [6, 31] | $24 |
| mid tier (1, 3) | co-located (5 ms) | vs zero | 3 | 6 | 89% | $29 | $8 | $10 | [-5, 27] | $27 |
| mid tier (1, 3) | co-located (5 ms) | vs trailing offset | 5 | 3 | 92% | $21 | $12 | $12 | [0, 28] | $22 |
| mid tier (1, 3) | from here (50 ms) | vs zero | 5 | 3 | 95% | $16 | $3 | $4 | [-3, 13] | $16 |
| mid tier (1, 3) | from here (50 ms) | vs trailing offset | 5 | 3 | 92% | $15 | $6 | $6 | [0, 14] | $16 |
| base tier (2, 5) | co-located (5 ms) | vs zero | 5 | 2 | 92% | $16 | $7 | $7 | [-1, 19] | $16 |
| base tier (2, 5) | co-located (5 ms) | vs trailing offset | 3 | 2 | 94% | $15 | $2 | $2 | [-9, 14] | $16 |
| base tier (2, 5) | from here (50 ms) | vs zero | 5 | 2 | 92% | $11 | $3 | $3 | [-3, 10] | $12 |
| base tier (2, 5) | from here (50 ms) | vs trailing offset | 5 | 2 | 90% | $11 | $2 | $2 | [-5, 10] | $12 |

Per-day components (trade P&L, funding, closing cost, peak position) for every configuration: `by_day.csv`.
