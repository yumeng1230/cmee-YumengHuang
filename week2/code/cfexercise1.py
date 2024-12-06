#!/usr/bin/env python3

"""
This script demonstrates various mathematical functions, including:
1. Calculating the square root of a number.
2. Finding the larger of two numbers.
3. Returning three values in ascending order.
4. Calculating the factorial of a number using different approaches:
   - For loop
   - Recursion
   - While loop

Author:
    Yumeng Huang (yh4724@ic.ac.uk)

Version:
    0.01
"""

_author_ = 'Yumeng Huang (yh4724@ic.ac.uk)'
_version_ = '0.01'

import sys

# Function to calculate the square root of a number
def foo_1(x):
    """
    Calculates the square root of a number.
    """
    return x ** 0.5

# Function to return the larger of two values
def foo_2(x, y):
    """
    Returns the larger of two values.
    """
    if x > y:
        return x
    return y

# Function to return three values in ascending order
def foo_3(x, y, z):
    """
    Returns three values in ascending order.
    """
    # Ensure x is the smallest
    if x > y:
        tmp = y
        y = x
        x = tmp
    # Ensure y is less than or equal to z
    if y > z:
        tmp = z
        z = y
        y = tmp
    return [x, y, z]

# Function to calculate the factorial of x using a loop
def foo_4(x):
    """
    Calculates the factorial of a number using a for loop.
    """
    result = 1
    for i in range(1, x + 1):
        result = result * i
    return result

# Recursive function to calculate the factorial of x
def foo_5(x):
    """
    Calculates the factorial of a number using recursion.
    """
    if x == 1:
        return 1
    return x * foo_5(x - 1)
     
# Function to calculate the factorial of x using a while loop (no if statement)
def foo_6(x):
    """
    Calculates the factorial of a number using a while loop.
    """

    facto = 1
    while x >= 1:
        facto = facto * x
        x = x - 1
    return facto

# Main function to demonstrate the use of the defined functions
def main(argv):
    """Main function to print results from the defined functions."""
    
    # Calculate and print the square root of 9
    print(f"foo_1(9) = {foo_1(9)}")
    
    # Find the larger value between 10 and 5
    print(f"foo_2(10, 5) = {foo_2(10, 5)}")
    
    # Return three values in ascending order
    print(f"foo_3(3, 1, 2) = {foo_3(3, 1, 2)}")
    
    # Calculate the factorial of 9 using a loop
    print(f"foo_4(9) = {foo_4(9)}")
    
    # Calculate the factorial of 9 using recursion
    print(f"foo_5(9) = {foo_5(9)}")
    
    # Calculate the factorial of 9 using a while loop
    print(f"foo_6(9) = {foo_6(9)}")

    return 0

# Entry point of the script
if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)
