"""Replay the bot on the last 48 hours of real BTC prices. Run: python backtest.py"""
import json, time, urllib.request
import bot

URL = "https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=1000&startTime="
now = int(time.time() * 1000)
c, start = [], now - 48 * 3600 * 1000
while start < now:
    batch = json.load(urllib.request.urlopen(URL + str(start), timeout=10))
    if not batch:
        break
    c += batch
    start = batch[-1][0] + 60000
print(len(c), "minutes of real prices")

for dip in (0.01, 0.005, 0.003):
    bot.DIP = dip
    s = {"cash": 50.0, "btc": 0.0, "cost": 0.0, "wait_until": 0, "wins": 0, "losses": 0}
    for i in range(60, len(c)):
        high = max(float(k[2]) for k in c[i - 59:i + 1])
        msg = bot.step(s, float(c[i][4]), high, c[i][0] / 1000)
        if msg:
            print(f"  {time.strftime('%m-%d %H:%M', time.localtime(c[i][0] / 1000))} {msg}")
    worth = s["cash"] + s["btc"] * float(c[-1][4]) * (1 - bot.FEE)
    print(f"DIP {dip:.1%}: wins {s['wins']} losses {s['losses']} "
          f"still holding {bool(s['btc'])} worth ${worth:.2f}\n")
