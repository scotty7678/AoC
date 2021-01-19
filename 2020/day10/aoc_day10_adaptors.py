import sys

with open("day10/input_day10.txt") as f:
    l = sorted([int(x) for x in f.readlines()])

d = {}

joltage = 0

for x in l:
    diff = x - joltage
    joltage = x
    if diff in d:
        d[diff] += 1
    else:
        d[diff] = 1
d[3] += 1

print(d)

print(d[1] * d[3])