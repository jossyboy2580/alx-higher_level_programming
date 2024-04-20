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
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
