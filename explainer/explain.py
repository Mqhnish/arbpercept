"""Explain a logged decision in plain English, and only with numbers that are in the log.

Two writers share one rule (verify.py): a deterministic template, which needs no API key, and Claude,
which reads better. Claude's text is checked; if it quotes a number that is not in the facts or reverses
the decision, it is asked again with the problem named, and after two failed tries the template is used.
Every explanation carries its source and whether it passed, so nothing unverified looks verified.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field

from .facts import POLICY_NAMES
from .verify import check

DEFAULT_MODEL = "claude-opus-5-5"
MAX_TRIES = 3  # the first answer and two corrections

SYSTEM = """You explain one decision made by an automated arbitrage trader to a student who has not seen the \
code. The trader watches the same coin on two exchanges and sometimes sees a price gap between them. For each \
gap it decides to trade, or to skip, and logs why.

Write two or three plain sentences. Say what the system saw, what it did, and the one reason that decided it. \
Rules:
- Use only numbers that appear in the facts JSON you are given, copied exactly or rounded. Never compute a new \
number, never estimate, never add a number from your own knowledge.
- Say clearly whether the trade was sent or skipped, in the same direction as the facts.
- Do not mention the time of day. Do not give investment advice. Do not call the decision good or bad.
- Quantities in basis points (bps): one bps is 0.01 percent of the trade's value."""


@dataclass
class Explanation:
    text: str
    source: str                      # "claude", "template", or "template (claude failed the check)"
    verified: bool
    tries: int = 0
    problems: list[str] = field(default_factory=list)


def template_explanation(f: dict) -> str:
    """A plain sentence built only from the facts. Always passes the check."""
    sell, buy = f["direction"].replace("sell ", "").split(" / buy ")
    offset = ""
    if abs(f["gap_bps"] - f["gap_vs_usual_offset_bps"]) > 1e-9:
        offset = f" ({f['gap_vs_usual_offset_bps']} bps once the usual offset between the two is removed)"
    head = f"{f['policy_name'].capitalize()} saw {sell} quoting {f['gap_bps']} bps above {buy}{offset}."
    a = f["action"]
    if a == "ENTER":
        tail = (f" It sent both orders. Fees on the two legs come to {f['both_legs_fees_bps']} bps, "
                f"which leaves {f['gap_after_fees_bps']} bps before fill risk.")
    elif a == "SKIP_EV":
        tail = (f" It skipped: the expected value after fees and the chance that only one leg fills was "
                f"{f['model_ev_bps']} bps, not positive.")
    elif a == "SKIP_THIN":
        tail = f" It skipped: the books showed only ${f['shown_usd']:,.0f} on both sides, too little to bother."
    elif a == "SKIP_STALE":
        tail = (f" It skipped: the {f['quiet_venue']} feed had been quiet for {f['quiet_s']} s, so the gap "
                f"could not be trusted.")
    else:
        tail = (f" It skipped: the trade would have taken the position to ${f['position_usd']:,.0f}, past the "
                f"${f['cap_usd']:,.0f} cap.")
    return head + tail


def _ask(client, model: str, facts: dict, feedback: str | None) -> str | None:
    """One call to Claude. Returns the text, or None on a refusal or an empty answer."""
    content = "Facts:\n" + json.dumps({k: v for k, v in facts.items() if k != "reason_text"}, indent=1)
    if feedback:
        content += "\n\nYour previous answer failed a check: " + feedback + "\nWrite it again, fixing that."
    resp = client.beta.messages.create(
        model=model,
        max_tokens=700,
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        output_config={"effort": "low"},
        system=SYSTEM,
        messages=[{"role": "user", "content": content}],
    )
    if resp.stop_reason == "refusal":
        return None
    text = "".join(b.text for b in resp.content if b.type == "text").strip()
    return text or None


def explain(facts: dict, client=None, model: str = DEFAULT_MODEL) -> Explanation:
    """Claude's explanation if it passes the check within MAX_TRIES, otherwise the template."""
    fallback = template_explanation(facts)
    if client is None:
        return Explanation(fallback, "template", True, 0)
    problems: list[str] = []
    feedback = None
    for attempt in range(1, MAX_TRIES + 1):
        text = _ask(client, model, facts, feedback)
        if text is None:
            problems.append("Claude declined or returned nothing")
            break
        result = check(text, facts)
        if result["ok"]:
            return Explanation(text, "claude", True, attempt, problems)
        bits = []
        if result["unsupported_numbers"]:
            bits.append("these numbers are not in the facts: " + ", ".join(result["unsupported_numbers"]))
        if result["wrong_action"]:
            bits.append(result["wrong_action"])
        feedback = "; ".join(bits)
        problems.append(feedback)
    return Explanation(fallback, "template (claude failed the check)", True, len(problems), problems)
