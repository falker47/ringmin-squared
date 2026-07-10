"""Command-line exporter for fixed-order result artifacts."""

from __future__ import annotations

import argparse
from collections.abc import Sequence
import math
from pathlib import Path
import shlex
import sys
from typing import Any, Literal

from power_ringmin.evaluator import full_radius
from power_ringmin.fixed_order_artifact import (
    UPSTREAM_RINGMIN_COMMIT,
    dump_fixed_order_artifact,
    export_full_result_artifact,
    export_highprec_artifact,
)
from power_ringmin.highprec import full_radius_mp, recover_positions_mp

Backend = Literal["float64", "mpmath"]


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the fixed-order exporter."""
    parser = argparse.ArgumentParser(
        description="Export a v1 fixed-order artifact from one explicit cyclic order.",
    )
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument(
        "--order",
        help="comma-separated quadratic radius order, e.g. 16,1,9,4",
    )
    source.add_argument(
        "--index-order",
        help="comma-separated quadratic index order, e.g. 4,1,3,2",
    )
    parser.add_argument(
        "-o",
        "--output",
        required=True,
        type=Path,
        help="path to write the v1 fixed-order JSON artifact",
    )
    parser.add_argument(
        "--backend",
        choices=("float64", "mpmath"),
        default="float64",
        help="fixed-order computation backend (default: float64)",
    )
    parser.add_argument(
        "--digits",
        type=int,
        default=80,
        help="mpmath working precision digits when --backend=mpmath (default: 80)",
    )
    parser.add_argument(
        "--local-radius-eta",
        help="optional positive local bracket radius offset for --backend=mpmath",
    )
    parser.add_argument(
        "--created-at-utc",
        help="optional UTC timestamp to record in artifact provenance",
    )
    return parser


def export_artifact_for_order(
    order: Sequence[int],
    *,
    backend: Backend,
    output: Path,
    argv_for_provenance: Sequence[str],
    digits: int = 80,
    local_radius_eta: str | None = None,
    created_at_utc: str | None = None,
    command_name: str = "power-ringmin-export-fixed-order",
    extra_source_files: Sequence[dict[str, str]] | None = None,
) -> dict[str, Any]:
    """Compute one fixed-order result and write its v1 artifact."""
    command = _command_record(
        argv_for_provenance,
        backend=backend,
        output=output,
        n=len(order),
        command_name=command_name,
    )
    source_files = list(extra_source_files or []) + _source_files_for_backend(backend)
    evidence_statement = (
        "This artifact was exported from one explicit fixed cyclic order; "
        "it is not a global optimum certificate."
    )

    if backend == "float64":
        result = full_radius(order)
        artifact = export_full_result_artifact(
            result,
            created_at_utc=created_at_utc,
            source_files=source_files,
            commands=[command],
            evidence_statement=evidence_statement,
        )
    else:
        radius = full_radius_mp(list(order), digits=digits)
        positions = recover_positions_mp(list(order), radius, digits=digits)
        artifact = export_highprec_artifact(
            order,
            radius,
            positions=positions,
            digits=digits,
            local_radius_eta=local_radius_eta,
            created_at_utc=created_at_utc,
            source_files=source_files,
            commands=[command],
            evidence_statement=evidence_statement,
        )

    if artifact["result"]["feasible"] is not True:
        raise ValueError(
            "exported fixed-order radius is not feasible at the requested "
            "precision; increase --digits"
        )
    dump_fixed_order_artifact(artifact, output)
    return artifact


def main(argv: Sequence[str] | None = None) -> int:
    """Run the fixed-order artifact export CLI."""
    parser = build_parser()
    raw_argv = list(sys.argv[1:] if argv is None else argv)
    args = parser.parse_args(raw_argv)

    if args.backend == "mpmath" and args.digits < 30:
        parser.error("--digits must be at least 30 when --backend=mpmath")
    if args.backend == "float64" and args.local_radius_eta is not None:
        parser.error("--local-radius-eta requires --backend=mpmath")

    try:
        order = _explicit_order(args.order, args.index_order)
        artifact = export_artifact_for_order(
            order,
            backend=args.backend,
            output=args.output,
            argv_for_provenance=raw_argv,
            digits=args.digits,
            local_radius_eta=args.local_radius_eta,
            created_at_utc=args.created_at_utc,
        )
    except ValueError as exc:
        parser.error(str(exc))

    radius = artifact["result"]["central_radius"]["decimal"]
    print(
        f"wrote {args.output} n={len(order)} backend={args.backend} "
        f"R={radius}"
    )
    return 0


def _explicit_order(raw_order: str | None, raw_index_order: str | None) -> tuple[int, ...]:
    if raw_order is not None:
        return _parse_radius_order(raw_order)
    if raw_index_order is not None:
        indices = _parse_index_order(raw_index_order)
        return tuple(index * index for index in indices)
    raise ValueError("either --order or --index-order is required")


def _parse_radius_order(text: str) -> tuple[int, ...]:
    radii = tuple(_parse_positive_int(part, "radius") for part in _split_csv(text, "order"))
    if len(radii) < 3:
        raise ValueError("fixed-order export requires at least three radii")
    indices = tuple(_square_index(radius) for radius in radii)
    _validate_quadratic_index_permutation(indices)
    return radii


def _parse_index_order(text: str) -> tuple[int, ...]:
    indices = tuple(_parse_positive_int(part, "index") for part in _split_csv(text, "index-order"))
    if len(indices) < 3:
        raise ValueError("fixed-order export requires at least three indices")
    _validate_quadratic_index_permutation(indices)
    return indices


def _split_csv(text: str, name: str) -> tuple[str, ...]:
    parts = tuple(part.strip() for part in text.split(","))
    if not parts or any(not part for part in parts):
        raise ValueError(f"{name} must be a non-empty comma-separated list")
    return parts


def _parse_positive_int(text: str, name: str) -> int:
    try:
        value = int(text, 10)
    except ValueError as exc:
        raise ValueError(f"{name} value must be a positive integer: {text!r}") from exc
    if value <= 0:
        raise ValueError(f"{name} value must be positive: {text!r}")
    return value


def _square_index(radius: int) -> int:
    index = math.isqrt(radius)
    if index * index != radius:
        raise ValueError(f"radius order must contain quadratic radii, got {radius!r}")
    return index


def _validate_quadratic_index_permutation(indices: Sequence[int]) -> None:
    n = len(indices)
    expected = list(range(1, n + 1))
    if sorted(indices) != expected:
        raise ValueError(
            "explicit fixed order must contain exactly the quadratic indices "
            f"1..{n}, got {tuple(indices)!r}"
        )


def _command_record(
    argv: Sequence[str],
    *,
    backend: Backend,
    output: Path,
    n: int,
    command_name: str,
) -> dict[str, str]:
    command = command_name
    if argv:
        command += " " + shlex.join(str(item) for item in argv)
    return {
        "command": command,
        "cwd": str(Path.cwd()),
        "result": "pass",
        "output_summary": (
            f"Exported one n={n} fixed-order artifact with the {backend} backend "
            f"to {output}."
        ),
    }


def _source_files_for_backend(backend: Backend) -> list[dict[str, str]]:
    files = [
        {
            "path": "src/power_ringmin/export_fixed_order_cli.py",
            "role": "fixed-order artifact CLI entry point",
        },
        {
            "path": "src/power_ringmin/fixed_order_artifact.py",
            "role": "artifact exporter and loader",
        },
    ]
    if backend == "float64":
        files.append(
            {
                "path": "src/power_ringmin/evaluator.py",
                "role": "float64 fixed-order STN evaluator",
                "upstream_ringmin_commit": UPSTREAM_RINGMIN_COMMIT,
            }
        )
    else:
        files.append(
            {
                "path": "src/power_ringmin/highprec.py",
                "role": "high-precision fixed-order STN computation",
                "upstream_ringmin_commit": UPSTREAM_RINGMIN_COMMIT,
            }
        )
    return files


if __name__ == "__main__":
    raise SystemExit(main())
