from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

import verify as standalone_verify


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "fixed_order_result.schema.json"
EXAMPLE_PATH = ROOT / "examples" / "fixed_order_result_n3.json"


def _load_json(path: Path) -> dict[str, object]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def _tolerance_value(artifact: dict[str, object], name: str) -> mp.mpf:
    precision = artifact["precision"]
    assert isinstance(precision, dict)
    tolerances = precision["tolerances"]
    assert isinstance(tolerances, list)
    for item in tolerances:
        assert isinstance(item, dict)
        if item["name"] == name:
            return mp.mpf(str(item["value_decimal"]))
    raise AssertionError(f"missing tolerance {name!r}")


def test_fixed_order_result_schema_contract() -> None:
    schema = _load_json(SCHEMA_PATH)

    assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    assert schema["properties"]["schema_version"]["const"] == "power-ringmin.fixed_order_result.v1"
    assert schema["properties"]["artifact_type"]["const"] == "fixed_order_numerical_result"

    required = set(schema["required"])
    assert {
        "instance",
        "fixed_order",
        "result",
        "precision",
        "provenance",
        "evidence",
    } <= required

    classifications = set(schema["$defs"]["evidenceClassification"]["enum"])
    assert {
        "definition",
        "verified_fact",
        "exact_theorem",
        "computer_certified_result",
        "numerical_observation",
        "empirical_pattern",
        "heuristic",
        "conjecture",
        "unresolved_claim",
        "disproved_claim",
    } == classifications


def test_fixed_order_result_example_has_required_semantics() -> None:
    schema = _load_json(SCHEMA_PATH)
    artifact = _load_json(EXAMPLE_PATH)

    assert artifact["schema_version"] == schema["properties"]["schema_version"]["const"]
    assert artifact["artifact_type"] == schema["properties"]["artifact_type"]["const"]
    assert artifact["problem"]["constraints"]["all_pairs_checked"] is True

    instance = artifact["instance"]
    fixed_order = artifact["fixed_order"]
    evidence = artifact["evidence"]
    assert isinstance(instance, dict)
    assert isinstance(fixed_order, dict)
    assert isinstance(evidence, dict)

    radius_sequence = instance["radius_sequence"]
    assert isinstance(radius_sequence, dict)
    n = instance["n"]
    assert isinstance(n, int)
    assert radius_sequence["indices"] == list(range(1, n + 1))
    assert radius_sequence["radii"] == [str(k * k) for k in range(1, n + 1)]

    assert sorted(fixed_order["index_order"]) == radius_sequence["indices"]
    assert sorted(fixed_order["radius_order"], key=mp.mpf) == radius_sequence["radii"]
    assert fixed_order["angle_anchor"] == {"position_index": 0, "angle_decimal": "0.0"}

    classifications = set(schema["$defs"]["evidenceClassification"]["enum"])
    assert evidence["classification"] in classifications
    assert evidence["claim"]["scope"] == "schema_fixture"
    assert all(check["classification"] in classifications for check in evidence["checks"])


def test_fixed_order_result_example_verifies_with_standalone_checker() -> None:
    artifact = _load_json(EXAMPLE_PATH)
    fixed_order = artifact["fixed_order"]
    result = artifact["result"]
    precision = artifact["precision"]
    assert isinstance(fixed_order, dict)
    assert isinstance(result, dict)
    assert isinstance(precision, dict)

    mp.mp.dps = int(precision["working_precision_digits"])
    order = standalone_verify._as_mpf_order(fixed_order["radius_order"])
    radius = mp.mpf(str(result["central_radius"]["decimal"]))
    positions = result["positions_rad"]
    assert isinstance(positions, list)

    stn_tol = _tolerance_value(artifact, "stn_diagonal_feasibility")
    eta = _tolerance_value(artifact, "local_radius_eta")

    margin = standalone_verify.feasibility_margin(order, radius)
    assert margin >= -stn_tol
    assert standalone_verify.feasible(order, radius + eta, stn_tol)
    assert not standalone_verify.feasible(order, radius - eta, stn_tol)

    messages: list[str] = []
    assert standalone_verify.check_witness(order, radius, positions, messages)
    assert messages == []
