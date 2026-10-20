import math

from arbtrade.live import PaperEngine


def engine(prior=None):
    return PaperEngine(("x", "y"), trigger_bps=2.0, fee_bps=0.0, latency_ms={"x": 5, "y": 1}, notional=1_000.0, prior=prior)


def test_both_legs_fill_and_lock_in_the_gap():
    e = engine()
    e.on_quote("x", 0, 100.0, 100.1, 10, 10)
    e.on_quote("y", 1, 99.9, 100.0, 10, 10)
    e.on_quote("x", 2, 100.1, 100.2, 10, 10)      # sell x at 100.1, buy y at 100.0: 10 bps opens
    assert e.triggers == 1
    e.on_quote("y", 10_000, 99.9, 100.0, 10, 10)  # both orders have arrived (5 ms and 1 ms); book unchanged
    s = e.summary()["naive"]
    assert s["trades"] == 1 and s["full_fills"] == 1
    qty = 1_000.0 / ((100.1 + 100.0) / 2)
    assert math.isclose(s["pnl_usd"], round(qty * 0.1, 2), rel_tol=1e-6)


def test_slow_leg_misses_and_is_unwound():
    e = engine()
    e.on_quote("x", 0, 100.0, 100.1, 10, 10)
    e.on_quote("y", 1, 99.9, 100.0, 10, 10)
    e.on_quote("x", 2, 100.1, 100.2, 10, 10)      # trigger at t=2 µs
    e.on_quote("x", 3_000, 100.0, 100.1, 10, 10)  # x's bid drops before the x order (5 ms) arrives
    e.on_quote("y", 20_000, 99.9, 100.0, 10, 10)  # y filled at 100.0, x rejected -> sell y back after 1 ms
    e.on_quote("y", 30_000, 99.9, 100.0, 10, 10)
    s = e.summary()["naive"]
    assert s["trades"] == 1 and s["full_fills"] == 0
    qty = 1_000.0 / ((100.1 + 100.0) / 2)
    assert math.isclose(s["pnl_usd"], round(-qty * 0.1, 2), rel_tol=1e-6)  # bought 100.0, sold 99.9


def test_gap_staying_open_does_not_retrigger():
    e = engine()
    e.on_quote("x", 0, 100.0, 100.1, 10, 10)
    e.on_quote("y", 1, 99.9, 100.0, 10, 10)
    for k in range(5):
        e.on_quote("x", 2 + k, 100.1, 100.2, 10 + k, 10)  # size-only updates while the gap stays open
    assert e.triggers == 1


def test_unwind_closes_the_whole_position_even_if_displayed_size_is_small():
    e = engine()
    e.on_quote("x", 0, 100.0, 100.1, 10, 10)
    e.on_quote("y", 1, 99.9, 100.0, 10, 10)
    e.on_quote("x", 2, 100.1, 100.2, 10, 10)
    e.on_quote("x", 3_000, 100.0, 100.1, 10, 10)
    e.on_quote("y", 20_000, 99.9, 100.0, 0.01, 10)  # tiny bid size when the unwind arrives
    e.on_quote("y", 30_000, 99.9, 100.0, 0.01, 10)
    qty = 1_000.0 / ((100.1 + 100.0) / 2)
    assert math.isclose(e.summary()["naive"]["pnl_usd"], round(-qty * 0.1, 2), rel_tol=1e-6)


def open_gap(e, t0=0, x_bid=100.1):
    e.on_quote("x", t0, 100.0, 100.1, 10, 10)
    e.on_quote("y", t0 + 1, 99.9, 100.0, 10, 10)
    e.on_quote("x", t0 + 2, x_bid, x_bid + 0.1, 10, 10)


def test_stale_book_is_skipped_with_a_reason():
    e = PaperEngine(("x", "y"), trigger_bps=2.0, fee_bps=0.0, latency_ms={"x": 5, "y": 1}, notional=1_000.0, stale_ms=100)
    e.on_quote("y", 0, 99.9, 100.0, 10, 10)
    e.on_quote("x", 1, 100.0, 100.1, 10, 10)
    e.on_quote("x", 500_000, 100.1, 100.2, 10, 10)   # y has been silent for 0.5 s when the gap opens
    assert e.triggers == 1 and not e.trades
    d = e.decisions[-1]
    assert d["action"] == "SKIP_STALE" and d["reason"].startswith("y book")


def test_position_cap_blocks_growth_but_not_unwinding():
    e = PaperEngine(("x", "y"), trigger_bps=2.0, fee_bps=0.0, latency_ms={"x": 1, "y": 1}, notional=1_000.0, cap_usd=1_500.0)
    open_gap(e)                                        # sell x / buy y: short ~10 on x
    e.on_quote("x", 10_000, 100.0, 100.1, 10, 10)      # orders filled, gap closed
    e.on_quote("x", 20_000, 100.1, 100.2, 10, 10)      # same gap again: would reach ~$2,000 short
    assert [d["action"] for d in e.decisions] == ["ENTER", "SKIP_INVENTORY"]
    e.on_quote("x", 30_000, 99.6, 99.7, 10, 10)        # reverse gap: buy x at 99.7, sell y at 99.9
    assert e.decisions[-1]["action"] == "ENTER"


def test_thin_books_are_skipped():
    e = PaperEngine(("x", "y"), trigger_bps=2.0, fee_bps=0.0, latency_ms={"x": 1, "y": 1}, notional=1_000.0)
    e.on_quote("x", 0, 100.0, 100.1, 0.5, 0.5)
    e.on_quote("y", 1, 99.9, 100.0, 0.5, 0.5)
    e.on_quote("x", 2, 100.1, 100.2, 0.5, 0.5)         # $50 shown, below the $100 minimum
    assert e.decisions[-1]["action"] == "SKIP_THIN" and not e.trades
