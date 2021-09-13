#!/usr/bin/bash

declare -a files=("absolute.sh" "home.sh" "current.sh" "parent.sh")
chmod +x $files

echo -e "Script sources:"
for f in "${files[@]}"
do
	echo -e "# $f"
	cat "./$f"
	echo -e "\n"
done
echo -e "\n"

for it in {1,2}
do
	echo -e "\nIteration: $it"
	for f in "${files[@]}"
	do
		./$f
	done
done

while getopts "c" opt; do
	case "$opt" in
	    c)
			echo -e "\nCleanup"
			rm -r "./hello current" "../hello parent" "/tmp/hello world" "/home/$USER/hello home"
	      	;;
	esac
done