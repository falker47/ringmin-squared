"""Independent exact diagnostic for the one-prefix label-aware filter.

This task-local script imports only the Python standard library.  It
exhausts bounded literal split histories, checks both the requested
cardinality-only order-statistic bound and the sharper forced-first-base
type bound, verifies the active-side Bernstein certificate, and uses exact
Sturm arithmetic for the two algebraic isolating intervals.  These bounded
checks corroborate, but do not replace, the written all-history and
all-real proofs.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from math import comb, factorial, prod


Q = Fraction


@dataclass(frozen=True)
class Case:
    name: str
    n: int
    r: int
    s: int
    weight: Fraction
    expected_histories: int
    expected_bound: Fraction


CASES = (
    Case("capacity_inactive", 7, 5, 2, Q(1, 2), 60, Q(607, 6)),
    Case("first_capacity_active", 7, 5, 1, Q(1, 2), 360, Q(263, 3)),
    Case("positive_floor_active", 12, 10, 6, Q(1, 2), 360, Q(1328, 3)),
    Case("two_forced_recursive", 14, 12, 7, Q(1, 2), 2_520, Q(3955, 6)),
)


def edges(cycle: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    return tuple(
        (cycle[index], cycle[(index + 1) % len(cycle)]) for index in range(len(cycle))
    )


def edge_key(left: int, right: int) -> tuple[int, int]:
    return (left, right) if left < right else (right, left)


def score(cycle: tuple[int, ...]) -> int:
    return sum(left * right for left, right in edges(cycle))


def split(cycle: tuple[int, ...], position: int, label: int) -> tuple[int, ...]:
    return cycle[: position + 1] + (label,) + cycle[position + 1 :]


def canonical_cycle(cycle: tuple[int, ...]) -> tuple[int, ...]:
    candidates = []
    for oriented in (cycle, tuple(reversed(cycle))):
        candidates.extend(
            oriented[index:] + oriented[:index] for index in range(len(cycle))
        )
    return min(candidates)


def g_floor(n: int, r: int, weight: Fraction, label: int) -> Fraction:
    center = n + r
    return (
        weight
        * (4 * center * label - center * center - 2 * weight * label * label)
        / (2 * (2 - weight))
    )


def j_floor(n: int, r: int, weight: Fraction, label: int) -> Fraction:
    return weight * ((n + r - 1) * label - n * (r - 1))


def advantage(n: int, r: int, weight: Fraction, label: int) -> Fraction:
    return j_floor(n, r, weight, label) - g_floor(n, r, weight, label)


def direct_requested_advantages(n: int, r: int, s: int, weight: Fraction) -> Fraction:
    length = r - s
    capacity = n - r + 1
    forced = max(0, length - capacity)
    return sum(
        (advantage(n, r, weight, label) for label in range(r - forced, r)),
        Q(),
    )


def direct_type_sharp_advantages(n: int, r: int, s: int, weight: Fraction) -> Fraction:
    length = r - s
    capacity = n - r + 1
    forced = max(0, length - capacity)
    return sum(
        (advantage(n, r, weight, label) for label in range(r - forced - 1, r - 1)),
        Q(),
    )


def closed_g_sum(n: int, r: int, s: int, weight: Fraction) -> Fraction:
    length = r - s
    center = n + r
    first_moment = Q(length * (s + r - 1), 2)
    second_moment = Q((r - 1) * r * (2 * r - 1) - (s - 1) * s * (2 * s - 1), 6)
    return (
        weight
        * (
            4 * center * first_moment
            - length * center * center
            - 2 * weight * second_moment
        )
        / (2 * (2 - weight))
    )


def closed_advantage_sum(
    n: int,
    r: int,
    s: int,
    weight: Fraction,
    *,
    forced_first_base: bool,
) -> Fraction:
    length = r - s
    capacity = n - r + 1
    forced = max(0, length - capacity)
    if forced == 0:
        return Q()

    start = 1 if forced_first_base else 0
    stop = forced if forced_first_base else forced - 1
    count = forced
    sum_h = Q((start + stop) * count, 2)
    sum_h2 = (
        Q(forced * (forced + 1) * (2 * forced + 1), 6)
        if forced_first_base
        else Q(forced * (forced - 1) * (2 * forced - 1), 6)
    )
    distance = n - r
    bracket = (
        count * distance * distance
        + 4 * (count * capacity + sum_h)
        + 2 * weight * (capacity * sum_h + sum_h2)
    )
    return weight * bracket / (2 * (2 - weight))


def pairing_floor(n: int, r: int) -> int:
    center = n + r
    return sum(label * (center - label) for label in range(r, n + 1))


def audit_literal_case(case: Case) -> tuple[int, Counter[int], Fraction, Fraction]:
    n, r, s, weight = case.n, case.r, case.s, case.weight
    length = r - s
    capacity = n - r + 1
    forced = max(0, length - capacity)
    labels = tuple(range(r - 1, s - 1, -1))

    assert capacity == 3
    assert 2 <= r <= n - 2
    assert 1 <= s <= r - 1
    assert len(labels) == length
    assert 0 <= weight <= 1

    base = (r, n, r + 1)
    base_edges = frozenset(edge_key(*edge) for edge in edges(base))
    base_score = score(base)
    floor = pairing_floor(n, r)
    center = n + r
    base_slack = {edge: Q((sum(edge) - center) ** 2, 2) for edge in base_edges}
    assert sum(base_slack.values(), Q()) == base_score - floor

    direct_g = sum((g_floor(n, r, weight, label) for label in labels), Q())
    requested_adv = direct_requested_advantages(n, r, s, weight)
    type_sharp_adv = direct_type_sharp_advantages(n, r, s, weight)
    requested_bound = floor + direct_g + requested_adv
    type_sharp_bound = floor + direct_g + type_sharp_adv

    assert direct_g == closed_g_sum(n, r, s, weight)
    assert requested_adv == closed_advantage_sum(
        n, r, s, weight, forced_first_base=False
    )
    assert type_sharp_adv == closed_advantage_sum(
        n, r, s, weight, forced_first_base=True
    )
    assert requested_bound == case.expected_bound
    assert type_sharp_bound >= requested_bound
    if forced and weight > 0:
        assert type_sharp_bound > requested_bound

    history_count = 0
    recursive_histogram: Counter[int] = Counter()
    final_cycles: set[tuple[int, ...]] = set()
    minimum_requested_margin: Fraction | None = None
    minimum_type_margin: Fraction | None = None

    def walk(
        cycle: tuple[int, ...],
        depth: int,
        used_base_edges: frozenset[tuple[int, int]],
        corrections: tuple[int, ...],
        contributions: tuple[Fraction, ...],
        recursive_labels: tuple[int, ...],
    ) -> None:
        nonlocal history_count
        nonlocal minimum_requested_margin
        nonlocal minimum_type_margin

        if depth == length:
            heights = []
            running = 0
            for correction in corrections:
                running += correction
                heights.append(running)
            selected_objective = base_score + max(0, *heights)
            weighted_objective = Q(base_score) + weight * running
            assert selected_objective >= weighted_objective

            unused_slack = sum(
                (
                    base_slack[edge]
                    for edge in base_edges
                    if edge not in used_base_edges
                ),
                Q(),
            )
            weighted_excess = weighted_objective - floor
            actual_advantage = sum(
                (advantage(n, r, weight, label) for label in recursive_labels),
                Q(),
            )
            assert weighted_excess == sum(contributions, Q()) + unused_slack
            assert len(recursive_labels) >= forced
            assert labels[0] not in recursive_labels
            assert actual_advantage >= requested_adv
            assert actual_advantage >= type_sharp_adv
            assert weighted_excess >= direct_g + actual_advantage
            assert selected_objective >= type_sharp_bound >= requested_bound

            requested_margin = Q(selected_objective) - requested_bound
            type_margin = Q(selected_objective) - type_sharp_bound
            if (
                minimum_requested_margin is None
                or requested_margin < minimum_requested_margin
            ):
                minimum_requested_margin = requested_margin
            if minimum_type_margin is None or type_margin < minimum_type_margin:
                minimum_type_margin = type_margin

            recursive_histogram[len(recursive_labels)] += 1
            final_key = canonical_cycle(cycle)
            assert final_key not in final_cycles
            final_cycles.add(final_key)
            history_count += 1
            return

        label = labels[depth]
        inserted = frozenset(labels[:depth])
        for position, (left, right) in enumerate(edges(cycle)):
            current_edge = edge_key(left, right)
            correction = label * (left + right) - left * right
            next_cycle = split(cycle, position, label)
            assert score(next_cycle) == score(cycle) + correction

            if current_edge in base_edges:
                assert current_edge not in used_base_edges
                next_used = used_base_edges | {current_edge}
                contribution = base_slack[current_edge] + weight * correction
                assert contribution >= g_floor(n, r, weight, label)
                next_recursive = recursive_labels
            else:
                assert inserted.intersection(current_edge)
                next_used = used_base_edges
                contribution = weight * correction
                assert contribution >= j_floor(n, r, weight, label)
                next_recursive = recursive_labels + (label,)

            walk(
                next_cycle,
                depth + 1,
                frozenset(next_used),
                corrections + (correction,),
                contributions + (contribution,),
                next_recursive,
            )

    walk(base, 0, frozenset(), (), (), ())

    expected_histories = prod(capacity + depth for depth in range(length))
    assert expected_histories == factorial(capacity + length - 1) // 2
    assert history_count == len(final_cycles) == case.expected_histories
    assert minimum_requested_margin is not None and minimum_requested_margin >= 0
    assert minimum_type_margin is not None and minimum_type_margin >= 0
    return (
        history_count,
        recursive_histogram,
        minimum_requested_margin,
        minimum_type_margin,
    )


Poly = tuple[Fraction, ...]


def poly_trim(poly: Poly) -> Poly:
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def poly_add(left: Poly, right: Poly) -> Poly:
    size = max(len(left), len(right))
    return poly_trim(
        tuple(
            (left[index] if index < len(left) else Q())
            + (right[index] if index < len(right) else Q())
            for index in range(size)
        )
    )


def poly_scale(poly: Poly, scalar: Fraction | int) -> Poly:
    scalar = Q(scalar)
    return poly_trim(tuple(scalar * coefficient for coefficient in poly))


def poly_mul(left: Poly, right: Poly) -> Poly:
    result = [Q()] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            result[left_index + right_index] += left_value * right_value
    return poly_trim(tuple(result))


def poly_pow(poly: Poly, exponent: int) -> Poly:
    result: Poly = (Q(1),)
    factor = poly
    power = exponent
    while power:
        if power & 1:
            result = poly_mul(result, factor)
        factor = poly_mul(factor, factor)
        power //= 2
    return result


def poly_derivative(poly: Poly) -> Poly:
    if len(poly) == 1:
        return (Q(),)
    return poly_trim(tuple(index * poly[index] for index in range(1, len(poly))))


def poly_divmod(numerator: Poly, denominator: Poly) -> tuple[Poly, Poly]:
    numerator = poly_trim(numerator)
    denominator = poly_trim(denominator)
    assert denominator != (Q(),)
    if len(numerator) < len(denominator):
        return (Q(),), numerator

    remainder = list(numerator)
    quotient = [Q()] * (len(numerator) - len(denominator) + 1)
    while len(remainder) >= len(denominator) and any(remainder):
        shift = len(remainder) - len(denominator)
        factor = remainder[-1] / denominator[-1]
        quotient[shift] = factor
        for index, value in enumerate(denominator):
            remainder[index + shift] -= factor * value
        while len(remainder) > 1 and remainder[-1] == 0:
            remainder.pop()
    return poly_trim(tuple(quotient)), poly_trim(tuple(remainder))


def poly_eval(poly: Poly, value: Fraction) -> Fraction:
    result = Q()
    for coefficient in reversed(poly):
        result = result * value + coefficient
    return result


def sturm_sequence(poly: Poly) -> tuple[Poly, ...]:
    sequence = [poly_trim(poly), poly_derivative(poly)]
    while sequence[-1] != (Q(),):
        _, remainder = poly_divmod(sequence[-2], sequence[-1])
        if remainder == (Q(),):
            break
        sequence.append(poly_scale(remainder, -1))
    return tuple(sequence)


def sign(value: Fraction) -> int:
    return (value > 0) - (value < 0)


def sturm_variations(sequence: tuple[Poly, ...], point: Fraction) -> int:
    signs = [sign(poly_eval(poly, point)) for poly in sequence]
    signs = [entry for entry in signs if entry]
    return sum(left != right for left, right in zip(signs, signs[1:]))


def affine_power_coefficients(poly: Poly, lower: Fraction, upper: Fraction) -> Poly:
    degree = len(poly) - 1
    width = upper - lower
    result = [Q()] * (degree + 1)
    for power, coefficient in enumerate(poly):
        for transformed_power in range(power + 1):
            result[transformed_power] += (
                coefficient
                * comb(power, transformed_power)
                * lower ** (power - transformed_power)
                * width**transformed_power
            )
    return poly_trim(tuple(result))


def bernstein_coefficients(
    poly: Poly, lower: Fraction = Q(), upper: Fraction = Q(1)
) -> tuple[Fraction, ...]:
    power = affine_power_coefficients(poly, lower, upper)
    degree = len(poly) - 1
    return tuple(
        sum(
            (
                power[index] * Q(comb(bernstein_index, index), comb(degree, index))
                for index in range(bernstein_index + 1)
            ),
            Q(),
        )
        for bernstein_index in range(degree + 1)
    )


def active_q(x_value: Fraction, beta: Fraction, weight: Fraction) -> Fraction:
    return (
        12 * ((3 * x_value + 1) * weight - 2 * x_value - 6) * beta * beta
        + 24 * (x_value + 1) * (2 - weight * x_value) * beta
        + 2 * weight * x_value**3
        + 6 * weight * x_value**2
        - 6 * weight * x_value
        - 2 * weight
        + 9 * x_value**3
        - 3 * x_value**2
        + 3 * x_value
        - 9
    )


def active_m(x_value: Fraction, weight: Fraction) -> Fraction:
    x = x_value
    w = weight
    return (
        6 * w**3 * x**4
        + 4 * w**3 * x**3
        + 24 * w**3 * x**2
        + 12 * w**3 * x
        + 2 * w**3
        - 26 * w**2 * x**4
        - 52 * w**2 * x**3
        - 96 * w**2 * x**2
        - 67 * w**2 * x
        - 3 * w**2
        + 26 * w * x**4
        + 128 * w * x**3
        + 132 * w * x**2
        + 120 * w * x
        - 6 * w
        - 4 * x**4
        - 48 * x**3
        - 120 * x**2
        - 36 * x
    )


def integral_g(
    alpha: Fraction, lower: Fraction, upper: Fraction, weight: Fraction
) -> Fraction:
    center = 1 + alpha

    def antiderivative(value: Fraction) -> Fraction:
        return (
            weight
            * (
                2 * center * value * value
                - center * center * value
                - Q(2, 3) * weight * value**3
            )
            / (2 * (2 - weight))
        )

    return antiderivative(upper) - antiderivative(lower)


def integral_j(
    alpha: Fraction, lower: Fraction, upper: Fraction, weight: Fraction
) -> Fraction:
    def antiderivative(value: Fraction) -> Fraction:
        return weight * (Q(1, 2) * (1 + alpha) * value * value - alpha * value)

    return antiderivative(upper) - antiderivative(lower)


def pairing_coefficient(alpha: Fraction) -> Fraction:
    return (1 - alpha) * (alpha * alpha + 4 * alpha + 1) / 6


def audit_active_certificate() -> int:
    f1: Poly = (Q(-3), Q(6), Q(-114), Q(-8), Q(7))
    f2: Poly = (Q(-15), Q(65), Q(-192), Q(60), Q(14))
    f3: Poly = (Q(-7), Q(29), Q(-60), Q(32), Q(2))
    assert bernstein_coefficients(f1) == (
        Q(-3),
        Q(-3, 2),
        Q(-19),
        Q(-115, 2),
        Q(-112),
    )
    assert bernstein_coefficients(f2, Q(), Q(1, 2)) == (
        Q(-15),
        Q(-55, 8),
        Q(-27, 4),
        Q(-51, 4),
        Q(-177, 8),
    )
    assert bernstein_coefficients(f2, Q(1, 2), Q(1)) == (
        Q(-177, 8),
        Q(-63, 2),
        Q(-177, 4),
        Q(-461, 8),
        Q(-68),
    )
    assert bernstein_coefficients(f3, Q(), Q(1, 2)) == (
        Q(-7),
        Q(-27, 8),
        Q(-9, 4),
        Q(-21, 8),
        Q(-27, 8),
    )
    assert bernstein_coefficients(f3, Q(1, 2), Q(1)) == (
        Q(-27, 8),
        Q(-33, 8),
        Q(-21, 4),
        Q(-45, 8),
        Q(-4),
    )

    # Five-by-four exact interpolation grids prove the two polynomial
    # identities because their degrees are at most four in x and three in w.
    for x_index in range(5):
        x = Q(x_index, 4)
        b0 = -4 * x * (x + 3) * (x * x + 9 * x + 3)
        b1 = Q(2, 3) * poly_eval(f1, x)
        b2 = Q(1, 3) * poly_eval(f2, x)
        b3 = poly_eval(f3, x)
        for weight_index in range(4):
            weight = Q(weight_index, 3)
            bernstein_value = (
                b0 * (1 - weight) ** 3
                + 3 * b1 * weight * (1 - weight) ** 2
                + 3 * b2 * weight * weight * (1 - weight)
                + b3 * weight**3
            )
            assert active_m(x, weight) == bernstein_value

            k_value = 2 * x + 6 - weight * (3 * x + 1)
            assert k_value > 0
            beta_vertex = (x + 1) * (2 - weight * x) / k_value
            e_value = x * (x * x + 9 * x + 3)
            left = (2 - weight) * e_value - weight * active_q(x, beta_vertex, weight)
            assert left == -active_m(x, weight) / k_value >= 0

    checked_points = 0
    for x_index in range(9):
        x = Q(x_index, 8)
        alpha = (1 + x) / 2
        for beta_index in range(9):
            beta = x * Q(beta_index, 8)
            split_point = 1 + beta - alpha
            for weight_index in range(9):
                weight = Q(weight_index, 8)
                direct = (
                    pairing_coefficient(alpha)
                    + integral_g(alpha, beta, split_point, weight)
                    + integral_j(alpha, split_point, alpha, weight)
                )
                formula = pairing_coefficient(alpha) + weight * active_q(
                    x, beta, weight
                ) / (48 * (2 - weight))
                assert direct == formula <= Q(13, 48)
                if direct == Q(13, 48):
                    assert (alpha, beta, weight) == (Q(1, 2), Q(), Q())
                checked_points += 1
    return checked_points


@dataclass(frozen=True)
class RatPoly:
    numerator: Poly
    denominator: Poly = (Q(1),)

    @staticmethod
    def coerce(value: int | Fraction | RatPoly) -> RatPoly:
        if isinstance(value, RatPoly):
            return value
        return RatPoly((Q(value),))

    def __add__(self, other: int | Fraction | RatPoly) -> RatPoly:
        other = self.coerce(other)
        return RatPoly(
            poly_add(
                poly_mul(self.numerator, other.denominator),
                poly_mul(other.numerator, self.denominator),
            ),
            poly_mul(self.denominator, other.denominator),
        )

    __radd__ = __add__

    def __neg__(self) -> RatPoly:
        return RatPoly(poly_scale(self.numerator, -1), self.denominator)

    def __sub__(self, other: int | Fraction | RatPoly) -> RatPoly:
        return self + (-self.coerce(other))

    def __rsub__(self, other: int | Fraction | RatPoly) -> RatPoly:
        return self.coerce(other) - self

    def __mul__(self, other: int | Fraction | RatPoly) -> RatPoly:
        other = self.coerce(other)
        return RatPoly(
            poly_mul(self.numerator, other.numerator),
            poly_mul(self.denominator, other.denominator),
        )

    __rmul__ = __mul__

    def __truediv__(self, other: int | Fraction | RatPoly) -> RatPoly:
        other = self.coerce(other)
        assert other.numerator != (Q(),)
        return RatPoly(
            poly_mul(self.numerator, other.denominator),
            poly_mul(self.denominator, other.numerator),
        )

    def __rtruediv__(self, other: int | Fraction | RatPoly) -> RatPoly:
        return self.coerce(other) / self

    def __pow__(self, exponent: int) -> RatPoly:
        return RatPoly(
            poly_pow(self.numerator, exponent),
            poly_pow(self.denominator, exponent),
        )


Q_POLY: Poly = tuple(
    Q(value)
    for value in (
        7,
        -132,
        1082,
        -5028,
        14420,
        -25856,
        27568,
        -14528,
        640,
        2048,
        256,
    )
)

VALUE_POLY: Poly = tuple(
    Q(value)
    for value in (
        9_684_288,
        -75_167_040,
        370_726_096,
        -1_455_471_984,
        3_125_143_800,
        -5_562_634_608,
        2_168_479_593,
        19_509_660_810,
        -8_989_732_026,
        79_843_376_538,
        159_529_146_921,
    )
)

D_POLY: Poly = tuple(Q(value) for value in (-1, 14, -66, 100, 106, -412, 248, 32))
N_POLY: Poly = tuple(Q(value) for value in (0, -3, 34, -146, 294, -284, 120))


def cleared_value_polynomial(value: RatPoly) -> Poly:
    degree = len(VALUE_POLY) - 1
    numerator_powers = [
        poly_pow(value.numerator, exponent) for exponent in range(degree + 1)
    ]
    denominator_powers = [
        poly_pow(value.denominator, exponent) for exponent in range(degree + 1)
    ]
    result: Poly = (Q(),)
    for exponent, coefficient in enumerate(VALUE_POLY):
        term = poly_mul(
            numerator_powers[exponent], denominator_powers[degree - exponent]
        )
        result = poly_add(result, poly_scale(term, coefficient))
    return result


def interval_add(
    left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]
) -> tuple[Fraction, Fraction]:
    return left[0] + right[0], left[1] + right[1]


def interval_neg(value: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return -value[1], -value[0]


def interval_mul(
    left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]
) -> tuple[Fraction, Fraction]:
    products = (
        left[0] * right[0],
        left[0] * right[1],
        left[1] * right[0],
        left[1] * right[1],
    )
    return min(products), max(products)


def interval_reciprocal(
    value: tuple[Fraction, Fraction],
) -> tuple[Fraction, Fraction]:
    assert value[0] > 0 or value[1] < 0
    return Q(1, 1) / value[1], Q(1, 1) / value[0]


def interval_poly_eval(
    poly: Poly, interval: tuple[Fraction, Fraction]
) -> tuple[Fraction, Fraction]:
    result = (Q(), Q())
    for coefficient in reversed(poly):
        result = interval_add(
            interval_mul(result, interval), (coefficient, coefficient)
        )
    return result


def audit_algebraic_optimum() -> tuple[int, int]:
    q_sequence = sturm_sequence(Q_POLY)
    value_sequence = sturm_sequence(VALUE_POLY)
    q_lower = Q(2_680_518, 10_000_000)
    q_upper = Q(2_680_519, 10_000_000)
    q_fine_lower = Q(26_805_182_086_214, 100_000_000_000_000)
    q_fine_upper = Q(26_805_182_086_215, 100_000_000_000_000)
    value_lower = Q(2_768_854, 10_000_000)
    value_upper = Q(2_768_855, 10_000_000)

    assert sturm_variations(q_sequence, Q(1, 4)) == 6
    assert sturm_variations(q_sequence, Q(293, 1000)) == 5
    assert sturm_variations(q_sequence, q_lower) == 6
    assert sturm_variations(q_sequence, q_upper) == 5
    assert sturm_variations(q_sequence, q_fine_lower) == 6
    assert sturm_variations(q_sequence, q_fine_upper) == 5
    assert sturm_variations(value_sequence, value_lower) == 5
    assert sturm_variations(value_sequence, value_upper) == 4

    q_symbol = RatPoly((Q(), Q(1)))
    d_value = RatPoly(D_POLY)
    n_value = RatPoly(N_POLY)
    alpha = -n_value / d_value
    beta = (1 + alpha) * q_symbol
    weight = (4 * q_symbol - 1) / (2 * q_symbol * q_symbol)
    pairing = (1 - alpha) * (alpha * alpha + 4 * alpha + 1) / 6
    residual = (
        (alpha - beta)
        * weight
        / (2 * (2 - weight))
        * (
            (1 + alpha) * (alpha + 2 * beta - 1)
            - Q(2, 3) * weight * (alpha * alpha + alpha * beta + beta * beta)
        )
    )
    optimum_value = pairing + residual
    cleared = cleared_value_polynomial(optimum_value)
    _, remainder = poly_divmod(cleared, Q_POLY)
    assert remainder == (Q(),)

    q_interval = (q_fine_lower, q_fine_upper)
    d_interval = interval_poly_eval(D_POLY, q_interval)
    n_interval = interval_poly_eval(N_POLY, q_interval)
    assert d_interval[0] > 0
    assert n_interval[1] < 0
    alpha_interval = interval_mul(
        (-n_interval[1], -n_interval[0]), interval_reciprocal(d_interval)
    )
    beta_interval = interval_mul(interval_add((Q(1), Q(1)), alpha_interval), q_interval)
    weight_interval = interval_mul(
        interval_add(interval_mul((Q(4), Q(4)), q_interval), (Q(-1), Q(-1))),
        interval_reciprocal(
            interval_mul((Q(2), Q(2)), interval_mul(q_interval, q_interval))
        ),
    )
    assert Q(4_365_889, 10_000_000) < alpha_interval[0]
    assert alpha_interval[1] < Q(4_365_890, 10_000_000)
    assert Q(3_850_802, 10_000_000) < beta_interval[0]
    assert beta_interval[1] < Q(3_850_803, 10_000_000)
    assert Q(5_024_738, 10_000_000) < weight_interval[0]
    assert weight_interval[1] < Q(5_024_739, 10_000_000)

    one = (Q(1), Q(1))
    two = (Q(2), Q(2))
    alpha_squared = interval_mul(alpha_interval, alpha_interval)
    pairing_interval = interval_mul(
        interval_mul(
            interval_add(one, interval_neg(alpha_interval)),
            interval_add(
                interval_add(
                    alpha_squared,
                    interval_mul((Q(4), Q(4)), alpha_interval),
                ),
                one,
            ),
        ),
        (Q(1, 6), Q(1, 6)),
    )
    alpha_beta = interval_mul(alpha_interval, beta_interval)
    beta_squared = interval_mul(beta_interval, beta_interval)
    quadratic_sum = interval_add(interval_add(alpha_squared, alpha_beta), beta_squared)
    bracket_interval = interval_add(
        interval_mul(
            interval_add(one, alpha_interval),
            interval_add(
                interval_add(
                    alpha_interval,
                    interval_mul((Q(2), Q(2)), beta_interval),
                ),
                (Q(-1), Q(-1)),
            ),
        ),
        interval_neg(
            interval_mul(
                interval_mul((Q(2, 3), Q(2, 3)), weight_interval),
                quadratic_sum,
            )
        ),
    )
    residual_interval = interval_mul(
        interval_mul(
            interval_mul(
                interval_add(alpha_interval, interval_neg(beta_interval)),
                weight_interval,
            ),
            interval_reciprocal(
                interval_mul(
                    two,
                    interval_add(two, interval_neg(weight_interval)),
                )
            ),
        ),
        bracket_interval,
    )
    optimum_interval = interval_add(pairing_interval, residual_interval)
    assert value_lower < optimum_interval[0]
    assert optimum_interval[1] < value_upper

    # Exact separators: old one-prefix < 0.2765 < 0.2768 < C* < 0.2769
    # < 0.277 < C_AF.  The two radical comparisons use integer squares.
    assert 6_931**2 - 3 * 4_000**2 == 38_761 > 0
    assert Q(553, 2000) < Q(173, 625) < value_lower
    assert value_upper < Q(2769, 10_000) < Q(277, 1000)
    assert 2 * 4_000**2 - 5_599**2 == 651_199 > 0

    witness_alpha = Q(7, 16)
    witness_beta = Q(3, 8)
    witness_weight = Q(1, 2)
    witness = pairing_coefficient(witness_alpha) + integral_g(
        witness_alpha, witness_beta, witness_alpha, witness_weight
    )
    assert witness == Q(20_411, 73_728) > Q(173, 625)

    return len(q_sequence), len(value_sequence)


def audit() -> None:
    if not __debug__:
        raise RuntimeError("exact diagnostic requires assertions; do not use python -O")

    print("label-aware selected-prefix histories")
    history_total = 0
    for case in CASES:
        histories, histogram, requested_margin, type_margin = audit_literal_case(case)
        history_total += histories
        print(
            f"{case.name}: histories={histories}; "
            f"recursive={dict(sorted(histogram.items()))}; "
            f"requested_margin={requested_margin}; type_margin={type_margin}"
        )

    active_points = audit_active_certificate()
    q_chain_length, value_chain_length = audit_algebraic_optimum()
    print(f"selected_prefix_histories_total={history_total}")
    print(f"active_exact_grid_points={active_points}; max=13/48")
    print(
        f"sturm_chain_lengths: optimizer={q_chain_length}; value={value_chain_length}"
    )
    print("exact comparison: C_1 < C_LA < C_AF")
    print("one-prefix label-aware capacity diagnostic: PASS")


if __name__ == "__main__":
    audit()
