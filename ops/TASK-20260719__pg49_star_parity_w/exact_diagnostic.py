"""Bounded exact checks for the odd-v PG49-star parity analogue.

This standalone diagnostic constructs only the a-priori fixed map on
``n = 10*m + 8``.  It imports no project helper, searches no cyclic order,
and enumerates no path permutation or matching.  Integer comparisons check
the local Ferrers relation, residual Hall support, image formula, cyclic
all-pairs product-distance score, and all declared boundary identities.
"""

RELATION_MAX_M = 40
SCORE_MAX_M = 80
FORMULA_MAX_M = 1000


def ceil_div(numerator: int, denominator: int) -> int:
    """Return the ceiling of a nonnegative exact quotient."""
    return (numerator + denominator - 1) // denominator


def scaffold(m: int) -> tuple[int, int, int, tuple[tuple[int, ...], ...]]:
    """Return ``d, n, T, paths`` for the odd-v e=4 scaffold."""
    if m < 1:
        raise ValueError("the symbolic branch requires m >= 1")
    d = 8 * m + 8
    n = 10 * m + 8
    threshold = d * (d - 1) // 2

    paths: list[tuple[int, ...]] = [
        (d - 1 - 2 * k, 4 * m + 4 + k, d - 2 - 2 * k) for k in range(m + 1)
    ]
    paths.append((5 * m + 5, 5 * m + 6))
    paths.extend((4 * m + 5 + k,) for k in range(m + 2, 2 * m + 1))
    result = tuple(paths)
    assert len(result) == 2 * m + 1

    middle_labels = [label for path in result for label in path]
    assert sorted(middle_labels) == list(range(4 * m + 4, 8 * m + 8))
    return d, n, threshold, result


def thresholds(m: int, d: int) -> tuple[int, ...]:
    """Return the literal odd Ferrers column thresholds."""
    return tuple(ceil_div(j * (d - 1), 2 * (d + j)) for j in range(2 * m + 1))


def candidate(m: int) -> tuple[int, ...]:
    """Return the fixed search-free path-to-gap map (PGODD-6)."""
    q = (4 * m + 5) // 5
    alpha: list[int | None] = [None] * (2 * m + 1)
    alpha[0] = 0
    for j in range(1, q):
        alpha[j] = j
    for j in range(q, m + 1):
        alpha[j] = j + 1
    for j in range(m + 1, 2 * m):
        alpha[j] = 3 * m + 1 - j
    alpha[2 * m] = q
    assert all(value is not None for value in alpha)
    return tuple(int(value) for value in alpha)


def local_word(
    m: int,
    d: int,
    paths: tuple[tuple[int, ...], ...],
    k: int,
    j: int,
) -> tuple[int, ...]:
    """Build the literal constant-size word for path ``k`` in gap ``j``."""
    next_j = (j + 1) % (2 * m + 1)
    return (
        d + j,
        4 * m + 2 - 2 * j,
        *paths[k],
        4 * m + 3 - 2 * next_j,
        d + next_j,
    )


def locally_allowed(word: tuple[int, ...], threshold: int) -> bool:
    """Check every one- and two-step pair in one literal gap word."""
    for distance in (1, 2):
        for start in range(len(word) - distance):
            if word[start] * word[start + distance] > distance * threshold:
                return False
    return True


def hall_extendible(k: int, j: int, kappas: tuple[int, ...]) -> bool:
    """Evaluate the exact residual-suffix Hall inequalities (PGODD-19)."""
    for r, kappa_r in enumerate(kappas):
        if r == j:
            continue
        left = kappa_r + int(k >= kappa_r)
        right = r + int(j > r)
        if left > right:
            return False
    return True


def expanded_order(m: int) -> tuple[int, ...]:
    """Expand the single prescribed candidate into its cyclic core order."""
    d, n, _threshold, paths = scaffold(m)
    alpha = candidate(m)
    order: list[int] = []
    for j, k in enumerate(alpha):
        next_j = (j + 1) % (2 * m + 1)
        order.extend((d + j, 4 * m + 2 - 2 * j))
        order.extend(paths[k])
        order.append(4 * m + 3 - 2 * next_j)
    result = tuple(order)
    assert len(result) == n - 1
    assert set(result) == set(range(2, n + 1))
    return result


