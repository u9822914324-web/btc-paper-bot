# BTC paper bot

**Fake money test.** Real Bitcoin prices from Binance, no real money used.

| | |
|---|---|
| Started with | $50.00 |
| Worth now | **$32.98** |
| Saved (profit set aside, never traded) | **$1.36** |
| Total profit (if sold now) | **-$17.02** (-34.03%) |
| Profit today (from sells, UTC) | **+$0.00** |
| Average per day | -$0.28 |
| Wins / safety exits | 55 / 11 |
| Right now | holding BTC (bought for $32.78) |
| BTC price | $57,033.50 |
| Updated | 2026-11-21 03:33 UTC (every hour + every trade) |

## Profit per day (from sells, UTC)

| Day | Profit |
|---|---|
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
2026-11-20 16:21 UTC  BUY  0.00054945 BTC @ 59,407.51 for $32.67
2026-11-20 15:21 UTC  SAFETY EXIT @ 60,204.96  loss $-2.00  now trading $32.90
2026-11-19 11:01 UTC  BUY  0.00053946 BTC @ 63,786.54 for $34.44
2026-11-19 10:51 UTC  SELL @ 63,973.30  profit $+0.11  saved $1.36
2026-11-19 07:11 UTC  BUY  0.00053946 BTC @ 63,646.66 for $34.37
2026-11-19 07:08 UTC  SELL @ 63,875.05  profit $+0.10  saved $1.36
2026-11-19 04:51 UTC  BUY  0.00053946 BTC @ 63,561.53 for $34.32
2026-11-19 04:46 UTC  SELL @ 63,598.47  profit $+0.12  saved $1.36
2026-11-18 17:30 UTC  BUY  0.00053946 BTC @ 63,235.80 for $34.15
2026-11-18 16:20 UTC  SAFETY EXIT @ 62,324.13  loss $-1.99  now trading $34.42
```

## How it works

- Trades $50 each time; profit above that is set aside, never traded
- Buys when BTC drops 0.3% below its 1-hour high
- Sells when up $0.10 after fees (0.1% per trade)
- Safety exit if down $2.00, then waits 60 min before buying again
