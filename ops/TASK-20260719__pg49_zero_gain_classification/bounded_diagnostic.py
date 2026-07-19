"""Bounded falsification checks for PG49 descending-min zero gains.

This is the sole diagnostic for the task.  It uses only the Python standard
library, checks the known exact witness, scans a small literal row range, and
tests bounded rational approximants to the cubic plateau boundary.  Its
finite output is not used to prove any all-parameter statement.
"""

from __future__ import annotations

from decimal import Decimal, getcontext
from math import gcd


DIRECT_MAX_M = 500
NEAR_ROOT_MAX_W = 100_000
APPROX_DENOMINATOR_LIMIT = 10**200
MAX_G = 200


def ceil_div(a: int, b: int) -> int:
    assert a >= 0 and b > 0
    return (a + b - 1) // b


def kappa(m: int, j: int) -> int:
    d = 8 * m + 4
    return ceil_div(j * (d - 1), 2 * (d + j))


def gains(m: int, j: int, r: int) -> tuple[int, int]:
    left = (
        j * j
        - 26 * j * m
        - 3 * j * r
        - 7 * j
        + 8 * m * m
        - 4 * m * r
        - 12 * m
        - 4 * r
        - 4
    )
    right = left - j - 16 * m - 2 * r - 7
    return left, right


def literal_valid(m: int, j: int, r: int, side: int) -> bool:
    if not (m >= 3 and 1 <= j < m):
        return False
    if not (r == kappa(m, j) == kappa(m, j + 1)):
        return False
    return gains(m, j, r)[side] == 0


def parameters(side: int, g: int, u: int, w: int) -> tuple[int, int, int] | None:
    assert side in (0, 1)
    if not (g > 0 and u > w > 0 and gcd(u, w) == 1):
        return None
    j_num = g * u * (u - w) - (4 + 3 * side)
    m_num = g * u * (2 * u + 3 * w) - (8 + side)
    r_num = g * (10 * w * w - 4 * u * u - u * w) + (6 - 3 * side)
    if j_num % 5 or m_num % 20 or r_num % 10:
        return None
    return m_num // 20, j_num // 5, r_num // 10


def boundary_form(u: int, w: int) -> int:
    return 50 * w**3 + 51 * u * w**2 - 27 * u * u * w - 24 * u**3


def plateau_residuals(side: int, g: int, u: int, w: int) -> tuple[int, int]:
    """Return 25 times (upper residual at j+1, lower-interval slack at j)."""
    f = boundary_form(u, w)
    if side == 0:
        upper = g * g * u * f + g * (7 * u * u + 18 * u * w + 50 * w * w) + 31
        lower = -g * g * u * f + 3 * g * u * (u - w) + 4
    else:
        upper = g * g * u * f + 2 * g * u * (13 * u + 12 * w) - 6
        lower = -g * g * u * f + g * (50 * w * w - 16 * u * u - 9 * u * w) - 14
    return upper, lower


def active_scale_window(side: int, g: int, u: int, w: int) -> bool:
    """Evaluate the exact sign-dependent quadratic window for g."""
    f = boundary_form(u, w)
    assert f != 0
    if f < 0:
        h = -f
        if side == 0:
            s_left = 7 * u * u + 18 * u * w + 50 * w * w
            return u * h * g * g - s_left * g - 31 <= 0
        s_right = 2 * u * (13 * u + 12 * w)
        return u * h * g * g - s_right * g + 31 <= 0
    if side == 0:
        return u * f * g * g - 3 * u * (u - w) * g + 21 <= 0
    t_right = 50 * w * w - 16 * u * u - 9 * u * w
    return u * f * g * g - t_right * g + 39 <= 0


def cubic_root() -> Decimal:
    getcontext().prec = 600
    x = Decimal("1.416")
    for _ in range(100):
        value = 24 * x**3 + 27 * x**2 - 51 * x - 50
        derivative = 72 * x**2 + 54 * x - 51
        x -= value / derivative
    return x


def continued_fraction_convergents(x: Decimal) -> list[tuple[int, int]]:
    p_prev2, p_prev1 = 0, 1
    q_prev2, q_prev1 = 1, 0
    result: list[tuple[int, int]] = []
    for _ in range(2_000):
        a = int(x)
        p = a * p_prev1 + p_prev2
        q = a * q_prev1 + q_prev2
        if q > APPROX_DENOMINATOR_LIMIT:
            break
        result.append((p, q))
        p_prev2, p_prev1 = p_prev1, p
        q_prev2, q_prev1 = q_prev1, q
        x = 1 / (x - a)
    return result


