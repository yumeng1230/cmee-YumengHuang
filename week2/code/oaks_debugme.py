#!/usr/bin/env python3

"""
This script filters taxa data from a CSV file to find rows with genus names similar to 'Quercus'.
The filtered data is saved to a new CSV file.

Usage:
    python3 oaks_debugme.py

Inputs:
    - ../data/TestOaksData.csv: A CSV file containing taxa data.

Outputs:
    - ../results/JustOaksData.csv: A CSV file with filtered rows matching 'Quercus'.

Features:
1. Uses fuzzy matching to identify genus names close to 'Quercus'.
2. Includes doctests for `is_an_oak` with additional edge-case examples.
3. Implements robust error handling to ensure input file existence before processing.
"""

import csv
import sys
import difflib
import os


def is_an_oak(name):
    """
    Returns True if the name is close to 'quercus'
    
    Args:
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
    >>> is_an_oak('Quercus-')  # Edge case: Genus name with special character
    False
    >>> is_an_oak('Quercus123')  # Edge case: Genus name with numbers
    False
    >>> is_an_oak('')  # Edge case: Empty string
    False
    >>> is_an_oak('QUERCUS')  # Case insensitive match
    True
    """
    close_matches = difflib.get_close_matches(name.lower(), ['quercus'], n=1, cutoff=0.85)
    return len(close_matches) > 0


def main(argv):
    """
    Processes the input CSV file, filters rows based on genus similarity,
    and writes the filtered data to an output CSV file.

    Args:
        argv (list): Command-line arguments (not used in this script).

    Returns:
        int: Exit status code (0 for success, 1 for errors).
    """
    # Ensure the output directory exists
    output_dir = '../results'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Define input and output file paths
    input_file = '../data/TestOaksData.csv'
    output_file = os.path.join(output_dir, 'JustOaksData.csv')

    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' does not exist.")
        return 1

    try:
        # Open input and output files
        with open(input_file, 'r', encoding='utf-8') as f, open(output_file, 'a', newline='', encoding='utf-8') as g:
            taxa = csv.reader(f)
            csv_writer = csv.writer(g)

            # Process each row in the input file
            for row in taxa:
                # Skip empty rows or rows with insufficient columns
                if len(row) < 2:
                    continue

                print(row)
                print(f"The genus is: {row[0]}\n")

                # Check if the genus is close to 'Quercus'
                if is_an_oak(row[0]):
                    print('FOUND AN OAK!\n')
                    # Write matching rows to the output file
                    csv_writer.writerow([row[0], row[1]])

    except FileNotFoundError as e:
        print(f"Error: {e}")
        return 1
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 1

    return 0


if __name__ == "__main__":
    # Run doctests for the is_an_oak function
    import doctest
    doctest.testmod()

    # Execute the main function
    status = main(sys.argv)
    sys.exit(status)
