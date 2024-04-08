#!/usr/bin/python3
"""
A Module that contains the definition of a class called Rectangle
along with various functions

Some doctests
>>> rec1 = Rectangle(35)
>>> print(rec1.width())
35
"""


class Rectangle:
    """
    A class that defines a rectangle object
    """

    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be an integer")
        self.__width = width
        self.__height = height

    def width(self):
        return (self.__width)

    def height(self):
        return (self.__height)
