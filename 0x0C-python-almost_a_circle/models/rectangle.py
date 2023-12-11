#!/usr/bin/python3
''' rectangle.py '''


from models.base import Base


class Rectangle(Base):
    ''' class that initialize the elements. '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' initialize the arguments. '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        ''' return the width. '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' set the width and make it private. '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        ''' getter of the height. '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' setter of the height. '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        ''' getter of x. '''
        return self.__x

    @x.setter
    def x(self, value):
        ''' setter that set x to be private. '''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        ''' getter of y. '''
        return self.__y

    @y.setter
    def y(self, value):
        ''' setter that set y to be private. '''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        ''' calculate the area of the rectangle. '''
        return self.__width * self.__height

    def display(self):
        ''' prints in stdout the rectangle with #. '''
        for width in range(self.__y):
            print()
        for height in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        ''' str methode. '''
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
                f" - {self.__width}/{self.__height}")
