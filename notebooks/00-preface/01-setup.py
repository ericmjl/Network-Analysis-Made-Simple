import marimo

__generated_with = "0.23.9"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Introduction

    In order to get the most of this book,
    you will want to be able to execute the examples in the notebooks,
    modify them, break the code, and fix it.
    Pedagogically, that is the best way for you to learn the concepts.
    Here's the recommended way to get set up.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Quick Setup

    To get started with the notebooks, follow these simple steps:

    1. Git clone the repository: https://github.com/ericmjl/Network-Analysis-Made-Simple

    2. **Install pixi** (the package manager):
       Follow the installation instructions at [https://pixi.sh](https://pixi.sh)

    3. **Run the notebooks**:
       ```bash
       pixi run marimo edit --no-token notebooks/
       ```

    Once Marimo is launched, on the bottom, click on "on startup", "on cell change", and "on module change" to disable automatic execution. This will allow us to mimic original Jupyter behaviour, which is advantageous for a teaching setting (but toggle them back to "autorun" when you're done with the tutorial).

    That's it! Pixi ensures a clean, isolated environment for running the notebooks with all necessary dependencies automatically managed.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## What this does

    - **pixi** is a fast package manager that handles dependency resolution and environments
    - **marimo** is an interactive notebook environment optimized for Python
    - All required packages are automatically installed via the pixi manifest
    - No manual environment setup, conda environments, or Docker containers needed

    This approach ensures reproducible execution of the tutorial content.
    """)
    return


if __name__ == "__main__":
    app.run()
