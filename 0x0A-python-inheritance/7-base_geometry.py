#!/usr/bin/python3
'''Module for BaseGeometry class.'''


class BaseGeometry:
    '''A BaseGeometry class.'''
    def area(self):
        ''' methode that raising an exception. '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' methode that check if the value is a positive number. '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
