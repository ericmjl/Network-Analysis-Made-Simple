from nams.builder_lib import read_mkdocs
from pyprojroot import here
from nams.builder_lib import parse_navigation
from nams.builder_lib import (
    read_notebook,
    insert_binder_link,
    remove_binder_cell,
    remove_binder_link,
)
from pathlib import Path


config = read_mkdocs()
nav = config["nav"]
docroot = here() / "docs"

nb_relpaths = [
    Path(i[1]) for i in parse_navigation(nav, accumulator=[]) if i[1].endswith(".ipynb")
]


for nb_relpath in nb_relpaths:
    remove_binder_link(nb_relpath, docroot)
