"""The explainer: facts come from the log, the verifier rejects invented numbers, and a model that keeps
inventing them is replaced by the template."""

from types import SimpleNamespace

import pytest

from explainer.cli import sample
from explainer.explain import MAX_TRIES, ClaudeAPIWriter, explain, template_explanation
from explainer.facts import ACTIONS, build_facts, numbers_in
from explainer.verify import check, style_problems, unsupported_numbers

T = 1792444361261301


def rec(action, reason, policy="prior", edge=1.45, rel=0.91):
    return {"t": T, "direction": "sell binance / buy bybit", "edge_bps": edge, "edge_rel_bps": rel,
            "policy": policy, "action": action, "reason": reason}


CASES = {
    "ENTER": "gap 0.91 bps",
    "SKIP_EV": "prior expected value -0.52 bps",
    "SKIP_THIN": "only $82 shown on both books",
    "SKIP_STALE": "binance book last updated 11.7 s ago",
    "SKIP_INVENTORY": "position would reach $59,866 (cap $50,000)",
}


@pytest.mark.parametrize("action", ACTIONS)
def test_template_passes_its_own_check_for_every_action(action):
    f = build_facts(rec(action, CASES[action]))
    assert check(template_explanation(f), f)["ok"]


def test_reason_numbers_are_parsed():
    assert build_facts(rec("SKIP_EV", CASES["SKIP_EV"]))["model_ev_bps"] == -0.52
    assert build_facts(rec("SKIP_THIN", CASES["SKIP_THIN"]))["shown_usd"] == 82
    f = build_facts(rec("SKIP_STALE", CASES["SKIP_STALE"]))
    assert f["quiet_s"] == 11.7 and f["quiet_venue"] == "binance"
    f = build_facts(rec("SKIP_INVENTORY", CASES["SKIP_INVENTORY"]))
    assert (f["position_usd"], f["cap_usd"]) == (59866, 50000)


def test_gap_after_fees_is_computed_from_the_offset_adjusted_gap():
    f = build_facts(rec("ENTER", CASES["ENTER"]), fee_bps_per_leg=1.0)
    assert f["both_legs_fees_bps"] == 2.0 and f["gap_after_fees_bps"] == pytest.approx(0.91 - 2.0)


def test_verifier_accepts_rounding_and_negatives_and_rejects_new_numbers():
    f = build_facts(rec("SKIP_EV", CASES["SKIP_EV"]))
    assert unsupported_numbers("Expected value was about -0.5 bps, a loss of 0.52 bps.", f) == []
    assert unsupported_numbers("It expected to lose 0.52 bps, around 3.4 bps in a bad case.", f) == ["3.4"]
    assert unsupported_numbers("The gap was 1.45 bps and fees were 2.0 bps.", f) == []


def test_verifier_catches_a_reversed_decision():
    f = build_facts(rec("SKIP_EV", CASES["SKIP_EV"]))
    assert not check("The system sent both orders.", f)["ok"]
    f = build_facts(rec("ENTER", CASES["ENTER"]))
    assert not check("It skipped this gap.", f)["ok"]
    assert check("It sent both orders.", f)["ok"]


def _client(answers):
    """A stand-in for anthropic.Anthropic() that returns the given texts in order."""
    calls = []

    def create(**kw):
        calls.append(kw)
        text = answers[min(len(calls) - 1, len(answers) - 1)]
        return SimpleNamespace(stop_reason="end_turn", content=[SimpleNamespace(type="text", text=text)])

    return SimpleNamespace(beta=SimpleNamespace(messages=SimpleNamespace(create=create))), calls


def test_good_model_answer_is_used_first_try():
    f = build_facts(rec("SKIP_EV", CASES["SKIP_EV"]))
    client, calls = _client(["It skipped because the expected value was -0.52 bps, below zero."])
    e = explain(f, ClaudeAPIWriter(client))
    assert e.source == "claude (API)" and e.verified and e.tries == 1 and len(calls) == 1


