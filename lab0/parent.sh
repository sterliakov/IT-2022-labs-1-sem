#!/usr/bin/bash

dir="../hello parent"
filename="$dir/parent.txt"
mkdir "$dir" -p
echo "hello world!!" > "$filename"
cat "$filename"
ls "$filename" -l