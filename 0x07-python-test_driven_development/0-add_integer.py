#!/usr/bin/python3
"""
A module that defines some function add
>>> add_integer(2, 6)
8
"""

def add_integer(a, b=98):
    """
    A function that adds two integers together
    """
    if type(a) is not int or float:
        raise TypeError("a must be and integer")
    if type(b) is not int or float:
        raise TypeError("b must be and integer")
    return (int(a) + int(b))
