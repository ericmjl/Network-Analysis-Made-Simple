# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo",
# ]
# ///

import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Introduction

    In order to get the most of this book,
    you will want to be able to execute the examples in the notebooks,
    modify them, break the code, and fix it.
    Pedagogically, that is the best way for you to learn the concepts.
    Here's the recommended way to get set up.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Quick Setup

    To get started with the notebooks, follow these simple steps:

    1. Git clone the repository: https://github.com/ericmjl/Network-Analysis-Made-Simple

    1. **Install uv** (the Python package manager):
       Follow the installation instructions at [https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/)

    2. **Navigate to the notebook directory**:
       ```bash
       cd notebooks/00-preface/ # replace with the actual numbered subdir!
       ```

    3. **Run the notebook**:
       ```bash
       uvx marimo edit --sandbox 01-setup.py
       ```

    Once Marimo is launched, on the bottom, click on "on startup", "on cel change", and "on module change" to disable automatic execution. This will allow us to mimic original Jupyter behaviour, which is advantageous for a teaching setting (but toggle them back to "autorun" )

 
    That's it! The `--sandbox` flag ensures a clean, isolated environment for running the notebooks with all necessary dependencies automatically managed.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## What this does

    - **uv** is a fast Python package manager that handles dependency resolution and virtual environments
    - **marimo** is an interactive notebook environment optimized for Python
    - The `--sandbox` flag creates an isolated environment for each notebook, preventing dependency conflicts
    - All required packages are automatically installed when you run the notebook

    This approach eliminates the need for manual environment setup, conda environments, or Docker containers while ensuring reproducible execution of the tutorial content.
    """
    )
    return


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
