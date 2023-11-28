#!/usr/bin/python3
""" Module for the methode matrix_divided. """


def matrix_divided(matrix, div):
    """Divides all elements of the input matrix by the input div.

    Args:
        matrix: List of lists of int or float
        div: number to divide matrix by

    Returns:
        list: List of lists representing divided matrix.

    Raises:
        TypeError: If matrix is not list of lists and containing int or float.
        TypeError: If sublists are not with the same size.
        TypeError: If div is not int or float.
        ZeroDivisionError: If div equale zero.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(element / div, 2) for element in row] for row in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
