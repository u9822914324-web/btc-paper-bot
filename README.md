# BTC paper bot

**Fake money test.** Real Bitcoin prices from Binance, no real money used.

| | |
|---|---|
| Started with | $50.00 |
| Worth now | **$49.61** |
| Saved (profit set aside, never traded) | **$1.36** |
| Total profit (if sold now) | **-$0.39** (-0.79%) |
| Profit today (from sells, UTC) | **+$0.00** |
| Average per day | -$0.02 |
| Wins / safety exits | 13 / 1 |
| Right now | holding BTC (bought for $48.09) |
| BTC price | $82,848.66 |
| Updated | 2026-10-13 03:01 UTC (every hour + every trade) |

## Profit per day (from sells, UTC)

| Day | Profit |
|---|---|
| 2026-10-12 | +$0.10 |
| 2026-10-11 | +$0.26 |
| 2026-10-07 | -$2.03 |
| 2026-10-02 | +$0.55 |
| 2026-09-30 | +$0.60 |
| 2026-09-29 | +$0.21 |

## Last 10 trades (newest first)

```
2026-10-12 14:17 UTC  BUY  0.00057942 BTC @ 82,838.01 for $48.05
2026-10-12 04:43 UTC  SELL @ 84,122.04  profit $+0.10  saved $1.36
2026-10-12 01:28 UTC  BUY  0.00056943 BTC @ 83,772.57 for $47.75
2026-10-11 17:36 UTC  SELL @ 84,173.02  profit $+0.15  saved $1.36
2026-10-11 16:02 UTC  BUY  0.00056943 BTC @ 83,734.73 for $47.73
2026-10-11 15:57 UTC  SELL @ 83,729.02  profit $+0.11  saved $1.36
2026-10-07 13:27 UTC  BUY  0.00056943 BTC @ 83,358.00 for $47.51
2026-10-07 12:27 UTC  SAFETY EXIT @ 83,472.01  loss $-2.03  now trading $47.77
2026-10-02 13:42 UTC  BUY  0.00056943 BTC @ 86,868.85 for $49.52
2026-10-02 13:37 UTC  SELL @ 87,111.06  profit $+0.10  saved $1.36
```

## How it works

- Trades $50 each time; profit above that is set aside, never traded
- Buys when BTC drops 0.3% below its 1-hour high
- Sells when up $0.10 after fees (0.1% per trade)
- Safety exit if down $2.00, then waits 60 min before buying again
