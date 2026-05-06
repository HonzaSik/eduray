from dataclasses import dataclass
from eduray.geometry.ray import Ray
from eduray.material.color import Color
from eduray.render.integrator.integrator import Integrator
from eduray.scene.scene import Scene
from eduray.shading.local_shading import LocalShading
from eduray.shading.color_shader import ColorShader


@dataclass
class RayCaster(Integrator):
    scene: Scene
    shader: LocalShading | None = None

    def __post_init__(self):
        if self.shader is None:
            self.shader = ColorShader()

    def cast_ray(self, ray: Ray, depth: int | None = None) -> Color:
        hit = self.scene.intersect(ray)

        if hit is not None:
            return self.shader.shade_multiple_lights(
                hit,
                lights=self.scene.lights,
                view_dir=-ray.direction,   # ray to camera is opposite of ray direction
                scene=self.scene
            )

        return self.scene.background_color if hasattr(self.scene, "background_color") else Color(0, 0, 0)