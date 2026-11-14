import os, pathlib
os.makedirs(pathlib.Path(__file__).resolve().parents[2] / "data" / "carry" / "data", exist_ok=True)
os.makedirs(pathlib.Path(__file__).resolve().parents[2] / "data" / "carry" / "wide", exist_ok=True)
os.chdir(pathlib.Path(__file__).resolve().parents[2] / "data" / "carry")  # downloads live here (not in git)
import time, os, datetime as dt, pandas as pd, requests
COINS = "BTC ETH SOL XRP DOGE ADA AVAX LINK LTC BCH DOT NEAR APT ARB OP SUI TIA WLD AAVE UNI".split()
E = int(dt.datetime(2026, 10, 1, tzinfo=dt.timezone.utc).timestamp() * 1000)
S = int(dt.datetime(2024, 4, 1, tzinfo=dt.timezone.utc).timestamp() * 1000)
for c in COINS:
    p = f"data/fund_hyper_{c}.parquet"
    old = pd.read_parquet(p) if os.path.exists(p) else pd.DataFrame(columns=["ts", "rate", "premium"])
    rows, cur, fails = [], (int(old.ts.max()) + 1 if len(old) else S), 0
    while cur < E and fails < 8:
        try:
            r = requests.post("https://api.hyperliquid.xyz/info", json=dict(type="fundingHistory", coin=c, startTime=cur, endTime=E), timeout=30)
        except requests.RequestException:
            fails += 1; time.sleep(3); continue
        if r.status_code != 200:
            fails += 1; time.sleep(5 * fails); continue
        l = r.json(); fails = 0
        if not l: break
        rows += [(int(x["time"]), float(x["fundingRate"]), float(x["premium"])) for x in l]
        cur = max(int(x["time"]) for x in l) + 1; time.sleep(0.6)
    d = pd.concat([old, pd.DataFrame(rows, columns=["ts", "rate", "premium"])]).drop_duplicates("ts").sort_values("ts")
    d = d[d.ts < E]; d.to_parquet(p, index=False)
    print(c, len(d), pd.to_datetime(d.ts.max(), unit="ms"), "fails", fails, flush=True)
