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

    def area(self):
        """
        Returns the area of this square object
        """
        return (self.__size ** 2)

    def __str__(self):
        """
        Display thw string representation of this square
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))
