#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = 0
    prev = 0

    for x in reversed(roman_string):
        val = rom_n.get(x, 0)
        if val < prev:
            n -= val
        else:
            n += val
        prev = val

    if 1 <= n <= 3999:
        return n
    else:
        return 0
