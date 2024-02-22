from typing import Tuple
import numpy as np


def to_cartesian(r, phi):
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    return (x, y)
