#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(args[0], args[1])
    except IndexError:
        print("Exception: list index out of range", file=sys.stderr)
        result = None
        pass
    except ZeroDivisionError:
        print("Exception: division by zero", file=sys.stderr)
        result = None
        pass
    return result
