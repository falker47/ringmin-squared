"""Standalone high-precision fixed-order verifier scaffold.

Adapted from upstream Ringmin commit
cc0327400819fe06b230d967cdcbafffe1648317 under the MIT license.

This file intentionally imports only the Python standard library and mpmath.
It verifies explicit fixed-order radius payloads and local radius brackets; it
does not import the Power-Ringmin package, result artifacts, frontiers, or the
certified-search pipeline.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import mpmath as mp

DEFAULT_DIGITS = 80
DIAG_TOL_EXPONENT_FLOOR = 30
WITNESS_ANGLE_TOL = mp.mpf("1e-8")
CARTESIAN_TOL = mp.mpf("1e-8")


def _tolerance(digits: int) -> mp.mpf:
    return mp.mpf(10) ** (-max(DIAG_TOL_EXPONENT_FLOOR, digits // 2))


def _as_mpf_order(order: list[Any] | tuple[Any, ...]) -> tuple[mp.mpf, ...]:
    radii = tuple(mp.mpf(str(value)) for value in order)
    if len(radii) < 3:
        raise ValueError("fixed-order verification requires at least three radii")
    if any(radius <= 0 for radius in radii):
        raise ValueError(f"radii must be positive: {order!r}")
    return radii


def _parse_order(text: str) -> tuple[mp.mpf, ...]:
    values = [part.strip() for part in text.split(",") if part.strip()]
    if not values:
        raise ValueError("order must contain comma-separated radii")
    return _as_mpf_order(values)


def theta(R: mp.mpf, a: mp.mpf, b: mp.mpf) -> mp.mpf:
    """High-precision required angular separation."""
    x2 = (a * b) / ((R + a) * (R + b))
    value = 2 * mp.asin(mp.sqrt(x2))
    if not (0 < value < mp.pi):
        raise AssertionError(f"theta outside (0, pi): R={R}, a={a}, b={b}, theta={value}")
    return value


def closed_stn(order: tuple[mp.mpf, ...], R: mp.mpf) -> list[list[mp.mpf]]:
    """Build and close the high-precision all-pairs STN."""
    tau = 2 * mp.pi
    n = len(order)
    dist = [[mp.inf] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = mp.mpf("0")
    for i in range(n):
        for j in range(i + 1, n):
            sep = theta(R, order[i], order[j])
            upper = tau - sep
            lower = -sep
            if upper < -lower:
                dist[0][0] = -mp.inf
                return dist
            if upper < dist[i][j]:
                dist[i][j] = upper
            if lower < dist[j][i]:
                dist[j][i] = lower
    for k in range(n):
        for i in range(n):
            dik = dist[i][k]
            if dik == mp.inf:
                continue
            for j in range(n):
                candidate = dik + dist[k][j]
                if candidate < dist[i][j]:
                    dist[i][j] = candidate
    return dist


def feasibility_margin(order: tuple[mp.mpf, ...], R: mp.mpf) -> mp.mpf:
    """Return the minimum closed-STN diagonal margin."""
    dist = closed_stn(order, R)
    return min(dist[i][i] for i in range(len(order)))


def feasible(order: tuple[mp.mpf, ...], R: mp.mpf, tol: mp.mpf) -> bool:
    """True when the fixed-order all-pairs STN is feasible at radius ``R``."""
    return feasibility_margin(order, R) >= -tol


def recover_positions(order: tuple[mp.mpf, ...], R: mp.mpf, tol: mp.mpf) -> tuple[mp.mpf, ...]:
    """Recover one feasible witness placement from the closed STN."""
    dist = closed_stn(order, R)
    if any(dist[i][i] < -tol for i in range(len(order))):
        raise AssertionError("cannot recover positions from infeasible STN")
    positions = [dist[0][i] for i in range(len(order))]
    positions[0] = mp.mpf("0")
    return tuple(positions)


def pair_slacks(
    order: tuple[mp.mpf, ...],
    R: mp.mpf,
    positions: tuple[mp.mpf, ...],
    i: int,
    j: int,
) -> tuple[mp.mpf, mp.mpf]:
    """Return forward and wrap angular slacks for one pair."""
    sep = theta(R, order[i], order[j])
    delta = positions[j] - positions[i]
    return delta - sep, (2 * mp.pi - sep) - delta


def check_witness(
    order: tuple[mp.mpf, ...],
    R: mp.mpf,
    raw_positions: list[Any],
    messages: list[str],
) -> bool:
    """Check optional payload positions in angular and Cartesian form."""
    if len(raw_positions) != len(order):
        messages.append("witness position count mismatch")
        return False
    positions = tuple(mp.mpf(str(value)) for value in raw_positions)
    ok = True
    for i in range(len(order)):
        for j in range(i + 1, len(order)):
            forward, wrap = pair_slacks(order, R, positions, i, j)
            if forward < -WITNESS_ANGLE_TOL or wrap < -WITNESS_ANGLE_TOL:
                ok = False
                messages.append(
                    f"witness angular violation i={i} j={j}: "
                    f"forward={mp.nstr(forward, 12)} wrap={mp.nstr(wrap, 12)}"
                )

    centers: list[tuple[mp.mpf, mp.mpf]] = []
    for radius, phi in zip(order, positions, strict=True):
        rho = R + radius
        centers.append((rho * mp.cos(phi), rho * mp.sin(phi)))
    for i in range(len(order)):
        xi, yi = centers[i]
        for j in range(i + 1, len(order)):
            xj, yj = centers[j]
            distance = mp.sqrt((xi - xj) ** 2 + (yi - yj) ** 2)
            required = order[i] + order[j]
            if distance < required - CARTESIAN_TOL:
                ok = False
                messages.append(
                    f"witness cartesian violation i={i} j={j}: "
                    f"distance={mp.nstr(distance, 12)} required={mp.nstr(required, 12)}"
                )
    return ok


def load_payload(path: Path) -> tuple[tuple[mp.mpf, ...], mp.mpf, list[Any] | None]:
    """Load a minimal fixed-order payload from JSON."""
    payload = json.loads(path.read_text(encoding="utf-8"))
    raw_order = payload.get("ordering", payload.get("order"))
    if not isinstance(raw_order, list):
        raise ValueError("payload must contain an 'ordering' or 'order' list")
    radius_value = None
    for key in ("R_mpmath_full", "R_mpmath_30", "R_full", "R"):
        if key in payload:
            radius_value = payload[key]
            break
    if radius_value is None:
        raise ValueError("payload must contain R, R_full, R_mpmath_30, or R_mpmath_full")
    raw_positions = payload.get("positions")
    if raw_positions is not None and not isinstance(raw_positions, list):
        raise ValueError("payload positions must be a list when present")
    return _as_mpf_order(raw_order), mp.mpf(str(radius_value)), raw_positions


def main() -> int:
    parser = argparse.ArgumentParser(description="Standalone fixed-order high-precision verifier")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--input", type=Path, help="JSON payload with ordering and R")
    source.add_argument("--order", help="comma-separated radius order, e.g. 1,4,9")
    parser.add_argument("--radius", help="claimed central radius; required with --order")
    parser.add_argument("--digits", type=int, default=DEFAULT_DIGITS)
    parser.add_argument("--eta", default="0", help="positive local bracket radius offset")
    parser.add_argument(
        "--stn-tol",
        help="override the absolute closed-STN diagonal tolerance derived from --digits",
    )
    args = parser.parse_args()

    if args.digits < 30:
        raise SystemExit("digits must be at least 30")
    mp.mp.dps = args.digits
    tol = _tolerance(args.digits)
    if args.stn_tol is not None:
        try:
            tol = mp.mpf(str(args.stn_tol))
        except Exception as exc:
            raise SystemExit(f"invalid --stn-tol: {args.stn_tol!r}") from exc
        if not mp.isfinite(tol) or tol < 0:
            raise SystemExit("stn-tol must be finite and nonnegative")

    if args.input is not None:
        order, R, raw_positions = load_payload(args.input)
    else:
        if args.radius is None:
            raise SystemExit("--radius is required with --order")
        order = _parse_order(args.order)
        R = mp.mpf(str(args.radius))
        raw_positions = None

    messages: list[str] = []
    ok = True
    margin = feasibility_margin(order, R)
    if margin < -tol:
        ok = False
        messages.append(f"STN infeasible at R: margin={mp.nstr(margin, 20)}")

    local_text = "SKIP"
    eta = mp.mpf(str(args.eta))
    if eta < 0:
        raise SystemExit("eta must be nonnegative")
    if eta > 0:
        high_ok = feasible(order, R + eta, tol)
        low_ok = not feasible(order, R - eta, tol) if R > eta else True
        local_text = "PASS" if high_ok and low_ok else "FAIL"
        if not high_ok:
            ok = False
            messages.append(f"STN infeasible at R+eta eta={mp.nstr(eta, 8)}")
        if not low_ok:
            ok = False
            messages.append(f"STN feasible at R-eta eta={mp.nstr(eta, 8)}")

    witness_text = "SKIP"
    if raw_positions is not None:
        witness_ok = check_witness(order, R, raw_positions, messages)
        witness_text = "PASS" if witness_ok else "FAIL"
        ok = ok and witness_ok

    print(
        f"fixed_order={'PASS' if margin >= -tol else 'FAIL'} "
        f"local={local_text} witness={witness_text} "
        f"n={len(order)} R={mp.nstr(R, 30)} margin={mp.nstr(margin, 12)}"
    )
    for message in messages:
        print(f"  - {message}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
