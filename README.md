# BTC paper bot

**Fake money test.** Real Bitcoin prices from Binance, no real money used.

| | |
|---|---|
| Started with | $50.00 |
| Worth now | **$48.16** |
| Saved (profit set aside, never traded) | **$1.36** |
| Total profit (if sold now) | **-$1.84** (-3.68%) |
| Profit today (from sells, UTC) | **+$0.00** |
| Average per day | -$0.06 |
| Wins / safety exits | 20 / 2 |
| Right now | holding BTC (bought for $46.80) |
| BTC price | $82,092.00 |
| Updated | 2026-10-20 03:56 UTC (every hour + every trade) |

## Profit per day (from sells, UTC)

| Day | Profit |
|---|---|
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
2026-10-16 11:40 UTC  BUY  0.00055944 BTC @ 82,688.01 for $46.31
2026-10-16 11:20 UTC  SELL @ 82,718.01  profit $+0.10  saved $1.36
2026-10-15 15:41 UTC  BUY  0.00055944 BTC @ 82,379.27 for $46.13
2026-10-15 15:18 UTC  SELL @ 82,364.90  profit $+0.10  saved $1.36
2026-10-15 15:07 UTC  BUY  0.00055944 BTC @ 82,017.98 for $45.93
2026-10-15 15:05 UTC  SELL @ 82,197.14  profit $+0.14  saved $1.36
2026-10-15 15:01 UTC  BUY  0.00055944 BTC @ 81,783.76 for $45.80
2026-10-15 14:56 UTC  SELL @ 81,991.81  profit $+0.11  saved $1.36
2026-10-15 14:50 UTC  BUY  0.00055944 BTC @ 81,637.19 for $45.72
2026-10-15 14:42 UTC  SELL @ 81,556.68  profit $+0.10  saved $1.36
```

## How it works

- Trades $50 each time; profit above that is set aside, never traded
- Buys when BTC drops 0.3% below its 1-hour high
- Sells when up $0.10 after fees (0.1% per trade)
- Safety exit if down $2.00, then waits 60 min before buying again
