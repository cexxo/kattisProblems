"https://open.kattis.com/problems/volim"
k = int(input())
n = int(input())
counter = k
current_time = 0
found = False
for i in range(n):
    temp = input().split()
    time = int(temp[0])
    action = temp[1]
    current_time += time
    if current_time >= 210 and not found:
        answer = counter
        found = True
    if action == 'T':
        counter+= 1
    if counter == 9:
        counter = 1
    
print(answer)