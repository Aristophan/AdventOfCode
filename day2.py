data = [[[pick.strip().split(' ') for pick in aset.split(',')] 
         for aset in l.strip().split(':')[1].split(';')] 
         for l in open('inputs/2.txt')]
sol1 = 0
sol2 = 0
for i,game in enumerate(data):
    game_impossible=False
    mini = [0,0,0]
    for aset in game:
        for pick in aset:
            if 'red' == pick[1]:
                if int(pick[0])>12:
                    game_impossible = True
                mini[0] = max(mini[0],int(pick[0]))
            if 'green' == pick[1]:
                if int(pick[0])>13:
                    game_impossible = True
                mini[1] = max(mini[1],int(pick[0]))
            if 'blue' == pick[1]:
                if int(pick[0])>14:
                    game_impossible = True
                mini[2] = max(mini[2],int(pick[0]))
    sol2+=mini[0]*mini[1]*mini[2]
    if not game_impossible : sol1+=i+1
print(sol1)
print(sol2)

