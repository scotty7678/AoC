import sys

f = open("input.txt")

l = [int(x) for x in f.readlines()]

for i in range(len(l)):
    for j in range(i,len(l)):
        sum = l[i] + l[j]
        if sum == 2020:
            print(l[i] * l[j])