import utils as u
import numpy as np
import math as m
import copy
import re
from math import gcd


data = open('inputs/13.txt').read().strip().split('\n\n')

sol1 = 0 
sol2 = 0

def check_horizontal_mirror(top,bottom):
    top = [top[-line-1] for line in range(len(top))]
    for line_top,line_bottom in zip(top,bottom):
        if line_bottom!=line_top:
            return False
    return True

def check_vertical_mirror(left,right):
    left = [u.concatenate([line[-char-1] for char in range(len(line))]) for line in left]
    for i,(_,_) in enumerate(zip(left[0],right[0])):
        column_left = [line[i] for line in left]
        column_right = [line[i] for line in right]
        if column_left!=column_right:
            return False
    return True
    
def split_left_right(lines,ind):
    left = [line[:ind] for line in lines]
    right = [line[ind:] for line in lines]
    return left,right

no_reflection = 0

def find_reflection(lines,sol):
    reflection = False
    for ind in range(1,len(lines[0])):
        left,right = split_left_right(lines,ind)
        if check_vertical_mirror(left,right):
            print(ind)
            sol+=ind
            reflection = True
    for ind in range(1,len(lines)):
        top,bottom = split_top_bottom(lines,ind)
        if check_horizontal_mirror(top,bottom):
            print(100*ind)
            sol+=100*ind
            reflection = True
    return sol,reflection

def split_top_bottom(lines,ind):
    return lines[:ind],lines[ind:]

def find_deformed_reflection(lines,ind):
    if ind < len(lines)-ind:
        h_range = range(0,2*ind)
    else:
        h_range = range(len(lines)-2*ind,len(lines))
    if ind < len(lines[0])-ind:
        v_range = range(0,2*ind)
    else:
        v_range = range(len(lines[0])-2*ind,len(lines[0]))

    if ind < len(lines):
        for i in h_range:
            for j in range(1,len(lines[0])):
                print(i)
                if ind==1 :print('-'*50)
                deformed_lines = copy.copy(lines)
                replacement = '.' if lines[i][j]=='#' else '#'
                deformed_lines[i] = deformed_lines[i][:j] + replacement + deformed_lines[i][j+1:]
                for line in deformed_lines:
                    if ind==1 :print(line)
                top,bottom = split_top_bottom(lines,ind)
                if check_horizontal_mirror(top,bottom):
                    return 100*ind
    if ind < len(lines[0]):
        for i in range(len(lines)):
            for j in v_range:
                deformed_lines = copy.copy(lines)
                replacement = '.' if lines[i][j]=='#' else '#'
                deformed_lines[i] = deformed_lines[i][:j] + replacement + deformed_lines[i][j+1:]
                left,right = split_left_right(lines,ind)
                if check_vertical_mirror(left,right):
                    return ind
    return 0

for pattern in data:
    lines = pattern.split('\n')
    sol1 = find_reflection(lines,sol1)[0]

    for ind in range(1,max(len(lines[0]),len(lines))):
        sol2+=find_deformed_reflection(lines,ind)
    
print('no reflection', no_reflection)


print(f'sol1 : {sol1}')
print(f'sol2 : {sol2}')