#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_map = {"M": 1000,
                "D": 500,
                "C": 100,
                "L": 50,
                "X": 10,
                "V": 5,
                "I": 1
            }
    if not roman_string or type(roman_string) != str:
        return (0)
    prev = None
    current = None
    result = 0
    for letter in roman_string:
        current = roman_map[letter]
        if prev:
            if prev < current:
                result = current - prev
            elif prev >= current:
                result += current
        else:
            result += current
        prev = current
    return (result)
