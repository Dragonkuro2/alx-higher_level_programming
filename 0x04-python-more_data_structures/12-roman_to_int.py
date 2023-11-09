#!/usr/bin/python3
def roman_to_int(roman_string):
    mylist = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if (type(roman_string) is not str) or (roman_string is None):
        return 0
    else:
        total = 0
        numb1 = 0
        numb2 = 0
        for idx in reversed(roman_string):
            numb1 = mylist[idx]
            total += numb1 if numb1 >= numb2 else -numb1
            numb2 = numb1
    return total
