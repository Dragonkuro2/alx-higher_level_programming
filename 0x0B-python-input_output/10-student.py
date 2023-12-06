#!/usr/bin/python3
''' the file  9-student.py Module. '''


class Student:
    ''' This class has two methodes init and to_json. '''
    def __init__(self, first_name, last_name, age):
        ''' initialize the public instances first_name, last_name, age. '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' retrieves a dictionary representation of a Student instance. '''
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__self
        mydict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                mydict[key] = value
        return mydict
