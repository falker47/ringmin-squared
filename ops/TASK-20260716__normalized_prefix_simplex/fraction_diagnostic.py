"""Independent exact diagnostics for the normalized prefix simplex lemma."""

from fractions import Fraction
from itertools import combinations_with_replacement
from math import comb


MAX_K = 8
GRID_DENOMINATOR = 12


def objective(coordinates: tuple[Fraction, ...]) -> Fraction:
    previous = Fraction(1)
    total = Fraction(0)
    for coordinate in coordinates:
        total += (previous - coordinate) * coordinate**2
        previous = coordinate
    return total


def bellman_values(max_k: int) -> tuple[Fraction, ...]:
    values = [Fraction(0)]
    for _ in range(max_k):
        previous = values[-1]
        values.append(Fraction(4, 27) / (1 - previous) ** 2)
    return tuple(values)


def candidate_ratios(max_k: int) -> tuple[Fraction, ...]:
    ratios = [Fraction(2, 3)]
    for _ in range(1, max_k):
        ratios.append(Fraction(2, 3 - ratios[-1] ** 2))
    return tuple(ratios)


def coordinates_for_k(
    forward_ratios: tuple[Fraction, ...],
    k: int,
) -> tuple[Fraction, ...]:
    coordinate = Fraction(1)
    coordinates = []
    for ratio in reversed(forward_ratios[:k]):
        coordinate *= ratio
        coordinates.append(coordinate)
    return tuple(coordinates)


def certificate_remainder(
    coordinates: tuple[Fraction, ...],
    bellman: tuple[Fraction, ...],
    forward_ratios: tuple[Fraction, ...],
) -> Fraction:
    k = len(coordinates)
    previous = Fraction(1)
    total = Fraction(0)
    for index, coordinate in enumerate(coordinates):
        remaining = k - index
        ratio = forward_ratios[remaining - 1]
        total += (
            (1 - bellman[remaining - 1])
            * (coordinate - ratio * previous) ** 2
            * (coordinate + ratio * previous / 2)
        )
        previous = coordinate
    return total


def brute_grid_maximum(k: int, denominator: int) -> Fraction:
    best_numerator = -1
    for nondecreasing in combinations_with_replacement(range(denominator + 1), k):
        previous = denominator
        numerator = 0
        for coordinate in reversed(nondecreasing):
            numerator += (previous - coordinate) * coordinate**2
            previous = coordinate
        best_numerator = max(best_numerator, numerator)
    return Fraction(best_numerator, denominator**3)


def discrete_bellman_grid_maximum(k: int, denominator: int) -> Fraction:
    previous_layer = [0] * (denominator + 1)
    for _ in range(k):
        current_layer = []
        for previous in range(denominator + 1):
            current_layer.append(
                max(
                    (previous - coordinate) * coordinate**2
                    + previous_layer[coordinate]
                    for coordinate in range(previous + 1)
                )
            )
        previous_layer = current_layer
    return Fraction(previous_layer[denominator], denominator**3)


def main() -> None:
    bellman = bellman_values(MAX_K)
    forward_ratios = candidate_ratios(MAX_K)

    documented = {
        1: ((Fraction(2, 3),), Fraction(4, 27)),
        2: (
            (Fraction(18, 23), Fraction(12, 23)),
            Fraction(108, 529),
        ),
        3: (
            (
                Fraction(1058, 1263),
                Fraction(276, 421),
                Fraction(184, 421),
            ),
            Fraction(1_119_364, 4_785_507),
        ),
    }
    expected_grid = (
        Fraction(4, 27),
        Fraction(13, 64),
        Fraction(403, 1728),
        Fraction(1, 4),
        Fraction(151, 576),
        Fraction(235, 864),
        Fraction(161, 576),
        Fraction(247, 864),
    )

    assert bellman[0] == 0
    assert Fraction(0) < bellman[1] < Fraction(1, 3)
    assert all(
        Fraction(0) < bellman[k - 1] < bellman[k] < Fraction(1, 3)
        for k in range(2, MAX_K + 1)
    )

    print("exact normalized optima")
    for k in range(1, MAX_K + 1):
        coordinates = coordinates_for_k(forward_ratios, k)
        ratios = tuple(reversed(forward_ratios[:k]))
        direct_value = objective(coordinates)
        recurrence_value = bellman[k]

        chain = (Fraction(1), *coordinates)
        assert all(
            left > right
            for left, right in zip(chain[:-1], chain[1:], strict=True)
        )
        assert coordinates[-1] > 0
        assert direct_value == recurrence_value == ratios[0] ** 2 / 3

        extended = (*coordinates, Fraction(0))
        for index, coordinate in enumerate(coordinates):
            previous = Fraction(1) if index == 0 else coordinates[index - 1]
            following = extended[index + 1]
            assert 2 * previous * coordinate - 3 * coordinate**2 + following**2 == 0

        if k in documented:
            assert (coordinates, recurrence_value) == documented[k]

        sample = tuple(Fraction(k - index, k + 2) for index in range(k))
        assert recurrence_value - objective(sample) == certificate_remainder(
            sample,
            bellman,
            forward_ratios,
        )

        print(f"k={k}: q_k={forward_ratios[k - 1]}, M_k={recurrence_value}")

    print(f"independent denominator-{GRID_DENOMINATOR} grid")
    grid_values = []
    total_states = 0
    for k in range(1, MAX_K + 1):
        brute_value = brute_grid_maximum(k, GRID_DENOMINATOR)
        dynamic_value = discrete_bellman_grid_maximum(k, GRID_DENOMINATOR)
        assert brute_value == dynamic_value == expected_grid[k - 1]
        assert brute_value <= bellman[k]
        grid_values.append(brute_value)
        total_states += comb(GRID_DENOMINATOR + k, k)

    print(f"grid_values={tuple(grid_values)}")
    print(f"literal_grid_states={total_states}")
    print("all Fraction diagnostics passed")


if __name__ == "__main__":
    main()
