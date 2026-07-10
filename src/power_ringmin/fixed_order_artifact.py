"""Export and load v1 fixed-order result artifacts.

The artifact schema is documented in ``schemas/fixed_order_result.schema.json``.
This module deliberately performs lightweight semantic validation instead of
depending on a JSON Schema runtime package.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import copy
import json
import math
import platform
import re
import subprocess
import sys
from typing import Any, Literal

import mpmath as mp

from power_ringmin import highprec
from power_ringmin.evaluator import (
    FULL_REL_TOL,
    TIGHT_TOL,
    BindingPair,
    FullResult,
)

SCHEMA_VERSION = "power-ringmin.fixed_order_result.v1"
ARTIFACT_TYPE = "fixed_order_numerical_result"
PROJECT_NAME = "power-ringmin"
RADIUS_MODEL = "quadratic"
DIMENSION = 2
UPSTREAM_RINGMIN_COMMIT = "cc0327400819fe06b230d967cdcbafffe1648317"

DECIMAL_STRING_RE = re.compile(r"^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?$")

EvidenceClassification = Literal[
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
]

EVIDENCE_CLASSIFICATIONS: frozenset[str] = frozenset(
    {
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
    }
)

RESULT_KINDS = frozenset(
    {
        "full_fixed_order_radius",
        "chain_relaxation_radius",
        "feasibility_witness",
        "optimizer_candidate",
    }
)

OBJECTIVE_STATUSES = frozenset(
    {
        "bracketed_fixed_order_minimum",
        "feasible_upper_bound",
        "infeasible_lower_bound",
        "optimizer_candidate",
        "diagnostic_only",
    }
)

EVIDENCE_SCOPES = frozenset(
    {
        "schema_fixture",
        "fixed_order_feasibility",
        "fixed_order_radius_bracket",
        "fixed_order_optimizer_candidate",
        "global_instance_claim",
    }
)


@dataclass(frozen=True)
class FixedOrderArtifact:
    """Validated view of a fixed-order v1 artifact."""

    data: dict[str, Any]

    @classmethod
    def from_mapping(cls, artifact: Mapping[str, Any]) -> "FixedOrderArtifact":
        data = copy.deepcopy(dict(artifact))
        validate_fixed_order_artifact(data)
        return cls(data)

    @property
    def n(self) -> int:
        return int(self.data["instance"]["n"])

    @property
    def index_order(self) -> tuple[int, ...]:
        return tuple(int(value) for value in self.data["fixed_order"]["index_order"])

    @property
    def radius_order(self) -> tuple[str, ...]:
        return tuple(str(value) for value in self.data["fixed_order"]["radius_order"])

    @property
    def central_radius_decimal(self) -> str:
        return str(self.data["result"]["central_radius"]["decimal"])

    @property
    def positions_rad(self) -> tuple[str, ...] | None:
        positions = self.data["result"].get("positions_rad")
        if positions is None:
            return None
        return tuple(str(value) for value in positions)

    @property
    def evidence_classification(self) -> str:
        return str(self.data["evidence"]["classification"])

    def to_dict(self) -> dict[str, Any]:
        """Return a deep copy suitable for JSON serialization."""
        return copy.deepcopy(self.data)

    def to_verifier_payload(self) -> dict[str, Any]:
        """Return the minimal payload accepted by root ``verify.py``."""
        payload: dict[str, Any] = {
            "ordering": list(self.radius_order),
            "R_mpmath_full": self.central_radius_decimal,
        }
        if self.positions_rad is not None:
            payload["positions"] = list(self.positions_rad)
        return payload


def export_full_result_artifact(
    result: FullResult,
    *,
    created_at_utc: str | None = None,
    repository: Mapping[str, Any] | None = None,
    software: Sequence[Mapping[str, Any]] | None = None,
    source_files: Sequence[Mapping[str, Any]] | None = None,
    commands: Sequence[Mapping[str, Any]] | None = None,
    evidence_classification: EvidenceClassification = "numerical_observation",
    evidence_scope: str = "fixed_order_radius_bracket",
    evidence_statement: str | None = None,
    evidence_checks: Sequence[Mapping[str, Any]] | None = None,
    limitations: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Build a v1 artifact from the float64 STN evaluator ``FullResult``."""
    source_digits = 17
    bindings = {
        "essential_tight_pairs": [
            _binding_pair_to_json(binding, digits=source_digits)
            for binding in result.essential_tight_pairs
        ],
        "recovered_tight_pairs": [
            _binding_pair_to_json(binding, digits=source_digits)
            for binding in result.recovered_tight_pairs
        ],
        "floating_radii": [_decimal_string(radius, digits=source_digits) for radius in result.floating_radii],
    }
    default_checks = [
        {
            "check_id": "EV-001",
            "classification": "verified_fact",
            "method": "float64 all-pairs STN fixed-order evaluator",
            "result": "pass" if result.feasible else "fail",
            "output_summary": (
                "Evaluator returned positions, Cartesian validation, tight-pair "
                "structure, and floating radii for the supplied fixed order."
            ),
            "limitations": "Float64 evaluator output is numerical evidence, not a theorem.",
        }
    ]
    return build_fixed_order_artifact(
        order=result.order,
        central_radius=result.R_full,
        chain_radius=result.R_chain,
        positions=result.positions,
        result_kind="full_fixed_order_radius",
        objective_status="bracketed_fixed_order_minimum" if result.feasible else "diagnostic_only",
        feasible=result.feasible,
        primary_backend="float64",
        working_precision_digits=source_digits,
        rounding_policy="Float64 values encoded with Python repr; integer radii encoded canonically.",
        tolerances=[
            {
                "name": "full_radius_relative_bisection",
                "value_decimal": FULL_REL_TOL,
                "tolerance_type": "relative",
                "applies_to": "float64 fixed-order radius bisection",
            },
            {
                "name": "binding_tight_pair",
                "value_decimal": TIGHT_TOL,
                "tolerance_type": "absolute",
                "applies_to": "tight-pair and floating-radius detection",
            },
            {
                "name": "cartesian_validation_abs",
                "value_decimal": "1e-9",
                "tolerance_type": "absolute",
                "applies_to": "Cartesian non-overlap assertion",
            },
        ],
        binding_structure=bindings,
        created_at_utc=created_at_utc,
        repository=repository,
        software=software,
        source_files=source_files
        or [
            {
                "path": "src/power_ringmin/evaluator.py",
                "role": "float64 fixed-order STN evaluator",
                "upstream_ringmin_commit": UPSTREAM_RINGMIN_COMMIT,
            },
            {
                "path": "src/power_ringmin/fixed_order_artifact.py",
                "role": "artifact exporter and loader",
            },
        ],
        commands=commands,
        evidence_classification=evidence_classification,
        evidence_scope=evidence_scope,
        evidence_statement=evidence_statement
        or (
            "This artifact records a numerical fixed-order float64 STN result; "
            "it is not a global optimum certificate."
        ),
        evidence_checks=evidence_checks or default_checks,
        limitations=limitations
        or [
            "Finite fixed-order computation only.",
            "Float64 numerical result.",
            "No global cyclic-order optimality claim.",
        ],
    )


