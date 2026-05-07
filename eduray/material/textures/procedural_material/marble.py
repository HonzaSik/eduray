from dataclasses import dataclass, field
import math
from eduray.material.color import clamp01
from eduray.material.material.phong_material import PhongMaterial, PhongMaterialSample
from eduray.material.textures.noise.noise import Noise
from eduray.material.textures.noise.perlin_noise import PerlinNoise
from eduray.math import Vector

# Marble texture based on the classical procedural approach
# related procedural texturing concepts are discussed in Ebert et al. (2003). TEXTURING & MODELING A Procedural Approach

@dataclass
class MarbleMaterial(PhongMaterial):
    """
    Marble material with procedural vein patterns. Uses a combination of sine waves and noise to create the characteristic swirling veins of marble.
     - vein_scale: Controls the frequency of the veins (higher values create more veins)
     - warp_strength: Controls how much the noise warps the veins (higher values create more distortion)
     - vein_sharpness: Controls how sharp the veins are (higher values create sharper veins)
     - color_noise: The noise function used to create color variation in the veins (default is Perlin noise)
     - n_noise: Optional noise function for adding surface detail to the normal (not used for vein generation)
     - color_one_factor: Multiplier for the base color in the lighter areas of the veins
     - color_two_factor: Multiplier for the base color in the darker areas of the veins
    """
    vein_scale: float = 6.0
    warp_strength: float = 2.0
    vein_sharpness: float = 4.0
    color_noise: Noise = field(default_factory=PerlinNoise)
    n_noise: Noise | None = None
    color_one_factor: float = 1.0
    color_two_factor: float = 0.75

    def sample(self, hit) -> PhongMaterialSample:
        p = hit.point
        dir = Vector(1.0, 0.35, 0.15).normalize()
        u = p.dot(dir)
        w = self.color_noise.value(p * 1.2)

        phase = (
                u * self.vein_scale
                + w * self.warp_strength
                + 0.3 * self.color_noise.value(p * 3.7)
        )
        s = 0.5 + 0.5 * math.sin(phase)
        vein = 1.0 - (abs(s - 0.5) * 2.0)
        vein = clamp01(vein)
        veins = vein ** self.vein_sharpness

        light = self.base_color * self.color_one_factor
        dark  = self.base_color * self.color_two_factor
        base_color = dark * (1.0 - veins) + light * veins
        ambient_color = self.base_color * 0.5

        shin = max(10.0, self.shininess * (0.7 + 0.3 * veins))

        return PhongMaterialSample(
            base_color=base_color,
            spec_color=self.spec_color,
            shininess=float(shin),
            ior=self.ior,
            transparency=self.transparency,
            normal_noise=self.n_noise,
            ambient_color=ambient_color,
        )