# BTC paper bot

**Fake money test.** Real Bitcoin prices from Binance, no real money used.

| | |
|---|---|
| Started with | $50.00 |
| Worth now | **$42.95** |
| Saved (profit set aside, never traded) | **$1.36** |
| Total profit (if sold now) | **-$7.05** (-14.10%) |
| Profit today (from sells, UTC) | **+$0.00** |
| Average per day | -$0.16 |
| Wins / safety exits | 42 / 6 |
| Right now | holding BTC (bought for $41.41) |
| BTC price | $73,865.54 |
| Updated | 2026-11-11 06:33 UTC (every hour + every trade) |

## Profit per day (from sells, UTC)

| Day | Profit |
|---|---|
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
2026-11-10 22:43 UTC  BUY  0.00055944 BTC @ 73,750.01 for $41.30
2026-11-10 22:42 UTC  SELL @ 73,772.01  profit $+0.11  saved $1.36
2026-11-10 18:48 UTC  BUY  0.00055944 BTC @ 73,427.54 for $41.12
2026-11-10 18:33 UTC  SELL @ 73,518.00  profit $+0.10  saved $1.36
2026-11-10 18:13 UTC  BUY  0.00055944 BTC @ 73,192.00 for $40.99
2026-11-10 17:54 UTC  SELL @ 73,208.35  profit $+0.13  saved $1.36
2026-11-10 16:37 UTC  BUY  0.00055944 BTC @ 72,814.24 for $40.78
2026-11-10 15:37 UTC  SAFETY EXIT @ 73,294.90  loss $-2.02  now trading $41.02
2026-11-05 16:26 UTC  BUY  0.00055944 BTC @ 76,750.00 for $42.98
2026-11-05 16:24 UTC  SELL @ 76,971.80  profit $+0.13  saved $1.36
```

## How it works

- Trades $50 each time; profit above that is set aside, never traded
- Buys when BTC drops 0.3% below its 1-hour high
- Sells when up $0.10 after fees (0.1% per trade)
- Safety exit if down $2.00, then waits 60 min before buying again
