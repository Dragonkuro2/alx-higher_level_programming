#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for idx in range(x):
            print(my_list[idx], end="")
        print()
    except IndexError:
        print("the number of element that you enter doesn't exist in the list")
    except:
        print("An unknown Error occured")
