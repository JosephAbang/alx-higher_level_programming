#!/usr/bin/python3
def uppercase(str):
    result = ''
    for c in range(len(str)):
        c_ascii = ord(str[c])
        if c_ascii >= 97 and c_ascii < 123:
            c_upper = chr(c_ascii - 32)
        else:
            c_upper = str[c]

        result += c_upper
    print(result)
