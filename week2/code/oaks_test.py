#!/usr/bin/env python3

"""
This script defines a function to check if a given genus name starts with 'Quercus'.
It includes doctests embedded in the function docstring to verify its correctness.

Functions:
    - is_an_oak: Returns True if a name starts with 'Quercus' (case-insensitive).

Usage:
    Run the script directly to test the function using the embedded doctests.
"""

def is_an_oak(name):
    """
    Returns True if name starts with 'quercus'.

    Args:
        name (str): The name to check.

    Returns:
        bool: True if the name starts with 'quercus', False otherwise.

    Examples:
        >>> is_an_oak('Fagus sylvatica')
        False

        >>> is_an_oak('Quercus robur')
        True

        # A typo
        >>> is_an_oak('Quercuss')
        False
    """
    return name.lower().startswith('quercus ')

# Print the function's docstring
print(is_an_oak.__doc__)

# Run doctests
if __name__ == "__main__":
    import doctest
    doctest.testmod()  # Run embedded tests

