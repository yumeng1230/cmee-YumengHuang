#!/usr/bin/env python3

"""
This script demonstrates the use of control statements in Python through functions 
and embedded doctests. It includes a function `even_or_odd` that determines whether 
a given number is even or odd.

Functions:
    - even_or_odd: Determines whether a number is even or odd.
    - main: Executes examples of the `even_or_odd` function.

Usage:
    Run the script directly to see outputs for sample inputs and test cases.
    The embedded doctests can be executed automatically to verify the correctness
    of the `even_or_odd` function.

Author:
    Yumeng Huang (yh4724@ic.ac.uk)

Version:
    0.0.1
"""

__author__ = 'Yumeng Huang (yh4724@ic.ac.uk)'
__version__ = '0.0.1'

import sys
import doctest  # Import the doctest module


def even_or_odd(x=0):
    """
    Determines whether a number x is even or odd.
      
    Examples:
        >>> even_or_odd(10)
        '10 is Even!'
        
        >>> even_or_odd(5)
        '5 is Odd!'
        
        In the case of negative numbers, the positive equivalent is taken:
        >>> even_or_odd(-2)
        '-2 is Even!'
    """
    # Determine if the number is even or odd
    if x % 2 == 0:
        return f"{x} is Even!"
    return f"{x} is Odd!"


def main(argv):
    """
    Main function that prints examples of the `even_or_odd` function.

    """
    print(even_or_odd(22))
    print(even_or_odd(33))
    return 0


if __name__ == "__main__":
    status = main(sys.argv)

# Run embedded doctests
doctest.testmod()

