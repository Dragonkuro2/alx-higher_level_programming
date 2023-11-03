#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    if len1 < 2:
        for i in range(len1, 3):
            tuple_a += (0,)
    if len2 < 2:
        for i in range(len2, 3):
            tuple_b += (0,)
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_tuple
