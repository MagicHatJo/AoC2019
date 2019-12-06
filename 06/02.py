#!/usr/bin/python3

import sys
import networkx as nx

if __name__ == '__main__':
    if len(sys.argv) is not 2:
        print("Usage: ./01.py input")
        exit()
    with open(sys.argv[1], 'r') as f:
        parents = dict(reversed(orbit.split(')')) for orbit in f.read().splitlines())
        ancestors = lambda x: ancestors(parents[x]).union([parents[x]]) if x in parents else set()
        print(len(ancestors('YOU') ^ ancestors('SAN')))
