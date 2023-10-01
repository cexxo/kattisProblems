"https://open.kattis.com/problems/multtable"
temp = input().split()
n= int(temp[0])
m = int(temp[1])
counter = 0
b = m
if m > n:
    for i in range(1,n+1):
        if b%i == 0 and b/i <=n:
            counter +=1
else:
    for i in range(1,m+1):
        if b%i == 0 and b/i <=m:
            counter +=1
print(counter)