"""Configuration loading and on-disk layout."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

DEFAULT_CONFIG = Path(__file__).resolve().parent.parent / "config" / "sources.yaml"


@dataclass(frozen=True)
class Stream:
    source: str
    venue: str
    pair: str
    kind: str
    symbol: str
    market: str | None = None
    exchange: str | None = None

    @property
    def key(self) -> str:
        return f"{self.source}/{self.venue}/{self.pair}/{self.kind}"


@dataclass(frozen=True)
class PairSpec:
    name: str
    type: str  # "cross" or "basis"
    a: str
    b: str


class Config:
    def __init__(self, raw: dict[str, Any], root: Path):
        self.raw = raw
        self.root = root
        self.data_root = (root / raw.get("data_root", "data")).resolve()
        self.sources: dict[str, dict[str, Any]] = raw["sources"]
        self.streams: dict[str, Stream] = {}
        for s in raw["streams"]:
            stream = Stream(**s)
            if stream.source not in self.sources:
                raise ValueError(f"stream {stream.key} uses unknown source {stream.source}")
            self.streams[stream.key] = stream
        self.pairs: dict[str, PairSpec] = {}
        for p in raw["pairs"]:
            spec = PairSpec(**p)
            for leg in (spec.a, spec.b):
                if leg not in self.streams:
                    raise ValueError(f"pair {spec.name} references unknown stream {leg}")
            if spec.type not in ("cross", "basis", "ratio"):
                raise ValueError(f"pair {spec.name} has unknown type {spec.type}")
            if spec.type == "basis":
                if self.streams[spec.a].kind != "spot" or self.streams[spec.b].kind != "perp":
                    raise ValueError(f"basis pair {spec.name} must be a=spot, b=perp")
            self.pairs[spec.name] = spec
        self.fees: dict[str, dict[str, float]] = raw["fees_taker_bps"]
        self.latency_ms: dict[str, float] = raw.get("order_latency_ms", {})
        self.quality: dict[str, Any] = raw["quality"]
        self.episodes: dict[str, Any] = raw["episodes"]
        self.features: dict[str, Any] = raw["features"]
        self.splits: dict[str, Any] = raw["splits"]

    # ---- on-disk layout -------------------------------------------------
    def raw_path(self, stream: Stream, date: str, ext: str) -> Path:
        return self.data_root / "raw" / stream.key / f"{date}{ext}"

    def l1_path(self, stream: Stream, date: str) -> Path:
        return self.data_root / "l1" / stream.key / f"{date}.parquet"

    def trades_raw_path(self, stream: Stream, date: str) -> Path:
        return self.data_root / "raw" / "trades" / stream.key / f"{date}.csv.gz"

    def trades_path(self, stream: Stream, date: str) -> Path:
        return self.data_root / "trades" / stream.key / f"{date}.parquet"

    def episodes_path(self, pair: str, date: str) -> Path:
        return self.data_root / "episodes" / pair / f"{date}.parquet"

    @property
    def reports_dir(self) -> Path:
        return self.data_root / "reports"

    @property
    def manifest_path(self) -> Path:
        return self.data_root / "raw" / "manifest.jsonl"

    @property
    def splits_path(self) -> Path:
        return self.data_root / "splits.json"

    # ---- helpers ----------------------------------------------------------
    def source_cfg(self, stream_key: str) -> dict[str, Any]:
        return self.sources[self.streams[stream_key].source]

    def resolution_ms(self, pair: PairSpec) -> float:
        """A pair is only as precise as its coarsest leg."""
        return max(self.source_cfg(pair.a)["resolution_ms"], self.source_cfg(pair.b)["resolution_ms"])

    def retail_hurdle_bps(self, pair: PairSpec) -> float:
        a, b = self.streams[pair.a], self.streams[pair.b]
        one_way = self.fees[a.venue][a.kind] + self.fees[b.venue][b.kind]
        # A cross-venue arb is two fills against pre-positioned inventory. A basis
        # trade must also be unwound when the basis reverts: four fills.
        return one_way if pair.type == "cross" else 2 * one_way


def load_config(path: str | Path | None = None) -> Config:
    path = Path(path) if path else DEFAULT_CONFIG
    with open(path) as fh:
        raw = yaml.safe_load(fh)
    return Config(raw, root=path.resolve().parent.parent)