def export_highprec_artifact(
    order: Sequence[Any],
    central_radius: Any,
    *,
    positions: Sequence[Any] | None = None,
    chain_radius: Any | None = None,
    digits: int = 80,
    local_radius_eta: Any | None = None,
    stn_tolerance: Any | None = None,
    created_at_utc: str | None = None,
    repository: Mapping[str, Any] | None = None,
    software: Sequence[Mapping[str, Any]] | None = None,
    source_files: Sequence[Mapping[str, Any]] | None = None,
    commands: Sequence[Mapping[str, Any]] | None = None,
    evidence_classification: EvidenceClassification = "numerical_observation",
    evidence_scope: str = "fixed_order_radius_bracket",
    evidence_statement: str | None = None,
    evidence_checks: Sequence[Mapping[str, Any]] | None = None,
    limitations: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Build a v1 artifact from high-precision fixed-order values."""
    if digits < 30:
        raise ValueError(f"digits must be at least 30, got {digits!r}")

    mp.mp.dps = digits
    mp_order = tuple(mp.mpf(str(value)) for value in order)
    radius = mp.mpf(str(central_radius))
    tolerance = (
        mp.mpf(10) ** (-max(30, digits // 2))
        if stn_tolerance is None
        else mp.mpf(str(stn_tolerance))
    )

    local_bracket = None
    tolerance_records = [
        {
            "name": "stn_diagonal_feasibility",
            "value_decimal": _decimal_string(tolerance, digits=digits),
            "tolerance_type": "absolute",
            "applies_to": "minimum closed-STN diagonal margin",
        }
    ]
    if local_radius_eta is not None:
        eta = mp.mpf(str(local_radius_eta))
        if eta <= 0:
            raise ValueError(f"local_radius_eta must be positive, got {local_radius_eta!r}")
        lower_feasible = False
        if radius > eta:
            lower_feasible = highprec.is_feasible_mp(mp_order, radius - eta, digits=digits, tol=tolerance)
        claimed_feasible = highprec.is_feasible_mp(mp_order, radius, digits=digits, tol=tolerance)
        upper_feasible = highprec.is_feasible_mp(mp_order, radius + eta, digits=digits, tol=tolerance)
        local_bracket = {
            "eta_decimal": _decimal_string(eta, digits=digits),
            "lower_radius_feasible": lower_feasible,
            "claimed_radius_feasible": claimed_feasible,
            "upper_radius_feasible": upper_feasible,
            "method": "mpmath all-pairs STN feasibility with local eta bracket",
        }
        tolerance_records.append(
            {
                "name": "local_radius_eta",
                "value_decimal": _decimal_string(eta, digits=digits),
                "tolerance_type": "absolute",
                "applies_to": "local fixed-order radius bracket",
            }
        )

    if positions is not None:
        tolerance_records.extend(
            [
                {
                    "name": "witness_angle",
                    "value_decimal": "1e-8",
                    "tolerance_type": "absolute",
                    "applies_to": "witness angular pair slacks",
                },
                {
                    "name": "witness_cartesian",
                    "value_decimal": "1e-8",
                    "tolerance_type": "absolute",
                    "applies_to": "witness Cartesian pair distances",
                },
            ]
        )

    margin = highprec.feasibility_margin_mp(mp_order, radius, digits=digits)
    default_checks = [
        {
            "check_id": "EV-001",
            "classification": "verified_fact",
            "method": "mpmath all-pairs STN fixed-order feasibility",
            "result": "pass" if margin >= -tolerance else "fail",
            "output_summary": f"Minimum closed-STN diagonal margin {mp.nstr(margin, min(digits, 30))}.",
            "limitations": "High-precision finite computation is not a theorem for all instances.",
        }
    ]
    return build_fixed_order_artifact(
        order=order,
        central_radius=central_radius,
        chain_radius=chain_radius,
        positions=positions,
        result_kind="full_fixed_order_radius",
        objective_status="bracketed_fixed_order_minimum",
        feasible=margin >= -tolerance,
        primary_backend="mpmath",
        working_precision_digits=digits,
        rounding_policy=f"Decimal strings emitted with mpmath nstr at {digits} significant digits.",
        tolerances=tolerance_records,
        local_radius_bracket=local_bracket,
        diagnostics={
            "stn_diagonal_margin_decimal": _decimal_string(margin, digits=digits),
        },
        created_at_utc=created_at_utc,
        repository=repository,
        software=software,
        source_files=source_files
        or [
            {
                "path": "src/power_ringmin/highprec.py",
                "role": "high-precision fixed-order STN computation",
                "upstream_ringmin_commit": UPSTREAM_RINGMIN_COMMIT,
            },
            {
                "path": "src/power_ringmin/fixed_order_artifact.py",
                "role": "artifact exporter and loader",
            },
        ],
        commands=commands,
        evidence_classification=evidence_classification,
        evidence_scope=evidence_scope,
        evidence_statement=evidence_statement
        or (
            "This artifact records a high-precision numerical fixed-order result; "
            "it is not a global optimum certificate."
        ),
        evidence_checks=evidence_checks or default_checks,
        limitations=limitations
        or [
            "Finite fixed-order computation only.",
            "No global cyclic-order optimality claim.",
            "No theorem for all n.",
        ],
    )


def build_fixed_order_artifact(
    *,
    order: Sequence[Any],
    central_radius: Any,
    result_kind: str,
    objective_status: str,
    feasible: bool,
    primary_backend: str,
    working_precision_digits: int,
    rounding_policy: str,
    tolerances: Sequence[Mapping[str, Any]],
    index_order: Sequence[int] | None = None,
    chain_radius: Any | None = None,
    positions: Sequence[Any] | None = None,
    local_radius_bracket: Mapping[str, Any] | None = None,
    binding_structure: Mapping[str, Any] | None = None,
    diagnostics: Mapping[str, Any] | None = None,
    created_at_utc: str | None = None,
    repository: Mapping[str, Any] | None = None,
    software: Sequence[Mapping[str, Any]] | None = None,
    source_files: Sequence[Mapping[str, Any]] | None = None,
    commands: Sequence[Mapping[str, Any]] | None = None,
    randomness: Mapping[str, Any] | None = None,
    evidence_classification: EvidenceClassification = "numerical_observation",
    evidence_scope: str = "fixed_order_feasibility",
    evidence_statement: str | None = None,
    evidence_checks: Sequence[Mapping[str, Any]] | None = None,
    limitations: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Build a validated v1 fixed-order artifact from explicit values."""
    if result_kind not in RESULT_KINDS:
        raise ValueError(f"unsupported result_kind {result_kind!r}")
    if objective_status not in OBJECTIVE_STATUSES:
        raise ValueError(f"unsupported objective_status {objective_status!r}")
    if primary_backend not in {"float64", "mpmath", "mixed"}:
        raise ValueError(f"unsupported primary_backend {primary_backend!r}")
    if working_precision_digits < 15:
        raise ValueError("working_precision_digits must be at least 15")
    if evidence_classification not in EVIDENCE_CLASSIFICATIONS:
        raise ValueError(f"unsupported evidence classification {evidence_classification!r}")
    if evidence_scope not in EVIDENCE_SCOPES:
        raise ValueError(f"unsupported evidence scope {evidence_scope!r}")

    normalized = _normalize_quadratic_order(order, index_order=index_order)
    n = len(normalized.index_order)

    result: dict[str, Any] = {
        "result_kind": result_kind,
        "objective_status": objective_status,
        "feasible": bool(feasible),
        "central_radius": _numeric_value(central_radius, working_precision_digits),
    }
    if chain_radius is not None:
        result["chain_radius"] = _numeric_value(chain_radius, working_precision_digits)
    if positions is not None:
        if isinstance(positions, (str, bytes)) or len(positions) != n:
            raise ValueError("positions must contain one angle per radius")
        result["positions_rad"] = [
            _decimal_string(position, digits=working_precision_digits) for position in positions
        ]
    if local_radius_bracket is not None:
        result["local_radius_bracket"] = _normalize_local_radius_bracket(
            local_radius_bracket,
            digits=working_precision_digits,
        )
    if binding_structure is not None:
        result["binding_structure"] = _normalize_binding_structure(
            binding_structure,
            normalized.radius_order,
            digits=working_precision_digits,
        )
    if diagnostics is not None:
        result["diagnostics"] = _normalize_diagnostics(diagnostics, digits=working_precision_digits)

    artifact: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "artifact_type": ARTIFACT_TYPE,
        "problem": {
            "project": PROJECT_NAME,
            "radius_model": RADIUS_MODEL,
            "dimension": DIMENSION,
            "constraints": {
                "central_external_tangency": True,
                "peripheral_pairwise_disjoint_interiors": True,
                "all_pairs_checked": True,
            },
        },
        "instance": {
            "n": n,
            "radius_sequence": {
                "kind": "explicit",
                "formula": "k^2",
                "index_base": 1,
                "indices": list(range(1, n + 1)),
                "radii": list(_canonical_square_radii(n)),
            },
        },
        "fixed_order": {
            "order_type": "cyclic",
            "index_order": list(normalized.index_order),
            "radius_order": list(normalized.radius_order),
            "orientation": "counterclockwise",
            "equivalence": "rotation_reflection",
            "angle_anchor": {
                "position_index": 0,
                "angle_decimal": "0.0",
            },
        },
        "result": result,
        "precision": {
            "value_encoding": "decimal_string",
            "primary_backend": primary_backend,
            "working_precision_digits": working_precision_digits,
            "rounding_policy": rounding_policy,
            "tolerances": [_normalize_tolerance(item) for item in tolerances],
        },
        "provenance": {
            "created_at_utc": created_at_utc or _created_at_utc_now(),
            "repository": _repository_record(repository),
            "software": _software_records(software),
            "source_files": _source_file_records(source_files),
            "commands": _command_records(commands),
            "randomness": _randomness_record(randomness),
        },
        "evidence": {
            "classification": evidence_classification,
            "claim": {
                "scope": evidence_scope,
                "statement": evidence_statement
                or "This artifact records a fixed-order numerical result.",
            },
            "checks": _evidence_check_records(evidence_checks),
            "limitations": list(limitations or ["Finite fixed-order computation only."]),
        },
    }
    validate_fixed_order_artifact(artifact)
    return artifact


