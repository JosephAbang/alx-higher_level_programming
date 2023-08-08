#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    LastDigit = number % 10
    print('{0}'.format(LastDigit), end='')
    return (LastDigit)
