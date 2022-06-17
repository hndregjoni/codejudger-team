#! /usr/bin/bash

dir=$1
format=$2

for f in $dir/*.svg; do
    fimg=${f%.svg}.$format
    echo convert$f $fimg
    convert $f $fimg
done