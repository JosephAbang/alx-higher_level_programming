#!/usr/bin/python3
"""Module contains a class named BAse"""


class Base:
    """base of all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects