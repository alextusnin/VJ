all: 
	@echo "python VJ.py $(Vol)"
	python VJ.py $(Vol)
	@echo "pdflatex VJ_$(Vol).tex"
	pdflatex VJ_$(Vol).tex
	rm -rf *.aux *.bbl *.blg *.glg *.glo *.gls *.idx  *.ilg *.ind *.ist *.log *.out *.toc *.backup *.xml *.bcf *.lot *.lof *.tex

clean:
	rm -rf *.aux *.bbl *.blg *.glg *.glo *.gls *.idx  *.ilg *.ind *.ist *.log *.out *.toc *.backup *.xml *.bcf *.lot *.lof *.tex
	
