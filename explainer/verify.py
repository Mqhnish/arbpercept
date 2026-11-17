"""Hold an explanation to the facts: every number it quotes must be one of the facts, and the sentence
must say the right thing about what the system did.

This is the part that makes a language model safe to put in front of a trading log. The model may phrase
things any way it likes, but it may not invent a number or reverse a decision.
"""

from __future__ import annotations

import math
import re

from .facts import numbers_in

# Precision is expressed as decimal places in the expanded value: 1.2k has
# precision -2 (rounding to the nearest hundred). Fractions use tight precision.
SMALL = dict(zip(
    "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen "
    "seventeen eighteen nineteen".split(), range(20)))
TENS = dict(zip("twenty thirty forty fifty sixty seventy eighty ninety".split(), range(20, 100, 10)))
SCALES = {"thousand": 1000, "million": 10**6, "billion": 10**9, "trillion": 10**12}
SUFFIXES = {**SCALES, "k": 1000, "m": 10**6, "b": 10**9, "bn": 10**9, "t": 10**12}
FRACTIONS = {"half": 2, "halves": 2, "third": 3, "thirds": 3, "quarter": 4, "quarters": 4,
             "fourth": 4, "fourths": 4, "fifth": 5, "fifths": 5, "sixth": 6, "sixths": 6,
             "seventh": 7, "sevenths": 7, "eighth": 8, "eighths": 8, "ninth": 9, "ninths": 9,
             "tenth": 10, "tenths": 10}
_NUMBER_WORDS = "|".join([*SMALL, *TENS, "hundred", *SCALES, *FRACTIONS])
# An article is numeric only before a scale or fraction, never in "a trade".
_ARTICLE = r"a(?=\s+(?:hundred|" + "|".join([*SCALES, *FRACTIONS]) + r")\b)"
_ATOM = rf"(?:{_NUMBER_WORDS}|{_ARTICLE})\b"
WORD_NUMBER = rf"(?:negative\s+|minus\s+|positive\s+)?{_ATOM}(?:[\s-]+(?:and\s+)?(?:{_ATOM}|point\b))*"
_DIGITS = r"(?:\d[\d,]*(?:\.\d+)?|\.\d+)"
_SUFFIX = "|".join(sorted(SUFFIXES, key=len, reverse=True))
NUMBER = re.compile(
    rf"(?<![\w.])(?:[-+]?\$?{_DIGITS}(?:\s*/\s*\d+|[eE][-+]?\d+)?"
    rf"(?:\s*(?:{_SUFFIX})(?=\b|(?:bps|usd)\b))?|{WORD_NUMBER})", re.I)


def _integer_words(words: list[str]) -> int:
    total = current = 0
    for word in words:
        if word == "and":
            continue
        if word == "a":
            current += 1
        elif word in SMALL:
            current += SMALL[word]
        elif word in TENS:
            current += TENS[word]
        elif word == "hundred":
            current = (current or 1) * 100
        else:
            total += (current or 1) * SCALES[word]
            current = 0
    return total + current


def _word_value(raw: str) -> tuple[float, int]:
    words = raw.lower().replace("-", " ").split()
    sign = -1 if words[0] in {"negative", "minus"} else 1
    if words[0] in {"negative", "minus", "positive"}:
        words = words[1:]
    if words[-1] in FRACTIONS:
        denominator = FRACTIONS[words.pop()]
        if "and" in words:
            split = words.index("and")
            value = _integer_words(words[:split]) + _integer_words(words[split + 1:]) / denominator
        else:
            value = (_integer_words(words) if words else 1) / denominator
        return sign * value, 12
    if "point" in words:
        split = words.index("point")
        digits = words[split + 1:]
        if not digits or any(w not in SMALL or SMALL[w] > 9 for w in digits):
            raise ValueError("malformed word decimal")
        decimal = "".join(str(SMALL[w]) for w in digits)
        return sign * (_integer_words(words[:split]) + float("0." + decimal)), len(decimal)
    return float(sign * _integer_words(words)), 0


