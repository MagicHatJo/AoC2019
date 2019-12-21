#!/usr/bin/python3

WIDTH = 25
HEIGHT = 6

def count_digits(layer, n):
	return sum(1 for y in layer for x in y if x == n)

if __name__ == "__main__":
	layers = []
	with open("input") as f:
		base = f.read()
		lines = [base[i:i + WIDTH] for i in range(0, len(base), WIDTH)]
		layer = []
		for i in range(len(lines)):
			layer.append(lines[i])
			if (i + 1) % HEIGHT == 0:
				layers.append(layer.copy())
				layer.clear()

	_, min_layer = min((count_digits(layer, '0'), layer) for layer in layers)
	print(count_digits(min_layer, '1') * count_digits(min_layer, '2'))
