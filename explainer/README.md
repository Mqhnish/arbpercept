# Why did it trade?

An explainer for an automated trader's decisions. It reads the paper trader's log, says in plain English why each
gap was traded or skipped, and checks every number in the explanation against the log before showing it.

Built for SLAY HACKS 2026 (AI theme). The paper trader it explains, `arbtrade/live.py`, comes from our earlier
Perceptron project; everything in this folder was written during the SLAY HACKS window.

## The problem

A trading system makes thousands of small decisions a day and logs a terse reason for each, such as
`SKIP_EV  prior expected value -0.52 bps`. Nobody reads those. A language model can turn them into sentences,
but a model that writes "the gap was 3.4 bps" when the log says 0.52 is worse than no explanation.

## How it works

1. `facts.py` reads one log line and builds a small dictionary of facts. Each number is either copied from the log
   or computed with a formula written next to it (the gap after both legs' fees).
2. `explain.py` asks Claude for two or three sentences, giving it only that dictionary.
3. `verify.py` extracts every number in the answer and checks it against the facts (with rounding), and checks the
   sentence does not reverse the decision (a skipped trade described as sent).
4. A failed check goes back to Claude with the problem named. After two failed corrections the deterministic
   template is used instead. Each explanation carries its source (`claude` or `template`), so nothing unverified
   looks verified.

## Run it

```bash
.venv/bin/python -m explainer.cli explainer/sample/decisions_btc_2026-10-19.jsonl --per-action 3
ANTHROPIC_API_KEY=... .venv/bin/python -m explainer.cli explainer/sample/decisions_btc_2026-10-19.jsonl --claude
```

Without `--claude` the explanations come from the template and need no key. The report is
`explainer/report.html`, with one card per decision and the original log line under each.

The sample is 1,754 real decisions from replaying our 10 ms recording of 19 Oct 2026 through the paper trader
(BTC, Binance vs Bybit, 1 bps fee per leg, 0.8 bps trigger):

```bash
.venv/bin/python -m arbtrade.live --replay 2026-10-19 --asset BTC --fee 1.0 --trigger 0.8 --offset-window-s 0 \
    --decisions explainer/sample/decisions_btc_2026-10-19.jsonl
```

## What the sample shows

The naive policy sent 258 of 877 triggers and the fast decay prior sent none: it skipped 673 for negative expected
value, 114 because a feed had gone quiet, and 90 because the books showed too little size. The naive policy's other
415 were blocked by the position cap. At 1 bps per leg, a gap of 0.8 to 1.2 bps does not cover two legs of fees, which
is the whole story the explanations tell.

## Tests and limits

`tests/test_explainer.py` covers the fact parsing, the verifier (rounding accepted, invented numbers and reversed
decisions rejected), the retry loop and the template fallback, with a stand-in for the API client.

- The Claude path has been exercised only against that stand-in. No API key was available when this was built, so
  the live call, and how often Claude passes the check on the first try, have not been measured.
- The default model is `claude-opus-5-5`, with low effort and the API's server-side refusal fallback switched on
  (`fallbacks="default"`). Change `DEFAULT_MODEL` or pass `--model` to use another.
- The verifier checks numbers and the direction of the decision. It cannot check that a sentence about the reason is
  well argued, so the facts it is given include a plain-language meaning of each action.
- Decisions come from replay, not live trading. No orders were sent anywhere.
