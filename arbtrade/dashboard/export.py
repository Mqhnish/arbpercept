"""Write the dashboard as a static site, for GitHub Pages: every API answer the read-only views can ask
for, computed once from data/reports/ and saved as a JSON file next to the page.

    .venv/bin/python -m arbtrade.dashboard.export site/

The page finds the files through api_file() below and its twin, staticFile() in static/app.js; the
two must name a request the same way. The paper trader needs live feeds, so the static page explains
how to run it locally instead.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
from pathlib import Path

from . import data as D
from .server import IMAGES, STATIC

REPO = Path(__file__).resolve().parents[2]
SITE_IMAGES = ["architecture", "btc_cumulative_v9", "coins_v9", "naive_v9", "tardis_binance_bybit", "decay_auc",
                   "survival", "dashboard_paper"]
MODES, CAPS = ("optimistic", "conservative"), ("capped", "uncapped")


def js_num(x: float) -> str:
    """A number as JavaScript's String() writes it (50.0 -> "50", 2.35 -> "2.35"): the page builds its
    requests from select values that went through JSON."""
    x = float(x)
    return str(int(x)) if x.is_integer() else repr(x)


def api_file(path: str, q: dict[str, str]) -> str:
    """The static file that holds the answer to one GET request."""
    if path == "/api/run":
        return f"api/run/{q['name']}/{q['fee']}_{q['tau']}_{q['mode']}_{q['cap']}.json"
    if path == "/api/coins":
        return f"api/coins/{q['tag']}_{q['mode']}_{q['cap']}.json"
    if path == "/api/note":
        return f"api/note/{q['path']}.json"
    return f"api/{path.removeprefix('/api/')}.json"


def _commit() -> str:
    sha = os.environ.get("GITHUB_SHA")
    if not sha:
        try:
            sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO, capture_output=True, text=True, check=True).stdout
        except (OSError, subprocess.CalledProcessError):
            sha = ""
    return sha.strip()[:7]


def export(reports: Path, out: Path) -> int:
    """Write the site to out (emptied first). Returns the number of API files written."""
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    n = 0

    def put(path: str, q: dict[str, str], obj: object) -> None:
        nonlocal n
        f = out / api_file(path, q)
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(json.dumps(obj, allow_nan=False, separators=(",", ":")), encoding="utf-8")
        n += 1

    runs = D.list_runs(reports)
    put("/api/runs", {}, runs)
    for r in runs:
        for fee in r["fees"]:
            for tau in r["taus"]:
                for mode in MODES:
                    for cap in CAPS:
                        q = {"name": r["name"], "fee": js_num(fee), "tau": js_num(tau), "mode": mode, "cap": cap}
                        put("/api/run", q, D.run_summary(reports, r["name"], fee, tau, mode, cap))
    for tag in sorted({r["tag"] for r in runs}):
        for mode in MODES:
            for cap in CAPS:
                put("/api/coins", {"tag": tag, "mode": mode, "cap": cap}, D.coins(reports, tag, mode, cap))
    put("/api/decay", {}, D.decay(reports))
    notes = D.notes(reports)
    put("/api/notes", {}, notes)
    for note in notes:
        put("/api/note", {"path": note["path"]}, {"path": note["path"], "text": D.read_note(reports, note["path"])})

    for f in STATIC.iterdir():
        if f.suffix in (".css", ".js"):
            shutil.copy(f, out / f.name)
    html = (STATIC / "index.html").read_text(encoding="utf-8")
    html = html.replace('<html lang="en">', f'<html lang="en" data-static="1" data-commit="{_commit()}">', 1)
    (out / "index.html").write_text(html.replace('"/static/', '"'), encoding="utf-8")
    (out / "img").mkdir()
    for name in SITE_IMAGES:
        shutil.copy(IMAGES / f"{name}.png", out / "img" / f"{name}.png")
    shutil.copy(IMAGES / "abstract.md", out / "abstract.md")
    (out / ".nojekyll").write_text("")  # serve files as they are (Jekyll would skip names starting with _)
    return n


def main() -> None:
    ap = argparse.ArgumentParser(description="write the dashboard as a static site")
    ap.add_argument("out", type=Path)
    ap.add_argument("--reports", type=Path, default=REPO / "data" / "reports")
    args = ap.parse_args()
    n = export(args.reports, args.out)
    print(f"{n} API files and the page written to {args.out}")


if __name__ == "__main__":
    main()
