from dataclasses import dataclass
from eduray.math.vertex import Vertex
from eduray.material.material.phong_material import PhongMaterial, PhongMaterialSample
from eduray.material.textures.noise.noise import Noise
from eduray.math.helpers import smooth_interpolation
from eduray.scene.surface_interaction import SurfaceInteraction

# related procedural texturing concepts are discussed in Ebert et al. (2003).

@dataclass
class RockMaterial(PhongMaterial):
    color_scale: float = 3.0
    color_noise: Noise | None = None
    normal_noise: Noise | None = None

    def sample(self, hit: SurfaceInteraction) -> PhongMaterialSample:
        p = hit.point

        if self.color_noise is not None:
            t = 0.5 * self.color_noise.value(p * Vertex(self.color_scale, self.color_scale, self.color_scale)) + 0.5
            t = smooth_interpolation(0.35, 0.75, t)
        else:
            t = 0.5

        dark = self.base_color * 0.2
        light_color = self.base_color * 1.5
        base_color = dark * (1.0 - t) + light_color * t
        ambient_color = self.base_color * 0.5

        shin = self.shininess * (1.0 - t)

        return PhongMaterialSample(
            base_color=base_color,
            spec_color=self.spec_color,
            shininess=float(shin),
            ior=self.ior,
            transparency=self.transparency,
            normal_noise=self.normal_noise,
            ambient_color=ambient_color,
        )