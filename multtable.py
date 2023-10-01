"https://open.kattis.com/problems/multtable"
temp = input().split()
n= int(temp[0])
m = int(temp[1])
counter = 0
b = m
for i in range(1,n+1):
    if b%i == 0 and b/i <=n:
        counter +=1
print(counter)