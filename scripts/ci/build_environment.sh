# Build conda environment.
conda env create -f environment.yml
source activate nams
python -m ipykernel install --user --name nams
pip install .
