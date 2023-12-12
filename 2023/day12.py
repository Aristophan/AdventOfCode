import utils as u
import numpy as np
import math as m
import copy
import re
from math import gcd


data = open('inputs/12.txt').read().strip().split('\n')

_PRINT = False

def evaluate_arrangement(springs,separation):
    regex = r'[\.]+'
    separated = re.split(regex,springs.strip(regex))
    if separation == [len(sep) for sep in separated]:
        if _PRINT : print(f'    {springs}')
    return separation == [len(sep) for sep in separated]

def find_combination(record,separation,count):
    if '?' in record:
        for replacement in ['.','#']:
            count = find_combination(record.replace('?',replacement,1),separation,count)
    elif evaluate_arrangement(record,separation) :
        return count+1
    return count

sol1 = 0 
for line in data:
    if _PRINT : print('-'*50)
    record, separation = line.split()
    separation = list(map(int,separation.split(',')))
    if _PRINT : print(record,separation,end = '\n\n')
    count = find_combination(record,separation,0)
    if _PRINT : print(f'\n{count}')
    sol1+=count
    #comb = 2**(sum([char=='?' for char in record])) 
    #if _PRINT : print(f'{comb}\n' if comb>100000 else '',end = '' )

print(f'sol1 : {sol1}')