# BTC paper bot

**Fake money test.** Real Bitcoin prices from Binance, no real money used.

| | |
|---|---|
| Started with | $50.00 |
| Worth now | **$49.05** |
| Saved (profit set aside, never traded) | **$1.36** |
| Total profit (if sold now) | **-$0.95** (-1.90%) |
| Profit today (from sells, UTC) | **+$0.45** |
| Average per day | -$0.04 |
| Wins / safety exits | 25 / 2 |
| Right now | holding BTC (bought for $47.60) |
| BTC price | $84,515.39 |
| Updated | 2026-10-21 15:18 UTC (every hour + every trade) |

## Profit per day (from sells, UTC)

| Day | Profit |
|---|---|
| 2026-10-21 | +$0.45 |
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
2026-10-21 15:18 UTC  BUY  0.00055944 BTC @ 84,515.39 for $47.33
2026-10-21 15:10 UTC  SELL @ 84,808.10  profit $+0.10  saved $1.36
2026-10-21 15:03 UTC  BUY  0.00055944 BTC @ 84,462.43 for $47.30
2026-10-21 14:43 UTC  SELL @ 84,260.00  profit $+0.11  saved $1.36
2026-10-21 14:29 UTC  BUY  0.00055944 BTC @ 83,888.56 for $46.98
2026-10-21 14:22 UTC  SELL @ 83,990.00  profit $+0.12  saved $1.36
2026-10-21 13:30 UTC  BUY  0.00055944 BTC @ 83,618.00 for $46.83
2026-10-21 10:58 UTC  SELL @ 83,429.88  profit $+0.12  saved $1.36
2026-10-20 14:16 UTC  BUY  0.00055944 BTC @ 83,054.45 for $46.51
2026-10-20 14:10 UTC  SELL @ 83,042.23  profit $+0.11  saved $1.36
```

## How it works

- Trades $50 each time; profit above that is set aside, never traded
- Buys when BTC drops 0.3% below its 1-hour high
- Sells when up $0.10 after fees (0.1% per trade)
- Safety exit if down $2.00, then waits 60 min before buying again
