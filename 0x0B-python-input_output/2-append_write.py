#!/usr/bin/python3
"""Module contains a file append function"""


def append_write(filename="", text=""):
    """
    function that appends to a text file (UTF8) and
    returns the number of characters added
    """

    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