def _digit_value(raw: str) -> tuple[float, int]:
    clean = raw.lower().replace("$", "").replace(",", "")
    suffix = re.search(rf"\s*({_SUFFIX})$", clean)
    scale = SUFFIXES[suffix[1]] if suffix else 1
    if suffix:
        clean = clean[:suffix.start()]
    if "/" in clean:
        numerator, denominator = clean.split("/")
        return float(numerator) / float(denominator) * scale, 12
    mantissa, _, exponent = clean.partition("e")
    exponent = int(exponent or "0")
    decimals = len(mantissa.split(".")[1]) if "." in mantissa else 0
    return float(clean) * scale, decimals - exponent - len(str(scale)) + 1

SAID_TRADED = re.compile(r"\b(sent|placed|entered|traded|submitted|took the trade|went ahead)\b", re.I)
SAID_SKIPPED = re.compile(r"\b(skipp?ed|declined|passed on|did not trade|didn't trade|did not send|did not enter|"
                          r"no trade|stayed out|held back|did not act)\b", re.I)


def quoted_numbers(text: str) -> list[tuple[str, float, int]]:
    """(as written, expanded value, decimal precision), in text order.

    Recognizes English cardinal numbers, word decimals and common fractions,
    digit fractions, scientific notation, and k/m/b/bn/t or named magnitudes.
    This is a bounded grammar, not a general natural-language quantity parser.
    Malformed recognized expressions fail closed rather than losing their scale.
    """
    out = []
    for match in NUMBER.finditer(text):
        raw = match.group(0)
        try:
            value, precision = _digit_value(raw) if re.search(r"\d", raw) else _word_value(raw)
        except (ValueError, KeyError, ZeroDivisionError, OverflowError):
            value, precision = float("nan"), 12
        if not math.isfinite(value) or precision < -308:
            value, precision = float("nan"), 12
        out.append((raw, value, precision))
    return out


def unsupported_numbers(text: str, facts: dict) -> list[str]:
    allowed = numbers_in(facts)
    # "Not positive" in expected-value facts implies the zero sign boundary.
    if "model_ev_bps" in facts:
        allowed.add(0.0)
    # Policy names contain factual counts ("six-feature", "thirty features").
    # Keep those templates valid without globally allowing six or thirty.
    allowed.update(abs(value) for _, value, _ in quoted_numbers(facts.get("policy_name", "")))
    bad = []
    for raw, val, dec in quoted_numbers(text):
        tol = 0.5 * 10 ** (-dec) + 1e-9
        if not any(abs(abs(val) - a) <= tol for a in allowed):
            bad.append(raw)
    return bad


def wrong_action(text: str, facts: dict) -> str | None:
    """A sentence that says the opposite of what the log says."""
    traded = facts["action"] == "ENTER"
    if traded and SAID_SKIPPED.search(text) and not SAID_TRADED.search(text):
        return "the log says the trade was sent, the text says it was skipped"
    if not traded and SAID_TRADED.search(text) and not SAID_SKIPPED.search(text):
        return "the log says the trade was skipped, the text says it was sent"
    return None


MAX_SENTENCES = 4
SENTENCE_END = re.compile(r"(?<!\d)[.!?](?=\s|$)")


def style_problems(text: str) -> list[str]:
    """Things a reader should never see in a finished explanation: markdown, dashes used as asides,
    a visible change of mind ("..."), or a wall of text."""
    out = []
    if "*" in text or "`" in text or text.lstrip().startswith(("#", "-")):
        out.append("no markdown")
    if "\u2014" in text or "\u2013" in text or "..." in text:
        out.append("no dashes or ellipses")
    if len(SENTENCE_END.findall(text)) > MAX_SENTENCES:
        out.append(f"at most {MAX_SENTENCES} sentences")
    return out


def check(text: str, facts: dict) -> dict:
    bad = unsupported_numbers(text, facts)
    wrong = wrong_action(text, facts)
    style = style_problems(text)
    return {"ok": not bad and wrong is None and not style, "unsupported_numbers": bad, "wrong_action": wrong,
            "style": style}
