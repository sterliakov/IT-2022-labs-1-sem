#!/usr/bin/bash

dir="./hello current"
filename="$dir/current.txt"
mkdir "$dir" -p
echo "hello world!!" > "$filename"
cat "$filename"
ls "$filename" -l