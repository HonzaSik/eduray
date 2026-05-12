from dataclasses import dataclass


@dataclass
class PostProcessConfig:
    """
    Configuration for post-processing effects.
    """
    enabled: bool = False
    scale_factor: int = 1
