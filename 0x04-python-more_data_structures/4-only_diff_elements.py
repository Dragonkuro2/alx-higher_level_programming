#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    # the ^ is just like if we wrote set1.symmetric_difference(set2)
    # and it mean just like NAND
    set_3 = set_1 ^ set_2
    return set_3
