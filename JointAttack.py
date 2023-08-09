"""
Joint Attack (https://open.kattis.com/problems/jointattack)
General Torstein has sent the x-coordinate for the next joint 
attack and is expecting you to promptly follow his orders in 
order to avoid impeding doom. Unfortunately Torstein hates 
numbers with more than 2 digits and loves horizontal line 
segments, and has therefore sent the coordinate as a continued
fraction, i.e. x = X_0 + 1/(x_1+1/(...))
Your rocket launcher only accepts coordinates as reduced 
fractions, so you need to quickly compute the correct numbers 
to feed it in order to commence the attack. Hurry! Failure 
may have dire consequences!
INPUT:
The first line of output is one integer n(1<=n<=40), the 
number of coefficients in the continued fraction, followed by 
a line with n integers (1 <= x_i<=100) the coefficients of x.
OUTPUT:
The coordinate x as a reduced fraction. It is guaranteed that 
the numerator and denominator are both less than 10^18.
"""
import math
s = int(input())
temp = input().split()
for i in range(len(temp)):
    temp[i] = int(temp[i])
temp.reverse()
numerator = 0
denominator = 0
a = 0
for i in range(len(temp)-1):
    if i == 0:
        numerator += temp[i]*temp[i+1] +1
        denominator += temp[i]
    else:
        a = numerator
        numerator = denominator
        denominator = a
        numerator += temp[i+1]*denominator
    #print(str(numerator)+"/"+str(denominator))
if denominator == 0:
    print("0/1")
else:
    print(str(numerator)+"/"+str(denominator)) 