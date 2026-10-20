# Maker-taker prototype, January 2024 (Bybit maker, Binance taker hedge), with inventory

31 days. Margin chosen on the first 20 days by capped realised P&L; everything below is the last 11 days.
Bybit latency 8 ms; one order per quoting spell; queue cancellations ignored (pessimistic).
Old accounting: each fill credited with the whole gap. Realised: positions tracked, funding paid or received, the remainder closed with taker orders at the day's end. Capped: no fill that would take the position past $50,000.

| Fees (bps) | Binance latency | Quoting rule | Margin | Fills per day | Fills going one way | Old accounting | Realised, no cap | Realised, capped | 95% interval (capped) | Marked, capped |
|---|---|---|---|---|---|---|---|---|---|---|
| top tier (maker 0, taker 1.7) | co-located (5 ms) | vs zero | 5 | 7 | 88% | $45 | $35 | $33 | [10, 62] | $41 |
| top tier (maker 0, taker 1.7) | co-located (5 ms) | vs trailing offset | 3 | 13 | 74% | $52 | $42 | $38 | [16, 64] | $44 |
| top tier (maker 0, taker 1.7) | from here (50 ms) | vs zero | 5 | 7 | 88% | $30 | $20 | $20 | [5, 36] | $28 |
| top tier (maker 0, taker 1.7) | from here (50 ms) | vs trailing offset | 5 | 5 | 81% | $24 | $19 | $19 | [7, 33] | $25 |
| mid tier (1, 3) | co-located (5 ms) | vs zero | 5 | 3 | 95% | $22 | $12 | $11 | [-0, 30] | $22 |
| mid tier (1, 3) | co-located (5 ms) | vs trailing offset | 5 | 3 | 92% | $21 | $13 | $13 | [1, 29] | $22 |
| mid tier (1, 3) | from here (50 ms) | vs zero | 5 | 3 | 95% | $16 | $5 | $5 | [-1, 15] | $16 |
| mid tier (1, 3) | from here (50 ms) | vs trailing offset | 5 | 3 | 92% | $15 | $7 | $7 | [1, 15] | $16 |
| base tier (2, 5) | co-located (5 ms) | vs zero | 5 | 2 | 92% | $16 | $8 | $8 | [-1, 21] | $16 |
| base tier (2, 5) | co-located (5 ms) | vs trailing offset | 3 | 2 | 94% | $15 | $3 | $3 | [-8, 15] | $16 |
| base tier (2, 5) | from here (50 ms) | vs zero | 5 | 2 | 92% | $11 | $4 | $4 | [-2, 11] | $12 |
| base tier (2, 5) | from here (50 ms) | vs trailing offset | 5 | 2 | 90% | $11 | $3 | $3 | [-4, 11] | $12 |

Per-day components (trade P&L, funding, closing cost, peak position) for every configuration: `by_day.csv`.
