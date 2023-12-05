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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    ''' This class inherits from the class BaseGeometry. '''
    def __init__(self, width, height):
        ''' This methode sets the width and the height to be private. '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