def validate_fixed_order_artifact(artifact: Mapping[str, Any]) -> None:
    """Raise ``ValueError`` if an artifact violates v1 semantic expectations."""
    if not isinstance(artifact, Mapping):
        raise ValueError("artifact must be a mapping")

    required = {
        "schema_version",
        "artifact_type",
        "problem",
        "instance",
        "fixed_order",
        "result",
        "precision",
        "provenance",
        "evidence",
    }
    missing = sorted(required - set(artifact))
    if missing:
        raise ValueError(f"artifact is missing top-level keys: {missing}")
    if artifact["schema_version"] != SCHEMA_VERSION:
        raise ValueError(f"unsupported schema_version {artifact['schema_version']!r}")
    if artifact["artifact_type"] != ARTIFACT_TYPE:
        raise ValueError(f"unsupported artifact_type {artifact['artifact_type']!r}")

    problem = _expect_mapping(artifact["problem"], "problem")
    if problem.get("project") != PROJECT_NAME:
        raise ValueError("problem.project must be power-ringmin")
    if problem.get("radius_model") != RADIUS_MODEL:
        raise ValueError("problem.radius_model must be quadratic")
    if problem.get("dimension") != DIMENSION:
        raise ValueError("problem.dimension must be 2")
    constraints = _expect_mapping(problem.get("constraints"), "problem.constraints")
    if constraints.get("central_external_tangency") is not True:
        raise ValueError("central_external_tangency must be true")
    if constraints.get("peripheral_pairwise_disjoint_interiors") is not True:
        raise ValueError("peripheral_pairwise_disjoint_interiors must be true")
    if not isinstance(constraints.get("all_pairs_checked"), bool):
        raise ValueError("all_pairs_checked must be boolean")

    instance = _expect_mapping(artifact["instance"], "instance")
    n = instance.get("n")
    if not isinstance(n, int) or n < 3:
        raise ValueError("instance.n must be an integer >= 3")
    radius_sequence = _expect_mapping(instance.get("radius_sequence"), "instance.radius_sequence")
    if radius_sequence.get("kind") != "explicit":
        raise ValueError("radius_sequence.kind must be explicit")
    if radius_sequence.get("formula") != "k^2":
        raise ValueError("radius_sequence.formula must be k^2")
    if radius_sequence.get("index_base") != 1:
        raise ValueError("radius_sequence.index_base must be 1")
    indices = _expect_list(radius_sequence.get("indices"), "radius_sequence.indices")
    radii = _expect_list(radius_sequence.get("radii"), "radius_sequence.radii")
    if tuple(indices) != tuple(range(1, n + 1)):
        raise ValueError("radius_sequence.indices must be consecutive 1..n")
    if len(radii) != n:
        raise ValueError("radius_sequence.radii length must match n")
    for index, radius_text in zip(indices, radii, strict=True):
        _assert_decimal_string(radius_text, f"radius_sequence.radii[{index - 1}]")
        if not _decimal_values_equal(radius_text, index * index):
            raise ValueError(f"radius_sequence radius mismatch for index {index}")

    fixed_order = _expect_mapping(artifact["fixed_order"], "fixed_order")
    if fixed_order.get("order_type") != "cyclic":
        raise ValueError("fixed_order.order_type must be cyclic")
    index_order = tuple(_expect_list(fixed_order.get("index_order"), "fixed_order.index_order"))
    radius_order = tuple(str(value) for value in _expect_list(fixed_order.get("radius_order"), "fixed_order.radius_order"))
    if sorted(index_order) != list(range(1, n + 1)):
        raise ValueError("fixed_order.index_order must be a permutation of 1..n")
    if len(radius_order) != n:
        raise ValueError("fixed_order.radius_order length must match n")
    for position, (index, radius_text) in enumerate(zip(index_order, radius_order, strict=True)):
        if not isinstance(index, int):
            raise ValueError("fixed_order.index_order values must be integers")
        _assert_decimal_string(radius_text, f"fixed_order.radius_order[{position}]")
        if not _decimal_values_equal(radius_text, index * index):
            raise ValueError(
                f"fixed_order radius_order[{position}] does not match index_order value {index}"
            )
    if fixed_order.get("orientation") not in {"counterclockwise", "clockwise", "unoriented"}:
        raise ValueError("fixed_order.orientation has unsupported value")
    if fixed_order.get("equivalence") not in {"rotation", "rotation_reflection", "oriented"}:
        raise ValueError("fixed_order.equivalence has unsupported value")
    anchor = _expect_mapping(fixed_order.get("angle_anchor"), "fixed_order.angle_anchor")
    anchor_index = anchor.get("position_index")
    if not isinstance(anchor_index, int) or not (0 <= anchor_index < n):
        raise ValueError("fixed_order.angle_anchor.position_index is out of range")
    _assert_decimal_string(anchor.get("angle_decimal"), "fixed_order.angle_anchor.angle_decimal")

    result = _expect_mapping(artifact["result"], "result")
    if result.get("result_kind") not in RESULT_KINDS:
        raise ValueError("result.result_kind has unsupported value")
    if result.get("objective_status") not in OBJECTIVE_STATUSES:
        raise ValueError("result.objective_status has unsupported value")
    if not isinstance(result.get("feasible"), bool):
        raise ValueError("result.feasible must be boolean")
    _validate_numeric_value(result.get("central_radius"), "result.central_radius")
    if "chain_radius" in result:
        _validate_numeric_value(result["chain_radius"], "result.chain_radius")
    if "positions_rad" in result:
        positions = _expect_list(result["positions_rad"], "result.positions_rad")
        if len(positions) != n:
            raise ValueError("result.positions_rad length must match n")
        for i, position in enumerate(positions):
            _assert_decimal_string(position, f"result.positions_rad[{i}]")
    if "local_radius_bracket" in result:
        _validate_local_radius_bracket(result["local_radius_bracket"])
    if "binding_structure" in result:
        _validate_binding_structure(result["binding_structure"], radius_order)
    if "diagnostics" in result:
        _validate_diagnostics(result["diagnostics"])

    precision = _expect_mapping(artifact["precision"], "precision")
    if precision.get("value_encoding") != "decimal_string":
        raise ValueError("precision.value_encoding must be decimal_string")
    if precision.get("primary_backend") not in {"float64", "mpmath", "mixed"}:
        raise ValueError("precision.primary_backend has unsupported value")
    digits = precision.get("working_precision_digits")
    if not isinstance(digits, int) or digits < 15:
        raise ValueError("precision.working_precision_digits must be integer >= 15")
    if not isinstance(precision.get("rounding_policy"), str) or not precision["rounding_policy"]:
        raise ValueError("precision.rounding_policy must be non-empty")
    tolerances = _expect_list(precision.get("tolerances"), "precision.tolerances")
    if not tolerances:
        raise ValueError("precision.tolerances must be non-empty")
    for i, tolerance in enumerate(tolerances):
        _validate_tolerance(tolerance, f"precision.tolerances[{i}]")

    provenance = _expect_mapping(artifact["provenance"], "provenance")
    _validate_repository(provenance.get("repository"))
    if not isinstance(provenance.get("created_at_utc"), str) or not provenance["created_at_utc"]:
        raise ValueError("provenance.created_at_utc must be non-empty string")
    if not _expect_list(provenance.get("software"), "provenance.software"):
        raise ValueError("provenance.software must be non-empty")
    if not _expect_list(provenance.get("source_files"), "provenance.source_files"):
        raise ValueError("provenance.source_files must be non-empty")
    if not _expect_list(provenance.get("commands"), "provenance.commands"):
        raise ValueError("provenance.commands must be non-empty")
    _expect_mapping(provenance.get("randomness"), "provenance.randomness")

    evidence = _expect_mapping(artifact["evidence"], "evidence")
    if evidence.get("classification") not in EVIDENCE_CLASSIFICATIONS:
        raise ValueError("evidence.classification has unsupported value")
    claim = _expect_mapping(evidence.get("claim"), "evidence.claim")
    if claim.get("scope") not in EVIDENCE_SCOPES:
        raise ValueError("evidence.claim.scope has unsupported value")
    if not isinstance(claim.get("statement"), str) or not claim["statement"]:
        raise ValueError("evidence.claim.statement must be non-empty")
    checks = _expect_list(evidence.get("checks"), "evidence.checks")
    if not checks:
        raise ValueError("evidence.checks must be non-empty")
    for i, check in enumerate(checks):
        _validate_evidence_check(check, f"evidence.checks[{i}]")
    _expect_list(evidence.get("limitations"), "evidence.limitations")


