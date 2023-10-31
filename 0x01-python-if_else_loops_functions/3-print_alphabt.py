#!/usr/bin/python3
for char in range(ord('a'), ord('z') + 1):
    char = chr(char)
    if char != 'q' and char != 'e':
        print("{:s}".format(char), end="")
