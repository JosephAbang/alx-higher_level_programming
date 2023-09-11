#!/usr/bin/python3
"""module contains a class called base geometry"""


class BaseGeometry:
    """raise exceptions"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0 or value is None:
            raise ValueError("{} must be greater than 0".format(name))