def test_invented_number_triggers_a_correction_then_passes():
    f = build_facts(rec("SKIP_EV", CASES["SKIP_EV"]))
    client, calls = _client(["It skipped; the expected value was -0.52 bps against a 7.5 bps target.",
                             "It skipped because the expected value was -0.52 bps."])
    e = explain(f, ClaudeAPIWriter(client))
    assert e.source == "claude (API)" and e.tries == 2 and "7.5" in calls[1]["messages"][0]["content"]


def test_model_that_keeps_inventing_numbers_is_replaced_by_the_template():
    f = build_facts(rec("SKIP_EV", CASES["SKIP_EV"]))
    client, calls = _client(["It skipped; a 9.9 bps cost was the reason."])
    e = explain(f, ClaudeAPIWriter(client))
    assert e.source.startswith("template") and check(e.text, f)["ok"] and len(calls) == MAX_TRIES


def test_refusal_falls_back_to_the_template():
    f = build_facts(rec("ENTER", CASES["ENTER"]))
    refusing = SimpleNamespace(beta=SimpleNamespace(messages=SimpleNamespace(
        create=lambda **kw: SimpleNamespace(stop_reason="refusal", content=[]))))
    assert explain(f, ClaudeAPIWriter(refusing)).source.startswith("template")


def test_no_client_uses_the_template():
    f = build_facts(rec("SKIP_THIN", CASES["SKIP_THIN"]))
    assert explain(f).source == "template"


def test_sample_covers_each_action_and_is_reproducible():
    recs = [rec(a, CASES[a]) | {"t": T + i} for a in ACTIONS for i in range(10)]
    s1, s2 = sample(recs, 2, None), sample(recs, 2, None)
    assert s1 == s2 and {r["action"] for r in s1} == set(ACTIONS) and len(s1) == 10


def test_numbers_in_includes_time_parts():
    f = build_facts(rec("ENTER", CASES["ENTER"]))
    assert 2026.0 in numbers_in(f)


def test_a_writer_that_crashes_falls_back_to_the_template():
    f = build_facts(rec("SKIP_EV", CASES["SKIP_EV"]))

    class Broken:
        name = "local model (Ollama)"

        def __call__(self, facts, feedback=None):
            raise ConnectionError("no server")

    e = explain(f, Broken())
    assert e.source.startswith("template") and check(e.text, f)["ok"] and "ConnectionError" in e.problems[0]


def test_style_check_rejects_markdown_dashes_ellipses_and_long_answers():
    assert style_problems("It **skipped** the trade.") == ["no markdown"]
    assert style_problems("It saw Bitcoin... no, a gap.") == ["no dashes or ellipses"]
    assert style_problems("It skipped \u2014 the books were thin.") == ["no dashes or ellipses"]
    assert style_problems("One. Two. Three. Four. Five.") == ["at most 4 sentences"]
    assert style_problems("It skipped because the gap was 0.52 bps. The books were thin.") == []


def test_openai_compatible_writer_needs_a_key_and_reads_the_reply(monkeypatch):
    import requests

    from explainer.explain import OpenAICompatWriter
    f = build_facts(rec("SKIP_EV", CASES["SKIP_EV"]))
    w = OpenAICompatWriter("https://api.example.com/v1/", "small-model")
    monkeypatch.delenv("LLM_API_KEY", raising=False)
    assert explain(f, w).source.startswith("template")  # no key: falls back instead of crashing

    seen = {}

    def fake_post(url, **kw):
        seen.update(url=url, auth=kw["headers"]["Authorization"], sys=kw["json"]["messages"][0]["role"])
        return SimpleNamespace(raise_for_status=lambda: None, json=lambda: {
            "choices": [{"message": {"content": "It skipped; the expected value was -0.52 bps."}}]})

    monkeypatch.setenv("LLM_API_KEY", "k")
    monkeypatch.setattr(requests, "post", fake_post)
    e = explain(f, w)
    assert e.source == w.name and e.verified and seen["url"] == "https://api.example.com/v1/chat/completions"
    assert seen["auth"] == "Bearer k" and seen["sys"] == "system"
