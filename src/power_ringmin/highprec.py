"""Independent mpmath fixed-order verification helpers.

Adapted from upstream Ringmin commit
cc0327400819fe06b230d967cdcbafffe1648317 under the MIT license.
"""

from __future__ import annotations

import mpmath as mp

MAX_BRACKET_STEPS = 160


def _as_mpf_order(order: tuple[int | float, ...] | list[int | float]) -> tuple[mp.mpf, ...]:
    radii = tuple(mp.mpf(r) for r in order)
    if not radii:
        raise ValueError("order must contain at least one radius")
    if any(r <= 0 for r in radii):
        raise ValueError(f"radii must be positive: {order!r}")
    return radii


def _initial_upper_mp(radii: tuple[mp.mpf, ...]) -> mp.mpf:
    n = mp.mpf(len(radii))
    return max(mp.mpf("1"), 4 * n * n, n * max(radii), mp.fsum(radii))


def _default_tol(digits: int) -> mp.mpf:
    return mp.mpf(10) ** (-max(30, digits // 2))


def theta_mp(R: mp.mpf, a: mp.mpf, b: mp.mpf) -> mp.mpf:
    """High-precision angular separation."""
    R = mp.mpf(R)
    a = mp.mpf(a)
    b = mp.mpf(b)
    if R <= 0:
        raise ValueError(f"R must be positive, got {R!r}")
    if a <= 0 or b <= 0:
        raise ValueError(f"radii must be positive, got {a!r}, {b!r}")

    x2 = (a * b) / ((R + a) * (R + b))
    value = 2 * mp.asin(mp.sqrt(x2))
    if not (0 < value < mp.pi):
        raise AssertionError(f"mp theta outside (0, pi): {value}")
    return value


def closed_stn_mp(radii: tuple[mp.mpf, ...], R: mp.mpf) -> list[list[mp.mpf]]:
    """Build and close the high-precision STN distance graph."""
    tau = 2 * mp.pi
    n = len(radii)
    dist = [[mp.inf] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = mp.mpf("0")
    for i in range(n):
        for j in range(i + 1, n):
            sep = theta_mp(R, radii[i], radii[j])
            dist[i][j] = min(dist[i][j], tau - sep)
            dist[j][i] = min(dist[j][i], -sep)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                candidate = dist[i][k] + dist[k][j]
                if candidate < dist[i][j]:
                    dist[i][j] = candidate
    return dist


def feasibility_margin_mp(
    order: tuple[int | float, ...] | list[int | float],
    R: mp.mpf,
    digits: int = 80,
) -> mp.mpf:
    """Return the minimum closed-STN diagonal value at radius R."""
    mp.mp.dps = digits
    radii = _as_mpf_order(order)
    dist = closed_stn_mp(radii, mp.mpf(R))
    return min(dist[i][i] for i in range(len(radii)))


def is_feasible_mp(
    order: tuple[int | float, ...] | list[int | float],
    R: mp.mpf,
    digits: int = 80,
    tol: mp.mpf | None = None,
) -> bool:
    """High-precision fixed-order feasibility oracle."""
    mp.mp.dps = digits
    tolerance = _default_tol(digits) if tol is None else mp.mpf(tol)
    return feasibility_margin_mp(order, mp.mpf(R), digits=digits) >= -tolerance


def full_radius_mp(
    order: tuple[int | float, ...] | list[int | float],
    digits: int = 80,
    iterations: int | None = None,
) -> mp.mpf:
    """Slow high-precision full STN bisection for a fixed order."""
    mp.mp.dps = digits
    radii = _as_mpf_order(order)
    if len(radii) < 3:
        raise ValueError("full_radius_mp requires at least three radii")

    lo = mp.mpf("0")
    hi = _initial_upper_mp(radii)
    for _ in range(MAX_BRACKET_STEPS):
        if is_feasible_mp(tuple(radii), hi, digits=digits):
            break
        hi *= 2
    else:
        raise AssertionError(f"high-precision feasibility bracket failed for {order!r}")

    steps = iterations if iterations is not None else max(180, 4 * digits)
    for _ in range(steps):
        mid = (lo + hi) / 2
        if is_feasible_mp(tuple(radii), mid, digits=digits):
            hi = mid
        else:
            lo = mid
    return hi


def recover_positions_mp(
    order: tuple[int | float, ...] | list[int | float],
    R: mp.mpf,
    digits: int = 80,
) -> tuple[mp.mpf, ...]:
    """Recover one high-precision feasible position vector."""
    mp.mp.dps = digits
    radii = _as_mpf_order(order)
    dist = closed_stn_mp(radii, mp.mpf(R))
    if any(dist[i][i] < -_default_tol(digits) for i in range(len(radii))):
        raise AssertionError("cannot recover mpmath positions from infeasible STN")
    positions = [dist[0][i] for i in range(len(radii))]
    positions[0] = mp.mpf("0")
    return tuple(positions)


def pair_slack_mp(
    order: tuple[int | float, ...] | list[int | float],
    R: mp.mpf,
    positions: tuple[mp.mpf, ...],
    i: int,
    j: int,
) -> tuple[mp.mpf, mp.mpf]:
    """Return forward and wrap slack for one pair in a high-precision placement."""
    radii = _as_mpf_order(order)
    sep = theta_mp(mp.mpf(R), radii[i], radii[j])
    delta = positions[j] - positions[i]
    return delta - sep, (2 * mp.pi - sep) - delta


def verify_fixed_order_mp(
    order: tuple[int | float, ...] | list[int | float],
    R: mp.mpf,
    digits: int = 80,
    tol: mp.mpf | None = None,
) -> bool:
    """Verify fixed-order all-pairs feasibility at radius R with mpmath."""
    return is_feasible_mp(order, mp.mpf(R), digits=digits, tol=tol)
