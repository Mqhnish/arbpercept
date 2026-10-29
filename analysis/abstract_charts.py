"""Draw the abstract's P&L charts from the v9 and Tardis reports. Usage: python analysis/abstract_charts.py . docs/abstract"""
import re
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

REPO, OUT = Path(sys.argv[1]), Path(sys.argv[2])
OUT.mkdir(parents=True, exist_ok=True)
PNL = REPO / "data/reports/pnl"

INK, INK2, MUTED, GRID, SURF = "#0b0b0b", "#52514e", "#8a8984", "#e6e5e0", "#fcfcfb"
BLUE, ORANGE, LOSS = "#2a78d6", "#eb6834", "#e9b3b3"
GOOD, BAD = "#0a7f0a", "#c03333"
plt.rcParams.update({"font.family": ["Helvetica Neue", "Arial", "DejaVu Sans"], "font.size": 11,
                     "axes.edgecolor": GRID, "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2,
                     "figure.facecolor": SURF, "text.parse_math": False, "axes.facecolor": SURF, "savefig.facecolor": SURF})
NUM = r"([+−-]?[\d,.]+)"
CI = re.compile(rf"{NUM} \[{NUM}, {NUM}\]")


def num(s):
    return float(s.replace("−", "-").replace(",", "").replace("+", ""))


def parse(md: Path):
    """Capped realised rows and paired differences, keyed by (bound, strategy)."""
    vals, diffs = {}, {}
    for line in md.read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 7 and cells[0] in ("optimistic", "conservative") and CI.fullmatch(cells[6]):
            vals.setdefault((cells[0], cells[2]), tuple(map(num, CI.fullmatch(cells[6]).groups())))
        if len(cells) == 4 and cells[0] in ("optimistic", "conservative") and " − " in cells[2] and CI.fullmatch(cells[3]):
            diffs.setdefault((cells[0], cells[2]), tuple(map(num, CI.fullmatch(cells[3]).groups())))
    return vals, diffs


def title(fig, head, sub):
    fig.text(0.03, 0.95, head, fontsize=13.5, fontweight="bold", color=INK, va="top")
    fig.text(0.03, 0.885, sub, fontsize=10.5, color=INK2, va="top", linespacing=1.5)


def clean(ax, grid_axis="y"):
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.grid(axis=grid_axis, color=GRID, lw=0.8)
    ax.set_axisbelow(True)
    ax.tick_params(length=0)


# 1. BTC cumulative realised P&L, optimistic fills, capped
d = pd.read_csv(PNL / "btc_perp_binance_bybit_v9_real/inventory_by_day.csv", parse_dates=["date"])
d = d[(d["mode"] == "optimistic") & (d.cap == "$50k cap")]
days = sorted(d.date.unique())
series = {}
for strat, name in [("latency-aware cascade", "Cascade"), ("fast path + decay prior", "Prior only"), ("gap size only", "Gap size only")]:
    s = d[d.strategy == strat].set_index("date").realised.reindex(days, fill_value=0.0).cumsum()
    series[name] = s
naive_day = d[d.strategy == "naive fast path"].set_index("date").realised.reindex(days, fill_value=0.0).mean()
casc, gap = series["Cascade"].iloc[-1], series["Gap size only"].iloc[-1]
fig = plt.figure(figsize=(7, 3.8), dpi=192)
title(fig, f"On BTC the cascade made ${casc:,.0f} in {len(days)} days, {casc / gap:.1f}× the gap-size rule",
      "Cumulative realised P&L over validation days, optimistic fills, fees 1.7 / 3.0 bps,\n"
      "latency 50 / 8 ms, $50k cap, Jul 2023 – Jan 2024. With conservative fills every gated policy\n"
      f"is near $0 a day; trading every gap loses ${-naive_day:,.0f} a day (not drawn).")
