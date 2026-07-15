"""Independent Arb cross-check for the checked ``n=3`` interval artifact.

This module is deliberately test-only.  It parses the checked JSON directly
and uses only python-flint's Arb arithmetic for interval evaluation.  It does
not import the production verifier, angular oracle, artifact loader, geometry,
or high-precision proposal code.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from importlib import metadata
from itertools import permutations
import json
from pathlib import Path
from types import ModuleType
from typing import Any

import pytest


ROOT = Path(__file__).resolve().parents[1]
N3_ARTIFACT = ROOT / "examples" / "small_n_interval_certificate_n3.json"
ARB_PRECISION_BITS = 384
EXPECTED_PYTHON_FLINT_VERSION = "0.9.0"


@dataclass(frozen=True)
class ArbN3CrossCheck:
    """Decisive bounds and exact coverage counts from the test-only check."""

    python_flint_version: str
    record_count: int
    cycle_edge_count: int
    witness_pair_count: int
    witness_slack_count: int
    lower_cycle_sum_upper: Any
    upper_witness_slack_lowers: tuple[Any, ...]


def _load_artifact() -> dict[str, Any]:
    return json.loads(N3_ARTIFACT.read_text(encoding="utf-8"))


def _canonical_n3_orders() -> tuple[tuple[int, int, int], ...]:
    """Regenerate only the bounded ``n=3`` rotation/reflection representatives."""
    return tuple(
        order
        for order in permutations((1, 2, 3))
        if order[0] == 3 and order[1] < order[-1]
    )


def _require_flint() -> ModuleType:
    try:
        import flint
    except ModuleNotFoundError as exc:
        if exc.name != "flint":
            raise
        pytest.skip("python-flint is an optional test dependency")
    return flint


def _theta_arb(flint: ModuleType, radius: Any, a: int, b: int) -> Any:
    """Recompute ``theta_R(a,b)`` directly with Arb ``sqrt`` and ``asin``."""
    a_ball = flint.arb(a)
    b_ball = flint.arb(b)
    x_squared = (a_ball * b_ball) / (
        (radius + a_ball) * (radius + b_ball)
    )
    assert x_squared.lower() > 0
    assert x_squared.upper() < 1
    return 2 * x_squared.sqrt().asin()


def _lower_cycle_upper_bound(
    flint: ModuleType,
    record: dict[str, Any],
) -> tuple[Any, int]:
    radius = flint.arb(record["lower_radius_decimal"])
    radii = record["radius_order"]
    edges = record["lower_certificate"]["cycle"]
    tau = 2 * flint.arb.pi()
    total = flint.arb(0)

    for position, edge in enumerate(edges):
        source = edge["source"]
        target = edge["target"]
        next_source = edges[(position + 1) % len(edges)]["source"]
        assert target == next_source

        if edge["edge_kind"] == "forward_lower":
            assert source > target
            i, j = target, source
            theta = _theta_arb(flint, radius, radii[i], radii[j])
            edge_upper = (flint.arb(0) - theta.lower()).upper()
        elif edge["edge_kind"] == "wrap_upper":
            assert source < target
            i, j = source, target
            theta = _theta_arb(flint, radius, radii[i], radii[j])
            edge_upper = (tau.upper() - theta.lower()).upper()
        else:
            raise AssertionError(f"unsupported edge kind: {edge['edge_kind']!r}")
        total += edge_upper

    return total.upper(), len(edges)


def _upper_witness_slack_lower_bounds(
    flint: ModuleType,
    record: dict[str, Any],
) -> tuple[tuple[Any, ...], int]:
    radius = flint.arb(record["upper_radius_decimal"])
    radii = record["radius_order"]
    positions = tuple(
        flint.arb(value)
        for value in record["upper_certificate"]["positions_rad"]
    )
    tau = 2 * flint.arb.pi()
    slack_lowers: list[Any] = []
    pair_count = 0

    for i in range(len(radii)):
        for j in range(i + 1, len(radii)):
            theta = _theta_arb(flint, radius, radii[i], radii[j])
            delta = positions[j] - positions[i]
            forward_lower = (delta.lower() - theta.upper()).lower()
            wrap_lower = (
                tau.lower() - theta.upper() - delta.upper()
            ).lower()
            slack_lowers.extend((forward_lower, wrap_lower))
            pair_count += 1

    return tuple(slack_lowers), pair_count


@pytest.fixture(scope="module")
def arb_n3_crosscheck() -> ArbN3CrossCheck:
    flint = _require_flint()
    artifact = _load_artifact()
    records = artifact["local_brackets"]

    cycle_edge_count = 0
    witness_pair_count = 0
    witness_slack_lowers: list[Any] = []
    cycle_upper: Any | None = None

    with flint.ctx.workprec(ARB_PRECISION_BITS):
        for record in records:
            cycle_upper, edge_count = _lower_cycle_upper_bound(flint, record)
            slack_lowers, pair_count = _upper_witness_slack_lower_bounds(
                flint,
                record,
            )
            cycle_edge_count += edge_count
            witness_pair_count += pair_count
            witness_slack_lowers.extend(slack_lowers)

    assert cycle_upper is not None
    return ArbN3CrossCheck(
        python_flint_version=metadata.version("python-flint"),
        record_count=len(records),
        cycle_edge_count=cycle_edge_count,
        witness_pair_count=witness_pair_count,
        witness_slack_count=len(witness_slack_lowers),
        lower_cycle_sum_upper=cycle_upper,
        upper_witness_slack_lowers=tuple(witness_slack_lowers),
    )


def test_n3_checked_artifact_embedded_data_coverage_is_complete() -> None:
    artifact = _load_artifact()

    assert artifact["schema_version"] == "power-ringmin.small_n_interval_certificate.v1"
    assert artifact["artifact_type"] == "small_n_interval_certificate"
    assert artifact["instance"]["n"] == 3
    assert artifact["instance"]["radius_sequence"]["indices"] == [1, 2, 3]
    assert artifact["instance"]["radius_sequence"]["radii"] == [1, 4, 9]

    order_space = artifact["order_space"]
    records = artifact["local_brackets"]
    summaries = artifact["local_bracket_summaries"]
    expected_orders = _canonical_n3_orders()
    embedded_orders = tuple(tuple(record["index_order"]) for record in records)

    assert expected_orders == ((3, 1, 2),)
    assert order_space["order_type"] == "cyclic"
    assert order_space["equivalence"] == "rotation_reflection"
    assert (
        order_space["canonicalization_rule"]
        == "largest_index_first_second_index_less_than_last"
    )
    assert (
        order_space["coverage_rule"]
        == "exactly_one_verified_local_bracket_per_canonical_order"
    )
    assert order_space["expected_canonical_count"] == len(expected_orders)
    assert order_space["covered_canonical_count"] == len(expected_orders)
    assert len(records) == len(summaries) == len(expected_orders) == 1
    assert embedded_orders == expected_orders
    assert len(set(embedded_orders)) == len(embedded_orders)

    for record, summary in zip(records, summaries, strict=True):
        index_order = record["index_order"]
        radius_order = record["radius_order"]
        cycle = record["lower_certificate"]["cycle"]
        positions = record["upper_certificate"]["positions_rad"]

        assert record["schema_version"] == "power-ringmin.fixed_order_interval_bracket.v1"
        assert record["artifact_type"] == "fixed_order_interval_bracket"
        assert radius_order == [index * index for index in index_order]
        assert record["lower_certificate"]["kind"] == "negative_cycle"
        assert len(cycle) == 3
        assert record["upper_certificate"]["kind"] == "witness_positions"
        assert len(positions) == 3
        assert Decimal(positions[0]) == 0
        assert Decimal(record["lower_radius_decimal"]) > 0
        assert Decimal(record["lower_radius_decimal"]) < Decimal(
            record["upper_radius_decimal"]
        )

        assert summary["check_id"] == "LB-0001"
        assert summary["result"] == "pass"
        assert summary["index_order"] == index_order
        assert summary["radius_order"] == radius_order
        assert summary["lower_radius_decimal"] == record["lower_radius_decimal"]
        assert summary["upper_radius_decimal"] == record["upper_radius_decimal"]

    result = artifact["result"]
    only_record = records[0]
    assert (
        result["global_lower_bound"]["radius_decimal"]
        == only_record["lower_radius_decimal"]
    )
    assert result["global_lower_bound"]["included"] is False
    assert (
        result["global_lower_bound"]["source_index_order"]
        == only_record["index_order"]
    )
    assert (
        result["global_upper_bound"]["radius_decimal"]
        == only_record["upper_radius_decimal"]
    )
    assert result["global_upper_bound"]["included"] is True
    assert (
        result["global_upper_bound"]["source_index_order"]
        == only_record["index_order"]
    )


def test_n3_arb_lower_cycle_upper_bound_is_strictly_negative(
    arb_n3_crosscheck: ArbN3CrossCheck,
) -> None:
    assert arb_n3_crosscheck.python_flint_version == EXPECTED_PYTHON_FLINT_VERSION
    assert arb_n3_crosscheck.record_count == 1
    assert arb_n3_crosscheck.cycle_edge_count == 3
    assert arb_n3_crosscheck.lower_cycle_sum_upper < 0


def test_n3_arb_all_upper_witness_slack_lowers_are_nonnegative(
    arb_n3_crosscheck: ArbN3CrossCheck,
) -> None:
    assert arb_n3_crosscheck.record_count == 1
    assert arb_n3_crosscheck.witness_pair_count == 3
    assert arb_n3_crosscheck.witness_slack_count == 6
    for slack_lower in arb_n3_crosscheck.upper_witness_slack_lowers:
        assert slack_lower >= 0
