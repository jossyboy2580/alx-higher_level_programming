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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be an integer")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((2 * self._width) + (2 * self.__height))

    def __str__(self):
        string_list = []
        for i in range(self.__height):
            for j in range(self.__width):
                string_list.append(Rectangle.print_symbol)
            string_list.append("\n")
        return ("".join(string_list).strip("\n"))

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
