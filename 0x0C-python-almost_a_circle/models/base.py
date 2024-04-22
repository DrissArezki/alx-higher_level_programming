#!usr/bin/python3
'''Module for the base class'''


class Base:
    '''Representing the base of the hierarchy.'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Construction.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
