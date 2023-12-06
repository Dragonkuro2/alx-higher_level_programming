#!/usr/bin/python3
''' this module is for the function save_to_json_file. '''


import json


def save_to_json_file(my_obj, filename):
    ''' function that writes an object usin json representation in a file. '''
    with open(filename, "w") as data:
        data.write(json.dumps(my_obj))
