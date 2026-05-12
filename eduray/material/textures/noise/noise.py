from abc import ABC, abstractmethod
from dataclasses import field, dataclass
from eduray.math.vector import Vector
from eduray.math.vertex import Vertex

@dataclass
class Noise(ABC):
    """
    Abstract base class for procedural noise textures.
    scale: Scaling factor intended for transforming input coordinates before sampling.
    offset: Optional coordinate offset that concrete noise implementations may use to shift the noise pattern.
    strength: Controls the strength of the effect, for example the amplitude of normal perturbation in bump mapping.
    eps: A small epsilon value used to prevent issues with floating-point precision when sampling the noise function, especially for functions that may have discontinuities
    """
    scale: float = 1.0
    offset: Vector = field(default_factory=lambda: Vector(0.0, 0.0, 0.0))
    strength: float = 0.0
    eps: float = 1e-3

    @abstractmethod
    def value(self, position: Vertex | Vector) -> float:
        """
        Get the noise value at a given vector position.
        :param position: Vector position to sample the noise
        :return: Noise value as a float
        """
        raise NotImplementedError

    def noise_fn(self, x: float, y: float) -> float:
        """
        Get the noise value at a given (x, y) coordinate by calling the value method with a Vector for Z = 0.0.
        :param x: X coordinate to sample the noise
        :param y: Y coordinate to sample the noise
        :return: Noise value as a float
        """
        return self.value(Vector(x, y, 0.0))
