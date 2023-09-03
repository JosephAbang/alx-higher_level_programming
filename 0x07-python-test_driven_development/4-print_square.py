#!/usr/bin/python3
"""Module that prints squares"""


def print_square(size):
    """print a square with character #"""

    if type(size) not in [int, float]:
        raise TypeError("size must be an integer")
    elif type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
