#!/usr/bin/python3
"""
A module for a Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    A class definition for a rectangle object
    """

    def __init__(self, width, height, x=0, y=0, id=None):

        """ Initializer for our class """

        super().__init__(id)

        # Attribute instantiation for width

        if type(width) is int:
            if width > 0:
                self.__width = width
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

        # Attribute instantiation for height

        if type(height) is int:
            if height > 0:
                self.__height = height
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

        # Attribute instantiation for x

        if type(x) is int:
            if x >= 0:
                self.__x = x
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

        # Attribute instantiation for y

        if type(y) is int:
            if y >= 0:
                self.__y = y
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    @property
    def width(self):

        """ Property getter for our class """

        return (self.__width)

    @width.setter
    def width(self, value):

        """ Property setter for our class """

        if type(value) is int:
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):

        """ Property getter for our class """

        return (self.__height)

    @height.setter
    def height(self, value):

        """ Property setter for our class """

        if type(value) is int:
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):

        """ Property getter for our class """

        return (self.__x)

    @x.setter
    def x(self, value):

        """ Property setter for our class """

        if type(value) is int:
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):

        """ Property getter for our class """

        return (self.__y)

    @y.setter
    def y(self, value):

        """ Property setter for our class """

        if type(value) is int:
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """ A method to get the area of the rectangle """
        return (self.__width * self.__height)

    def display(self):
        """
        This method prints out a rectangle of the dimension
        width * height
        using '#'
        """
        total_height = self.__height + self.__y
        total_width = self.__width + self.__x
        for i in range(total_height):
            if i < self.__y:
                print()
                continue
            for j in range(total_width):
                if j < self.__x:
                    print(" ", end="")
                else:
                    print("#", end="")
            print()

    def __str__(self):
        """
        Paramenter overloading for the str method or printing
        of object
        """
        identity = " ({})".format(self.id)
        coordinates = " {}/{}".format(self.__x, self.__y)
        dimensions = " {}/{}".format(self.__width, self.__height)
        return ("[Rectangle]" + identity + coordinates + " -" + dimensions)

    def update(self, *args, **kwargs):

        """ A method that uses variable arguments to update
        our rectangle """

        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        return ({'id': self.id, 'width': self.width, 'height': self.height, 'x':self.x, 'y': self.y})
