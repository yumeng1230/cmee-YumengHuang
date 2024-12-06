#!/usr/bin/env python3

"""
This script demonstrates how to write the elements of a list to a file in Python.

Steps:
1. Define a list or range of elements to save to a file.
2. Open a file in write mode.
3. Iterate through the list and write each element to the file, adding a newline at the end.
4. Close the file to ensure all data is written and resources are released.

Input:
    - None (the list is defined within the script).

Output:
    - ../sandbox/testout.txt: A text file containing the elements of the list, 
      each on a new line.
"""

#############################
# FILE OUTPUT
#############################

# Define a list or range of elements to save
list_to_save = range(100)

# Open the output file in write mode
f = open('../sandbox/testout.txt', 'w')
for i in list_to_save:
    f.write(str(i) + '\n')  # Write each element followed by a newline

# Close the file
f.close()
