n = int(input())
counter = [0,0,0]
for i in range(n):
    k = input().split()
    for i in range(len(k)):
        if k[i] == 'J':
            counter[i] +=1
min = 1000000
for i in counter:
    if i <= min:
        min = i
print(min)