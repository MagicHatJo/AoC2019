#!/usr/bin/python3

import sys
import numpy as np

def make_list(input):
    l = []
    x, y = 0, 0
    for i in input:
        if i[0] == 'R':
            for k in range(0, int(i[1:])):
                l.append((x, y))
                x += 1
        elif i[0] == 'L':
            for k in range(0, int(i[1:])):
                l.append((x, y))
                x -= 1
        elif i[0] == 'U':
            for k in range(0, int(i[1:])):
                l.append((x, y))
                y -= 1
        elif i[0] == 'D':
            for k in range(0, int(i[1:])):
                l.append((x, y))
                y += 1
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
        l = set(make_list(f.readline().split(','))).intersection(make_list(f.readline().split(',')))
        for s in l:
            manh.append(get_manhattan_distance(s[0], s[1]))
        manh.remove(0)
        print(min(manh))
    return

main()
