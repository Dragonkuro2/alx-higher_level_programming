#!/usr/bin/python3
""" This module is for the class MyList. """


class MyList(list):
    """ This class define a methode that sort a list. """
    def print_sorted(self):
        """ This method print the sorted list. """
        print(sorted(self))
