#!/usr/bin/python3
'''Module for the base class'''
from json import dumps, loads


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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Don't be afraid of J(a)son xD.'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Saves jasonfied object to a file.'''
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("().json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))
