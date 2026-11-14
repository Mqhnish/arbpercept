import os, pathlib
os.makedirs(pathlib.Path(__file__).resolve().parents[2] / "data" / "carry" / "data", exist_ok=True)
os.makedirs(pathlib.Path(__file__).resolve().parents[2] / "data" / "carry" / "wide", exist_ok=True)
os.chdir(pathlib.Path(__file__).resolve().parents[2] / "data" / "carry")  # downloads live here (not in git)
"""Funding carry on 20 large coins: thresholds tuned before 2025-07-01, tested after. Funding only (no price gap).
Return is per year on total capital, one equal slot per coin, idle when flat. Retail taker fees."""
import pandas as pd, numpy as np, itertools
COINS = "BTC ETH SOL XRP DOGE ADA AVAX LINK LTC BCH DOT NEAR APT ARB OP SUI TIA WLD AAVE UNI".split()
SPLIT = "2025-07-01"
def daily(v, c):
    p = f"data/fund_{v}_{c}.parquet"
    if not os.path.exists(p): return None
    d = pd.read_parquet(p); d["day"] = pd.to_datetime(d.ts, unit="ms").dt.floor("D")
    return d.groupby("day").rate.sum()
def run(f, k, enter, exit_, cost, both):
    """f: daily funding received by the +1 position (fraction of notional). Signal uses days before t only."""
    s = (f.rolling(k).mean().shift(1) * 365).to_numpy(); fv = f.to_numpy()
    pos = 0; pnl = np.zeros(len(fv)); held = np.zeros(len(fv)); trades = 0
    for t in range(len(fv)):
        if np.isnan(s[t]): continue
        if pos and pos * s[t] < exit_: pos = 0; pnl[t] -= cost / 2; trades += 1
        if not pos and (s[t] > enter or (both and -s[t] > enter)):
            pos = 1 if s[t] > 0 else -1; pnl[t] -= cost / 2
        pnl[t] += pos * fv[t]; held[t] = abs(pos)
    return pd.Series(pnl, f.index), pd.Series(held, f.index), trades
def study(name, series, cost, both, cap_mult):
    """series: {coin: daily f}. cap_mult: capital needed per 1 of notional. Equal slots, idle when flat."""
    grid = list(itertools.product([3, 7, 14, 30], [0.05, 0.10, 0.15, 0.20, 0.30], [0.0, 0.05, 0.10]))
    best = None
    for k, en, exi in grid:
        if exi >= en: continue
        tr = sum(run(f[:SPLIT], k, en, exi, cost, both)[0].sum() for f in series.values())
        if best is None or tr > best[0]: best = (tr, k, en, exi)
    _, k, en, exi = best
    out = {c: run(f, k, en, exi, cost, both) for c, f in series.items()}
    pnl = pd.DataFrame({c: o[0] for c, o in out.items()}).fillna(0); held = pd.DataFrame({c: o[1] for c, o in out.items()}).fillna(0)
    port = pnl.mean(axis=1) / cap_mult          # return on total capital, equal slot per coin
    res = dict(strategy=name, k=k, enter=en, exit=exi)
    for lab, sl in (("train", slice(None, SPLIT)), ("test", slice(SPLIT, None))):
        p, h = port[sl], held[sl]
        yrs = len(p) / 365
        res[f"{lab}_apr_%"] = 100 * p.sum() / yrs
        res[f"{lab}_time_in_%"] = 100 * h.to_numpy().mean()
        dep = (pnl[sl].to_numpy().sum() / max(h.to_numpy().sum(), 1)) * 365 / cap_mult
        res[f"{lab}_apr_when_in_%"] = 100 * dep
    te = port[SPLIT:]; rng = np.random.default_rng(0)
    wk = te.groupby(np.arange(len(te)) // 7).sum().to_numpy()   # weekly blocks
    bs = [rng.choice(wk, len(wk)).sum() / (len(te) / 365) * 100 for _ in range(4000)]
    res["test_ci"] = f"[{np.percentile(bs, 2.5):.1f}, {np.percentile(bs, 97.5):.1f}]"
    res["trades"] = sum(o[2] for o in out.values())
    return res, port
if __name__ == "__main__":
    fb = {c: daily("binance", c) for c in COINS}; fy = {c: daily("bybit", c) for c in COINS}
    R = []
    # spot-perp on one venue: long spot + short perp, receives funding. retail taker: spot 10 bps, perp 5.5 bps, each twice
    R.append(study("bybit spot+short perp", fy, 31e-4, False, 1.5)[0])
    R.append(study("binance spot+short perp", fb, 30e-4, False, 1.5)[0])
    # perp-perp across venues: +1 = short binance, long bybit; four perp taker fills
    R.append(study("binance-bybit perp pair", {c: (fb[c] - fy[c]).dropna() for c in COINS}, 21e-4, True, 1.0)[0])
    fh = {c: daily("hyper", c) for c in COINS}; fh = {c: f for c, f in fh.items() if f is not None and f.index.max() >= pd.Timestamp("2026-09-01")}  # complete downloads only
    if fh:
        R.append(study("hyper-bybit perp pair", {c: (fh[c] - fy[c]).dropna() for c in fh}, 20e-4, True, 1.0)[0])
        R.append(study("spot + short hyper perp", fh, 2 * (10e-4 + 4.5e-4), False, 1.5)[0])
        R.append(study("hyper-binance perp pair", {c: (fh[c] - fb[c]).dropna() for c in fh}, 19e-4, True, 1.0)[0])
    print(pd.DataFrame(R).round(2).T.to_string())
