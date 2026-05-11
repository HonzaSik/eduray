from __future__ import annotations

from eduray.material.color import Color, clamp_color255
from eduray.scene.surface_interaction import SurfaceInteraction
from eduray.scene.light import Light
from eduray.scene.scene import Scene
from eduray.math import Vector
from .local_shading import LocalShading

# Simple Lambertian diffuse shader.
# Uses the cosine term max(0, n·l), as described in standard computer graphics texts.

class LambertShader(LocalShading):
    def shade(
        self,
        hit: SurfaceInteraction,
        light: Light,
        view_dir: Vector,
        scene: Scene | None = None
    ) -> Color:
        material = hit.material

        n = hit.normal.normalize()
        l = (light.position - hit.point).normalize()
        intensity = light.intensity_at(hit.point)

        ndotl = max(0.0, n.dot(l))
        return material.get_color() * ndotl * intensity

    def shade_multiple_lights(
        self,
        hit: SurfaceInteraction,
        lights: list[Light],
        view_dir: Vector,
        scene: Scene | None = None
    ) -> Color:
        color = Color.custom_rgb(0, 0, 0)

        for light in lights:
            color += self.shade(hit, light, view_dir, scene)

        return clamp_color255(color)