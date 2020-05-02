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


def _convert_notebook():
    pass


def _convert_markdown():
    pass


suffix_converter = {".ipynb": _convert_notebook, ".md": _convert_markdown}


def convert_file(fname):
    suffix = fname.split(".")[-1]
    try:
        converter_func = suffix_converter[suffix]
    except KeyError:
        raise KeyError(f"{fname} has unsupported suffix `{suffix}`!")


convert_file("hello.world")
