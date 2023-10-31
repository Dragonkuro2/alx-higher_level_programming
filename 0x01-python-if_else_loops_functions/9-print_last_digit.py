#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number *= -1
    if number < 10:
        last_d = number
        print(last_d, end="")
        return last_d
    else:
        last_d = number % 10
    print(last_d, end="")
    return last_d
