"""Deterministic verification of checked finite certificate artifacts.

This command is intended for local review and CI. It does not generate
certificates; it reloads checked artifacts, validates their structural JSON
Schema contracts, and reruns the semantic interval validators.
"""

from __future__ import annotations

import argparse
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
import json
from pathlib import Path
import re
import sys
from typing import Any

from power_ringmin.finite_results import (
    load_finite_results_summary,
)
from power_ringmin.interval_verifier import (
    MPMathIntervalAngularOracle,
    assert_fixed_order_interval_bracket_verified,
)
from power_ringmin.small_n_interval_certificate import (
    load_small_n_interval_certificate_artifact,
)

COMMAND_NAME = "power-ringmin-verify-checked-artifacts"
DEFAULT_CERTIFICATE_GLOB = "examples/small_n_interval_certificate_n*.json"
DEFAULT_SUMMARY_PATH = Path("examples/finite_results_summary_n3_n6.json")
SMALL_N_SCHEMA_PATH = Path("schemas/small_n_interval_certificate.schema.json")
FINITE_RESULTS_SCHEMA_PATH = Path("schemas/finite_results_summary.schema.json")
_CERTIFICATE_N_RE = re.compile(r"small_n_interval_certificate_n([0-9]+)\.json$")


@dataclass(frozen=True)
class CheckedArtifactVerification:
    """Summary of checked finite artifact verification."""

    certificate_paths: tuple[Path, ...]
    summary_path: Path
    n_values: tuple[int, ...]
    local_bracket_count: int

    @property
    def certificate_count(self) -> int:
        return len(self.certificate_paths)


def discover_checked_certificate_paths(
    *,
    base_dir: str | Path = ".",
    pattern: str = DEFAULT_CERTIFICATE_GLOB,
) -> tuple[Path, ...]:
    """Return checked small-n certificate paths sorted by ``n`` then path."""

    root = Path(base_dir)
    paths = [path for path in root.glob(pattern) if path.is_file()]
    return tuple(sorted(paths, key=_certificate_sort_key))


def verify_checked_artifacts(
    *,
    certificate_paths: Sequence[str | Path] | None = None,
    certificate_glob: str = DEFAULT_CERTIFICATE_GLOB,
    summary_path: str | Path = DEFAULT_SUMMARY_PATH,
    schema_dir: str | Path = ".",
    base_dir: str | Path = ".",
) -> CheckedArtifactVerification:
    """Validate checked finite certificate and summary artifacts.

    Structural JSON Schema validation is performed first. Semantic validation
    is then delegated to the package validators, with an explicit second pass
    over embedded local interval brackets for review visibility.
    """

    root = Path(base_dir)
    paths = (
        tuple(Path(path) for path in certificate_paths)
        if certificate_paths is not None
        else discover_checked_certificate_paths(base_dir=root, pattern=certificate_glob)
    )
    if not paths:
        raise ValueError("no checked small-n interval certificate artifacts were found")

    small_n_schema = _load_schema(Path(schema_dir) / SMALL_N_SCHEMA_PATH)
    finite_results_schema = _load_schema(Path(schema_dir) / FINITE_RESULTS_SCHEMA_PATH)

    n_values: list[int] = []
    local_bracket_count = 0
    for path in paths:
        payload = _load_json(path)
        _validate_with_json_schema(payload, small_n_schema, schema_name=SMALL_N_SCHEMA_PATH.as_posix())
        loaded = load_small_n_interval_certificate_artifact(path)
        artifact = loaded.to_dict()
        n_values.append(loaded.n)
        local_bracket_count += _reverify_embedded_local_brackets(artifact)

    summary_payload = _load_json(summary_path)
    _validate_with_json_schema(
        summary_payload,
        finite_results_schema,
        schema_name=FINITE_RESULTS_SCHEMA_PATH.as_posix(),
    )
    summary = load_finite_results_summary(summary_path, base_dir=root).to_dict()
    _validate_summary_sources_match_certificates(summary, paths, base_dir=root)

    return CheckedArtifactVerification(
        certificate_paths=tuple(paths),
        summary_path=Path(summary_path),
        n_values=tuple(n_values),
        local_bracket_count=local_bracket_count,
    )


