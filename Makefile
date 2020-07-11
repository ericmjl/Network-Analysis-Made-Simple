NBS = $(wildcard *instructor.ipynb)
NBHTML = $(wildcard *.html)

.PHONY = serve

all: clean nbhtml readme


readme: README.md
	pandoc README.md -o docs/index.html -c gh.css
	cp ./images/custom-logo.png ./docs/images/custom-logo.png

conda:
	set -ex
	conda env create -f environment.yml
	conda activate nams
    python setup.py develop
	python checkenv.py

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
    python setup.py develop
	python checkenv.py

check:
	python checkenv.py

docs:
	mkdocs build

serve:
	mkdocs build
	python -m http.server 8149 -d site/

format:
	isort -rc -y .
	black -l 79 .
