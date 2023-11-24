import matplotlib.pyplot as plt
import numpy as np

M = 0.3
E1 = -2.4
E2 = -1.5
E3 = -0.4

def U(x):
	return 1 - np.cos(x) - M * x

def T(dxdt):
	return dxdt**2 / 2

def E(x, dxdt):
	return T(dxdt) + U(x)

x = np.linspace(4.5, 18, num=1000)
y = np.linspace(-4, 4, num=1000)

fig, (ax1, ax2) = plt.subplots(2, sharex=True)

fig.suptitle("Rotating pendulum")

ax1.plot(x, U(x))
ax1.set(xlabel="x", ylabel="U(x)")

X, Y = np.meshgrid(x,y)
Z = E(X, Y)

levels = [E1, E2, E3]

ax2.contour(X,Y,Z, levels)
ax2.set(xlabel="x", ylabel="dx/dt")

plt.show()