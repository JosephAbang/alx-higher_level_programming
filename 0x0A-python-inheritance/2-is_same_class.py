#!/usr/bin/python3
"""module contains function that chevks if an object
is an instance of a class"""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an instance of the specified class
    """
    return type(obj) is a_class
