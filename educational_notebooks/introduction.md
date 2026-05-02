# Introduction to the notebook series

---

In this series of notebooks, we will explore ray tracing step by step, starting from the basic principles and gradually building a simple Whitted-style ray tracer.

We will begin with the fundamentals: how a camera works, how primary rays are generated, and how rays intersect objects in a scene. After that, we will move on to shading, lighting, materials, reflections, refractions, and other core parts of the rendering pipeline. Finally, we will combine these ideas into a simple ray tracer capable of rendering scenes made from mathematically defined objects and materials. The later notebooks also introduce more advanced educational topics, such as normal perturbation and procedural textures.

Some parts of the implementation are intentionally simplified and are not physically accurate. The goal of this series is not to build a production renderer, but to understand the basic ray-tracing pipeline and learn how its main components can be implemented in code.

While going through the notebooks, try to experiment with the code and modify it. Implementing your own small features, changing parameters, and testing different scenes is one of the best ways to understand the concepts. Jupyter notebooks are especially useful for this because they allow you to run, inspect, and modify individual parts of the rendering process interactively.

Some things to keep in mind:

- Python is used for the implementation, but the main concepts can be applied in other programming languages as well.
- The code in the notebooks is written mainly for clarity and educational value, not for performance. The goal is to understand how ray tracing works and how its main parts fit together, not to create a highly optimized renderer.

## Cheat sheet: how to use this library

#### Importing from the library:
- `from src import *` to import all the necessary classes and functions.
- `from src.internals import *` to import the internals

---
# Configuration Classes

### `RenderConfig`

Controls the main rendering quality and recursion settings.

| Parameter | Type | Default | Description |
|---|---|---:|---|
| `resolution` | `Resolution` | `Resolution.R360p` | Output image resolution. Can use a predefined resolution or a custom one. |
| `samples_per_pixel` | `int` | `1` | Number of samples per pixel. Higher values improve anti-aliasing and noise reduction, but increase render time. |
| `max_depth` | `int` | `5` | Maximum recursion depth for secondary rays such as reflections and refractions. |

Example:

```
RenderConfig(
    resolution=Resolution.R360p,
    samples_per_pixel=1,
    max_depth=5,
)
```

### `PreviewConfig`

Controls how rendering progress is displayed.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `progress_display` | `ProgressDisplay` | `ProgressDisplay.NONE` | Chooses the progress display mode. |
| `refresh_interval_rows` | `int` | `10` | Number of rendered rows between preview updates. |
| `fill_missing_rows` | `bool` | `True` | Fills not-yet-rendered rows in the preview. |
| `show_status` | `bool` | `True` | Shows extra rendering status information. |
| `border` | `str` | `"1px solid #ddd"` | Border style for image preview output. |

Example:

```python
PreviewConfig(
    progress_display=ProgressDisplay.TQDM_IMAGE_PREVIEW,
    refresh_interval_rows=10,
    fill_missing_rows=True,
    show_status=True,
    border="1px solid #ddd",
)
```


### `PostProcessConfig`

Controls post-processing after rendering.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `enabled` | `bool` | `False` | Enables or disables post-processing. |
| `scale_factor` | `int` | `1` | Scales the final image by the given factor. |

Example:

```python
PostProcessConfig(
    enabled=False,
    scale_factor=1,
)
```

### `ProgressDisplay`

Available progress display modes.

| Mode | Value | Description |
|---|---|---|
| `NONE` | `0` | No progress output. |
| `TQDM_CONSOLE` | `1` | Progress output in the console. |
| `TQDM_BAR` | `2` | Standard tqdm progress bar. |
| `TQDM_IMAGE_PREVIEW` | `3` | Live image preview during rendering. |

Example:

```python
preview_config=PreviewConfig(
    progress_display=ProgressDisplay.TQDM_IMAGE_PREVIEW
)
```