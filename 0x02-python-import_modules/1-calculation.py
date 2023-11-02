#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print(f"10 + 5 = {add(a, b):d}")
    print(f"10 - 5 = {sub(a, b):d}")
    print(f"10 * 5 = {mul(a, b):d}")
    print(f"10 / 5 = {div(a, b):d}")
