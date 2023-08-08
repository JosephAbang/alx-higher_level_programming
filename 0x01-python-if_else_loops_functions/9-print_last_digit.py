#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    LastDigit = number % 10
    print('{0}'.format(LastDigit), end='')
    return (LastDigit)

print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
