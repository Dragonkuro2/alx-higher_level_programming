#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) == 0:
            print()
        i = 1
        for element in row:
            if i < len(row):
                print("{:d} ".format(element), end="")
            else:
                print("{:d}".format(element))
            i += 1