def check_formula_row(m: int) -> int:
    """Check thresholds, image blocks, and every candidate Ferrers edge."""
    d, _n, _threshold, _paths = scaffold(m)
    kappas = thresholds(m, d)
    alpha = candidate(m)
    q = (4 * m + 5) // 5

    assert kappas[0] == 0
    assert kappas[1] == 1
    assert all(kappas[j] <= j - 1 for j in range(2, 2 * m + 1))
    assert all(kappas[j] <= kappas[j + 1] for j in range(2 * m))
    assert kappas[2 * m] == q
    assert 1 <= q <= m

    blocks = (
        {0},
        set(range(1, q)),
        set(range(q + 1, m + 2)),
        set(range(m + 2, 2 * m + 1)),
        {q},
    )
    union: set[int] = set()
    for block in blocks:
        assert not union.intersection(block)
        union.update(block)
    assert union == set(range(2 * m + 1))
    assert set(alpha) == union
    assert len(alpha) == len(set(alpha))
    assert alpha[2 * m] == q == kappas[2 * m]
    assert all(k >= kappas[j] for j, k in enumerate(alpha))

    if m == 1:
        assert kappas == (0, 1, 1)
        assert alpha == (0, 2, 1)
    return len(alpha)


def check_relation_row(m: int) -> tuple[int, int]:
    """Check the exact local suffix relation and exact PG49 Hall support."""
    d, _n, threshold, paths = scaffold(m)
    kappas = thresholds(m, d)
    relation_checks = 0
    hall_checks = 0
    for j in range(2 * m + 1):
        for k in range(2 * m + 1):
            direct_local = locally_allowed(local_word(m, d, paths, k, j), threshold)
            expected_local = k >= kappas[j]
            assert direct_local == expected_local
            relation_checks += 1

            direct_hall = direct_local and hall_extendible(k, j, kappas)
            expected_hall = expected_local and (j > 0 or k == 0)
            assert direct_hall == expected_hall
            hall_checks += 2 * m
    return relation_checks, hall_checks


def check_score_row(m: int) -> int:
    """Check every unordered pair in the fixed cyclic order with integers."""
    d, n, threshold, _paths = scaffold(m)
    order = expanded_order(m)
    size = len(order)
    pair_checks = 0
    best_numerator = -1
    best_denominator = 1

    for left in range(size):
        for right in range(left + 1, size):
            linear = right - left
            distance = min(linear, size - linear)
            product = order[left] * order[right]
            assert product <= distance * threshold
            if product * best_denominator > best_numerator * distance:
                best_numerator = product
                best_denominator = distance
            pair_checks += 1

    assert best_numerator == threshold * best_denominator
    positions = {label: index for index, label in enumerate(order)}
    a0 = d - 1
    c0 = d // 2
    assert (
        min(
            (positions[a0] - positions[c0]) % size,
            (positions[c0] - positions[a0]) % size,
        )
        == 1
    )
    assert a0 * c0 == threshold
    assert (
        min(
            (positions[d] - positions[a0]) % size,
            (positions[a0] - positions[d]) % size,
        )
        == 2
    )
    assert d * a0 == 2 * threshold
    assert set(order) == set(range(2, n + 1))
    return pair_checks


def main() -> None:
    """Run the declared bounded exact checks."""
    formula_entries = sum(check_formula_row(m) for m in range(1, FORMULA_MAX_M + 1))

    relation_checks = 0
    hall_checks = 0
    for m in range(1, RELATION_MAX_M + 1):
        row_relation, row_hall = check_relation_row(m)
        relation_checks += row_relation
        hall_checks += row_hall

    pair_checks = sum(check_score_row(m) for m in range(1, SCORE_MAX_M + 1))

    print("odd-v PG49-star parity W diagnostic: PASS")
    print(f"formula/Ferrers rows: {FORMULA_MAX_M} (m=1..{FORMULA_MAX_M})")
    print(f"candidate image entries checked: {formula_entries}")
    print(f"local-relation rows: {RELATION_MAX_M} (m=1..{RELATION_MAX_M})")
    print(f"local relation checks: {relation_checks}")
    print(f"residual Hall inequality checks: {hall_checks}")
    print(f"full all-pairs score rows: {SCORE_MAX_M} (m=1..{SCORE_MAX_M})")
    print(f"unordered cyclic pairs checked: {pair_checks}")
    print("minimum boundary, doubleton, singleton reversal, and closure verified")


if __name__ == "__main__":
    main()
