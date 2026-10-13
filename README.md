# BTC paper bot

**Fake money test.** Real Bitcoin prices from Binance, no real money used.

| | |
|---|---|
| Started with | $50.00 |
| Worth now | **$49.79** |
| Saved (profit set aside, never traded) | **$1.36** |
| Total profit (if sold now) | **-$0.21** (-0.43%) |
| Profit today (from sells, UTC) | **+$0.32** |
| Average per day | +$0.00 |
| Wins / safety exits | 15 / 1 |
| Right now | holding BTC (bought for $48.46) |
| BTC price | $83,427.12 |
| Updated | 2026-10-13 22:09 UTC (every hour + every trade) |

## Profit per day (from sells, UTC)

| Day | Profit |
|---|---|
| 2026-10-13 | +$0.32 |
| 2026-10-12 | +$0.10 |
| 2026-10-11 | +$0.26 |
| 2026-10-07 | -$2.03 |
| 2026-10-02 | +$0.55 |
| 2026-09-30 | +$0.60 |
| 2026-09-29 | +$0.21 |

## Last 10 trades (newest first)

```
2026-10-13 05:32 UTC  BUY  0.00056943 BTC @ 83,649.78 for $47.68
2026-10-13 05:14 UTC  SELL @ 83,698.71  profit $+0.13  saved $1.36
2026-10-13 03:37 UTC  BUY  0.00056943 BTC @ 83,319.83 for $47.49
2026-10-13 03:32 UTC  SELL @ 83,333.32  profit $+0.19  saved $1.36
2026-10-12 14:17 UTC  BUY  0.00057942 BTC @ 82,838.01 for $48.05
2026-10-12 04:43 UTC  SELL @ 84,122.04  profit $+0.10  saved $1.36
2026-10-12 01:28 UTC  BUY  0.00056943 BTC @ 83,772.57 for $47.75
2026-10-11 17:36 UTC  SELL @ 84,173.02  profit $+0.15  saved $1.36
2026-10-11 16:02 UTC  BUY  0.00056943 BTC @ 83,734.73 for $47.73
2026-10-11 15:57 UTC  SELL @ 83,729.02  profit $+0.11  saved $1.36
```

## How it works

- Trades $50 each time; profit above that is set aside, never traded
- Buys when BTC drops 0.3% below its 1-hour high
- Sells when up $0.10 after fees (0.1% per trade)
- Safety exit if down $2.00, then waits 60 min before buying again
