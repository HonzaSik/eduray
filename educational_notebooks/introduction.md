# Introduction to the notebook series

---

In this series of notebooks, we will explore ray tracing step by step, starting from the basic principles and gradually building a simple Whitted-style ray tracer.

We will begin with the fundamentals: how a camera works, how primary rays are generated, and how rays intersect objects in a scene. After that, we will move on to shading, lighting, materials, reflections, refractions, and other core parts of the rendering pipeline. Finally, we will combine these ideas into a simple ray tracer capable of rendering scenes made from mathematically defined objects and materials. The later notebooks also introduce more advanced educational topics, such as normal perturbation and procedural textures.

Some parts of the implementation are intentionally simplified and are not physically accurate. The goal of this series is not to build a production renderer, but to understand the basic ray-tracing pipeline and learn how its main components can be implemented in code.

While going through the notebooks, try to experiment with the code and modify it. Implementing your own small features, changing parameters, and testing different scenes is one of the best ways to understand the concepts. Jupyter notebooks are especially useful for this because they allow you to run, inspect, and modify individual parts of the rendering process interactively.

Some things to keep in mind:

- The code in the notebooks is written mainly for clarity and educational value, not for performance. The goal is to understand how ray tracing works and how its main parts fit together, not to create a highly optimized rendering software.


## Notebooks in this series

1. **Data and visualizer** — color, image, coordinate system
2. **Camera and render loop** — pinhole camera, ray generation, render loops, progress display
3. **Intersections and geometry** — sphere, plane, transformations, implicit surfaces, object definitions
4. **Materials, shaders and lights** —  Phong, Blinn–Phong, ambient/diffuse/specular components, lights
5. **Integrators - recursion, refraction, reflection** — Whitted-style ray tracing, Fresnel, Snell's law, recursive ray tracing
6. **Noise and procedural textures** — Perlin, fBM, turbulence, normal perturbation, procedural patterns
7. **Final scene** — Sandbox scene with various objects, materials, and lights for further experimentation and starting point for experiments and using the library as render software.
8. **Bonus: Other** — In folder other are notebooks showcasing some additional features like post processing and video rendering using EduRay.

Notebooks build on each other and are intended to be read in order.

---
## Cheat sheet: how to use this library

#### Importing from the library:
- `from eduray import` to import classes and functions from the main API
- `from eduray.internals import` to import the internal classes and functions, which are not part of the public API but are used in the notebooks for educational purposes and visualisation.


> Note: The main documentation of EduRay is provided through the educational Jupyter notebooks. These notebooks introduce the library step by step and show how its classes, methods, and rendering components are used in practice. This is intentional: many parts of the library are easiest to understand when they are shown directly in context, together with small scenes, visualizations, and experiments. The final demo notebook is intended as a practical sandbox for users who want to create their own scenes and experiments.
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