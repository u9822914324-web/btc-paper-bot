# BTC paper bot

**Fake money test.** Real Bitcoin prices from Binance, no real money used.

| | |
|---|---|
| Started with | $50.00 |
| Worth now | **$37.35** |
| Saved (profit set aside, never traded) | **$1.36** |
| Total profit (if sold now) | **-$12.65** (-25.29%) |
| Profit today (from sells, UTC) | **+$0.00** |
| Average per day | -$0.23 |
| Wins / safety exits | 52 / 9 |
| Right now | holding BTC (bought for $36.48) |
| BTC price | $64,726.01 |
| Updated | 2026-11-18 05:21 UTC (every hour + every trade) |

## Profit per day (from sells, UTC)

| Day | Profit |
|---|---|
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
2026-11-15 09:07 UTC  BUY  0.00054945 BTC @ 65,813.16 for $36.20
2026-11-15 09:06 UTC  SELL @ 65,992.39  profit $+0.12  saved $1.36
2026-11-15 09:05 UTC  BUY  0.00054945 BTC @ 65,648.55 for $36.11
2026-11-15 09:03 UTC  SELL @ 65,693.99  profit $+0.11  saved $1.36
2026-11-15 03:03 UTC  BUY  0.00054945 BTC @ 65,365.01 for $35.95
2026-11-15 03:00 UTC  SELL @ 65,064.18  profit $+0.11  saved $1.36
2026-11-15 02:39 UTC  BUY  0.00054945 BTC @ 64,736.01 for $35.60
2026-11-15 02:31 UTC  SELL @ 64,704.47  profit $+0.15  saved $1.36
2026-11-15 00:13 UTC  BUY  0.00054945 BTC @ 64,304.75 for $35.37
2026-11-15 00:12 UTC  SELL @ 64,286.01  profit $+0.11  saved $1.36
```

## How it works

- Trades $50 each time; profit above that is set aside, never traded
- Buys when BTC drops 0.3% below its 1-hour high
- Sells when up $0.10 after fees (0.1% per trade)
- Safety exit if down $2.00, then waits 60 min before buying again
