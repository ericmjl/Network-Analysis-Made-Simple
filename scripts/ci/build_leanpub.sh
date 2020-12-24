# Build LeanPub book
source nams/bin/activate || conda activate nams || source activate nams
jupyter nbconvert --to python scripts/bookbuilder/markua.ipynb
python scripts/bookbuilder/markua.py
