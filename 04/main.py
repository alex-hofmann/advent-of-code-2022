#!/usr/bin/env python3

import re

with open('input.txt', 'r') as f:
    data = f.read().split('\n')

part_one = part_two = 0

for line in data:

	numbers_list = list(map(int, re.findall('\d+', line)))

	a = set(range(numbers_list[0], numbers_list[1]+1))

	b = set(range(numbers_list[2], numbers_list[3]+1))

	# print(f"a:\n{a}\nb:\n{b}\n")

	if a <= b or b <= a:
		part_one += 1
	
	if a & b:
		part_two += 1

print(part_one, part_two)
