"""Exact boundary diagnostic for the fixed five-prefix rational witness."""

from fractions import Fraction


def floor_fraction(value: Fraction) -> int:
    """Return the floor of an exact rational."""
    return value.numerator // value.denominator


def ceil_fraction(value: Fraction) -> int:
    """Return the ceiling of an exact rational."""
    return -((-value.numerator) // value.denominator)


def prefix_objective(xs: tuple[Fraction, ...]) -> Fraction:
    """Evaluate the normalized finite-prefix objective."""
    previous = Fraction(1)
    total = Fraction(0)
    for current in xs:
        total += (previous - current) * current**2
        previous = current
    return total


DENOMINATOR = 30_143_556_935_103
NUMERATORS = (
    26_881_208_992_898,
    23_392_470_652_668,
    19_595_592_993_288,
    15_335_681_473_008,
    10_223_787_648_672,
)
ALPHA = Fraction(13, 30)
SCALE = 1 + ALPHA
AMPLITUDE = 3 * ALPHA - 1
XS = tuple(Fraction(value, DENOMINATOR) for value in NUMERATORS)
BETAS = tuple((SCALE + AMPLITUDE * value) / 4 for value in XS)
WEIGHTS = tuple(AMPLITUDE * value / beta for value, beta in zip(XS, BETAS, strict=True))
TRANSFORMED = tuple(AMPLITUDE * value for value in XS)
LOCAL_LEADING = tuple(value**2 / 2 for value in TRANSFORMED)
COEFFICIENT = Fraction(
    2_263_404_122_555_368_590_593_580_404_287,
    8_177_706_222_298_165_502_582_585_481_000,
)


def cutoff_row(n: int) -> tuple[int, tuple[int, ...], int]:
    """Return r, the five ceiling cutoffs, and S=n+r."""
    r = floor_fraction(ALPHA * n)
    cutoffs = tuple(ceil_fraction(beta * n) for beta in BETAS)
    return r, cutoffs, n + r


def pairing_floor(n: int, r: int) -> int:
    """Return the exact duplicated-pairing floor P_{r,n}."""
    value = Fraction(
        (n - r + 1) * (r * r + 4 * r * n + r + n * n - n),
        6,
    )
    assert value.denominator == 1
    return value.numerator


def local_floor(n: int, r: int, cutoff: int, weight: Fraction) -> Fraction:
    """Evaluate G_{n,weight}(cutoff) with the fixed rational weight."""
    center = n + r
    return (
        weight
        * (4 * center * cutoff - center**2 - 2 * weight * cutoff**2)
        / (2 * (2 - weight))
    )


def literal_bound(n: int) -> Fraction:
    """Evaluate the literal fixed-weight bound B_{5,n}."""
    r, cutoffs, _ = cutoff_row(n)
    total = Fraction(pairing_floor(n, r))
    previous = r
    for cutoff, weight in zip(cutoffs, WEIGHTS, strict=True):
        total += (previous - cutoff) * local_floor(n, r, cutoff, weight)
        previous = cutoff
    return total


def exact_remainder_terms(
    n: int,
) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    """Return the exact remainder and its n^2, n, and constant coefficients."""
    r, cutoffs, _ = cutoff_row(n)
    eta = ALPHA * n - r
    epsilons = tuple(
        Fraction(cutoff) - beta * n for cutoff, beta in zip(cutoffs, BETAS, strict=True)
    )
    errors = (-eta, *epsilons)
    beta_previous = ALPHA
    quadratic = ALPHA + Fraction(49, 1800) * eta
    linear = -(SCALE * eta**2 / 2 + eta + (1 - ALPHA) / 6)
    constant = (eta**3 - eta) / 6

    for index, (beta, weight, transformed, leading, epsilon) in enumerate(
        zip(
            BETAS,
            WEIGHTS,
            TRANSFORMED,
            LOCAL_LEADING,
            epsilons,
            strict=True,
        )
    ):
        density_gap = beta_previous - beta
        error_gap = errors[index] - errors[index + 1]
        first_order = transformed * (eta + 4 * epsilon)
        constant_order = (
            -transformed
            / (SCALE - transformed)
            * (eta**2 + 4 * eta * epsilon + 2 * weight * epsilon**2)
        )
        direct = local_floor(n, r, cutoffs[index], weight)
        assert direct == leading * n**2 + first_order * n + constant_order
        quadratic += density_gap * first_order + error_gap * leading
        linear += density_gap * constant_order + error_gap * first_order
        constant += error_gap * constant_order
        beta_previous = beta

    remainder = literal_bound(n) - COEFFICIENT * n**3
    assert remainder == quadratic * n**2 + linear * n + constant
    return remainder, quadratic, linear, constant


def check_parameters_and_remainder() -> None:
    """Check the fixed tuple, exact cancellation, and uniform lower bound."""
    assert AMPLITUDE == Fraction(3, 10)
    assert SCALE == Fraction(43, 30)
    assert Fraction(1) > XS[0] > XS[1] > XS[2] > XS[3] > XS[4] > 0
    assert 0 < BETAS[4] < BETAS[3] < BETAS[2] < BETAS[1] < BETAS[0] < ALPHA
    assert 0 < WEIGHTS[4] < WEIGHTS[3] < WEIGHTS[2] < WEIGHTS[1] < WEIGHTS[0] < 1

    x_extended = (Fraction(1), *XS, Fraction(0))
    for index in range(1, 6):
        assert (
            2 * x_extended[index - 1] * x_extended[index]
            - 3 * x_extended[index] ** 2
            + x_extended[index + 1] ** 2
            == 0
        )

    m5 = Fraction(
        722_599_396_919_860_307_414_438_404,
        2_725_902_074_099_388_500_860_861_827,
    )
    assert prefix_objective(XS) == m5
    p_alpha = (1 - ALPHA) * (ALPHA**2 + 4 * ALPHA + 1) / 6
    density_previous = ALPHA
    direct_coefficient = p_alpha
    for beta, leading in zip(BETAS, LOCAL_LEADING, strict=True):
        direct_coefficient += (density_previous - beta) * leading
        density_previous = beta
    assert direct_coefficient == COEFFICIENT

    first_leading = LOCAL_LEADING[0]
    cancellation_coefficient = Fraction(49, 1800) - 3 * first_leading / 4
    assert cancellation_coefficient == Fraction(
        34_730_769_300_472_139_183_348_711,
        90_863_402_469_979_616_695_362_060_900,
    )
    assert cancellation_coefficient > 0

    for n in (*range(233, 248), 300, 1_000):
        remainder, quadratic, _, _ = exact_remainder_terms(n)
        eta = ALPHA * n - floor_fraction(ALPHA * n)
        assert quadratic == ALPHA + cancellation_coefficient * eta
        remainder_polynomial = ALPHA * n**2 - Fraction(25, 2) * n - Fraction(109, 6)
        assert remainder > remainder_polynomial
        if n >= 234:
            assert remainder_polynomial > 0
            assert ceil_fraction(literal_bound(n)) >= literal_bound(n)

    assert ALPHA * 234**2 - Fraction(25, 2) * 234 - Fraction(109, 6) == Fraction(
        623_533, 30
    )
    assert ALPHA * (2 * 234 + 1) - Fraction(25, 2) == Fraction(2_861, 15)


def check_threshold() -> None:
    """Check exact boundary rows and the symbolic-tail margins."""
    expected_rows = {
        233: (100, (100, 98, 95, 93, 90)),
        234: (101, (100, 98, 96, 93, 90)),
        235: (101, (100, 98, 96, 94, 91)),
        236: (102, (101, 99, 97, 94, 91)),
        237: (102, (101, 99, 97, 94, 91)),
        238: (103, (102, 100, 97, 95, 92)),
        239: (103, (102, 100, 98, 95, 92)),
        240: (104, (103, 100, 98, 96, 93)),
        241: (104, (103, 101, 99, 96, 93)),
        242: (104, (103, 101, 99, 96, 93)),
        243: (105, (104, 102, 99, 97, 94)),
        244: (105, (104, 102, 100, 97, 94)),
        245: (106, (105, 103, 100, 98, 95)),
        246: (106, (105, 103, 101, 98, 95)),
    }
    for n, expected in expected_rows.items():
        r, cutoffs, center = cutoff_row(n)
        assert (r, cutoffs) == expected
        if n >= 234:
            points = (r, *cutoffs)
            assert all(left > right for left, right in zip(points, points[1:]))
            assert all(4 * cutoff > center for cutoff in cutoffs)
            assert all(3 * cutoff < center for cutoff in cutoffs)

    r_233, cutoffs_233, _ = cutoff_row(233)
    assert r_233 == cutoffs_233[0]
    r_234, cutoffs_234, center_234 = cutoff_row(234)
    lengths_234 = tuple(
        left - right for left, right in zip((r_234, *cutoffs_234), cutoffs_234)
    )
    assert lengths_234 == (1, 2, 2, 3, 3)
    assert tuple(4 * value - center_234 for value in cutoffs_234) == (
        65,
        57,
        49,
        37,
        25,
    )
    assert tuple(center_234 - 3 * value for value in cutoffs_234) == (
        35,
        41,
        47,
        56,
        65,
    )

    last_top_failure = max(
        n for n in range(1, 247) if cutoff_row(n)[0] <= cutoff_row(n)[1][0]
    )
    last_lower_block_failure = max(n for n in range(1, 247) if cutoff_row(n)[0] < 2)
    last_upper_block_failure = max(n for n in range(1, 247) if cutoff_row(n)[0] > n - 2)
    positive_last_cutoff_failures = tuple(
        n for n in range(1, 247) if cutoff_row(n)[1][-1] < 1
    )
    last_order_failures = tuple(
        max(
            n
            for n in range(1, 247)
            if cutoff_row(n)[1][index] <= cutoff_row(n)[1][index + 1]
        )
        for index in range(4)
    )
    last_upper_middle_failures = tuple(
        max(n for n in range(1, 247) if 3 * cutoff_row(n)[1][index] >= cutoff_row(n)[2])
        for index in range(5)
    )
    lower_middle_failures = tuple(
        n
        for n in range(1, 247)
        if any(4 * cutoff <= cutoff_row(n)[2] for cutoff in cutoff_row(n)[1])
    )
    assert last_top_failure == 233
    assert last_lower_block_failure == 4
    assert last_upper_block_failure == 1
    assert positive_last_cutoff_failures == ()
    assert last_order_failures == (101, 96, 81, 73)
    assert last_upper_middle_failures == (19, 17, 15, 13, 11)
    assert lower_middle_failures == ()

    top_gap = ALPHA - BETAS[0]
    assert top_gap == Fraction(652_469_588_441, 80_382_818_493_608)
    assert 247 * top_gap - 2 == Fraction(
        394_351_357_711,
        80_382_818_493_608,
    )
    internal_gaps = tuple(BETAS[index] - BETAS[index + 1] for index in range(4))
    assert internal_gaps[0] == min(internal_gaps)
    assert 234 * internal_gaps[0] - 1 == Fraction(
        20_722_533_957_289,
        20_095_704_623_402,
    )
    upper_gaps = tuple(SCALE - 3 * beta for beta in BETAS)
    assert upper_gaps[0] == min(upper_gaps)
    assert 26 * upper_gaps[0] - 4 == Fraction(
        60_163_435_263_553,
        602_871_138_702_060,
    )


def main() -> None:
    check_parameters_and_remainder()
    check_threshold()
    print("five-prefix finite floor/ceiling diagnostic: PASS")
    print("minimal uniform threshold=234; failure row=233")
    print("symbolic tail starts at 247; boundary bridge=234..246")
    print(f"coefficient={COEFFICIENT}")
    print(f"I_5,234={ceil_fraction(literal_bound(234))}")
    print("remainder_234 > 623533/30 > 0")


if __name__ == "__main__":
    main()
