#!/usr/bin/python3
""" The module of the class Rectangle. """


class Rectangle:
    """ Empty class with the name Rectangle. """
    def __init__(self, width=0, height=0):
        """ Initialize the value of the width and the height. """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ make the width private. """

        return self.__width

    @width.setter
    def width(self, value):
        """ checking if width is an int and >= 0.
            Args:
                Value: the value of the width.

            Raises:
                TypeError: when the value isn't an integer.
                ValueError: when the value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ make the height private. """

        return self.__height

    @height.setter
    def height(self, value):
        """ checking if value is an int and not less than 0.
            Args:
                value: the value of the height.

            Raises:
                TypeError: when the value isn't an integer.
                ValueError: when height is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ the method returns the area of the rectangle. """

        return self.__width * self.__height

    def perimeter(self):
        """ This method returns the perimeter of the rectangle. """

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width * 2 + self.__height * 2
