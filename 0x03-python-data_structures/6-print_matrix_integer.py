#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) == 0:
            print()
        i = 1
        for element in row:
            if i < len(row):
                print("{} ".format(element), end="")
            else:
                print("{}".format(element))
            i += 1
