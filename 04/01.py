#!/usr/bin/python3

MIN = 152085
MAX = 670283

def is_valid(n):
    current = 0
    m = [0] * 10
    for i in str(n):
        if int(i) < current:
            return False
        current = int(i)
        m[int(i)] += 1
    if all(x < 2 for x in m):
        return False
    return True

if __name__ == '__main__':
    print(len([x for x in range(MIN, MAX) if is_valid(x)]))
