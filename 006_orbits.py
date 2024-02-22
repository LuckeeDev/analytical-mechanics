# This example was discussed during the lecture on the 12th of December, 2023

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

M: float = 1
E: float = -2
r0: float = 1.5
drdt0: float = 1
phi0: float = 0


def U(r: float):
    return np.exp(r - 6) - 4


def V(r: float):
    return U(r) + M**2 / (2 * r**2)


def drdt(_, r: float) -> float:
    return np.sqrt(2 * (E - V(r)))


# y is [r, dr/dt,, dphi/dt]
def system(_, y):
    return [y[1], -np.exp(y[0] - 6) + M**2 / y[0] ** 3, M / y[0] ** 2]


t0 = 0
tf = 180
result = spi.solve_ivp(
    system, [t0, tf], [r0, drdt0, phi0], t_eval=np.linspace(t0, tf, 1000)
)


fig = plt.figure(figsize=(10, 5))

# Normal plot
ax1 = fig.add_subplot(1, 2, 1)
ax1.axhline(y=E, color="r", linestyle="--", label="E")
ax1.set_xlabel("r")
ax1.set_ylabel("V(r)")
r_begin = 0.3
r_end = 7.5
ax1.plot(
    np.linspace(r_begin, r_end, 100), [V(r) for r in np.linspace(r_begin, r_end, 100)]
)
ax1.legend()

# Polar plot
ax2 = fig.add_subplot(1, 2, 2, projection="polar")
time_step = (tf - t0) / 1000
r_values = result.y[0]
phi_values = result.y[2]
ax2.plot(phi_values, r_values)

plt.show()
