#!/usr/bin/env python
# coding: utf-8

# # An attempt at writing a script that can convert every specified file to markua for publication on Leanpub

# In[1]:


from lib import read_mkdocs


# In[2]:


from pyprojroot import here


# In[3]:


mkdocs_config = read_mkdocs()
nav = mkdocs_config["nav"]
docroot = here() / "docs"


# In[4]:


from lib import parse_navigation

# The goal here is to flatten the tree structure into a list of 2-tuples,
# where the title is the first element and the filename is the second element.
title_files = parse_navigation(nav, [])
title_files.insert(0, ("Preface", "preface/preface.md"))
title_files


# In[5]:


from lib import exclude

exclusion = ["Welcome", "Get Setup", "Prerequisites", "Further Learning", "Style Guide"]

title_files = exclude(title_files, titles=exclusion)


# In[6]:


title_files


# We now need to convert each of the files into Markua.

# In[7]:


from nbconvert.exporters import MarkdownExporter
from nbformat.notebooknode import NotebookNode
from nbconvert.preprocessors import ExecutePreprocessor
from lib import strip_execution_count


def nb2markdown(nb: NotebookNode, kernel: str):
    """
    Compile final notebook into a single PDF while executing it.

    :param nb: The compiled notebook object with all notebook cells.
    :param kernel: String name of the kernel to output.
    :param fpath: The path to write hte notebook to.
    """
    ep = ExecutePreprocessor(timeout=600, kernel_name=kernel)
    ep.preprocess(nb)

    strip_execution_count(nb)
    pdf_exporter = MarkdownExporter()
    body, resources = pdf_exporter.from_notebook_node(nb)
    return body, resources


# In[8]:


from lib import read_notebook


# In[10]:


sample_chapters = [
    "Preface",
    "Learning Goals",
    "Introduction to Graphs",
    "The NetworkX API",
]


# In[11]:


# Now, convert everything into plain text markdown.


# In[12]:


from pathlib import Path
from pyprojroot import here

build_dir = here() / "manuscript"
build_dir.mkdir(parents=True, exist_ok=True)

resources_dir = build_dir / "resources"
resources_dir.mkdir(parents=True, exist_ok=True)


# In[13]:


for chapter, fpath in title_files:
    fpath = Path(fpath)
    source_path = docroot / fpath
    # Handle notebooks
    if source_path.suffix == ".ipynb":
        text, resources = nb2markdown(read_notebook(source_path), kernel="nams")
    # Handle markdown files
    else:
        with open(source_path, "r+") as f:
            text = f.read()
        resources = dict()
        resources["outputs"] = dict()

    print(source_path)
    if chapter in sample_chapters:
        insert = "{sample: true}\n\n"
        text = insert + text

    markdown_dir = (build_dir / fpath).with_suffix(".md")
    markdown_dir.mkdir(parents=True, exist_ok=True)
    print(markdown_dir)

    images_dir = (resources_dir / fpath).with_suffix(".md")
    images_dir.mkdir(parents=True, exist_ok=True)
    print(images_dir)

    # Write the text out
    with open(markdown_dir / "index.md", "w+") as f:
        f.write(text)

    # Write the resources out
    for k, v in resources["outputs"].items():
        with open(images_dir / k, "wb") as f:
            f.write(v)


# In[ ]:
