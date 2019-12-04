#!/usr/bin/python3

import sys
import numpy as np

def make_list(input):
    l = {}
    x, y, steps = 0, 0, 0
    for i in input:
        if i[0] == 'R':
            for k in range(0, int(i[1:])):
                if (x, y) not in l:
                    l[x, y] = steps
                x += 1
                steps +=1
        elif i[0] == 'L':
            for k in range(0, int(i[1:])):
                if (x, y) not in l:
                    l[x, y] = steps
                x -= 1
                steps += 1
        elif i[0] == 'U':
            for k in range(0, int(i[1:])):
                if (x, y) not in l:
                    l[x, y] = steps
                y -= 1
                steps += 1
        elif i[0] == 'D':
            for k in range(0, int(i[1:])):
                if (x, y) not in l:
                    l[x, y] = steps
                y += 1
                steps += 1
        else:
            print("Error")
            return
    return l

def get_manhattan_distance(x, y):
    return abs(x) + abs(y)

def main():
    if len(sys.argv) is not 2:
        print("Usage: ./01.py input")
    with open(sys.argv[1]) as f:
        manh = []
        l1 = make_list(f.readline().split(','))
        l2 = make_list(f.readline().split(','))
        for t in l1:
            if t in l2:
                manh.append(l1[t] + l2[t])
        manh.remove(0)
        print(min(manh))
    return

main()
