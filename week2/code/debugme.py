#!/usr/bin/env python3

"""
This script demonstrates a function (`buggyfunc`) that iteratively decrements a value 
and calculates a division. It highlights potential issues with zero division 
for certain input values and demonstrates how to document such behavior.

Function:
    - buggyfunc: Decrements a value and performs a division in a loop.

Usage:
    - python debugme.py

"""

def buggyfunc(x):
    """
    A function that iteratively decrements a value and computes a division.
    """
    y = x
    for i in range(x):
        y = y-1
        z = x/y
    return z

buggyfunc(20)