"""Float64 fixed-order STN evaluator for Power-Ringmin.

Adapted from upstream Ringmin commit
cc0327400819fe06b230d967cdcbafffe1648317 under the MIT license.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Literal

from power_ringmin.geometry import TAU, as_order, theta

CHAIN_REL_TOL = 1e-13
FULL_REL_TOL = 1e-12
TIGHT_TOL = 1e-9
MAX_BRACKET_STEPS = 120


@dataclass(frozen=True)
class BindingPair:
    """A tight pairwise outer-circle constraint."""

    i: int
    j: int
    radius_i: float
    radius_j: float
    kind: Literal["forward", "wrap"]
    slack: float


@dataclass(frozen=True)
class FullResult:
    """Full fixed-order solve result."""

    order: tuple[float, ...]
    R_chain: float
    R_full: float
    positions: tuple[float, ...]
    recovered_tight_pairs: tuple[BindingPair, ...]
    essential_tight_pairs: tuple[BindingPair, ...]
    floating_radii: tuple[float, ...]
    feasible: bool

    @property
    def binding_pairs(self) -> tuple[BindingPair, ...]:
        """Backward-compatible alias for essential tight pairs."""
        return self.essential_tight_pairs


def _initial_radius_upper(radii: tuple[float, ...]) -> float:
    n = len(radii)
    return max(1.0, 4.0 * n * n, float(n) * max(radii), sum(radii))


def _chain_sum(R: float, radii: tuple[float, ...]) -> float:
    total = 0.0
    n = len(radii)
    for i, a in enumerate(radii):
        total += theta(R, a, radii[(i + 1) % n])
    return total


def chain_angle_sum(order: tuple[int | float, ...] | list[int | float], R: float) -> float:
    """Return the adjacent-chain angular sum for one cyclic order at radius R."""
    return _chain_sum(R, as_order(order))


def chain_radius(order: tuple[int | float, ...] | list[int | float]) -> float:
    """Evaluator A: adjacent-chain relaxation radius for one cyclic order."""
    radii = as_order(order)
    if len(radii) < 3:
        raise ValueError("chain_radius requires at least three radii")

    lo = 0.0
    hi = _initial_radius_upper(radii)
    target = TAU

    for _ in range(MAX_BRACKET_STEPS):
        hi_value = _chain_sum(hi, radii)
        if hi_value < target:
            break
        hi *= 2.0
    else:
        raise AssertionError(f"chain-radius bracket failed for {radii!r}")

    while hi - lo > CHAIN_REL_TOL * max(1.0, hi):
        mid = 0.5 * (lo + hi)
        if _chain_sum(mid, radii) > target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def build_stn_distances(order: tuple[int | float, ...] | list[int | float], R: float) -> list[list[float]]:
    """Build and close the STN distance graph by Floyd-Warshall."""
    radii = as_order(order)
    return _closed_stn_distances(radii, R)


def _closed_stn_distances(
    radii: tuple[float, ...],
    R: float,
    slack_index: int | None = None,
    slack_pair: tuple[int, int] | None = None,
    slack: float = 0.0,
) -> list[list[float]]:
    n = len(radii)
    dist = [[math.inf] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0.0

    for i in range(n):
        for j in range(i + 1, n):
            sep = theta(R, radii[i], radii[j])
            if slack_index is not None and (i == slack_index or j == slack_index):
                sep += slack
            if slack_pair is not None and (i, j) == slack_pair:
                sep += slack
            upper = TAU - sep
            lower_edge = -sep
            if upper < -lower_edge:
                dist[0][0] = -math.inf
                return dist
            if upper < dist[i][j]:
                dist[i][j] = upper
            if lower_edge < dist[j][i]:
                dist[j][i] = lower_edge

    for k in range(n):
        row_k = dist[k]
        for i in range(n):
            dik = dist[i][k]
            if dik == math.inf:
                continue
            row_i = dist[i]
            for j in range(n):
                candidate = dik + row_k[j]
                if candidate < row_i[j]:
                    row_i[j] = candidate
    return dist


def is_feasible(order: tuple[int | float, ...] | list[int | float], R: float, tol: float = 1e-11) -> bool:
    """Evaluator B feasibility oracle for a fixed order and R."""
    dist = build_stn_distances(order, R)
    return all(dist[i][i] >= -tol for i in range(len(dist)))


def _is_floatable_circle(radii: tuple[float, ...], R: float, index: int, slack: float) -> bool:
    dist = _closed_stn_distances(radii, R, slack_index=index, slack=slack)
    return all(dist[i][i] >= -1e-11 for i in range(len(dist)))


def _is_essential_pair(radii: tuple[float, ...], R: float, i: int, j: int, slack: float) -> bool:
    dist = _closed_stn_distances(radii, R, slack_pair=(i, j), slack=slack)
    return any(dist[k][k] < -1e-11 for k in range(len(dist)))


def recover_positions(order: tuple[int | float, ...] | list[int | float], R: float) -> tuple[float, ...]:
    """Recover one feasible position vector using shortest paths from node 0."""
    dist = build_stn_distances(order, R)
    if any(dist[i][i] < -1e-10 for i in range(len(dist))):
        raise AssertionError(f"cannot recover positions from infeasible STN at R={R!r}")
    positions = [dist[0][k] for k in range(len(dist))]
    positions[0] = 0.0
    return tuple(positions)


def recovered_tight_pairs(
    order: tuple[int | float, ...] | list[int | float],
    R: float,
    positions: tuple[float, ...],
    tol: float = TIGHT_TOL,
) -> tuple[BindingPair, ...]:
    """Return placement-dependent tight constraints in the recovered STN solution."""
    radii = as_order(order)
    bindings: list[BindingPair] = []

    for i in range(len(radii)):
        for j in range(i + 1, len(radii)):
            sep = theta(R, radii[i], radii[j])
            delta = positions[j] - positions[i]
            forward_slack = delta - sep
            wrap_slack = (TAU - sep) - delta
            if abs(forward_slack) <= tol:
                bindings.append(BindingPair(i, j, radii[i], radii[j], "forward", forward_slack))
            if abs(wrap_slack) <= tol:
                bindings.append(BindingPair(i, j, radii[i], radii[j], "wrap", wrap_slack))
    return tuple(bindings)


def essential_tight_pairs(
    order: tuple[int | float, ...] | list[int | float],
    R: float,
    positions: tuple[float, ...],
    tol: float = TIGHT_TOL,
) -> tuple[BindingPair, ...]:
    """Return constraints whose individual strict separation forces R upward."""
    radii = as_order(order)
    essentials: list[BindingPair] = []
    for i in range(len(radii)):
        for j in range(i + 1, len(radii)):
            if not _is_essential_pair(radii, R, i, j, slack=tol):
                continue
            sep = theta(R, radii[i], radii[j])
            delta = positions[j] - positions[i]
            forward_slack = delta - sep
            wrap_slack = (TAU - sep) - delta
            kind: Literal["forward", "wrap"]
            slack_value: float
            if abs(forward_slack) <= abs(wrap_slack):
                kind = "forward"
                slack_value = forward_slack
            else:
                kind = "wrap"
                slack_value = wrap_slack
            essentials.append(BindingPair(i, j, radii[i], radii[j], kind, slack_value))
    return tuple(essentials)


def floating_radii_by_stn(
    order: tuple[int | float, ...] | list[int | float],
    R: float,
    tol: float = TIGHT_TOL,
) -> tuple[float, ...]:
    """Return radii whose incident constraints can all be relaxed by ``tol``."""
    radii = as_order(order)
    return tuple(
        radius
        for i, radius in enumerate(radii)
        if _is_floatable_circle(radii, R, i, slack=tol)
    )


def binding_structure(
    order: tuple[int | float, ...] | list[int | float],
    R: float,
    positions: tuple[float, ...],
    tol: float = TIGHT_TOL,
) -> tuple[tuple[BindingPair, ...], tuple[float, ...]]:
    """Return essential binding pairs and floating radii."""
    essentials = essential_tight_pairs(order, R, positions, tol=tol)
    floating = floating_radii_by_stn(order, R, tol=tol)
    _assert_floating_consistency(as_order(order), essentials, floating)
    return essentials, floating


def _assert_floating_consistency(
    radii: tuple[float, ...],
    essentials: tuple[BindingPair, ...],
    floating: tuple[float, ...],
) -> None:
    essential_indices = {binding.i for binding in essentials} | {binding.j for binding in essentials}
    zero_essential = tuple(radius for i, radius in enumerate(radii) if i not in essential_indices)
    if zero_essential != floating:
        raise AssertionError(
            "floating consistency failed: "
            f"zero_essential={zero_essential!r}, floating={floating!r}, essentials={essentials!r}"
        )


def assert_cartesian(order: tuple[int | float, ...] | list[int | float], R: float, positions: tuple[float, ...]) -> None:
    """Hard Cartesian non-overlap and central-tangency verification."""
    radii = as_order(order)
    centers: list[tuple[float, float]] = []
    for radius, phi in zip(radii, positions, strict=True):
        center_radius = R + radius
        x = center_radius * math.cos(phi)
        y = center_radius * math.sin(phi)
        if not math.isclose(math.hypot(x, y), center_radius, rel_tol=1e-12, abs_tol=1e-9):
            raise AssertionError(
                f"central distance assert failed: radius={radius}, R={R}, phi={phi}"
            )
        centers.append((x, y))

    for i in range(len(radii)):
        xi, yi = centers[i]
        for j in range(i + 1, len(radii)):
            xj, yj = centers[j]
            dist = math.hypot(xi - xj, yi - yj)
            required = radii[i] + radii[j]
            if dist < required - 1e-9:
                raise AssertionError(
                    "outer non-overlap assert failed: "
                    f"i={i}, j={j}, radii=({radii[i]}, {radii[j]}), "
                    f"dist={dist}, required={required}, R={R}"
                )


def full_radius_value(
    order: tuple[int | float, ...] | list[int | float],
    R_chain: float | None = None,
) -> tuple[float, float]:
    """Evaluator B objective only: return ``(R_chain, R_full)`` without recovery."""
    radii = as_order(order)
    lower = chain_radius(radii) if R_chain is None else float(R_chain)
    upper = lower

    if not is_feasible(radii, upper):
        upper = max(upper * 2.0, _initial_radius_upper(radii), 1e-8)
        for _ in range(MAX_BRACKET_STEPS):
            if is_feasible(radii, upper):
                break
            upper *= 2.0
        else:
            raise AssertionError(f"full-radius feasibility bracket failed for {radii!r}")

        lo = lower
        hi = upper
        while hi - lo > FULL_REL_TOL * max(1.0, hi):
            mid = 0.5 * (lo + hi)
            if is_feasible(radii, mid):
                hi = mid
            else:
                lo = mid
        R_full = hi
    else:
        R_full = upper
    return lower, R_full


def full_radius(
    order: tuple[int | float, ...] | list[int | float],
    R_chain: float | None = None,
) -> FullResult:
    """Evaluator B: minimal feasible R for a fixed cyclic order."""
    radii = as_order(order)
    lower, R_full = full_radius_value(radii, R_chain=R_chain)

    positions = recover_positions(radii, R_full)
    assert_cartesian(radii, R_full, positions)
    recovered = recovered_tight_pairs(radii, R_full, positions)
    essentials = essential_tight_pairs(radii, R_full, positions)
    floating = floating_radii_by_stn(radii, R_full)
    _assert_floating_consistency(radii, essentials, floating)
    return FullResult(
        order=radii,
        R_chain=lower,
        R_full=R_full,
        positions=positions,
        recovered_tight_pairs=recovered,
        essential_tight_pairs=essentials,
        floating_radii=floating,
        feasible=True,
    )
