#!/bin/bash

echo "Building PDF ..."
pdflatex thebook.tex

echo "Building EPUB ..."
tex4ebook -m index -c thebook.cfg -e thebook.mk4 -f epub thebook.tex

echo "Building MOBI ..."
ebook-convert thebook.epub thebook.mobi
