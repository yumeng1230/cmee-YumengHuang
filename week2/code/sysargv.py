#!/usr/bin/env python3
"""
This script demonstrates how to use command-line arguments in Python using the sys module.

It prints:
1. The name of the script being executed.
2. The number of command-line arguments passed to the script.
3. The list of all command-line arguments.

Usage:
    Run the script with optional arguments:
    $ python3 script_args.py arg1 arg2 arg3

Example Output:
    This is the name of the script:  script_args.py
    Number of arguments:  4
    The arguments are:  ['script_args.py', 'arg1', 'arg2', 'arg3']

Note:
    - `sys.argv[0]` is always the name of the script.
    - The rest of the elements in `sys.argv` are the command-line arguments provided.
"""
import sys
print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: " , str(sys.argv))