from __future__ import annotations
import numpy as np
from dataclasses import dataclass, field
from eduray.math import Vertex, Vector
from eduray.geometry.primitive import Primitive
from eduray.geometry.ray import Ray
from eduray.geometry.geometry_hit import GeometryHit

# Ray-torus intersection by substituting the ray into the implicit torus equation.
# Based on Hanrahan's derivation in Glassner (1989).

@dataclass
class Torus(Primitive):
    """
    Circular torus primitive.

    The torus is represented by the standard implicit equation. Ray intersection
    is computed by substituting the ray equation into the implicit equation,
    which gives a quartic polynomial in the ray parameter t. The real roots are
    found numerically with numpy.roots, and the nearest valid root is used.

    The intersection method follows the standard ray/torus derivation described
    by Hanrahan in Glassner, An Introduction to Ray Tracing, 1989.
    """
    center: Vertex = field(default_factory=lambda: Vertex(0, 0, 0))
    radius_major: float = 1.0  # Major radius (distance from center to tube center)
    radius_tube: float  = 0.2  # Minor radius (tube radius)

    def normal_at(self, point: Vertex) -> Vector:
        hit = point - self.center
        nx = 4 * hit.x * (
                hit.x ** 2 + hit.y ** 2 + hit.z ** 2 - self.radius_major ** 2 - self.radius_tube ** 2)
        ny = 4 * hit.y * (
                hit.x ** 2 + hit.y ** 2 + hit.z ** 2 - self.radius_major ** 2 - self.radius_tube ** 2) + 8 * self.radius_major ** 2 * hit.y
        nz = 4 * hit.z * (
                hit.x ** 2 + hit.y ** 2 + hit.z ** 2 - self.radius_major ** 2 - self.radius_tube ** 2)
        return Vector(nx, ny, nz).normalize()

    def intersect(self, ray: Ray, t_min=1e-3, t_max=float('inf')) -> GeometryHit | None:
        ray_origin = ray.origin - self.center
        rd = ray.direction

        # coefficients for quartic equation
        ox, oy, oz = ray_origin.x, ray_origin.y, ray_origin.z
        dx, dy, dz = rd.x, rd.y, rd.z

        sum_d_sq = dx * dx + dy * dy + dz * dz
        e = ox * ox + oy * oy + oz * oz - self.radius_major * self.radius_major - self.radius_tube * self.radius_tube
        f = ox * dx + oy * dy + oz * dz
        four_R2 = 4.0 * self.radius_major * self.radius_major

        coeffs = [
            sum_d_sq * sum_d_sq,
            4.0 * sum_d_sq * f,
            2.0 * sum_d_sq * e + 4.0 * f * f + four_R2 * dy * dy,
            4.0 * f * e + 2.0 * four_R2 * oy * dy,
            e * e - four_R2 * (self.radius_tube * self.radius_tube - oy * oy)
        ]

        roots = np.roots(coeffs)
        roots = np.real(roots[np.isreal(roots)])
        roots = [r for r in roots if t_min < r < t_max]

        if not roots:
            return None

        t = min(roots)
        hit_point = ray.point_at(t)

        normal = self.normal_at(hit_point)

        return GeometryHit(
            point=hit_point,
            normal=normal,
            dist=t,
            front_face=ray.direction.dot(normal) < 0.0,
        )