# BTC paper bot

**Fake money test.** Real Bitcoin prices from Binance, no real money used.

| | |
|---|---|
| Started with | $50.00 |
| Worth now | **$48.15** |
| Saved (profit set aside, never traded) | **$1.36** |
| Total profit (if sold now) | **-$1.85** (-3.70%) |
| Profit today (from sells, UTC) | **-$1.76** |
| Average per day | -$0.10 |
| Wins / safety exits | 17 / 2 |
| Right now | holding BTC (bought for $46.43) |
| BTC price | $81,783.76 |
| Updated | 2026-10-15 15:01 UTC (every hour + every trade) |

## Profit per day (from sells, UTC)

| Day | Profit |
|---|---|
| 2026-10-15 | -$1.76 |
| 2026-10-13 | +$0.32 |
| 2026-10-12 | +$0.10 |
| 2026-10-11 | +$0.26 |
| 2026-10-07 | -$2.03 |
| 2026-10-02 | +$0.55 |
| 2026-09-30 | +$0.60 |
| 2026-09-29 | +$0.21 |

## Last 10 trades (newest first)

```
2026-10-15 15:01 UTC  BUY  0.00055944 BTC @ 81,783.76 for $45.80
2026-10-15 14:56 UTC  SELL @ 81,991.81  profit $+0.11  saved $1.36
2026-10-15 14:50 UTC  BUY  0.00055944 BTC @ 81,637.19 for $45.72
2026-10-15 14:42 UTC  SELL @ 81,556.68  profit $+0.10  saved $1.36
2026-10-15 14:29 UTC  BUY  0.00055944 BTC @ 81,178.03 for $45.46
2026-10-15 13:26 UTC  SAFETY EXIT @ 80,344.01  loss $-1.97  now trading $45.93
2026-10-13 05:32 UTC  BUY  0.00056943 BTC @ 83,649.78 for $47.68
2026-10-13 05:14 UTC  SELL @ 83,698.71  profit $+0.13  saved $1.36
2026-10-13 03:37 UTC  BUY  0.00056943 BTC @ 83,319.83 for $47.49
2026-10-13 03:32 UTC  SELL @ 83,333.32  profit $+0.19  saved $1.36
```

## How it works

- Trades $50 each time; profit above that is set aside, never traded
- Buys when BTC drops 0.3% below its 1-hour high
- Sells when up $0.10 after fees (0.1% per trade)
- Safety exit if down $2.00, then waits 60 min before buying again
