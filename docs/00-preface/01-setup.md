## Introduction

In order to get the most of this book,
you will want to be able to execute the examples in the notebooks,
modify them,
break the code,
and fix it.
Pedagogically, that is the best way for you to learn the concepts.
Here are the recommended ways in which you can get set up.

## Binder

We recommend the use of Binder!
This is because Binder will automagically setup
an isolated and ephemeral compute environment for you
with all of the packages needed to run the code in your notebooks.
As such, you won't have to wrestle with anything at the terminal.
To go there, click on the following button:

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/ericmjl/Network-Analysis-Made-Simple/master)

Once you're in there, do a final setup step,
by opening up a terminal in the Jupyter session,
and installing the custom package `nams` that we wrote,
which contains data loaders and solutions.

```bash
# In the root directory of the repository
python setup.py develop
```

## `conda` environments

We also recommend the use of `conda` environments!
If you are feeling confident enough to set up a conda environment at the terminal,
then follow along.
(We'll be assuming you've already cloned the repository locally.)

### Leverage the Makefile

We've provided a Makefile with a single command:

```bash
make conda
```

On most \*nix systems, that should get you most of the way
to having the environment setup.

### Alternative: Execute individual commands

If you encounter errors, then you should know that the Makefile command
`make conda`
basically wraps the following steps.

Firstly, it creates the conda environment based on the `environment.yml` file:

```bash
conda env create -f environment.yml
```

Next, it activates the environment:

```bash
conda activate nams
```

We have a custom module for the project, which is called `nams`,
that you will have to install.

```bash
# In the root directory of the cloned repository
python setup.py develop
```

Finally, it runs a check on the environment
to make sure everything is installed correctly:

```bash
python checkenv.py
```

## `venv` environments

If you're not a `conda` user, then you can use `venv` to create your environment.


### Leverage the Makefile

As with the `conda` commands, you should be able
to execute a single Makefile command at your terminal:

```bash
make venv
```

Special heartfelt thanks goes out to GitHub user @matt-land
who contributed the `venv` script.
