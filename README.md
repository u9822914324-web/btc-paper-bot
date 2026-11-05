# BTC paper bot

**Fake money test.** Real Bitcoin prices from Binance, no real money used.

| | |
|---|---|
| Started with | $50.00 |
| Worth now | **$46.04** |
| Saved (profit set aside, never traded) | **$1.36** |
| Total profit (if sold now) | **-$3.96** (-7.93%) |
| Profit today (from sells, UTC) | **+$0.00** |
| Average per day | -$0.09 |
| Wins / safety exits | 36 / 4 |
| Right now | holding BTC (bought for $44.92) |
| BTC price | $80,425.75 |
| Updated | 2026-11-05 05:54 UTC (every hour + every trade) |

## Profit per day (from sells, UTC)

| Day | Profit |
|---|---|
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
2026-11-04 15:14 UTC  BUY  0.00054945 BTC @ 80,795.29 for $44.44
2026-11-04 15:08 UTC  SELL @ 80,578.51  profit $+0.13  saved $1.36
2026-11-04 15:07 UTC  BUY  0.00054945 BTC @ 80,188.33 for $44.10
2026-11-04 15:04 UTC  SELL @ 79,849.99  profit $+0.17  saved $1.36
2026-11-04 14:52 UTC  BUY  0.00054945 BTC @ 79,377.23 for $43.66
2026-11-04 14:49 UTC  SELL @ 79,617.64  profit $+0.14  saved $1.36
2026-11-04 14:46 UTC  BUY  0.00054945 BTC @ 79,213.71 for $43.57
2026-11-04 14:40 UTC  SELL @ 78,977.46  profit $+0.10  saved $1.36
2026-11-02 03:59 UTC  BUY  0.00054945 BTC @ 78,634.01 for $43.25
2026-11-02 03:57 UTC  SELL @ 78,725.00  profit $+0.10  saved $1.36
```

## How it works

- Trades $50 each time; profit above that is set aside, never traded
- Buys when BTC drops 0.3% below its 1-hour high
- Sells when up $0.10 after fees (0.1% per trade)
- Safety exit if down $2.00, then waits 60 min before buying again
