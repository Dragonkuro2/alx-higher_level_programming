#!/usr/bin/python3
''' A square module. '''


class Square:
    ''' the square class. '''

    def __init__(self, size=0, position=(0, 0)):
        ''' initializes size and position. '''
        self.position = position
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
            if self.__position[1] > 0:
                print('\n' * self.__position[1], end='')
            for row in range(self.__size):
                print(' ' * self.__position[0], end='')
                print("#" * self.__size)

    @property
    def position(self):
        ''' property that define the getter.'''
        return self.__position

    @position.setter
    def position(self, value):
        ''' setter of property position.
        Args:
            value: must be a tuple of two integres.

        Raises:
            TypeError: if the tuple hasn't 2 two positive integers.
        '''

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(itm, int) or itm >= 0 for itm in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
