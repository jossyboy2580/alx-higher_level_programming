#!/usr/bin/python3
"""
A module containing a function to check
instances
"""


def is_same_class(obj, a_class):
    """
    this function ascertains if obj is an instance
    of a_class
    """
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
