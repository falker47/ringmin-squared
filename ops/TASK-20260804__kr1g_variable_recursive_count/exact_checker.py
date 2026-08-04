"""Small exact checker for the variable-count KR1G order statistics.

The script is standalone and uses only ``Fraction`` arithmetic extended to
``Q(sqrt(2))``.  It checks the deliberately enlarged coordinate-subset
relaxation after KR1G-98.  It does not enumerate histories and does not claim
that an order-statistic minimizing subset, or the residual bound, is attained
by a discrete history.
"""

from dataclasses import dataclass
from fractions import Fraction
from functools import cmp_to_key, total_ordering
from itertools import combinations


@total_ordering
@dataclass(frozen=True)
class Surd2:
    """An exact value ``p + q*sqrt(2)``."""

    p: Fraction
    q: Fraction = Fraction()

    @staticmethod
    def coerce(value: "Surd2 | Fraction | int") -> "Surd2":
        return value if isinstance(value, Surd2) else Surd2(Fraction(value))

    def __add__(self, other: "Surd2 | Fraction | int") -> "Surd2":
        rhs = self.coerce(other)
        return Surd2(self.p + rhs.p, self.q + rhs.q)

    def __radd__(self, other: "Surd2 | Fraction | int") -> "Surd2":
        return self + other

    def __neg__(self) -> "Surd2":
        return Surd2(-self.p, -self.q)

    def __sub__(self, other: "Surd2 | Fraction | int") -> "Surd2":
        return self + (-self.coerce(other))

    def __rsub__(self, other: "Surd2 | Fraction | int") -> "Surd2":
        return self.coerce(other) - self

    def __mul__(self, other: "Surd2 | Fraction | int") -> "Surd2":
        rhs = self.coerce(other)
        return Surd2(
            self.p * rhs.p + 2 * self.q * rhs.q,
            self.p * rhs.q + self.q * rhs.p,
        )

    def __rmul__(self, other: "Surd2 | Fraction | int") -> "Surd2":
        return self * other

    def __truediv__(self, other: "Surd2 | Fraction | int") -> "Surd2":
        rhs = self.coerce(other)
        norm = rhs.p * rhs.p - 2 * rhs.q * rhs.q
        if norm == 0:
            raise ZeroDivisionError
        return self * Surd2(rhs.p / norm, -rhs.q / norm)

    def __rtruediv__(self, other: "Surd2 | Fraction | int") -> "Surd2":
        return self.coerce(other) / self

    def sign(self) -> int:
        """Determine the sign exactly by one rational square comparison."""
        if self.q == 0:
            return (self.p > 0) - (self.p < 0)
        if self.p == 0:
            return (self.q > 0) - (self.q < 0)
        if self.p > 0 and self.q > 0:
            return 1
        if self.p < 0 and self.q < 0:
            return -1
        margin = self.p * self.p - 2 * self.q * self.q
        if self.p > 0:
            return 1 if margin > 0 else -1
        return 1 if margin < 0 else -1

    def __lt__(self, other: "Surd2 | Fraction | int") -> bool:
        return (self - other).sign() < 0


ZERO = Surd2(Fraction())
ONE = Surd2(Fraction(1))


def floor_exact(value: Surd2, bound: int) -> int:
    """Floor a nonnegative surd by exact binary search."""
    if value < 0 or value > bound:
        raise AssertionError("invalid exact-floor bounds")
    lower, upper = 0, bound + 1
    while upper - lower > 1:
        middle = (lower + upper) // 2
        if value < middle:
            upper = middle
        else:
            lower = middle
    return lower


def ceil_exact(value: Surd2, bound: int) -> int:
    """Ceil a nonnegative surd exactly."""
    lower = floor_exact(value, bound)
    return lower if value == Surd2(Fraction(lower)) else lower + 1


@dataclass(frozen=True)
class Coordinate:
    """One finite selected coordinate."""

    label: int
    segment: int
    weight: Surd2
    displacement: Surd2


@dataclass(frozen=True)
class Row:
    """One finite cutoff row and all its selected coordinates."""

    n: int
    r: int
    cutoffs: tuple[int, ...]
    weights: tuple[Surd2, ...]
    coordinates: tuple[Coordinate, ...]

    @property
    def q(self) -> int:
        return self.n - self.r + 1

    @property
    def ell(self) -> int:
        return self.r - self.cutoffs[-1]

    @property
    def denominator(self) -> Surd2:
        reciprocal = sum(
            (4 / (2 - item.weight) for item in self.coordinates),
            ZERO,
        )
        return reciprocal + 2 * (self.q - self.ell)


