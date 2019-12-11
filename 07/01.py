#!/usr/bin/python3

import sys
import itertools
import numpy as np

def execute(code, phase_setting, input_signal):
    i = 0

    def get(n):
        if ((code[i] // 100) >> (n - 1)) & 1 is 0:
            return code[code[i + n]]
        return code[i + n]

    used_phase = False
    while True:
        op = code[i] % 100
        if op is 1:
            code[code[i + 3]] = get(1) + get(2)
            i += 4
        elif op is 2:
            code[code[i + 3]] = get(1) * get(2)
            i += 4
        elif op is 3:
            code[code[i + 1]] = phase_setting if not used_phase else input_signal
            used_phase = True
            i += 2
        elif op is 4:
            return get(1)
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
            return None
        else:
            print("Error: Invalid Op: ", op)
            exit()

def calculate_permutation(mem, permutation):
    signal = 0
    for num in permutation:
        signal = execute(mem, num, signal)
    return signal

if __name__ == '__main__':
    if len(sys.argv) is not 2:
        print("Usage: ./01.py input")
        exit()

    code = [int(i) for i in np.genfromtxt(sys.argv[1], delimiter=',')]
    print(max([calculate_permutation(code, permutation) for permutation in itertools.permutations([0, 1, 2, 3, 4])]))

