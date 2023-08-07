"""
3D printed Satues(https://open.kattis.com/problems/3dprinter)
You have a single 3D printer, and would like to use it to 
produce n statues. However, printing the statues one by one 
on the 3D printer takes a long time, so it may be more 
time-efficient to first use the 3D printer to print a new 
printer. That new printer may then in turn be used to print 
statues or even more printers. Print jobs take a full day, 
and every day you can choose for each printer in your 
possession to have it print a statue, or to have it 3D print 
a new printer (which becomes available for use the next day).

What is the minimum possible number of days needed to print 
at least n statues?
INPUT:
The input contains a single integer (1<=n<=10000), 
the number of statues you need to print.
OUTPUT:
Output a single integer, the minimum number of days needed to
print at least n statues.
"""
import math
s = int(input())
if s != 1:
    b = int(math.log2(s))
    if 2**b == s:
        print(2+b-1)
    else:
        print(2+b)
else:
    print(1)