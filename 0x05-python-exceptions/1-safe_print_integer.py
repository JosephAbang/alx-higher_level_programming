#!/usr/bin/python3
def safe_print_integer(value):
    ret_bool = False
    try:
        print(("{:d}".format(), value))
        retbool = True
    except IndexError:
        pass
    return ret_bool
