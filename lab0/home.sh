#!/usr/bin/bash

dir="/home/$USER/hello home"
filename="$dir/home.txt"
mkdir "$dir" -p
echo "hello world!!" > "$filename"
cat "$filename"
ls "$filename" -l