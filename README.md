# BTC paper bot

**Fake money test.** Real Bitcoin prices from Binance, no real money used.

| | |
|---|---|
| Started with | $50.00 |
| Worth now | **$44.75** |
| Saved (profit set aside, never traded) | **$1.36** |
| Total profit (if sold now) | **-$5.25** (-10.49%) |
| Profit today (from sells, UTC) | **+$0.00** |
| Average per day | -$0.11 |
| Wins / safety exits | 32 / 4 |
| Right now | holding BTC (bought for $43.89) |
| BTC price | $76,947.25 |
| Updated | 2026-11-03 02:17 UTC (every hour + every trade) |

## Profit per day (from sells, UTC)

| Day | Profit |
|---|---|
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
2026-11-02 03:59 UTC  BUY  0.00054945 BTC @ 78,634.01 for $43.25
2026-11-02 03:57 UTC  SELL @ 78,725.00  profit $+0.10  saved $1.36
2026-11-02 02:01 UTC  BUY  0.00054945 BTC @ 78,386.00 for $43.11
2026-11-02 01:26 UTC  SELL @ 78,622.23  profit $+0.10  saved $1.36
2026-11-02 00:09 UTC  BUY  0.00054945 BTC @ 78,286.00 for $43.06
2026-11-01 23:38 UTC  SELL @ 78,359.95  profit $+0.11  saved $1.36
2026-10-30 04:02 UTC  BUY  0.00054945 BTC @ 78,018.00 for $42.91
2026-10-30 03:30 UTC  SELL @ 77,704.00  profit $+0.12  saved $1.36
2026-10-30 02:50 UTC  BUY  0.00055944 BTC @ 77,336.97 for $43.31
2026-10-30 02:38 UTC  SELL @ 77,504.55  profit $+0.11  saved $1.36
```

## How it works

- Trades $50 each time; profit above that is set aside, never traded
- Buys when BTC drops 0.3% below its 1-hour high
- Sells when up $0.10 after fees (0.1% per trade)
- Safety exit if down $2.00, then waits 60 min before buying again
