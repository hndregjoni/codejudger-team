#! /usr/bin/bash

for f in usecases/*.md; do
    short=`basename $f`
    tex_f=${short%.md}.tex

    echo "Doing $short"
    [[ $short == "_boilerplate.md" ]] && continue
    # [ -s $f ] && continue

    ./scripts/latexUC.py $f > ./requirement_document/src/sections/04_usecases/$tex_f
    echo Saved to $tex_f
done