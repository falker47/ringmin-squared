"""Standalone exact diagnostic for the five-prefix rational witness."""

from fractions import Fraction


def prefix_objective(xs: tuple[Fraction, ...]) -> Fraction:
    previous = Fraction(1)
    total = Fraction(0)
    for current in xs:
        total += (previous - current) * current**2
        previous = current
    return total


def local_floor(alpha: Fraction, beta: Fraction, weight: Fraction) -> Fraction:
    scale = 1 + alpha
    return (
        weight
        * (4 * scale * beta - scale**2 - 2 * weight * beta**2)
        / (2 * (2 - weight))
    )


def main() -> None:
    q_values = [Fraction(2, 3)]
    for _ in range(4):
        q_values.append(Fraction(2, 3 - q_values[-1] ** 2))

    expected_q = (
        Fraction(2, 3),
        Fraction(18, 23),
        Fraction(1058, 1263),
        Fraction(3190338, 3666143),
        Fraction(26881208992898, 30143556935103),
    )
    assert tuple(q_values) == expected_q

    ratios = tuple(reversed(q_values))
    xs_list: list[Fraction] = []
    current = Fraction(1)
    for ratio in ratios:
        current *= ratio
        xs_list.append(current)
    xs = tuple(xs_list)

    denominator = 30143556935103
    numerators = (
        26881208992898,
        23392470652668,
        19595592993288,
        15335681473008,
        10223787648672,
    )
    expected_xs = tuple(Fraction(value, denominator) for value in numerators)
    assert xs == expected_xs
    assert Fraction(1) > xs[0] > xs[1] > xs[2] > xs[3] > xs[4] > 0

    m5 = Fraction(
        722599396919860307414438404,
        2725902074099388500860861827,
    )
    assert m5 == q_values[-1] ** 2 / 3
    assert prefix_objective(xs) == m5
    for index, current_x in enumerate(xs):
        previous_x = Fraction(1) if index == 0 else xs[index - 1]
        next_x = Fraction(0) if index == len(xs) - 1 else xs[index + 1]
        assert 2 * previous_x * current_x - 3 * current_x**2 + next_x**2 == 0

    alpha = Fraction(13, 30)
    scale = 1 + alpha
    amplitude = 3 * alpha - 1
    assert scale == Fraction(43, 30)
    assert amplitude == Fraction(3, 10)

    betas = tuple((scale + amplitude * value) / 4 for value in xs)
    weights = tuple(amplitude * value / beta for value, beta in zip(xs, betas))
    expected_betas = (
        Fraction(512701276381837, 1205742277404120),
        Fraction(502235061361147, 1205742277404120),
        Fraction(21341062103609, 52423577278440),
        Fraction(20785421470529, 52423577278440),
        Fraction(20118652710833, 52423577278440),
    )
    expected_weights = (
        Fraction(322574507914776, 512701276381837),
        Fraction(280709647832016, 502235061361147),
        Fraction(10223787648672, 21341062103609),
        Fraction(8001225116352, 20785421470529),
        Fraction(5334150077568, 20118652710833),
    )
    assert betas == expected_betas
    assert weights == expected_weights

    lower_middle = scale / 4
    upper_middle = scale / 3
    assert 0 < betas[4] < betas[3] < betas[2] < betas[1] < betas[0] < alpha < 1
    assert all(lower_middle < beta < upper_middle for beta in betas)
    assert 0 < weights[4] < weights[3] < weights[2] < weights[1] < weights[0] < 1
    assert (
        sum(
            (
                1 - weights[0],
                weights[0] - weights[1],
                weights[1] - weights[2],
                weights[2] - weights[3],
                weights[3] - weights[4],
                weights[4],
            ),
            Fraction(0),
        )
        == 1
    )

    transformed = tuple(amplitude * value for value in xs)
    for beta, weight, transformed_x in zip(betas, weights, transformed):
        assert weight == 4 - scale / beta
        assert local_floor(alpha, beta, weight) == transformed_x**2 / 2

    p_alpha = (1 - alpha) * (alpha**2 + 4 * alpha + 1) / 6
    assert p_alpha == Fraction(44693, 162000)
    direct_coefficient = p_alpha
    previous_beta = alpha
    for beta, weight in zip(betas, weights):
        direct_coefficient += (previous_beta - beta) * local_floor(alpha, beta, weight)
        previous_beta = beta

    coefficient = Fraction(
        2263404122555368590593580404287,
        8177706222298165502582585481000,
    )
    assert direct_coefficient == p_alpha + amplitude**3 * m5 / 8
    assert direct_coefficient == coefficient

    separator = Fraction(75, 271)
    assert coefficient > separator
    assert (
        271 * coefficient.numerator - 75 * coefficient.denominator
        == 54550540142475357166378486777
    )

    c4_rational = 597580022071777213687318156
    c4_radical = 21288970076515705538
    c4_radicand = 2903456040383
    c4_denominator = 2290468477489828247376833403
    radical_gap = 75 * c4_denominator - 271 * c4_rational
    square_margin = radical_gap**2 - c4_radicand * (271 * c4_radical) ** 2
    assert radical_gap == 9840949830285493643999284949
    assert square_margin == (202909790739538065073835756341295480167322654096276669)
    assert radical_gap > 0
    assert square_margin > 0

    print("five-prefix rational asymptotic diagnostic: PASS")
    print(f"q5={q_values[-1]}")
    print(f"M5={m5}")
    print(f"coefficient={coefficient}")
    print(f"separator={separator}")
    print(f"C4 radical gap={radical_gap}")
    print(f"C4 squared margin={square_margin}")


if __name__ == "__main__":
    main()
