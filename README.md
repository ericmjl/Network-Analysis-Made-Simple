Network-Analysis-Made-Simple
============================

![](images/custom-logo.png)

# Getting Set Up

For this tutorial, you will need the following packages:

1. Python 3
2. `matplotlib`
3. `networkx`
4. `pandas`
5. `hiveplot` - do not do `conda install hiveplot`, but `pip install hiveplot`.
6. `circos` - install using `pip install circos`
6. `numpy`
7. `scipy`

## Clone the repository

1. `$ cd /path/to/your/directory`
1. Clone the repository to disk:
    1. `$ git clone https://github.com/ericmjl/Network-Analysis-Made-Simple.git`
1. `$ cd Network-Analysis-Made-Simple`

## Easiest way: Anaconda Distribution of Python

If you have the Anaconda distribution of **Python 3** installed, then run `bash conda-setup.sh`, which wraps the commands below.

1. `$ conda env create -f environment.yml`
1. `$ source activate network`

Check your environment by running the following command:

1. `$ python checkenv.py`

If you do not have the Anaconda distribution, I would highly recommend getting it for [Windows][2], [Mac][3] or [Linux][4]. It provides an isolated Python computing environment that will not interfere with your system Python installation, and comes with a very awesome package manager (`conda`) that makes installation of new packages a single `conda install pkgname` away.

If you're not using Python 3, then check out @jakevdp's talk at SciPy2015 to find out why!

## Alternative to Anaconda: `pip install`

For those who do not have the capability of installing the Anaconda Python 3 distribution on their computers, please follow the instructions below.

Run `bash venv-setup.sh`, which wraps up the commands below. Special thanks to @matt-land for putting this script together.

1. Create a virtual environment for this tutorial, so that the installed packages do not mess with your regular Python environment.
    2. `$ pip install virtualenv`
    3. `$ virtualenv network`
    4. `$ source network/bin/activate`
5. `$ pip install matplotlib networkx pandas hiveplot numpy jupyter`

Check your environment:

1. `$ python checkenv.py`

## Run the Jupyter Notebook

    $ jupyter notebook

Your browser will open to an index page where you can click on a notebook to run it.

# Feedback

If you've attended this workshop, please leave [feedback][7]!.

# Issues

## Known Issues

If you get a "Python is not installed as a framework" error with matplotlib, please check out [this issue][8] for instructions to resolve it.

## New Issues

If you're facing difficulties, please report it as an [issue][1] on this repository.

# Credits

1. Divvy Data Challenge: https://www.divvybikes.com/datachallenge

# Resources

1. Jon Charest's use of Circos plots to visualize networks of Metal music genres. [blog post][5] | [notebook][6]

# People

Many thanks to the following users who have contributed to improving the content and finding bugs.

1. @jzab
2. @muthazhagu
3. @ghirlekar
4. @jamesbev
5. @romanchyla
1. @jonchar
2. @remik
2. @matt-land
3. @smacleod
4. @RyPeck
5. @zmilicc

[1]: https://github.com/ericmjl/Network-Analysis-Made-Simple/issues
[2]: http://repo.continuum.io/archive/Anaconda3-4.0.0-Windows-x86_64.exe
[3]: http://repo.continuum.io/archive/Anaconda3-4.0.0-MacOSX-x86_64.pkg
[4]: http://repo.continuum.io/archive/Anaconda3-4.0.0-Linux-x86_64.sh
[5]: http://jonchar.net/2016/05/20/exploring-metal-subgenres-with-python.html
[6]: http://jonchar.net/notebooks/MA-Exploratory-Analysis#Enter-the-Circos-plot
[7]: https://ericma1.typeform.com/to/aCljQl
[8]: https://github.com/ericmjl/Network-Analysis-Made-Simple/issues/8