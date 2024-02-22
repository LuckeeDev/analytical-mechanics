# This example was discussed during the lecture on the 12th of December, 2023

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import root_scalar
from utils.polar import *

M: float = 1
r0: float = 1
E: float = -3.4
phi0: float = 0


def U(r: float):
    return np.exp(r - 6) - 4


def V(r: float):
    return U(r) + M**2 / (2 * r**2)


drdt0 = np.sqrt(2 * (E - V(r0)))

r_min = root_scalar(lambda r: V(r) - E, bracket=[0.1, 5])
r_max = root_scalar(lambda r: V(r) - E, bracket=[5, 10])


# y is [r, dr/dt,, phi]
# return is [dr/dt, d^2r/dt^2, dphi/dt]
def system(_, y):
    return [y[1], -np.exp(y[0] - 6) + M**2 / y[0] ** 3, M / y[0] ** 2]


t0 = 0
tf = 150
result = solve_ivp(
    system, [t0, tf], [r0, drdt0, phi0], t_eval=np.linspace(t0, tf, 10000)
)


fig = plt.figure(figsize=(10, 5))

# Potential plot
ax1 = fig.add_subplot(1, 2, 1)
ax1.axhline(y=E, color="r", linestyle="--", label="E")
ax1.set_title("Effective potential")
ax1.set_xlabel("r")
ax1.set_ylabel("V(r)")
r_begin = 0.3
r_end = 7.5
ax1.plot(
    np.linspace(r_begin, r_end, 100),
    [V(r) for r in np.linspace(r_begin, r_end, 100)],
    label="V(r)",
)
ax1.legend()

# Orbit plot
r_values = result.y[0]
phi_values = result.y[2]
x_values, y_values = to_cartesian(r_values, phi_values)

ax2 = fig.add_subplot(1, 2, 2)
ax2.set_aspect("equal")
ax2.set_title("Orbit")
ax2.grid(True)

ax2.plot(x_values[0], y_values[0], marker="o", color="r")
ax2.plot(x_values[-1], y_values[-1], marker="o", color="r")

# Plot orbit
ax2.plot(x_values, y_values, label="Orbit", color="r")

# Plot limits: r_min and r_max
ax2.add_patch(
    patches.Circle(
        (0, 0),
        r_min.root,
        fill=False,
        color="tab:green",
        zorder=2,
        label="Minimum radius",
    )
)
ax2.add_artist(
    patches.Circle(
        (0, 0),
        r_max.root,
        fill=False,
        color="tab:purple",
        zorder=2,
        label="Maximum radius",
    )
)

ax2.legend()

plt.show()