def check_parameter_candidate(
    side: int, g: int, u: int, w: int
) -> tuple[int, int, int, int, int, int, int] | None:
    row = parameters(side, g, u, w)
    if row is None:
        return None
    m, j, r = row
    upper, lower = plateau_residuals(side, g, u, w)
    in_domain = m >= 3 and 1 <= j < m and r >= 1
    if in_domain:
        assert active_scale_window(side, g, u, w) == (upper >= 0 and lower > 0)
    assert (upper >= 0 and lower > 0) == (
        in_domain and r == kappa(m, j) == kappa(m, j + 1)
    )
    if literal_valid(m, j, r, side):
        return side, g, u, w, m, j, r
    return None


def main() -> None:
    known = (4, 11_116_408_784, 7_852_541_895)
    known_row = parameters(0, *known)
    assert known_row == (
        101_805_057_120_180_546_870,
        29_025_982_843_749_082_380,
        14_013_559_766_810_587_979,
    )
    assert literal_valid(*known_row, 0)
    assert gains(*known_row) == (0, -1_685_934_016_300_259_008_265)
    assert all(value > 0 for value in plateau_residuals(0, *known))

    literal_zeros: list[tuple[int, int, int, int]] = []
    for m in range(3, DIRECT_MAX_M + 1):
        for j in range(1, m):
            r = kappa(m, j)
            if r != kappa(m, j + 1):
                continue
            left, right = gains(m, j, r)
            if left == 0:
                literal_zeros.append((0, m, j, r))
            if right == 0:
                literal_zeros.append((1, m, j, r))

    root = cubic_root()
    candidate_zeros: set[tuple[int, int, int, int, int, int, int]] = set()
    for w in range(1, NEAR_ROOT_MAX_W + 1):
        center = int(root * w)
        for u in range(max(w + 1, center - 2), center + 3):
            if gcd(u, w) != 1:
                continue
            f = boundary_form(u, w)
            # At g >= 1, either plateau inequality forces this coarse bound.
            if abs(f) > 100 * (u + w):
                continue
            for side in (0, 1):
                for g in range(1, MAX_G + 1):
                    found = check_parameter_candidate(side, g, u, w)
                    if found is not None:
                        candidate_zeros.add(found)

    convergents = continued_fraction_convergents(root)
    for u, w in convergents:
        if u <= w:
            continue
        for side in (0, 1):
            for g in range(1, MAX_G + 1):
                found = check_parameter_candidate(side, g, u, w)
                if found is not None:
                    candidate_zeros.add(found)

    assert (0, *known, *known_row) in candidate_zeros
    known_index = convergents.index((known[1], known[2]))
    left_zeros = sorted(
        (item for item in candidate_zeros if item[0] == 0), key=lambda item: item[4]
    )
    right_zeros = sorted(
        (item for item in candidate_zeros if item[0] == 1), key=lambda item: item[4]
    )
    assert right_zeros
    for side, _g, _u, _w, m, j, r in left_zeros + right_zeros:
        assert literal_valid(m, j, r, side)
    _, right_g, right_u, right_w, right_m, right_j, right_r = right_zeros[0]
    right_d = 8 * right_m + 4
    right_q0 = 2 * right_r * (right_d + right_j) - right_j * (right_d - 1)
    right_q1 = 2 * right_r * (right_d + right_j + 1) - (right_j + 1) * (right_d - 1)
    right_k = right_r + 2 * right_m - 1 - right_j
    right_label = 4 * right_m - 2 * right_j - 1
    right_left_gain, right_right_gain = gains(right_m, right_j, right_r)
    assert right_right_gain == 0 < right_left_gain
    assert 0 <= right_q0 < 2 * (right_d + right_j)
    assert 0 <= right_q1 < 2 * (right_d + right_j + 1)
    print("PG49 zero-gain bounded diagnostic: PASS")
    print(f"literal rows checked: m=3..{DIRECT_MAX_M}")
    print(f"literal zero gains: {literal_zeros}")
    print(f"near-root denominator scan: w<= {NEAR_ROOT_MAX_W}")
    print(f"continued-fraction denominator limit: {APPROX_DENOMINATOR_LIMIT}")
    print(f"parameter scale bound: g<= {MAX_G}")
    print(f"bounded left parameter zeros: {len(left_zeros)}")
    print(f"bounded right parameter zeros: {len(right_zeros)}")
    print(f"first three left rows by m: {left_zeros[:3]}")
    print(f"first three right rows by m: {right_zeros[:3]}")
    print(
        "smallest bounded right witness details:",
        (right_g, right_u, right_w, right_m, right_j, right_r),
    )
    print(
        "right label, singleton index, L, R, q0, q1:",
        (
            right_label,
            right_k,
            right_left_gain,
            right_right_gain,
            right_q0,
            right_q1,
        ),
    )
    print(
        "right plateau denominators:",
        (2 * (right_d + right_j), 2 * (right_d + right_j + 1)),
    )
    print(f"known boundary form F(u,w): {boundary_form(known[1], known[2])}")
    print(f"known witness convergent index (zero based): {known_index}")
    print(f"neighboring convergents: {convergents[known_index - 2 : known_index + 3]}")


if __name__ == "__main__":
    main()
