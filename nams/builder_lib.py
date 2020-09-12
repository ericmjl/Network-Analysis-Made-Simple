"""
Some utility functions to help with building notebooks.

This module exists because I saw common usable functions
across both the LeanPub and MkDocs build steps.
"""
import nbformat
from nbconvert import MarkdownExporter, PDFExporter
from nbconvert.preprocessors import ExecutePreprocessor
from pyprojroot import here

import yaml
from pyprojroot import here
from typing import Dict, List
from pathlib import Path
from pyprojroot import here


def read_mkdocs() -> Dict:
    """
    Parse mkdocs.yml in project root dir.
    """
    with open(here() / "mkdocs.yml", "r+") as f:
        f = "".join(l for l in f.readlines())
        mkdocs_config = yaml.safe_load(f)
    return mkdocs_config


def parse_navigation(nav: Dict, accumulator: List) -> List:
    """
    Collect all files in mkdocs navigation
    into a list of 2-tuples
    with titles as the first element
    and file path relative to docroot as the second.

    :param nav: mkdocs navigation dictionary.
    :param accumulator: A list of accumulated navigation items.
    """
    for item in nav:
        if isinstance(item, dict):
            for k, v in item.items():
                if isinstance(v, list):
                    parse_navigation(v, accumulator)
                if isinstance(v, str):
                    accumulator.append((k.split(": ")[-1], v))
    return accumulator


def read_markdown(fpath: Path) -> str:
    """Read Markdown file as a string."""
    with open(fpath, "r+") as f:
        md = f.read()
    return md


from nbformat.notebooknode import NotebookNode


def read_notebook(fpath: Path) -> NotebookNode:
    """Read notbook as a nbformat.notebooknode.NotebookNode."""
    with open(fpath, "r+") as f:
        nb = nbformat.reads(f.read(), as_version=4)
    for cell in nb.cells:
        sanitize_image_paths(cell, fpath)
    return nb


def md2nbcell(md: str) -> NotebookNode:
    """Convert markdown to Jupyter notebook cell."""
    data = {"cell_type": "markdown", "metadata": {}, "source": md}
    cell = nbformat.NotebookNode(**data)
    return cell


def compile_code_cells(title_fpaths: List, docroot: Path, insert_titles=True) -> List:
    """
    Compile Markdown and Jupyter cells into a single collection of Jupyter cells.

    :param title_fpaths: A list of 2-tuples returned from
    """
    cells = [md2nbcell("\pagebreak")]
    for title, file in title_fpaths:
        fpath = docroot / file
        if insert_titles:
            titlecell = md2nbcell(f"# {title}")
            cells.append(titlecell)

        if file.endswith(".md"):
            md = read_markdown(fpath)
            cell = md2nbcell(md)
            cells.append(cell)
        elif file.endswith(".ipynb"):
            nb = read_notebook(fpath)
            cells.extend([c for c in nb.cells if len(c["source"]) > 0])
        cells.append(md2nbcell("\pagebreak"))
    return cells


def sanitize_image_paths(cell, fpath: Path):
    """
    Sanitize the image path by replacing it with an absolute path.

    `fpath` is a Pathlib object that contains a relative path of a notebook,
    e.g. `/path/to/nams/.../docs/advanced/bipartite.ipynb`.
    The parent/enclosing directory of fpath,
    i.e. `/path/to/nams/.../docs/advanced/` is now used as the root directory
    to replace all `./figures` with `/path/to/nams/.../docs/advanced/figures`.
    """
    nbdir = fpath.parent
    cell["source"] = cell["source"].replace("./figures", str(nbdir / "figures"))


def make_compiled_notebook(cells: List, title: str = None) -> NotebookNode:
    """Compile notebooks into a notebook"""
    metadata = {
        "kernelspec": {"display_name": "nams", "language": "python", "name": "nams"},
        "language_info": {
            "codemirror_mode": {"name": "ipython", "version": 3},
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.7.7",
        },
        "title": title,
    }

    compiled_nb = nbformat.v4.new_notebook()
    compiled_nb.metadata = metadata
    compiled_nb.cells = cells
    return compiled_nb


from typing import Tuple, Any


def strip_execution_count(nb):
    for cell in nb.cells:
        if "execution_count" in cell:
            cell["execution_count"] = None


def to_pdf(nb: NotebookNode, kernel: str, fpath: Path) -> Tuple[Any, Dict]:
    """
    Compile final notebook into a single PDF while executing it.

    :param nb: The compiled notebook object with all notebook cells.
    :param kernel: String name of the kernel to output.
    :param fpath: The path to write hte notebook to.
    """
    ep = ExecutePreprocessor(timeout=600, kernel_name=kernel)
    ep.preprocess(nb)

    strip_execution_count(nb)
    pdf_exporter = PDFExporter()
    body, resources = pdf_exporter.from_notebook_node(nb)

    with open(fpath, "wb") as f:
        f.write(body)


from typing import Optional, List


def exclude(title_files: List, titles: List = [], files: List = []):
    """
    Exclude both titles and files from the title_files list.

    Assumes that titles are index 0,
    and files are index 1,
    in each of the tuples in title_files.

    Only exact matches are used.
    """
    filtered = []
    for title, fname in title_files:
        if title in titles or fname in files:
            continue
        filtered.append((title, fname))
    return filtered


def insert_binder_cell(
    nb_relpath: Path, docroot: Path, nb: NotebookNode
) -> NotebookNode:
    """
    Insert a Markdown with Binder link.

    This inserts a Markdown cell at the top of the notebook
    that allows a student to directly open _that_ notebook
    inside Binder (without needing to navigate to it).

    Returns a NotebookNode object,
    which is the `nbformat` representation of a Jupyter notebook.

    :param nb_relpath: The relative path to the notebook,
        where the docroot is the root directory of the docs.
    :param docroot: The docs directory, relative to the project root.
    :param nb: The notebook for which a binder link
        is supposed to be added into.
    """
    badge_url = f"[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ericmjl/Network-Analysis-Made-Simple/master?filepath=docs%2F{nb_relpath.parent.name}%2F{nb_relpath.name})"
    nb_path = docroot / nb_relpath
    nb["cells"].insert(0, nbformat.v4.new_markdown_cell(source=badge_url))
    return nb


def insert_binder_link(nb_relpath, docroot):
    """
    Insert a binder link into a given notebook.

    This function is one level of abstraction above insert_binder_cell.

    :param nb_relpath: The relative path to the notebook,
        where the docroot is the root directory of the docs.
    :param docroot: The docs directory, relative to the project root.
    """
    nb_path = docroot / nb_relpath
    nb = read_notebook(nb_path)
    nb = insert_binder_cell(nb_relpath, docroot, nb)
    nbformat.write(nb, docroot / nb_relpath)


def remove_binder_cell(nb: NotebookNode) -> NotebookNode:
    """
    Remove cell that contains Binder link.
    """
    new_cells = []
    for cell in nb["cells"]:
        if not "https://mybinder.org/badge_logo.svg" in cell.source:
            new_cells.append(cell)
    nb["cells"] = new_cells
    return nb


def remove_binder_link(nb_relpath: Path, docroot: Path) -> None:
    """Remove a binder link from a given notebook at the nb_relpath."""
    nb_path = docroot / nb_relpath
    nb = read_notebook(nb_path)
    nb = remove_binder_cell(nb)
    nbformat.write(nb, docroot / nb_relpath)
