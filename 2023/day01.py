data = [l.strip() for l in open('input.txt')]
#part1
numbers = list(map(str,range(10)))
X = [[int(char) for char in l if char in numbers]for l in data]
print(sum([10*l[0]+l[-1] for l in X]))

#part2
sol2 = 0
for ligne in data:
    digits = []
    for i,c in enumerate(ligne):
        if c.isdigit():
            digits.append(c)
        for num,d in enumerate(["one","two","three","four","five","six","seven","eight","nine"]):
            if ligne[i:].startswith(d):
                digits.append(str(num+1))
    sol2+=int(digits[0]+digits[-1])
print(sol2)
