
from collections import deque

class InputInterrupt(Exception):
    pass

class OutputInterrupt(Exception):
    pass

class Intcode:

    def get_value(self, n):
        op = self.mem[self.ptr] // (10 ** (n + 1)) % 10
        if op == 0:
            return self.mem[self.mem[self.ptr + n]]
        elif op == 1:
            return self.mem[self.ptr + n]
        elif op == 2:
            return self.mem[self.rbase + self.mem[self.ptr + n]]

    def get_index(self, n):
        op = self.mem[self.ptr] // (10 ** (n + 1)) % 10
        if op == 0:
            return self.mem[self.ptr + n]
        elif op == 1:
            return self.ptr + n
        elif op == 2:
            return self.rbase + self.mem[self.ptr + n]

    def d_add(self):
        self.mem[self.get_index(3)] = self.get_value(1) + self.get_value(2)
        self.ptr += 4
    
    def d_multiply(self):
        self.mem[self.get_index(3)] = self.get_value(1) * self.get_value(2)
        self.ptr += 4
    
    def d_input(self):
        try:
            self.mem[self.get_index(1)] = self.input_queue.popleft()
        except(IndexError):
            raise InputInterrupt
        else:
            self.ptr += 2
    
    def d_output(self):
        self.output_queue.append(self.get_value(1))
        print(self.output_queue[-1])
        self.ptr += 2
        raise OutputInterrupt
    
    def d_jump(self):
        self.ptr = self.get_value(2) if self.get_value(1) else self.ptr + 3
    
    def d_fjump(self):
        self.ptr = self.get_value(2) if not self.get_value(1) else self.ptr + 3
    
    def d_less(self):
        self.mem[self.get_index(3)] = int(self.get_value(1) < self.get_value(2))
        self.ptr += 4
    
    def d_equal(self):
        self.mem[self.get_index(3)] = int(self.get_value(1) == self.get_value(2))
        self.ptr += 4

    def d_relative(self):
        self.rbase += self.get_value(1)
        self.ptr += 2

    def d_exit(self):
        self.complete = True

    def __init__(self, program, phase_setting):
        self.ops = {   
            1: self.d_add,
            2: self.d_multiply,
            3: self.d_input,
            4: self.d_output,
            5: self.d_jump,
            6: self.d_fjump,
            7: self.d_less,
            8: self.d_equal,
            9: self.d_relative,
            99:self.d_exit,
        }
        self.mem = program
        self.mem.extend([0 for i in range(100000000)])
        self.ptr = 0
        self.input_queue = deque()
        self.input_queue.append(phase_setting)
        self.output_queue = deque()
        self.complete = False
        self.rbase = 0

    def run(self):
        while not self.complete:
            self.ops[self.mem[self.ptr] % 100]()
