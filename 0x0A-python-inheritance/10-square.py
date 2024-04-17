#!/usr/bin/python3
"""
Square object representation in
classes defined below
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A Square class
    """

    def __init__(self, size):
        """ class obj initializer """
        try:
            self.integer_validator("size", size)
        except Exception:
            raise
        else:
            self.__size = size
