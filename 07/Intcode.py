
from queue import Queue

class Intcode:

    def get(self, n):
        if ((self.mem[self.ptr] // 100) >> (n - 1)) & 1 is 0:
            return self.mem[self.mem[self.ptr + n]]
        return self.mem[self.ptr + n]

    def d_add(self):
        self.mem[self.mem[self.ptr + 3]] = get(1) + get(2)
        self.ptr += 4
    
    def d_multiply(self):
        self.mem[self.mem[self.ptr + 3]] = get(1) * get(2)
        self.ptr += 4
    
    def d_input(self):
        self.mem[self.mem[self.ptr + 1]] = input_queue.get()
        self.ptr += 2
    
    def d_output(self):
        self.output_queue.put(get(1))
        self.ptr += 2
    
    def d_jump(self):
        self.ptr = get(2) if get(1) else self.ptr + 3
    
    def d_fjump(self):
        self.ptr = get(2) if not get(1) else self.ptr + 3
    
    def d_less(self):
        self.mem[self.mem[self.ptr + 3]] = int(get(1) < get(2))
        self.ptr += 4
    
    def d_equal(self):
        self.mem[self.mem[self.ptr + 3]] = int(get(1) == get(2))
        self.ptr += 4

    def d_exit(self):
        self.complete = True

    def __init__(self, program, phase_setting):
        self.ops = {   
            1: self.d_add,
            2: self.d_multply,
            3: self.d_input,
            4: self.d_output,
            5: self.d_jump,
            6: self.d_fjump,
            7: self.d_less,
            8: self.d_equal,
            99:self.d_exit,
        }
        self.mem = program
        self.ptr = 0
        self.input_queue = Queue()
        self.input_queue.append(phase_setting)
        self.output_queue = Queue()
        self.complete = False
