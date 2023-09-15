"https://open.kattis.com/problems/wheretolive"
x = 0
y = 0
while True:
    n = int(input())
    if n==0:
        break
    for i in range(n):
        a = input().split()
        x += int(a[0])
        y += int(a[1])
    print(round(x/n)," ",print(y/n))
    x = 0
    y = 0
