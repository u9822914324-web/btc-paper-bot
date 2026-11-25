# BTC paper bot

**Fake money test.** Real Bitcoin prices from Binance, no real money used.

| | |
|---|---|
| Started with | $50.00 |
| Worth now | **$33.40** |
| Saved (profit set aside, never traded) | **$1.36** |
| Total profit (if sold now) | **-$16.60** (-33.20%) |
| Profit today (from sells, UTC) | **-$1.75** |
| Average per day | -$0.28 |
| Wins / safety exits | 63 / 13 |
| Right now | holding BTC (bought for $31.62) |
| BTC price | $60,076.01 |
| Updated | 2026-11-25 19:19 UTC (every hour + every trade) |

## Profit per day (from sells, UTC)

| Day | Profit |
|---|---|
| 2026-11-25 | -$1.75 |
| 2026-11-23 | +$0.36 |
| 2026-11-22 | +$0.16 |
| 2026-11-21 | +$0.32 |
| 2026-11-20 | -$2.00 |
| 2026-11-19 | +$0.33 |
| 2026-11-18 | -$1.99 |
| 2026-11-15 | +$0.60 |
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
2026-11-25 19:19 UTC  BUY  0.00051948 BTC @ 60,076.01 for $31.24
2026-11-25 19:16 UTC  SELL @ 60,142.30  profit $+0.13  saved $1.36
2026-11-25 17:43 UTC  BUY  0.00051948 BTC @ 59,770.03 for $31.08
2026-11-25 17:42 UTC  SELL @ 59,862.78  profit $+0.10  saved $1.36
2026-11-25 17:37 UTC  BUY  0.00051948 BTC @ 59,513.46 for $30.95
2026-11-25 16:37 UTC  SAFETY EXIT @ 58,502.81  loss $-1.98  now trading $31.41
2026-11-23 17:02 UTC  BUY  0.00052947 BTC @ 62,126.80 for $32.93
2026-11-23 17:02 UTC  SELL @ 62,147.78  profit $+0.16  saved $1.36
2026-11-23 03:21 UTC  BUY  0.00052947 BTC @ 61,737.74 for $32.72
2026-11-23 03:21 UTC  SELL @ 61,596.02  profit $+0.10  saved $1.36
```

## How it works

- Trades $50 each time; profit above that is set aside, never traded
- Buys when BTC drops 0.3% below its 1-hour high
- Sells when up $0.10 after fees (0.1% per trade)
- Safety exit if down $2.00, then waits 60 min before buying again
