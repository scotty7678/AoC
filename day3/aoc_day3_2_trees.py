import sys

f = open("day3/input_day3.txt")
l = f.readlines()


# Count of trees encountered
trees = []
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

for slope in slopes:
    tree = 0

    x_inc, y_inc = slope
    #  x position counter to use with modulus of width
    x = 0
    mod = len(l[0])-1  # Needed the -1 for the right modulus to be applied
    i = 0

    for y in range(0, len(l), y_inc):
        row = l[y]

        if row[x] == '#':
            tree += 1
        i += x_inc
        x = i%mod
    trees.append(tree)

print(trees)

prod = 1
for n in trees:
    prod *= n
print(prod)