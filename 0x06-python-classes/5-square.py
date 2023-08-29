#!/usr/bin/python3
"""Module defines classes"""


class Square:
    """Class defines a square"""
    __size = 0

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            count = self.__size
            i = 0
            j = 0
            while i < count:
                j = 0
                while j < count:
                    print("#", end='')
                    j += 1
                print()
                i += 1
