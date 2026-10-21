# BTC paper bot

**Fake money test.** Real Bitcoin prices from Binance, no real money used.

| | |
|---|---|
| Started with | $50.00 |
| Worth now | **$48.95** |
| Saved (profit set aside, never traded) | **$1.36** |
| Total profit (if sold now) | **-$1.05** (-2.09%) |
| Profit today (from sells, UTC) | **+$0.35** |
| Average per day | -$0.04 |
| Wins / safety exits | 24 / 2 |
| Right now | holding BTC (bought for $47.61) |
| BTC price | $84,462.43 |
| Updated | 2026-10-21 15:03 UTC (every hour + every trade) |

## Profit per day (from sells, UTC)

| Day | Profit |
|---|---|
| 2026-10-21 | +$0.35 |
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
2026-10-21 15:03 UTC  BUY  0.00055944 BTC @ 84,462.43 for $47.30
2026-10-21 14:43 UTC  SELL @ 84,260.00  profit $+0.11  saved $1.36
2026-10-21 14:29 UTC  BUY  0.00055944 BTC @ 83,888.56 for $46.98
2026-10-21 14:22 UTC  SELL @ 83,990.00  profit $+0.12  saved $1.36
2026-10-21 13:30 UTC  BUY  0.00055944 BTC @ 83,618.00 for $46.83
2026-10-21 10:58 UTC  SELL @ 83,429.88  profit $+0.12  saved $1.36
2026-10-20 14:16 UTC  BUY  0.00055944 BTC @ 83,054.45 for $46.51
2026-10-20 14:10 UTC  SELL @ 83,042.23  profit $+0.11  saved $1.36
2026-10-16 11:40 UTC  BUY  0.00055944 BTC @ 82,688.01 for $46.31
2026-10-16 11:20 UTC  SELL @ 82,718.01  profit $+0.10  saved $1.36
```

## How it works

- Trades $50 each time; profit above that is set aside, never traded
- Buys when BTC drops 0.3% below its 1-hour high
- Sells when up $0.10 after fees (0.1% per trade)
- Safety exit if down $2.00, then waits 60 min before buying again
