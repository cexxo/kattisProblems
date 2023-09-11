"https://open.kattis.com/problems/zebrasocelots"
n = int(input())
animals = {}
for i in range(n):
    animals[i] = input()
counter = 0
found = False
index = -1
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