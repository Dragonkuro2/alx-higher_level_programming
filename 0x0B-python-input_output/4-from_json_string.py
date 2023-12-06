#!/usr/bin/python3
''' this module is for the fonction from_json_string. '''


import json


def from_json_string(my_str):
    ''' this function returns an object represented by json. '''
    return json.loads(my_str)
