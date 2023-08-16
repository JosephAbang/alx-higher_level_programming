#!/usr/bin/python3
def roman_to_int(roman_string):
    numeral_dict = \
            {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    str_rev = list(reversed(roman_string))
    result = 0
    prev_value = 0

    for idx in range(len(str_rev)):
        key = str_rev[idx]
        if str_rev[idx] in numeral_dict.keys():
            if numeral_dict[key] >= prev_value:
                result += numeral_dict[key]
            else:
                result -= numeral_dict[key]
            prev_value = numeral_dict[key]
    return result