def load_fixed_order_artifact(path: str | Path) -> FixedOrderArtifact:
    """Load and validate a v1 fixed-order artifact from JSON."""
    return loads_fixed_order_artifact(Path(path).read_text(encoding="utf-8"))


def loads_fixed_order_artifact(text: str) -> FixedOrderArtifact:
    """Load and validate a v1 fixed-order artifact from a JSON string."""
    payload = json.loads(text)
    if not isinstance(payload, dict):
        raise ValueError("fixed-order artifact JSON must contain an object")
    return FixedOrderArtifact.from_mapping(payload)


def dump_fixed_order_artifact(
    artifact: Mapping[str, Any] | FixedOrderArtifact,
    path: str | Path,
    *,
    indent: int = 2,
) -> None:
    """Validate and write a v1 fixed-order artifact as UTF-8 JSON."""
    Path(path).write_text(dumps_fixed_order_artifact(artifact, indent=indent), encoding="utf-8")


def dumps_fixed_order_artifact(
    artifact: Mapping[str, Any] | FixedOrderArtifact,
    *,
    indent: int = 2,
) -> str:
    """Validate and serialize a v1 fixed-order artifact."""
    data = artifact.to_dict() if isinstance(artifact, FixedOrderArtifact) else copy.deepcopy(dict(artifact))
    validate_fixed_order_artifact(data)
    return json.dumps(data, indent=indent, sort_keys=False) + "\n"


