#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        num = 0
        for idx in range(x):
            print(my_list[idx], end="")
            num += 1
    except IndexError:
        None
    print()
    return(num)
