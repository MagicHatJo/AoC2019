#!/usr/bin/python

import sys
import itertools
import numpy as np

from collections import deque
from Intcode import Intcode, InputInterrupt, OutputInterrupt

def calculate_permutation(mem, permutation):
    vm = []
    for phase_setting in permutation:
        vm.append(Intcode(mem, phase_setting))
    vm[0].input_queue.append(0)

    i = -1
    while not all(map(lambda x: x.complete, vm)):
        i = (i + 1) % 5
        while not vm[i].complete:
            try:
                vm[i].run()
            except(OutputInterrupt):
                vm[(i + 1) % 5].input_queue.append(vm[i].output_queue[-1])
                continue
            except(InputInterrupt):
                break
    return vm[0].input_queue[-1]

if __name__ == '__main__':
    if len(sys.argv) is not 2:
        print("Usage: ./02.py input")
        exit()

    code = [int(i) for i in np.genfromtxt(sys.argv[1], delimiter=',')]
    sequences = itertools.permutations([5, 6, 7, 8, 9])
    best = max(sequences, key = lambda x: calculate_permutation(code, x))
    print(calculate_permutation(code, best))