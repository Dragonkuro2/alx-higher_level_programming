#!/usr/bin/python3
''' square.py '''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' square class. '''
    def __init__(self, size, x=0, y=0, id=None):
        ''' initialize the size and x, y and the id. '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        ''' overwrite the str methode. '''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    @property
    def size(self):
        ''' size of the square. '''
        return self.height

    @size.setter
    def size(self, value):
        ''' setter of width and height. '''
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''Internal method that updates instance attributes via */**args.'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Updates instance attributes via no-keyword & keyword args.'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Returns dictionary representation of this class.'''
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
