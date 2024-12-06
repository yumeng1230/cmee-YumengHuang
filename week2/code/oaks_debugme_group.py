#!/usr/bin/env python3
"""
This script processes an input CSV file containing genus and species data. It identifies rows 
where the genus is close to 'Quercus' using fuzzy matching and writes those rows to an output CSV file. 
The script includes a header in the output file if the input contains one.

Features:
1. Identifies genus names close to 'Quercus' using fuzzy matching with a similarity cutoff of 85%.
2. Handles both header and non-header input files gracefully.
3. Skips empty rows and rows with insufficient data.
4. Writes filtered rows to an output CSV file in the specified format.

Modules Used:
- `csv` for reading and writing CSV files.
- `difflib` for fuzzy matching of genus names.
- `os` for file and directory operations.
- `doctest` for testing the functions with embedded examples.

Input:
    - ../data/TestOaksData.csv: The input CSV file containing genus and species data.

Output:
    - ../results/JustOaksData.csv: The output CSV file with rows containing genus names close to 'Quercus'.

"""


import csv
import sys
import difflib
import os
import doctest

def is_an_oak(name):
    """
    Returns True if the name is close to 'quercus' using fuzzy matching.
    
    Parameters:
    name (str): The genus name to check.
    
    Returns:
    bool: True if the name is similar to 'quercus', otherwise False.

    Examples:
    >>> is_an_oak('Quercus')
    True
    >>> is_an_oak('quercus')
    True
    >>> is_an_oak('Querqus')
    True
    >>> is_an_oak('Pinus')
    False
    >>> is_an_oak('quercuz')
    True
    >>> is_an_oak('Betula')
    False
    """
    close_matches = difflib.get_close_matches(name.lower(), ['quercus'], n=1, cutoff=0.85)
    return bool(close_matches)  

def is_header(row):
    """
    Returns True if the row contains 'Genus' and 'Species', indicating it's a header row.
    
    Parameters:
    row (list): A row from the CSV file.
    
    Returns:
    bool: True if the row contains 'Genus' and 'Species', otherwise False.
    
    Examples:
    >>> is_header(['Genus', 'Species'])
    True
    >>> is_header(['genus', 'species'])
    True
    >>> is_header(['genus', 'scientific_name'])
    False
    """
    return row[0].lower() == 'genus' and 'species' in row[1].lower()

def main(argv):
    """
    The main function of the script that processes an input CSV file containing genus and species data.
    
    It searches for rows where the genus is close to 'quercus' and writes those rows to the output CSV file, 
    including a header row if necessary.

    Parameters:
    argv (list): Command-line arguments (not used in this function).

    Returns:
    int: 0 if the script runs successfully, 1 if an error occurs.
    """
    # Define input and output file paths
    input_file = '../data/TestOaksData.csv'
    output_file = '../results/JustOaksData.csv'
 
    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' does not exist.")
        return 1
 
    # Ensure the output directory exists, if not, create it
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
 
    try:
        # Open the input file in read mode, output file in write mode
        with open(input_file, 'r', encoding='utf-8') as f, open(output_file, 'w', newline='', encoding='utf-8') as g:
            taxa = csv.reader(f)
            csvwrite = csv.writer(g)
 
            # Read the first row and check if it's a header
            first_row = next(taxa)
            has_header = is_header(first_row)
 
            # If there is a header, write it to the output file
            if has_header:
                csvwrite.writerow(['Genus', 'Species'])
            else:
                # If no header, manually write header and process the first data row
                csvwrite.writerow(['Genus', 'Species'])
                if is_an_oak(first_row[0]):
                    print(f"FOUND AN OAK! Genus: {first_row[0]}")
                    csvwrite.writerow([first_row[0], first_row[1]])
 
            # Process the remaining rows
            for row in taxa:
                # Skip empty rows or rows with fewer than two columns
                if len(row) < 2:
                    continue

                # If the genus is close to 'quercus', write the row to the output file and print a message
                if is_an_oak(row[0]):
                    print(f"FOUND AN OAK! Genus: {row[0]}")
                    csvwrite.writerow([row[0], row[1]])
 
    except Exception as e:
        print(f"Error processing files: {e}")
        return 1
    return 0
 
# Entry point of the program
if __name__ == "__main__":
    # Run doctest to test the is_an_oak function
    doctest.testmod()
    status = main(sys.argv)
    sys.exit(status)
