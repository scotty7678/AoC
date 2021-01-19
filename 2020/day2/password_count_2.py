import sys

f = open("day2/input_day2.txt")

l = [x.split() for x in f.readlines()]

c = 0

for row in l:
    p1, p2 = [int(x)-1 for x in row[0].split('-')]
    letter = row[1][0]
    password = row[2]

    #print(p1,p2,letter,password)
    if (password[p1] == letter and password[p2] != letter) or (password[p2] == letter and password[p1] != letter):
        c += 1

print(c)