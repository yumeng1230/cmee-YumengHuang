#!/usr/bin/env python3

"""
This script identifies oak trees from a list of species names and demonstrates 
the use of `for` loops and list comprehensions to process the data.

Steps:
1. Define a function `is_an_oak` to check if a species belongs to the oak genus (`Quercus`).
2. Use `for` loops and list comprehensions to:
    - Extract oak tree species into a set.
    - Convert oak tree species names to uppercase.

Input:
    - A predefined list of species names.

Output:
    - Sets of oak tree species, printed in their original and uppercase formats.
"""
## Finds just those taxa that are oak trees from a list of species

taxa = [ 'Quercus robur',
         'Fraxinus excelsior',
         'Pinus sylvestris',
         'Quercus cerris',
         'Quercus petraea',
       ]

def is_an_oak(name):
    """
    Determines if a species belongs to the oak genus (`Quercus`).
    """
    return name.lower().startswith('quercus ')

##Using for loops
oaks_loops = set()
for species in taxa:
    if is_an_oak(species):
        oaks_loops.add(species)
print(oaks_loops)

##Using list comprehensions   
oaks_lc = set([species for species in taxa if is_an_oak(species)])
print(oaks_lc)

##Get names in UPPER CASE using for loops
oaks_loops = set()
for species in taxa:
    if is_an_oak(species):
        oaks_loops.add(species.upper())
print(oaks_loops)

##Get names in UPPER CASE using list comprehensions
oaks_lc = set([species.upper() for species in taxa if is_an_oak(species)])
print(oaks_lc)