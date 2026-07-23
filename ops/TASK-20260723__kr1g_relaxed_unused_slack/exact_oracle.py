"""Independent exact oracle for the relaxed unused-original-edge slack.

After translating ``S_r = {r, ..., n}`` by ``r``, put
``q = n - r + 1``.  For an edge ``{x, y}`` on ``{0, ..., q - 1}``,

    2 Delta = (x + y - (q - 1))**2.

The oracle imports no project code.  It enumerates Hamiltonian cycles modulo
rotation and reversal, removes the at most ``ell`` largest nonnegative edge
slacks, and checks the resulting exact minimum against

    max(ceil(q / 2) - ell, 0) / 2

for every tested ``ell >= 1``.  It separately checks the explicit alternating
low/high (zigzag) cycle.
"""

from fractions import Fraction
from itertools import permutations
from math import factorial


MIN_Q = 3
MAX_Q = 10


def canonical_cycles(q: int):
    """Yield cycles on range(q), once modulo rotation and reversal."""
    for tail in permutations(range(1, q)):
        # Fixing 0 removes rotations.  Exactly one orientation has its first
        # nonzero vertex smaller than its last nonzero vertex.
        if tail[0] < tail[-1]:
            yield (0, *tail)


def doubled_slacks(cycle: tuple[int, ...]) -> tuple[int, ...]:
    """Return the integer values 2*Delta for all cyclic edges."""
    target = len(cycle) - 1
    successors = cycle[1:] + cycle[:1]
    return tuple((u + v - target) ** 2 for u, v in zip(cycle, successors))


def doubled_residual_profile(cycle: tuple[int, ...]) -> tuple[int, ...]:
    """Return exact minima for this cycle after 1, ..., q deletions."""
    ordered = sorted(doubled_slacks(cycle))
    return tuple(
        sum(ordered[: max(len(cycle) - ell, 0)]) for ell in range(1, len(cycle) + 1)
    )


def zigzag_cycle(q: int) -> tuple[int, ...]:
    """Return (0, q-1, 1, q-2, ...) with the middle vertex last."""
    cycle: list[int] = []
    for low in range(q // 2):
        cycle.extend((low, q - 1 - low))
    if q % 2:
        cycle.append(q // 2)
    return tuple(cycle)


def candidate_profile(q: int) -> tuple[Fraction, ...]:
    """Return the claimed exact values for ell = 1, ..., q."""
    half_count = (q + 1) // 2
    return tuple(Fraction(max(half_count - ell, 0), 2) for ell in range(1, q + 1))


def exhaustive_minimum_profile(q: int) -> tuple[tuple[Fraction, ...], int]:
    """Enumerate canonical cycles and return their coordinatewise minima."""
    minima: list[int | None] = [None] * q
    count = 0
    for cycle in canonical_cycles(q):
        count += 1
        for index, value in enumerate(doubled_residual_profile(cycle)):
            if minima[index] is None or value < minima[index]:
                minima[index] = value

    expected_count = factorial(q - 1) // 2
    if count != expected_count:
        raise AssertionError(
            f"q={q}: got {count} canonical cycles, expected {expected_count}"
        )
    if any(value is None for value in minima):
        raise AssertionError(f"q={q}: empty cycle enumeration")
    return tuple(Fraction(value, 2) for value in minima if value is not None), count


def main() -> None:
    total_cycles = 0
    total_cases = 0
    for q in range(MIN_Q, MAX_Q + 1):
        expected = candidate_profile(q)
        exhaustive, count = exhaustive_minimum_profile(q)
        zigzag = tuple(
            Fraction(value, 2) for value in doubled_residual_profile(zigzag_cycle(q))
        )

        if exhaustive != expected:
            raise AssertionError(f"q={q}: exhaustive={exhaustive}, expected={expected}")
        if zigzag != expected:
            raise AssertionError(f"q={q}: zigzag={zigzag}, expected={expected}")

        total_cycles += count
        total_cases += q
        print(f"q={q:2d}  cycles={count:7d}  ell=1..{q}: PASS")

    print(
        f"PASS: {total_cycles} canonical cycles, {total_cases} exact (q, ell) cases, "
        "and every zigzag profile"
    )


if __name__ == "__main__":
    main()
