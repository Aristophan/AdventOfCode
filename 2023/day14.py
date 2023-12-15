import utils as u
import numpy as np
import math as m
import copy
import re
from math import gcd

_PRINT = False

def part1():

    data = open('inputs/14.txt').read().strip().split('\n')
    data.insert(0,u.concatenate(['#' for _ in range(len(data[0]))]))
    data.append(u.concatenate(['#' for _ in range(len(data[0]))]))
    data = ['#' + line +'#' for line in data]

    def roll(data,direction):

        direction2coord = {
            'north' : (-1,0),
            'south' : (+1,0),
            'west'  : (0,-1),
            'est'   : (0,+1),
        }

        direction2range = {
            'north' : [range(len(data))               ,range(len(data[0]))],
            'south' : [list(range(len(data)).__reversed__()),range(len(data[0]))],
            'west'  : [range(len(data))               ,range(len(data[0]))],
            'est'   : [range(len(data))               ,list(range(len(data[0])).__reversed__())],
        }

        incrementation = direction2coord[direction]
        line_iteration = direction2range[direction]

        for i in line_iteration[0]:
            for j in line_iteration[1]:
                if data[i][j]=='O':
                    v_shift,h_shift = 0,0
                    while data[i+v_shift+incrementation[0]][j+h_shift+incrementation[1]]=='.':
                        v_shift+=incrementation[0]
                        h_shift+=incrementation[1]
                    data[i] = data[i][:j] + '.' + data[i][j+1:]
                    data[i+v_shift] = data[i+v_shift][:j+h_shift] + 'O' + data[i+v_shift][j+1+h_shift:]
                    if _PRINT : print('- - '*25)
                    if _PRINT : print(f'\ni : {i}, j : {j}\n')
                    if _PRINT : 
                        for line in data : print(line)

    roll(data,'north')
    return sum([sum([len(data)-i-1 if char=='O' else 0 for char in line]) for i,line in enumerate(data)])



def part2():

    data = open('inputs/14.txt').read().strip().split('\n')
    data.insert(0,u.concatenate(['#' for _ in range(len(data[0]))]))
    data.append(u.concatenate(['#' for _ in range(len(data[0]))]))
    data = ['#' + line +'#' for line in data]
    original_data = copy.copy(data)

    # for line in data : print(line)
    # print('-'*50,'-'*50,sep = '\n')

    def roll(data,direction):

        direction2coord = {
            'north' : (-1,0),
            'south' : (+1,0),
            'west'  : (0,-1),
            'est'   : (0,+1),
        }

        direction2range = {
            'north' : [range(len(data))               ,range(len(data[0]))],
            'south' : [list(range(len(data)).__reversed__()),range(len(data[0]))],
            'west'  : [range(len(data))               ,range(len(data[0]))],
            'est'   : [range(len(data))               ,list(range(len(data[0])).__reversed__())],
        }

        incrementation = direction2coord[direction]
        line_iteration = direction2range[direction]

        for i in line_iteration[0]:
            for j in line_iteration[1]:
                if data[i][j]=='O':
                    v_shift,h_shift = 0,0
                    while data[i+v_shift+incrementation[0]][j+h_shift+incrementation[1]]=='.':
                        v_shift+=incrementation[0]
                        h_shift+=incrementation[1]
                    data[i] = data[i][:j] + '.' + data[i][j+1:]
                    data[i+v_shift] = data[i+v_shift][:j+h_shift] + 'O' + data[i+v_shift][j+1+h_shift:]
                    if _PRINT : print('- - '*25)
                    if _PRINT : print(f'\ni : {i}, j : {j}\n')
                    if _PRINT : 
                        for line in data : print(line)

    def find_loop(N = 1):
        data = copy.copy(original_data)
        memory = np.array([copy.copy(original_data) for _ in range(N)])
        for loop in range(N):
            roll(data,'north')
            roll(data,'west')
            roll(data,'south')
            roll(data,'est')
            for i,existing_data in enumerate(memory):
                if np.array_equal(existing_data,data):
                    print(f'Loops of length {loop-i} found on {i}th cycle')
                    return i,loop-i
            memory[loop]=data
        print(f'No loop found, trying with wider memory ({2*N})')
        return find_loop(N = 2*N)

    start_loop, length_loop = find_loop()
    loops = start_loop + (1000000000-start_loop)%length_loop

    data = copy.copy(original_data)
    for _ in range(loops):
            roll(data,'north')
            roll(data,'west')
            roll(data,'south')
            roll(data,'est')


    return sum([sum([len(data)-i-1 if char=='O' else 0 for char in line]) for i,line in enumerate(data)])

sol1 = part1()
sol2 = part2()

print(f'sol1 : {sol1}')
print(f'sol2 : {sol2}')
