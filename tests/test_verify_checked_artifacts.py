from __future__ import annotations

from pathlib import Path
import tomllib

import pytest

from power_ringmin.verify_checked_artifacts import (
    COMMAND_NAME,
    DEFAULT_CERTIFICATE_GLOB,
    discover_checked_certificate_paths,
    main,
    verify_checked_artifacts,
)


CHECKED_CERTIFICATE_PATHS = (
    Path("examples/small_n_interval_certificate_n3.json"),
    Path("examples/small_n_interval_certificate_n4.json"),
    Path("examples/small_n_interval_certificate_n5.json"),
    Path("examples/small_n_interval_certificate_n6.json"),
)


def test_discover_checked_certificate_paths_finds_checked_examples_only() -> None:
    paths = discover_checked_certificate_paths(pattern=DEFAULT_CERTIFICATE_GLOB)

    assert paths == CHECKED_CERTIFICATE_PATHS


def test_verify_checked_artifacts_revalidates_certificates_local_brackets_and_summary() -> None:
    result = verify_checked_artifacts(certificate_paths=CHECKED_CERTIFICATE_PATHS)

    assert result.certificate_count == 4
    assert result.n_values == (3, 4, 5, 6)
    assert result.local_bracket_count == 76
    assert result.summary_path == Path("examples/finite_results_summary_n3_n6.json")


def test_checked_artifact_verifier_cli_reports_deterministic_summary(
    capsys: pytest.CaptureFixture[str],
) -> None:
    exit_code = main([])

    assert exit_code == 0
    stdout = capsys.readouterr().out
    assert "verified checked artifacts certificates=4" in stdout
    assert "local_brackets=76" in stdout
    assert "summary_n_values=3,4,5,6" in stdout


def test_checked_artifact_verifier_cli_exits_nonzero_on_summary_source_mismatch() -> None:
    with pytest.raises(SystemExit) as exc_info:
        main([str(CHECKED_CERTIFICATE_PATHS[0])])

    assert exc_info.value.code == 2


def test_checked_artifact_verifier_console_script_entry_point_is_registered() -> None:
    pyproject = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))

    assert pyproject["project"]["scripts"][COMMAND_NAME] == (
        "power_ringmin.verify_checked_artifacts:main"
    )
