# BTC paper bot

**Fake money test.** Real Bitcoin prices from Binance, no real money used.

| | |
|---|---|
| Started with | $50.00 |
| Worth now | **$49.62** |
| Profit | **-$0.38** (-0.75%) |
| Wins / safety exits | 2 / 0 |
| Right now | holding BTC (bought for $50.21) |
| BTC price | $83,425.00 |
| Updated | 2026-09-29 21:46 UTC (every hour + every trade) |

## Last 10 trades (newest first)

```
2026-09-29 12:19 UTC  BUY  0.00059542 BTC @ 84,245.04 for $50.21
2026-09-29 11:56 UTC  SELL @ 84,447.29  profit $+0.10  cash $50.21
2026-09-29 08:31 UTC  BUY  0.00059518 BTC @ 84,106.01 for $50.11
2026-09-29 08:22 UTC  SELL @ 84,368.00  profit $+0.11  cash $50.11
2026-09-28 02:01:26  BUY  0.00059452 BTC @ 84,017.42 for $50.00
```

## How it works

- Buys when BTC drops 0.3% below its 1-hour high
- Sells when up $0.10 after fees (0.1% per trade)
- Safety exit if down $2.00, then waits 60 min before buying again
