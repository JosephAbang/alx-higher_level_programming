#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        print("Exception: Unknown format code 'd' for object of type 'str'\n", file=sys.stderr)
        return False
    return True
