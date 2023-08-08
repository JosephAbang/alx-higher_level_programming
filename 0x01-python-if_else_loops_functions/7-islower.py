#!/usr/bin/python3
def islower(c):
    _ascii = ord(c)
    if _ascii >= 95 and _ascii < 123:
        return True
    else:
        return False
