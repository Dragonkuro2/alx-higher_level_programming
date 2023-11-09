#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total = 0
    weight = 0
    for score, value in my_list:
        total += score * value
        weight += value
    return total/weight
