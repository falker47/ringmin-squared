from __future__ import annotations

import copy

import mpmath as mp
import pytest

from power_ringmin.highprec import full_radius_mp, theta_mp
from power_ringmin.interval_verifier import (
    FIXED_ORDER_INTERVAL_BRACKET_ARTIFACT_TYPE,
    FIXED_ORDER_INTERVAL_BRACKET_SCHEMA_VERSION,
    MPMathIntervalAngularOracle,
    assert_fixed_order_interval_bracket_verified,
    verify_fixed_order_interval_bracket,
)


def test_mpmath_interval_oracle_contains_high_precision_theta_and_tau() -> None:
    digits = 90
    oracle = MPMathIntervalAngularOracle(digits=digits, guard_decimal="1e-80")

    with mp.workdps(digits):
        R = mp.mpf("0.5")
        theta = theta_mp(R, mp.mpf("1"), mp.mpf("4"))
        interval = oracle.theta(R, mp.mpf("1"), mp.mpf("4"))
        tau_interval = oracle.tau()

        assert interval.lower <= theta <= interval.upper
        assert tau_interval.lower <= 2 * mp.pi <= tau_interval.upper
        assert oracle.backend_info.to_record()["tolerance_based"] is False


def test_local_interval_bracket_accepts_strict_n3_record() -> None:
    oracle = MPMathIntervalAngularOracle(digits=90, guard_decimal="1e-80")
    record = _strict_n3_bracket_record(oracle)

    result = verify_fixed_order_interval_bracket(record, oracle=oracle)

    assert result.verified
    assert result.messages == ()
    assert result.index_order == (3, 1, 2)
    assert result.radius_order == (9, 1, 4)
    assert result.lower_negative_cycle_sum_upper < 0
    assert result.min_upper_witness_slack_lower > 0
    assert assert_fixed_order_interval_bracket_verified(record, oracle=oracle) == result


def test_local_interval_bracket_parses_decimals_at_oracle_precision() -> None:
    oracle = MPMathIntervalAngularOracle(digits=90, guard_decimal="1e-80")
    record = _strict_n3_bracket_record(oracle)
    with mp.workdps(90):
        expected_lower = mp.mpf(str(record["lower_radius_decimal"]))

    old_dps = mp.mp.dps
    try:
        mp.mp.dps = 15
        result = verify_fixed_order_interval_bracket(record, oracle=oracle)
    finally:
        mp.mp.dps = old_dps

    assert result.verified
    with mp.workdps(90):
        assert result.lower_radius == expected_lower


def test_local_interval_bracket_rejects_artifact_type_tampering() -> None:
    oracle = MPMathIntervalAngularOracle(digits=90, guard_decimal="1e-80")
    record = _strict_n3_bracket_record(oracle)
    record["artifact_type"] = "fixed_order_numerical_result"

    result = verify_fixed_order_interval_bracket(record, oracle=oracle)

    assert not result.verified
    assert any("artifact_type" in message for message in result.messages)


@pytest.mark.parametrize(
    ("field", "tampered_value"),
    [
        ("backend", "mpmath_iv_unguarded"),
        ("precision_digits", 89),
        ("rounding_policy", "some non-empty but untrusted policy"),
        ("outward_enclosure", False),
        ("certification_capable", False),
        ("tolerance_based", True),
        ("guard_decimal", "1e-79"),
    ],
)
def test_local_interval_bracket_rejects_tampered_backend_metadata(
    field: str,
    tampered_value: object,
) -> None:
    oracle = MPMathIntervalAngularOracle(digits=90, guard_decimal="1e-80")
    record = _strict_n3_bracket_record(oracle)
    record["theta_interval_backend"][field] = tampered_value

    result = verify_fixed_order_interval_bracket(record, oracle=oracle)

    assert not result.verified
    assert any(f"theta_interval_backend.{field}" in message for message in result.messages)


def test_local_interval_bracket_rejects_backend_metadata_key_tampering() -> None:
    oracle = MPMathIntervalAngularOracle(digits=90, guard_decimal="1e-80")
    record = _strict_n3_bracket_record(oracle)
    del record["theta_interval_backend"]["rounding_policy"]

    missing_result = verify_fixed_order_interval_bracket(record, oracle=oracle)

    assert not missing_result.verified
    assert any("keys must exactly match" in message for message in missing_result.messages)

    record = _strict_n3_bracket_record(oracle)
    record["theta_interval_backend"]["unreviewed_backend_claim"] = "trusted"

    extra_result = verify_fixed_order_interval_bracket(record, oracle=oracle)

    assert not extra_result.verified
    assert any("keys must exactly match" in message for message in extra_result.messages)


