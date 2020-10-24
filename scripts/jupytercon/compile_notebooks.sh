# To comply with JupyterCon requirements, here's a bash script
# that generates a directory under /tmp
# with all of the contents that are structured according to the platform's requirements.

export WORKDIR="/tmp/jupytercon/notebooks"
mkdir -p $WORKDIR
cp notebooks/01-introduction/01-graphs.ipynb $WORKDIR/01-graphs.ipynb
cp notebooks/01-introduction/02-networkx-intro.ipynb $WORKDIR/02-networkx-intro.ipynb
cp notebooks/01-introduction/03-viz.ipynb $WORKDIR/03-viz.ipynb
cp notebooks/02-algorithms/01-hubs.ipynb $WORKDIR/04-hubs.ipynb
cp notebooks/02-algorithms/02-paths.ipynb $WORKDIR/05-paths.ipynb
cp notebooks/02-algorithms/03-structures.ipynb $WORKDIR/06-structures.ipynb
cp notebooks/03-practical/01-io.ipynb $WORKDIR/07-io.ipynb
cp notebooks/03-practical/02-testing.ipynb $WORKDIR/08-testing.ipynb
cp notebooks/04-advanced/01-bipartite.ipynb $WORKDIR/09-bipartite.ipynb
cp notebooks/04-advanced/02-linalg.ipynb $WORKDIR/10-linalg.ipynb
cp notebooks/04-advanced/03-stats.ipynb $WORKDIR/11-stats.ipynb

export WORKDIR="/tmp/jupytercon"
cp -r nams $WORKDIR/.
cp setup.py $WORKDIR/.
cp requirements.txt $WORKDIR/.
cp README.md $WORKDIR/.
cp -r data $WORKDIR/.
