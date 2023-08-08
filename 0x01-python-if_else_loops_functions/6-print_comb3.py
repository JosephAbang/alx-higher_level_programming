#!/usr/bin/python3
for num in range(100):
    num1 = num // 10
    num2 = num % 10
    if num == 89:
        print(f'{num}')
    elif num1 < num2:
        print(f'{num1}{num2}, ', end='')

