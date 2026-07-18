"""Exact corroboration for the global finite-prefix clipped envelope."""

from fractions import Fraction


Q = Fraction
ZERO = Q(0)
ONE = Q(1)


def sign(value: Fraction) -> int:
    return (value > 0) - (value < 0)


def surd_sign(a: Fraction, b: Fraction, radicand: int) -> int:
    """Return the exact sign of a + b*sqrt(radicand)."""
    if b < 0:
        return -surd_sign(-a, -b, radicand)
    if b == 0:
        return sign(a)
    if a >= 0:
        return 1
    return sign(b * b * radicand - a * a)


def p(alpha: Fraction) -> Fraction:
    return (1 - alpha) * (alpha * alpha + 4 * alpha + 1) / 6


def g(alpha: Fraction, beta: Fraction, weight: Fraction) -> Fraction:
    s = 1 + alpha
    numerator = weight * (4 * s * beta - s * s - 2 * weight * beta * beta)
    return numerator / (2 * (2 - weight))


def clipped_weight(alpha: Fraction, beta: Fraction) -> Fraction:
    s = 1 + alpha
    if beta <= s / 4:
        return ZERO
    if beta >= s / 3:
        return ONE
    return 4 - s / beta


def clipped_floor(alpha: Fraction, beta: Fraction) -> Fraction:
    s = 1 + alpha
    if beta <= s / 4:
        return ZERO
    if beta <= s / 3:
        return (4 * beta - s) ** 2 / 2
    return (4 * s * beta - s * s - 2 * beta * beta) / 2


def phi(x: Fraction) -> Fraction:
    if x <= Q(1, 4):
        return ZERO
    if x <= Q(1, 3):
        return (4 * x - 1) ** 2 / 2
    return -x * x + 2 * x - Q(1, 2)


def integral_phi(t: Fraction) -> Fraction:
    if t <= Q(1, 4):
        return ZERO
    if t <= Q(1, 3):
        return (4 * t - 1) ** 3 / 24
    return -(t**3) / 3 + t * t - t / 2 + Q(5, 72)


def limiting_envelope(alpha: Fraction) -> Fraction:
    tau = alpha / (1 + alpha)
    return p(alpha) + (1 + alpha) ** 3 * integral_phi(tau)


def expected_limiting_envelope(alpha: Fraction) -> Fraction:
    if alpha <= Q(1, 3):
        return p(alpha)
    if alpha <= Q(1, 2):
        numerator = 23 * alpha**3 - 39 * alpha**2 + 21 * alpha + 3
        return numerator / 24
    numerator = 5 * alpha**3 - 21 * alpha**2 + 15 * alpha + 17
    return numerator / 72


def normalized_value(point: tuple[Fraction, ...]) -> Fraction:
    previous = ONE
    total = ZERO
    for current in point:
        total += (previous - current) * current * current
        previous = current
    return total


def middle_envelope(alpha: Fraction, m_value: Fraction) -> Fraction:
    return p(alpha) + m_value * (3 * alpha - 1) ** 3 / 8


def critical_polynomial(alpha: Fraction, m_value: Fraction) -> Fraction:
    return (
        (81 * m_value - 4) * alpha * alpha
        - (54 * m_value + 8) * alpha
        + 9 * m_value
        + 4
    )


def critical_bracket(m_value: Fraction, steps: int = 96) -> tuple[Fraction, Fraction]:
    lower = Q(1, 3)
    upper = Q(1, 2)
    assert critical_polynomial(lower, m_value) > 0
    assert critical_polynomial(upper, m_value) < 0
    for _ in range(steps):
        middle = (lower + upper) / 2
        if critical_polynomial(middle, m_value) > 0:
            lower = middle
        else:
            upper = middle
    return lower, upper


def check_clipping() -> None:
    alphas = (Q(1, 3), Q(2, 5), Q(1, 2), Q(3, 4), ONE)
    for alpha in alphas:
        betas = tuple(alpha * index / 12 for index in range(13))
        weights = tuple(clipped_weight(alpha, beta) for beta in betas)
        assert weights == tuple(sorted(weights))
        for beta, weight in zip(betas, weights, strict=True):
            assert g(alpha, beta, weight) == clipped_floor(alpha, beta)


