"""
Attempt 1 (2 May 2020) at building an automatic
PDF builder for NAMS hybrid Markdown and Jupyter files
"""

import nbformat
import yaml
from pyprojroot import here

with open(here() / "mkdocs.yml", "r+") as f:
    f = "".join(l for l in f.readlines())
    mkdocs_config = yaml.safe_load(f)


nav = mkdocs_config["nav"]

docroot = here() / "docs"

for navitems in nav:
    for section, items in navitems.items():
        if isinstance(items, list):
            for item in items:
                print(item)
        else:
            print(items)


def _convert_notebook(filepath):
    """Convert notebook into a Markdown file in memory."""


def _convert_markdown():
    pass


suffix_converter = {".ipynb": _convert_notebook, ".md": _convert_markdown}


def convert_file(fname):
    suffix = fname.split(".")[-1]
    try:
        converter_func = suffix_converter[suffix]
    except KeyError:
        raise KeyError(f"{fname} has unsupported suffix `{suffix}`!")


# TODO:
# - execute Jupyter nbconvert to convert notebooks to Markdown with outputs
# - inject titles into individual Markdown files
# - concatenate Markdown files into a master file
# - generate "custom" Markdown based on inputted "name", and add signature
# - compile Markdown files into a single PDF.
