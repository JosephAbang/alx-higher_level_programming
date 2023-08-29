#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        print("Exception: Unknown format code 'd' for object of type '{}'\
".format(value.__class__.__name__), file=sys.stderr)
        return False
    except Exception:
        print("Exception: unsupported format string passed to {}.__format__\
".format(value.__class__.__name__), file=sys.stderr)
        return False


value = '89'
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))
