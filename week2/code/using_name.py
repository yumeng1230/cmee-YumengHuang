#!/usr/bin/env python3
# Filename: using_name.py
"""
This script demonstrates the use of the special variable __name__ in Python.
It prints different messages depending on whether the script is run directly
or imported as a module in another script.

When run directly:
    - Prints "This program is being run by itself!"
When imported as a module:
    - Prints "I am being imported from another script/program/module!"

It also displays the module's name using the __name__ variable.
"""
 
if __name__ == '__main__':
    print('This program is being run by itself!')
else:
    print('I am being imported from another script/program/module!')
 
print("This module's name is: " + __name__)


