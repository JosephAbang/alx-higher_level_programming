#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        int_val = int(value)
        print("{:d}".format(int_val))
        return True
    except ValueError:
        print("Exception: Unknown format code 'd' for object of type '{}'\
                ".format(value.__class__.__name__), file=sys.stderr)
        return False
    except TypeError:
        print("Exception: unsupported format string passed to \
                {}.__format__".format(value.__class__.__name__), file=sys.stderr)
        return False