def verifier_payload_from_artifact(artifact: Mapping[str, Any] | FixedOrderArtifact) -> dict[str, Any]:
    """Return the minimal standalone-verifier payload for a v1 artifact."""
    loaded = artifact if isinstance(artifact, FixedOrderArtifact) else FixedOrderArtifact.from_mapping(artifact)
    return loaded.to_verifier_payload()


artifact_from_full_result = export_full_result_artifact
artifact_from_highprec_result = export_highprec_artifact


@dataclass(frozen=True)
class _NormalizedOrder:
    index_order: tuple[int, ...]
    radius_order: tuple[str, ...]


def _normalize_quadratic_order(
    order: Sequence[Any],
    *,
    index_order: Sequence[int] | None,
) -> _NormalizedOrder:
    if isinstance(order, (str, bytes)):
        raise ValueError("order must be a sequence of radius values, not a string")
    radii = tuple(order)
    if len(radii) < 3:
        raise ValueError("fixed-order artifacts require at least three radii")
    if index_order is None:
        inferred = tuple(_infer_square_index(value) for value in radii)
    else:
        inferred = tuple(int(value) for value in index_order)
        if len(inferred) != len(radii):
            raise ValueError("index_order length must match order length")
        for radius, index in zip(radii, inferred, strict=True):
            if _infer_square_index(radius) != index:
                raise ValueError(f"radius {radius!r} does not match index {index}")
    n = len(radii)
    if sorted(inferred) != list(range(1, n + 1)):
        raise ValueError("order must contain exactly the quadratic radii 1^2..n^2")
    return _NormalizedOrder(
        index_order=inferred,
        radius_order=tuple(str(index * index) for index in inferred),
    )


