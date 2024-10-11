#!/bin/bash
# Author: Yumeng Huang  yh4724@ic.ac.uk
# Script: Countlines.sh
# Description: 

# Validates if the file exists and if it is a .txt file before proceeding
# Arguments: 1 -> tab delimited file
# Date: Oct 2024

#!/bin/bash

# Check if the Bash interpreter is available
if [ -z "$(command -v bash)" ]; then
  echo "Error: Bash is not available or not in the PATH."
  exit 1
fi

# Check if a file name is provided as an argument
if [ -z "$1" ]; then
  echo "Error: No file provided. Please provide a file name."
  exit 1
fi

# Check if the file exists and is a regular file
if [ ! -f "$1" ]; then
  echo "Error: File '$1' does not exist or is not a regular file."
  exit 1
fi

# Check if the file is readable
if [ ! -r "$1" ]; then
  echo "Error: File '$1' is not readable. Please check permissions."
  exit 1
fi

# Output the result
echo "The file $1 has $NumLines lines"


