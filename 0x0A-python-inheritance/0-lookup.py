#!/usr/bin/python3
"""
A module containing a function that lists all attributes and
methods of an object
"""
def lookup(obj):
    """
    A function that returns the names of available
    attributes and functions in an object
    """
    if obj:
        return (dir(obj))
