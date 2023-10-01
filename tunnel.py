import math
a = int(input())
ans = 0
ans2 = 0
for i in range(a):
    coordinates = input().split()
    lat1 = float(coordinates[0])
    lon1 = float(coordinates[1])
    lat2 = float(coordinates[2])
    lon2 = float(coordinates[3])
    theta = float(((lat1-lat2)**2 +(lon1-lon2)**2)**0.5)
    ans = float((lat1-lat2)**2 +(lon1-lon2)**2)
    ans = ans**0.5
    ans = ans*3.14*6371009
    ans2 = 2*math.sin(theta/2)*6371009
    print(abs(ans-ans2))