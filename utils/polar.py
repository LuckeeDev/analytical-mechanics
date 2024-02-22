from typing import Tuple
import numpy as np


def to_cartesian(r: float, phi: float) -> Tuple[float, float]:
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    return (x, y)
