.PHONY: all clean

all: main.pdf

main.pdf: main.tex references.bib
	latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

clean:
	latexmk -C
