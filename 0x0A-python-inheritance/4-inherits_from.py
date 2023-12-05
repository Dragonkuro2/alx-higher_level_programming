#!/usr/bin/python3
""" This is the module of the function inherits_from. """


def inherits_from(obj, a_class):
    """ function that returns True if the object is an instance
        of a class that inherited. """
    return isinstance(obj, a_class) and type(obj) is not a_class
