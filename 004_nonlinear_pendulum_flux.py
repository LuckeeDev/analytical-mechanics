# This example was discussed during a lecture on the 21st of November, 2023.

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

graph_name = "Non-linear pendulum flux"

fig = plt.gcf()
fig.canvas.manager.set_window_title(graph_name)
plt.title(graph_name)

plt.xlabel("x")
plt.ylabel("dx/dt")

plt.grid()

def U(x):
	return -np.cos(x)

def T(dxdt):
	return dxdt**2 / 2

def E(x, dxdt):
	return U(x) + T(dxdt)

X, Y = np.meshgrid(np.linspace(-2, 2, num=1000), np.linspace(-2, 2, num=1000))

E2 = -0.5
E1 = E(0, 0.5)
E3 = E(0, 1.5)

plt.contour(X, Y, E(X, Y), levels=[E1, E2, E3])

# Define how many points should lie at a distance of RADIUS from the center
RADIUS = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
POINTS_COUNT = [1, 5, 10, 15, 20, 25]

def system(_, y):
	return [y[1], -np.sin(y[0])]

def ra_pairs(r, n):
	for i in range(len(r)):
		for j in range(n[i]):
			# Yield radius and angle
			yield r[i], j * (2 * np.pi / n[i])

xi = [r*np.cos(a) for r, a in ra_pairs(RADIUS, POINTS_COUNT)]
# Add 1 to the y component because the circle should be centered in (0,1)
dxdti = [r*np.sin(a) + 1 for r, a in ra_pairs(RADIUS, POINTS_COUNT)]

plt.plot(xi, dxdti, 'bo', label="t=0s")

t0 = 0
tf = 5

xf = []
dxdtf = []

# compute solutions
for p in range(len(xi)):
	x = xi[p]
	dxdt = dxdti[p]

	solution = solve_ivp(system, [t0, tf], [x, dxdt], t_eval=[tf])

	xf.append(solution.y[0][0])
	dxdtf.append(solution.y[1][0])

plt.plot(xf, dxdtf, 'ro', label="t=5s")

plt.legend()
plt.show()
