"""BTC bot. Fake money by default; `live` trades REAL money on Binance.com (BTC/EUR).

Fake money: python bot.py          (real prices, fake money; this is what runs on GitHub)
Check key:  python bot.py check    (tests your API key and shows your balance; buys NOTHING)
Real money: python bot.py live     (needs your key file, see KEYS below)
Self-test:  python bot.py test
Ctrl+C stops it. Run the same command again to resume where it left off.
"""
import base64, hashlib, hmac, json, math, os, socket, ssl, subprocess, sys, time
import urllib.error, urllib.parse, urllib.request
from datetime import datetime, timezone
from pathlib import Path

START_CASH = 50.00   # money traded each time; profit above this goes to cash, never traded
FEE = 0.001          # Binance spot fee, 0.1% per trade
TAKE_PROFIT = 0.10   # sell when up this much after fees
STOP_LOSS = 2.00     # safety exit: sell when down this much after fees
DIP = 0.003          # only buy when price is 0.3% under the last hour's high
COOLDOWN = 3600      # seconds to wait after a safety exit before buying again
POLL = 15            # fake-money mode: seconds between price checks (real money watches every change)
DECIMALS = 5         # Binance trades BTC in steps of 0.00001 (live mode reads the real value)
RUN_SECONDS = int(os.environ.get("RUN_SECONDS", 0))  # 0 = forever; cloud stops before GitHub's 6h limit

HERE = Path(__file__).parent
STATE, LOG, README = HERE / "state.json", HERE / "trades.log", HERE / "README.md"
SYMBOL, CUR, LIVE = "BTCUSDT", "$", False
URLS = [  # public price data only; second one for places where binance.com is blocked
    "https://data-api.binance.vision/api/v3/klines?symbol={}&interval=1m&limit=60",
    "https://api.binance.us/api/v3/klines?symbol={}&interval=1m&limit=60",
]

# Real money only. The key file lives OUTSIDE this folder so it can never end up on GitHub.
API = "https://api.binance.com"
STREAM_HOST = "stream.binance.com"
KEYS = Path.home() / "binance-keys.txt"  # line 1: API key, line 2: secret key
KEY = SECRET = ""
CLOCK = 0  # ms between this PC's clock and Binance's


def fetch():
    """Return (price now, highest price in the last 60 minutes)."""
    for url in URLS:
        try:
            with urllib.request.urlopen(url.format(SYMBOL), timeout=10) as r:
                candles = json.load(r)
            return float(candles[-1][4]), max(float(c[2]) for c in candles)
        except Exception as e:
            err = e
    raise err


def polled():
    """Fake-money mode: price every POLL seconds (works from GitHub's servers)."""
    while True:
        try:
            yield fetch()
        except Exception as e:
            print(f"\nCan't get price ({e}), trying again...")
        time.sleep(POLL)


def websocket(host, path):
    """Minimal WebSocket client (Python has none built in). Yields each text message."""
    raw = socket.create_connection((host, 443), timeout=30)
    sock = ssl.create_default_context().wrap_socket(raw, server_hostname=host)
    key = base64.b64encode(os.urandom(16)).decode()
    sock.sendall(f"GET {path} HTTP/1.1\r\nHost: {host}\r\nUpgrade: websocket\r\nConnection: Upgrade\r\n"
                 f"Sec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n".encode())
    f = sock.makefile("rb")
    if b" 101 " not in f.readline():
        raise ConnectionError("price stream refused the connection")
    while f.readline() not in (b"\r\n", b""):  # skip the rest of the handshake
        pass
    while True:
        head = f.read(2)
        if len(head) < 2:
            raise ConnectionError("price stream closed")
        n = head[1] & 127
        if n >= 126:
            n = int.from_bytes(f.read(2 if n == 126 else 8), "big")
        data, op = f.read(n), head[0] & 15
        if op == 1:
            yield data.decode()
        elif op == 9:  # Binance pings every ~20s; answer or it hangs up
            mask = os.urandom(4)
            sock.sendall(bytes([0x8A, 0x80 | len(data)]) + mask + bytes(b ^ mask[i % 4] for i, b in enumerate(data)))
        elif op == 8:
            raise ConnectionError("price stream closed")


