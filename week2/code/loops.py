#!/usr/bin/env python3

"""
This script demonstrates the use of `for` and `while` loops in Python.
It covers the following examples:

1. Using a `for` loop to iterate over a range of numbers and print them.
2. Using a `for` loop to iterate over a list of mixed data types and print each element.
3. Using a `for` loop to calculate a running total from a list of numbers.
4. Using a `while` loop to increment a counter until it reaches a specific condition.
"""

# FOR loops
for i in range(5):
    print(i)

my_list = [0, 2, "geronimo!", 3.0, True, False]
for k in my_list:
    print(k)

total = 0
summands = [0, 1, 11, 111, 1111]
for s in summands:
    total = total + s
    print(total)

# WHILE loop
z = 0
while z < 100:
    z = z + 1
    print(z)