"""
99 Problems(https://open.kattis.com/problems/99problems)
"""
s = input()
order = 10**(len(s)-1)
s = int(s)
difference = 100000
temp = 0
answer = 99
for i in range(99,order*10,100):
    temp = abs(i-s)
    if(temp <= difference):
        difference = temp
        answer = i
print(answer)