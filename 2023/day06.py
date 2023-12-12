import utils as u
import numpy as np
import math as m
import copy

data = open('inputs/6.txt').read().strip().split('\n')
times = [int(time) for time in data[0][5:].strip().split()]
records = [int(record) for record in data[1][9:].strip().split()]

time2 = int(u.concatenate(map(str,times)))
record2 = int(u.concatenate(map(str,records)))

#equ : -x2 + time x -time*record > 0
#delta : -b2-4ac
#roots : -b - sqrt(delta) / 2a
a,b,c = -1,time2,-record2
delta = b**2-4*a*c
roots = list(map(int,[(-b+m.sqrt(delta))/(2*a),(-b-m.sqrt(delta))/(2*a)]))
sol1=1
sol2=int(roots[1]-roots[0])

for time,record in zip(times,records):
    ways = 0
    for button in range(time):
        if (time-button)*button>record:
            ways+=1
    sol1*=ways
print(roots)
print(f'sol1 : {sol1}')
print(f'sol2 : {sol2}')