def streamed():
    """Real-money mode: every BTC price change, live from Binance. Reconnects if the stream drops."""
    high, high_at = 0.0, 0.0
    while True:
        try:
            for msg in websocket(STREAM_HOST, f"/ws/{SYMBOL.lower()}@bookTicker"):  # every bid/ask move
                book = json.loads(msg)
                price = (float(book["b"]) + float(book["a"])) / 2
                if time.time() - high_at > 60:  # refresh the 1-hour high once a minute
                    high, high_at = fetch()[1], time.time()
                yield price, max(high, price)
        except Exception as e:
            print(f"\nPrice stream dropped ({e}), reconnecting...")
            time.sleep(5)


def lot(btc):
    """Round BTC down to what Binance accepts (whole 0.00001 steps)."""
    return math.floor(btc * 10 ** DECIMALS + 1e-9) / 10 ** DECIMALS


def paper_buy(money, price):
    """Fake market buy with Binance's rounding and fee. Returns (BTC received, money spent)."""
    qty = lot(money / price)
    return qty * (1 - FEE), qty * price


def paper_sell(qty, price):
    """Fake market sell. Returns money received after fee."""
    return qty * price * (1 - FEE)


def sign(query, secret):
    return hmac.new(secret.encode(), query.encode(), hashlib.sha256).hexdigest()


def signed(method, path, **params):
    """Call a private Binance endpoint with your API key. Raises with Binance's error message."""
    q = urllib.parse.urlencode({**params, "recvWindow": 10000, "timestamp": int(time.time() * 1000) + CLOCK})
    req = urllib.request.Request(f"{API}{path}?{q}&signature={sign(q, SECRET)}", method=method,
                                 headers={"X-MBX-APIKEY": KEY})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"Binance said: {e.read().decode()}") from None


def live_buy(money, price):
    """REAL market buy for `money` euros. Returns (BTC received after fee, euros spent)."""
    o = signed("POST", "/api/v3/order", symbol=SYMBOL, side="BUY", type="MARKET",
               quoteOrderQty=f"{money:.2f}", newOrderRespType="FULL")
    fee = sum(float(f["commission"]) for f in o["fills"] if f["commissionAsset"] == "BTC")
    return float(o["executedQty"]) - fee, float(o["cummulativeQuoteQty"])


def live_sell(qty, price):
    """REAL market sell of qty BTC. Returns euros received after fee."""
    o = signed("POST", "/api/v3/order", symbol=SYMBOL, side="SELL", type="MARKET",
               quantity=f"{qty:.{DECIMALS}f}", newOrderRespType="FULL")
    fee = sum(float(f["commission"]) for f in o["fills"] if f["commissionAsset"] == SYMBOL[3:])
    return float(o["cummulativeQuoteQty"]) - fee


BUY, SELL = paper_buy, paper_sell  # go_live() swaps in the real ones


def step(s, price, high, now):
    """One price check. Updates state s, returns a trade message or None.

    Binance only sells whole 0.00001 BTC steps, so a few crumbs of BTC can stay behind after a sell.
    They keep their share of the cost in s["cost"] and get sold with the next trade.
    """
    if not s["holding"]:
        if now < s["wait_until"] or price > high * (1 - DIP) or s["cash"] < 10:
            return None
        got, spent = BUY(s["cash"], price)
        s["btc"] += got
        s["cost"] += spent
        s["cash"] -= spent
        s["holding"] = True
        return f"BUY  {got:.8f} BTC @ {price:,.2f} for {CUR}{spent:.2f}"

    pnl = s["btc"] * price * (1 - FEE) - s["cost"]  # estimate, to decide
    if -STOP_LOSS < pnl < TAKE_PROFIT:
        return None
    qty = lot(s["btc"])
    got = SELL(qty, price)  # money actually received (the real fill in live mode)
    sold_cost = s["cost"] * qty / s["btc"]
    pnl = got - sold_cost
    s["btc"] -= qty
    s["cost"] -= sold_cost
    total = s["cash"] + got
    s["cash"] = min(total, START_CASH - s["cost"])  # trade at most START_CASH next time
    s["saved"] += total - s["cash"]                 # profit above that goes to cash, never traded again
    s["holding"] = False
    if pnl > 0:
        s["wins"] += 1
        return f"SELL @ {price:,.2f}  profit {CUR}{pnl:+.2f}  saved {CUR}{s['saved']:.2f}"
    s["losses"] += 1
    s["wait_until"] = now + COOLDOWN
    return f"SAFETY EXIT @ {price:,.2f}  loss {CUR}{pnl:+.2f}  now trading {CUR}{s['cash']:.2f}"


