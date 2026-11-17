# Working in this repo (for coding agents)

Public repo: github.com/Mqhnish/arbpercept. Two agents may work here at the same time (Claude Code and Codex), so read the
coordination rules at the bottom before editing.

## What this repo is

Cross-venue crypto arbitrage research from the Optiver Perceptron 2026 hackathon (Binance vs Bybit, latency-aware
decisions). Packages: `arbdata/` (data pipeline and recorder), `arbtrade/` (replay, models, paper trader `live.py`,
dashboard), `analysis/` (reports), `explainer/` (the SLAY HACKS project, below), `tests/`. Run Python with
`.venv/bin/python`. Raw data lives in `data/` and is gitignored except `data/reports/` and `data/splits.json`.
`README.md` has the research results; do not change those numbers.

## Current job: SLAY HACKS 2026 (AI theme)

An online student hackathon on Devpost (slayy-hacks.devpost.com). Project period started 7 Nov 2026; **submission
deadline 7 Dec 2026, 5:00 pm EST**. The entry must be original work with a meaningful use of AI, so the explainer is
new code written inside `explainer/`; the paper trader and the recordings it reads come from the earlier project, and the
submission text says so.

**The project, "Why did it trade?":** it reads the paper trader's decision log (one JSON line per decision) and explains
each decision in plain English, then checks the explanation before showing it.

- `explainer/facts.py`: one log line to a dictionary of facts. Each number is copied from the log or computed with a formula
  stated next to it (`both_legs_fees_bps = 2 x fee`, `gap_after_fees_bps = gap vs offset - both fees`).
- `explainer/verify.py`: every number in an answer must match a fact (rounding allowed, 1 and 2 always allowed); the answer
  must not reverse the decision (skipped described as sent, or the reverse); plain style (no markdown, dashes, ellipses,
  more than 4 sentences).
- `explainer/explain.py`: `template_explanation` (always passes), writers (`ClaudeCLIWriter`, `ClaudeAPIWriter`,
  `OllamaWriter`, `OpenAICompatWriter`), and `explain(facts, writer)`, which retries a failed answer up to three tries with the
  problem named, then falls back to the template.
- `explainer/cli.py`: `--backend template|claude-cli|claude-api|ollama|openai-compat`, `--render report.json` to rebuild the
  page without calling a writer. `explainer/page.py` renders the single-file page `explainer/report.html`.
- Data: `explainer/sample/decisions_btc_2026-10-19.jsonl` (1,754 real decisions from replaying a recorded day through
  `python -m arbtrade.live`, command in `explainer/README.md`).
- `explainer/README.md` and `explainer/DEVPOST.md` (the submission text draft).

**State (18 Nov 2026):** built and pushed; `.venv/bin/python -m pytest -q` gives **187 passed** (19 in
`tests/test_explainer.py`). The committed report was written by Claude through `claude-cli`: 15 of 15 explanations passed the
check on the first try (a small sample from one day). The Ollama, OpenAI-compatible and API writers have been tested only
with stand-ins, never against a real service.

**Environment facts that limit you:**
- There is no Anthropic API key and the owner will not get one. Do not add code paths or docs that require one.
- `claude-cli` uses the owner's Claude login, which you cannot use. You cannot regenerate `report.json` with a real writer;
  you can re-render the page from the existing `report.json` (`--render`).
- Free options for a real writer: `ollama` (local, needs Ollama installed) or `openai-compat` with a free-tier key the owner
  supplies in `LLM_API_KEY`. Never write a key into a file.

## Open tasks (good work for Codex; each is independent, one branch each)

1. **Writer evaluation harness**: `explainer/evaluate.py` that runs any writer over N sampled decisions and prints the
   first-try pass rate, mean tries, template fallbacks and failure reasons, by action. Test it with stand-in writers. Run it
   for real only if a free writer is available; otherwise say that you did not.
2. **Stricter verifier**: handle numbers written as words ("two point zero", "ten", "a third") and units like "1.2k",
   so an invented figure cannot slip past the number check. Add tests that fail first.
3. **Demo script**: `explainer/DEMO_SCRIPT.md`, a 2 to 3 minute storyboard for the submission video (what is on screen, what is
   said, with the claims taken from the README). The owner records it.
4. **Devpost text pass**: tighten `explainer/DEVPOST.md`. Every claim must trace to the repo or a measured result; no
   unmeasured numbers; plain prose without stock AI phrasing.
5. **Page checks**: keyboard and screen-reader pass on `explainer/page.py` (the filter is `role=tablist`; check arrow-key
   behavior, focus rings, contrast in both color schemes).

Claude Code handles anything that needs the owner's Claude login (regenerating `report.json`), repo-wide results, and
submission logistics.

## Rules

- **Never open the holdouts**: main Bybit 10 to 18 Oct 2026 (`ARBDATA_UNLOCK_HOLDOUT`) and cross-venue Feb 2 to Mar 31 2024
  (`ARBDATA_UNLOCK_CROSS_HOLDOUT`). Never set those variables.
- Do not edit `data/`, `README.md` result tables, `docs/abstract/`, or the recorder (`arbdata/recorder.py`), and do not
  start or stop the recorder.
- Do not invent numbers. A figure goes in docs only if a command in this repo produced it; say what produced it.
- No new dependencies without asking. Tests that need a network or a model must use stand-ins.
- Commit messages carry no attribution lines (no Co-Authored-By, no "generated by"). Do not put personal details, keys or
  tokens in any file: the repo is public.
- Before every commit: `.venv/bin/python -m pytest -q` must pass.

## Coordination between agents

- `git pull --rebase origin main` before you start and before you push. Never force-push.
- Codex works on branches named `codex/<topic>` and pushes them; the owner merges. Claude Code commits to `main`.
- Touch only the files your task needs. If two tasks would edit the same file, stop and tell the owner.
- Finish each task with a short note: what changed, the test result, anything you could not verify.
