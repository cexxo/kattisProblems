"https://open.kattis.com/problems/zebrasocelots"
n = int(input())
animals = []
found = False
for i in range(n):
    animals.append(input())
counter = 0
indeces = []
for i in range(n):
    if animals[i] == 'O':
        indeces.append(i)
for i in indeces:
    counter += 2**(n-i-1)
print(counter)