def build_row(
    n: int,
    r: int,
    cutoffs: tuple[int, ...],
    weights: tuple[Surd2 | Fraction, ...],
) -> Row:
    """Construct the exact ``d_t`` multiset from literal cutoffs."""
    exact_weights = tuple(Surd2.coerce(weight) for weight in weights)
    if len(cutoffs) != len(exact_weights) or not cutoffs:
        raise AssertionError("cutoff/weight mismatch")
    items: list[Coordinate] = []
    upper = r
    for segment, (cutoff, weight) in enumerate(
        zip(cutoffs, exact_weights),
        start=1,
    ):
        if not 1 <= cutoff < upper or not ZERO < weight < ONE:
            raise AssertionError("invalid finite segment")
        factor = weight / (2 - weight)
        for label in range(cutoff, upper):
            displacement = factor * (n + r - 2 * label)
            if displacement <= ZERO:
                raise AssertionError("nonpositive displacement")
            items.append(Coordinate(label, segment, weight, displacement))
        upper = cutoff
    row = Row(n, r, cutoffs, exact_weights, tuple(items))
    if len(items) != row.ell or row.q - row.ell < 1:
        raise AssertionError("invalid row cardinality")
    return row


def compare_coordinates(left: Coordinate, right: Coordinate) -> int:
    """Sort exactly by displacement, stabilizing equal values by label."""
    sign = (left.displacement - right.displacement).sign()
    return sign or (left.label > right.label) - (left.label < right.label)


def ordered(row: Row) -> tuple[Coordinate, ...]:
    """Return increasing displacement order."""
    return tuple(sorted(row.coordinates, key=cmp_to_key(compare_coordinates)))


def smallest_sum(row: Row, count: int) -> Surd2:
    """Sum the ``count`` smallest displacements."""
    return sum((item.displacement for item in ordered(row)[:count]), ZERO)


def audit_subsets(row: Row) -> tuple[int, tuple[int, ...]]:
    """Exhaust the subset minimum and the uniform denominator relaxation."""
    subset_count = 0
    minimizer_counts: list[int] = []
    for size in range(row.ell + 1):
        target = smallest_sum(row, size)
        minimum: Surd2 | None = None
        minimizers = 0
        for indices in combinations(range(row.ell), size):
            subset_count += 1
            chosen = tuple(row.coordinates[index] for index in indices)
            numerator = sum((item.displacement for item in chosen), ZERO)
            if minimum is None or numerator < minimum:
                minimum, minimizers = numerator, 1
            elif numerator == minimum:
                minimizers += 1
            if size == 0:
                continue
            denominator = sum(
                (4 / (2 - item.weight) for item in chosen),
                ZERO,
            ) + 2 * (row.q - size)
            if numerator < target or denominator > row.denominator:
                raise AssertionError("coordinate relaxation failed")
            left = numerator * numerator / denominator
            right = target * target / row.denominator
            if left < right:
                raise AssertionError("uniform finite ratio failed")
        if minimum != target:
            raise AssertionError("subset minimum differs from order statistics")
        minimizer_counts.append(minimizers)
    return subset_count, tuple(minimizer_counts)


def verify_rational_fixtures() -> None:
    """Check a crossover fixture and a genuine cross-segment tie."""
    crossover = build_row(
        11,
        5,
        (3, 2),
        (Fraction(3, 4), Fraction(1, 4)),
    )
    expected = (Fraction(), Fraction(12, 7), Fraction(228, 35), Fraction(438, 35))
    sums = tuple(smallest_sum(crossover, size) for size in range(4))
    if tuple(item.label for item in ordered(crossover)) != (2, 4, 3):
        raise AssertionError("changed crossover order")
    if sums != tuple(Surd2(value) for value in expected):
        raise AssertionError("changed crossover sums")
    if crossover.denominator != Surd2(Fraction(584, 35)):
        raise AssertionError("changed crossover denominator")
    first_bound = sums[1] * sums[1] / crossover.denominator
    if first_bound != Surd2(Fraction(90, 511)):
        raise AssertionError("changed crossover uniform bound")

    tie = build_row(
        11,
        5,
        (4, 2),
        (Fraction(2, 3), Fraction(1, 2)),
    )
    tie_expected = (Fraction(), Fraction(10, 3), Fraction(22, 3), Fraction(34, 3))
    tie_sums = tuple(smallest_sum(tie, size) for size in range(4))
    if tuple(item.label for item in ordered(tie)) != (3, 2, 4):
        raise AssertionError("changed tie order")
    if tie_sums != tuple(Surd2(value) for value in tie_expected):
        raise AssertionError("changed tie sums")

    count_a, minimizers_a = audit_subsets(crossover)
    count_b, minimizers_b = audit_subsets(tie)
    if minimizers_a != (1, 1, 1, 1) or minimizers_b != (1, 1, 2, 1):
        raise AssertionError("changed rational minimizer counts")
    print(
        "finite-order-statistics: fixtures=2 "
        f"subsets={count_a + count_b} crossover_W=(12/7,228/35,438/35) "
        "tie_b2=2 uniform_b1=90/511: PASS"
    )


