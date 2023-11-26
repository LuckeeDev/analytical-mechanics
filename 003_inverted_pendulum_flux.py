# This example was discussed during a lecture on the 21st of November, 2023.

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define how many points should lie at a distance of RADIUS from the center
RADIUS = [0.0, 0.05, 0.10, 0.15, 0.20, 0.25]
POINTS_COUNT = [1, 5, 10, 15, 20, 25, 30]

def system(_, y):
	return [y[1], y[0]]

def ra_pairs(r, n):
	for i in range(len(r)):
		for j in range(n[i]):
			# Yield radius and angle
			yield r[i], j * (2 * np.pi / n[i])

for r, a in ra_pairs(RADIUS, POINTS_COUNT):
	# Add 1 to the y component because the circle should be centered in (0,1)
	x = r * np.cos(a)
	dxdt = r * np.sin(a) + 1

	plt.plot(x, dxdt, 'bo')

	solution = solve_ivp(system, [0, 1.4], [x, dxdt], t_eval=[1.4])

	new_x = solution.y[0]
	new_dxdt = solution.y[1]

	plt.plot(new_x, new_dxdt, 'ro')

plt.xlabel = "x"
plt.ylabel = "dx/dt"
plt.grid()
plt.show()