#!/usr/bin/python3

import sys
import itertools
import numpy as np

import Intcode

def calculate_permutation(mem, permutation):
    vm = []
    for phase_setting in permutation:
        vm.append(Intcode(mem, phase_setting))
    vm[0].input_queue.append(0)

    i = -1
    while not all(map(lambda x: x.complete, vm)):
        i = (i + 1) % 5
        while not vm[i].complete:
            vm[i].run()
            vm[(i + 1) % 5].input_queue.append(vm[i].output_queue.get())
    return vm[0].input_queue.get()

if __name__ == '__main__':
    if len(sys.argv) is not 2:
        print("Usage: ./02.py input")
        exit()

    code = [int(i) for i in np.genfromtxt(sys.argv[1], delimiter=',')]
    print(max([calculate_permutation(code, permutation) for permutation in itertools.permutations([5, 6, 7, 8, 9])]))


    sequences = itertools.permutations([5, 6, 7, 8, 9])
    print(max(sequences, key = lambda x: calulate_permutation(code, x)))