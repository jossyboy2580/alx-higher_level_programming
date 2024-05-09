#!/usr/bin/python3
"""
A Module that defines a class
"""


class Square:
    """
    A class that defines a square object
    """
    def __init__(self, size=0):
        """
        Initialization for our object
        """
        self.__setattr__("size", size)

    def area(self):
        """
        Compute the area of the square object
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        A property getter for the attribute size
        """
        return (self.__size)
    
    @size.setter
    def size(self, value):
        """
        A property setter for the attribute size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        A method to print the structure of this square object
        """
        if not self.size:
            print()
            return
        i = 0
        while i < self.size:
            print("#" * self.size)
            i += 1
