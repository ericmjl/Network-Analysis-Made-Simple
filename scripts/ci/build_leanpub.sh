# Build LeanPub book
source nams_env/bin/activate || conda activate nams || source activate nams
echo `which python`  # debugging statement
python -m ipykernel install --user --name nams
jupyter nbconvert --to python scripts/bookbuilder/markua.ipynb
python scripts/bookbuilder/markua.py
