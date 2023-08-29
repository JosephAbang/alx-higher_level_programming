#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        try:
            int(value)
            print("Exception: Unknown format code 'd' for object of type '{}'\
                    ".format(value.__class__.__name__), file=sys.stderr)
            return False
        except (ValueError, TypeError):
            print("Exception: unsupported format string passed to str.__format__", file=sys.stderr)
            return False