ax = fig.add_axes([0.1, 0.09, 0.66, 0.57])
for name, s in series.items():
    main = name == "Cascade"
    ax.plot(s.index, s.values, color=BLUE if main else ("#b9b8b2" if name == "Prior only" else "#d6d5cf"), lw=2 if main else 1.5,
            zorder=3 if main else 2)
    ax.plot(s.index[-1], s.values[-1], "o", ms=5, color=BLUE if main else "#b9b8b2", zorder=4)
    ax.annotate(f"{name} ${s.values[-1]:,.0f}", (s.index[-1], s.values[-1]), xytext=(8, 0), textcoords="offset points",
                va="center", fontsize=10.5, color=INK if main else INK2, fontweight="bold" if main else "normal",
                annotation_clip=False)
ax.axhline(0, color="#c9c8c2", lw=0.8)
ax.yaxis.set_major_formatter(lambda v, _: f"${v:,.0f}")
ax.xaxis.set_major_locator(mdates.MonthLocator(bymonthday=15))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b ’%y"))
clean(ax)
fig.savefig(OUT / "btc_cumulative_v9.png")
plt.close(fig)

# 2. Nine coins: cascade vs gap-size rule, optimistic fills
coins = ["btc", "eth", "sol", "tia", "wld", "xrp", "arb", "aave", "doge"]
rows = []
for c in coins:
    p = PNL / f"{c}_perp_binance_bybit_v9_real"
    v, df = parse(p / "inventory.md")
    n = int(re.search(r"(\d+) validation days", (p / "inventory.md").read_text()).group(1))
    rows.append(dict(coin=c.upper(), casc=v[("optimistic", "Cascade")], gap=v[("optimistic", "Gap size only")][0],
                     naive=v[("optimistic", "Naive")][0], diff=df[("optimistic", "Cascade − Gap size only")], days=n))
r = pd.DataFrame(rows).sort_values("casc", key=lambda s: s.map(lambda t: t[0]), ascending=True).reset_index(drop=True)
pos = sum(t[1] > 0 for t in r.casc)
beats = sum(t[1] >= 0 and t[0] > 0 for t in r["diff"])  # BTC: +0.3 unrounded
fig = plt.figure(figsize=(7, 4.1), dpi=192)
title(fig, f"The cascade is profitable on {pos} of 9 coins and beats the gap-size rule on {beats}",
      "Realised P&L per validation day, optimistic fills, 95% CI. Square: cascade. Circle: gap-size rule.\n"
      "BTC and ETH May 2023 – Jan 2024; mid-caps Oct – Dec 2023.")
ax = fig.add_axes([0.1, 0.08, 0.52, 0.62])
ax.set_ylim(-0.6, len(r) - 0.4)
for i, row in r.iterrows():
    m, lo, hi = row.casc
    col = BLUE if lo > 0 else "#55544f"
    ax.plot([lo, hi], [i, i], color=col, lw=2, solid_capstyle="round", zorder=2)
    ax.plot(m, i, "s", ms=7, color=col, zorder=4)
    ax.plot(row.gap, i, "o", ms=7, mfc=SURF, mec=INK2, mew=1.4, zorder=3)
    dm, dlo, dhi = row["diff"]
    dcol = GOOD if (dlo >= 0 and dm > 0) else (BAD if dhi < 0 else INK2)
    fig.text(0.66, ax.transData.transform((0, i))[1] / fig.dpi / fig.get_figheight(), (f"{dm:+.0f}" if round(dm) else "0") + f" [{dlo:+.0f}, {dhi:+.0f}]",
             color=dcol, fontweight="bold" if dcol != INK2 else "normal", fontsize=10.5, va="center")
    fig.text(0.97, ax.transData.transform((0, i))[1] / fig.dpi / fig.get_figheight(), str(row.days), color=INK2, fontsize=10.5,
             va="center", ha="right")
