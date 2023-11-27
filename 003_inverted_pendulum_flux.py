# This example was discussed during a lecture on the 21st of November, 2023.

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

graph_name = "Inverted pendulum flux"

fig = plt.gcf()
fig.canvas.manager.set_window_title(graph_name)
plt.title(graph_name)

# Define how many points should lie at a distance of RADIUS from the center
RADIUS = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
POINTS_COUNT = [1, 5, 10, 15, 20, 25, 30]

def system(_, y):
	return [y[1], y[0]]

def ra_pairs(r, n):
	for i in range(len(r)):
		for j in range(n[i]):
			# Yield radius and angle
			yield r[i], j * (2 * np.pi / n[i])

xi = []
dxdti = []

for r, a in ra_pairs(RADIUS, POINTS_COUNT):
	# Add 1 to the y component because the circle should be centered in (0,1)
	xi.append(r * np.cos(a))
	dxdti.append(r * np.sin(a) + 1)

plt.plot(xi, dxdti, 'bo', label="t=0s")

xf = []
dxdtf = []

for p in range(len(xi)):
	x = xi[p]
	dxdt = dxdti[p]
	
	solution = solve_ivp(system, [0, 1.4], [x, dxdt], t_eval=[1.4])

	xf.append(solution.y[0])
	dxdtf.append(solution.y[1])

plt.plot(xf, dxdtf, 'ro', label="t=1.4s")

plt.xlabel = "x"
plt.ylabel = "dx/dt"

plt.legend()
plt.grid()
plt.show()