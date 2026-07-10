"""Batch command-line exporter for fixed-order result artifacts."""

from __future__ import annotations

import argparse
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
import json
import math
from pathlib import Path
import sys
from typing import Any, Literal

from power_ringmin.export_fixed_order_cli import Backend, export_artifact_for_order

OrderKind = Literal["radius", "index"]


@dataclass(frozen=True)
class BatchExportRecord:
    """One artifact produced by a batch export run."""

    path: Path
    artifact: dict[str, Any]


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the batch fixed-order exporter."""
    parser = argparse.ArgumentParser(
        description=(
            "Export one v1 fixed-order artifact per explicit cyclic order in a "
            "JSON list."
        ),
    )
    parser.add_argument(
        "orders_json",
        type=Path,
        help="JSON file containing a list of explicit orders, or an object with an orders list",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        required=True,
        type=Path,
        help="directory to receive one v1 fixed-order JSON artifact per order",
    )
    parser.add_argument(
        "--order-kind",
        choices=("radius", "index"),
        default="radius",
        help="interpret each JSON order as quadratic radii or quadratic indices (default: radius)",
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
    parser.add_argument(
        "--filename-prefix",
        default="fixed_order",
        help="prefix for generated artifact filenames (default: fixed_order)",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="allow replacement of existing generated artifact files",
    )
    return parser


def load_orders_json(path: str | Path, *, order_kind: OrderKind = "radius") -> list[tuple[int, ...]]:
    """Load and normalize explicit fixed orders from a JSON file."""
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    raw_orders = _orders_payload(payload, order_kind=order_kind)
    return [
        _normalize_json_order(raw_order, order_kind=order_kind, position=position)
        for position, raw_order in enumerate(raw_orders, start=1)
    ]


def export_batch_artifacts(
    orders: Sequence[Sequence[int]],
    *,
    backend: Backend,
    output_dir: Path,
    argv_for_provenance: Sequence[str],
    digits: int = 80,
    local_radius_eta: str | None = None,
    created_at_utc: str | None = None,
    filename_prefix: str = "fixed_order",
    overwrite: bool = False,
) -> list[BatchExportRecord]:
    """Compute and write one fixed-order artifact per explicit order."""
    normalized_orders = [tuple(order) for order in orders]
    if not normalized_orders:
        raise ValueError("batch export requires at least one explicit order")
    _validate_filename_prefix(filename_prefix)

    output_dir.mkdir(parents=True, exist_ok=True)
    if not output_dir.is_dir():
        raise ValueError(f"output path is not a directory: {output_dir}")

    output_paths = [
        _artifact_output_path(output_dir, filename_prefix, ordinal, order)
        for ordinal, order in enumerate(normalized_orders, start=1)
    ]
    existing = [path for path in output_paths if path.exists()]
    if existing and not overwrite:
        preview = ", ".join(str(path) for path in existing[:3])
        suffix = "" if len(existing) <= 3 else f", ... ({len(existing)} total)"
        raise ValueError(f"refusing to overwrite existing artifact(s): {preview}{suffix}")

    records: list[BatchExportRecord] = []
    for order, output in zip(normalized_orders, output_paths, strict=True):
        artifact = export_artifact_for_order(
            order,
            backend=backend,
            output=output,
            argv_for_provenance=argv_for_provenance,
            digits=digits,
            local_radius_eta=local_radius_eta,
            created_at_utc=created_at_utc,
            command_name="power-ringmin-export-fixed-order-batch",
            extra_source_files=[
                {
                    "path": "src/power_ringmin/export_fixed_order_batch_cli.py",
                    "role": "batch fixed-order artifact CLI entry point",
                }
            ],
        )
        records.append(BatchExportRecord(path=output, artifact=artifact))
    return records


def main(argv: Sequence[str] | None = None) -> int:
    """Run the batch fixed-order artifact export CLI."""
    parser = build_parser()
    raw_argv = list(sys.argv[1:] if argv is None else argv)
    args = parser.parse_args(raw_argv)

    if args.backend == "mpmath" and args.digits < 30:
        parser.error("--digits must be at least 30 when --backend=mpmath")
    if args.backend == "float64" and args.local_radius_eta is not None:
        parser.error("--local-radius-eta requires --backend=mpmath")

    try:
        orders = load_orders_json(args.orders_json, order_kind=args.order_kind)
        records = export_batch_artifacts(
            orders,
            backend=args.backend,
            output_dir=args.output_dir,
            argv_for_provenance=raw_argv,
            digits=args.digits,
            local_radius_eta=args.local_radius_eta,
            created_at_utc=args.created_at_utc,
            filename_prefix=args.filename_prefix,
            overwrite=args.overwrite,
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

    for record in records:
        artifact = record.artifact
        radius = artifact["result"]["central_radius"]["decimal"]
        print(
            f"wrote {record.path} n={artifact['instance']['n']} "
            f"backend={args.backend} R={radius}"
        )
    print(
        f"batch complete count={len(records)} output_dir={args.output_dir} "
        f"backend={args.backend}"
    )
    return 0


def _orders_payload(payload: Any, *, order_kind: OrderKind) -> list[Any]:
    if isinstance(payload, list):
        return payload
    if isinstance(payload, Mapping):
        key = "index_orders" if order_kind == "index" and "index_orders" in payload else "orders"
        raw_orders = payload.get(key)
        if isinstance(raw_orders, list):
            return raw_orders
    raise ValueError(
        "orders JSON must be a list or an object with an 'orders' list"
    )


def _normalize_json_order(raw_order: Any, *, order_kind: OrderKind, position: int) -> tuple[int, ...]:
    if isinstance(raw_order, (str, bytes)) or not isinstance(raw_order, Sequence):
        raise ValueError(f"order {position} must be a JSON array")
    values = tuple(
        _parse_json_positive_int(value, f"order {position} value {index}")
        for index, value in enumerate(raw_order, start=1)
    )
    if len(values) < 3:
        raise ValueError(f"order {position} requires at least three entries")
    if order_kind == "radius":
        indices = tuple(_square_index(radius) for radius in values)
        _validate_quadratic_index_permutation(indices, position=position)
        return values
    _validate_quadratic_index_permutation(values, position=position)
    return tuple(index * index for index in values)


def _parse_json_positive_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise ValueError(f"{name} must be a positive integer: {value!r}")
    if isinstance(value, int):
        parsed = value
    elif isinstance(value, str):
        try:
            parsed = int(value, 10)
        except ValueError as exc:
            raise ValueError(f"{name} must be a positive integer: {value!r}") from exc
    else:
        raise ValueError(f"{name} must be a positive integer: {value!r}")
    if parsed <= 0:
        raise ValueError(f"{name} must be positive: {value!r}")
    return parsed


def _square_index(radius: int) -> int:
    index = math.isqrt(radius)
    if index * index != radius:
        raise ValueError(f"radius order must contain quadratic radii, got {radius!r}")
    return index


def _validate_quadratic_index_permutation(indices: Sequence[int], *, position: int) -> None:
    n = len(indices)
    expected = list(range(1, n + 1))
    if sorted(indices) != expected:
        raise ValueError(
            f"order {position} must contain exactly the quadratic indices "
            f"1..{n}, got {tuple(indices)!r}"
        )


def _artifact_output_path(
    output_dir: Path,
    filename_prefix: str,
    ordinal: int,
    order: Sequence[int],
) -> Path:
    return output_dir / f"{filename_prefix}_{ordinal:04d}_n{len(order)}.json"


def _validate_filename_prefix(prefix: str) -> None:
    if not prefix:
        raise ValueError("filename prefix must be non-empty")
    if "/" in prefix or "\\" in prefix:
        raise ValueError("filename prefix must not contain path separators")


if __name__ == "__main__":
    raise SystemExit(main())
