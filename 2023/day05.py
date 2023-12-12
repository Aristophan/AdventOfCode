import utils as u
import numpy as np
import copy

data = open('inputs/5.txt').read().strip()


sol1=0
sol2=0

seeds = [int(seed) for seed in data[7:].split('\n')[0].strip().split(' ')]
seeds2 = [(seed, seed+seeds[2*i+1]-1) for i,seed in enumerate(seeds[::2])]

new = copy.copy(seeds)
new_seeds = copy.copy(seeds2)

for mapping in data.split('map:\n')[1:]:
    new = copy.copy(seeds)
    new_seeds = list(set(copy.copy(seeds2)))
    print('-')
    for line in mapping.split('\n')[:-2]:
        destination,source,rng = list(map(int,line.strip().split(' ')))
        print(destination,source,rng)
        print(new_seeds)
        for i,seed in enumerate(seeds):
            if source<=seed<source+rng:
                new[i] = seed - source + destination 
        
        for i,(start,stop) in enumerate(seeds2):
            if source<=start<source+rng:
                if stop <source+rng:
                    new_seeds[i] = (start - source + destination, stop - source + destination)
                else:
                    new_seeds[i] = (start - source + destination, destination + rng - 1)
                    new_seeds.append((source + rng,stop))
            if start<source:
                if source<=stop<source+rng:
                    new_seeds[i] = (start,source-1)
                    new_seeds.append((destination,stop-source+destination))
                if stop>=source+rng:
                    new_seeds[i] = (start,source-1)
                    new_seeds.append((destination,destination+rng))
                    new_seeds.append((source+rng,stop))
            print(new_seeds)
    print('-')
    seeds2 = copy.copy(new_seeds)
    seeds = new

sol2 = min([start for start,_ in seeds2])


print(seeds2)
print(f'sol1 : {min(seeds)}')
print(f'sol2 : {sol2}')