def money(x):
    return f"{'+' if x >= 0 else '-'}{CUR}{abs(x):.2f}"


def daily_profit(lines):
    """Locked-in profit per UTC day, added up from the SELL / SAFETY EXIT lines in the trade log."""
    days = {}
    for line in lines:
        if f"profit {CUR}" in line or f"loss {CUR}" in line:
            days[line[:10]] = days.get(line[:10], 0) + float(line.split(CUR)[1].split()[0])
    return days


def report(s, price):
    """Write the scoreboard (README.md on the GitHub page; live-scoreboard.md for real money)."""
    worth = s["cash"] + s["saved"] + s["btc"] * price * (1 - FEE)
    profit = worth - START_CASH
    doing = f"holding BTC (bought for {CUR}{s['cost']:.2f})" if s["holding"] else "waiting to buy"
    lines = LOG.read_text(encoding="utf-8").splitlines() if LOG.exists() else []
    recent = lines[::-1][:10] or ["no trades yet"]
    days = daily_profit(lines)
    today = f"{datetime.now(timezone.utc):%Y-%m-%d}"
    ran = (datetime.fromisoformat(today) - datetime.fromisoformat(lines[0][:10])).days + 1 if lines else 1
    avg = sum(days.values()) / ran  # over every day since the first trade, not just days with sells
    README.write_text(
        ("# BTC bot (REAL money)\n\n**Real money** on Binance.com, BTC/EUR.\n\n" if LIVE else
         "# BTC paper bot\n\n**Fake money test.** Real Bitcoin prices from Binance, no real money used.\n\n")
        + "| | |\n|---|---|\n"
        f"| Started with | {CUR}{START_CASH:.2f} |\n"
        f"| Worth now | **{CUR}{worth:.2f}** |\n"
        f"| Saved (profit set aside, never traded) | **{CUR}{s['saved']:.2f}** |\n"
        f"| Total profit (if sold now) | **{money(profit)}** ({profit / START_CASH:+.2%}) |\n"
        f"| Profit today (from sells, UTC) | **{money(days.get(today, 0))}** |\n"
        f"| Average per day | {money(avg)} |\n"
        f"| Wins / safety exits | {s['wins']} / {s['losses']} |\n"
        f"| Right now | {doing} |\n"
        f"| BTC price | {CUR}{price:,.2f} |\n"
        f"| Updated | {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC (every hour + every trade) |\n\n"
        "## Profit per day (from sells, UTC)\n\n| Day | Profit |\n|---|---|\n"
        + "".join(f"| {d} | {money(p)} |\n" for d, p in sorted(days.items(), reverse=True)) + "\n"
        "## Last 10 trades (newest first)\n\n```\n" + "\n".join(recent) + "\n```\n\n"
        "## How it works\n\n"
        f"- Trades {CUR}{START_CASH:.0f} each time; profit above that is set aside, never traded\n"
        f"- Buys when BTC drops {DIP:.1%} below its 1-hour high\n"
        f"- Sells when up {CUR}{TAKE_PROFIT:.2f} after fees ({FEE:.1%} per trade)\n"
        f"- Safety exit if down {CUR}{STOP_LOSS:.2f}, then waits {COOLDOWN // 60} min before buying again\n",
        encoding="utf-8")


