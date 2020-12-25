# Build MkDocs website
source nams_env/bin/activate || conda activate nams || source activate nams
echo `which python`  # debugging statement
python -m ipykernel install --user --name nams
mkdocs build
