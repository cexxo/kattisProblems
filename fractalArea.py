"""
Fractal Area(https://open.kattis.com/problems/fractalarea)
"""
import math
numIterations = int(input())
PI = math.pi
for i in range (numIterations):
    temp = input().split()
    radius = int(temp[0])
    numExpansions = int(temp[1])
    area = 0
    factor = 1
    for i in range(numExpansions):
        if i == 0:
            area+=PI*radius*radius*factor
        elif i == 1:
            radius /= 2
            area += 4*PI*radius*radius*factor
            factor = 4
        else:
            radius /=2
            factor *=3
            area += PI*radius*radius*factor
    print(area)