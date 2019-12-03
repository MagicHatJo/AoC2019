#!/usr/bin/python3

import sys
import numpy as np
from copy import deepcopy

def calculate(code):
    i = 0
    length = len(code)
    while i < length and code[i] is not 99:
        if code[i] is 1:
            code[code[i + 3]] = code[code[i + 1]] + code[code[i + 2]]
        elif code[i] is 2:
            code[code[i + 3]] = code[code[i + 1]] * code[code[i + 2]]
        else:
            return 0
        i += 4
    return code[0]

def main():
    if len(sys.argv) is not 3:
        print("Usage: ./01.py input [expected output]")
        return
    code = [int(i) for i in np.genfromtxt(sys.argv[1], delimiter=',')]
    for n in range(0, 100):
        for v in range(0, 100):
            code[1] = n
            code[2] = v
            if int(calculate(deepcopy(code))) == int(sys.argv[2]):
                print(100 * n + v)
                return
    print("Error")
    return

main()