def check_integral_envelope() -> None:
    for index in range(97):
        alpha = Q(index, 96)
        actual = limiting_envelope(alpha)
        assert actual == expected_limiting_envelope(alpha)
        assert surd_sign(Q(434, 1587) - actual, Q(4, 1587), 2) > 0

    assert 5 * Q(1, 2) ** 2 - 14 * Q(1, 2) + 5 < 0
    assert 5 - 14 + 5 < 0
    assert surd_sign(Q(-10, 81), Q(6, 81), 3) > 0
    assert surd_sign(Q(-221, 1728), Q(128, 1728), 3) > 0
    assert 3 * 128**2 - 221**2 == 311


def check_bellman_grid(max_k: int = 12, denominator: int = 48) -> int:
    points = tuple(Q(index, denominator) for index in range(denominator // 2 + 1))
    previous = {t: ZERO for t in points}
    checked = 0
    for _ in range(max_k):
        current: dict[Fraction, Fraction] = {}
        for t in points:
            current[t] = max((t - x) * phi(x) + previous[x] for x in points if x <= t)
            assert current[t] >= previous[t]
            assert current[t] <= integral_phi(t)
            if t > Q(1, 4):
                assert current[t] < integral_phi(t)
            checked += 1
        previous = current
    return checked


def check_fixed_k_rows(max_k: int = 12) -> None:
    m_values = [ZERO]
    q_values = [ZERO]
    sampled_optima: list[Fraction] = []

    for k in range(1, max_k + 1):
        q_k = 2 / (3 * (1 - m_values[-1]))
        m_k = q_k * q_k / 3
        q_values.append(q_k)
        m_values.append(m_k)

        point: list[Fraction] = []
        current = ONE
        for ratio_index in range(k, 0, -1):
            current *= q_values[ratio_index]
            point.append(current)
        assert ONE > point[0] > ZERO
        assert point[-1] > ZERO
        assert all(a > b for a, b in zip(point, point[1:]))
        assert normalized_value(tuple(point)) == m_k
        assert m_values[k - 1] < m_k < Q(1, 3)

        transition = (3 * q_k + 1) / (9 * q_k - 1)
        assert transition > Q(1, 2)

        lower, upper = critical_bracket(m_k)
        alpha = (lower + upper) / 2
        assert Q(1, 3) < alpha < Q(1, 2)
        assert critical_polynomial(lower, m_k) > 0
        assert critical_polynomial(upper, m_k) < 0

        second_left = -1 - Q(1, 3)
        second_right = -Q(3, 2) + 27 * m_k / 8
        assert second_left < 0
        assert second_right < 0

        s = 1 + alpha
        a_term = 3 * alpha - 1
        betas = tuple((s + a_term * x) / 4 for x in point)
        weights = tuple(a_term * x / beta for x, beta in zip(point, betas, strict=True))
        assert alpha > betas[0] > s / 4
        assert betas[-1] > s / 4
        assert all(a > b for a, b in zip(betas, betas[1:]))
        assert betas[0] < s / 3
        assert ONE > weights[0] > ZERO
        assert weights[-1] > ZERO
        assert all(a > b for a, b in zip(weights, weights[1:]))

        sampled = middle_envelope(alpha, m_k)
        assert surd_sign(Q(434, 1587) - sampled, Q(4, 1587), 2) > 0
        sampled_optima.append(sampled)

    assert all(
        later > earlier for earlier, later in zip(sampled_optima, sampled_optima[1:])
    )

    # The formal upper relaxation is already too weak for the sharp bound.
    assert surd_sign(m_values[7] - Q(434, 1587), Q(-4, 1587), 2) > 0


def main() -> None:
    check_clipping()
    check_integral_envelope()
    states = check_bellman_grid()
    check_fixed_k_rows()
    print("PASS: exact global finite-prefix clipped-envelope diagnostic")
    print(f"bellman_states={states}")
    print("fixed_k_rows=12")


if __name__ == "__main__":
    main()
