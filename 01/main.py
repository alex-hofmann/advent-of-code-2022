#!/usr/bin/env python3

with open('01/input.txt', 'r') as f:
    text = f.read()

sorted_array = sorted(
    map(
        sum, map(
            lambda x : map(
                int, x.strip().split()),
                    text.split('\n\n')
            )
        )
    )

print(sorted_array[-1], sum(sorted_array[-3:]))
