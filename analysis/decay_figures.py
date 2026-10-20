"""Figures for the decay pilot (development data only; the holdout stays locked).

1. fig_survival.png: share of fresh-quote births still alive t ms after birth, per hurdle.
   The band is what 100 ms sampling allows: its bottom edge counts only episodes surely
   alive (lower bound >= t), its top edge those possibly alive (upper bound > t).
2. fig_models.png: walk-forward AUC at a 500 ms budget on fresh-quote births, per model.

Each figure has a CSV with the plotted numbers next to it (the table view).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
import decay_pilot as D  # noqa: E402
from arbdata.config import load_config  # noqa: E402
from arbdata.dataset import load_episodes  # noqa: E402
from arbdata.splits import walk_forward_folds  # noqa: E402

SURFACE, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
SERIES = ["#2a78d6", "#eb6834", "#1baf7a"]  # reference palette slots 1-3 (validated all-pairs)
PAIR = "bybit_btc_basis"


def style(ax):
    ax.set_facecolor(SURFACE)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(GRID)
    ax.tick_params(colors=INK2, labelsize=9.5, length=0)
    ax.grid(True, color=GRID, linewidth=1, linestyle="-")
    ax.set_axisbelow(True)


def survival_figure(dev: pd.DataFrame, out: Path) -> None:
    fresh = dev[~dev.stale_partner]
    taus = np.unique(np.round(np.logspace(np.log10(100), np.log10(20_000), 60)))
    rows = []
    fig, ax = plt.subplots(figsize=(7.2, 4.2), dpi=200)
    fig.patch.set_facecolor(SURFACE)
    style(ax)
    for color, hurdle, label in zip(SERIES, ("gross>1bps", "gross>2bps", "gross>5bps"), ("1 bps", "2 bps", "5 bps")):
        g = fresh[fresh.hurdle_name == hurdle]
        lo = np.array([(g.lower_ms >= t).mean() for t in taus])
        hi = np.array([(g.upper_ms > t).mean() for t in taus])
        mid = (lo + hi) / 2
        ax.fill_between(taus, lo * 100, hi * 100, color=color, alpha=0.18, linewidth=0)
        ax.plot(taus, mid * 100, color=color, linewidth=2, solid_capstyle="round", label=f"> {label} (n={len(g):,})")
        # Direct label where the curves are well apart (they converge near zero at the right edge).
        at = int(np.argmin(np.abs(taus - 215)))
        ax.annotate(f"> {label}", xy=(taus[at], mid[at] * 100), xytext=(4, 7), textcoords="offset points",
                    va="bottom", fontsize=9.5, color=INK)
        rows += [{"hurdle": hurdle, "t_ms": t, "surely_alive": a, "possibly_alive": b, "n": len(g)}
                 for t, a, b in zip(taus, lo, hi)]
    ax.set_xscale("log")
    ax.set_xlim(100, 20_000)
    ax.set_ylim(0, 100)
    ax.set_xticks([100, 250, 500, 1000, 2000, 5000, 10000, 20000])
    ax.set_xticklabels(["100", "250", "500", "1K", "2K", "5K", "10K", "20K"])
    ax.set_xlabel("Time since the opportunity appeared (ms, log scale)", color=INK2, fontsize=10)
    ax.set_ylabel("Still open (%)", color=INK2, fontsize=10)
    ax.set_title("Most basis dislocations close within half a second", loc="left", color=INK, fontsize=12.5, pad=24)
    ax.text(0, 1.03, "Bybit BTC spot vs perpetual, fresh quotes on both legs, 32 development days. "
            "Bands show 100 ms sampling uncertainty.", transform=ax.transAxes, fontsize=8.5, color=INK2)
    ax.legend(frameon=False, fontsize=9, loc="upper right", labelcolor=INK)
    fig.subplots_adjust(right=0.88)
    fig.savefig(out / "fig_survival.png", facecolor=SURFACE, bbox_inches="tight")
    pd.DataFrame(rows).to_csv(out / "fig_survival.csv", index=False)
    plt.close(fig)


def model_figure(dev: pd.DataFrame, folds: list[dict], out: Path) -> None:
    df = dev[(dev.hurdle_name == "gross>1bps") & ~dev.stale_partner].reset_index(drop=True)
    res = pd.DataFrame(D.evaluate(df, folds, 500))
    order = ["survival rate only (Kaplan-Meier style)", "gap size only (logistic)",
             "all features (logistic)", "all features (gradient boosting)"]
    names = ["Survival rate only", "Gap size only", "All features, linear", "All features, boosted"]
    g = res.groupby("model").auc.agg(["mean", "min", "max"]).reindex(order)
    g.insert(0, "label", names)
    g.to_csv(out / "fig_models.csv")
    fig, ax = plt.subplots(figsize=(7.2, 3.0), dpi=200)
    fig.patch.set_facecolor(SURFACE)
    style(ax)
    ax.grid(axis="y", visible=False)
    y = np.arange(len(g))[::-1]
    for yi, (_, r) in zip(y, g.iterrows()):
        strong = r.label == "All features, boosted"
        ax.hlines(yi, r["min"], r["max"], color=SERIES[0] if strong else INK2, linewidth=2)
        ax.plot(r["mean"], yi, "o", ms=8, color=SERIES[0] if strong else INK2, mec=SURFACE, mew=2)
        ax.annotate(f"{r['mean']:.2f}", xy=(max(r["max"], r["mean"]), yi), xytext=(8, 0), textcoords="offset points",
                    va="center", fontsize=9.5, color=INK, fontweight="bold" if strong else "normal")
    ax.axvline(0.5, color=INK2, linewidth=1, linestyle="-", alpha=0.6)
    ax.text(0.5, y.max() + 0.62, "chance", ha="center", fontsize=8.5, color=INK2)
    ax.set_yticks(y)
    ax.set_yticklabels(g.label, color=INK, fontsize=10)
    ax.set_xlim(0.4, 1.0)
    ax.set_ylim(-0.6, y.max() + 0.9)
    ax.set_xlabel("AUC on later, unseen days (dot = mean, line = range over 4 walk-forward folds)", color=INK2, fontsize=9.5)
    ax.set_title("Gap size alone cannot tell which opportunities will last", loc="left", color=INK, fontsize=12.5, pad=10)
    fig.savefig(out / "fig_models.png", facecolor=SURFACE, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    cfg = load_config()
    out = cfg.reports_dir / "decay"
    out.mkdir(parents=True, exist_ok=True)
    splits = json.loads(cfg.splits_path.read_text())
    dev = load_episodes(split="development", pairs=[PAIR], cfg=cfg)
    folds = walk_forward_folds(sorted(dev.date.unique()), splits["params"]["embargo_days"], splits["params"]["n_folds"])
    survival_figure(dev, out)
    model_figure(dev, folds, out)
    print(f"wrote figures to {out}")


if __name__ == "__main__":
    main()
