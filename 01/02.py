#!/usr/bin/python3
import sys

def get_fuel_sum(num):
    current = num // 3 - 2
    if current >= 0:
        return current + get_fuel_sum(current)
    return 0

def main():
    if len(sys.argv) is not 2:
        print("Usage: ./fuelsum [input_file]")
    total = 0
    with open(sys.argv[1]) as file:
        for line in file:
            total += get_fuel_sum(int(line))
    print(total)

main()
