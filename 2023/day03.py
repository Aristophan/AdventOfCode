import utils as u

data = open('inputs/3.txt').read().strip()

symbols = set(data).difference(set(map(str,range(0,10))))
symbols.remove('\n')
symbols.remove('.')

data = data.split('\n')

def findSymbol(i,a,b):
    research =data[i][a]
    research+=data[i][b-1]
    if i!=0:
        research += data[i-1][a:b]
    if i!=len(data)-1:
        research += data[i+1][a:b]
    return not set(research).isdisjoint(symbols)

def updateGear(i,j,num):
    if f'{i},{j}' in gears.keys():
        gears[f'{i},{j}']['parts'] += 1 
        gears[f'{i},{j}']['value'] *= num
    else:
        gears[f'{i},{j}'] = {}
        gears[f'{i},{j}']['parts'] = 1 
        gears[f'{i},{j}']['value'] = num

num = 0
gears = {}

sol1 = 0
sol2 = 0

for i,line in enumerate(data):
    for j,char in enumerate(line):
        if char.isdigit():
            num*=10
            num+=int(char)
        if (char=='.' or j==len(line)-1 or char in symbols) and num!=0:
            length = len(str(num))
            a,b = max(0,j-length-1),min(len(line)-1,j+1)
            if findSymbol(i,a,b):
                sol1+=num
            if i!=0:
                for pos in u.findall(data[i-1][a:b],'\*'):
                    updateGear(i-1,a+pos,num)
            if i!=len(data)-1:
                for pos in u.findall(data[i+1][a:b],'\*'):
                    updateGear(i+1,a+pos,num)
            if line[a]=='*':
                updateGear(i,a,num)
            if line[b-1]=='*':
                updateGear(i,b-1,num)
            num=0

for gear in gears.values():
    if gear['parts']==2:
        sol2+=gear['value']

print(f'sol1 : {sol1}')
print(f'sol2 : {sol2}')


