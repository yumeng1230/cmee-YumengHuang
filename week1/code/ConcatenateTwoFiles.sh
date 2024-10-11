#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 3 ]; then
  echo "Usage: $0 <file1> <file2> <output_file>"
  exit 1
fi

# Check if the input files exist and are readable
if [ ! -f "$1" ]; then
  echo "Error: File $1 does not exist."
  exit 1
fi

if [ ! -f "$2" ]; then
  echo "Error: File $2 does not exist."
  exit 1
fi

# Check if the output file is writable or if the directory is writable
if [ -f "$3" ] && [ ! -w "$3" ]; then
  echo "Error: File $3 is not writable."
  exit 1
fi

if [ ! -f "$3" ] && [ ! -w "$(dirname "$3")" ]; then
  echo "Error: Directory $(dirname "$3") is not writable."
  exit 1
fi

# Merge the files
cat "$1" > "$3"
if [ $? -ne 0 ]; then
  echo "Error: Failed to write content of $1 to $3"
  exit 1
fi

cat "$2" >> "$3"
if [ $? -ne 0 ]; then
  echo "Error: Failed to append content of $2 to $3"
  exit 1
fi

# Display the merged file
echo "Merged File is"
cat "$3"
