from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from power_ringmin.finite_results import validate_finite_results_summary_artifact
from power_ringmin.small_n_interval_certificate import (
    validate_small_n_interval_certificate_artifact,
)


CHECKED_CERTIFICATE_PATHS = (
    Path("examples/small_n_interval_certificate_n3.json"),
    Path("examples/small_n_interval_certificate_n4.json"),
    Path("examples/small_n_interval_certificate_n5.json"),
    Path("examples/small_n_interval_certificate_n6.json"),
)
CHECKED_SUMMARY_PATH = Path("examples/finite_results_summary_n3_n6.json")


def test_checked_small_n_certificate_examples_validate_against_json_schema() -> None:
    schema = _load_schema(Path("schemas/small_n_interval_certificate.schema.json"))
    validator = Draft202012Validator(schema)

    for path in CHECKED_CERTIFICATE_PATHS:
        payload = json.loads(path.read_text(encoding="utf-8"))
        validator.validate(payload)


def test_checked_finite_results_summary_validates_against_json_schema() -> None:
    schema = _load_schema(Path("schemas/finite_results_summary.schema.json"))
    payload = json.loads(CHECKED_SUMMARY_PATH.read_text(encoding="utf-8"))

    Draft202012Validator(schema).validate(payload)


def test_schema_validation_is_structural_not_semantic_for_small_n_certificate() -> None:
    schema = _load_schema(Path("schemas/small_n_interval_certificate.schema.json"))
    payload = json.loads(CHECKED_CERTIFICATE_PATHS[0].read_text(encoding="utf-8"))
    structurally_valid_but_semantically_stale = copy.deepcopy(payload)
    structurally_valid_but_semantically_stale["result"]["global_upper_bound"][
        "radius_decimal"
    ] = "1"

    Draft202012Validator(schema).validate(structurally_valid_but_semantically_stale)
    with pytest.raises(ValueError, match="global_upper_bound"):
        validate_small_n_interval_certificate_artifact(
            structurally_valid_but_semantically_stale
        )


def test_schema_validation_is_structural_not_semantic_for_finite_summary() -> None:
    schema = _load_schema(Path("schemas/finite_results_summary.schema.json"))
    payload = json.loads(CHECKED_SUMMARY_PATH.read_text(encoding="utf-8"))
    structurally_valid_but_semantically_stale = copy.deepcopy(payload)
    structurally_valid_but_semantically_stale["source_certificates"][0][
        "content_sha256"
    ] = "0" * 64

    Draft202012Validator(schema).validate(structurally_valid_but_semantically_stale)
    with pytest.raises(ValueError, match="source_certificates"):
        validate_finite_results_summary_artifact(
            structurally_valid_but_semantically_stale
        )


def _load_schema(path: Path) -> dict:
    schema = json.loads(path.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return schema
