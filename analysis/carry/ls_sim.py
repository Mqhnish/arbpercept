"""Market-neutral long/short baskets of Bybit perps, rebalanced weekly, fixed textbook parameters (nothing tuned).
Return per day on capital = gross notional (half long, half short). Costs per unit traded: 5.5 bps fee + 5 bps slippage."""
import os, pathlib
os.makedirs(pathlib.Path(__file__).resolve().parents[2] / "data" / "carry" / "data", exist_ok=True)
os.makedirs(pathlib.Path(__file__).resolve().parents[2] / "data" / "carry" / "wide", exist_ok=True)
os.chdir(pathlib.Path(__file__).resolve().parents[2] / "data" / "carry")  # downloads live here (not in git)
import numpy as np, pandas as pd
from wide_sim import F, PP, TP, SPLIT, idx
R = PP.pct_change(fill_method=None)
liq = (TP.rolling(30).median().shift(1) >= 20e6) & PP.shift(30).notna()
COST = 10.5e-4
def backtest(signal, q=0.2, every=7, long_only_btc=False):
    w = pd.DataFrame(0.0, idx, PP.columns); cur = pd.Series(0.0, PP.columns)
    for i, t in enumerate(idx):
        if i % every == 0:
            s = signal.loc[t][liq.loc[t]].dropna()
            cur = pd.Series(0.0, PP.columns)
            if len(s) >= 20:
                n = max(int(len(s) * q), 3); o = s.sort_values()
                cur[o.index[-n:]] = 0.5 / n; cur[o.index[:n]] = -0.5 / n
        w.loc[t] = cur
    gross = (w * (R.fillna(0) - F.fillna(0))).sum(axis=1)       # a long pays funding, a short receives it
    turn = w.diff().abs().sum(axis=1).fillna(0)
    return gross - turn * COST, gross, turn
def report(name, net, gross):
    rng = np.random.default_rng(0); row = dict(strategy=name)
    for lab, r in (("train", net[:SPLIT]), ("test", net[SPLIT:])):
        row[f"{lab}_apr_%"] = 100 * r.mean() * 365; row[f"{lab}_sharpe"] = r.mean() / r.std() * np.sqrt(365)
    te = net[SPLIT:]; wk = te.groupby(np.arange(len(te)) // 7).sum().to_numpy()
    bs = [rng.choice(wk, len(wk)).mean() / 7 * 365 * 100 for _ in range(4000)]
    row["test_95%"] = f"[{np.percentile(bs,2.5):.0f}, {np.percentile(bs,97.5):.0f}]"
    eq = (1 + net).cumprod(); row["max_drawdown_%"] = 100 * (eq / eq.cummax() - 1).min()
    row["gross_apr_%"] = 100 * gross.mean() * 365
    return row
sh = lambda x: x.shift(1)
rows = []
for name, sig in (("carry: long low funding, short high (7d)", -sh(F.rolling(7).mean())),
                  ("momentum: long 28d winners, short losers", sh(PP.pct_change(28, fill_method=None))),
                  ("reversal: long 7d losers, short winners", -sh(PP.pct_change(7, fill_method=None))),
                  ("low volatility: long calm, short wild (28d)", -sh(R.rolling(28).std()))):
    net, gross, _ = backtest(sig); rows.append(report(name, net, gross))
# trend on BTC alone: long the perp when yesterday's close is above its 50-day average, otherwise flat
b = PP["BTCUSDT"]; pos = (b > b.rolling(50).mean()).shift(1).astype("boolean").fillna(False).astype(float)
net = pos * (R["BTCUSDT"] - F["BTCUSDT"].fillna(0)) - pos.diff().abs().fillna(0) * COST
rows.append(report("BTC trend: long above 50d average, else flat", net, net))
hold = R["BTCUSDT"].fillna(0); rows.append(report("(reference) hold BTC spot", hold, hold))
pd.set_option("display.width", 250); print(pd.DataFrame(rows).round(2).to_string(index=False))
