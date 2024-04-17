#!/usr/bin/python3
"""
A module containing a function to try
and add an attribute to an object
"""


def add_attribute(my_obj, name, value):
    """
    Use the hasattr function to check if a function
    can take dynamic attributes
    """
    if not hasattr(my_obj, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        my_obj[name] = value