def log(msg):
    line = f"{datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC  {msg}"
    print("\n" + line)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def main():
    s = json.loads(STATE.read_text()) if STATE.exists() else {
        "cash": START_CASH, "btc": 0.0, "cost": 0.0, "wait_until": 0, "wins": 0, "losses": 0}
    s.setdefault("saved", 0.0)             # older state files
    s.setdefault("holding", s["btc"] > 0)
    if s.get("halted"):
        sys.exit(f"Bot is stopped because an order failed:\n  {s['halted']}\n"
                 f"Check your Binance account, then delete the \"halted\" part of {STATE.name} to restart.")
    print(f"Bot running with {'REAL' if LIVE else 'FAKE'} money ({SYMBOL}). Ctrl+C to stop. "
          f"Trades go to {LOG.name}")
    end = time.time() + RUN_SECONDS if RUN_SECONDS else float("inf")
    last_report = shown = 0
    for price, high in streamed() if LIVE else polled():
        if time.time() > end:
            break
        try:
            msg = step(s, price, high, time.time())
        except Exception as e:  # a real order failed: stop rather than guess whether it went through
            s["halted"] = str(e)
            STATE.write_text(json.dumps(s))
            log(f"ORDER FAILED, bot stopped: {e}")
            return
        if msg:
            log(msg)
            STATE.write_text(json.dumps(s))
        if msg or time.time() - last_report > 3600:
            report(s, price)
            last_report = time.time()
            if os.environ.get("PUSH"):  # cloud: put the scoreboard on the GitHub page
                subprocess.run("git add -A && git commit -qm 'bot: update scoreboard' "
                               "&& git pull -q --rebase && git push -q", shell=True)
        if time.time() - shown >= 1:  # status line at most once a second
            worth = s["cash"] + s["saved"] + s["btc"] * price * (1 - FEE)
            status = "holding BTC" if s["holding"] else "waiting to buy"
            print(f"BTC {CUR}{price:,.2f} | {status} | worth {CUR}{worth:.2f} | "
                  f"wins {s['wins']} losses {s['losses']}   ", end="\r")
            shown = time.time()


def go_live():
    """Switch to REAL money: load the key, read Binance's rules, use separate private files."""
    global LIVE, SYMBOL, CUR, URLS, KEY, SECRET, CLOCK, DECIMALS, BUY, SELL, STATE, LOG, README
    parts = KEYS.read_text(encoding="utf-8-sig").split() if KEYS.exists() else []
    if len(parts) < 2:
        sys.exit(f"No key file. Make {KEYS} with your API key on line 1 and secret key on line 2.")
    KEY, SECRET = parts[:2]
    LIVE, SYMBOL, CUR = True, "BTCEUR", "€"
    URLS = [API + "/api/v3/klines?symbol={}&interval=1m&limit=60"]
    STATE, LOG, README = HERE / "live-state.json", HERE / "live-trades.log", HERE / "live-scoreboard.md"
    BUY, SELL = live_buy, live_sell
    with urllib.request.urlopen(f"{API}/api/v3/time", timeout=10) as r:
        CLOCK = json.load(r)["serverTime"] - int(time.time() * 1000)
    with urllib.request.urlopen(f"{API}/api/v3/exchangeInfo?symbol={SYMBOL}", timeout=10) as r:
        lot_size = next(f for f in json.load(r)["symbols"][0]["filters"] if f["filterType"] == "LOT_SIZE")
    DECIMALS = len(lot_size["stepSize"].rstrip("0").split(".")[1])


