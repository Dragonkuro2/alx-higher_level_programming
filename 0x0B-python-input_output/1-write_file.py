#!/usr/bin/python3
''' This is the module of the file 1-write_file.py
    that contient the function write_file. '''


def write_file(filename="", text=""):
    ''' this function write the input text in a file with the input file name.'''
    with open(filename, "w", encoding='utf-8') as data:
        data.write(text)
        return len(text)
