import sys

with open("day9/input_day9.txt") as f:
    l = [int(x.replace('\n','')) for x in f.readlines()]
print(l)

len_preamble = 25

for i in range(len_preamble,len(l)):
    found = False
    for j in range(i-len_preamble,i-1):
        for k in range(j+1,i):
            sum = l[j] + l[k]
            if sum == l[i]:
                found = True
    if not found:
        invalid = l[i]
        print(invalid)
        break

for i in range(len(l)):
    sum = l[i]
    for j in range(i+1,len(l)):
        sum += l[j]
        if sum == invalid:
            print(min(l[i:j+1]), max(l[i:j+1]))
            total = min(l[i:j+1]) + max(l[i:j+1])
            print(total)
