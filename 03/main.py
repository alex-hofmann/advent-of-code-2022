#!/usr/bin/env python3

import math
from string import ascii_letters

data = open('input.txt','r').read().rstrip().split()

part_one = 0
for line in data:
	a, b = line[:math.floor(len(line)/2)], line[-math.floor(len(line)/2):]
	intersect = (set(a) & set(b)).pop()
	part_one += ascii_letters.index(intersect) + 1


part_two = 0
for a, b, c in zip(data[::3], data[1::3], data[2::3]):
	intersect = (set(a) & set(b) & set(c)).pop()
	part_two += ascii_letters.index(intersect) + 1

print(part_one, part_two)