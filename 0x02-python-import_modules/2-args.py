#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    name = sys.argv[0]
    arguments = sys.argv[1:]
    numarg = len(sys.argv)
    print(f"{numarg - 1} arguments:")
    for i in range(1, numarg):
        print(f"{numarg}: {sys.argv[i]}")
