#!/usr/bin/env python3

with open('input.txt', 'r') as f:
	data = f.read()

parts = [4, 14]

for part in parts:
	for i in range(part, len(data)):
		packet = data[i-part:i]
		if len(set(packet)) == part:
			print(i)
			break
