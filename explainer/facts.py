"""Turn one logged trading decision into a small set of checked facts.

Every number an explanation may quote comes from this dictionary, either copied from the log or
computed here with a formula that is stated next to it. The verifier (verify.py) holds any text,
human or model, to that set.

A decision record is one line of the paper trader's --decisions file:
    {"t": µs since epoch, "direction": "sell binance / buy bybit", "edge_bps": 0.91,
     "edge_rel_bps": 0.47, "policy": "prior", "action": "SKIP_EV",
     "reason": "prior expected value -0.52 bps"}
"""

from __future__ import annotations

import datetime as dt
import re

ACTIONS = ("ENTER", "SKIP_EV", "SKIP_THIN", "SKIP_STALE", "SKIP_INVENTORY")

MEANING = {
    "ENTER": "the system sent both orders",
    "SKIP_EV": "the model's expected value after fees and fill risk was not positive, so it skipped",
    "SKIP_THIN": "the order books showed too little size to be worth trading, so it skipped",
    "SKIP_STALE": "one venue's feed had gone quiet, so the quoted gap could not be trusted and it skipped",
    "SKIP_INVENTORY": "the trade would have pushed the net position past its cap, so it skipped",
}

POLICY_NAMES = {
    "naive": "the naive policy (trades every gap)",
    "prior": "the fast decay prior (a six-feature model of whether the gap survives)",
    "slow": "the slow model (gradient boosting on about thirty features)",
}


def _first_number(pattern: str, text: str) -> float | None:
    m = re.search(pattern, text)
    return float(m.group(1).replace(",", "")) if m else None


def parse_reason(action: str, reason: str) -> dict:
    """Pull the numbers the paper trader wrote into its reason string."""
    out: dict[str, float] = {}
    if action == "SKIP_EV":
        v = _first_number(r"expected value ([+-]?\d+(?:\.\d+)?) bps", reason)
        if v is not None:
            out["model_ev_bps"] = v
    elif action == "SKIP_THIN":
        v = _first_number(r"\$([\d,]+(?:\.\d+)?) shown", reason)
        if v is not None:
            out["shown_usd"] = v
    elif action == "SKIP_STALE":
        v = _first_number(r"last updated ([\d.]+) s ago", reason)
        if v is not None:
            out["quiet_s"] = v
        m = re.match(r"(\w+) book", reason)
        if m:
            out["quiet_venue"] = m.group(1)
    elif action == "SKIP_INVENTORY":
        v = _first_number(r"reach \$([\d,]+(?:\.\d+)?)", reason)
        c = _first_number(r"cap \$([\d,]+(?:\.\d+)?)", reason)
        if v is not None:
            out["position_usd"] = v
        if c is not None:
            out["cap_usd"] = c
    elif action == "ENTER":
        v = _first_number(r"gap ([+-]?\d+(?:\.\d+)?) bps", reason)
        if v is not None:
            out["gap_bps"] = v
    return out


def build_facts(rec: dict, fee_bps_per_leg: float = 1.0) -> dict:
    """Facts for one decision record. fee_bps_per_leg is the paper trader's --fee setting."""
    action = rec["action"]
    if action not in ACTIONS:
        raise ValueError(f"unknown action {action!r}")
    when = dt.datetime.fromtimestamp(rec["t"] / 1e6, dt.timezone.utc)
    f: dict = {
        "time_utc": when.strftime("%Y-%m-%d %H:%M:%S"),
        "policy": rec["policy"],
        "policy_name": POLICY_NAMES.get(rec["policy"], rec["policy"]),
        "direction": rec["direction"],
        "action": action,
        "what_it_means": MEANING[action],
        "gap_bps": round(float(rec["edge_bps"]), 2),
        "gap_vs_usual_offset_bps": round(float(rec["edge_rel_bps"]), 2),
        "fee_bps_per_leg": fee_bps_per_leg,
        "both_legs_fees_bps": round(2 * fee_bps_per_leg, 2),  # two taker legs
        "reason_text": rec["reason"],
    }
    # the gap net of both legs' fees, before any fill risk: computed here, not logged
    f["gap_after_fees_bps"] = round(f["gap_vs_usual_offset_bps"] - f["both_legs_fees_bps"], 2)
    f.update(parse_reason(action, rec["reason"]))
    return f


def numbers_in(facts: dict) -> set[float]:
    """Every number a faithful explanation could quote, with its absolute value, plus the date and time
    parts and the small counts 1 and 2 (one fee per leg, two legs)."""
    nums: set[float] = {1.0, 2.0}
    for k, v in facts.items():
        if isinstance(v, bool):
            continue
        if isinstance(v, (int, float)):
            nums.update({float(v), abs(float(v))})
        elif k == "time_utc":
            nums.update(float(x) for x in re.findall(r"\d+", v))
    return nums
