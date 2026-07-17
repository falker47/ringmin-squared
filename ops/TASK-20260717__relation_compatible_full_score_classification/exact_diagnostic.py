"""Polynomial exact check of the arbitrary-path distance-three theorem.

The scan ranges over local gap/path/next-path types, not over path
permutations or matchings.  Two explicit PG46 shifts separately witness the
sharp cases inside the relation-compatible class.
"""

from fractions import Fraction


ROWS = (3, 4, 9, 34)


def parameters(m: int) -> tuple[int, int, int, int]:
    """Return ``(n, d, T, v)`` for the residue-three branch."""
    n = 10 * m + 3
    d = 8 * m + 4
    return n, d, d * (d - 1) // 2, 2 * m


def path(m: int, k: int) -> tuple[int, ...]:
    """Return the retained oriented middle path ``P_k``."""
    _, d, _, v = parameters(m)
    assert 0 <= k < v
    if k <= m:
        return d - 1 - 2 * k, 4 * m + 2 + k, d - 2 - 2 * k
    return (4 * m + 2 + k,)


def path_type(m: int, k: int) -> str:
    """Classify a path as a triple or singleton."""
    return "triple" if k <= m else "singleton"


def terminal(m: int, j: int) -> int:
    """Return the cyclic terminal label ``E_j``."""
    _, d, _, v = parameters(m)
    return d + (j % v)


def left_low(m: int, j: int) -> int:
    """Return the cyclic low label ``lambda_j``."""
    *_, v = parameters(m)
    return 4 * m - 2 * (j % v)


def right_low(m: int, j: int) -> int:
    """Return the cyclic low label ``rho_j``."""
    *_, v = parameters(m)
    return 4 * m + 1 - 2 * (j % v)


def local_word(m: int, j: int, k: int, h: int) -> tuple[int, ...]:
    """Build enough of gaps ``j`` and ``j+1`` to read every current start."""
    *_, v = parameters(m)
    jp = (j + 1) % v
    return (
        terminal(m, j),
        left_low(m, j),
        *path(m, k),
        right_low(m, jp),
        terminal(m, jp),
        left_low(m, jp),
        *path(m, h),
    )


def direct_distance_three_pairs(
    m: int, j: int, k: int, h: int
) -> tuple[tuple[int, int], ...]:
    """Read the current gap's distance-three pairs directly from its word."""
    word = local_word(m, j, k, h)
    starts = len(path(m, k)) + 3
    return tuple((word[index], word[index + 3]) for index in range(starts))


def classified_distance_three_pairs(
    m: int, j: int, k: int, h: int
) -> tuple[tuple[int, int], ...]:
    """Return the symbolic PG50--PG51 classification."""
    *_, v = parameters(m)
    jp = (j + 1) % v
    current = path(m, k)
    first_next = path(m, h)[0]
    if len(current) == 3:
        a_k, c_k, b_k = current
        return (
            (terminal(m, j), c_k),
            (left_low(m, j), b_k),
            (a_k, right_low(m, jp)),
            (c_k, terminal(m, jp)),
            (b_k, left_low(m, jp)),
            (right_low(m, jp), first_next),
        )
    (x_k,) = current
    return (
        (terminal(m, j), right_low(m, jp)),
        (left_low(m, j), terminal(m, jp)),
        (x_k, left_low(m, jp)),
        (right_low(m, jp), first_next),
    )


def kappa(m: int, j: int) -> int:
    """Return the exact Ferrers threshold in column ``j``."""
    _, d, _, _ = parameters(m)
    numerator = j * (d - 1)
    denominator = 2 * (d + j)
    return (numerator + denominator - 1) // denominator


def relation_compatible(m: int, alpha: tuple[int, ...]) -> bool:
    """Check bijectivity and every Ferrers edge without matching search."""
    *_, v = parameters(m)
    return sorted(alpha) == list(range(v)) and all(
        alpha[j] >= kappa(m, j) for j in range(v)
    )


def pg46_shift(m: int, j: int) -> tuple[int, ...]:
    """Construct the PG46 witness with target path ``P_m`` in ``G_j``."""
    *_, v = parameters(m)
    assert m < j < v
    alpha = list(range(v))
    for index in range(m, j):
        alpha[index] = index + 1
    alpha[j] = m
    return tuple(alpha)


