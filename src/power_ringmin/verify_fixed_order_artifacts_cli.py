"""Batch standalone-verifier check for fixed-order result artifacts."""

from __future__ import annotations

import argparse
from collections.abc import Sequence
from dataclasses import dataclass
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from typing import Any

from power_ringmin.fixed_order_artifact import (
    FixedOrderArtifact,
    load_fixed_order_artifact,
    verifier_payload_from_artifact,
)


@dataclass(frozen=True)
class ArtifactVerificationRecord:
    """One standalone-verifier result for one fixed-order artifact."""

    artifact_path: Path
    n: int | None
    central_radius: str | None
    eta: str | None
    stn_tol: str | None
    command: tuple[str, ...]
    returncode: int
    stdout: str
    stderr: str
    error: str | None = None

    @property
    def passed(self) -> bool:
        """True when the artifact loaded and root ``verify.py`` accepted it."""
        return self.error is None and self.returncode == 0


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for batch artifact verification."""
    parser = argparse.ArgumentParser(
        description=(
            "Validate v1 fixed-order artifacts and run root verify.py against "
            "each derived standalone-verifier payload."
        ),
    )
    parser.add_argument(
        "artifacts_dir",
        type=Path,
        help="directory containing fixed-order artifact JSON files",
    )
    parser.add_argument(
        "--pattern",
        default="*.json",
        help="glob pattern for artifact files inside artifacts_dir (default: *.json)",
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="search artifacts_dir recursively",
    )
    parser.add_argument(
        "--digits",
        type=int,
        default=80,
        help="mpmath working precision digits passed to verify.py (default: 80)",
    )
    parser.add_argument(
        "--eta",
        help=(
            "local bracket radius offset passed to verify.py for every artifact; "
            "by default each artifact's local_radius_bracket eta is used when present"
        ),
    )
    parser.add_argument(
        "--no-artifact-eta",
        action="store_true",
        help="do not use local_radius_bracket eta values recorded in artifacts",
    )
    parser.add_argument(
        "--stn-tol",
        help=(
            "absolute closed-STN diagonal tolerance passed to verify.py; useful "
            "for explicitly tolerance-labeled float64 artifacts"
        ),
    )
    parser.add_argument(
        "--verify-script",
        type=Path,
        default=_default_verify_script(),
        help="path to standalone verify.py (default: repository root verify.py)",
    )
    parser.add_argument(
        "--timeout-seconds",
        type=float,
        default=60.0,
        help="per-artifact standalone verifier timeout (default: 60)",
    )
    return parser


def verify_artifact_directory(
    artifacts_dir: str | Path,
    *,
    pattern: str = "*.json",
    recursive: bool = False,
    digits: int = 80,
    eta: str | None = None,
    use_artifact_eta: bool = True,
    stn_tol: str | None = None,
    verify_script: str | Path | None = None,
    timeout_seconds: float = 60.0,
) -> list[ArtifactVerificationRecord]:
    """Run root ``verify.py`` against every matching v1 artifact in a directory."""
    if digits < 30:
        raise ValueError("digits must be at least 30")
    if timeout_seconds <= 0:
        raise ValueError("timeout_seconds must be positive")

    script = Path(verify_script).resolve() if verify_script is not None else _default_verify_script()
    if not script.is_file():
        raise ValueError(f"standalone verifier not found: {script}")

    artifact_paths = find_artifact_paths(
        artifacts_dir,
        pattern=pattern,
        recursive=recursive,
    )
    records: list[ArtifactVerificationRecord] = []
    with tempfile.TemporaryDirectory(prefix="power_ringmin_verify_") as temp_dir:
        payload_dir = Path(temp_dir)
        for ordinal, artifact_path in enumerate(artifact_paths, start=1):
            records.append(
                verify_one_artifact(
                    artifact_path,
                    payload_dir=payload_dir,
                    payload_ordinal=ordinal,
                    digits=digits,
                    eta=eta,
                    use_artifact_eta=use_artifact_eta,
                    stn_tol=stn_tol,
                    verify_script=script,
                    timeout_seconds=timeout_seconds,
                )
            )
    return records


def find_artifact_paths(
    artifacts_dir: str | Path,
    *,
    pattern: str = "*.json",
    recursive: bool = False,
) -> list[Path]:
    """Return sorted artifact candidate paths for a directory scan."""
    root = Path(artifacts_dir)
    if not root.is_dir():
        raise ValueError(f"artifact path is not a directory: {root}")
    candidates = root.rglob(pattern) if recursive else root.glob(pattern)
    paths = sorted(path for path in candidates if path.is_file())
    if not paths:
        raise ValueError(f"no artifact files matched {pattern!r} in {root}")
    return paths


def verify_one_artifact(
    artifact_path: str | Path,
    *,
    payload_dir: Path,
    payload_ordinal: int,
    digits: int,
    eta: str | None,
    use_artifact_eta: bool,
    stn_tol: str | None,
    verify_script: Path,
    timeout_seconds: float,
) -> ArtifactVerificationRecord:
    """Validate one artifact, derive a payload, and invoke root ``verify.py``."""
    path = Path(artifact_path)
    try:
        artifact = load_fixed_order_artifact(path)
        data = artifact.to_dict()
        if eta is not None:
            eta_value = eta
        elif use_artifact_eta:
            eta_value = _artifact_eta(data)
        else:
            eta_value = None
        payload_path = _write_payload(
            artifact,
            payload_dir=payload_dir,
            ordinal=payload_ordinal,
            artifact_path=path,
        )
        command = _verify_command(
            verify_script,
            payload_path=payload_path,
            digits=digits,
            eta=eta_value,
            stn_tol=stn_tol,
        )
        completed = subprocess.run(
            list(command),
            check=False,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout_seconds,
            cwd=str(verify_script.parent),
        )
        return ArtifactVerificationRecord(
            artifact_path=path,
            n=artifact.n,
            central_radius=artifact.central_radius_decimal,
            eta=eta_value,
            stn_tol=stn_tol,
            command=command,
            returncode=completed.returncode,
            stdout=completed.stdout,
            stderr=completed.stderr,
        )
    except subprocess.TimeoutExpired as exc:
        return ArtifactVerificationRecord(
            artifact_path=path,
            n=None,
            central_radius=None,
            eta=eta,
            stn_tol=stn_tol,
            command=tuple(str(item) for item in exc.cmd),
            returncode=-1,
            stdout=exc.stdout or "",
            stderr=exc.stderr or "",
            error=f"standalone verifier timed out after {timeout_seconds:g} seconds",
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return ArtifactVerificationRecord(
            artifact_path=path,
            n=None,
            central_radius=None,
            eta=eta,
            stn_tol=stn_tol,
            command=(),
            returncode=1,
            stdout="",
            stderr="",
            error=str(exc),
        )


def main(argv: Sequence[str] | None = None) -> int:
    """Run the batch standalone-verifier artifact check CLI."""
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        records = verify_artifact_directory(
            args.artifacts_dir,
            pattern=args.pattern,
            recursive=args.recursive,
            digits=args.digits,
            eta=args.eta,
            use_artifact_eta=not args.no_artifact_eta,
            stn_tol=args.stn_tol,
            verify_script=args.verify_script,
            timeout_seconds=args.timeout_seconds,
        )
    except ValueError as exc:
        parser.error(str(exc))

    passed = 0
    for record in records:
        if record.passed:
            passed += 1
        print(_record_summary(record))
        if not record.passed:
            for line in _failure_detail_lines(record):
                print(f"  - {line}")

    failed = len(records) - passed
    print(
        "batch standalone verification complete "
        f"count={len(records)} passed={passed} failed={failed}"
    )
    return 0 if failed == 0 else 1


def _default_verify_script() -> Path:
    return Path(__file__).resolve().parents[2] / "verify.py"


def _artifact_eta(artifact: dict[str, Any]) -> str | None:
    bracket = artifact["result"].get("local_radius_bracket")
    if isinstance(bracket, dict) and "eta_decimal" in bracket:
        return str(bracket["eta_decimal"])
    return None


def _write_payload(
    artifact: FixedOrderArtifact,
    *,
    payload_dir: Path,
    ordinal: int,
    artifact_path: Path,
) -> Path:
    payload = verifier_payload_from_artifact(artifact)
    payload_path = payload_dir / f"payload_{ordinal:04d}_{artifact_path.stem}.json"
    payload_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return payload_path


def _verify_command(
    verify_script: Path,
    *,
    payload_path: Path,
    digits: int,
    eta: str | None,
    stn_tol: str | None,
) -> tuple[str, ...]:
    command = [
        sys.executable,
        str(verify_script),
        "--input",
        str(payload_path),
        "--digits",
        str(digits),
    ]
    if eta is not None:
        command.extend(["--eta", eta])
    if stn_tol is not None:
        command.extend(["--stn-tol", stn_tol])
    return tuple(command)


def _record_summary(record: ArtifactVerificationRecord) -> str:
    status = "PASS" if record.passed else "FAIL"
    verifier_line = _first_stdout_line(record) or record.error or "no verifier output"
    n_text = "?" if record.n is None else str(record.n)
    eta_text = "" if record.eta is None else f" eta={record.eta}"
    tol_text = "" if record.stn_tol is None else f" stn_tol={record.stn_tol}"
    return f"{status} {record.artifact_path} n={n_text}{eta_text}{tol_text} :: {verifier_line}"


def _first_stdout_line(record: ArtifactVerificationRecord) -> str | None:
    for line in record.stdout.splitlines():
        if line.strip():
            return line.strip()
    return None


def _failure_detail_lines(record: ArtifactVerificationRecord) -> list[str]:
    details: list[str] = []
    if record.error:
        details.append(record.error)
    for text in (record.stdout, record.stderr):
        for line in text.splitlines():
            if line.strip():
                details.append(line.strip())
    if not details:
        details.append(f"standalone verifier exited with code {record.returncode}")
    return details


if __name__ == "__main__":
    raise SystemExit(main())
