#!/bin/sh
# Author: Yumeng Huang  yh4724@ic.ac.uk
# Script: csvtospace.sh
# Description: Converts comma-separated values (CSV) files to space-separated values files
#
# If no file is provided, the script converts all CSV files in the current directory
# Saves the output into new files with the suffix "_space" added to the original filenames in the "week1/results" directory
# Arguments: 1 (optional) -> CSV file or leave blank to convert all CSV files in the directory
# Date: Oct 2024

# Function to convert a CSV file to a space-separated file
convert_file() {
    input_file="$1"
    
    # Check if the file exists
    if [ ! -f "$input_file" ]; then
        echo "Error: File '$input_file' not found!"
        exit 1
    fi

    # Check if the file is a .csv file
    if [ "${input_file##*.}" != "csv" ]; then
        echo "Error: The file must be a .csv file."
        exit 2
    fi

    # Set the output file name in the week1/results directory
    filename=$(basename "$input_file" .csv)
    output="../results/${filename}_space.csv"

    echo "Creating a space-delimited version of $input_file ..."

    # Convert commas to spaces and save to the new file
    cat "$input_file" | tr -s "," " " > "$output"

    # Check if the output file was successfully created
    if [ $? -ne 0 ]; then
        echo "Error: Failed to create the output file '$output'."
        exit 3
    fi

    echo "Done! The space-separated file is saved as '$output'."
}

# If an argument is provided, convert that specific file
if [ $# -eq 1 ]; then
    convert_file "$1"
else
    # Convert all CSV files in the current directory
    echo "No file specified. Converting all CSV files in the current directory..."

    for file in *.csv; do
        convert_file "$file"
    done
fi

exit 0
