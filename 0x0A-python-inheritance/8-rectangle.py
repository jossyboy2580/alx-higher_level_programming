#!/usr/bin/python3
"""
Geometric objec representation in
classes defined below
"""


class BaseGeometry(object):
    """
    A base class for a geometric object
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if name:
            if type(value) is not int:
                raise TypeError("{} must be an integer".format(name))
            if value < 1:
                raise ValueError("{} must be greater than 0".format(name))
