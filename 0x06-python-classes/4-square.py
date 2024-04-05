#!/usr/bin/python3
"""
A Module that defines a class
"""


class Square:
    """
    A class that defines a square object
    """
    def __init__(self, size=0):
        self.__setattr__("size", size)

    def area(self):
        return (self.__size ** 2)

    def __getattr__(self):
        return (self.__size)

    def __setattr__(self, name, value):
        if name == "size":
            if type(value) is not int:
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
