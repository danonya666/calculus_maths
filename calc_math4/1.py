import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

x_data = np.array([0.142, 0.494, 0.847, 1.199, 1.552, 1.904, 2.257, 2.609, 2.962])
y_data = np.array([5.642, 4.096, 3.390, 2.924, 2.775, 2.534, 2.418, 2.405, 2.298])


def f1(x, *args):
    a, b, c = args
    return a * x + b * np.exp(-x) + c


def f2(x, *args):
    a, b, c = args
    return a / x + b * np.exp(x) + c


def f3(x, *args):
    a, b, c = args
    return np.log(x) * a * x + b * np.exp(x) + c


def f4(x, *args):
    a,b,c = args
    return a * np.sqrt(x) + b * np.sin(x) + c


"""popt, pcov = curve_fit(f1, x_data, y_data, p0=[1, 1, 1])
plt.plot(x_data, y_data, 'o')
plt.plot(x_data, f1(x_data, *popt), '-')"""

popt, pcov = curve_fit(f2, x_data, y_data, p0=[1, 1, 1])
plt.plot(x_data, y_data, 'o')
plt.plot(x_data, f2(x_data, *popt), '-')

"""popt, pcov = curve_fit(f3, x_data, y_data, p0=[1, 1, 1])
plt.plot(x_data, y_data, 'o')
plt.plot(x_data, f3(x_data, *popt), '-')"""

"""popt, pcov = curve_fit(f4, x_data, y_data, p0=[1, 1, 1])
plt.plot(x_data, y_data, 'o')
plt.plot(x_data, f4(x_data, *popt), '-')"""

plt.show()


"""
НОРМАЛЬНАЯ СИСТЕМА УРАВНЕНИЙ
9a + 13.41b = 28.48 
13.41a + 56.93b = 60.35
"""