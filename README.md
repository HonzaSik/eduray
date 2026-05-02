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

EduRay is an educational ray tracer implemented in Python. It is designed to be simple, readable, and modular, making it suitable for learning the fundamentals of ray tracing and computer graphics.

The project focuses on clarity rather than performance. It includes the source code of the ray tracer, visualization tools, example scenes, and educational Jupyter notebooks.

### Jupyter Notebooks

A series of educational Jupyter notebooks is available in the `educational_notebooks` directory.

The notebooks explain selected ray tracing concepts step by step, including:

- camera construction
- ray-object intersections
- shading
- rendering
- reflections and refractions
- procedural texturing
- visualization of ray tracing concepts

---
### Installation

You can install the package from PyPI without the notebooks:

```bash
pip install eduray
```

Or clone the repository to use the educational notebooks and install the package in editable mode:

```bash
git clone https://github.com/HonzaSik/eduray.git
cd eduray
python3 -m venv .venv

# macOS/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate

pip install -e .
```

To run the educational notebooks, you can either install Jupyter and launch it from the terminal:

```bash
pip install jupyter
jupyter notebook
```

Or open the notebooks directly in an IDE with Jupyter support, such as VS Code or PyCharm.

Then open `educational_notebooks/01_data_visualizer.ipynb` to start with the first lesson. The notebooks are numbered and meant to be followed in order.

> **Note**
> The project requires Python 3.13 or newer.