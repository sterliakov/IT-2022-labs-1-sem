#!/usr/bin/bash

dir="/tmp/hello world"
filename="$dir/absolute.txt"
mkdir "$dir" -p
echo "hello world!!" > "$filename"
cat "$filename"
ls "$filename" -l