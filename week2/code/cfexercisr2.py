#!/usr/bin/env python3

"""
This script demonstrates various looping and conditional examples, 
where the word 'hello' is printed based on different criteria.

Functions:
    - hello_1: Prints 'hello' for numbers divisible by 3 in a range.
    - hello_2: Prints 'hello' for numbers satisfying specific remainders.
    - hello_3: Prints 'hello' for each number in a given range.
    - hello_4: Prints 'hello' repeatedly until a value reaches 15.
    - hello_5: Prints 'hello' based on multiple conditions while iterating.
    - hello_6: Prints 'hello' with an incrementing counter until a limit.

Usage:
    Simply run the script to see outputs from each function demonstrating
    the specified conditions.
"""

#############################################################################
def hello_1(x):
    """
    Prints 'hello' for numbers divisible by 3 from 0 to x-1.

    Args:
        x (int): The upper limit (exclusive).
    """
    for j in range(x):
        if j % 3 == 0:
            print('hello')
    print(' ')


hello_1(12)


##############################################################################
def hello_2(x):
    """
    Prints 'hello' for numbers in 0 to x-1 where:
    - Remainder is 3 when divided by 5 or 4.

    Args:
        x (int): The upper limit (exclusive).
    """
    for j in range(x):
        if j % 5 == 3 or j % 4 == 3:
            print('hello')
    print(' ')


hello_2(12)


####################################################################
def hello_3(x, y):
    """
    Prints 'hello' for each number in the range [x, y).

    Args:
        x (int): Start of the range (inclusive).
        y (int): End of the range (exclusive).
    """
    for i in range(x, y):
        print('hello')
    print(' ')


hello_3(3, 17)


########################################################################
def hello_4(x):
    """
    Prints 'hello' repeatedly until x reaches 15, incrementing by 3.

    Args:
        x (int): Starting value.
    """
    while x != 15:
        print('hello')
        x += 3
    print(' ')


hello_4(0)


####################################################################
def hello_5(x):
    """
    Prints 'hello' based on specific conditions while x < 100:
    - Prints 7 times if x == 31.
    - Prints once if x == 18.

    Args:
        x (int): Starting value.
    """
    while x < 100:
        if x == 31:
            for k in range(7):
                print('hello')
        elif x == 18:
            print('hello')
        x += 1
    print(' ')


hello_5(12)


#######################################################################
def hello_6(x, y):
    """
    Prints 'hello' with an incrementing counter until y reaches 6.

    Args:
        x (bool): Condition to control the loop.
        y (int): Starting counter value.
    """
    while x:
        print(f"hello! {y}")
        y += 1
        if y == 6:
            break
    print(' ')


hello_6(True, 0)

