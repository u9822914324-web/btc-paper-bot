"""Paper-trading BTC bot. Fake money, real Binance prices. No account or API key needed.

Run:        python bot.py
Self-test:  python bot.py test
Ctrl+C stops it. Run again to resume where it left off (state.json).
Delete state.json and trades.log to start over with fresh $50.
"""
import json, os, sys, time, urllib.request
from datetime import datetime
from pathlib import Path

START_CASH = 50.00   # fake dollars
FEE = 0.001          # Binance spot fee, 0.1% per trade
TAKE_PROFIT = 0.10   # sell when up this many dollars after fees
STOP_LOSS = 2.00     # safety exit: sell when down this many dollars after fees
DIP = 0.003          # only buy when price is 0.3% under the last hour's high
COOLDOWN = 3600      # seconds to wait after a safety exit before buying again
POLL = 15            # seconds between price checks
RUN_SECONDS = int(os.environ.get("RUN_SECONDS", 0))  # 0 = forever; cloud stops before GitHub's 6h limit

HERE = Path(__file__).parent
STATE = HERE / "state.json"
LOG = HERE / "trades.log"
URLS = [  # public price data only; second one for places where binance.com is blocked
    "https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=60",
    "https://api.binance.us/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=60",
]


def fetch():
    """Return (price now, highest price in the last 60 minutes)."""
    for url in URLS:
        try:
            with urllib.request.urlopen(url, timeout=10) as r:
                candles = json.load(r)
            return float(candles[-1][4]), max(float(c[2]) for c in candles)
        except Exception as e:
            err = e
    raise err


def step(s, price, high, now):
    """One price check. Updates state s, returns a trade message or None."""
    if s["btc"] == 0:
        if now < s["wait_until"] or price > high * (1 - DIP):
            return None
        s["cost"] = s["cash"]
        s["btc"] = s["cash"] * (1 - FEE) / price
        s["cash"] = 0.0
        return f"BUY  {s['btc']:.8f} BTC @ {price:,.2f} for ${s['cost']:.2f}"

    value = s["btc"] * price * (1 - FEE)
    pnl = value - s["cost"]
    if -STOP_LOSS < pnl < TAKE_PROFIT:
        return None
    s["cash"], s["btc"] = value, 0.0
    if pnl > 0:
        s["wins"] += 1
        return f"SELL @ {price:,.2f}  profit ${pnl:+.2f}  cash ${value:.2f}"
    s["losses"] += 1
    s["wait_until"] = now + COOLDOWN
    return f"SAFETY EXIT @ {price:,.2f}  loss ${pnl:+.2f}  cash ${value:.2f}"


def main():
    s = json.loads(STATE.read_text()) if STATE.exists() else {
        "cash": START_CASH, "btc": 0.0, "cost": 0.0, "wait_until": 0, "wins": 0, "losses": 0}
    print(f"Paper bot running with FAKE money. Ctrl+C to stop. Trades go to {LOG.name}")
    end = time.time() + RUN_SECONDS if RUN_SECONDS else float("inf")
    while time.time() < end:
        try:
            price, high = fetch()
        except Exception as e:
            print(f"\nCan't get price ({e}), trying again...")
            time.sleep(POLL)
            continue
        msg = step(s, price, high, time.time())
        if msg:
            line = f"{datetime.now():%Y-%m-%d %H:%M:%S}  {msg}"
            print("\n" + line)
            with LOG.open("a") as f:
                f.write(line + "\n")
            STATE.write_text(json.dumps(s))
        worth = s["cash"] + s["btc"] * price * (1 - FEE)
        status = "holding BTC" if s["btc"] else "waiting to buy"
        print(f"BTC ${price:,.2f} | {status} | worth ${worth:.2f} | "
              f"wins {s['wins']} losses {s['losses']}   ", end="\r")
        time.sleep(POLL)


def test():
    s = {"cash": 50.0, "btc": 0.0, "cost": 0.0, "wait_until": 0, "wins": 0, "losses": 0}
    assert step(s, 100_000, 100_000, 0) is None                    # no dip: wait
    assert step(s, 98_900, 100_000, 0).startswith("BUY")           # 1.1% dip: buy
    assert step(s, 99_000, 100_000, 0) is None                     # up, but fees not covered
    assert step(s, 99_400, 100_000, 0).startswith("SELL")          # +$0.15 after fees
    assert s["cash"] > 50.10 and s["wins"] == 1
    assert step(s, 98_000, 100_000, 0).startswith("BUY")
    assert step(s, 94_000, 100_000, 0).startswith("SAFETY")        # -$2.14: bail out
    assert s["losses"] == 1 and s["btc"] == 0
    assert step(s, 90_000, 100_000, 10) is None                    # cooldown blocks rebuy
    assert step(s, 90_000, 100_000, COOLDOWN + 1).startswith("BUY")
    print("all tests passed")


if __name__ == "__main__":
    try:
        test() if sys.argv[1:] == ["test"] else main()
    except KeyboardInterrupt:
        print("\nStopped. Run again to continue.")
