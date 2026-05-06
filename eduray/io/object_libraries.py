from dataclasses import dataclass, field
from eduray.material.color import Color
from eduray.scene.light import Light, LightType
from eduray.material.material.material import Material

# this file is not used in the current implementation, but it was intended to be a simple way to manage libraries of materials, colors, and lights.
# I also used it for my internal testing a log way ago, and it might be useful in the future so i do not delete it.
# The idea was to have a simple way to store and access commonly used colors, materials, and lights by name, and to be able to easily save and load these libraries
# using the PickleManager. It also provides a convenient way to organize and manage these objects in a larger project and scene setup.

@dataclass
class ColorLibrary:
    """Simple library wrapper so you can access colors as attributes."""
    colors: dict[str, Color] = field(default_factory=dict)

    def __getattr__(self, name: str) -> Color:
        try:
            return self.colors[name]
        except KeyError:
            raise AttributeError(f"No color named '{name}'")

    def add(self, name: str, color: Color):
        self.colors[name] = color

    def get_all_names(self) -> list[str]:
        return list(self.colors.keys())


@dataclass
class LightLibrary:
    """Container for various object libraries."""
    lights: dict[str, Light] = field(default_factory=dict)

    def __getattr__(self, name: str) -> Light:
        try:
            return self.lights[name]
        except KeyError:
            raise AttributeError(f"No light named '{name}'")

    def add(self, name: str, light: Light):
        """
        Add a light to the library.
        :param name: Name of the light
        :param light: Light object
        :return: None
        """
        self.lights[name] = light

    def get_all_names(self) -> list[str]:
        """
        Get all light names from the library.
        :return: List of all light names
        """
        return list(self.lights.keys())

    def get_all_lights(self) -> list[Light]:
        """
        Get all lights from the library.
        :return: List of all Lights
        """
        return list(self.lights.values())

    def get_point_lights(self) -> list[Light]:
        """
        Get all point lights from the library.
        :return: List of Point Lights
        """
        return [light for light in self.lights.values() if
                isinstance(light.type, LightType) and light.type == LightType.POINT]

    def get_ambient_light(self) -> Light | None:
        """
        Get the ambient light from the library, if it exists. Assumes only one ambient light else returns the first one found.
        :return: Ambient Light or None if not found
        """
        for light in self.lights.values():
            if light.type == LightType.AMBIENT:
                return light
        return None


@dataclass
class MaterialLibrary:
    """Simple library wrapper so you can access material as attributes."""
    materials: dict[str, Material] = field(default_factory=dict)

    def __getattr__(self, name: str) -> Material:
        try:
            return self.materials[name]
        except KeyError:
            raise AttributeError(f"No material named '{name}'")

    def add(self, name: str, material: Material):
        self.materials[name] = material

    def get_all_names(self) -> list[str]:
        return list(self.materials.keys())
