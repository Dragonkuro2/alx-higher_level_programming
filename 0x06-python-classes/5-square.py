#!/usr/bin/python3
''' A square module. '''


class Square:
    ''' the square class. '''

    def __init__(self, size=0):
        ''' initializes self to a value. '''

        self.size = size

    @property
    def size(self):
        '''property is the setter here that set the new value of size.'''
        return self.__size

    @size.setter
    def size(self, value):
        ''' Raising the error type.
        Args:
            value: the value of the size.

        Raises:
            TypeError: if the size isn't an integer.
            ValueError: if size is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        ''' area of this square
        Returns:
            the size of the squar. '''
        return self.__size ** 2

    def my_print(self):
        ''' print the square using #.
        it takes no args but it use self.area to check if the area isn't empty.
        And we use self.__size to get the size.
        '''
        sz = self.area()
        if sz == 0:
            print()
        else:
            for row in range(self.__size):
                print("#" * self.__size)
