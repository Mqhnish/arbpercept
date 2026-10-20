import numpy as np

from arbdata.kalman import kalman_regression, local_level, ou_halflife_s


def test_local_level_innovations_are_standardised():
    rng = np.random.default_rng(0)
    t = np.arange(0, 20_000, dtype=np.int64) * 100_000          # 100 ms steps
    level = np.cumsum(rng.normal(0, 0.2e-4 * np.sqrt(0.1), len(t)))
    y = level + rng.normal(0, 0.5e-4, len(t))
    m, p = local_level(t, y, (0.2e-4) ** 2, (0.5e-4) ** 2)
    z = (y - m) / np.sqrt(p + (0.5e-4) ** 2)
    assert np.isnan(m[0])
    assert 0.9 < np.nanstd(z[1000:]) < 1.1                      # well-specified filter: z ~ N(0, 1)


def test_regression_recovers_hedge_ratio():
    rng = np.random.default_rng(1)
    t = np.arange(0, 5_000, dtype=np.int64) * 1_000_000
    x = np.cumsum(rng.normal(0, 0.01, len(t)))
    y = 0.5 + 2.0 * x + rng.normal(0, 0.001, len(t))
    a, b, z = kalman_regression(t, y, x, 1e-8, 1e-8, 1e-6)
    assert abs(b[-1] - 2.0) < 0.05 and abs(a[-1] - 0.5) < 0.05


def test_ou_half_life_is_recovered():
    rng = np.random.default_rng(2)
    theta = np.log(2) / 20.0                                     # true half-life 20 s
    n = 4_000
    x = np.zeros(n)
    for i in range(1, n):
        x[i] = x[i - 1] * np.exp(-theta) + rng.normal(0, 1.0)
    t = np.arange(n, dtype=np.int64) * 1_000_000 + 500_000       # one observation mid-second
    hl = ou_halflife_s(t, x, window_s=600)
    assert np.isnan(hl[:2]).all()                                # nothing before two completed seconds
    est = np.nanmedian(hl[1500:])
    assert 14 < est < 28


def test_ou_uses_only_completed_seconds():
    rng = np.random.default_rng(3)
    t = np.sort(rng.integers(0, 900_000_000, 5_000)).astype(np.int64)
    x = rng.normal(0, 1, len(t))
    full = ou_halflife_s(t, x, window_s=100)
    cut = t[3000]
    part = ou_halflife_s(t[t <= cut], x[t <= cut], window_s=100)
    assert np.allclose(full[: len(part)], part, equal_nan=True)
