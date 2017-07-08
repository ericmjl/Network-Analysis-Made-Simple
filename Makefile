NBS = $(wildcard *instructor.ipynb)
NBHTML = $(wildcard *.html)

all: clean nbhtml readme

nbhtml:
	jupyter nbconvert --to html $(NBS) 0-pre-tutorial-exercises.ipynb 1-introduction.ipynb bonus-2-one-more-thing.ipynb
	mv *.html docs/.

readme: README.md
	pandoc README.md -o docs/index.html -c gh.css
	cp ./images/custom-logo.png ./docs/images/custom-logo.png

clean:
	rm docs/*.html