def _infer_square_index(value: Any) -> int:
    try:
        numeric = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"radius value is not numeric: {value!r}") from exc
    if not math.isfinite(numeric) or numeric <= 0:
        raise ValueError(f"radius value must be positive and finite: {value!r}")
    index = int(round(math.sqrt(numeric)))
    if index < 1 or not math.isclose(numeric, index * index, rel_tol=0.0, abs_tol=1e-9):
        raise ValueError(f"radius value is not a recognized quadratic radius: {value!r}")
    return index


def _canonical_square_radii(n: int) -> tuple[str, ...]:
    return tuple(str(index * index) for index in range(1, n + 1))


def _numeric_value(value: Any, digits: int) -> dict[str, Any]:
    return {
        "decimal": _decimal_string(value, digits=digits),
        "encoding": "decimal_string",
        "source_precision_digits": digits,
    }


def _decimal_string(value: Any, *, digits: int | None = None) -> str:
    if isinstance(value, bool):
        raise ValueError("boolean values are not numeric decimal strings")
    if isinstance(value, str):
        text = value.strip()
    elif isinstance(value, int):
        text = str(value)
    elif isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError(f"float must be finite: {value!r}")
        text = str(int(value)) if value.is_integer() else repr(value)
    else:
        mp_value = mp.mpf(value)
        text = mp.nstr(mp_value, n=digits or mp.mp.dps)
    if text.startswith("+"):
        text = text[1:]
    _assert_decimal_string(text, "decimal value")
    return text


def _assert_decimal_string(value: Any, name: str) -> None:
    if not isinstance(value, str) or DECIMAL_STRING_RE.fullmatch(value) is None:
        raise ValueError(f"{name} must be a decimal string, got {value!r}")
    mp.mpf(value)


def _decimal_values_equal(left: Any, right: Any) -> bool:
    return mp.mpf(str(left)) == mp.mpf(str(right))


def _binding_pair_to_json(binding: BindingPair, *, digits: int) -> dict[str, Any]:
    return {
        "i": binding.i,
        "j": binding.j,
        "radius_i": _decimal_string(binding.radius_i, digits=digits),
        "radius_j": _decimal_string(binding.radius_j, digits=digits),
        "kind": binding.kind,
        "slack_decimal": _decimal_string(binding.slack, digits=digits),
    }


def _normalize_binding_structure(
    binding_structure: Mapping[str, Any],
    radius_order: tuple[str, ...],
    *,
    digits: int,
) -> dict[str, Any]:
    source = _expect_mapping(binding_structure, "binding_structure")
    return {
        "essential_tight_pairs": [
            _normalize_binding_pair(pair, radius_order, digits=digits)
            for pair in source.get("essential_tight_pairs", [])
        ],
        "recovered_tight_pairs": [
            _normalize_binding_pair(pair, radius_order, digits=digits)
            for pair in source.get("recovered_tight_pairs", [])
        ],
        "floating_radii": [
            _decimal_string(radius, digits=digits) for radius in source.get("floating_radii", [])
        ],
    }


def _normalize_binding_pair(
    pair: Mapping[str, Any],
    radius_order: tuple[str, ...],
    *,
    digits: int,
) -> dict[str, Any]:
    source = _expect_mapping(pair, "binding pair")
    i = int(source["i"])
    j = int(source["j"])
    if not (0 <= i < j < len(radius_order)):
        raise ValueError("binding pair indices must satisfy 0 <= i < j < n")
    radius_i = _decimal_string(source.get("radius_i", radius_order[i]), digits=digits)
    radius_j = _decimal_string(source.get("radius_j", radius_order[j]), digits=digits)
    if not _decimal_values_equal(radius_i, radius_order[i]):
        raise ValueError("binding pair radius_i does not match fixed order")
    if not _decimal_values_equal(radius_j, radius_order[j]):
        raise ValueError("binding pair radius_j does not match fixed order")
    kind = source["kind"]
    if kind not in {"forward", "wrap"}:
        raise ValueError(f"unsupported binding pair kind {kind!r}")
    return {
        "i": i,
        "j": j,
        "radius_i": radius_i,
        "radius_j": radius_j,
        "kind": kind,
        "slack_decimal": _decimal_string(source["slack_decimal"], digits=digits),
    }


