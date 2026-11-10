# BTC paper bot

**Fake money test.** Real Bitcoin prices from Binance, no real money used.

| | |
|---|---|
| Started with | $50.00 |
| Worth now | **$43.50** |
| Saved (profit set aside, never traded) | **$1.36** |
| Total profit (if sold now) | **-$6.50** (-13.01%) |
| Profit today (from sells, UTC) | **+$0.00** |
| Average per day | -$0.12 |
| Wins / safety exits | 39 / 5 |
| Right now | holding BTC (bought for $43.27) |
| BTC price | $74,853.03 |
| Updated | 2026-11-10 05:03 UTC (every hour + every trade) |

## Profit per day (from sells, UTC)

| Day | Profit |
|---|---|
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
2026-11-05 16:26 UTC  BUY  0.00055944 BTC @ 76,750.00 for $42.98
2026-11-05 16:24 UTC  SELL @ 76,971.80  profit $+0.13  saved $1.36
2026-11-05 16:19 UTC  BUY  0.00054945 BTC @ 76,583.01 for $42.12
2026-11-05 16:19 UTC  SELL @ 76,610.00  profit $+0.12  saved $1.36
2026-11-05 16:13 UTC  BUY  0.00054945 BTC @ 76,244.39 for $41.93
2026-11-05 16:13 UTC  SELL @ 76,233.09  profit $+0.12  saved $1.36
2026-11-05 16:10 UTC  BUY  0.00055944 BTC @ 75,826.01 for $42.46
2026-11-05 15:09 UTC  SAFETY EXIT @ 77,229.89  loss $-2.04  now trading $42.48
2026-11-04 15:14 UTC  BUY  0.00054945 BTC @ 80,795.29 for $44.44
2026-11-04 15:08 UTC  SELL @ 80,578.51  profit $+0.13  saved $1.36
```

## How it works

- Trades $50 each time; profit above that is set aside, never traded
- Buys when BTC drops 0.3% below its 1-hour high
- Sells when up $0.10 after fees (0.1% per trade)
- Safety exit if down $2.00, then waits 60 min before buying again
