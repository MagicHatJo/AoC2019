#!/usr/bin/python3
import sys


def main():
    if len(sys.argv) is not 2:
        print("Usage: ./fuelsum [input_file]")
    total = 0
    with open(sys.argv[1]) as file:
        for line in file:
            total += int(line) // 3 - 2
    print(total)

main()
