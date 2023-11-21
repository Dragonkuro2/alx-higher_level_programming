#!/usr/bin/python3
''' A class that named Square that will createa private attribute.'''


class Sqaure:
    ''' A class represent a square. '''

    def __init__(self, size):
        ''' initialize a square instance.

            Arguments:
          --------------
        size (int): the size of square. '''

        self.__size = size
