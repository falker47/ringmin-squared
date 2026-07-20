"""Bounded exact checks for the odd-v residue-two PG49-star analogue.

This standalone standard-library diagnostic constructs only the prescribed
map on the odd v = 2*m + 1 branch of the existing residue-two e = 2
scaffold, where n = 10*m + 7.  It imports no project helper and performs no
candidate generation, matching, path-assignment, order, subset, or K search.
Exact integer comparisons check the scaffold and orientations, map formula,
image partition, literal local Ferrers relation, residual Hall support,
empty ranges, minimum row, cyclic closure, and every unordered cyclic pair
of the one fixed order within the declared finite limits.
"""

FORMULA_MAX_M = 1000
RELATION_MAX_M = 40
SCORE_MAX_M = 80


def ceil_div(numerator: int, denominator: int) -> int:
    """Return the ceiling of a nonnegative exact quotient."""
    assert numerator >= 0
    assert denominator > 0
    return (numerator + denominator - 1) // denominator


def scaffold(
    m: int,
) -> tuple[int, int, int, int, tuple[tuple[int, ...], ...]]:
    """Return d, D, n, J, and the literal odd-v residue-two paths."""
    if m < 1:
        raise ValueError("the symbolic branch requires m >= 1")

    d = 8 * m + 8
    D = d - 1
    n = 10 * m + 7
    threshold = d * (d - 2) // 2

    paths: list[tuple[int, ...]] = [
        (D - 1 - 2 * k, 4 * m + 4 + k, D - 2 - 2 * k) for k in range(m + 1)
    ]
    paths.extend((4 * m + 4 + k,) for k in range(m + 1, 2 * m + 1))
    result = tuple(paths)

    assert d == 8 * m + 8
    assert D == 8 * m + 7
    assert n == 10 * m + 7
    assert threshold == (D * D - 1) // 2
    assert len(result) == 2 * m + 1
    assert sum(len(path) == 3 for path in result) == m + 1
    assert sum(len(path) == 1 for path in result) == m
    assert all(len(path) != 2 for path in result)
    middle_labels = [label for path in result for label in path]
    assert sorted(middle_labels) == list(range(4 * m + 4, D))
    return d, D, n, threshold, result


def thresholds(m: int, D: int) -> tuple[int, ...]:
    """Return the literal local Ferrers column thresholds."""
    result: list[int] = []
    for j in range(2 * m + 1):
        if j <= 1:
            result.append(0)
        else:
            result.append(ceil_div((j - 1) * (D - 1), 2 * (D + j)))
    return tuple(result)


def closing_threshold(m: int) -> int:
    """Return the exact threshold of the genuine closing column."""
    return ceil_div((2 * m - 1) * (4 * m + 3), 10 * m + 7)


def candidate(m: int) -> tuple[int, ...]:
    """Return the sole fixed path-to-gap map from the task statement."""
    q = closing_threshold(m)
    alpha: list[int | None] = [None] * (2 * m + 1)

    for j in range(q):
        alpha[j] = j
    for j in range(q, m):
        alpha[j] = j + 1
    for j in range(m, 2 * m):
        alpha[j] = 3 * m - j
    alpha[2 * m] = q

    assert all(value is not None for value in alpha)
    return tuple(int(value) for value in alpha)


def local_word(
    m: int,
    D: int,
    paths: tuple[tuple[int, ...], ...],
    k: int,
    j: int,
) -> tuple[int, ...]:
    """Build the literal gap word for placing oriented path k in gap j."""
    next_j = (j + 1) % (2 * m + 1)
    return (
        D + j,
        4 * m + 2 - 2 * j,
        *paths[k],
        4 * m + 3 - 2 * next_j,
        D + next_j,
    )


def locally_allowed(word: tuple[int, ...], threshold: int) -> bool:
    """Check every one- and two-step pair in one literal cyclic gap word."""
    for distance in (1, 2):
        for start in range(len(word) - distance):
            if word[start] * word[start + distance] > distance * threshold:
                return False
    return True


def residual_hall(
    k: int,
    j: int,
    kappas: tuple[int, ...],
) -> tuple[bool, int]:
    """Evaluate every residual-suffix Hall inequality for one fixed edge."""
    valid = True
    checks = 0
    for r, kappa_r in enumerate(kappas):
        if r == j:
            continue
        left = kappa_r + int(k >= kappa_r)
        right = r + int(j > r)
        valid = valid and left <= right
        checks += 1
    return valid, checks


def expanded_order(m: int) -> tuple[int, ...]:
    """Expand the sole prescribed map into its cyclic core order."""
    _d, D, n, _threshold, paths = scaffold(m)
    alpha = candidate(m)
    order: list[int] = []
    for j, k in enumerate(alpha):
        next_j = (j + 1) % (2 * m + 1)
        order.extend((D + j, 4 * m + 2 - 2 * j))
        order.extend(paths[k])
        order.append(4 * m + 3 - 2 * next_j)
    result = tuple(order)

    assert len(result) == n - 1
    assert set(result) == set(range(2, n + 1))
    return result


