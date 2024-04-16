#!/usr/bin/python3
"""
Geometric objec representation in
classes defined below
"""


class BaseGeometry(object):
    """
    A base class for a geometric object
    """
    
    def area(self):
        raise Exception("area() is not implemented")
