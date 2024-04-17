#!/usr/bin/python3
"""
Module containing a function that checks for
subclassing
"""


def inherits_from(obj, a_class):
    """
    Function to chexk if an obj is a
    subclass of a_class
    """
    return (issubclass(type(obj), a_class) and isinstance(obj, a_class))
