from eduray.math import Vector
from eduray.math.helpers import clamp_float_01

def fresnel_schlick(ray_dir: Vector, normal: Vector, ior_out: float = 1.0, ior_in: float = 1.5) -> float:
    """
    Schlick's approximation for Fresnel reflectance.
    ray_dir - direction of the incoming ray (should be normalized)
    normal - surface normal at the hit point (should be normalized)
    ior_out - index of refraction of the medium the ray is coming from (default is 1.0 for air)
    ior_in - index of refraction of the medium the ray is entering (default is 1.5 for glass)
    """
    d = ray_dir.normalize()
    n = normal.normalize()

    cos_theta = n.dot(-d)

    # flip normal if ray is inside the medium
    if cos_theta < 0.0:
        n = -n
        cos_theta = n.dot(-d)
        ior_out, ior_in = ior_in, ior_out

    cos_theta = clamp_float_01(cos_theta)

    r0 = ((ior_out - ior_in) / (ior_out + ior_in)) ** 2
    return r0 + (1.0 - r0) * (1.0 - cos_theta) ** 5