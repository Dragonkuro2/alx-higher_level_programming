#!/usr/bin/python3
""" This module contain a function named add_intege
    that return the sum of two integers """


def add_integer(a, b=98):
    """ This function takes two arguments 'a' and 'b'.
    it sets the argument 'b' to 98 if it was blank.
    this function returns the sum of the two arguments.
    Args:
        a (int): the first argument
        b (int): the second arguemnt that will initialize
                    by default to 98 if b was empty.

    Return:
        the sum of the two arguments as integers if it worked.

    Raises:
        TypeError: (arguement) must be an integer"
        """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
