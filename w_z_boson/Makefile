make all:
	lualatex template.tex
	bibtex template
	lualatex template.tex
	lualatex template.tex

clean:
	-rm template.pdf
	-rm template.aux
	-rm template.bbl
	-rm template.blg
	-rm template.log
	-rm template.toc