#!/usr/bin/python3
# this function make the sqaure of the matrix
def square_matrix_simple(matrix=[]):
    # this line is to copy the matrix to an other one
    matrix2 = [row[:] for row in matrix]
    for i in range(len(matrix2)):
        for j in range(len(matrix2[i])):
            matrix2[i][j] = matrix2[i][j] ** 2
    return matrix2
