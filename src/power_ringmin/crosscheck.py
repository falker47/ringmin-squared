"""Independent fixed-order SciPy SLSQP cross-checks.

Adapted from upstream Ringmin commit
cc0327400819fe06b230d967cdcbafffe1648317 under the MIT license.

Only the fixed-order optimizer is imported here.  The upstream unconstrained
global SLSQP helper is deliberately omitted because it hardcodes the original
``1, ..., n`` radius sequence and is coupled to certified-search comparisons.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
import random
from typing import Iterable

from power_ringmin.geometry import TAU, as_order

DEFAULT_MARGIN_TOL = 1e-6
MAX_START_RADIUS_STEPS = 160


@dataclass(frozen=True)
class SLSQPCheckResult:
    """Result of an independent fixed-order SLSQP minimization."""

    R: float
    positions: tuple[float, ...]
    success: bool
    message: str
    min_pair_margin: float
    min_order_margin: float
    starts_attempted: int

    @property
    def min_constraint(self) -> float:
        """Backward-compatible aggregate minimum constraint margin."""
        return min(self.min_pair_margin, self.min_order_margin)


def _initial_radius_upper(radii: tuple[float, ...]) -> float:
    n = len(radii)
    return max(1.0, 4.0 * n * n, float(n) * max(radii), sum(radii))


def _ordered_random_phis(n: int, rng: random.Random) -> tuple[float, ...]:
    raw = [rng.expovariate(1.0) for _ in range(n)]
    total = math.fsum(raw)
    cumulative = 0.0
    phis: list[float] = []
    for gap in raw[:-1]:
        cumulative += gap / total * TAU
        phis.append(cumulative)
    return tuple(phis)


def _even_phis(n: int) -> tuple[float, ...]:
    return tuple((i + 1) * TAU / n for i in range(n - 1))


def _pair_margin(
    radii: tuple[float, ...],
    phis: tuple[float, ...],
    R: float,
    i: int,
    j: int,
) -> float:
    delta = phis[j] - phis[i]
    dist2 = (R + radii[i]) ** 2 + (R + radii[j]) ** 2
    dist2 -= 2.0 * (R + radii[i]) * (R + radii[j]) * math.cos(delta)
    return dist2 - (radii[i] + radii[j]) ** 2


def _min_pair_margin(radii: tuple[float, ...], phis: tuple[float, ...], R: float) -> float:
    best = math.inf
    for i in range(len(radii)):
        for j in range(i + 1, len(radii)):
            best = min(best, _pair_margin(radii, phis, R, i, j))
    return best


def _min_order_margin(phis: tuple[float, ...]) -> float:
    if len(phis) <= 1:
        return TAU
    gaps = [phis[1] - phis[0]]
    gaps.extend(phis[i + 1] - phis[i] for i in range(1, len(phis) - 1))
    gaps.append(TAU - phis[-1])
    return min(gaps)


def _feasible_start_radius(
    radii: tuple[float, ...],
    phis: tuple[float, ...],
    floor: float,
) -> float:
    R = max(floor, _initial_radius_upper(radii))
    for _ in range(MAX_START_RADIUS_STEPS):
        if _min_pair_margin(radii, (0.0, *phis), R) >= 0.0:
            return R
        R *= 2.0
    raise AssertionError(f"SLSQP start radius bracket failed for order={radii!r}")


def slsqp_fixed_order(
    order: Iterable[int | float],
    starts: int = 20,
    seed: int = 0,
    margin_tol: float = DEFAULT_MARGIN_TOL,
) -> SLSQPCheckResult:
    """Minimize central radius for a fixed cyclic order with SLSQP.

    The input is a radius sequence, not an implicit ``1, ..., n`` instance.
    Position variables are constrained to remain in the supplied cyclic order,
    and every pairwise Cartesian non-overlap constraint is enforced.
    """
    if starts < 1:
        raise ValueError(f"starts must be positive, got {starts!r}")

    try:
        import numpy as np
        from scipy.optimize import minimize
    except ImportError as exc:  # pragma: no cover - exercised only without extras
        raise RuntimeError(
            "slsqp_fixed_order requires the optional crosscheck dependencies: numpy and scipy"
        ) from exc

    radii = as_order(order)
    n = len(radii)
    if n < 3:
        raise ValueError("slsqp_fixed_order requires at least three radii")

    rng = random.Random(seed)
    radius_floor = 1e-12
    bounds = [(0.0, TAU)] * (n - 1) + [(radius_floor, None)]

    def unpack(x: np.ndarray) -> tuple[tuple[float, ...], float]:
        return (0.0, *[float(value) for value in x[: n - 1]]), float(x[-1])

    def objective(x: np.ndarray) -> float:
        return float(x[-1])

    constraints = []
    constraints.append({"type": "ineq", "fun": lambda x: x[0]})
    for i in range(1, n - 1):
        constraints.append({"type": "ineq", "fun": lambda x, i=i: x[i] - x[i - 1]})
    constraints.append({"type": "ineq", "fun": lambda x: TAU - x[n - 2]})
    for i in range(n):
        for j in range(i + 1, n):
            constraints.append(
                {
                    "type": "ineq",
                    "fun": lambda x, i=i, j=j: _pair_margin(
                        radii, unpack(x)[0], float(x[-1]), i, j
                    ),
                }
            )

    best: SLSQPCheckResult | None = None
    messages: list[str] = []
    for start_index in range(starts):
        phis = _even_phis(n) if start_index == 0 else _ordered_random_phis(n, rng)
        x0 = np.empty(n, dtype=np.float64)
        x0[: n - 1] = phis
        x0[-1] = _feasible_start_radius(radii, phis, radius_floor)
        opt = minimize(
            objective,
            x0,
            method="SLSQP",
            bounds=bounds,
            constraints=constraints,
            options={"ftol": 1e-12, "maxiter": 1000, "disp": False},
        )
        positions, R = unpack(opt.x)
        min_pair = _min_pair_margin(radii, positions, R)
        min_order = _min_order_margin(positions)
        success = bool(opt.success) and min_pair >= -margin_tol and min_order >= -margin_tol
        candidate = SLSQPCheckResult(
            R=R,
            positions=positions,
            success=success,
            message=str(opt.message),
            min_pair_margin=min_pair,
            min_order_margin=min_order,
            starts_attempted=start_index + 1,
        )
        messages.append(candidate.message)
        if candidate.success and (best is None or candidate.R < best.R):
            best = candidate

    if best is None:
        unique_messages = "; ".join(dict.fromkeys(messages))
        raise AssertionError(
            f"SLSQP fixed-order validation failed for order={radii!r}: {unique_messages}"
        )
    return SLSQPCheckResult(
        R=best.R,
        positions=best.positions,
        success=best.success,
        message=best.message,
        min_pair_margin=best.min_pair_margin,
        min_order_margin=best.min_order_margin,
        starts_attempted=starts,
    )
