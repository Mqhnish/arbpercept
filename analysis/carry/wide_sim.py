"""Rotating cash-and-carry on Bybit: long spot + short perp in the coins whose funding has been highest.
Daily decisions from data up to the previous day. P&L = funding + change in the spot-perp gap - costs."""
import os, pathlib
os.makedirs(pathlib.Path(__file__).resolve().parents[2] / "data" / "carry" / "data", exist_ok=True)
os.makedirs(pathlib.Path(__file__).resolve().parents[2] / "data" / "carry" / "wide", exist_ok=True)
os.chdir(pathlib.Path(__file__).resolve().parents[2] / "data" / "carry")  # downloads live here (not in git)
import glob, itertools, os, sys, numpy as np, pandas as pd
SPLIT = pd.Timestamp("2025-07-01")
def load():
    F, PS, PP, TP, TS = {}, {}, {}, {}, {}
    for p in glob.glob("wide/fund_*.parquet"):
        s = os.path.basename(p)[5:-8]
        f = pd.read_parquet(p); f["day"] = pd.to_datetime(f.ts, unit="ms").dt.floor("D")
        x = pd.read_parquet(f"wide/px_{s}.parquet"); x.index = pd.to_datetime(x.ts, unit="ms")
        F[s] = f.groupby("day").rate.sum(); PS[s], PP[s], TP[s], TS[s] = x.close_spot, x.close_perp, x.turnover_perp, x.turnover_spot
    D = lambda d: pd.DataFrame(d).sort_index()
    return D(F), D(PS), D(PP), D(TP), D(TS)
F, PS, PP, TP, TS = load()
idx = PP.index; F = F.reindex(idx)
basis = (PS.pct_change(fill_method=None) - PP.pct_change(fill_method=None))      # daily gain of long spot / short perp, per notional
day_pnl = (F.fillna(0) + basis).to_numpy()
ok_liq = ((TP.rolling(30).median().shift(1) >= 20e6) & (TS.rolling(30).median().shift(1) >= 2e6)).to_numpy()
perp_ret = PP.pct_change(fill_method=None).to_numpy()
valid = (PP.notna() & PS.notna() & F.notna()).to_numpy()
def sim(k, enter, exit_, N, side_cost, cap_mult=1.5, detail=False):
    sig = (F.rolling(k, min_periods=k).mean().shift(1) * 365).to_numpy()
    T, M = sig.shape; held = np.zeros(M, bool); since = np.zeros(M); out = np.zeros(T); nheld = np.zeros(T); trades = 0; rebal = 0; worst = 0.0
    for t in range(T):
        s = sig[t]
        drop = held & (~(s >= exit_) | ~valid[t])
        trades += drop.sum(); out[t] -= drop.sum() * side_cost; held &= ~drop; since[drop] = 0
        free = N - held.sum()
        if free > 0:
            cand = np.where(~held & ok_liq[t] & valid[t] & (s > enter))[0]
            for j in cand[np.argsort(-s[cand])][:free]:
                held[j] = True; out[t] -= side_cost
        g = np.where(held, np.nan_to_num(day_pnl[t]), 0.0); out[t] += g.sum(); nheld[t] = held.sum()
        r = np.where(held, np.nan_to_num(perp_ret[t]), 0.0); worst = max(worst, r.max(initial=0.0))
        since = np.where(held, (1 + since) * (1 + r) - 1, 0.0)
        hit = held & (since > 0.30); rebal += hit.sum(); since[hit] = 0    # short perp up 30% since entry: margin must be topped up from spot
    ret = pd.Series(out / N / cap_mult, idx)       # return on total capital, N equal slots
    return (ret, pd.Series(nheld, idx), trades, rebal, worst) if detail else ret
def apr(r): return 100 * r.sum() / (len(r) / 365)
if __name__ == "__main__":
    print("symbols", F.shape[1], "days", len(idx), idx[0].date(), idx[-1].date())
    for label, cost in (("fees only (15.5 bps a side)", 15.5e-4), ("fees + 10 bps slippage a side", 25.5e-4)):
        best = None
        for k, en, ex, N in itertools.product([3, 7, 14, 30], [0.15, 0.25, 0.40, 0.60], [0.0, 0.10, 0.20], [5, 10, 20]):
            if ex >= en: continue
            a = apr(sim(k, en, ex, N, cost)[:SPLIT])
            if best is None or a > best[0]: best = (a, k, en, ex, N)
        a, k, en, ex, N = best
        ret, nh, trades, rebal, worst = sim(k, en, ex, N, cost, detail=True)
        te = ret[SPLIT:]; rng = np.random.default_rng(0)
        wk = te.groupby(np.arange(len(te)) // 7).sum().to_numpy()
        bs = [rng.choice(wk, len(wk)).sum() / (len(te) / 365) * 100 for _ in range(4000)]
        eq = (1 + te).cumprod(); dd = (eq / eq.cummax() - 1).min() * 100
        print(f"\n{label}: k={k}d enter>{en:.0%} exit<{ex:.0%} slots={N}")
        print(f"  train APR {a:.1f}%   test APR {apr(te):.1f}%  95% [{np.percentile(bs,2.5):.1f}, {np.percentile(bs,97.5):.1f}]")
        print(f"  test: slots filled {100*nh[SPLIT:].mean()/N:.0f}%  worst drawdown {dd:.1f}%  worst day {100*te.min():.2f}%  best day {100*te.max():.2f}%")
        print(f"  whole run: {trades} round trips, {rebal} margin top-ups, largest one-day rise in a shorted perp {100*worst:.0f}%")
        for y in ("2024", "2025", "2026"): print(f"  {y}: {apr(ret[y]):.1f}% a year")
        ret.to_frame("ret").to_parquet(f"wide_ret_{int(cost*1e5)}.parquet")
