# Build conda environment.
conda install -c conda-forge mamba
mamba env create -f environment.yml
source activate nams
pip install --no-deps mknotebooks
pip install --no-deps .
python -m ipykernel install --user --name nams
pip install .
conda install conda-pack
conda pack -n nams -o nams.tar.gz