def core_order(m: int, alpha: tuple[int, ...]) -> tuple[int, ...]:
    """Expand a prescribed path-to-gap bijection into its cyclic core order."""
    n, _, _, v = parameters(m)
    order: list[int] = []
    for j, k in enumerate(alpha):
        order.extend((terminal(m, j), left_low(m, j)))
        order.extend(path(m, k))
        order.append(right_low(m, (j + 1) % v))
    assert len(order) == n - 1
    assert sorted(order) == list(range(2, n + 1))
    return tuple(order)


def score_classes(
    order: tuple[int, ...],
) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    """Return maxima at distance at most two, exactly three, at least four, and all."""
    length = len(order)
    by_short = Fraction(0)
    by_three = Fraction(0)
    by_long = Fraction(0)
    overall = Fraction(0)
    for left in range(length):
        for right in range(left + 1, length):
            forward = right - left
            distance = min(forward, length - forward)
            score = Fraction(order[left] * order[right], distance)
            overall = max(overall, score)
            if distance <= 2:
                by_short = max(by_short, score)
            elif distance == 3:
                by_three = max(by_three, score)
            else:
                by_long = max(by_long, score)
    return by_short, by_three, by_long, overall


def check_row(m: int) -> tuple[int, int, int]:
    """Check one fixed row and return diagnostic counts."""
    n, d, threshold, v = parameters(m)
    product_bound = n * (5 * m + 2)
    assert 3 * threshold - product_bound == 46 * m * m + 49 * m + 12
    assert 4 * threshold - n * (n - 1) == 28 * m * m + 62 * m + 18
    assert n * (5 * m + 2) - (4 * m + 1) * (d - 1) == (18 * m * m + 15 * m + 3)
    assert 6 * (m + 1) + 4 * (m - 1) == n - 1

    transition_types: set[tuple[str, str]] = set()
    equality_positions: set[tuple[int, int]] = set()
    local_words = 0
    for j in range(v):
        for k in range(v):
            for h in range(v):
                if h == k:
                    continue
                direct = direct_distance_three_pairs(m, j, k, h)
                classified = classified_distance_three_pairs(m, j, k, h)
                assert direct == classified
                assert len(direct) == (6 if k <= m else 4)
                assert all(left * right <= product_bound for left, right in direct)
                if any(left * right == product_bound for left, right in direct):
                    equality_positions.add((j, k))
                transition_types.add((path_type(m, k), path_type(m, h)))
                local_words += 1

    assert transition_types == {
        ("triple", "triple"),
        ("triple", "singleton"),
        ("singleton", "triple"),
        ("singleton", "singleton"),
    }
    assert equality_positions == {(v - 2, m), (v - 1, m)}

    closing_cases = 0
    for k in range(1, v):
        if k < kappa(m, v - 1):
            continue
        closing = classified_distance_three_pairs(m, v - 1, k, 0)
        if k <= m:
            a_k, c_k, b_k = path(m, k)
            expected = (
                (n, c_k),
                (2, b_k),
                (a_k, 4 * m + 1),
                (c_k, d),
                (b_k, 4 * m),
                (4 * m + 1, d - 1),
            )
        else:
            (x_k,) = path(m, k)
            expected = (
                (n, 4 * m + 1),
                (2, d),
                (x_k, 4 * m),
                (4 * m + 1, d - 1),
            )
        assert closing == expected
        closing_cases += 1

    for target_gap in (v - 2, v - 1):
        alpha = pg46_shift(m, target_gap)
        assert relation_compatible(m, alpha)
        assert alpha[0] == 0
        assert alpha[target_gap] == m
        short, three, long, overall = score_classes(core_order(m, alpha))
        assert short == threshold
        assert three == Fraction(product_bound, 3)
        assert long < threshold
        assert overall == threshold

    return local_words, closing_cases, len(transition_types)


def main() -> None:
    """Run all fixed polynomial rows."""
    print("m local_words closing_cases transition_types sharp_witnesses")
    for m in ROWS:
        local_words, closing_cases, transitions = check_row(m)
        print(f"{m} {local_words} {closing_cases} {transitions} 2")
    print("PASS: polynomial local/transition scan; no path-permutation enumeration")


if __name__ == "__main__":
    main()
