#!/usr/bin/python3

import sys
import numpy as np

def execute(code):
    i = 0

    def get(n):
        if ((code[i] // 100) >> (n - 1)) & 1 is 0:
            return code[code[i + n]]
        return code[i + n]

    while True:
        op = code[i] % 100
        if op is 1:
            code[code[i + 3]] = get(1) + get(2)
            i += 4
        elif op is 2:
            code[code[i + 3]] = get(1) * get(2)
            i += 4
        elif op is 3:
            code[code[i + 1]] = int(input("Input:"))
            i += 2
        elif op is 4:
            print(get(1))
            i += 2
        elif op is 5:
            i = get(2) if get(1) else i + 3
        elif op is 6:
            i = get(2) if not get(1) else i + 3
        elif op is 7:
            code[code[i + 3]] = 1 if get(1) < get(2) else 0
            i += 4
        elif op is 8:
            code[code[i + 3]] = 1 if get(1) == get(2) else 0
            i += 4
        elif op is 99:
            exit()
        else:
            print("Error: Invalid Op: ", op)
            exit()

if __name__ == '__main__':
    if len(sys.argv) is not 2:
        print("Usage: ./01.py input")
        exit()
    execute([int(i) for i in np.genfromtxt(sys.argv[1], delimiter=',')])
