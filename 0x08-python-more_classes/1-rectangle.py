#!/usr/bin/python3
"""
A Module that contains the definition of a class called Rectangle
along with various functions

Some doctests

"""


class Rectangle:
    """
    A class that defines a rectangle object
    """

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be an integer")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """ A property getter function """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ A property setter function """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be an integer")
        self.__height = value
