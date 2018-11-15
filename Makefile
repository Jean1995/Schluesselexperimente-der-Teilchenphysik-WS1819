make all:
	lualatex summary.tex
	bibtex summary
	lualatex summary.tex
	lualatex summary.tex

clean:
	-rm summary.pdf
	-rm summary.aux
	-rm summary.bbl
	-rm summary.blg
	-rm summary.log
	-rm summary.toc