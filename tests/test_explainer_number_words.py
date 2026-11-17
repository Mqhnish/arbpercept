"""Word numbers and magnitude suffixes must face the same fact check as digits."""

import pytest

from explainer.explain import explain, template_explanation
from explainer.facts import ACTIONS, build_facts
from explainer.verify import check, quoted_numbers, unsupported_numbers


@pytest.mark.parametrize("phrase, value", [
    ("two point zero", 2.0), ("ten", 10), ("a third", 1 / 3),
    ("negative zero point five two", -0.52), ("minus ten", -10),
    ("twenty-three", 23), ("one hundred and twenty", 120),
    ("one thousand two hundred", 1200), ("two thirds", 2 / 3),
    ("one and a half", 1.5), ("a quarter", 0.25),
    ("1.2k", 1200), ("$1.2K", 1200), ("1.2 million", 1200000),
    ("1.2M", 1200000), ("1.2bn", 1200000000), ("1.2e3", 1200),
    ("1/3", 1 / 3),
])
def test_extracts_complete_number_expressions(phrase, value):
    numbers = quoted_numbers(f"The amount was {phrase} bps.")
    assert len(numbers) == 1
    assert numbers[0][0] == phrase
    assert numbers[0][1] == pytest.approx(value)


@pytest.mark.parametrize("phrase", ["ten", "three point zero", "a third", "two thirds",
                                     "1.2k", "$1.2K", "1.2 million", "1.2e3", "1/3"])
def test_invented_numbers_cannot_hide_in_words_or_suffixes(phrase):
    assert unsupported_numbers(f"It skipped because the amount was {phrase} bps.", {"gap": 1.2}) == [phrase]


@pytest.mark.parametrize("phrase, facts", [
    ("two point zero", {"fees": 2}), ("negative zero point five two", {"ev": -0.52}),
    ("a third", {"fraction": 1 / 3}), ("1/3", {"fraction": 1 / 3}),
    ("1.2k", {"size": 1234}), ("one thousand two hundred", {"size": 1200}),
])
def test_supported_word_numbers_and_scaled_rounding_pass(phrase, facts):
    assert unsupported_numbers(phrase, facts) == []


def test_fraction_is_not_rounded_as_an_integer():
    assert unsupported_numbers("a third", {"ev": 0.52}) == ["a third"]
    assert unsupported_numbers("two thirds", {"ev": 0.52}) == ["two thirds"]


def test_words_have_boundaries_and_do_not_consume_prose():
    assert quoted_numbers("Someone monitored the books at once.") == []
    assert [n[1] for n in quoted_numbers("Two legs and one order.")] == [2, 1]
    assert [n[1] for n in quoted_numbers("ten bps and twenty bps")] == [10, 20]


def test_failure_reaches_the_retry_loop():
    facts = build_facts({"t": 1792444361261301, "direction": "sell binance / buy bybit",
                         "edge_bps": 1.45, "edge_rel_bps": 0.91, "policy": "prior",
                         "action": "SKIP_EV", "reason": "prior expected value -0.52 bps"})

    class Writer:
        name = "stand-in"

        def __init__(self):
            self.feedback = []

        def __call__(self, facts, feedback=None):
            self.feedback.append(feedback)
            return "It skipped because fees were ninety-nine bps." if feedback is None else template_explanation(facts)

    writer = Writer()
    result = explain(facts, writer)
    assert result.tries == 2
    assert "ninety-nine" in writer.feedback[1]


@pytest.mark.parametrize("policy", ["naive", "prior", "slow"])
@pytest.mark.parametrize("action, reason", list(zip(ACTIONS, [
    "gap 0.91 bps", "prior expected value -0.52 bps", "only $82 shown on both books",
    "binance book last updated 11.7 s ago", "position would reach $59,866 (cap $50,000)",
])))
def test_existing_templates_remain_verified(policy, action, reason):
    facts = build_facts({"t": 1792444361261301, "direction": "sell binance / buy bybit",
                         "edge_bps": 1.45, "edge_rel_bps": 0.91, "policy": policy,
                         "action": action, "reason": reason})
    assert check(template_explanation(facts), facts)["ok"]


@pytest.mark.parametrize("phrase", ["one point ten", "1/0", "1e999", "1e999999999"])
def test_malformed_or_unbounded_expressions_fail_closed(phrase):
    assert unsupported_numbers(phrase, {"gap": 1.2}) == [phrase]


def test_policy_counts_are_grounded_in_this_facts_dictionary():
    assert unsupported_numbers("six features", {"policy_name": "a six-feature model"}) == []
    assert unsupported_numbers("six features", {"policy_name": "naive policy"}) == ["six"]


def test_expected_value_sign_boundary_does_not_allow_unrelated_zero_claims():
    assert unsupported_numbers("below zero", {"model_ev_bps": -0.52}) == []
    assert unsupported_numbers("zero dollars", {"size": 82}) == ["zero"]


@pytest.mark.parametrize("text", ["1.2kbps", "$1.2kUSD", "1.2Mbps"])
def test_attached_units_do_not_hide_magnitude(text):
    raw = "$1.2k" if text.startswith("$") else text[:4]
    assert unsupported_numbers(text, {"gap": 1.2}) == [raw]
