#!/usr/bin/python3
def safe_print_integer(value):
    retbool = False
    try:
        print(("{:d}".format(value)))
        retbool = True
    except (IndexError, ValueError):
        pass
    return retbool
