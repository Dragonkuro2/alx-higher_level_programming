#!/usr/bin/python3
''' Module of the file 0-read_file.py that include the function raed_file. '''


def read_file(filename=""):
    ''' this function read and print the content of the input file. '''
    with open(filename, "r", encoding="utf-8") as data:
        print(data.read(), end="")
