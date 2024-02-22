# This example was discussed during the lecture on the 12th of December, 2023

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from utils.polar import *

M: float = 1
r0: float = 1
drdt0: float = 1
phi0: float = 0


def U(r: float):
    return np.exp(r - 6) - 4


def V(r: float):
    return U(r) + M**2 / (2 * r**2)


E = V(r0) + drdt0**2 / 2


# y is [r, dr/dt,, phi]
# return is [dr/dt, d^2r/dt^2, dphi/dt]
def system(_, y):
    return [y[1], -np.exp(y[0] - 6) + M**2 / y[0] ** 3, M / y[0] ** 2]


t0 = 0
tf = 180
result = solve_ivp(
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
ax2 = fig.add_subplot(1, 2, 2)
ax2.set_aspect("equal")
ax2.grid(True)
time_step = (tf - t0) / 1000
r_values = result.y[0]
phi_values = result.y[2]
x_values, y_values = to_cartesian(r_values, phi_values)
ax2.plot(x_values, y_values, label="Orbit", color="tab:orange")
ax2.legend()

plt.show()