def verify_rounded_all_middle() -> tuple[Surd2, Surd2]:
    """Audit the actual rounded all-middle row ``k=3,n=200``."""
    a = Surd2(Fraction(13, 23), Fraction(-2, 23))
    total_density = 1 + a
    amplitude = 3 * a - 1
    xs = (Fraction(1058, 1263), Fraction(276, 421), Fraction(184, 421))
    betas = tuple((total_density + amplitude * x) / 4 for x in xs)
    weights = tuple(amplitude * x / beta for x, beta in zip(xs, betas))

    n = 200
    r = floor_exact(a * n, n)
    cutoffs = tuple(ceil_exact(beta * n, n) for beta in betas)
    if not r <= a * n < r + 1:
        raise AssertionError("incorrect exact floor rounding")
    for cutoff, beta in zip(cutoffs, betas):
        if not cutoff - 1 < beta * n <= cutoff:
            raise AssertionError("incorrect exact ceiling rounding")

    row = build_row(n, r, cutoffs, weights)
    labels = tuple(item.label for item in ordered(row))
    expected_labels = (82, 81, 80, 85, 84, 83, 87, 86)
    if (r, cutoffs, row.ell, labels) != (88, (86, 83, 80), 8, expected_labels):
        raise AssertionError("changed rounded all-middle row")

    direct = sum((item.displacement for item in row.coordinates), ZERO)
    formula = ZERO
    upper = row.r
    for cutoff, weight in zip(row.cutoffs, row.weights):
        length = upper - cutoff
        formula += weight / (2 - weight) * length * (row.n + row.r - cutoff - upper + 1)
        upper = cutoff
    if direct != formula:
        raise AssertionError("literal and closed finite T sums disagree")
    subset_count, _ = audit_subsets(row)
    if subset_count != 256:
        raise AssertionError("changed rounded subset count")
    print(
        "rounded-all-middle: k=3 n=200 r=88 cutoffs=(86,83,80) "
        f"ell=8 subsets={subset_count} order={labels}: PASS"
    )
    lower_endpoint = total_density / 4
    return total_density, a - lower_endpoint


def verify_limiting_profile(total_density: Surd2, width: Surd2) -> None:
    """Check exactly the ``sigma^2`` numerator and ``sigma^4`` square."""
    sigmas = (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1))
    cells = 12
    cell_width = width / cells
    lower_endpoint = total_density / 4
    values: list[Surd2] = []
    for index in range(cells):
        offset = (Fraction(index) + Fraction(1, 2)) * cell_width
        value = 4 * (lower_endpoint + offset) - total_density
        if value != 4 * offset:
            raise AssertionError("changed limiting linear profile")
        values.append(value)

    tau_infinity = 2 * width * width
    for sigma in sigmas:
        count = sigma * cells
        if count.denominator != 1:
            raise AssertionError("midpoint grid does not resolve sigma")
        integral = cell_width * sum(values[: count.numerator], ZERO)
        expected = sigma * sigma * tau_infinity
        if integral != expected:
            raise AssertionError("sigma^2 numerator identity failed")
        if integral * integral != sigma**4 * tau_infinity * tau_infinity:
            raise AssertionError("sigma^4 squared-factor identity failed")
    print(
        "limiting-profile: sigma=(1/4,1/2,3/4,1) "
        "numerator=sigma^2*tau_infinity squared_factor=sigma^4: PASS"
    )


def main() -> None:
    """Run the focused exact checks."""
    verify_rational_fixtures()
    total_density, width = verify_rounded_all_middle()
    verify_limiting_profile(total_density, width)
    print(
        "PASS: focused exact order-statistic relaxation; "
        "no discrete residual attainment asserted"
    )


if __name__ == "__main__":
    main()
