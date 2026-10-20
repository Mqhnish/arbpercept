"""Chart the walk-forward P&L-vs-latency results from arbtrade.evaluate.

    .venv/bin/python analysis/pnl_figure.py [--pair btc_perp_binance_bybit] [--fee 1.0]

Two panels share one y-axis: the optimistic and conservative fill bounds. The truth lies
between them for the sampled (Bybit) leg. The CSV next to the chart is its table view.
"""

from __future__ import annotations

import argparse

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

from arbdata.config import load_config

SURFACE, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
COLORS = {"naive fast path": "#2a78d6", "fast path + decay prior": "#eb6834",
          "slow model always": "#1baf7a", "latency-aware cascade": "#eda100"}
LABELS = {"naive fast path": "Naive fast path", "fast path + decay prior": "Fast path + decay prior",
          "slow model always": "Slow model always", "latency-aware cascade": "Latency-aware cascade"}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pair", default="btc_perp_binance_bybit")
    ap.add_argument("--fee", type=float, default=1.0)
    ap.add_argument("--tag", default="")
    args = ap.parse_args()
    cfg = load_config()
    d = cfg.reports_dir / "pnl" / f"{args.pair}{args.tag}"
    df = pd.read_csv(d / "pnl_vs_latency.csv")
    df = df[(df.fee_bps_per_leg == args.fee) & df.strategy.isin(COLORS)]
    days = int(df.val_days.max())
    table = df.pivot_table(index=["mode", "tau_ms"], columns="strategy", values="pnl_per_day_usd")
    table.to_csv(d / f"fig_pnl_fee{args.fee:g}.csv")

    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.2), dpi=200, sharey=True)
    fig.patch.set_facecolor(SURFACE)
    lo = min(0, df.pnl_per_day_usd.min()) * 1.1
    hi = max(0, df.pnl_per_day_usd.max()) * 1.15
    for ax, mode in zip(axes, ("optimistic", "conservative")):
        ax.set_facecolor(SURFACE)
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
        for side in ("left", "bottom"):
            ax.spines[side].set_color(GRID)
        ax.tick_params(colors=INK2, labelsize=9, length=0)
        ax.grid(True, color=GRID, linewidth=1)
        ax.set_axisbelow(True)
        ax.axhline(0, color=INK2, linewidth=1)
        for s, c in COLORS.items():
            g = df[(df["mode"] == mode) & (df.strategy == s)].sort_values("tau_ms")
            x = g.tau_ms.to_numpy().astype(float)
            ax.plot(x, g.pnl_per_day_usd, color=c, linewidth=2, marker="o", ms=4.5, mec=SURFACE, mew=1.5,
                    label=LABELS[s], solid_capstyle="round")
        ax.set_xscale("symlog", linthresh=1)
        ax.set_xlim(0, 230)
        ticks = [0, 1, 2, 5, 10, 20, 50, 100, 200]
        ax.set_xticks(ticks)
        ax.set_xticklabels([str(t) for t in ticks])
        ax.set_ylim(lo, hi)
        ax.set_xlabel("One-way order latency (ms)", color=INK2, fontsize=9.5)
        ax.set_title(f"{mode.capitalize()} fill bound", loc="left", color=INK, fontsize=10.5)
    axes[0].set_ylabel("Net P&L per validation day (USD)", color=INK2, fontsize=9.5)
    axes[0].legend(frameon=False, fontsize=8.5, loc="lower left", labelcolor=INK)
    fig.suptitle("Latency decides whether cross-venue arbitrage pays", x=0.07, ha="left", color=INK, fontsize=12.5, y=1.02)
    fig.text(0.07, 0.955, f"Binance vs Bybit BTC perpetual, {days} walk-forward validation days, fees {args.fee:g} bps per leg, "
             "$10k per trade. The slow model also waits its measured inference time.", color=INK2, fontsize=8.5, ha="left")
    fig.savefig(d / f"fig_pnl_fee{args.fee:g}.png", facecolor=SURFACE, bbox_inches="tight")
    print(f"wrote {d / f'fig_pnl_fee{args.fee:g}.png'}")


if __name__ == "__main__":
    main()