def check_formula_row(m: int) -> int:
    """Check the scaffold, q formula, fixed map, images, and boundaries."""
    d, D, n, threshold, paths = scaffold(m)
    kappas = thresholds(m, D)
    alpha = candidate(m)
    q = closing_threshold(m)

    assert d == 8 * m + 8
    assert n == 10 * m + 7
    assert threshold == d * (d - 2) // 2
    assert kappas[0] == 0
    assert kappas[1] == 0
    assert kappas[2] == 1
    assert all(kappas[j] <= kappas[j + 1] for j in range(2 * m))
    assert all(1 <= kappas[j] <= j - 1 for j in range(2, 2 * m + 1))
    assert kappas[-1] == q
    assert 1 <= q <= m

    q_numerator = (2 * m - 1) * (4 * m + 3)
    q_denominator = 10 * m + 7
    assert (q - 1) * q_denominator < q_numerator <= q * q_denominator
    assert q == (4 * m + 3) // 5
    assert (q == m) == (m <= 3)

    image_blocks = (
        set(range(q)),
        set(range(q + 1, m + 1)),
        set(range(m + 1, 2 * m + 1)),
        {q},
    )
    image_union: set[int] = set()
    for block in image_blocks:
        assert not image_union.intersection(block)
        image_union.update(block)
    assert image_union == set(range(2 * m + 1))
    assert set(alpha) == image_union
    assert len(alpha) == len(set(alpha))

    assert alpha[-1] == q == kappas[-1]
    assert tuple(alpha[j] for j in range(m, 2 * m)) == tuple(range(2 * m, m, -1))
    assert all(len(paths[alpha[j]]) == 1 for j in range(m, 2 * m))
    assert all(alpha[j] >= kappas[j] for j in range(2 * m + 1))
    assert all(
        k >= kappas[j] for j in range(2 * m + 1) for k in range(m + 1, 2 * m + 1)
    )
    assert (tuple(range(q, m)) == ()) == (m <= 3)
    assert (image_blocks[1] == set()) == (m <= 3)
    assert len(tuple(range(m, 2 * m))) == m
    assert all(len(path) != 2 for path in paths)

    closing_word = local_word(m, D, paths, alpha[-1], 2 * m)
    assert closing_word == (n, 2, *paths[q], 4 * m + 3, D)

    if m == 1:
        assert (d, D, n, threshold, q) == (16, 15, 17, 112, 1)
        assert kappas == (0, 0, 1)
        assert paths == ((14, 8, 13), (12, 9, 11), (10,))
        assert alpha == (0, 2, 1)
        assert tuple(range(q, m)) == ()
        assert image_blocks[1] == set()
        assert tuple(alpha[j] for j in range(m, 2 * m)) == (2,)
        assert closing_word == (17, 2, 12, 9, 11, 7, 15)
        assert expanded_order(m) == (
            15,
            6,
            14,
            8,
            13,
            5,
            16,
            4,
            10,
            3,
            17,
            2,
            12,
            9,
            11,
            7,
        )

    return len(alpha)


def check_relation_row(m: int) -> tuple[int, int]:
    """Check the literal local relation and its exact residual Hall support."""
    _d, D, _n, threshold, paths = scaffold(m)
    kappas = thresholds(m, D)
    relation_checks = 0
    hall_checks = 0

    for j in range(2 * m + 1):
        for k in range(2 * m + 1):
            direct_local = locally_allowed(local_word(m, D, paths, k, j), threshold)
            expected_local = k >= kappas[j]
            assert direct_local == expected_local
            relation_checks += 1

            hall_valid, row_checks = residual_hall(k, j, kappas)
            direct_extendible = direct_local and hall_valid
            assert direct_extendible == expected_local
            hall_checks += row_checks

    return relation_checks, hall_checks


def check_score_row(m: int) -> int:
    """Check every unordered pair at its exact circular positional distance."""
    _d, D, n, threshold, paths = scaffold(m)
    alpha = candidate(m)
    order = expanded_order(m)
    size = len(order)
    pair_checks = 0
    best_numerator = -1
    best_denominator = 1

    for left in range(size):
        for right in range(left + 1, size):
            linear_distance = right - left
            distance = min(linear_distance, size - linear_distance)
            product = order[left] * order[right]
            assert product <= distance * threshold
            if product * best_denominator > best_numerator * distance:
                best_numerator = product
                best_denominator = distance
            pair_checks += 1

    A0, c0, _B0 = paths[0]
    positions = {label: index for index, label in enumerate(order)}
    internal_distance = min(
        (positions[A0] - positions[c0]) % size,
        (positions[c0] - positions[A0]) % size,
    )
    assert internal_distance == 1
    assert A0 * c0 == threshold
    assert best_numerator == threshold * best_denominator

    q = closing_threshold(m)
    closing = local_word(m, D, paths, alpha[-1], 2 * m)
    assert closing == (n, 2, *paths[q], 4 * m + 3, D)
    assert set(order) == set(range(2, n + 1))
    return pair_checks


def main() -> None:
    """Run all declared bounded exact checks."""
    image_entries = sum(check_formula_row(m) for m in range(1, FORMULA_MAX_M + 1))

    relation_checks = 0
    hall_checks = 0
    for m in range(1, RELATION_MAX_M + 1):
        row_relation, row_hall = check_relation_row(m)
        relation_checks += row_relation
        hall_checks += row_hall

    pair_checks = sum(check_score_row(m) for m in range(1, SCORE_MAX_M + 1))

    print("odd-v residue-two PG49-star W diagnostic: PASS")
    print(f"formula/Ferrers rows: {FORMULA_MAX_M} (m=1..{FORMULA_MAX_M})")
    print(f"candidate image entries checked: {image_entries}")
    print(f"local-relation rows: {RELATION_MAX_M} (m=1..{RELATION_MAX_M})")
    print(f"literal local relation checks: {relation_checks}")
    print(f"residual Hall inequality checks: {hall_checks}")
    print(f"full all-pairs score rows: {SCORE_MAX_M} (m=1..{SCORE_MAX_M})")
    print(f"unordered cyclic pairs checked: {pair_checks}")
    print("q, images, empty ranges, no doubleton, m=1, and closure verified")


if __name__ == "__main__":
    main()
