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
