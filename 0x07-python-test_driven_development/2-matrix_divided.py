#!/usr/bin/python3


def matrix_divided(matrix, div):
    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)

    _len = 0
    msg_size = "Each row of the matrix must have the same size"

    for elem in matrix:
        if not elem or not isinstance(elem, list):
            raise TypeError(msg_type)

        if _len != 0 and len(elem) != _len:
            raise TypeError(msg_size)

        for num in elem:
            if not type(num) in (int, float):
                raise TypeError(msg_type)

        _len = len(elem)

    result = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return result
