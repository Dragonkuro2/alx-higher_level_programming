#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    name = sys.argv[0]
    argnum = sys.argv[1:]
    S = 0
    length = len(sys.argv)
    for i in range(1, length):
        S += int(sys.argv[i])
    print(S)
