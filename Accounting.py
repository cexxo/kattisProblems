"https://open.kattis.com/problems/bokforing"
N, Q = map(int, input().split())
money = [0] * N
prova = 0
indeces = set()

for _ in range(Q):
    temp = input().split()
    j = int(temp[1]) - 1
    if temp[0] == 'SET':
        money[j] = int(temp[2])
        indeces.add(j)
    elif temp[0] == 'PRINT':
        print(money[j] if j in indeces else prova)
    elif temp[0] == 'RESTART':
        prova = int(temp[1])
        indeces.clear()
