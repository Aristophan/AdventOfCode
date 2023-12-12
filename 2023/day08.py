import utils as u
import numpy as np
import math as m
import copy
from math import gcd

data = open('inputs/8.txt').read().strip().split('\n')
directions = [int(direction) for direction in data[0].replace('R','1').replace('L','0')]
nodes = {}
for line in data[2:]:
    current,next = line.split(' = ')
    nodes[current] = (next[1:4],next[6:-1])

step = 0
# node = 'AAA'
# while node!='ZZZ':
#     direction = directions[step%len(directions)]
#     node = nodes[node][direction]
#     step+=1
sol1 = step

step = 0
sol2 = 0
current = list(filter(lambda x : x.endswith('A'),nodes.keys()))

def condition(current):
    for node in current:
        if not node.endswith('Z'):
            return True
    return False

while condition(current) and step<100:
    direction = directions[step%len(directions)]
    for i,node in enumerate(current):
        current[i] = nodes[node][direction]
    step+=1
    if step%1000000==0:
        print(step)
print(current)
sol2 = step

print(f'sol1 : {sol1}')
print(f'sol2 : {sol2}')