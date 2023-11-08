#!/usr/bin/python3

def uniq_add(my_list=[]):
    res = 0
    my_list2 = my_list[:]
    tab = []
    for i in range(len(my_list2)):
        if my_list2[i] not in tab:
            tab.append(my_list2[i])
            res += my_list2[i]
    return res
