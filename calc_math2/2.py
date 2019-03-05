from cmath import sin, cos

import math


def F(x):
    return 2 - 0.5 * x ** 2 - 0.5 * x ** -1 * sin(x) - x


def F1(x):
    """Производная F(x)"""
    return -x - 1 - 0.5 * cos(x) / x + 0.5 * sin(x) / x ** 2


def newton(a, b, epsilon=math.pow(10, -3)):
    try:
        x0 = (a + b) / 2
        xn = F(x0)
        xn1 = xn - F(xn) / F1(xn)
        while abs(xn1 - xn) > epsilon:
            xn = xn1
            xn1 = xn - F(xn) / F1(xn)
        return xn1
    except ValueError:
        print("Value not invalidate")


print(newton(-10, 11))
