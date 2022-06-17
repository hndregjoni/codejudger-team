#! /usr/bin/bash

dir=$1
format=$2

for f in $dir/*.md; do
    fimg=${f%.md}.$format
    echo mmdc -i $f -o $fimg
    mmdc -i $f -o $fimg
done