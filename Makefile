make all:
	lualatex summary.tex
	bibtex summary
	lualatex summary.tex
	lualatex summary.tex
