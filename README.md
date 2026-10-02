# BTC paper bot

**Fake money test.** Real Bitcoin prices from Binance, no real money used.

| | |
|---|---|
| Started with | $50.00 |
| Worth now | **$50.96** |
| Saved (profit set aside, never traded) | **$1.06** |
| Total profit (if sold now) | **+$0.96** (+1.92%) |
| Profit today (from sells, UTC) | **+$0.25** |
| Average per day | +$0.21 |
| Wins / safety exits | 7 / 0 |
| Right now | holding BTC (bought for $49.40) |
| BTC price | $85,988.01 |
| Updated | 2026-10-02 06:17 UTC (every hour + every trade) |

## Profit per day (from sells, UTC)

| Day | Profit |
|---|---|
| 2026-10-02 | +$0.25 |
| 2026-09-30 | +$0.60 |
| 2026-09-29 | +$0.21 |

## Last 10 trades (newest first)

```
2026-10-02 06:17 UTC  BUY  0.00056943 BTC @ 85,988.01 for $49.01
2026-10-02 06:17 UTC  SELL @ 85,972.00  profit $+0.25  saved $1.06
2026-09-30 13:14 UTC  BUY  0.00059451 BTC @ 85,382.00 for $50.81
2026-09-30 13:09 UTC  SELL @ 85,608.18  profit $+0.13  cash $50.81
2026-09-30 13:01 UTC  BUY  0.00059413 BTC @ 85,213.91 for $50.68
2026-09-30 12:49 UTC  SELL @ 85,154.99  profit $+0.11  cash $50.68
2026-09-30 12:42 UTC  BUY  0.00059573 BTC @ 84,800.00 for $50.57
2026-09-30 12:40 UTC  SELL @ 84,946.12  profit $+0.13  cash $50.57
2026-09-30 12:37 UTC  BUY  0.00059590 BTC @ 84,555.66 for $50.44
2026-09-30 12:35 UTC  SELL @ 84,793.75  profit $+0.23  cash $50.44
```

## How it works

- Trades $50 each time; profit above that is set aside, never traded
- Buys when BTC drops 0.3% below its 1-hour high
- Sells when up $0.10 after fees (0.1% per trade)
- Safety exit if down $2.00, then waits 60 min before buying again
