.PHONY: all arxiv clean

all: main.pdf

main.pdf: main.tex references.bib
	latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

arxiv: main.pdf
	python3 scripts/package-arxiv.py

clean:
	latexmk -C
