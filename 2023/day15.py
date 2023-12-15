import re
import copy
import numpy as np
import utils as u

data = open('inputs/15.txt').read().strip().split(',')


def hash_func(str):
    num = 0
    for char in str:
        ascii = ord(char)
        num+=ascii
        num*=17
        num = num%256
        #print(f'----char : {char}, ascii : {ascii}, num : {num}')
    return num
def part1(data):
    sol1=0
    for str in data:
        print(str)
        sol1+=hash_func(str)

    return sol1

def part2(data):
    sol2 = 0
    lenses = []
    for lens in data :
        if '=' in lens:
            label,power = lens.split('=')
            lenses.append({'label' : label,'power' : int(power),'action' : '=','box' : hash_func(label)})
        else:
            label = lens[:-1]
            lenses.append({'label' : label, 'action' : '-', 'box' : hash_func(label)})    

    # boxes = {
    #     0 : [{
    #         'power' : 7,
    #         'label' : 'ab'
    #     },
    #     {
    #         'power' : 8,
    #         'label' : 'df'
    #     }
    #     ]
    # }
    boxes = {}
    for box in range(256):
        boxes[box] = []
    
    print('-'*50)
    for lens in lenses:
        print('\n',lens['label'],'\n')
        box = boxes[lens['box']]
        if lens['action'] == '-':
            for i,lens_in_box in enumerate(box):
                if lens_in_box['label'] == lens['label']:
                    box.pop(i)
        else:
            if not box:
                box.append(lens)
            else:
                for i,lens_in_box in enumerate(box):
                    if lens_in_box['label'] == lens['label']:
                        box[i] = lens
                if not lens in box : 
                    box.append(lens)
        boxes[lens['box']] = box
        print(boxes)
        print('\n')
        print('-'*50)

    for i,box in enumerate(boxes):
        for j,lens in enumerate(boxes[i]):
            print(lens)
            print(lens['power']*(i+1)*(j+1))
            sol2 += lens['power']*(i+1)*(j+1)


    return sol2

sol1 = part1(data)
sol2 = part2(data)

print(f'sol1 : {sol1}')
print(f'sol2 : {sol2}')
