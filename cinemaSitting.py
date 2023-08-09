"""
Cinema Sitting(https://open.kattis.com/problems/cinemaseating)
"""
s = input().split()
rows,columns = int(s[0]),int(s[1])
numBookings = int(input())
grid = [[0 for j in range(-1,columns+1)] for i in range(-1,rows+1)]
#print(grid)
for i in range(numBookings):
    temp = input().split()
    x = int(temp[0])
    y = int(temp[1])
    grid[x][y] = 1
#print(grid)
k = [0 for j in range(9)]
neighbours = 0
for i in range(1,len(grid)-1):
    for j in range(1,len(grid[0])-1):
        if grid[i][j] != 0:
            if grid[i-1][j] != 0:
                neighbours+=1
            if grid[i+1][j] != 0:
                neighbours+=1
            if grid[i][j-1] != 0:
                neighbours+=1
            if grid[i][j+1] != 0:
                neighbours+=1
            if grid[i-1][j-1] != 0:
                neighbours+=1
            if grid[i-1][j+1] != 0:
                neighbours+=1
            if grid[i+1][j+1] != 0:
                neighbours+=1
            if grid[i+1][j-1] != 0:
                neighbours+=1
            k[neighbours] +=1
            neighbours = 0
        #print("new Point")
stringa = ''
for i in k:
    stringa += str(i)+' '
print(stringa[:len(stringa)-1])