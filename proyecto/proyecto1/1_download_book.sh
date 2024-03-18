#!/bin/bash

dir="/home/laura/Desktop/univ/univ2024-1/BigData/proyecto/proyecto1/input"

mkdir -p "$dir"

count=1

while IFS= read -r url
do
    file_name="libro${count}.txt"
  
  wget -O "$dir/$file_name" "$url"
  ((count++))

done < text_url.txt

echo "Descarga completada."

