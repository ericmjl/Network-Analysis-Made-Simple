Network-Analysis-Made-Simple
============================

# Getting Set Up

For this tutorial, you will need the following packages:

1. Python 3
2. `matplotlib`
3. `networkx`
4. `pandas`
5. `hiveplot` - do not do `conda install hiveplot`, but `pip install hiveplot`.
6. `numpy`

## Easiest way: Anaconda Distribution of Python

If you have the Anaconda distribution of **Python 3** installed, then follow this set of instructions.

1. `$ cd /path/to/your/directory`
1. Clone the repository to disk:
    1. `$ git clone https://github.com/ericmjl/Network-Analysis-Made-Simple.git`
1. `$ cd Network-Analysis-Made-Simple`
1. `$ conda env create -f environment.yml`

Finally, check your environment by running the following command:

1. `$ python checkenv.py`

If you do not have the Anaconda distribution, I would highly recommend getting it. Check out @jakevdp's talk at SciPy2015 - it's time to switch over to Python 3!

# Dataset Credits

1. Divvy Data Challenge: https://www.divvybikes.com/datachallenge