def test_local_interval_bracket_rejects_tolerance_based_backend_metadata() -> None:
    oracle = MPMathIntervalAngularOracle(digits=90, guard_decimal="1e-80")
    record = _strict_n3_bracket_record(oracle)
    record["theta_interval_backend"]["tolerance_based"] = True

    result = verify_fixed_order_interval_bracket(record, oracle=oracle)

    assert not result.verified
    assert any("theta_interval_backend.tolerance_based" in message for message in result.messages)


def test_local_interval_bracket_rejects_bad_witness_position() -> None:
    oracle = MPMathIntervalAngularOracle(digits=90, guard_decimal="1e-80")
    record = _strict_n3_bracket_record(oracle)
    broken = copy.deepcopy(record)
    broken["upper_certificate"]["positions_rad"][1] = "0"

    result = verify_fixed_order_interval_bracket(broken, oracle=oracle)

    assert not result.verified
    assert any("upper witness minimum slack" in message for message in result.messages)


def test_local_interval_bracket_rejects_nonnegative_lower_cycle() -> None:
    oracle = MPMathIntervalAngularOracle(digits=90, guard_decimal="1e-80")
    record = _strict_n3_bracket_record(oracle)
    broken = copy.deepcopy(record)
    broken["lower_certificate"]["cycle"] = [
        {"source": 1, "target": 0, "edge_kind": "forward_lower"},
        {"source": 0, "target": 1, "edge_kind": "wrap_upper"},
    ]

    result = verify_fixed_order_interval_bracket(broken, oracle=oracle)

    assert not result.verified
    assert any("strictly negative" in message for message in result.messages)


def test_local_interval_bracket_rejects_noncanonical_index_order() -> None:
    oracle = MPMathIntervalAngularOracle(digits=90, guard_decimal="1e-80")
    record = _strict_n3_bracket_record(oracle)
    record["index_order"] = [1, 2, 3]
    record["radius_order"] = [1, 4, 9]

    result = verify_fixed_order_interval_bracket(record, oracle=oracle)

    assert not result.verified
    assert any("canonical" in message for message in result.messages)


def _strict_n3_bracket_record(oracle: MPMathIntervalAngularOracle) -> dict[str, object]:
    digits = oracle.digits
    order = (9, 1, 4)
    with mp.workdps(digits):
        radius = full_radius_mp(order, digits=digits)
        eta = mp.mpf("1e-4")
        lower = radius - eta
        upper = radius + eta
        positions = _strict_n3_positions(order, upper, digits=digits)

    return {
        "schema_version": FIXED_ORDER_INTERVAL_BRACKET_SCHEMA_VERSION,
        "artifact_type": FIXED_ORDER_INTERVAL_BRACKET_ARTIFACT_TYPE,
        "index_order": [3, 1, 2],
        "radius_order": [9, 1, 4],
        "lower_radius_decimal": mp.nstr(lower, digits),
        "upper_radius_decimal": mp.nstr(upper, digits),
        "lower_certificate": {
            "kind": "negative_cycle",
            "cycle": [
                {"source": 1, "target": 0, "edge_kind": "forward_lower"},
                {"source": 0, "target": 2, "edge_kind": "wrap_upper"},
                {"source": 2, "target": 1, "edge_kind": "forward_lower"},
            ],
        },
        "upper_certificate": {
            "kind": "witness_positions",
            "positions_rad": positions,
        },
        "theta_interval_backend": oracle.backend_info.to_record(),
        "min_upper_witness_slack_lower": "0",
        "lower_negative_cycle_sum_upper": "-1e-20",
    }


def _strict_n3_positions(
    order: tuple[int, int, int],
    R: mp.mpf,
    *,
    digits: int,
) -> list[str]:
    with mp.workdps(digits):
        theta_01 = theta_mp(R, mp.mpf(order[0]), mp.mpf(order[1]))
        theta_02 = theta_mp(R, mp.mpf(order[0]), mp.mpf(order[2]))
        theta_12 = theta_mp(R, mp.mpf(order[1]), mp.mpf(order[2]))
        gap = (2 * mp.pi - theta_01 - theta_02 - theta_12) / 3
        assert gap > mp.mpf("1e-5")
        positions = (
            mp.mpf("0"),
            theta_01 + gap,
            theta_01 + gap + theta_12 + gap,
        )
        return [mp.nstr(position, digits) for position in positions]