ax.set_yticks(range(len(r)), r.coin, fontweight="bold", color=INK)
ax.set_ylim(-0.6, len(r) - 0.4)
ax.axvline(0, color="#c9c8c2", lw=1)
ax.xaxis.set_major_formatter(lambda v, _: f"${v:+.0f}".replace("$+0", "$0").replace("$-", "−$").replace("$+", "+$"))
clean(ax, "x")
fig.text(0.36, 0.72, "Cascade, $ per day", ha="center", color=INK2, fontsize=10.5)
fig.text(0.66, 0.72, "Cascade − gap rule", color=INK2, fontsize=10.5)
fig.text(0.97, 0.72, "Days", color=INK2, fontsize=10.5, ha="right")
fig.savefig(OUT / "coins_v9.png")
plt.close(fig)

# 3. Naive losses
r3 = r.sort_values("naive", ascending=False).reset_index(drop=True)
fig = plt.figure(figsize=(7, 3.1), dpi=192)
title(fig, "Trading every gap loses money on every coin",
      "Naive policy: realised loss per validation day, same replays, fees and latency as above.")
ax = fig.add_axes([0.1, 0.04, 0.78, 0.72])
ax.barh(range(len(r3)), -r3.naive, height=0.62, color=LOSS)
for i, v in enumerate(r3.naive):
    ax.text(-v + 12, i, f"−${-v:,.0f}", va="center", fontsize=10.5, color=INK)
ax.set_yticks(range(len(r3)), r3.coin, fontweight="bold", color=INK)
ax.set_xticks([])
for s in ("top", "right", "bottom"):
    ax.spines[s].set_visible(False)
ax.spines["left"].set_color("#b9b8b2")
ax.tick_params(length=0)
fig.savefig(OUT / "naive_v9.png")
plt.close(fig)

# 4. Tardis tick data, Binance–Bybit, both fill assumptions
trows = []
for c in ["btc", "eth", "sol"]:
    p = PNL / f"tick_{c}_perp_binance_bybit_tardis_real/inventory.md"
    v, _ = parse(p)
    n = int(re.search(r"(\d+) validation days", p.read_text()).group(1))
    trows.append((c.upper(), v[("optimistic", "Cascade")], v[("conservative", "Cascade")], n))
fig = plt.figure(figsize=(7, 3.3), dpi=192)
title(fig, "On tick data the cascade earns even with conservative fills",
      "Tardis.dev ticks, Binance vs Bybit perpetuals, 1st of each month 2020 – 2026. Cascade, realised\n"
      "P&L per validation day with 95% CI; same fees, latency and $50k cap as above.")
ax = fig.add_axes([0.1, 0.1, 0.72, 0.52])
ax.set_ylim(-0.55, 2.55)
for i, (coin, opt, con, n) in enumerate(reversed(trows)):
    for dy, (m, lo, hi), col, mk in ((0.16, opt, BLUE, "s"), (-0.16, con, ORANGE, "D")):
        ax.plot([lo, hi], [i + dy] * 2, color=col, lw=2, solid_capstyle="round")
        ax.plot(m, i + dy, mk, ms=6.5, color=col, mec=SURF, mew=1)
        ax.text(hi + 1, i + dy, f"${m:.0f}", va="center", fontsize=10, color=INK)
    fig.text(0.97, ax.transData.transform((0, i))[1] / fig.dpi / fig.get_figheight(), f"{n} days", color=INK2, fontsize=10.5,
             va="center", ha="right")
ax.set_yticks(range(3), [t[0] for t in reversed(trows)], fontweight="bold", color=INK)
ax.set_ylim(-0.55, 2.55)
ax.set_xlim(left=min(0, min(t[2][1] for t in trows)) - 2)
ax.axvline(0, color="#c9c8c2", lw=1)
ax.xaxis.set_major_formatter(lambda v, _: f"${v:.0f}")
clean(ax, "x")
ax.legend(handles=[plt.Line2D([], [], color=BLUE, marker="s", lw=2, label="Optimistic fills"),
                   plt.Line2D([], [], color=ORANGE, marker="D", lw=2, label="Conservative fills")],
          loc="lower left", bbox_to_anchor=(0.0, 1.0), ncol=2, frameon=False, fontsize=10)
fig.savefig(OUT / "tardis_binance_bybit.png")
plt.close(fig)

print(r.to_string())
print(trows)
