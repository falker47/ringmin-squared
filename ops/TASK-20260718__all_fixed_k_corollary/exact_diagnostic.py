"""Exact bounded diagnostics for the all-fixed-k corollary."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q


@dataclass(frozen=True)
class QRoot2:
    """An exact element a + b*sqrt(2)."""

    a: Q
    b: Q = Q(0)

    @staticmethod
    def coerce(value: object) -> QRoot2:
        if isinstance(value, QRoot2):
            return value
        if isinstance(value, (int, Q)):
            return QRoot2(Q(value))
        return NotImplemented

    def __add__(self, other: object) -> QRoot2:
        rhs = self.coerce(other)
        if rhs is NotImplemented:
            return NotImplemented
        return QRoot2(self.a + rhs.a, self.b + rhs.b)

    __radd__ = __add__

    def __neg__(self) -> QRoot2:
        return QRoot2(-self.a, -self.b)

    def __sub__(self, other: object) -> QRoot2:
        rhs = self.coerce(other)
        if rhs is NotImplemented:
            return NotImplemented
        return self + (-rhs)

    def __rsub__(self, other: object) -> QRoot2:
        lhs = self.coerce(other)
        if lhs is NotImplemented:
            return NotImplemented
        return lhs - self

    def __mul__(self, other: object) -> QRoot2:
        rhs = self.coerce(other)
        if rhs is NotImplemented:
            return NotImplemented
        return QRoot2(
            self.a * rhs.a + 2 * self.b * rhs.b,
            self.a * rhs.b + self.b * rhs.a,
        )

    __rmul__ = __mul__

    def __truediv__(self, other: object) -> QRoot2:
        rhs = self.coerce(other)
        if rhs is NotImplemented:
            return NotImplemented
        norm = rhs.a * rhs.a - 2 * rhs.b * rhs.b
        if norm == 0:
            raise ZeroDivisionError
        return QRoot2(
            (self.a * rhs.a - 2 * self.b * rhs.b) / norm,
            (self.b * rhs.a - self.a * rhs.b) / norm,
        )

    def __rtruediv__(self, other: object) -> QRoot2:
        lhs = self.coerce(other)
        if lhs is NotImplemented:
            return NotImplemented
        return lhs / self

    def __pow__(self, exponent: int) -> QRoot2:
        if exponent < 0:
            return 1 / (self ** (-exponent))
        result = QRoot2(Q(1))
        base = self
        power = exponent
        while power:
            if power & 1:
                result *= base
            base *= base
            power //= 2
        return result

    def sign(self) -> int:
        """Return the exact sign using one rational squared comparison."""

        if self.b == 0:
            return (self.a > 0) - (self.a < 0)
        if self.a == 0 or (self.a > 0) == (self.b > 0):
            return (self.b > 0) - (self.b < 0)
        margin = self.a * self.a - 2 * self.b * self.b
        if margin == 0:
            return 0
        if self.a > 0:
            return (margin > 0) - (margin < 0)
        return (margin < 0) - (margin > 0)


def positive(value: QRoot2) -> bool:
    return value.sign() > 0


def main() -> None:
    alpha = QRoot2(Q(13, 23), Q(-2, 23))
    a_scale = 3 * alpha - 1
    s_scale = 1 + alpha
    lower_clip = s_scale / 4
    upper_clip = s_scale / 3

    assert positive(alpha - Q(1, 3))
    assert positive(Q(1, 2) - alpha)
    assert 23 * alpha**2 - 26 * alpha + 7 == QRoot2(Q(0))
    assert (46 * alpha - 26).sign() < 0

    p_alpha = (1 - alpha) * (alpha**2 + 4 * alpha + 1) / 6
    residual_limit = a_scale**3 / 24
    target = QRoot2(Q(434, 1587), Q(4, 1587))
    assert p_alpha == QRoot2(Q(9038, 36501), Q(722, 36501))
    assert residual_limit == QRoot2(Q(944, 36501), Q(-630, 36501))
    assert p_alpha + residual_limit == target

    m_values = [Q(0)]
    q_values = [Q(0)]
    for _ in range(8):
        q_value = Q(2, 3) / (1 - m_values[-1])
        q_values.append(q_value)
        m_values.append(q_value * q_value / 3)

    previous_coefficient = None
    for k in range(1, 9):
        x_values = [Q(1)]
        for remaining in range(k, 0, -1):
            x_values.append(x_values[-1] * q_values[remaining])
        assert all(x_values[i - 1] > x_values[i] > 0 for i in range(1, k + 1))

        objective = sum(
            (x_values[i - 1] - x_values[i]) * x_values[i] ** 2 for i in range(1, k + 1)
        )
        assert objective == m_values[k]

        betas = [alpha]
        lambdas = []
        residual = QRoot2(Q(0))
        for i in range(1, k + 1):
            x_value = x_values[i]
            beta = (s_scale + a_scale * x_value) / 4
            weight = a_scale * x_value / beta
            assert positive(beta - lower_clip)
            assert positive(upper_clip - beta)
            assert positive(alpha - beta)
            assert positive(weight)
            assert positive(1 - weight)
            if i > 1:
                assert positive(betas[-1] - beta)
                assert positive(lambdas[-1] - weight)

            g_value = (
                weight
                * (4 * s_scale * beta - s_scale**2 - 2 * weight * beta**2)
                / (2 * (2 - weight))
            )
            assert g_value == a_scale**2 * x_value**2 / 2
            residual += (betas[-1] - beta) * g_value
            betas.append(beta)
            lambdas.append(weight)

        expected_residual = a_scale**3 * m_values[k] / 8
        assert residual == expected_residual
        coefficient = p_alpha + expected_residual
        assert positive(target - coefficient)
        if previous_coefficient is not None:
            assert positive(coefficient - previous_coefficient)
        previous_coefficient = coefficient

    separator = Q(277, 1000)
    c5_upper = Q(276777463862377, 10**15)
    assert positive(target - separator)
    assert c5_upper < separator
    assert 4000**2 * 2 - 5599**2 == 651199

    print("PASS: exact all-fixed-k diagnostic (k=1..8)")


if __name__ == "__main__":
    main()