def _normalize_local_radius_bracket(
    bracket: Mapping[str, Any],
    *,
    digits: int,
) -> dict[str, Any]:
    source = _expect_mapping(bracket, "local_radius_bracket")
    return {
        "eta_decimal": _decimal_string(source["eta_decimal"], digits=digits),
        "lower_radius_feasible": bool(source["lower_radius_feasible"]),
        "claimed_radius_feasible": bool(source["claimed_radius_feasible"]),
        "upper_radius_feasible": bool(source["upper_radius_feasible"]),
        "method": str(source["method"]),
    }


def _normalize_diagnostics(diagnostics: Mapping[str, Any], *, digits: int) -> dict[str, Any]:
    source = _expect_mapping(diagnostics, "diagnostics")
    allowed = {
        "stn_diagonal_margin_decimal",
        "min_pair_margin_decimal",
        "min_order_margin_decimal",
    }
    normalized: dict[str, Any] = {}
    for key, value in source.items():
        if key not in allowed:
            raise ValueError(f"unsupported diagnostic key {key!r}")
        normalized[key] = _decimal_string(value, digits=digits)
    return normalized


def _normalize_tolerance(tolerance: Mapping[str, Any]) -> dict[str, Any]:
    source = _expect_mapping(tolerance, "tolerance")
    tolerance_type = source["tolerance_type"]
    if tolerance_type not in {"absolute", "relative", "other"}:
        raise ValueError(f"unsupported tolerance_type {tolerance_type!r}")
    value = source.get("value_decimal", source.get("value"))
    return {
        "name": str(source["name"]),
        "value_decimal": _decimal_string(value),
        "tolerance_type": tolerance_type,
        "applies_to": str(source["applies_to"]),
    }


def _repository_record(repository: Mapping[str, Any] | None) -> dict[str, Any]:
    if repository is not None:
        source = _expect_mapping(repository, "repository")
        return {
            "name": PROJECT_NAME,
            "git_commit": source.get("git_commit"),
            "git_dirty": bool(source.get("git_dirty", True)),
            **({"notes": str(source["notes"])} if "notes" in source else {}),
        }
    return detect_repository_state()


def detect_repository_state(cwd: str | Path | None = None) -> dict[str, Any]:
    """Best-effort read-only Git provenance for generated artifacts."""
    root = Path.cwd() if cwd is None else Path(cwd)

    def run_git(args: list[str]) -> str:
        completed = subprocess.run(
            ["git", *args],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        )
        return completed.stdout.strip()

    try:
        commit = run_git(["rev-parse", "HEAD"])
        status = run_git(["status", "--short"])
    except Exception as exc:  # pragma: no cover - depends on local Git availability
        return {
            "name": PROJECT_NAME,
            "git_commit": None,
            "git_dirty": True,
            "notes": f"Git provenance unavailable: {exc}",
        }
    return {
        "name": PROJECT_NAME,
        "git_commit": commit if re.fullmatch(r"[0-9a-f]{40}", commit) else None,
        "git_dirty": bool(status),
    }


def _software_records(software: Sequence[Mapping[str, Any]] | None) -> list[dict[str, Any]]:
    if software is not None:
        return [
            {"name": str(item["name"]), "version": str(item["version"]), "role": str(item["role"])}
            for item in software
        ]
    return [
        {
            "name": "Python",
            "version": platform.python_version(),
            "role": "runtime",
        },
        {
            "name": "mpmath",
            "version": getattr(mp, "__version__", "unknown"),
            "role": "high-precision arithmetic",
        },
        {
            "name": PROJECT_NAME,
            "version": _package_version(),
            "role": "artifact exporter",
        },
    ]


def _package_version() -> str:
    try:
        from importlib.metadata import version

        return version(PROJECT_NAME)
    except Exception:  # pragma: no cover - source tree may be uninstalled
        return "0.1.0"


def _source_file_records(source_files: Sequence[Mapping[str, Any]] | None) -> list[dict[str, Any]]:
    items = list(
        source_files
        or [
            {
                "path": "src/power_ringmin/fixed_order_artifact.py",
                "role": "artifact exporter and loader",
            }
        ]
    )
    records: list[dict[str, Any]] = []
    for item in items:
        record = {
            "path": str(item["path"]),
            "role": str(item["role"]),
        }
        if "upstream_ringmin_commit" in item:
            record["upstream_ringmin_commit"] = str(item["upstream_ringmin_commit"])
        records.append(record)
    return records


def _command_records(commands: Sequence[Mapping[str, Any]] | None) -> list[dict[str, Any]]:
    if commands is None:
        return [
            {
                "command": "not recorded (package API call)",
                "cwd": str(Path.cwd()),
                "result": "informational",
                "output_summary": "Artifact was constructed through the package exporter API.",
            }
        ]
    records: list[dict[str, Any]] = []
    for item in commands:
        record = {
            "command": str(item["command"]),
            "cwd": str(item["cwd"]),
            "result": str(item["result"]),
        }
        if "output_summary" in item:
            record["output_summary"] = str(item["output_summary"])
        records.append(record)
    return records


def _randomness_record(randomness: Mapping[str, Any] | None) -> dict[str, Any]:
    if randomness is None:
        return {"used": False, "seeds": []}
    source = _expect_mapping(randomness, "randomness")
    return {
        "used": bool(source["used"]),
        "seeds": list(source.get("seeds", [])),
    }


