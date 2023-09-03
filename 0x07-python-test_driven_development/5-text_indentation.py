#!/usr/bin/python3
"""Module contains a function used to split texts"""


def text_indentation(text):
    """Function that prints a texts after these character ['.', '?', ':']"""

    if text is None:
        text = ""
    elif type(text) != str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] not in [".", "?", ":"]:
            print('{}'.format(text[i]), end='')
            i += 1
        else:
            print('{}'.format(text[i]))
            i += 1
            if i < len(text) and text[i] == ' ':
                i += 1
            print()
