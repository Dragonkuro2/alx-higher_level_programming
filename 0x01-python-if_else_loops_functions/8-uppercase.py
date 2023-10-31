#!/usr/bin/python3
def uppercase(str):
    for num in str:
        c = num
        if ord(num) >= ord('a') and ord(num) <= ord('z'):
            c = chr(ord(num) - 32)

        print("{:s}".format(c), end="")
    print("")