def build_parser() -> argparse.ArgumentParser:
    """Build the checked-artifact verifier CLI parser."""

    parser = argparse.ArgumentParser(
        prog=COMMAND_NAME,
        description=(
            "Validate checked finite small-n certificate artifacts and the "
            "derived finite-results summary. This command does not generate "
            "new certificates."
        ),
    )
    parser.add_argument(
        "certificates",
        nargs="*",
        type=Path,
        help=(
            "checked small-n certificate path(s); when omitted, "
            f"{DEFAULT_CERTIFICATE_GLOB!r} is discovered"
        ),
    )
    parser.add_argument(
        "--certificate-glob",
        default=DEFAULT_CERTIFICATE_GLOB,
        help=f"glob used when no explicit certificate paths are supplied (default: {DEFAULT_CERTIFICATE_GLOB})",
    )
    parser.add_argument(
        "--summary",
        type=Path,
        default=DEFAULT_SUMMARY_PATH,
        help=f"finite-results summary artifact path (default: {DEFAULT_SUMMARY_PATH.as_posix()})",
    )
    parser.add_argument(
        "--schema-dir",
        type=Path,
        default=Path("."),
        help="repository root containing the schemas/ directory",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run checked-artifact verification."""

    parser = build_parser()
    raw_argv = list(sys.argv[1:] if argv is None else argv)
    args = parser.parse_args(raw_argv)
    try:
        result = verify_checked_artifacts(
            certificate_paths=args.certificates or None,
            certificate_glob=args.certificate_glob,
            summary_path=args.summary,
            schema_dir=args.schema_dir,
        )
    except (OSError, RuntimeError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

    n_text = ",".join(str(n) for n in result.n_values)
    print(
        "verified checked artifacts "
        f"certificates={result.certificate_count} "
        f"local_brackets={result.local_bracket_count} "
        f"summary={result.summary_path.as_posix()} "
        f"summary_n_values={n_text}"
    )
    return 0


def _certificate_sort_key(path: Path) -> tuple[int, str]:
    match = _CERTIFICATE_N_RE.search(path.name)
    if match is None:
        return (10**9, path.as_posix())
    return (int(match.group(1)), path.as_posix())


def _load_schema(path: Path) -> dict[str, Any]:
    payload = _load_json(path)
    if not isinstance(payload, dict):
        raise ValueError(f"schema {path.as_posix()} must contain a JSON object")
    return payload


def _load_json(path: str | Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _validate_with_json_schema(
    payload: Any,
    schema: Mapping[str, Any],
    *,
    schema_name: str,
) -> None:
    try:
        from jsonschema import Draft202012Validator
    except ImportError as exc:  # pragma: no cover - exercised only without test deps
        raise RuntimeError(
            "JSON Schema validation requires the test dependency 'jsonschema'; "
            "install with power-ringmin[test]"
        ) from exc

    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(payload), key=lambda item: item.json_path)
    if errors:
        first = errors[0]
        raise ValueError(f"{schema_name} validation failed at {first.json_path}: {first.message}")


def _reverify_embedded_local_brackets(artifact: Mapping[str, Any]) -> int:
    local_brackets = artifact.get("local_brackets")
    if not isinstance(local_brackets, list):
        raise ValueError("local_brackets must be a list")
    for index, record in enumerate(local_brackets):
        if not isinstance(record, Mapping):
            raise ValueError(f"local_brackets[{index}] must be a mapping")
        metadata = record.get("theta_interval_backend")
        if not isinstance(metadata, Mapping):
            raise ValueError(f"local_brackets[{index}].theta_interval_backend must be a mapping")
        oracle = _oracle_from_backend_metadata(metadata)
        assert_fixed_order_interval_bracket_verified(record, oracle=oracle)
    return len(local_brackets)


def _oracle_from_backend_metadata(metadata: Mapping[str, Any]) -> MPMathIntervalAngularOracle:
    if metadata.get("backend") != "mpmath_iv_guarded_atan2_v1":
        raise ValueError("only mpmath_iv_guarded_atan2_v1 local records are supported")
    digits = metadata.get("precision_digits")
    if isinstance(digits, bool) or not isinstance(digits, int):
        raise ValueError("theta_interval_backend.precision_digits must be an integer")
    guard = metadata.get("guard_decimal")
    if guard is not None and not isinstance(guard, str):
        raise ValueError("theta_interval_backend.guard_decimal must be a string")
    return MPMathIntervalAngularOracle(digits=digits, guard_decimal=guard)


def _validate_summary_sources_match_certificates(
    summary: Mapping[str, Any],
    certificate_paths: Sequence[Path],
    *,
    base_dir: Path,
) -> None:
    sources = summary.get("source_certificates")
    if not isinstance(sources, list):
        raise ValueError("finite-results summary source_certificates must be a list")
    actual = tuple(str(source.get("path")) for source in sources if isinstance(source, Mapping))
    expected = tuple(_display_path(path, base_dir=base_dir) for path in certificate_paths)
    if actual != expected:
        raise ValueError(
            "finite-results summary sources do not match discovered checked certificates: "
            f"expected={expected}, actual={actual}"
        )


def _display_path(path: Path, *, base_dir: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(base_dir.resolve()).as_posix()
    except ValueError:
        return resolved.as_posix()


__all__ = [
    "COMMAND_NAME",
    "DEFAULT_CERTIFICATE_GLOB",
    "DEFAULT_SUMMARY_PATH",
    "CheckedArtifactVerification",
    "build_parser",
    "discover_checked_certificate_paths",
    "main",
    "verify_checked_artifacts",
]


if __name__ == "__main__":
    raise SystemExit(main())
