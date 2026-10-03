"""Replay the bot on real BTC/EUR prices for 2024, 2025 and 2026 so far. Fake money only.

Run: python backtest.py
A setting is only good if it holds up in every year: 2024 went up, 2025 went down.
Prices are cached in data/ after the first run (that first run takes a few minutes).
"""
import json, time, urllib.request
from datetime import datetime, timezone
from pathlib import Path
import bot

URL = "https://api.binance.com/api/v3/klines?symbol=BTCEUR&interval=1m&limit=1000&startTime={}"
CACHE = Path(__file__).parent / "data"
MONTH = 30 * 1440  # minutes of history needed before trading starts (longest trend average)


def ms(y, m=1, d=1):
    return int(datetime(y, m, d, tzinfo=timezone.utc).timestamp() * 1000)


def candles(since, until):
    """[time, high, close] per minute; cached on disk (until is always a past midnight)."""
    f = CACHE / f"BTCEUR-{since}-{until}.json"
    if f.exists():
        return json.loads(f.read_text())
    c, start = [], since
    while start < until:
        batch = json.load(urllib.request.urlopen(URL.format(start), timeout=10))
        if not batch:
            break
        c += [[k[0] / 1000, float(k[2]), float(k[4])] for k in batch if k[0] < until]
        start = batch[-1][0] + 60_000
    CACHE.mkdir(exist_ok=True)
    f.write_text(json.dumps(c))
    return c


def prepare(since, until):
    c = candles(since - MONTH * 60_000, until)
    t, hi, close = (list(x) for x in zip(*c))
    high1h = [max(hi[max(0, i - 59):i + 1]) for i in range(len(c))]
    sums = [0.0]
    for x in close:
        sums.append(sums[-1] + x)
    first = next(i for i, x in enumerate(t) if x >= since / 1000)
    return t, close, high1h, sums, first


def run(p, trend, take, stop):
    """Profit (€) over one period with these settings, plus the bot's final state."""
    t, close, high1h, sums, first = p
    bot.TAKE_PROFIT, bot.STOP_LOSS = take, stop
    s = {"cash": 50.0, "saved": 0.0, "holding": False, "btc": 0.0, "cost": 0.0,
         "wait_until": 0, "wins": 0, "losses": 0}
    for i in range(first, len(t)):
        avg = (sums[i + 1] - sums[i + 1 - trend]) / trend if trend else 0.0
        bot.step(s, close[i], high1h[i], t[i], avg)
    return s["cash"] + s["saved"] + s["btc"] * close[-1] * (1 - bot.FEE) - 50, s


today = datetime.now(timezone.utc)
PERIODS = {"2024": (ms(2024), ms(2025)), "2025": (ms(2025), ms(2026)),
           "2026": (ms(2026), ms(today.year, today.month, today.day))}
data = {}
for name, (a, b) in PERIODS.items():
    data[name] = p = prepare(a, b)
    t, close, *_, first = p
    move = close[-1] / close[first] - 1
    print(f"{name}: BTC/EUR €{close[first]:,.0f} -> €{close[-1]:,.0f} ({move:+.1%}), "
          f"just holding €50 of BTC: €{50 * move:+.2f}")

TRENDS = {0: "none", 1440: "1 day", 7 * 1440: "7 days", MONTH: "30 days"}
rows = []
for trend in TRENDS:
    for take in (0.10, 0.25, 0.50):
        for stop in (2.0, 5.0, 1000.0):  # 1000 = no safety exit
            results = [run(data[n], trend, take, stop) for n in PERIODS]
            rows.append((trend, take, stop, [r[0] for r in results], [r[1] for r in results]))

print("\nbuy only above | take  stop  |   2024    2025    2026 | worst year | trades (wins/stops)")
for trend, take, stop, profits, states in sorted(rows, key=lambda r: -min(r[3])):
    now_ = "  <- now" if (trend, take, stop) == (0, 0.10, 2.0) else ""
    trades = " ".join(f"{s['wins']}/{s['losses']}" for s in states)
    print(f"{TRENDS[trend]:>14} | €{take:.2f} {'none' if stop > 100 else f'€{stop:.0f}':>5} | "
          + " ".join(f"€{p:+6.2f}" for p in profits) + f" |   €{min(profits):+6.2f} | {trades}{now_}")
