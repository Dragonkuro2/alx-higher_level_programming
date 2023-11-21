#!/usr/bin/python3
''' A square defined.'''


class Square:
    ''' A square class.'''

    def __init__(self, size=0):
        ''' Initialize a square with specified size.
        Args:
            size (int): the size of the square.

        Raises:
            TypeError: is the size is not an integr.
            ValueError: is the size is less than 0.
        '''

        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        ''' Calculate the area of the square.

        Returns:
            type int: the area of the square
        '''

        return self.__size ** 2
