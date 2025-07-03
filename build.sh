#!/bin/bash

echo "Building PDF ..."
pdflatex thebook.tex || exit $?
pdflatex thebook.tex || exit $?
makeindex thebook.idx || exit $?
pdflatex thebook.tex || exit $?

echo "Building EPUB ..."
tex4ebook -m index -c thebook.cfg -e thebook.mk4 -f epub thebook.tex || exit $?

echo "Building MOBI ..."
ebook-convert thebook.epub thebook.mobi || exit $?