def _evidence_check_records(checks: Sequence[Mapping[str, Any]] | None) -> list[dict[str, Any]]:
    if checks is None:
        return [
            {
                "check_id": "EV-001",
                "classification": "verified_fact",
                "method": "artifact construction validation",
                "result": "pass",
                "output_summary": "Exporter constructed a semantically valid v1 artifact.",
                "limitations": "Exporter validation is not mathematical proof.",
            }
        ]
    records: list[dict[str, Any]] = []
    for item in checks:
        record = {
            "check_id": str(item["check_id"]),
            "classification": str(item["classification"]),
            "method": str(item["method"]),
            "result": str(item["result"]),
        }
        for key in ("command", "output_summary", "limitations"):
            if key in item:
                record[key] = str(item[key])
        records.append(record)
    return records


def _created_at_utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _expect_mapping(value: Any, name: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ValueError(f"{name} must be a mapping")
    return value


def _expect_list(value: Any, name: str) -> list[Any]:
    if not isinstance(value, list):
        raise ValueError(f"{name} must be a list")
    return value


def _validate_numeric_value(value: Any, name: str) -> None:
    source = _expect_mapping(value, name)
    if source.get("encoding") != "decimal_string":
        raise ValueError(f"{name}.encoding must be decimal_string")
    _assert_decimal_string(source.get("decimal"), f"{name}.decimal")
    digits = source.get("source_precision_digits")
    if "source_precision_digits" in source and (not isinstance(digits, int) or digits < 15):
        raise ValueError(f"{name}.source_precision_digits must be integer >= 15")


def _validate_local_radius_bracket(value: Any) -> None:
    source = _expect_mapping(value, "result.local_radius_bracket")
    _assert_decimal_string(source.get("eta_decimal"), "local_radius_bracket.eta_decimal")
    for key in ("lower_radius_feasible", "claimed_radius_feasible", "upper_radius_feasible"):
        if not isinstance(source.get(key), bool):
            raise ValueError(f"local_radius_bracket.{key} must be boolean")
    if not isinstance(source.get("method"), str) or not source["method"]:
        raise ValueError("local_radius_bracket.method must be non-empty")


def _validate_binding_structure(value: Any, radius_order: tuple[str, ...]) -> None:
    source = _expect_mapping(value, "result.binding_structure")
    for key in ("essential_tight_pairs", "recovered_tight_pairs", "floating_radii"):
        _expect_list(source.get(key), f"binding_structure.{key}")
    for key in ("essential_tight_pairs", "recovered_tight_pairs"):
        for pair in source[key]:
            _normalize_binding_pair(pair, radius_order, digits=80)
    for i, radius in enumerate(source["floating_radii"]):
        _assert_decimal_string(radius, f"binding_structure.floating_radii[{i}]")


def _validate_diagnostics(value: Any) -> None:
    source = _expect_mapping(value, "result.diagnostics")
    for key, item in source.items():
        if key not in {"stn_diagonal_margin_decimal", "min_pair_margin_decimal", "min_order_margin_decimal"}:
            raise ValueError(f"unsupported diagnostic key {key!r}")
        _assert_decimal_string(item, f"diagnostics.{key}")


def _validate_tolerance(value: Any, name: str) -> None:
    source = _expect_mapping(value, name)
    if not isinstance(source.get("name"), str) or not source["name"]:
        raise ValueError(f"{name}.name must be non-empty")
    _assert_decimal_string(source.get("value_decimal"), f"{name}.value_decimal")
    if source.get("tolerance_type") not in {"absolute", "relative", "other"}:
        raise ValueError(f"{name}.tolerance_type has unsupported value")
    if not isinstance(source.get("applies_to"), str) or not source["applies_to"]:
        raise ValueError(f"{name}.applies_to must be non-empty")


def _validate_repository(value: Any) -> None:
    source = _expect_mapping(value, "provenance.repository")
    if source.get("name") != PROJECT_NAME:
        raise ValueError("provenance.repository.name must be power-ringmin")
    commit = source.get("git_commit")
    if commit is not None and (not isinstance(commit, str) or not re.fullmatch(r"[0-9a-f]{40}", commit)):
        raise ValueError("provenance.repository.git_commit must be null or a 40-character hash")
    if not isinstance(source.get("git_dirty"), bool):
        raise ValueError("provenance.repository.git_dirty must be boolean")


def _validate_evidence_check(value: Any, name: str) -> None:
    source = _expect_mapping(value, name)
    if not isinstance(source.get("check_id"), str) or not re.fullmatch(r"EV-[0-9]{3}", source["check_id"]):
        raise ValueError(f"{name}.check_id must match EV-###")
    if source.get("classification") not in EVIDENCE_CLASSIFICATIONS:
        raise ValueError(f"{name}.classification has unsupported value")
    if not isinstance(source.get("method"), str) or not source["method"]:
        raise ValueError(f"{name}.method must be non-empty")
    if source.get("result") not in {"pass", "fail", "not_run", "informational"}:
        raise ValueError(f"{name}.result has unsupported value")


__all__ = [
    "ARTIFACT_TYPE",
    "EVIDENCE_CLASSIFICATIONS",
    "SCHEMA_VERSION",
    "FixedOrderArtifact",
    "artifact_from_full_result",
    "artifact_from_highprec_result",
    "build_fixed_order_artifact",
    "detect_repository_state",
    "dump_fixed_order_artifact",
    "dumps_fixed_order_artifact",
    "export_full_result_artifact",
    "export_highprec_artifact",
    "load_fixed_order_artifact",
    "loads_fixed_order_artifact",
    "validate_fixed_order_artifact",
    "verifier_payload_from_artifact",
]
