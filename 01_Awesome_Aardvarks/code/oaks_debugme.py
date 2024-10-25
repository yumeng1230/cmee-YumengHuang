#!/usr/bin/env python3


 
import csv

import sys

import difflib

import os

import doctest  # Import the doctest module
 
# Define function to check if the genus is close to 'quercus' using fuzzy matching

def is_an_oak(name):

    """

    Returns True if the name is close to 'quercus'
 
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

    return len(close_matches) > 0
 
def is_header(row):

    """

    Checks if the row is a header (e.g., it contains 'Genus' and 'Species').

    Returns True if it is a header, False otherwise.

    """

    return row[0].lower() == 'genus' and 'species' in row[1].lower()
 
 #main function
def main(argv):

    # Define input and output file paths

    input_file = '../data/TestOaksData.csv'

    output_file = '../results/JustOaksData.csv'

    # Check if the input file exists

    if not os.path.exists(input_file):

        print(f"Error: Input file '{input_file}' does not exist.")

        return 1

    # Ensure the output directory exists

    output_dir = os.path.dirname(output_file)

    if not os.path.exists(output_dir):

        os.makedirs(output_dir)

    try:

        # Open the input file in read mode and the output file in write mode

        with open(input_file, 'r', encoding='utf-8') as f, open(output_file, 'w', newline='', encoding='utf-8') as g:

            taxa = csv.reader(f)

            csvwrite = csv.writer(g)

            # Read the first row and check if it's a header

            first_row = next(taxa)

            if not is_header(first_row):

                # If it's not a header, write header to output and process it like a normal data row

                csvwrite.writerow(['Genus', 'Species'])

                print(first_row)

                print("The genus is:")

                print(first_row[0] + '\n')
 
                if is_an_oak(first_row[0]):

                    print('FOUND AN OAK!\n')

                    csvwrite.writerow([first_row[0], first_row[1]])
 
            # Write the header to the output file if the first row was a header

            if is_header(first_row):

                csvwrite.writerow(['Genus', 'Species'])  # Add header if the first row was skipped

            # Process the remaining rows

            for row in taxa:

                # Ensure the row has at least 2 columns (to avoid IndexError)

                if len(row) < 2:

                    continue  # Skip malformed rows
 
                print(row)

                print("The genus is:")

                print(row[0] + '\n')  # Output the genus name

                # Check if the genus is close to 'quercus' using fuzzy matching

                if is_an_oak(row[0]):

                    print('FOUND AN OAK!\n')

                    # Write the relevant row to the output file if it's an oak

                    csvwrite.writerow([row[0], row[1]])

    except Exception as e:

        print(f"Error processing files: {e}")

        return 1
 
    return 0
 
# Entry point for script execution

if __name__ == "__main__":

    # Run doctest to test the is_an_oak function

    doctest.testmod()

    status = main(sys.argv)

    sys.exit(status)

 