#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    argc = len(argv) - 1
    if argc != 3:
        print(f'{argv[0]} <a> <operator> <b>')
        exit(1)
    _op = {"+": add, "-": sub, "*": mul, "/": div}
    if argv[2] not in _op.keys():
        print(f'Unknown operator. Available operators: +, -, * and /')
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    res = _op[argv[2]](a, b)
    print(f'{argv[1]} {argv[2]} {argv[3]} = {res}')
