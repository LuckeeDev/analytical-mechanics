import matplotlib.pyplot as plt
import numpy as np

M = 0.3

def U(x):
	return 1 - np.cos(x) - M * x

def T(dxdt):
	return dxdt**2 / 2

def E(x, dxdt):
	return T(dxdt) + U(x)

x = np.linspace(3, 15, num=1000)
y = np.linspace(-4, 4, num=1000)

fig, (ax1, ax2) = plt.subplots(2, sharex=True)

fig.suptitle("Rotating pendulum")

ax1.plot(x, U(x))
ax1.set(xlabel="x", ylabel="U(x)")

X, Y = np.meshgrid(x,y)
Z = E(X, Y)

levels = [-1.5, -0.4, 1]

ax2.contour(X,Y,Z, levels)
ax2.set(xlabel="x", ylabel="dx/dt")

plt.show()