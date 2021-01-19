import sys

l = []
t = ''

with open("day4/input_day4.txt") as f:
    for row in f.readlines():
        if row != '\n':
            t += row
        else:
            l.append(t.replace('\n',' '))
            t =''

valid = 0
for row in l:
    if (all(x in row for x in ['byr:', 'iyr:','eyr', 'hgt:', 'hcl:', 'ecl:', 'pid:'])): valid += 1
print(valid)