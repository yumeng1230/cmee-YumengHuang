#!/usr/bin/env python3

import csv
import sys
import difflib
import os

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
    #cutoff=0.85 is the minimum similarity ratio required for a match to be considered. 
    close_matches = difflib.get_close_matches(name.lower(), ['quercus'], n=1, cutoff=0.85)
    return len(close_matches) > 0

def main(argv): 
    # Check if the ../results directory exists, if not, create it
    output_dir = '../results'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Open the input file in read mode and the output file in append mode
    f = open('../data/TestOaksData.csv', 'r')
    g = open(os.path.join(output_dir, 'JustOaksData.csv'), 'a', newline='')  # Save output to '../results'

    taxa = csv.reader(f)
    csvwrite = csv.writer(g)
    
    for row in taxa:
        print(row)
        print("The genus is:") 
        print(row[0] + '\n')  # Output the genus name
        
        # Check if the genus is close to 'quercus' using fuzzy matching
        if is_an_oak(row[0]):
            print('FOUND AN OAK!\n')
            # Write the relevant row to the output file if it's an oak
            csvwrite.writerow([row[0], row[1]])

    f.close()  # Close the input file
    g.close()  # Close the output file
    
    return 0

# Entry point for script execution
if __name__ == "__main__":
    status = main(sys.argv)
