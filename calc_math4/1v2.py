import math
from matplotlib import mlab
import pylab


ARGS = [0.142, 0.494, 0.847, 1.199, 1.552, 1.904, 2.257, 2.609, 2.962]
VALUES = [5.642, 4.096, 3.390, 2.924, 2.775, 2.534, 2.418, 2.405, 2.298]


def compute_system(x, y):
    a = [[0 for _ in range(3)] for _ in range(3)]
    b = [0 for _ in range(3)]
    n = len(x)
    a[0][0] = sum(x[i] ** 2 for i in range(n))
    a[0][1] = sum(x[i] * math.exp(-x[i]) for i in range(n))
    a[1][0] = a[0][1]
    a[0][2] = sum(x)
    a[2][0] = a[0][2]
    a[1][1] = sum(math.exp(-x[i]) ** 2 for i in range(n))
    a[1][2] = sum(math.exp(-x[i]) for i in range(n))
    a[2][1] = a[1][2]
    a[2][2] = n
    b[0] = sum(y[i] * x[i] for i in range(n))
    b[1] = sum(y[i] * math.exp(-x[i]) for i in range(n))
    b[2] = sum(y)
    return a, b


def solve_with_gauss(a, b):
    for i in range(len(a)):
        divisor = a[i][i]
        a[i][i:len(a)] = [a[i][j] / divisor for j in range(i, len(a))]
        b[i] /= divisor
        if i == len(a):
            break
        for j in range(i + 1, len(a)):
            difference = a[j][i]
            a[j] = [a[j][k] - difference * a[i][k] for k in range(len(a))]
            b[j] -= difference * b[i]
    x = [0 for _ in range(len(a))]
    for i in reversed(range(len(a))):
        x[i] = b[i] - sum(x[j] * a[i][j] for j in range(i + 1, len(a)))
    return x


def plot(a, b, c):
    x_min = ARGS[0]
    x_max = ARGS[-1]
    dx = 0.001
    x_list = mlab.frange(x_min, x_max, dx)
    y_list = [a * arg + b * math.exp(-arg) + c for arg in x_list]
    pylab.scatter(ARGS, VALUES)
    pylab.plot(x_list, y_list)
    pylab.show()


if __name__ == "__main__":
    matrix, remainder = compute_system(ARGS, VALUES)
    q_a, q_b, q_c = solve_with_gauss(matrix, remainder)
    print(q_a, q_b, q_c)
    plot(q_a, q_b, q_c)