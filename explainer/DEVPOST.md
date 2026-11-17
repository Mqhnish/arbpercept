# SLAY HACKS 2026: submission text (draft)

**Project name:** Why did it trade?

**Tagline:** An AI that explains an automated trader's decisions and is not allowed to make up a number.

## Inspiration

Our trading research system logs thousands of decisions a day in terse codes. We could not read them, and a
language model that explains them but invents a figure is worse than silence.

## What it does

It reads the trader's decision log and explains each decision in two or three plain sentences: what the system
saw, what it did, and the one reason that decided it. Every number in an explanation is checked against the log
before it is shown. If Claude quotes a number that is not in the log, or says a skipped trade was sent, the answer
goes back with the problem named, and after two failed tries a template built from the log is shown instead. Each
card says which writer produced it and shows the original log line.

## How we built it

Python. `facts.py` turns a log line into a dictionary of checked facts. `explain.py` calls Claude through the
Anthropic SDK with only those facts. `verify.py` extracts every number and the direction of the decision from the
answer and compares them with the facts. The demo runs on 1,754 real decisions from replaying a recorded day
(19 Oct 2026, Bitcoin on Binance and Bybit) through our paper trader. 16 tests cover the checker and the retry
loop.

## Challenges

Deciding what "faithful" means for a sentence. We settled on two checks that can be automated: every number is in
the facts (rounding allowed), and the action is not reversed. The checker cannot judge whether the reasoning is
good, and we say so.

## What we learned

On this day the fast model sent no trades at all: at 1 basis point per leg, gaps of 0.8 to 1.2 bps do not cover
two legs of fees. The plain-English explanations make that obvious in a way the log codes did not.

## Honest limits

No API key was available while building, so the live Claude path has only been tested against a stand-in client.
The paper trader and recordings come from our earlier Perceptron project; the explainer is new work for this
hackathon.

## Built with

Python, Anthropic Claude API, pytest

## Try it

Code: github.com/Mqhnish/arbpercept (folder `explainer/`); run `python -m explainer.cli explainer/sample/decisions_btc_2026-10-19.jsonl`.
