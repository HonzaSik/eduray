from typing import Callable
from enum import Enum


# enum of ease types
class EaseType(Enum):
    LINEAR = 1
    EASE_IN_OUT = 2


def linear(t: float) -> float:
    return t


def ease_in_out(t: float) -> float:
    if t < 0.5:
        return 2 * t * t
    else:
        return -1 + (4 - 2 * t) * t

# You can add more easing functions as needed, such as ease_in, ease_out, etc.

Easing = Callable[[float], float]
