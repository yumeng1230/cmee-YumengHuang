#!/bin/bash

# Loop through all .tif files in the current directory
for f in *.tif; 
do  
    # Check if there are no .tif files in the directory
    if [ "$f" = "*.tif" ]; then
        echo "No .tif files found in the current directory."
        exit 1
    fi

    # Check if the file exists and is a regular file
    if [ ! -f "$f" ]; then
        echo "Error: File $f does not exist or is not a regular file."
        exit 1
    fi

    # Check if the file has the correct .tif extension
    if [[ "${f##*.}" != "tif" ]]; then
        echo "Error: $f is not a .tif file."
        exit 1
    fi

    # Check if the script has permission to read the input file
    if [ ! -r "$f" ]; then
        echo "Error: No read permission for $f."
        exit 1
    fi

    # Prepare the output file name
    output_file="$(basename "$f" .tif).png"

    # Check if the script has permission to write the output file
    if [ -e "$output_file" ] && [ ! -w "$output_file" ]; then
        echo "Error: No write permission for $output_file."
        exit 1
    fi

    # Perform the conversion from .tif to .png
    echo "Converting $f"
    convert "$f" "$output_file"

    # Verify if the output file was successfully created and has a .png extension
    if [ -f "$output_file" ] && [[ "${output_file##*.}" == "png" ]]; then
        echo "Successfully converted $f to $output_file."
    else
        echo "Error: Conversion failed for $f."
        exit 1
    fi
done
