# BTC paper bot

**Fake money test.** Real Bitcoin prices from Binance, no real money used.

| | |
|---|---|
| Started with | $50.00 |
| Worth now | **$41.57** |
| Saved (profit set aside, never traded) | **$1.36** |
| Total profit (if sold now) | **-$8.43** (-16.85%) |
| Profit today (from sells, UTC) | **+$0.00** |
| Average per day | -$0.15 |
| Wins / safety exits | 45 / 6 |
| Right now | holding BTC (bought for $41.72) |
| BTC price | $71,595.03 |
| Updated | 2026-11-12 19:27 UTC (every hour + every trade) |

## Profit per day (from sells, UTC)

| Day | Profit |
|---|---|
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
2026-11-11 17:21 UTC  BUY  0.00054945 BTC @ 74,522.59 for $40.99
2026-11-11 17:17 UTC  SELL @ 74,532.01  profit $+0.10  saved $1.36
2026-11-11 15:36 UTC  BUY  0.00055944 BTC @ 74,201.54 for $41.55
2026-11-11 15:35 UTC  SELL @ 74,293.24  profit $+0.11  saved $1.36
2026-11-11 08:23 UTC  BUY  0.00055944 BTC @ 73,948.01 for $41.41
2026-11-11 07:57 UTC  SELL @ 74,096.02  profit $+0.11  saved $1.36
2026-11-10 22:43 UTC  BUY  0.00055944 BTC @ 73,750.01 for $41.30
2026-11-10 22:42 UTC  SELL @ 73,772.01  profit $+0.11  saved $1.36
2026-11-10 18:48 UTC  BUY  0.00055944 BTC @ 73,427.54 for $41.12
2026-11-10 18:33 UTC  SELL @ 73,518.00  profit $+0.10  saved $1.36
```

## How it works

- Trades $50 each time; profit above that is set aside, never traded
- Buys when BTC drops 0.3% below its 1-hour high
- Sells when up $0.10 after fees (0.1% per trade)
- Safety exit if down $2.00, then waits 60 min before buying again
