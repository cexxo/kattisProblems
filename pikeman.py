"""
pikeman easy (https://open.kattis.com/problems/pikemaneasy)
"""
s = input().split()
N = int(s[0])
T = int(s[1])
s = input().split()
A = int(s[0])
B = int(s[1])
C = int(s[2])
t0 = int(s[3])
t = [0 for j in range(0,N)]
t[0] = t0
for i in range(1,N):
    t[i] = ((A*t[i-1]+B)%C) +1
task = 0
counter = 0
residual = T
penalty = 0
t = sorted(t)
for i in range(T):
    if task < len(t):
        if t[task] == counter:
            task+=1
            penalty += i
            counter = 0
    if task >=len(t):
        break
    counter += 1
    #penalty += 1
            #print(i,"task {} was completed".format(task+1),task)
print(task,penalty%1000000007)