"""Funding history, 2024-04-01 to 2026-10-01 (outside both holdouts), four venues, public endpoints only."""
import os, pathlib
os.makedirs(pathlib.Path(__file__).resolve().parents[2] / "data" / "carry" / "data", exist_ok=True)
os.makedirs(pathlib.Path(__file__).resolve().parents[2] / "data" / "carry" / "wide", exist_ok=True)
os.chdir(pathlib.Path(__file__).resolve().parents[2] / "data" / "carry")  # downloads live here (not in git)
import io, sys, time, zipfile, datetime as dt
from concurrent.futures import ThreadPoolExecutor
import pandas as pd, requests
COINS = "BTC ETH SOL XRP DOGE ADA AVAX LINK LTC BCH DOT NEAR APT ARB OP SUI TIA WLD AAVE UNI".split()
S = int(dt.datetime(2024, 4, 1, tzinfo=dt.timezone.utc).timestamp() * 1000)
E = int(dt.datetime(2026, 10, 1, tzinfo=dt.timezone.utc).timestamp() * 1000)
ses = requests.Session()
def get(url, **kw):
    for i in range(5):
        try:
            r = ses.request(kw.pop("method", "GET"), url, timeout=30, **kw)
            if r.status_code == 429: time.sleep(2 + i); continue
            return r
        except requests.RequestException: time.sleep(1 + i)
    return None
def binance(c):
    parts, m = [], dt.date(2024, 4, 1)
    while m < dt.date(2026, 10, 1):
        r = get(f"https://data.binance.vision/data/futures/um/monthly/fundingRate/{c}USDT/{c}USDT-fundingRate-{m:%Y-%m}.zip")
        if r is not None and r.status_code == 200:
            z = zipfile.ZipFile(io.BytesIO(r.content)); d = pd.read_csv(z.open(z.namelist()[0]))
            parts.append(pd.DataFrame({"ts": d.calc_time, "rate": d.last_funding_rate}))
        m = (m.replace(day=28) + dt.timedelta(days=4)).replace(day=1)
    return pd.concat(parts) if parts else None
def bybit(c):
    rows, cur = [], E
    while cur > S:
        r = get("https://api.bybit.com/v5/market/funding/history", params=dict(category="linear", symbol=c + "USDT", startTime=S, endTime=cur, limit=200))
        l = r.json()["result"]["list"] if r is not None and r.status_code == 200 else []
        if not l: break
        rows += [(int(x["fundingRateTimestamp"]), float(x["fundingRate"])) for x in l]
        cur = min(int(x["fundingRateTimestamp"]) for x in l) - 1; time.sleep(0.1)
    return pd.DataFrame(rows, columns=["ts", "rate"]) if rows else None
def okx(c):
    rows, cur = [], E
    while cur > S:
        r = get("https://www.okx.com/api/v5/public/funding-rate-history", params=dict(instId=f"{c}-USDT-SWAP", after=cur, limit=100))
        l = r.json().get("data", []) if r is not None and r.status_code == 200 else []
        if not l: break
        rows += [(int(x["fundingTime"]), float(x["realizedRate"])) for x in l]
        cur = min(int(x["fundingTime"]) for x in l); time.sleep(0.15)
    return pd.DataFrame(rows, columns=["ts", "rate"]) if rows else None
def hyper(c):
    rows, cur = [], S
    while cur < E:
        r = get("https://api.hyperliquid.xyz/info", method="POST", json=dict(type="fundingHistory", coin=c, startTime=cur, endTime=E))
        l = r.json() if r is not None and r.status_code == 200 else []
        if not l: break
        rows += [(int(x["time"]), float(x["fundingRate"]), float(x["premium"])) for x in l]
        cur = max(int(x["time"]) for x in l) + 1; time.sleep(0.2)
        if len(l) < 500: break
    return pd.DataFrame(rows, columns=["ts", "rate", "premium"]) if rows else None
def job(a):
    v, c = a
    try:
        d = dict(binance=binance, bybit=bybit, okx=okx, hyper=hyper)[v](c)
    except Exception as ex:
        return f"{v} {c} ERROR {ex!r}"
    if d is None or not len(d): return f"{v} {c} none"
    d = d[(d.ts >= S) & (d.ts < E)].drop_duplicates("ts").sort_values("ts")
    d.to_parquet(f"data/fund_{v}_{c}.parquet", index=False)
    return f"{v} {c} {len(d)} {pd.to_datetime(d.ts.min(), unit='ms'):%Y-%m-%d}..{pd.to_datetime(d.ts.max(), unit='ms'):%Y-%m-%d}"
with ThreadPoolExecutor(4) as ex:   # one thread per venue-ish load; gentle on each API
    for v in (sys.argv[1:] or ["binance", "bybit"]):
        for out in ex.map(job, [(v, c) for c in COINS]): print(out, flush=True)
