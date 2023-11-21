#!/usr/bin/python3
''' Square Module.'''


class Square:
    ''' A class representing a square. '''

    def __init__(self, size=0):
        ''' initializes a square instance with a specified size.

            Arrguments:
                size (int): the size of the square. by default it is 0.

            Raises:
                TypeError: if the size is not an integer.
                ValueError: if the size is less than 0.
        '''
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
