#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
check = 0
if number < 0:
    number *= -1
    check = 1
last_digit = number % 10
if check == 1:
    number *= -1

if last_digit > 5:
    string = "and is greater than 5"
elif last_digit == 0:
    string = "and is 0"
else:
    string = "and is less than 6 and not 0"
print(f"Last digit of {number:d} is {last_digit:d} {string}")
