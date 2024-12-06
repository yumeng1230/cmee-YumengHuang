#!/usr/bin/env python3

"""
This script demonstrates how to read and write CSV files in Python.

Steps:
1. Read a CSV file (`testcsv.csv`) containing data fields:
   'Species', 'Infraorder', 'Family', 'Distribution', 'Body mass male (Kg)'.
   - Print each row and display the species name.

2. Write a new CSV file (`bodymass.csv`) containing only the species name
   and body mass of the male from the input file.

Input:
    - ../data/testcsv.csv: The input CSV file with complete data.

Output:
    - ../data/bodymass.csv: The output CSV file containing species name and body mass.
"""

import csv

# Step 1: Read the input file and print each row
with open('../data/testcsv.csv', 'r') as f:
    csvread = csv.reader(f)
    temp = []
    for row in csvread:
        temp.append(tuple(row))  # Convert each row to a tuple and store in a list
        print(row)
        print("The species is", row[0])

# Step 2: Write a new file with only species name and body mass
with open('../data/testcsv.csv', 'r') as f:
    with open('../data/bodymass.csv', 'w') as g:
        csvread = csv.reader(f)
        csvwrite = csv.writer(g)
        for row in csvread:
            print(row)  # Print each row for verification
            csvwrite.writerow([row[0], row[4]])  # Write only species name and body mass
