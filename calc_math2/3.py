from math import sin
from typing import Callable
import unittest


def secant(f: Callable[[float], float], x0: float, eps: float = 1e-3, kmax: int = 1e3) -> float:
    """
    solves f(x) = 0 by secant method with precision eps
    :param f: f
    :param x0: starting point
    :param eps: precision wanted
    :return: root of f(x) = 0
    """
    x, x_prev, i = x0, x0 + 2 * eps, 0

    while abs(x - x_prev) >= eps and i < kmax:
        x, x_prev, i = x - f(x) / (f(x) - f(x_prev)) * (x - x_prev), x, i + 1

    return x


class TestSecant(unittest.TestCase):
    def test_0(self):
        def f(x: float) -> float:
            return 2 - 0.5 * x ** 2 - 0.5 * x ** -1 * sin(x) - x

        x0, x_star = 0.5, 1.0424308094424766

        self.assertAlmostEqual(secant(f, x0), x_star)


if __name__ == '__main__':
    unittest.main()