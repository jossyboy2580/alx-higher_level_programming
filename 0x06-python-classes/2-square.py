#!/usr/bin/python3
"""
A Module that defines a class
"""


class Square:
    """
    A class that defines a square object
    """
    def __init__(self, size=0):
        if size is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
