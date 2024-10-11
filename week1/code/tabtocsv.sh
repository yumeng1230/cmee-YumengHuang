#!/bin/sh
# Author: Yumeng Huang  yh4724@ic.ac.uk
# Script: tabtocsv.sh
# Description: Substitute the tabs in the files with commas
# Saves the output into a .csv file located in the "result" directory
# Validates if the file exists and if it is a .txt file before proceeding
# Arguments: 1 -> tab delimited file
# Date: Oct 2024

set -e

# Check if the argument is provided
if [ $# -eq 0 ]; then
    echo "Error: No file provided. Usage: $0 filename"
    exit 1
fi

# Check if the file exists
if [ ! -f "$1" ]; then
    echo "Error: File '$1' not found!"
    exit 2
fi

# Check if the file is a .txt file
if [ "${1##*.}" != "txt" ]; then
    echo "Error: The file must be a .txt file (tab-delimited)."
    exit 3
fi

# Check if the file is tab-delimited
if ! grep -q $'\t' "$1"; then
    echo "Error: The file '$1' does not appear to be tab-delimited."
    exit 3
fi

# Check write permissions for the result directory
if [ ! -w result ]; then
    echo "Error: No write permission for the 'result' directory."
    exit 4
fi

# Set the output file path in the 'result' directory
filename=$(basename "$1")
output="result/${filename}.csv"

# Check if output file already exists to avoid overwriting
if [ -f "$output" ]; then
    echo "Error: Output file '$output' already exists. Please remove it or choose a different input file."
    exit 4
fi

# Convert tabs to commas and save to the result directory
echo "Creating a comma delimited version of $1 ..."
cat "$1" | tr -s "\t" "," >> "$output"

# Check if the output file was successfully created
# If the status code is not 0(indicating failure), an error message is displayed and the exit code is 5
if [ $? -ne 0 ]; then
    echo "Error: Failed to create the output file."
    exit 5
fi

echo "Done!"
exit 0
