"""Geometric primitives for central-circle packing.

Adapted from upstream Ringmin commit
cc0327400819fe06b230d967cdcbafffe1648317 under the MIT license.
"""

from __future__ import annotations

from collections.abc import Iterable
import math

TAU = 2.0 * math.pi


def quadratic_radii(n: int) -> tuple[int, ...]:
    """Return the Power-Ringmin radii ``1^2, ..., n^2``."""
    if n < 1:
        raise ValueError(f"n must be positive, got {n!r}")
    return tuple(k * k for k in range(1, n + 1))


def as_order(order: Iterable[int | float]) -> tuple[float, ...]:
    """Return an immutable radius order as floats."""
    values = tuple(float(x) for x in order)
    if not values:
        raise ValueError("order must contain at least one radius")
    if any(r <= 0.0 for r in values):
        raise ValueError(f"radii must be positive: {values!r}")
    return values


def theta(R: float, a: float, b: float) -> float:
    """Required angular separation for two outer circles at central radius R."""
    if R <= 0.0:
        raise ValueError(f"R must be positive, got {R!r}")
    if a <= 0.0 or b <= 0.0:
        raise ValueError(f"radii must be positive, got {a!r}, {b!r}")

    x2 = (a * b) / ((R + a) * (R + b))
    if not (0.0 < x2 < 1.0):
        raise AssertionError(
            f"theta argument must lie in (0, 1): R={R!r}, a={a!r}, b={b!r}, x2={x2!r}"
        )
    value = 2.0 * math.asin(math.sqrt(x2))
    if not (0.0 < value < math.pi):
        raise AssertionError(
            f"theta must lie in (0, pi): R={R!r}, a={a!r}, b={b!r}, theta={value!r}"
        )
    return value


def cyclic_pairs(order: Iterable[int | float]) -> tuple[tuple[float, float], ...]:
    """Return adjacent cyclic radius pairs."""
    radii = as_order(order)
    return tuple((radii[i], radii[(i + 1) % len(radii)]) for i in range(len(radii)))


def cycle_equivalent(a: Iterable[int | float], b: Iterable[int | float]) -> bool:
    """True when two cyclic orders agree up to rotation or reflection."""
    aa = tuple(a)
    bb = tuple(b)
    if len(aa) != len(bb):
        return False
    if not aa:
        return True
    doubled = aa + aa
    rev = tuple(reversed(aa))
    doubled_rev = rev + rev
    return any(doubled[i : i + len(bb)] == bb for i in range(len(bb))) or any(
        doubled_rev[i : i + len(bb)] == bb for i in range(len(bb))
    )
