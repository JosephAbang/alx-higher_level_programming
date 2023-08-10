#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    total = 0
    for arg in range(1, argc):
        total += int(argv[arg])
    print(total)
