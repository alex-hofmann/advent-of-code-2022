#!/usr/bin/env python3

import re
import sys


with open('input.txt', 'r') as f:
	data = f.read().split('\n\n')

stacks = data[0]# gave up; hardcoded
steps = data[1]

stacks_part_one = [
	list('LNWTD'), 
	list('CPH'), 
	list('WPHNDGMJ'), 
	list('CWSNTQL'), 
	list('PHCN'), 
	list('THNDMWQB'), 
	list('MBRJGSL'), 
	list('ZNWGVBRT'), 
	list('WGDNPL')
]

stacks_part_two = [
	list('LNWTD'), 
	list('CPH'), 
	list('WPHNDGMJ'), 
	list('CWSNTQL'), 
	list('PHCN'), 
	list('THNDMWQB'), 
	list('MBRJGSL'), 
	list('ZNWGVBRT'), 
	list('WGDNPL')
]

steps_tuples_list = \
	[tuple(map(int, re.findall(r"\d+", steps))) for steps in steps.strip().split("\n")]

for a,b,c in steps_tuples_list:
	for i in range(a):
		stacks_part_one[c-1].append(stacks_part_one[b-1].pop())

print(part_one := "".join(stack[-1] for stack in stacks_part_one))

for a,b,c in steps_tuples_list:
	stack_swp = []
	for i in range(a):
		stack_swp.append(stacks_part_two[b-1].pop())
	stack_swp.reverse()
	for j in stack_swp:
		stacks_part_two[c-1].append(j)

print(part_two := "".join(stack[-1] for stack in stacks_part_two))