def uppercase(str):
    for c in str:
        c_ascii = ord(c)
        if c_ascii >= 97 and c_ascii < 123:
            c_upper = chr(c_ascii - 32)
        else:
            c_upper = c
        print(c_upper, end='')
    print()
