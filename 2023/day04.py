import utils as u
import numpy as np

data = open('inputs/4.txt').read().strip().replace('  ',' 0')

N = len(data.split('\n'))

sol1 = 0
sol2 = np.ones(N)
sol1_1 = 0

for i,line in enumerate(data.split('\n')):
    ticket=0
    left,right = line.split(':')[1].strip().split('|')

    winning = set([int(char.strip()) for char in left.strip().split(' ')])
    play = set([int(char.strip()) for char in right.strip().split(' ')])

    ticket = len(winning.intersection(play))
    prize = 2**(ticket-1) if ticket>0 else 0

    sol1+=prize

    if i<N-ticket-1:
        sol2[i+1:i+1+ticket] += sol2[i]
    elif i<N:
        sol2[i+1:] += sol2[i]

print(f'sol1 : {int(sol1)}')
print(f'sol2 : {int(sum(sol2))}')