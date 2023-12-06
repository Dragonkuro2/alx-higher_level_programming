#!/usr/bin/python3
''' this module is for the fonction append_write. '''


def append_write(filename="", text=""):
    ''' function that append a text at the end of the input file. '''
    with open(filename, "a", encoding='utf-8') as data:
        data.write(text)
        return len(text)
