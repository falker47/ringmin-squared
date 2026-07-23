"""Exact finite-row audit of the KR1 versus finite-prefix gap decomposition.

The script reconstructs the KR1 core order without importing project or test
helpers.  On each row it uses every integer cutoff in the active all-middle
window.  That growing-cutoff choice is only a Riemann-sum diagnostic for the
already proved all-fixed-prefix supremum; it is not used as a charging theorem
or as a new optimized fixed-prefix model.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, localcontext
from fractions import Fraction


ROWS = (200, 201, 1000, 1001, 20000, 20001)


@dataclass(frozen=True)
class SqrtTwo:
    """An exact element ``rational + radical * sqrt(2)``."""

    rational: Fraction
    radical: Fraction = Fraction()

    def __add__(self, other: SqrtTwo | Fraction | int) -> SqrtTwo:
        value = other if isinstance(other, SqrtTwo) else SqrtTwo(Fraction(other))
        return SqrtTwo(
            self.rational + value.rational,
            self.radical + value.radical,
        )

    __radd__ = __add__

    def __neg__(self) -> SqrtTwo:
        return SqrtTwo(-self.rational, -self.radical)

    def __sub__(self, other: SqrtTwo | Fraction | int) -> SqrtTwo:
        value = other if isinstance(other, SqrtTwo) else SqrtTwo(Fraction(other))
        return self + (-value)

    def __rsub__(self, other: Fraction | int) -> SqrtTwo:
        return SqrtTwo(Fraction(other)) - self

    def __mul__(self, other: SqrtTwo | Fraction | int) -> SqrtTwo:
        value = other if isinstance(other, SqrtTwo) else SqrtTwo(Fraction(other))
        return SqrtTwo(
            self.rational * value.rational + 2 * self.radical * value.radical,
            self.rational * value.radical + self.radical * value.rational,
        )

    __rmul__ = __mul__

    def __truediv__(self, other: Fraction | int) -> SqrtTwo:
        scalar = Fraction(other)
        return SqrtTwo(self.rational / scalar, self.radical / scalar)

    def __pow__(self, exponent: int) -> SqrtTwo:
        if exponent < 0:
            raise ValueError("negative powers are not needed")
        result = SqrtTwo(Fraction(1))
        for _ in range(exponent):
            result *= self
        return result


def check_exact_algebra() -> None:
    """Check the algebraic coefficients and logarithmic cancellation."""
    alpha = SqrtTwo(Fraction(13, 23), Fraction(-2, 23))
    sigma = 1 + alpha

    base_slack = (
        17 * alpha**3 / 6 - 43 * alpha**2 / 10 + 103 * alpha / 50 - Fraction(923, 3000)
    )
    used_slack = (
        970875 * alpha**3 - 1267575 * alpha**2 + 549345 * alpha - 78893
    ) / 192000
    unused = base_slack - used_slack
    expected_unused = SqrtTwo(
        Fraction(-5527598, 146004000),
        Fraction(4614125, 146004000),
    )
    assert unused == expected_unused

    height_polynomial = (
        47875 * alpha**3 - 106875 * alpha**2 + 165825 * alpha - 51393
    ) / 12000
    product_polynomial = (
        3 * (5 * alpha - 3) * (25 * alpha**2 - 150 * alpha - 303) / 64000
    )
    square_polynomial = (
        -(262125 * alpha**3 - 793725 * alpha**2 + 1328895 * alpha - 412567) / 96000
    )

    log_plus_coefficient = -64 * sigma / 25 + 64 * sigma / 25
    log_minus_coefficient = -2 * sigma / 5 - 9 * sigma / 100 + 49 * sigma / 100
    assert log_plus_coefficient == SqrtTwo(Fraction())
    assert log_minus_coefficient == SqrtTwo(Fraction())

    gap = SqrtTwo(Fraction(19353, 1587000), Fraction(-4000, 1587000))
    assert unused + height_polynomial + product_polynomial + square_polynomial == gap


def kr1_order(row: int) -> tuple[int, ...]:
    """Reconstruct the residue-one core order for ``n = 5 * row + 1``."""
    if row < 2:
        raise ValueError("the KR1 row parameter must be at least two")

    n = 5 * row + 1
    terminal_start = 4 * row + 2
    triple_count, has_doubleton = divmod(row, 2)

    middle_paths: list[tuple[int, ...]] = [(terminal_start - 1,)]
    middle_paths.extend(
        (
            terminal_start - 2 * block,
            2 * row + 1 + block,
            terminal_start - 2 * block - 1,
        )
        for block in range(1, triple_count + 1)
    )
    middle_paths.extend(
        (terminal_start - triple_count - block - 1,)
        for block in range(triple_count + 1, row - has_doubleton)
    )
    if has_doubleton:
        middle_paths.append((2 * row + triple_count + 3, 2 * row + triple_count + 2))
    assert len(middle_paths) == row

    order: list[int] = []
    for block, middle_path in enumerate(middle_paths):
        next_block = (block + 1) % row
        order.extend(
            (
                terminal_start + block,
                2 * row - 2 * block,
                *middle_path,
                2 * row + 1 - 2 * next_block,
            )
        )

    result = tuple(order)
    assert len(result) == n - 1
    assert set(result) == set(range(2, n + 1))
    return result


def cycle_score(cycle: tuple[int, ...]) -> int:
    """Return the exact cyclic adjacent-product sum."""
    return sum(
        cycle[index] * cycle[(index + 1) % len(cycle)] for index in range(len(cycle))
    )


def deletion_endpoints(order: tuple[int, ...], stop: int) -> dict[int, tuple[int, int]]:
    """Record the neighbors of each label when deleting upward to ``stop``."""
    previous = {
        value: order[(index - 1) % len(order)] for index, value in enumerate(order)
    }
    following = {
        value: order[(index + 1) % len(order)] for index, value in enumerate(order)
    }
    endpoints: dict[int, tuple[int, int]] = {}

    for value in range(2, stop):
        left = previous[value]
        right = following[value]
        endpoints[value] = (left, right)
        following[left] = right
        previous[right] = left

    return endpoints


def normalized(value: Fraction | int, n: int) -> Decimal:
    """Convert an exact integer or fraction to a high-precision coefficient."""
    exact = value if isinstance(value, Fraction) else Fraction(value)
    return Decimal(exact.numerator) / Decimal(exact.denominator) / Decimal(n**3)


def alpha_floor(n: int) -> int:
    """Return ``floor(n * (13 - 2 * sqrt(2)) / 23)`` by integer comparisons."""

    def below_alpha(candidate: int) -> bool:
        radical_gap = 13 * n - 23 * candidate
        return radical_gap > 0 and radical_gap**2 > 8 * n**2

    low, high = 0, n + 1
    while low + 1 < high:
        middle = (low + high) // 2
        if below_alpha(middle):
            low = middle
        else:
            high = middle

    assert below_alpha(low)
    assert not below_alpha(low + 1)
    return low


def audit_row(row: int) -> dict[str, Fraction | int]:
    """Compute and exactly verify one dense-cutoff decomposition."""
    n = 5 * row + 1
    order = kr1_order(row)
    r = alpha_floor(n)
    total_height = n + r
    s = (total_height + 3) // 4
    maximizing_tail = 2 * row + 1
    assert s < maximizing_tail < r
    assert 2 * r <= n + 2

    endpoints = deletion_endpoints(order, r)
    base_cycle = tuple(value for value in order if value >= r)
    base_edges = {
        frozenset(
            (
                base_cycle[index],
                base_cycle[(index + 1) % len(base_cycle)],
            )
        )
        for index in range(len(base_cycle))
    }

    base_score = cycle_score(base_cycle)
    exact_score = cycle_score(
        tuple(value for value in order if value >= maximizing_tail)
    )
    pairing_floor = sum(value * (total_height - value) for value in range(r, n + 1))
    base_slack = base_score - pairing_floor

    used_edges: set[frozenset[int]] = set()
    charged_slack = Fraction()
    weighted_corrections = Fraction()
    local_floor_loss = Fraction()
    product_relaxation_loss = Fraction()
    residual_bound = Fraction()
    correction_prefix = 0
    maximum_prefix = 0

    for value in range(r - 1, s - 1, -1):
        left, right = endpoints[value]
        edge = frozenset((left, right))
        assert edge in base_edges
        assert edge not in used_edges
        used_edges.add(edge)

        correction = value * (left + right) - left * right
        correction_prefix += correction
        maximum_prefix = max(maximum_prefix, correction_prefix)

        weight = Fraction(4 * value - total_height, value)
        assert 0 <= weight <= 1
        delta = Fraction((left + right - total_height) ** 2, 2)
        floor = (
            weight
            * (4 * total_height * value - total_height**2 - 2 * weight * value**2)
            / (2 * (2 - weight))
        )

        product_loss = weight * Fraction((left - right) ** 2, 4)
        center = Fraction(left + right) - 2 * (
            Fraction(total_height) - weight * value
        ) / (2 - weight)
        square_loss = (2 - weight) * center**2 / 4
        assert delta + weight * correction - floor == product_loss + square_loss

        charged_slack += delta
        weighted_corrections += weight * correction
        local_floor_loss += product_loss + square_loss
        product_relaxation_loss += product_loss
        residual_bound += floor

    assert maximum_prefix == exact_score - base_score
    unused_slack = Fraction(base_slack) - charged_slack
    height_loss = Fraction(maximum_prefix) - weighted_corrections
    square_center_loss = local_floor_loss - product_relaxation_loss
    lower_bound = Fraction(pairing_floor) + residual_bound
    total_gap = Fraction(exact_score) - lower_bound

    assert unused_slack >= 0
    assert height_loss >= 0
    assert product_relaxation_loss >= 0
    assert square_center_loss >= 0
    assert total_gap == unused_slack + height_loss + local_floor_loss

    return {
        "n": n,
        "cutoffs": r - s,
        "recursive": 0,
        "bound": lower_bound,
        "gap": total_gap,
        "unused": unused_slack,
        "height": height_loss,
        "local": local_floor_loss,
        "product": product_relaxation_loss,
        "square": square_center_loss,
    }


def limiting_coefficients() -> dict[str, Decimal]:
    """Evaluate the exact closed forms at the algebraic optimum."""
    with localcontext() as context:
        context.prec = 80
        root_two = Decimal(2).sqrt()
        alpha = (Decimal(13) - 2 * root_two) / Decimal(23)
        one = Decimal(1)

        gap = (Decimal(19353) - Decimal(4000) * root_two) / Decimal(1587000)
        unused = (Decimal(4614125) * root_two - Decimal(5527598)) / Decimal(146004000)
        height_polynomial = (
            Decimal(47875) * alpha**3
            - Decimal(106875) * alpha**2
            + Decimal(165825) * alpha
            - Decimal(51393)
        ) / Decimal(12000)
        height = (
            height_polynomial
            + 2 * (one + alpha) / 5 * (5 * (one + alpha) / 8).ln()
            - 64 * (one + alpha) / 25 * (5 * alpha / 2).ln()
        )
        local = gap - unused - height
        product_polynomial = (
            Decimal(3) * alpha**3 / 512
            - Decimal(99) * alpha**2 / 2560
            - Decimal(639) * alpha / 12800
            + Decimal(2727) / 64000
        )
        product = (
            product_polynomial
            + Decimal(9) * (one + alpha) / 100 * (5 * (one + alpha) / 8).ln()
        )
        square = local - product

        return {
            "gap": +gap,
            "unused": +unused,
            "height": +height,
            "local": +local,
            "product": +product,
            "square": +square,
        }


def main() -> None:
    with localcontext() as context:
        context.prec = 80
        targets = limiting_coefficients()
        print("KR1 / arbitrary-finite-prefix dense-cutoff audit")
        print("classification: bounded exact finite computation")
        print("growing cutoffs: Riemann diagnostic only")
        print(
            "targets:",
            " ".join(f"{name}={value:.15f}" for name, value in targets.items()),
        )

        last: dict[str, Fraction | int] | None = None
        for row in ROWS:
            result = audit_row(row)
            last = result
            n = int(result["n"])
            print(
                f"n={n} cutoffs={result['cutoffs']} recursive={result['recursive']}",
                " ".join(
                    f"{name}={normalized(result[name], n):.15f}"
                    for name in (
                        "gap",
                        "unused",
                        "height",
                        "local",
                        "product",
                        "square",
                    )
                ),
            )

        assert last is not None
        last_n = int(last["n"])
        for name in ("gap", "unused", "height", "local", "product", "square"):
            observed = normalized(last[name], last_n)
            assert abs(observed - targets[name]) < Decimal("2e-5")

        assert 2 * 4614125**2 - 5527598**2 == 12025959381646
        check_exact_algebra()
        print("exact identities and limiting discriminants: PASS")


if __name__ == "__main__":
    main()
