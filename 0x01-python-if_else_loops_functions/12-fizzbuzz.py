#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz ", end="")
            pass
        elif num % 3 == 0:
            print("Fizz ", end="")
            pass
        elif num % 5 == 0:
            print("Buzz ", end="")
            pass
        else:
            print(f"{num:d} ", end="")
    print("")
