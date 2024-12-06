#!/usr/bin/env python3

"""
This script demonstrates basic file input operations in Python.

Steps:
1. Open a file and print each line, including blank lines.
2. Re-open the same file and print each line, skipping blank lines.

Input:
    - ../sandbox/test.txt: A text file to be read.

Output:
    - Lines from the input file are printed to the console, either all lines or only non-blank lines.
"""

#############################
# FILE INPUT
#############################

def read_and_print_all_lines():
    """
    Reads and prints all lines from a file, including blank lines.
    """
    f = open('../sandbox/test.txt', 'r')
    for line in f:
        print(line)
    f.close()


def read_and_print_non_blank_lines():
    """
    Reads and prints only non-blank lines from a file.
    """
    f = open('../sandbox/test.txt', 'r')
    for line in f:
        if len(line.strip()) > 0:
            print(line)
    f.close()


if __name__ == "__main__":
    # Read and print all lines
    print("Printing all lines (including blanks):")
    read_and_print_all_lines()

    # Read and print non-blank lines
    print("\nPrinting non-blank lines:")
    read_and_print_non_blank_lines()

