# BTC paper bot

**Fake money test.** Real Bitcoin prices from Binance, no real money used.

| | |
|---|---|
| Started with | $50.00 |
| Worth now | **$33.43** |
| Saved (profit set aside, never traded) | **$1.36** |
| Total profit (if sold now) | **-$16.57** (-33.13%) |
| Profit today (from sells, UTC) | **+$0.50** |
| Average per day | -$0.25 |
| Wins / safety exits | 69 / 13 |
| Right now | holding BTC (bought for $32.92) |
| BTC price | $59,963.00 |
| Updated | 2026-11-27 18:56 UTC (every hour + every trade) |

## Profit per day (from sells, UTC)

| Day | Profit |
|---|---|
| 2026-11-27 | +$0.50 |
| 2026-11-26 | +$0.39 |
| 2026-11-25 | -$1.64 |
| 2026-11-23 | +$0.36 |
| 2026-11-22 | +$0.16 |
| 2026-11-21 | +$0.32 |
| 2026-11-20 | -$2.00 |
| 2026-11-19 | +$0.33 |
| 2026-11-18 | -$1.99 |
| 2026-11-15 | +$0.60 |
| 2026-11-14 | -$3.90 |
| 2026-11-13 | -$1.97 |
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
2026-11-27 06:20 UTC  BUY  0.00052947 BTC @ 61,748.09 for $32.73
2026-11-27 06:12 UTC  SELL @ 61,944.00  profit $+0.11  saved $1.36
2026-11-27 02:26 UTC  BUY  0.00052947 BTC @ 61,619.74 for $32.66
2026-11-27 02:26 UTC  SELL @ 61,793.86  profit $+0.21  saved $1.36
2026-11-27 02:10 UTC  BUY  0.00052947 BTC @ 61,284.96 for $32.48
2026-11-27 02:07 UTC  SELL @ 61,372.47  profit $+0.18  saved $1.36
2026-11-26 02:27 UTC  BUY  0.00052947 BTC @ 60,912.92 for $32.28
2026-11-26 02:21 UTC  SELL @ 61,091.12  profit $+0.12  saved $1.36
2026-11-26 01:27 UTC  BUY  0.00051948 BTC @ 60,748.95 for $31.59
2026-11-26 01:25 UTC  SELL @ 60,892.88  profit $+0.27  saved $1.36
```

## How it works

- Trades $50 each time; profit above that is set aside, never traded
- Buys when BTC drops 0.3% below its 1-hour high
- Sells when up $0.10 after fees (0.1% per trade)
- Safety exit if down $2.00, then waits 60 min before buying again
