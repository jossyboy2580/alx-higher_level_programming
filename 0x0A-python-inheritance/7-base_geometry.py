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

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
