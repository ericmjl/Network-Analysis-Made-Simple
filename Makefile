NBS = $(wildcard *instructor.ipynb)
NBHTML = $(wildcard *.html)

all: clean nbhtml readme

nbhtml:
	jupyter nbconvert --to html --ExecutePreprocessor.timeout=600 --ExecutePreprocessor.kernel_name="nams" --execute $(NBS) 1-introduction.ipynb bonus-2-one-more-thing.ipynb
	jupyter nbconvert --to html --ExecutePreprocessor.kernel_name="nams"  0-pre-tutorial-exercises.ipynb
	mv *.html docs/.

readme: README.md
	pandoc README.md -o docs/index.html -c gh.css
	cp ./images/custom-logo.png ./docs/images/custom-logo.png

clean:
	rm docs/*.html

conda:
	set -ex
	conda env create -f environment.yml
	source activate nams
	python checkenv.py

updateconda:
	conda env update -f environment.yml

venv:
	set -x
	VENV="$(which virtualenv)"
	if [ -z "$VENV" ]; then
	   pip install virtualenv
	fi
	if [[ -d 'network' ]]; then
	   rm -rf ./network
	   echo 'xx';
	fi
	virtualenv network
	source network/bin/activate && pip install -r requirements.txt
	echo "Run 'source network/bin/activate' to begin"

	python checkenv.py
