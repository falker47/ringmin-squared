"""Independent exact diagnostic for the finite three-prefix theorem.

This script deliberately imports no project, production, or test helper.  It
reconstructs the CR28cn optimizer in ``Q(sqrt(377823))``, evaluates its integer
floor/ceiling cutoffs exactly, and checks the finite clipped-weight lower bound.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt


RADICAND = 377_823
FINITE_SCAN_END = 170
MINIMUM_UNIFORM_THRESHOLD = 159
SYMBOLIC_TAIL_START = 171
FINITE_CHECK_END = 1_000


@dataclass(frozen=True)
class Surd:
    """An exact element ``rational + radical * sqrt(RADICAND)``."""

    rational: Fraction = Fraction(0)
    radical: Fraction = Fraction(0)

    def __post_init__(self) -> None:
        object.__setattr__(self, "rational", Fraction(self.rational))
        object.__setattr__(self, "radical", Fraction(self.radical))

    @staticmethod
    def coerce(value: int | Fraction | Surd) -> Surd:
        if isinstance(value, Surd):
            return value
        return Surd(Fraction(value))

    def __add__(self, other: int | Fraction | Surd) -> Surd:
        other = self.coerce(other)
        return Surd(
            self.rational + other.rational,
            self.radical + other.radical,
        )

    __radd__ = __add__

    def __neg__(self) -> Surd:
        return Surd(-self.rational, -self.radical)

    def __sub__(self, other: int | Fraction | Surd) -> Surd:
        return self + (-self.coerce(other))

    def __rsub__(self, other: int | Fraction | Surd) -> Surd:
        return self.coerce(other) - self

    def __mul__(self, other: int | Fraction | Surd) -> Surd:
        other = self.coerce(other)
        return Surd(
            self.rational * other.rational + RADICAND * self.radical * other.radical,
            self.rational * other.radical + self.radical * other.rational,
        )

    __rmul__ = __mul__

    def __truediv__(self, other: int | Fraction | Surd) -> Surd:
        other = self.coerce(other)
        norm = other.rational**2 - RADICAND * other.radical**2
        assert norm != 0
        return self * Surd(other.rational / norm, -other.radical / norm)

    def __rtruediv__(self, other: int | Fraction | Surd) -> Surd:
        return self.coerce(other) / self


ZERO = Surd()


def sign(value: Surd) -> int:
    """Return the exact sign of a quadratic surd."""

    rational = value.rational
    radical = value.radical
    if radical == 0:
        return (rational > 0) - (rational < 0)
    if rational == 0:
        return (radical > 0) - (radical < 0)
    if rational > 0 and radical > 0:
        return 1
    if rational < 0 and radical < 0:
        return -1

    rational_square = rational**2
    radical_square = RADICAND * radical**2
    if rational_square == radical_square:
        return 0
    if rational > 0:
        return 1 if rational_square > radical_square else -1
    return 1 if radical_square > rational_square else -1


def floor_fraction(value: Fraction) -> int:
    return value.numerator // value.denominator


def ceil_fraction(value: Fraction) -> int:
    return -floor_fraction(-value)


def floor_surd(value: Surd) -> int:
    """Evaluate a floor by an integer bracket and exact sign bisection."""

    if value.radical == 0:
        return floor_fraction(value.rational)

    radical_floor = isqrt(RADICAND)
    assert radical_floor**2 < RADICAND < (radical_floor + 1) ** 2
    if value.radical > 0:
        lower = value.rational + radical_floor * value.radical
        upper = value.rational + (radical_floor + 1) * value.radical
    else:
        lower = value.rational + (radical_floor + 1) * value.radical
        upper = value.rational + radical_floor * value.radical

    low = floor_fraction(lower)
    high = floor_fraction(upper) + 1
    assert sign(value - low) >= 0
    assert sign(value - high) < 0
    while high - low > 1:
        midpoint = (low + high) // 2
        if sign(value - midpoint) >= 0:
            low = midpoint
        else:
            high = midpoint
    return low


def ceil_surd(value: Surd) -> int:
    return -floor_surd(-value)


def surd_text(value: Surd) -> str:
    separator = "+" if value.radical >= 0 else "-"
    return f"{value.rational} {separator} {abs(value.radical)}*sqrt({RADICAND})"


ALPHA = Surd(Fraction(685_623, 993_423), Fraction(-421, 993_423))
A = 3 * ALPHA - 1
NORMALIZED_COORDINATES = (
    Fraction(1_058, 1_263),
    Fraction(276, 421),
    Fraction(184, 421),
)
BETAS = tuple((1 + ALPHA + coordinate * A) / 4 for coordinate in NORMALIZED_COORDINATES)
ASYMPTOTIC_WEIGHTS = tuple(
    coordinate * A / beta
    for coordinate, beta in zip(
        NORMALIZED_COORDINATES,
        BETAS,
        strict=True,
    )
)
LIMITING_FLOORS = tuple(
    coordinate**2 * A * A / 2 for coordinate in NORMALIZED_COORDINATES
)
PAIRING_COEFFICIENT = (1 - ALPHA) * (ALPHA * ALPHA + 4 * ALPHA + 1) / 6
EXACT_COEFFICIENT = Surd(
    Fraction(753_972_193_324, 2_960_667_770_787),
    Fraction(106_042_322, 2_960_667_770_787),
)
SEGMENT_GAPS = (
    ALPHA - BETAS[0],
    BETAS[0] - BETAS[1],
    BETAS[1] - BETAS[2],
)
ROUNDING_LOSSES = (2, 1, 1)
QUADRATIC_LOSS = 2 * LIMITING_FLOORS[0]
POSITIVE_QUADRATIC = ALPHA - QUADRATIC_LOSS
LINEAR_LOSS = (5 + ALPHA) / 3
PAIRING_ETA_COEFFICIENT = (ALPHA * ALPHA + 2 * ALPHA - 1) / 2


@dataclass(frozen=True)
class CutoffRow:
    n: int
    r: int
    cutoffs: tuple[int, int, int]

    @property
    def center(self) -> int:
        return self.n + self.r

    @property
    def lengths(self) -> tuple[int, int, int]:
        high, middle, low = self.cutoffs
        return (self.r - high, high - middle, middle - low)

    @property
    def lower_clip_gaps(self) -> tuple[int, int, int]:
        return tuple(4 * cutoff - self.center for cutoff in self.cutoffs)

    @property
    def upper_clip_gaps(self) -> tuple[int, int, int]:
        return tuple(self.center - 3 * cutoff for cutoff in self.cutoffs)

    @property
    def admissible(self) -> bool:
        high, middle, low = self.cutoffs
        return 2 <= self.r <= self.n - 2 and 1 <= low < middle < high <= self.r - 1

    @property
    def clipped_middle(self) -> bool:
        return all(gap > 0 for gap in self.lower_clip_gaps) and all(
            gap > 0 for gap in self.upper_clip_gaps
        )


def cutoff_row(n: int) -> CutoffRow:
    r = floor_surd(n * ALPHA)
    cutoffs = tuple(ceil_surd(n * beta) for beta in BETAS)
    return CutoffRow(n, r, cutoffs)


def certify_rounding(row: CutoffRow) -> None:
    alpha_n = row.n * ALPHA
    assert sign(alpha_n - row.r) > 0
    assert sign(row.r + 1 - alpha_n) > 0
    for cutoff, beta in zip(row.cutoffs, BETAS, strict=True):
        beta_n = row.n * beta
        assert sign(beta_n - (cutoff - 1)) > 0
        assert sign(cutoff - beta_n) > 0


def pairing_floor_closed(n: int, r: int) -> int:
    center = n + r
    count = n - r + 1
    label_sum = (r + n) * count // 2
    square_sum = (n * (n + 1) * (2 * n + 1) - (r - 1) * r * (2 * r - 1)) // 6
    return center * label_sum - square_sum


def pairing_floor_direct(n: int, r: int) -> int:
    center = n + r
    return sum(label * (center - label) for label in range(r, n + 1))


def generic_local_floor(
    center: int,
    cutoff: int,
    weight: Fraction,
) -> Fraction:
    return (
        weight
        * (4 * center * cutoff - center**2 - 2 * weight * cutoff**2)
        / (2 * (2 - weight))
    )


def recursive_floor(
    n: int,
    r: int,
    cutoff: int,
    weight: Fraction,
) -> Fraction:
    center = n + r
    return weight * ((center - 1) * cutoff - n * (r - 1))


def pairing_expansion(row: CutoffRow) -> Surd:
    eta = row.n * ALPHA - row.r
    quadratic = ALPHA + PAIRING_ETA_COEFFICIENT * eta
    linear = (1 + ALPHA) * eta * eta / 2 + eta + (1 - ALPHA) / 6
    constant = (eta * eta * eta - eta) / 6
    return (
        PAIRING_COEFFICIENT * row.n**3
        + quadratic * row.n**2
        - linear * row.n
        + constant
    )


def polynomial_lower_bound(n: int) -> Surd:
    return (
        EXACT_COEFFICIENT * n**3
        + POSITIVE_QUADRATIC * n**2
        - LINEAR_LOSS * n
        - Fraction(1, 15)
    )


def check_optimizer() -> None:
    isolation_scale = 10**12
    isolation_lower = 614_673_083_842_134
    isolation_upper = isolation_lower + 1
    assert RADICAND * isolation_scale**2 - isolation_lower**2 == 906_132_566_326_044
    assert isolation_upper**2 - RADICAND * isolation_scale**2 == 323_213_601_358_225

    assert 993_423 * ALPHA * ALPHA - 1_371_246 * ALPHA + 405_782 == ZERO
    assert sign(ALPHA - Fraction(1, 3)) > 0
    assert sign(Fraction(1, 2) - ALPHA) > 0
    assert sign(A) > 0

    expected_betas = (
        Surd(Fraction(1_284_941, 1_986_846), Fraction(-493, 1_324_564)),
        Surd(Fraction(396_037, 662_282), Fraction(-1_249, 3_973_692)),
        Surd(Fraction(357_305, 662_282), Fraction(-973, 3_973_692)),
    )
    expected_weights = (
        Surd(Fraction(20_512_504, 17_448_241), Fraction(-16_928, 17_448_241)),
        Surd(Fraction(5_097_168, 5_090_507), Fraction(-4_416, 5_090_507)),
        Surd(Fraction(3_194_976, 4_266_371), Fraction(-2_944, 4_266_371)),
    )
    assert BETAS == expected_betas
    assert ASYMPTOTIC_WEIGHTS == expected_weights
    high_floor, middle_floor, low_floor = LIMITING_FLOORS
    for positive in (
        low_floor,
        middle_floor - low_floor,
        high_floor - middle_floor,
    ):
        assert sign(positive) > 0

    high, middle, low = BETAS
    weight_high, weight_middle, weight_low = ASYMPTOTIC_WEIGHTS
    for positive in (
        low,
        middle - low,
        high - middle,
        ALPHA - high,
        weight_low,
        weight_middle - weight_low,
        weight_high - weight_middle,
        1 - weight_high,
    ):
        assert sign(positive) > 0

    center = 1 + ALPHA
    for coordinate, beta, weight, limiting_floor in zip(
        NORMALIZED_COORDINATES,
        BETAS,
        ASYMPTOTIC_WEIGHTS,
        LIMITING_FLOORS,
        strict=True,
    ):
        raw_value = coordinate * A
        assert sign(4 * beta - center) > 0
        assert sign(center - 3 * beta) > 0
        assert weight * beta == raw_value
        assert weight == 4 - center / beta
        assert limiting_floor == raw_value * raw_value / 2

    reconstructed = PAIRING_COEFFICIENT
    for gap, limiting_floor in zip(
        SEGMENT_GAPS,
        LIMITING_FLOORS,
        strict=True,
    ):
        reconstructed += gap * limiting_floor
    assert reconstructed == EXACT_COEFFICIENT
    assert (
        79_938_029_811_249 * EXACT_COEFFICIENT * EXACT_COEFFICIENT
        - 40_714_498_439_496 * EXACT_COEFFICIENT
        + 5_145_490_327_924
        == ZERO
    )
    assert sign(EXACT_COEFFICIENT - Fraction(276_678_647_461, 10**12)) > 0
    assert sign(Fraction(276_678_647_462, 10**12) - EXACT_COEFFICIENT) > 0

    assert QUADRATIC_LOSS == 2 * LIMITING_FLOORS[0]
    assert QUADRATIC_LOSS == Fraction(1_119_364, 1_595_169) * A * A
    assert POSITIVE_QUADRATIC == Surd(
        Fraction(-535_396_585_939, 986_889_256_929),
        Fraction(1_466_777_893, 986_889_256_929),
    )
    assert (
        RADICAND * 1_466_777_893**2 - 864_359_671_582**2
        == 65_744_886_159_838_800_396_803
    )
    assert sign(PAIRING_ETA_COEFFICIENT) > 0
    assert sign(POSITIVE_QUADRATIC - Fraction(1, 3)) > 0
    assert sign(Fraction(11, 6) - LINEAR_LOSS) > 0
    assert 25 < 27  # Certifies 1 / (9 * sqrt(3)) < 1 / 15 after squaring.


def check_symbolic_tail() -> tuple[int, int, int, int]:
    segment_thresholds = tuple(
        ceil_surd(Fraction(loss) / gap)
        for loss, gap in zip(
            ROUNDING_LOSSES,
            SEGMENT_GAPS,
            strict=True,
        )
    )
    upper_clip_gap = 1 + ALPHA - 3 * BETAS[0]
    upper_clip_threshold = ceil_surd(4 / upper_clip_gap)
    assert segment_thresholds == (171, 77, 64)
    assert upper_clip_threshold == 23
    assert max(*segment_thresholds, upper_clip_threshold) == (SYMBOLIC_TAIL_START)

    for gap, loss, threshold in zip(
        SEGMENT_GAPS,
        ROUNDING_LOSSES,
        segment_thresholds,
        strict=True,
    ):
        assert sign((threshold - 1) * gap - loss) < 0
        assert sign(threshold * gap - loss) > 0

    assert sign(4 * BETAS[2] - (1 + ALPHA)) > 0
    assert sign((upper_clip_threshold - 1) * upper_clip_gap - 4) < 0
    assert sign(upper_clip_threshold * upper_clip_gap - 4) > 0
    assert ceil_surd(2 / ALPHA) == 5
    assert ceil_surd(1 / (1 - ALPHA)) == 2

    tail_row = cutoff_row(SYMBOLIC_TAIL_START)
    certify_rounding(tail_row)
    assert tail_row.admissible
    assert tail_row.clipped_middle
    return (*segment_thresholds, upper_clip_threshold)


def check_finite_row(row: CutoffRow) -> None:
    assert row.admissible
    assert row.clipped_middle
    certify_rounding(row)

    high, middle, low = row.cutoffs
    assert 0 < low < middle < high < row.r
    weights = tuple(Fraction(4 * cutoff - row.center, cutoff) for cutoff in row.cutoffs)
    weight_high, weight_middle, weight_low = weights
    assert Fraction(0) < weight_low < weight_middle < weight_high < Fraction(1)

    local_floors = tuple(Fraction(gap**2, 2) for gap in row.lower_clip_gaps)
    for cutoff, weight, local_floor in zip(
        row.cutoffs,
        weights,
        local_floors,
        strict=True,
    ):
        assert generic_local_floor(row.center, cutoff, weight) == local_floor
        recursive = recursive_floor(row.n, row.r, cutoff, weight)
        difference = recursive - local_floor
        identity = (
            weight
            * (
                (row.n - row.r) ** 2
                + 4 * (row.n - cutoff)
                + 2 * weight * (row.r - 1 - cutoff) * (row.n - cutoff)
            )
            / (2 * (2 - weight))
        )
        assert difference == identity
        assert difference > 0

    eta = row.n * ALPHA - row.r
    assert sign(eta) > 0
    assert sign(1 - eta) > 0
    epsilons = tuple(
        cutoff - row.n * beta for cutoff, beta in zip(row.cutoffs, BETAS, strict=True)
    )
    for epsilon in epsilons:
        assert sign(epsilon) > 0
        assert sign(1 - epsilon) > 0

    telescoping_error = (
        -LIMITING_FLOORS[0] * eta
        + (LIMITING_FLOORS[1] - LIMITING_FLOORS[0]) * epsilons[0]
        + (LIMITING_FLOORS[2] - LIMITING_FLOORS[1]) * epsilons[1]
        - LIMITING_FLOORS[2] * epsilons[2]
    )
    assert sign(telescoping_error + 2 * LIMITING_FLOORS[0]) > 0

    for index, (cutoff, beta, limiting_floor, local_floor) in enumerate(
        zip(
            row.cutoffs,
            BETAS,
            LIMITING_FLOORS,
            local_floors,
            strict=True,
        )
    ):
        raw_gap = 4 * cutoff - row.center
        limiting_gap = (4 * beta - (1 + ALPHA)) * row.n
        assert sign(raw_gap - limiting_gap) > 0
        assert sign(Surd(local_floor) - limiting_floor * row.n**2) > 0

        rounded_length_floor = SEGMENT_GAPS[index] * row.n - ROUNDING_LOSSES[index]
        assert sign(row.lengths[index] - rounded_length_floor) > 0
        coarse_term = rounded_length_floor * limiting_floor * row.n**2
        assert sign(Surd(row.lengths[index] * local_floor) - coarse_term) > 0

    pairing_closed = pairing_floor_closed(row.n, row.r)
    pairing_direct = pairing_floor_direct(row.n, row.r)
    assert pairing_closed == pairing_direct
    assert Surd(pairing_closed) == pairing_expansion(row)

    pairing_lower = (
        PAIRING_COEFFICIENT * row.n**3
        + ALPHA * row.n**2
        - LINEAR_LOSS * row.n
        - Fraction(1, 15)
    )
    assert sign(Surd(pairing_closed) - pairing_lower) > 0

    literal_bound = Fraction(pairing_closed) + sum(
        length * local_floor
        for length, local_floor in zip(
            row.lengths,
            local_floors,
            strict=True,
        )
    )
    integer_bound = ceil_fraction(literal_bound)
    polynomial = polynomial_lower_bound(row.n)
    leading = EXACT_COEFFICIENT * row.n**3
    coarse_positive_remainder = (
        Fraction(row.n**2, 3) - Fraction(11 * row.n, 6) - Fraction(1, 15)
    )
    assert sign(Surd(literal_bound) - polynomial) > 0
    assert Fraction(integer_bound) >= literal_bound
    assert Fraction(integer_bound) < literal_bound + 1
    assert sign(Surd(integer_bound) - polynomial) > 0
    assert sign(polynomial - leading - coarse_positive_remainder) > 0
    assert coarse_positive_remainder > 0


def row_text(row: CutoffRow) -> str:
    return (
        f"n={row.n}: r={row.r}, s={row.cutoffs}, lengths={row.lengths}, "
        f"4s-S={row.lower_clip_gaps}, S-3s={row.upper_clip_gaps}, "
        f"admissible={row.admissible}, clipped={row.clipped_middle}"
    )


def main() -> None:
    check_optimizer()

    scan_rows = tuple(cutoff_row(n) for n in range(1, FINITE_SCAN_END + 1))
    for row in scan_rows:
        certify_rounding(row)
    admissibility_failures = tuple(row.n for row in scan_rows if not row.admissible)
    clipping_failures = tuple(row.n for row in scan_rows if not row.clipped_middle)
    proof_domain_failures = tuple(
        row.n for row in scan_rows if not (row.admissible and row.clipped_middle)
    )
    assert admissibility_failures[-1] == 158
    assert clipping_failures[-1] == 17
    assert proof_domain_failures[-1] == 158
    assert all(
        row.admissible and row.clipped_middle
        for row in scan_rows[MINIMUM_UNIFORM_THRESHOLD - 1 :]
    )

    expected_bridge = {
        158: (67, (67, 64, 62), (0, 3, 2)),
        159: (68, (67, 65, 62), (1, 2, 3)),
        160: (68, (67, 65, 63), (1, 2, 2)),
        161: (69, (68, 66, 63), (1, 2, 3)),
        162: (69, (68, 66, 64), (1, 2, 2)),
        163: (70, (69, 66, 64), (1, 3, 2)),
        164: (70, (69, 67, 64), (1, 2, 3)),
        165: (70, (69, 67, 65), (1, 2, 2)),
        166: (71, (70, 68, 65), (1, 2, 3)),
        167: (71, (70, 68, 65), (1, 2, 3)),
        168: (72, (71, 69, 66), (1, 2, 3)),
        169: (72, (71, 69, 66), (1, 2, 3)),
        170: (73, (72, 69, 67), (1, 3, 2)),
        171: (73, (72, 70, 67), (1, 2, 3)),
    }
    bridge_rows = tuple(cutoff_row(n) for n in expected_bridge)
    for row in bridge_rows:
        expected_r, expected_cutoffs, expected_lengths = expected_bridge[row.n]
        assert (row.r, row.cutoffs, row.lengths) == (
            expected_r,
            expected_cutoffs,
            expected_lengths,
        )
    boundary_rows = tuple(cutoff_row(n) for n in (158, 159, 170, 171))
    assert not boundary_rows[0].admissible
    assert boundary_rows[0].clipped_middle
    assert all(row.admissible and row.clipped_middle for row in boundary_rows[1:])

    half_integer_row = cutoff_row(162)
    half_integer_floors = tuple(
        Fraction(gap**2, 2) for gap in half_integer_row.lower_clip_gaps
    )
    half_integer_literal = Fraction(
        pairing_floor_closed(half_integer_row.n, half_integer_row.r)
    ) + sum(
        length * local_floor
        for length, local_floor in zip(
            half_integer_row.lengths,
            half_integer_floors,
            strict=True,
        )
    )
    assert half_integer_literal == Fraction(2_374_661, 2)
    assert ceil_fraction(half_integer_literal) == 1_187_331

    tail_thresholds = check_symbolic_tail()
    for n in range(MINIMUM_UNIFORM_THRESHOLD, FINITE_CHECK_END + 1):
        check_finite_row(cutoff_row(n))

    print("exact optimizer and coefficient checks: passed")
    print(f"polynomial kappa={surd_text(POSITIVE_QUADRATIC)}")
    print(f"polynomial ell={surd_text(LINEAR_LOSS)}")
    print(
        "scan n=1..170: "
        f"admissibility_failures={len(admissibility_failures)}, "
        f"last={admissibility_failures[-1]}; "
        f"clipping_failures={len(clipping_failures)}, "
        f"last={clipping_failures[-1]}"
    )
    print("boundary rows")
    for row in boundary_rows:
        print(row_text(row))
    print(
        "symbolic tail thresholds: "
        f"segments={tail_thresholds[:3]}, "
        f"upper_clip={tail_thresholds[3]}, "
        f"tail_start={SYMBOLIC_TAIL_START}"
    )
    print(
        "finite clipped-weight theorem checks: "
        f"n={MINIMUM_UNIFORM_THRESHOLD}..{FINITE_CHECK_END}, "
        "integer closure >= literal >= polynomial > C_3,* n^3"
    )
    print("all exact Q(sqrt(377823)) diagnostics passed")


if __name__ == "__main__":
    main()
