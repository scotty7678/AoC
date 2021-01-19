import sys

#  I added two newlines at the end of input for this to work
#  Fix at a later date

l = []
t = ''

with open("day6/input_day6.txt") as f:
    for row in f.readlines():
        if row != '\n':
            t += row
        else:
            s = ''
            for c in t:
                if c.isalpha():s+=c
            t = set(s)
            l.append(t)
            t =''

print(sum([len(x) for x in l]))