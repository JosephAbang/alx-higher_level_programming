#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for c in range(len(str)):
        c_ascii = ord(str[c])
        if c_ascii >= 97 and c_ascii < 123:
            new_str += chr(c_ascii - 32)
        else:
            new_str += str[c]
    print(new_str)
