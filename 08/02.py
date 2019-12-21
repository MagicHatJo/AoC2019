#!/usr/bin/python3

WIDTH = 25
HEIGHT = 6

def count_digits(layer, n):
	return sum(1 for y in layer for x in y if x == n)

def squash_layers(layers):
	image = [[2 for x in range(WIDTH)] for y in range(HEIGHT)]

	for layer in layers:
		for y in range(HEIGHT):
			for x in range(WIDTH):
				if image[y][x] == 2:
					image[y][x] = int(layer[y][x])
	return image

def print_image(image):
	for line in image:
		for n in line:
			if n == 1:
				print('*', end='')
			else:
				print(' ', end='')
		print()

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

	image = squash_layers(layers)
	print_image(image)