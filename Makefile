NBS = $(wildcard *.ipynb)
NBHTML = $(wildcard *.html)

docs: nbhtml readme

nbhtml:
	jupyter nbconvert --to html $(NBS)
	mv *.html docs/.

readme: README.md
	pandoc README.md -o docs/index.html -c gh.css
	cp custom-logo.png docs/images/custom-logo.png
