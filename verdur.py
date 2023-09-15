max = int(input())
n = int(input())
for i in range(n):
    temp = input().split()
    if int(temp[1] )< max:
        print(temp[0], " lokud")
    else:
        print(temp[0], " opin")