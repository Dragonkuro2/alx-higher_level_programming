#!/usr/bin/python3
'''Module for BaseGeometry class.'''


class BaseGeometry:
    '''A BaseGeometry class.'''
    def area(self):
        ''' methode that raising an exception. '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' this methode is checking if the value is integer and >0. '''
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")


class Rectangle(BaseGeometry):
    ''' This class inherits from the class BaseGeometry. '''
    def __init__(self, width, height):
        ''' This methode sets the width and the height to be private. '''
        if self.integer_validator(width, height):
            self.__width = width
            self.__height = height
