"""Evaluation uses stand-in writers; no model or network is needed."""

import json

import pytest

from explainer.evaluate import evaluate, main


def decision(action="ENTER", i=0):
    return {"t": 1792444361261301 + i, "direction": "sell binance / buy bybit",
            "edge_bps": 1.45, "edge_rel_bps": 0.91, "policy": "naive",
            "action": action, "reason": "gap 0.91 bps" if action == "ENTER"
            else "prior expected value -0.52 bps"}


class Writer:
    name = "stand-in"

    def __init__(self):
        self.calls = []

    def __call__(self, facts, feedback=None):
        self.calls.append((facts["action"], feedback))
        if facts["action"] == "ENTER":
            return "It sent both orders."
        if feedback is None:
            return "It skipped because the cost was 999.9 bps."
        return "It skipped because expected value was -0.52 bps."


def test_evaluation_measures_first_attempt_retries_and_actions():
    writer = Writer()
    result = evaluate([decision(), decision("SKIP_EV")], writer, count=2)
    total = result["overall"]
    assert total == {"decisions": 2, "first_try_passes": 1, "first_try_pass_rate": 0.5,
                     "mean_tries": 1.5, "template_fallbacks": 0,
                     "failure_reasons": {"unsupported_numbers": 1}}
    assert result["by_action"]["ENTER"]["first_try_pass_rate"] == 1.0
    assert result["by_action"]["SKIP_EV"]["mean_tries"] == 2.0
    assert result["by_action"]["SKIP_THIN"]["first_try_pass_rate"] is None
    assert result["by_action"]["SKIP_THIN"]["mean_tries"] is None
    assert any(feedback and "999.9" in feedback for _, feedback in writer.calls)


@pytest.mark.parametrize("mode, tries, reasons", [
    ("invalid", 3, {"unsupported_numbers": 3, "wrong_action": 3, "style: no markdown": 3}),
    ("empty", 1, {"empty_response": 1}),
    ("error", 1, {"writer_error: ConnectionError": 1}),
])
def test_fallbacks_are_failures_even_though_template_passes(mode, tries, reasons):
    class Failing:
        name = "stand-in"

        def __call__(self, facts, feedback=None):
            if mode == "error":
                raise ConnectionError("private service details must not appear in the report")
            return None if mode == "empty" else "It **skipped** because fees were 999.9 bps."

    total = evaluate([decision()], Failing(), count=1)["overall"]
    assert total["first_try_pass_rate"] == 0.0
    assert total["mean_tries"] == tries
    assert total["template_fallbacks"] == 1
    assert total["failure_reasons"] == reasons


def test_sampling_is_seeded_capped_and_filtered_before_selection():
    records = [decision(i=i) for i in range(20)]
    records += [decision("SKIP_EV") | {"policy": "prior"}]
    first, second = Writer(), Writer()
    a = evaluate(records, first, count=5, seed=12, policy="naive")
    b = evaluate(records, second, count=5, seed=12, policy="naive")
    assert a == b
    assert a["sampled"] == 5 and a["available"] == 20
    assert evaluate(records, Writer(), count=50, policy="prior")["sampled"] == 1
    assert records[0]["t"] == 1792444361261301  # input is not shuffled in place


def test_sample_identity_is_reproducible_and_seed_changes_selection():
    class Recording(Writer):
        def __init__(self):
            super().__init__()
            self.times = []

        def __call__(self, facts, feedback=None):
            self.times.append(facts["gap_bps"])
            return super().__call__(facts, feedback)

    records = [decision(i=i) | {"reason": f"gap {i}.0 bps"} for i in range(30)]
    writers = [Recording() for _ in range(3)]
    for writer, seed in zip(writers, [12, 12, 13]):
        evaluate(records, writer, count=5, seed=seed)
    assert writers[0].times == writers[1].times
    assert writers[0].times != writers[2].times


def test_template_baseline_is_not_reported_as_a_model_pass():
    result = evaluate([decision()], count=1)
    assert result["writer"] == "template"
    assert result["overall"] == {"decisions": 1, "first_try_passes": 0,
                                 "first_try_pass_rate": None, "mean_tries": 0.0,
                                 "template_fallbacks": 0, "failure_reasons": {}}


@pytest.mark.parametrize("records, count, policy", [([], 1, None), ([decision()], 0, None),
                                                  ([decision()], -1, None), ([decision()], 1, "prior")])
def test_invalid_or_empty_samples_are_rejected(records, count, policy):
    with pytest.raises(ValueError):
        evaluate(records, Writer(), count=count, policy=policy)


def test_cli_prints_json_without_writing_report_files(tmp_path, capsys):
    path = tmp_path / "decisions.jsonl"
    path.write_text(json.dumps(decision()) + "\n")
    main([str(path), "--count", "1", "--seed", "42"])
    result = json.loads(capsys.readouterr().out)
    assert result["sampled"] == 1 and result["seed"] == 42
    assert list(tmp_path.iterdir()) == [path]


def test_cli_rejects_incomplete_service_configuration(tmp_path):
    with pytest.raises(SystemExit) as exc:
        main([str(tmp_path / "unused.jsonl"), "--backend", "openai-compat"])
    assert exc.value.code == 2
