from typing import Callable
from enum import Enum

# See, http://robertpenner.com/easing/ if you want to add more easing functions

# enum of ease types
class EaseType(Enum):
    LINEAR = 1
    EASE_IN_OUT = 2


def linear(t: float) -> float:
    return t


def ease_in_out(t: float) -> float:
    t = max(0.0, min(1.0, t))

    if t <= 0.5:
        return 0.5 * (2.0 * t) ** 2

    u = 2.0 * (1.0 - t)
    return 1.0 - 0.5 * u ** 2

# You can add more easing functions as needed, such as ease_in, ease_out, etc.

Easing = Callable[[float], float]
