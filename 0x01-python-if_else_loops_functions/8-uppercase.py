#!/usr/bin/python
def uppercase(str):
    for char in str:
        ascii_code = ord(char)
        if 97 <= ascii_code <= 122:
            upper_char = chr(ascii_code - 32)
        else:
            upper_char = char
        print(upper_char, end='')
    print()
