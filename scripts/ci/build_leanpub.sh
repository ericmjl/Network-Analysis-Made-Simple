# Build LeanPub files
source activate nams
jupyter nbconvert --to python scripts/bookbuilder/markua.ipynb
python scripts/bookbuilder/markua.py
