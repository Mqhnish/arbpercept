"""Hold an explanation to the facts: every number it quotes must be one of the facts, and the sentence
must say the right thing about what the system did.

This is the part that makes a language model safe to put in front of a trading log. The model may phrase
things any way it likes, but it may not invent a number or reverse a decision.
"""

from __future__ import annotations

import re

from .facts import numbers_in

NUMBER = re.compile(r"(?<![\w.])[-+]?\$?\d[\d,]*(?:\.\d+)?")

SAID_TRADED = re.compile(r"\b(sent|placed|entered|traded|submitted|took the trade|went ahead)\b", re.I)
SAID_SKIPPED = re.compile(r"\b(skipp?ed|declined|passed on|did not trade|didn't trade|did not send|did not enter|"
                          r"no trade|stayed out|held back|did not act)\b", re.I)


def quoted_numbers(text: str) -> list[tuple[str, float, int]]:
    """(as written, value, decimals written) for every number in the text."""
    out = []
    for m in NUMBER.finditer(text):
        raw = m.group(0)
        clean = raw.replace("$", "").replace(",", "")
        try:
            val = float(clean)
        except ValueError:
            continue
        dec = len(clean.split(".")[1]) if "." in clean else 0
        out.append((raw, val, dec))
    return out


def unsupported_numbers(text: str, facts: dict) -> list[str]:
    allowed = numbers_in(facts)
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
