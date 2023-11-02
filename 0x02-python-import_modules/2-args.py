#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    name = sys.argv[0]
    arguments = sys.argv[1:]
    numarg = len(sys.argv)
    if numarg == 1:
        print(f"{numarg - 1} arguments.")
    else:
        print(f"{numarg - 1} argument", end="")
        if numarg > 2:
            print("s", end="")
        print(":")
        for i in range(1, numarg):
            print(f"{i}: {sys.argv[i]}")
