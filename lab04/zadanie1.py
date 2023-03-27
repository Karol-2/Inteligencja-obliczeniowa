import math

import numpy as np
import pyswarms as ps
from pyswarms.utils.plotters import plot_cost_history
from matplotlib import pyplot as plt


def endurance(tab):
    x, y, z, u, v, w = tab
    return -(math.exp(-2 * (y - math.sin(x)) ** 2) + math.sin(z * u) + math.cos(v * w))


def f(x):
    n_particles = x.shape[0]
    j = [endurance(x[i]) for i in range(n_particles)]
    return np.array(j)


options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}  # w - współcznynnik bezwładności, c1 - cognitive parameter, c2 - social parameter
x_max = np.ones(6)
x_min = np.zeros(6)
my_bounds = (x_min, x_max)

optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=6, options=options, bounds=my_bounds)
optimizer.optimize(f, iters=1000)

cost_history = optimizer.cost_history

plot_cost_history(cost_history)
plt.show()
print("Najlepszy wynik: ", abs(cost_history[-1]))