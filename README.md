<h1 align="center">EduRay: Educational Ray Tracer in Python</h1>

<p align="center">
  <a href="https://github.com/HonzaSik/eduray/commits/main">
    <img src="https://img.shields.io/github/last-commit/HonzaSik/eduray?logo=github" alt="Last Commit">
  </a>
  <a href="https://github.com/HonzaSik/eduray/issues">
    <img src="https://img.shields.io/github/issues/HonzaSik/eduray?logo=github" alt="Open Issues">
  </a>
  <a href="https://github.com/HonzaSik/eduray/pulls">
    <img src="https://img.shields.io/github/issues-pr/HonzaSik/eduray?logo=github" alt="Open PRs">
  </a>
  <a href="./LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green.svg?logo=open-source-initiative" alt="MIT License">
  </a>
</p>

<p align="center">
  <a href="https://pypi.org/project/eduray/">
    <img src="https://img.shields.io/pypi/v/eduray?label=PyPI&color=blue" alt="PyPI package">
  </a>
  <a href="https://github.com/HonzaSik/eduray/stargazers">
    <img src="https://img.shields.io/github/stars/HonzaSik/eduray?logo=github" alt="GitHub Stars">
  </a>
  <a href="https://github.com/HonzaSik/eduray/network/members">
    <img src="https://img.shields.io/github/forks/HonzaSik/eduray?logo=github" alt="GitHub Forks">
  </a>
</p>

---
<p align="center">
  <img src="examples/demo_scene.png" alt="Scene" width="600">
</p>

> *Rendered image of the demo scene included in the educational notebooks series.*
---

EduRay is an educational ray tracer implemented in Python. It is designed to be simple, readable, and modular, making it suitable for learning the fundamentals of ray tracing and computer graphics.

The project focuses on clarity rather than performance. It includes the source code of the ray tracer, visualization tools, example scenes, and educational Jupyter notebooks.

---
# Installation and setup

You can install the package from PyPI without the notebooks as rendering and visualization software:

```bash
pip install eduray
```

Or clone the repository to use the educational notebooks and install the package in editable mode:

```bash
git clone https://github.com/HonzaSik/eduray.git
cd eduray
python3.13 -m venv .venv

# macOS/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate

# Option A: Library only — for use in IDEs like PyCharm or VS Code
pip install -e .
# You need to set your interpreter to the virtual environment you just created for the editable install to work in your IDE.

# Option B: Library + Jupyter — for running educational notebooks in the browser
pip install -e ".[all]"
```

To run the educational notebooks in your browser, start a Jupyter server in the project directory:

```bash
jupyter notebook
```

Or open the notebooks directly in an IDE with Jupyter support, such as VS Code or PyCharm.

Then open `educational_notebooks/1_data_visualizer.ipynb` to start with the first lesson. The notebooks are numbered and meant to be followed in order.

> **Note**
> The project was developed and tested on Python 3.13. Requires Python 3.11 or newer.

---

# Quick start

The smallest working example:

```python
from eduray import Object, Sphere, PhongMaterial, Scene, PinholeCamera, PointLight, LinearRenderLoop

sphere = Object(
    geometry=Sphere(),
    material=PhongMaterial()
).translate(0, 0, -5)

scene = Scene(
    camera=PinholeCamera(),
    objects=[sphere],
    lights=[PointLight()],
)

rt = LinearRenderLoop(scene=scene)
rt.render("hello_world.png")
```

To try the library, open the [Hello World](hello_world.ipynb) notebook. It demonstrates how to set up a minimal scene and render an image using only a few lines of code.

```bash
jupyter notebook ./hello_world.ipynb
```

---
# Educational notebooks series

A series of educational Jupyter notebooks is available in the `educational_notebooks` directory.

The notebooks explain selected ray tracing concepts step by step, including:

- camera construction
- ray-object intersections
- shading
- rendering
- reflections and refractions
- procedural texturing
- visualization of ray tracing concepts

More detailed description of the notebooks can be found in the [introduction notebook](educational_notebooks/introduction.md).

---

## For those who want to experiment

1. Click "Fork" on https://github.com/HonzaSik/eduray
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/eduray.git
   ```
3. Continue with the editable install steps from the [Installation](#installation-and-setup) section above.

---

## Troubleshooting

**`ModuleNotFoundError: No module named 'eduray'` in PyCharm or VS Code**

Make sure your IDE is configured to use the `.venv` you created above,
not the system Python:

- **PyCharm**: `Settings → Project → Python Interpreter → Add Interpreter
  → Add Local → Virtualenv → Existing`, then select
  `<repo>/.venv/bin/python` (macOS/Linux) or `<repo>\.venv\Scripts\python.exe` (Windows).
- **VS Code**: `Cmd/Ctrl+Shift+P → Python: Select Interpreter`, pick the
  `.venv` from this project (workspace).