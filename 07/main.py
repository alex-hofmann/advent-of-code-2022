#!/usr/bin/env python3

import re
from collections import defaultdict
from itertools import accumulate


with open('input.txt', 'r') as f:
	data = f.readlines()

dirs = defaultdict(int)
part_one = 0
part_two = 70000000

re_cd_x = re.compile(r'^\$.+cd.+?(\w+)')
re_cd_up = re.compile(r'^\$.+cd.+\.\.')
re_cd_root = re.compile(r'^\$.+cd.+\/')
re_dir = re.compile(r'^dir\s.+')
re_ls = re.compile(r'^$.+ls')
re_size = re.compile(r'^\d+')

for line in data:
	if re_cd_up.match(line):
		curr.pop()

	elif re_cd_x.match(line):
		print(line)
		curr.append(f"{re_cd_x.search(line)[1]}/")

	elif re_cd_root.match(line):
		curr = ['/'] 

	elif re_ls.match(line):
		pass

	elif re_dir.match(line):
		pass

	elif re_size.match(line):
		for i in accumulate(curr):
			dirs[i] += int(re_size.findall(line)[0])

print(dirs)
for i in dirs.values():
	if i <= 100000:
		part_one += i

	if i >= dirs['/'] - 40000000 and i < part_two:
		part_two = i


print(part_one, part_two)
