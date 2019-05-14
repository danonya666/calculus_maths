import numpy as np

A = 2
B = 3


def f(x):
    return x ** -0.5 * np.log(x)


def F(x, c=0):
    return 2 * np.sqrt(x) * (np.log(x) - 2) + c


def newton_meth(a=A, b=B):
    return F(b) - F(a)


def trapeze_meth(func=f, n=20, a=A, b=B):
    delta = float(b - a) / n
    result = 0.5 * (func(a) + func(b))
    for i in range(1, n):
        result += func(a + i * delta)
    result *= delta
    return result


def simp_meth(func=f, n=20, a=A, b=B):
    delta = float(b - a) / (2 * n)
    result = func(a) + func(b)
    for i in range(1, 2 * n):
        if i % 2 == 0:
            result += 2 * func(a + delta * i)
        else:
            result += 4 * func(a + delta * i)
    result *= delta / 3
    return result


if __name__ == '__main__':
    print("newton_meth:\n", newton_meth())
    print("trapeze_meth:\n", trapeze_meth())
    print("simp_meth:\n", simp_meth())

