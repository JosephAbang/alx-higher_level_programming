#!/usr/bin/python3
"""module contains function that chevks if an object
is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """
    returns True if the object is exactly an instance
    of the class that inherited from the specified class
    """
    return isinstance(obj, a_class)
