"https://open.kattis.com/problems/zebrasocelots"
n = int(input())
animals = {}
found = False
for i in range(n):
    k = input()
    if k == 'O':
        found = True
    if found:
        animals[i] = k
counter = 0
while True:
    indeces = [k for k,v in animals.items() if v=='O']
    if len(indeces)==0:
        break
    for i in range(indeces[-1],n):
        if animals[i]=='Z':
            animals[i]='O'
        elif animals[i]=='O':
            animals[i]='Z'
    counter += 1
print(counter)