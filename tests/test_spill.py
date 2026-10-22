import numpy as np

from arbtrade.evaluate import spill_legs
from arbtrade.replay import Leg, execute


def leg(t, bid, ask, size=10.0):
    t = np.asarray(t, dtype=np.int64)
    return Leg(t, np.asarray(bid, float), np.asarray(ask, float), np.full(len(t), size), np.full(len(t), size), False)


def test_spilled_legs_are_disk_backed_and_replay_identically(tmp_path):
    legs = {"a": leg([0, 5_000], [101.0, 100.9], [101.1, 101.0]), "b": leg([0, 5_000], [99.9, 100.0], [100.0, 100.1]),
            "offset": (np.array([0, 5_000], np.int64), np.array([0.5, 0.4]))}
    mapped = spill_legs(legs, tmp_path / "2024-01-01")
    assert isinstance(mapped["a"].bid, np.memmap) and isinstance(mapped["offset"][1], np.memmap)
    assert not mapped["a"].bid.flags.writeable
    t = np.array([0, 1_000], np.int64)
    before = execute(legs["a"], legs["b"], t, 2_000, 1.0, 1.0, 1_000.0, "optimistic")
    after = execute(mapped["a"], mapped["b"], t, 2_000, 1.0, 1.0, 1_000.0, "optimistic")
    assert before.equals(after)
