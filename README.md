# BTC paper bot

**Fake money test.** Real Bitcoin prices from Binance, no real money used.

| | |
|---|---|
| Started with | $50.00 |
| Worth now | **$37.35** |
| Saved (profit set aside, never traded) | **$1.36** |
| Total profit (if sold now) | **-$12.65** (-25.30%) |
| Profit today (from sells, UTC) | **+$0.00** |
| Average per day | -$0.26 |
| Wins / safety exits | 47 / 9 |
| Right now | holding BTC (bought for $35.63) |
| BTC price | $63,954.01 |
| Updated | 2026-11-15 00:06 UTC (every hour + every trade) |

## Profit per day (from sells, UTC)

| Day | Profit |
|---|---|
| 2026-11-14 | -$3.90 |
| 2026-11-13 | -$1.97 |
| 2026-11-11 | +$0.32 |
| 2026-11-10 | -$1.68 |
| 2026-11-05 | -$1.67 |
| 2026-11-04 | +$0.54 |
| 2026-11-02 | +$0.20 |
| 2026-11-01 | +$0.11 |
| 2026-10-30 | +$0.23 |
| 2026-10-29 | -$2.11 |
| 2026-10-22 | -$1.91 |
| 2026-10-21 | +$0.56 |
| 2026-10-20 | +$0.11 |
| 2026-10-16 | +$0.10 |
| 2026-10-15 | -$1.52 |
| 2026-10-13 | +$0.32 |
| 2026-10-12 | +$0.10 |
| 2026-10-11 | +$0.26 |
| 2026-10-07 | -$2.03 |
| 2026-10-02 | +$0.55 |
| 2026-09-30 | +$0.60 |
| 2026-09-29 | +$0.21 |

## Last 10 trades (newest first)

```
2026-11-15 00:06 UTC  BUY  0.00054945 BTC @ 63,954.01 for $35.17
2026-11-14 23:50 UTC  SELL @ 64,182.01  profit $+0.12  saved $1.36
2026-11-14 23:20 UTC  BUY  0.00054945 BTC @ 63,845.74 for $35.12
2026-11-14 23:20 UTC  SELL @ 63,836.64  profit $+0.10  saved $1.36
2026-11-14 23:08 UTC  BUY  0.00054945 BTC @ 63,462.24 for $34.90
2026-11-14 22:08 UTC  SAFETY EXIT @ 63,860.25  loss $-2.04  now trading $35.28
2026-11-14 03:28 UTC  BUY  0.00054945 BTC @ 67,379.21 for $37.06
2026-11-14 02:28 UTC  SAFETY EXIT @ 67,436.31  loss $-2.08  now trading $37.25
2026-11-13 01:40 UTC  BUY  0.00054945 BTC @ 71,014.01 for $39.06
2026-11-13 00:36 UTC  SAFETY EXIT @ 71,072.23  loss $-1.97  now trading $39.26
```

## How it works

- Trades $50 each time; profit above that is set aside, never traded
- Buys when BTC drops 0.3% below its 1-hour high
- Sells when up $0.10 after fees (0.1% per trade)
- Safety exit if down $2.00, then waits 60 min before buying again
