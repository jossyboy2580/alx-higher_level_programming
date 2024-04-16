#!/usr/bin/python3
def lookup(obj):
    """
    A function that returns the names of available
    attributes and functions in an object
    """
    if obj:
        return (dir(obj))
