from pathlib import Path
from pickle import dump, load
from pprint import pprint
from typing import Any
from eduray.scene import Scene
from eduray.io.object_libraries import ColorLibrary, LightLibrary, MaterialLibrary

# this file is not used in the current implementation, but it was intended to be a simple way to manage libraries of materials, colors, and lights.
# I also used it for my internal testing a log way ago, and it might be useful in the future so i do not delete it.
# The idea was to have a simple way to store and access commonly used colors, materials, and lights by name, and to be able to easily save and load these libraries
# using the PickleManager. It also provides a convenient way to organize and manage these objects in a larger project and scene setup.

class PickleManager:
    """
    Manages saving and loading objects using pickle in a specified directory. Supports optional verbose mode (prints actions) and object validation.
    Can save/load lists or libraries (dicts) of Lights, Materials, and Colors.
    """

    def __init__(self, directory: str | Path = "./", verbose: bool = False):
        self.directory: Path = Path(directory)
        self.verbose: bool = verbose
        self.__post_init__()

    def __post_init__(self):
        self.directory.mkdir(parents=True, exist_ok=True)

    def set_verbose(self, verbose: bool) -> None:
        self.verbose = verbose

    def save(self, data: Any, filename: str | Path) -> Path:
        path = self.directory / Path(str(filename))
        with open(path, "wb") as f:
            dump(data, f)
        if self.verbose:
            print(f"Saved object to {path}")
            pprint(data)
        return path

    def load(self, filename: str | Path) -> Any:
        path = self.directory / Path(str(filename))
        with open(path, "rb") as f:
            obj = load(f)
        if self.verbose:
            print(f"Loaded object from {path}")
            pprint(obj)
        return obj

    def save_color_library(self, color_lib: ColorLibrary) -> None:
        self.save(color_lib.colors, "colors.pkl")

    def load_color_library(self) -> ColorLibrary:
        colors = self.load("colors.pkl")
        return ColorLibrary(colors)

    def save_light_library(self, light_lib: LightLibrary) -> None:
        self.save(light_lib.lights, "lights.pkl")

    def load_light_library(self) -> LightLibrary:
        lights = self.load("lights.pkl")
        return LightLibrary(lights)

    def save_material_library(self, material_lib: MaterialLibrary) -> None:
        self.save(material_lib.materials, "material.pkl")

    def load_material_library(self) -> MaterialLibrary:
        materials = self.load("material.pkl")
        return MaterialLibrary(materials)

    def save_scene(self, scene: Scene, scene_name: str = "default") -> None:
        self.save(scene, f"scene_{scene_name}.pkl")

    def load_scene(self, scene_name: str = "default") -> Scene:
        scene = self.load(f"scene_{scene_name}.pkl")
        return scene
