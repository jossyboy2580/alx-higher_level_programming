#!/usr/bin/python3
"""
A module containing an instance checker
"""


def is_kind_of_class(obj, a_class):
    """
    Check if object is an instance or instance of
    a descendant
    """
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
