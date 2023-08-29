#!/usr/bin/python3
def safe_print_division(a, b):
    res = 0
    try:
        res = a / b
    except Exception:
        res = None
        pass
    finally:
        if res is not None:
            print("Inside result: {}".format(res))
        else:
            print("Inside result: {}".format(res))
        return res
