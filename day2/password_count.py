import sys

f = open("day2/input_day2.txt")

l = [x.split() for x in f.readlines()]

c = 0

for row in l:
    min, max = [int(x) for x in row[0].split('-')]
    letter = row[1][0]
    password = row[2]

    num = password.count(letter)

    if num >= min and num <= max:
        c += 1

print(c)