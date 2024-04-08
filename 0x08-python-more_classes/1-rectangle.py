#!/usr/bin/python3
"""
A Module that contains the definition of a class called Rectangle
along with various functions
"""


class Rectangle:
    """
    A class that defines a rectangle object
    """
    
    def __init__(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
    
    def width(self):
        return (self.__width)
