"""Bounded exact-integer checks for the monotone all-index KR1 lift.

This dossier-local script imports only the Python standard library.  It
checks residue coverage, the lift offset, both exact KR1 formulas, and the
common cubic coefficient.  It constructs and searches no order family.  The
finite checks corroborate the arithmetic; the cancellation proof is the
all-index argument.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction


MIN_N = 7
MAX_N = 1006
EXPECTED_OFFSET_BY_MOD_5 = (1, 0, 4, 3, 2)


def lifted_index(n: int) -> int:
    """Return ``5 * ceil((n - 1) / 5) + 1`` using integers only."""
    return 5 * ((n + 3) // 5) + 1


def kr1_k_formula(k: int) -> int:
    if k < 2:
        raise ValueError(f"KR1 requires k >= 2: {k}")
    epsilon = k % 2
    numerator = 857 * k**3 + 891 * k**2 + 214 * k + epsilon * (27 * k**2 - 51 * k - 18)
    assert numerator % 24 == 0
    return numerator // 24


def kr1_n_formula(n: int) -> int:
    if n < 11:
        raise ValueError(f"KR1 requires n >= 11: {n}")
    if n % 10 == 1:
        numerator = 857 * n**3 + 1884 * n**2 - 989 * n - 1752
    elif n % 10 == 6:
        numerator = 857 * n**3 + 2019 * n**2 - 2534 * n - 2592
    else:
        raise ValueError(f"KR1 requires n congruent to 1 or 6 modulo 10: {n}")
    assert numerator % 3000 == 0
    return numerator // 3000


def main() -> None:
    assert lifted_index(6) == 6  # k=1 is outside the proved KR1 domain.
    assert lifted_index(7) == 11  # First lift into the proved k>=2 domain.
    for formula, value in ((kr1_k_formula, 1), (kr1_n_formula, 6)):
        try:
            formula(value)
        except ValueError:
            pass
        else:
            raise AssertionError("unsupported KR1 formula domain was accepted")

    boundary = tuple(
        (
            n,
            lifted_index(n),
            lifted_index(n) - n,
            kr1_n_formula(lifted_index(n)),
        )
        for n in range(7, 17)
    )
    assert boundary == (
        (7, 11, 4, 452),
        (8, 11, 3, 452),
        (9, 11, 2, 452),
        (10, 11, 1, 452),
        (11, 11, 0, 452),
        (12, 16, 4, 1328),
        (13, 16, 3, 1328),
        (14, 16, 2, 1328),
        (15, 16, 1, 1328),
        (16, 16, 0, 1328),
    )

    residue_counts: Counter[int] = Counter()
    offset_counts: Counter[int] = Counter()
    branch_counts: Counter[int] = Counter()
    lifted_values: set[int] = set()
    scores_by_residue: defaultdict[int, list[int]] = defaultdict(list)

    for n in range(MIN_N, MAX_N + 1):
        lifted = lifted_index(n)
        offset = lifted - n
        k = (lifted - 1) // 5

        assert lifted % 5 == 1
        assert lifted >= n
        assert 0 <= offset <= 4
        assert offset == EXPECTED_OFFSET_BY_MOD_5[n % 5]
        assert all(candidate % 5 != 1 for candidate in range(n, lifted))
        assert k >= 2

        score = kr1_k_formula(k)
        assert score == kr1_n_formula(lifted)

        residue_counts[n % 10] += 1
        offset_counts[offset] += 1
        branch_counts[lifted % 10] += 1
        lifted_values.add(lifted)
        scores_by_residue[n % 10].append(score)

    assert residue_counts == Counter({residue: 100 for residue in range(10)})
    assert offset_counts == Counter({offset: 200 for offset in range(5)})
    assert branch_counts == Counter({1: 500, 6: 500})
    assert len(lifted_values) == 200

    third_difference_checks = 0
    for residue in range(10):
        values = scores_by_residue[residue]
        assert len(values) == 100
        for a, b, c, d in zip(values, values[1:], values[2:], values[3:]):
            assert d - 3 * c + 3 * b - a == 1714
            third_difference_checks += 1

    coefficient = Fraction(1714, 6 * 10**3)
    assert coefficient == Fraction(857, 3000)
    assert third_difference_checks == 970

    print("KR1 monotone lift exact-integer diagnostic: PASS")
    print("lifted n rows: 1000 (n=7..1006)")
    print("n modulo 10 coverage: 10 residues x 100")
    print("lift offsets 0..4: 200 each")
    print("KR1 N modulo 10 branches: 1 -> 500, 6 -> 500")
    print("distinct lifted KR1 rows: 200")
    print("third finite differences: 970 checks, all 1714")
    print("all-index leading coefficient: 857/3000")


if __name__ == "__main__":
    main()
