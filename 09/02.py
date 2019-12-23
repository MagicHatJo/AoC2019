#!/usr/bin/python3

import sys
import itertools
import numpy as np

from collections import deque
from Intcode import Intcode, InputInterrupt, OutputInterrupt

if __name__ == '__main__':
    if len(sys.argv) is not 2:
        print("Usage: ./02.py input")
        exit()

    code = [int(i) for i in np.genfromtxt(sys.argv[1], delimiter=',')]
    vm = Intcode(code, 2)
    while not vm.complete:
            try:
                vm.run()
            except(OutputInterrupt):
                vm.input_queue.append(vm.output_queue)
                continue
            except(InputInterrupt):
                break