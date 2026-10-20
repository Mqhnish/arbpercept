"""Label opportunity episodes: when each mispricing was born, how long it lived, and why it ended.

An episode is a maximal run of consecutive events where a direction's executable edge
exceeds a hurdle while both legs are valid. Lifetimes are survival data:
  died=True    the edge fell back below the hurdle (an observed death)
  died=False   the run was cut by a data gap or the end of the day (right-censored);
               dropping these would bias lifetimes short, so they are kept and flagged
Runs already in progress when data became valid have an unknown birth and are dropped.
Sampled sources only time births and deaths to within their resolution, so every
death carries an interval [lower_ms, upper_ms] (interval censoring).
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from .config import PairSpec


def ratio_fair(t: np.ndarray, al: pd.DataFrame, valid: np.ndarray, cfg_features: dict) -> tuple[np.ndarray, np.ndarray]:
    """Cross-asset fair value: log(b) = alpha + beta * log(a), both drifting (two-state Kalman).

    Variables are centred on the day's first valid observation so the filter starts at
    alpha = 0, beta = 1. Returns, at every event, the filter's predicted (pre-update, so
    causal) intercept and hedge ratio converted back to absolute log prices.
    """
    from .kalman import kalman_regression
    x = np.log(al.a_mid.to_numpy())
    y = np.log(al.b_mid.to_numpy())
    first = int(np.argmax(valid & ~np.isnan(x) & ~np.isnan(y)))
    x0, y0 = x[first], y[first]
    xs = np.where(valid, x - x0, np.nan)
    ys = np.where(valid, y - y0, np.nan)
    qa = (cfg_features.get("ratio_q_alpha_bps_per_sqrt_s", 0.5) * 1e-4) ** 2
    qb = cfg_features.get("ratio_q_beta_per_sqrt_s", 1e-3) ** 2
    r = (cfg_features.get("ratio_r_bps", 2.0) * 1e-4) ** 2
    alpha, beta, _ = kalman_regression(t, ys, xs, qa, qb, r)
    return alpha + y0 - beta * x0, beta  # fair log(b) = alpha_abs + beta * log(a)


def cross_offset_bps(al: pd.DataFrame, window_s: float) -> np.ndarray:
    """The venues' usual offset at every event: trailing (strictly past) median of mid a minus
    mid b, in bps of the pair mid. Moments when either leg is down are left out, so a dead
    feed cannot drag the reference."""
    from .features import trailing_reference
    mid = ((al.a_mid + al.b_mid) / 2).to_numpy()
    x = (al.a_mid - al.b_mid).to_numpy() / mid * 1e4
    if "valid" in al:
        x = np.where(al.valid.to_numpy(), x, np.nan)
    return trailing_reference(al.t.to_numpy(), x, window_s)


CROSS_SIGN = {"sell_a_buy_b": 1.0, "sell_b_buy_a": -1.0}  # how the a-minus-b offset enters each direction's gap


def edges(al: pd.DataFrame, pair_type: str, basis_ref: np.ndarray | None,
          ratio: tuple[np.ndarray, np.ndarray] | None = None,
          cross_ref: np.ndarray | None = None) -> dict[str, np.ndarray]:
    """Executable gross edge in bps for each trade direction, crossing both spreads.

    cross_ref (cross pairs): the venues' usual offset (cross_offset_bps). When given, each gap
    is measured against it instead of zero, so a persistent offset is not counted as edge."""
    a_bid, a_ask = al.a_bid_px.to_numpy(), al.a_ask_px.to_numpy()
    b_bid, b_ask = al.b_bid_px.to_numpy(), al.b_ask_px.to_numpy()
    a_mid = al.a_mid.to_numpy()
    if pair_type == "ratio":
        # b rich: sell b at its bid, buy beta units of a at its ask; b cheap: the reverse.
        # The edge is how far b's executable price sits from its fair value given a's
        # executable price; profit comes when the relationship reverts.
        alpha, beta = ratio
        return {
            "sell_b_buy_a": (np.log(b_bid) - (alpha + beta * np.log(a_ask))) * 1e4,
            "buy_b_sell_a": ((alpha + beta * np.log(a_bid)) - np.log(b_ask)) * 1e4,
        }
    if pair_type == "cross":
        mid_ref = (a_mid + al.b_mid.to_numpy()) / 2
        raw = {
            "sell_a_buy_b": (a_bid - b_ask) / mid_ref * 1e4,
            "sell_b_buy_a": (b_bid - a_ask) / mid_ref * 1e4,
        }
        if cross_ref is None:
            return raw
        return {d: e - CROSS_SIGN[d] * cross_ref for d, e in raw.items()}
    # basis: a = spot, b = perp. The edge is the dislocation from the trailing normal
    # basis that remains after paying both spreads; profit comes when the basis reverts.
    return {
        "sell_perp_buy_spot": (b_bid - a_ask) / a_mid * 1e4 - basis_ref,
        "buy_perp_sell_spot": basis_ref - (b_ask - a_bid) / a_mid * 1e4,
    }


def label_runs(t: np.ndarray, edge: np.ndarray, valid: np.ndarray, hurdle: float,
               warmup_end: int, resolution_ms: float) -> pd.DataFrame:
    n = len(t)
    known = valid & ~np.isnan(edge)  # no reference level yet counts as unknown, not "no edge"
    state = np.where(known, (edge > hurdle).astype(np.int8), np.int8(-1))
    up = (state == 1).astype(np.int8)
    d = np.diff(np.concatenate(([0], up, [0])))
    starts = np.flatnonzero(d == 1)
    ends = np.flatnonzero(d == -1) - 1
    if len(starts) == 0:
        return pd.DataFrame()

    prev_state = np.where(starts > 0, state[np.maximum(starts - 1, 0)], -1)
    keep = (prev_state == 0) & (t[starts] >= warmup_end)
    starts, ends = starts[keep], ends[keep]
    if len(starts) == 0:
        return pd.DataFrame()

    nxt = ends + 1
    has_next = nxt < n
    next_state = np.full(len(nxt), -2, dtype=np.int8)
    next_state[has_next] = state[nxt[has_next]]
    died = next_state == 0
    end_t = np.where(died, t[np.minimum(nxt, n - 1)], t[ends])
    obs_ms = (end_t - t[starts]) / 1000
    lower = np.where(died, np.maximum(obs_ms - resolution_ms, 0.0), obs_ms)
    upper = np.where(died, obs_ms + resolution_ms, np.inf)
    end_reason = np.where(died, "died", np.where(next_state == -1, "data_gap", "end_of_day"))

    lengths = ends - starts + 1
    seg = np.repeat(np.arange(len(starts)), lengths)
    rows = np.arange(lengths.sum()) - np.repeat(np.cumsum(lengths) - lengths, lengths) + np.repeat(starts, lengths)
    vals = edge[rows]
    offsets = np.concatenate(([0], np.cumsum(lengths)[:-1]))
    peak = np.maximum.reduceat(vals, offsets)
    first_peak_row = np.minimum.reduceat(np.where(vals == peak[seg], rows, n), offsets)

    return pd.DataFrame({
        "birth_idx": starts,
        "birth_ts": t[starts],
        "obs_ms": obs_ms,
        "lower_ms": lower,
        "upper_ms": upper,
        "died": died,
        "end_reason": end_reason,
        # Shorter than the pair's sampling step: on sampled feeds these are mostly births at one
        # leg's update while the other leg's quote is old, so only [lower_ms, upper_ms] is known.
        "sub_resolution": obs_ms < resolution_ms,
        "edge_birth_bps": edge[starts],
        "edge_peak_bps": peak,
        "t_to_peak_ms": (t[first_peak_row] - t[starts]) / 1000,
        "n_events": lengths,
    })


def kalman_context(al: pd.DataFrame, valid: np.ndarray, cfg_features: dict) -> dict[str, np.ndarray]:
    """Slow-path statistics at every event: the log-spread's deviation from its Kalman-filtered fair
    level, standardised (z), and the deviation's mean-reversion half-life. Invalid events do not
    update the filter. arbtrade/slowpath.py computes the same values one update at a time."""
    from .kalman import local_level, ou_halflife_s
    t = al.t.to_numpy()
    spread = np.log(al.b_mid.to_numpy()) - np.log(al.a_mid.to_numpy())
    q = (cfg_features.get("kalman_q_bps_per_sqrt_s", 0.2) * 1e-4) ** 2
    r = (cfg_features.get("kalman_r_bps", 0.5) * 1e-4) ** 2
    m_pred, p_pred = local_level(t, np.where(valid, spread, np.nan), q, r)
    k_dev = spread - m_pred
    return {"f_kalman_dev_bps": k_dev * 1e4, "f_kalman_z": k_dev / np.sqrt(p_pred + r),
            "f_ou_halflife_s": ou_halflife_s(t, k_dev, int(cfg_features.get("ou_window_s", 300)))}


def recent_births(birth_ts: np.ndarray, window_us: int) -> np.ndarray:
    """For each birth, how many earlier births fall in [t - window, t)."""
    order = np.argsort(birth_ts, kind="stable")
    sorted_ts = birth_ts[order]
    lo = np.searchsorted(sorted_ts, sorted_ts - window_us, side="left")
    here = np.searchsorted(sorted_ts, sorted_ts, side="left")
    out = np.empty(len(birth_ts), dtype=np.int64)
    out[order] = here - lo
    return out


def edge_change(t: np.ndarray, edge: np.ndarray, idx: np.ndarray, lookback_us: int) -> np.ndarray:
    """edge(t) minus the edge in force lookback_us earlier (as-of, past only)."""
    j = np.searchsorted(t, t[idx] - lookback_us, side="right") - 1
    prev = np.where(j >= 0, edge[np.maximum(j, 0)], np.nan)
    return edge[idx] - prev


def label_pair_day(al: pd.DataFrame, pair: PairSpec, date: str, hurdles: dict[str, float],
                   resolution_ms: float, cfg_episodes: dict, cfg_features: dict,
                   leg_resolution_ms: tuple[float, float] = (1.0, 1.0),
                   trades: tuple[pd.DataFrame | None, pd.DataFrame | None] = (None, None),
                   cross_offset_window_s: float | None = None) -> pd.DataFrame:
    """cross_offset_window_s (cross pairs only): label births on the gap measured against the
    venues' trailing offset over this window, instead of against zero. edge_birth_bps is then the
    relative gap, and edge_offset_bps is the offset that was subtracted (raw = relative + offset)."""
    from .features import features_at, rolling_context, trade_flow_at, trailing_reference

    use_offset = pair.type == "cross" and cross_offset_window_s is not None
    windows = [*cfg_features["vol_windows_s"], *cfg_features["rate_windows_s"],
               *cfg_features.get("trade_windows_s", []), cfg_features.get("ou_window_s", 0),
               cfg_episodes["basis_ref_window_s"], cross_offset_window_s if use_offset else 0]
    if cfg_episodes["warmup_s"] < max(windows):
        raise ValueError("warmup_s must cover the longest trailing window, or early features are incomplete")

    t = al.t.to_numpy()
    valid = al.valid.to_numpy()
    basis_bps = ((al.b_mid - al.a_mid) / al.a_mid * 1e4).to_numpy()
    basis_ref = trailing_reference(t, basis_bps, cfg_episodes["basis_ref_window_s"])
    basis_dev = basis_bps - basis_ref
    day_start = int(pd.Timestamp(date, tz="UTC").value // 1000)
    warmup_end = day_start + int(cfg_episodes["warmup_s"] * 1e6)

    ctx = rolling_context(al, cfg_features["vol_windows_s"], cfg_features["rate_windows_s"])
    ctx.update(kalman_context(al, valid, cfg_features))
    max_lag = cfg_episodes["max_feed_lag_ms"]
    window_us = int(cfg_features["recent_births_window_s"] * 1e6)
    trade_windows = cfg_features.get("trade_windows_s", [1, 10])
    margin_us = int(cfg_features.get("trade_publish_margin_ms", 50) * 1000)
    partner_frac = cfg_features.get("stale_partner_fraction", 0.5)

    frames = []
    ratio = ratio_fair(t, al, valid, cfg_features) if pair.type == "ratio" else None
    cross_ref = cross_offset_bps(al, cross_offset_window_s) if use_offset else None
    for direction, edge in edges(al, pair.type, basis_ref, ratio, cross_ref).items():
        for hurdle_name, hurdle in hurdles.items():
            ep = label_runs(t, edge, valid, hurdle, warmup_end, resolution_ms)
            if ep.empty:
                continue
            idx = ep.birth_idx.to_numpy()
            ep.insert(0, "hurdle_bps", hurdle)
            ep.insert(0, "hurdle_name", hurdle_name)
            ep.insert(0, "direction", direction)
            ep["stale_birth"] = ((al.a_lag_ms.to_numpy()[idx] > max_lag) | (al.b_lag_ms.to_numpy()[idx] > max_lag))
            # On a sampled leg, a quote older than part of its step may already have changed
            # unseen: the opportunity may be an artefact of comparing a fresh quote with a stale one.
            stale_partner = np.zeros(len(idx), dtype=bool)
            for leg, res in (("a", leg_resolution_ms[0]), ("b", leg_resolution_ms[1])):
                if res > 1:
                    stale_partner |= al[f"{leg}_age_ms"].to_numpy()[idx] > partner_frac * res
            ep["stale_partner"] = stale_partner
            if use_offset:
                ep["edge_offset_bps"] = CROSS_SIGN[direction] * cross_ref[idx]
            ep["f_edge_change_1s_bps"] = edge_change(t, edge, idx, 1_000_000)
            ep["f_recent_births"] = recent_births(ep.birth_ts.to_numpy(), window_us)
            feats = features_at(al, ctx, basis_dev, idx)
            births = t[idx]
            for leg, tr in (("a", trades[0]), ("b", trades[1])):
                for k, v in trade_flow_at(tr, births, trade_windows, margin_us, leg).items():
                    feats[k] = v
            frames.append(pd.concat([ep.reset_index(drop=True), feats], axis=1))
    if not frames:
        return pd.DataFrame()
    out = pd.concat(frames, ignore_index=True).drop(columns=["birth_idx"])
    out.insert(0, "resolution_ms", resolution_ms)
    out.insert(0, "date", date)
    out.insert(0, "pair_type", pair.type)
    out.insert(0, "pair", pair.name)
    return out
