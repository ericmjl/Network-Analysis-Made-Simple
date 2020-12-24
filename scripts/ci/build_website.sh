# Build MkDocs website
source nams_env/bin/activate || conda activate nams || source activate nams
python -m ipykernel install --user --name nams
mkdocs build
