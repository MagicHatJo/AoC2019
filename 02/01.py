#!/usr/bin/python3

import sys
import numpy as np

def main():
    if len(sys.argv) is not 2:
        print("Usage: ./01.py input")
        return
    code = [int(i) for i in np.genfromtxt(sys.argv[1], delimiter=',')]
    code[1] = 12
    code[2] = 2
    length = len(code)
    i = 0
    while i < length and code[i] is not 99:
        if code[i] is 1:
            code[code[i + 3]] = code[code[i + 1]] + code[code[i + 2]]
        elif code[i] is 2:
            code[code[i + 3]] = code[code[i + 1]] * code[code[i + 2]]
        else:
            print("Error")
            return
        i += 4
    print(code[0])

main()
