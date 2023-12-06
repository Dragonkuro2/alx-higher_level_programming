#!/usr/bin/python3
''' this modue for the function load_from_json_file. '''


import json


def load_from_json_file(filename):
    ''' this function create an object from a json file. '''
    with open(filename, "r") as data:
        return json.load(data)
