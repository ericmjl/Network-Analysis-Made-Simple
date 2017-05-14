NBS = $(wildcard *.ipynb)
NBHTML = $(wildcard *.html)

all: nbhtml readme

nbhtml:
	jupyter nbconvert --to html $(NBS)
	mv *.html docs/.

readme: README.md
	pandoc README.md -o docs/index.html -c gh.css
	cp ./images/custom-logo.png ./docs/images/custom-logo.png
