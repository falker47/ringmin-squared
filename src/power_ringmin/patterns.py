"""Generic cyclic-order pattern helpers for comparison experiments.

Adapted from upstream Ringmin commit
cc0327400819fe06b230d967cdcbafffe1648317 under the MIT license.
"""

from __future__ import annotations

from collections.abc import Iterable
import json
from pathlib import Path


def _sorted_values(values: Iterable[int | float]) -> tuple[int | float, ...]:
    result = tuple(sorted(values))
    if len(set(result)) != len(result):
        raise ValueError(f"pattern values must be distinct: {result!r}")
    return result


def sequential(values: Iterable[int | float]) -> tuple[int | float, ...]:
    """Return values in increasing order."""
    return _sorted_values(values)


def zigzag(values: Iterable[int | float]) -> tuple[int | float, ...]:
    """Alternate largest remaining, smallest remaining."""
    v = _sorted_values(values)
    out: list[int | float] = []
    lo = 0
    hi = len(v) - 1
    while lo <= hi:
        out.append(v[hi])
        hi -= 1
        if lo <= hi:
            out.append(v[lo])
            lo += 1
    return tuple(out)


def interleave(values: Iterable[int | float]) -> tuple[int | float, ...]:
    """Return the generic interleaved comparison order."""
    v = _sorted_values(values)
    m = len(v)
    used: set[int] = set()
    mid = (m + 1) // 2

    def append_index(target: list[int | float], idx_1_based: int) -> None:
        idx = idx_1_based - 1
        if 0 <= idx < m and idx not in used:
            used.add(idx)
            target.append(v[idx])

    arm_a: list[int | float] = []
    arm_b: list[int | float] = []

    append_index(arm_a, m)
    offset = 0
    while True:
        before = len(used)
        low_a = 1 + 2 * offset
        high_a = m - 1 - 2 * offset
        low_b = 2 + 2 * offset
        high_b = m - 2 - 2 * offset
        if low_a <= mid:
            append_index(arm_a, low_a)
        if high_a > mid:
            append_index(arm_a, high_a)
        if low_b <= mid:
            append_index(arm_b, low_b)
        if high_b > mid:
            append_index(arm_b, high_b)
        offset += 1
        if len(used) == before:
            break
    if len(used) != m:
        missing = [v[i] for i in range(m) if i not in used]
        raise AssertionError(f"interleave failed to consume all values: {missing!r}")
    return tuple(arm_a + list(reversed(arm_b)))


def supnick_max_tour(values: Iterable[int | float]) -> tuple[int | float, ...]:
    """Published Supnick maximum-tour form, equivalent to interleave as a cycle."""
    v = _sorted_values(values)
    m = len(v)
    mid = (m + 1) // 2
    used: set[int] = set()
    first_arm: list[int | float] = []
    second_arm: list[int | float] = []

    def append_index(target: list[int | float], idx_1_based: int) -> None:
        idx = idx_1_based - 1
        if 0 <= idx < m and idx not in used:
            used.add(idx)
            target.append(v[idx])

    offset = 0
    while True:
        before = len(used)
        low = 1 + 2 * offset
        high = m - 1 - 2 * offset
        if low <= mid:
            append_index(first_arm, low)
        if high > mid:
            append_index(first_arm, high)
        offset += 1
        if len(used) == before:
            break

    offset = 0
    while True:
        before = len(used)
        low = 2 + 2 * offset
        high = m - 2 - 2 * offset
        if low <= mid:
            append_index(second_arm, low)
        if high > mid:
            append_index(second_arm, high)
        offset += 1
        if len(used) == before:
            break

    append_index(first_arm, m)
    if len(used) != m:
        missing = [v[i] for i in range(m) if i not in used]
        raise AssertionError(f"supnick_max_tour failed to consume all values: {missing!r}")
    return tuple(first_arm[:-1] + list(reversed(second_arm)) + first_arm[-1:])


def supnick_min_tour(values: Iterable[int | float]) -> tuple[int | float, ...]:
    """Supnick minimum-tour order: odd indexed values ascending, evens descending."""
    v = _sorted_values(values)
    odds = [v[i] for i in range(0, len(v), 2)]
    evens_desc = [v[i] for i in range(len(v) - 1, 0, -1) if (i + 1) % 2 == 0]
    return tuple(odds + evens_desc)


def load_json_orders(path: str | Path) -> list[tuple[int | float, ...]]:
    """Load user-supplied cyclic orders from a JSON file."""
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(raw, dict):
        raw_orders = raw.get("orders")
    else:
        raw_orders = raw
    if not isinstance(raw_orders, list):
        raise ValueError("JSON orders must be a list or an object with an 'orders' list")
    return [tuple(order) for order in raw_orders]
