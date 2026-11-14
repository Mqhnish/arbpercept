"""Every Bybit USDT perpetual that also has a Bybit spot pair: funding history and daily closes of both."""
import os, pathlib
os.makedirs(pathlib.Path(__file__).resolve().parents[2] / "data" / "carry" / "data", exist_ok=True)
os.makedirs(pathlib.Path(__file__).resolve().parents[2] / "data" / "carry" / "wide", exist_ok=True)
os.chdir(pathlib.Path(__file__).resolve().parents[2] / "data" / "carry")  # downloads live here (not in git)
import time, datetime as dt, pandas as pd, requests
from concurrent.futures import ThreadPoolExecutor
S = int(dt.datetime(2024, 4, 1, tzinfo=dt.timezone.utc).timestamp() * 1000)
E = int(dt.datetime(2026, 10, 1, tzinfo=dt.timezone.utc).timestamp() * 1000)
B = "https://api.bybit.com/v5/market/"
def get(path, **p):
    for i in range(6):
        try:
            r = requests.get(B + path, params=p, timeout=30)
            if r.status_code == 200 and r.json().get("retCode") == 0: return r.json()["result"]
        except requests.RequestException: pass
        time.sleep(1 + 2 * i)
    return None
def instruments(cat):
    out, cur = [], ""
    while True:
        r = get("instruments-info", category=cat, limit=1000, cursor=cur)
        out += r["list"]; cur = r.get("nextPageCursor", "")
        if not cur: return out
perp = [x for x in instruments("linear") if x["quoteCoin"] == "USDT" and x["contractType"] == "LinearPerpetual"]
spot = {x["symbol"] for x in instruments("spot") if x["quoteCoin"] == "USDT"}
syms = sorted(x["symbol"] for x in perp if x["symbol"] in spot)
print(len(perp), "perps,", len(syms), "with spot", flush=True)
def klines(cat, s):
    r = get("kline", category=cat, symbol=s, interval="D", start=S, end=E - 1, limit=1000)
    if not r or not r["list"]: return None
    return pd.DataFrame([(int(x[0]), float(x[4]), float(x[6])) for x in r["list"]], columns=["ts", "close", "turnover"]).sort_values("ts")
def job(s):
    rows, cur = [], E
    while cur > S:
        r = get("funding/history", category="linear", symbol=s, startTime=S, endTime=cur, limit=200)
        l = r["list"] if r else []
        if not l: break
        rows += [(int(x["fundingRateTimestamp"]), float(x["fundingRate"])) for x in l]
        cur = min(int(x["fundingRateTimestamp"]) for x in l) - 1; time.sleep(0.05)
    kp, ks = klines("linear", s), klines("spot", s)
    if not rows or kp is None or ks is None: return f"{s} missing"
    pd.DataFrame(rows, columns=["ts", "rate"]).drop_duplicates("ts").sort_values("ts").to_parquet(f"wide/fund_{s}.parquet", index=False)
    kp.merge(ks, on="ts", suffixes=("_perp", "_spot")).to_parquet(f"wide/px_{s}.parquet", index=False)
    return f"{s} {len(rows)}"
with ThreadPoolExecutor(4) as ex:
    for i, o in enumerate(ex.map(job, syms)):
        if i % 25 == 0 or "missing" in o: print(i, o, flush=True)
