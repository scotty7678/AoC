import sys

f = open("day3/input_day3.txt")
l = f.readlines()
print(l)

# Count of trees encountered
trees = 0

#  x position counter to use with modulus of width
x = 0
mod = len(l[0])-1  # Needed the -1 for the right modulus to be applied
i = 0

for row in l:
    if row[x] == '#':
        trees += 1
    i += 3
    x = i%mod
    print(i, x)

print(trees)

