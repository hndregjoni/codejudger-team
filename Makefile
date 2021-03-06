# A makefile to build parts of the documentation

.PHONY: reqs_clean

#
# Requirement document:
#

REQ_DIR=./requirement_document
REQ_NAME=document.pdf
REQ_PDF=$(REQ_DIR)/$(REQ_NAME)

ROOT_DIR=$(shell pwd)

TEX=latexmk -interaction=nonstopmode -pdf -shell-escape

reqs: $(REQ_PDF)
reqs_clean:
	rm -rf $(REQ_DIR)/src/build/*
	rm $(REQ_PDF)

$(REQ_PDF): $(REQ_DIR)/src/document.tex
	mkdir -p $(REQ_DIR)/src/build

	cd $(REQ_DIR)/src && \
		$(TEX) -output-directory=build/ document.tex

	@mv $(REQ_DIR)/src/build/document.pdf $(REQ_PDF)

$(REQ_DIR)/src/build:
	@mkdir $(REQ_DIR)/src/build