#!/usr/bin/env python3

"""
This script demonstrates how to use Python's pickle module to save and load objects.

Steps:
1. Save a dictionary object to a binary file using `pickle.dump`.
2. Load the dictionary object back from the binary file using `pickle.load`.

Input:
    - ../sandbox/testp.p: The binary file used to store the pickled object.

Output:
    - The loaded dictionary is printed to the console.
"""

#############################
# STORING OBJECTS
#############################
# To save an object (even complex) for later use
my_dictionary = {"a key": 10, "another key": 11}

import pickle

f = open('../sandbox/testp.p','wb') ## note the b: accept binary files
pickle.dump(my_dictionary, f)
f.close()

## Load the data again
f = open('../sandbox/testp.p','rb')
another_dictionary = pickle.load(f)
f.close()

print(another_dictionary)
