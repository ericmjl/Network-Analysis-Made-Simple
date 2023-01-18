# Build conda environment.
conda update -n base -c defaults conda
conda install -c conda-forge mamba
mamba env create -f environment.yml
mamba activate nams || mamba activate nams
python -m pip install --no-deps .
python -m pip install .
conda list
conda install conda-pack
conda pack -n nams -o nams.tar.gz
