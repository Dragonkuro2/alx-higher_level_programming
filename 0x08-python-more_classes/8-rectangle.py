#!/usr/bin/python3
""" The module of the class Rectangle. """


class Rectangle:
    """ Empty class with the name Rectangle. """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Initialize the value of the width and the height. """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """ print the rectangle with the character #,

        Returns:
            str: the rectangle with #
        """

        rectangle = []
        if self.__width == 0 or self.__height == 0:
            return ""

        for column in range(self.__height):
            for row in range(self.__width):
                rectangle.append(str(self.print_symbol))
            rectangle.append("\n")

        # remove the last blank line
        rectangle.pop()

        return "".join(rectangle)

    def __repr__(self):
        """ Returns a string representation of the rectangle. """

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ uses when a instance deletes"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ the method checks for the biggest area.

        Args:
            rect_1: the first Rectangle element.
            rect_2: the second Rectangle element.

        Returns:
            TypeError: when the input argument isn't an rectangle element.
        Returns: the biggest area from the rect_1 and rect_2
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1

        return rect_2
