#!/usr/bin/python3
'''Module for the method is_same_class.'''


def is_same_class(obj, a_class):
    '''Determines if an object is an instance of a class.'''
    return type(obj) == a_class
