import sys

seat_id = ['.']*1024

with open("day5/input_day5.txt") as f:
    l = f.readlines()

for line in l:
    row = list(range(128))
    seat = list(range(8))
    
    for c in line[:7]:
        if c == 'F':
            row = row[:len(row)//2]
        else:
            row = row[len(row)//2:]

    for c in line[7:10]:
        if c == 'R':
            seat = seat[len(seat)//2:]
        else:
            seat = seat[:len(seat)//2]

    id = row[0]*8+seat[0]
    seat_id[id] = 'x'

my_seat = seat_id.index('.',seat_id.index('x'))
print(my_seat)