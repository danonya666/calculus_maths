import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.015, 0.681, 1.342, 2.118, 2.671], dtype=float)
y = np.array([-2.417, -3.819, -0.642, 0.848, 2.815], dtype=float)


def interpolation_polynomial_lagrange(x, y, t):
    z = 0
    for j in range(len(y)):
        p1 = 1;
        p2 = 1
        for i in range(len(x)):
            if i == j:
                p1 = p1 * 1;
                p2 = p2 * 1
            else:
                p1 = p1 * (t - x[i])
                p2 = p2 * (x[j] - x[i])
        z = z + y[j] * p1 / p2
    return z


xnew = np.linspace(np.min(x), np.max(x), 100)
ynew = [interpolation_polynomial_lagrange(x, y, i) for i in xnew]
plt.plot(x, y, 'o', xnew, ynew)
plt.grid(True)
plt.show()
