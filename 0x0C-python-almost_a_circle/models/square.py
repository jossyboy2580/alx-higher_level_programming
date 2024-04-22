#!/usr/bin/python3
"""
A module that defines a class for an object 'square'
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class that defines a square shape
    this class inherits from The Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):

        """
        Square object initializer
        This simply calls the init of the super class
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Paramenter overloading for the str method or printing
        of object
        """
        identity = " ({})".format(self.id)
        coordinates = " {}/{}".format(self.x, self.y)
        size = " {}".format(self.width)
        return ("[Square]" + identity + coordinates + " -" + size)

    @property
        def size(self):

            """ Property getter for our class """

        return (self.__width)

    @size.setter
        def size(self, value):

            """ Property setter for our class """

        if type(value) is int:
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    def update(self, *args, **kwargs):

        """ A method that uses variable arguments to update
        our rectangle """

        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
