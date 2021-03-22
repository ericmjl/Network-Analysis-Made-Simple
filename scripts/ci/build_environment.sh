# Build conda environment.
conda install -c conda-forge mamba
conda env create -f environment.yml
conda activate nams || source activate nams
python -m pip install --no-deps git+https://github.com/greenape/mknotebooks.git
python -m pip install --no-deps .
python -m pip install .
conda install conda-pack
conda pack -n nams -o nams.tar.gz
