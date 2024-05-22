#!/usr/bin/python3
"""
A Module that defines a class
"""


class Square:
    """
    A class that defines a square object
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialization for our object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        ps = position  # aliasing position to reduce length of next line
        if not isinstance(ps[0], int) or not isinstance(ps[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        """
        Return the value of the position attribute
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        The position attribute setter
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        A method to print the structure of this square object
        """
        if not self.size:
            print()
            return
        i = 0
        y_lines = 0
        for j in range(self.position[1]):
            print()
        while i < self.size:
            print("_" * self.position[0], end="")
            print("#" * self.size)
            i += 1
