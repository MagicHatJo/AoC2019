#!/usr/bin/python3

MIN = 152085
MAX = 670283

def valid_number(n):
    current = 0
    for i in str(n):
        if int(i) < current:
            return False
        current = int(i)
    return True

def has_double(n):
    prev = 10
    m = [0] * 10
    for i in str(n):
        m[int(i)] += 1
    if 2 in m:
        return True
    return False

if __name__ == '__main__':
    count = 0
    i = MIN
    while i <= MAX:
        if valid_number(i) and has_double(i):
            count += 1
        i += 1
    print(count)
