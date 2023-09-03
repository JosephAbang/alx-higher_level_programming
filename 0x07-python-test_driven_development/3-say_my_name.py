#!/usr/bin/python3
"""Module contains functionjs that prints strings"""


def say_my_name(first_name, last_name=""):
    """Function prints the full name"""

    if first_name is None:
        first_name = ""
    elif type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    print(f'My name is {first_name} {last_name}')