def check():
    """Test the API key without trading anything."""
    go_live()
    acct = signed("GET", "/api/v3/account")
    free = {b["asset"]: float(b["free"]) for b in acct["balances"] if b["asset"] in ("EUR", "BTC")}
    print(f"Key works. Trading allowed: {acct['canTrade']}. Free in Spot wallet: {free}")
    if free.get("EUR", 0) < START_CASH:
        print(f"Note: the bot needs at least €{START_CASH:.0f} EUR in your Spot wallet.")
    if signed("GET", "/sapi/v1/account/apiRestrictions").get("enableWithdrawals"):
        print("WARNING: this key can WITHDRAW money. Turn withdrawals OFF for this key on Binance.")
    signed("POST", "/api/v3/order/test", symbol=SYMBOL, side="BUY", type="MARKET",
           quoteOrderQty=f"{START_CASH:.2f}")
    print(f"Binance accepted a TEST order for €{START_CASH:.2f} of BTC (nothing was bought).")


def test():
    global signed
    s = {"cash": 50.0, "saved": 0.0, "btc": 0.0, "cost": 0.0, "holding": False,
         "wait_until": 0, "wins": 0, "losses": 0}
    assert step(s, 100_000, 100_000, 0) is None                    # no dip: wait
    assert step(s, 98_900, 100_000, 0).startswith("BUY")           # 1.1% dip: buys 0.00050 BTC
    assert step(s, 99_000, 100_000, 0) is None                     # up, but fees not covered
    assert step(s, 99_400, 100_000, 0).startswith("SELL")          # +$0.15 after fees
    assert s["wins"] == 1 and s["saved"] > 0.10                    # profit goes to cash
    assert 0 < s["btc"] < 0.00001 and s["cash"] + s["cost"] <= 50 + 1e-9  # crumbs kept, $50 cap
    assert step(s, 98_000, 100_000, 0).startswith("BUY")
    assert s["cost"] <= 50                                         # trades $50, not $50.15
    assert step(s, 94_000, 100_000, 0).startswith("SAFETY")        # -$2.14: bail out
    assert s["losses"] == 1 and s["cash"] < 50
    assert step(s, 90_000, 100_000, 10) is None                    # cooldown blocks rebuy
    assert step(s, 90_000, 100_000, COOLDOWN + 1).startswith("BUY")
    assert s["cost"] < 50 and s["saved"] > 0.10                    # saved money never traded
    assert lot(0.00058941) == 0.00058
    d = daily_profit(["2026-09-29 08:22 UTC  SELL @ 84,368.00  profit $+0.11  saved $0.11",
                      "2026-09-29 09:00 UTC  BUY  0.0006 BTC @ 84,000.00 for $50.00",
                      "2026-09-29 11:56 UTC  SAFETY EXIT @ 82,000.00  loss $-2.14  now trading $47.86",
                      "2026-09-30 12:35 UTC  SELL @ 84,793.75  profit $+0.23  saved $0.34"])
    assert {k: round(v, 2) for k, v in d.items()} == {"2026-09-29": -2.03, "2026-09-30": 0.23}
    # Binance's documented signing example
    assert sign("symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1"
                "&recvWindow=5000&timestamp=1499827319559",
                "NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"
                ) == "c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71"
    # real-order parsing, against a fake Binance
    sent = []

    def fake(method, path, **p):
        sent.append(p)
        if p["side"] == "BUY":
            return {"executedQty": "0.00059000", "cummulativeQuoteQty": "49.98",
                    "fills": [{"commission": "0.00000059", "commissionAsset": "BTC"}]}
        return {"cummulativeQuoteQty": "50.20", "fills": [{"commission": "0.0502", "commissionAsset": "USDT"}]}

    real, signed = signed, fake
    try:
        assert live_buy(50, 84_000) == (0.00059 - 0.00000059, 49.98) and sent[-1]["quoteOrderQty"] == "50.00"
        assert abs(live_sell(0.00058, 85_000) - 50.1498) < 1e-9 and sent[-1]["quantity"] == "0.00058"
    finally:
        signed = real
    print("all tests passed")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    try:
        if cmd == "test":
            test()
        elif cmd == "check":
            check()
        else:
            if cmd == "live":
                go_live()
            main()
    except KeyboardInterrupt:
        print("\nStopped. Run the same command again to continue.")
    except RuntimeError as e:  # Binance error during `check`
        sys.exit(str(e))
