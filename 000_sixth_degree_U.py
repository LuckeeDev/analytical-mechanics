# This phase diagram was given as an exercise during a lecture on the 14th of November, 2023.

import matplotlib.pyplot as plt
import numpy as np

graph_name = "Sixth degree potential"

E1 = -2
E2 = 0
E3 = 1


def U(x):
	return (x - 0.5) * (x + 0.5) * (x - 1) * (x + 1) * (x - 2) * (x + 2)

def T(dxdt):
	return dxdt**2 / 2

def E(x, dxdt):
	return T(dxdt) + U(x)

x = np.linspace(-2.01, 2.01, num=1000)
y = np.linspace(-4, 4, num=1000)

fig, (ax1, ax2) = plt.subplots(2, sharex=True)

fig.canvas.manager.set_window_title(graph_name)
fig.suptitle(graph_name)

ax1.plot(x, U(x))
ax1.set(xlabel="x", ylabel="U(x)")

X, Y = np.meshgrid(x,y)
Z = E(X, Y)

levels = [E1, E2, E3]

ax2.contour(X,Y,Z, levels)
ax2.set(xlabel="x", ylabel="dx/dt")

plt.show()