from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from eduray.math import Vertex, Vector
from eduray.geometry.ray import Ray

@dataclass
class Camera(ABC):
    origin: Vertex = field(default_factory=lambda: Vertex(0, 0, 0))
    _aspect_ratio: float = 16.0 / 9.0

    @abstractmethod
    def make_ray(self, u: float, v: float) -> Ray:
        """Generate a ray for normalized image coordinates u, v in [-1, 1]."""
        pass

    @abstractmethod
    def update_camera(self) -> None:
        """Recalculate internal state after parameter changes."""
        pass

    @abstractmethod
    def copy(self) -> Camera:
        """Create a copy of the camera."""
        pass

    def translate(self, offset: Vector) -> None:
        """Translate the camera by adding an offset to its origin."""
        self.origin += offset

    def set_aspect_ratio(self, aspect_ratio: float) -> None:
        """Set the camera's aspect ratio and update internal state accordingly."""
        self._aspect_ratio = aspect_ratio
        self.update_camera()

    def zoom(self, factor: float) -> None:
        """Zoom the camera by scaling the field of view or focal length."""
        pass