#!/usr/bin/python3
"""Module contains function that writes to file"""


def write_file(filename="", text=""):
    """
    function writes a string to a text file (UTF8) and
    returns the number of characters written
    """

    with open(filename, mode="w", encoding="utf-8") as f:
        return (f.write(text))
