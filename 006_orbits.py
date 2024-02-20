# This example was discussed during the lecture on the 12th of December, 2023

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
import scipy.optimize as spo

M: float = 0.5
E: float = -1.8
r0: float = 0.2


def U(r: float):
    return -1 / r


def V(r: float):
    return U(r) + M**2 / (2 * r**2)


def drdt(t: float, r: float) -> float:
    return np.sqrt(2 * (E - V(r)))


sol = spi.solve_ivp(drdt, [0, 0.3], [r0], t_eval=np.linspace(0, 0.3))


def integrand(x: float):
    return M / x**2 / np.sqrt(2 * (E - V(x)))


def phi(r: float):
    return spi.quad(integrand, r0, r)


fig = plt.figure(figsize=(10, 5))

# Normal plot
ax1 = fig.add_subplot(1, 2, 1)
ax1.axhline(y=E, color="r", linestyle="--", label="E")
ax1.set_xlabel("r")
ax1.set_ylabel("V(r)")
r_begin = 0.15
r_end = 0.6
ax1.plot(
    np.linspace(r_begin, r_end, 100), [V(r) for r in np.linspace(r_begin, r_end, 100)]
)
ax1.legend()

# Polar plot
ax2 = fig.add_subplot(1, 2, 2, projection="polar")
r_values = sol.y[0]
phi_values = [phi(r) for r in r_values]
ax2.plot(phi_values, r_values)

plt.show()
