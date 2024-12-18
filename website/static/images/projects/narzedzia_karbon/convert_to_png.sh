#!/bin/bash

for file in ./*.jpg; do
    if [[ ! -e "$file" ]]; then
        break 
    fi
    base_name=$(basename "$file" .jpg)
    
    output_file="./$base_name.png"
    echo "Converting $file -> $output_file"
    convert "$file" "$output_file"
    rm "$file"
done

for file in ./*.jpeg; do
    if [[ ! -e "$file" ]]; then
        break 
    fi
    base_name=$(basename "$file" .jpeg)
    
    output_file="./$base_name.png"
    echo "Converting $file -> $output_file"
    convert "$file" "$output_file"
    rm "$file"
done

for file in ./*.gif; do
    if [[ ! -e "$file" ]]; then
        break 
    fi
    base_name=$(basename "$file" .gif)
    
    output_file="./$base_name.png"
    echo "Converting $file -> $output_file"
    convert "$file" "$output_file"
    rm "$file"
done

for file in ./*.bmp; do
    if [[ ! -e "$file" ]]; then
	break
    fi
    base_name=$(basename "$file" .bmp)
    
    output_file="./$base_name.png"
    echo "Converting $file -> $output_file"
    convert "$file" "$output_file"
    rm "$file"
done
