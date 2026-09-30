# BTC paper bot

**Fake money test.** Real Bitcoin prices from Binance, no real money used.

| | |
|---|---|
| Started with | $50.00 |
| Worth now | **$50.08** |
| Profit | **+$0.08** (+0.16%) |
| Wins / safety exits | 6 / 0 |
| Right now | holding BTC (bought for $50.81) |
| BTC price | $84,321.91 |
| Updated | 2026-09-30 16:15 UTC (every hour + every trade) |

## Last 10 trades (newest first)

```
2026-09-30 13:14 UTC  BUY  0.00059451 BTC @ 85,382.00 for $50.81
2026-09-30 13:09 UTC  SELL @ 85,608.18  profit $+0.13  cash $50.81
2026-09-30 13:01 UTC  BUY  0.00059413 BTC @ 85,213.91 for $50.68
2026-09-30 12:49 UTC  SELL @ 85,154.99  profit $+0.11  cash $50.68
2026-09-30 12:42 UTC  BUY  0.00059573 BTC @ 84,800.00 for $50.57
2026-09-30 12:40 UTC  SELL @ 84,946.12  profit $+0.13  cash $50.57
2026-09-30 12:37 UTC  BUY  0.00059590 BTC @ 84,555.66 for $50.44
2026-09-30 12:35 UTC  SELL @ 84,793.75  profit $+0.23  cash $50.44
2026-09-29 12:19 UTC  BUY  0.00059542 BTC @ 84,245.04 for $50.21
2026-09-29 11:56 UTC  SELL @ 84,447.29  profit $+0.10  cash $50.21
```

## How it works

- Buys when BTC drops 0.3% below its 1-hour high
- Sells when up $0.10 after fees (0.1% per trade)
- Safety exit if down $2.00, then waits 60 min before buying again
