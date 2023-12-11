#!/bin/bash
''' base.py module file. '''


class Base:
    ''' base class that have init methode. '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' initialize the id. '''
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
