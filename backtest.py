"""Replay the bot on past real BTC/EUR prices with different settings. Fake money only.

Run: python backtest.py [days]      (default 30)
     python backtest.py 2025        (a whole calendar year)
Each setting is also scored on the first and second half separately: a setting that only
wins in one half got lucky, not good.
"""
import json, sys, time, urllib.request
from datetime import datetime, timezone
import bot

ARG = sys.argv[1] if len(sys.argv) > 1 else "30"
if len(ARG) == 4:  # a year
    since = int(datetime(int(ARG), 1, 1, tzinfo=timezone.utc).timestamp() * 1000)
    until = int(datetime(int(ARG) + 1, 1, 1, tzinfo=timezone.utc).timestamp() * 1000)
else:
    until = int(time.time() * 1000)
    since = until - int(ARG) * 86_400_000
DAYS = (until - since) / 86_400_000
URL = "https://api.binance.com/api/v3/klines?symbol=BTCEUR&interval=1m&limit=1000&startTime="

c, start = [], since
while start < until:
    batch = json.load(urllib.request.urlopen(URL + str(start), timeout=10))
    if not batch:
        break
    c += [k for k in batch if k[0] < until]
    start = batch[-1][0] + 60_000
t = [k[0] / 1000 for k in c]
close = [float(k[4]) for k in c]
hi = [float(k[2]) for k in c]
high1h = [max(hi[max(0, i - 59):i + 1]) for i in range(len(c))]
print(f"{len(c)} minutes ({DAYS:.0f} days) of real BTC/EUR: €{close[0]:,.0f} -> €{close[-1]:,.0f} "
      f"({close[-1] / close[0] - 1:+.1%})")
print(f"Just buying €50 of BTC and holding it: €{50 * (close[-1] / close[0] - 1):+.2f}\n")


def run(dip, take, stop, a, b):
    """Profit (€) trading prices a..b with these settings, plus the bot's final state."""
    bot.DIP, bot.TAKE_PROFIT, bot.STOP_LOSS = dip, take, stop
    s = {"cash": 50.0, "saved": 0.0, "holding": False, "btc": 0.0, "cost": 0.0,
         "wait_until": 0, "wins": 0, "losses": 0}
    for i in range(a, b):
        bot.step(s, close[i], high1h[i], t[i])
    return s["cash"] + s["saved"] + s["btc"] * close[b - 1] * (1 - bot.FEE) - 50, s


mid, end = len(c) // 2, len(c)
rows = []
for dip in (0.003, 0.005, 0.01):
    for take in (0.10, 0.25, 0.50):
        for stop in (1.0, 2.0, 5.0, 1000.0):  # 1000 = no safety exit
            p, s = run(dip, take, stop, 60, end)
            rows.append((p, run(dip, take, stop, 60, mid)[0], run(dip, take, stop, mid, end)[0],
                         dip, take, stop, s))

print("buy dip  take  stop  | wins stops holding | total   1st half 2nd half | per day")
for p, h1, h2, dip, take, stop, s in sorted(rows, key=lambda r: -r[0]):
    now_ = " <- now" if (dip, take, stop) == (0.003, 0.10, 2.0) else ""
    print(f"{dip:6.1%}  €{take:.2f} {'none' if stop > 100 else f'€{stop:.0f}':>5} | {s['wins']:4} {s['losses']:5} "
          f"{'yes' if s['holding'] else 'no':>7} | €{p:+6.2f}  €{h1:+6.2f}  €{h2:+6.2f} | €{p / DAYS:+.2f}{now_}")
