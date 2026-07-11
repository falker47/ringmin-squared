from __future__ import annotations

import copy
import math
from pathlib import Path
import tomllib

import pytest

from power_ringmin.evaluator import full_radius
from power_ringmin.geometry import quadratic_radii
from power_ringmin.search_small_n import (
    build_small_n_search_artifact,
    canonical_index_order_count,
    canonical_index_orders,
    canonicalize_index_order,
    exhaustive_float64_search,
    index_order_to_radius_order,
    load_small_n_search_artifact,
    main,
    validate_small_n_search_artifact,
)


def test_canonical_index_orders_have_expected_counts_and_shape() -> None:
    for n in range(3, 9):
        orders = tuple(canonical_index_orders(n))

        assert len(orders) == canonical_index_order_count(n)
        assert len(orders) == math.factorial(n - 1) // 2
        assert len({canonicalize_index_order(order) for order in orders}) == len(orders)

        for order in orders:
            assert order[0] == n
            assert order[1] < order[-1]
            assert sorted(order) == list(range(1, n + 1))
            assert canonicalize_index_order(order) == order


def test_canonicalize_index_order_collapses_rotation_and_reflection() -> None:
    base = (6, 1, 5, 2, 4, 3)
    rotated = (5, 2, 4, 3, 6, 1)
    reflected = tuple(reversed(base))

    assert canonicalize_index_order(base) == base
    assert canonicalize_index_order(rotated) == base
    assert canonicalize_index_order(reflected) == base


def test_index_order_to_radius_order_maps_quadratic_indices() -> None:
    assert index_order_to_radius_order((4, 1, 3, 2)) == (16, 1, 9, 4)

    with pytest.raises(ValueError):
        index_order_to_radius_order((4, 1, 1, 2))


def test_exhaustive_float64_search_n3_matches_fixed_order_radius() -> None:
    result = exhaustive_float64_search(3, top_k=5)
    fixed = full_radius(quadratic_radii(3))

    assert result.mode == "exhaustive_float64"
    assert result.evidence_classification == "numerical_observation"
    assert result.expected_canonical_count == 1
    assert result.enumerated_count == 1
    assert result.evaluated_full_count == 1
    assert result.best.index_order == (3, 1, 2)
    assert result.best.radius_order == (9, 1, 4)
    assert result.best.R_full == pytest.approx(fixed.R_full, rel=1e-10, abs=1e-10)
    assert result.ties == (result.best,)
    assert result.top_records == (result.best,)


def test_small_n_search_artifact_validates_classification_and_orders() -> None:
    result = exhaustive_float64_search(4, top_k=3)
    artifact = build_small_n_search_artifact(
        result,
        created_at_utc="2026-07-11T00:00:00Z",
        argv_for_provenance=["--n", "4", "--output", "search.json"],
    )

    validate_small_n_search_artifact(artifact)
    assert artifact["schema_version"] == "power-ringmin.small_n_search_result.v1"
    assert artifact["evidence"]["classification"] == "numerical_observation"
    assert artifact["evidence"]["claim"]["scope"] == "finite_exhaustive_float64_order_search"
    assert "not a computer-certified global optimum" in artifact["evidence"]["claim"]["statement"]
    assert artifact["order_space"]["expected_canonical_count"] == 3
    assert artifact["order_space"]["enumerated_count"] == 3
    assert artifact["result"]["evaluated_full_count"] == 3

    bad_radius = copy.deepcopy(artifact)
    bad_radius["result"]["best"]["radius_order"][0] = 999
    with pytest.raises(ValueError):
        validate_small_n_search_artifact(bad_radius)

    bad_classification = copy.deepcopy(artifact)
    bad_classification["evidence"]["classification"] = "computer_certified_result"
    with pytest.raises(ValueError):
        validate_small_n_search_artifact(bad_classification)

    bad_n = copy.deepcopy(artifact)
    bad_n["instance"]["n"] = 5
    with pytest.raises(ValueError):
        validate_small_n_search_artifact(bad_n)


def test_small_n_search_cli_writes_deterministic_n3_output(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    output = tmp_path / "small_n_search.json"

    exit_code = main(
        [
            "--n",
            "3",
            "--top-k",
            "5",
            "--output",
            str(output),
            "--created-at-utc",
            "2026-07-11T00:00:00Z",
        ]
    )

    assert exit_code == 0
    stdout = capsys.readouterr().out
    assert "wrote" in stdout
    assert "backend=float64" in stdout
    assert "enumerated=1" in stdout

    artifact = load_small_n_search_artifact(output)
    assert artifact["provenance"]["created_at_utc"] == "2026-07-11T00:00:00Z"
    assert artifact["result"]["best"]["index_order"] == [3, 1, 2]
    assert artifact["result"]["best"]["radius_order"] == [9, 1, 4]
    assert artifact["result"]["top_records"] == artifact["result"]["ties"]
    assert artifact["evidence"]["classification"] == "numerical_observation"


def test_small_n_search_console_script_entry_point_is_registered() -> None:
    pyproject = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))

    assert pyproject["project"]["scripts"]["power-ringmin-search-small-n"] == (
        "power_ringmin.search_small_n:main"
    )

