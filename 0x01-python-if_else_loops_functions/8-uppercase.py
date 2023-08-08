#!/usr/bin/python3
def uppercase(str):
    for c in str:
        c_ascii = ord(c)
        if 97 <= c_ascii <= 122:
            c_upper = chr(c_ascii - 32)
        else:
            c_upper = c
        print(c_upper, end='')
    print()
