# Download Miniconda and install it
# wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh;
# bash miniconda.sh -b -p $HOME/miniconda

# # Configure miniconda
# export PATH="$HOME/miniconda/bin:$PATH"
# conda config --set always_yes yes --set changeps1 no
# conda config --add channels conda-forge

# Create environment
conda install -c conda-forge mamba conda-pack
mamba env create -f environment.yml
source activate nams
python -m ipykernel install --user --name nams
pip install .

# Pack up environment
# conda pack -n nams -o /tmp/nams.tar.gz
