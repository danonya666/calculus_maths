import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline

# experimental data
arr_x = [0.015, 0.681, 1.342, 2.118, 2.671]
arr_y = [-2.417, -3.819, -0.642, 0.848, 2.815]

xi = np.array(arr_x)
yi = np.array(arr_y)

x = np.linspace(xi.min(), xi.max(), len(xi) * 100)

# sp = InterpolatedUnivariateSpline(xi, yi, k=1)
# y = sp(x)

# interpolation
plt.plot(xi, yi, '-')
plt.grid(True)
plt.show()
