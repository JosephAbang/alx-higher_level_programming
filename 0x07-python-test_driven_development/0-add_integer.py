#!/usr/bin/python3
"""Module contains function that adds two integers"""


def add_integer(a, b=98):
    """add two integers"""

    if a == None:
        a = 0
    elif type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
