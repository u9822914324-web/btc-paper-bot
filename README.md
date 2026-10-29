# BTC paper bot

**Fake money test.** Real Bitcoin prices from Binance, no real money used.

| | |
|---|---|
| Started with | $50.00 |
| Worth now | **$46.37** |
| Saved (profit set aside, never traded) | **$1.36** |
| Total profit (if sold now) | **-$3.63** (-7.26%) |
| Profit today (from sells, UTC) | **+$0.00** |
| Average per day | -$0.08 |
| Wins / safety exits | 27 / 3 |
| Right now | holding BTC (bought for $45.90) |
| BTC price | $80,140.00 |
| Updated | 2026-10-29 13:05 UTC (every hour + every trade) |

## Profit per day (from sells, UTC)

| Day | Profit |
|---|---|
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
2026-10-23 04:28 UTC  BUY  0.00055944 BTC @ 81,738.95 for $45.77
2026-10-22 21:23 UTC  SELL @ 81,561.28  profit $+0.10  saved $1.36
2026-10-22 17:58 UTC  BUY  0.00055944 BTC @ 81,200.01 for $45.47
2026-10-22 16:47 UTC  SAFETY EXIT @ 81,220.01  loss $-2.01  now trading $45.71
2026-10-21 16:44 UTC  BUY  0.00055944 BTC @ 84,638.76 for $47.40
2026-10-21 16:39 UTC  SELL @ 84,882.88  profit $+0.11  saved $1.36
2026-10-21 15:18 UTC  BUY  0.00055944 BTC @ 84,515.39 for $47.33
2026-10-21 15:10 UTC  SELL @ 84,808.10  profit $+0.10  saved $1.36
2026-10-21 15:03 UTC  BUY  0.00055944 BTC @ 84,462.43 for $47.30
2026-10-21 14:43 UTC  SELL @ 84,260.00  profit $+0.11  saved $1.36
```

## How it works

- Trades $50 each time; profit above that is set aside, never traded
- Buys when BTC drops 0.3% below its 1-hour high
- Sells when up $0.10 after fees (0.1% per trade)
- Safety exit if down $2.00, then waits 60 min before buying again
