"""
Above Average (https://open.kattis.com/problems/aboveaverage)
It is said that 90% of frosh expect to be above average in their class. You are to provide a reality check.
INPUT:
The first line of standard input contains an integer 1 <= C <= 50,
the number of test cases. C data sets follow. Each data set 
begins with an integer, N, the number of people in the class
(1 <= N <= 1000). N integers follow, separated by spaces 
or newlines, each giving the final grade (an integer between 0
and 100) of a student in the class.
OUTPUT:
For each case you are to output a line giving 
the percentage of students whose grade is above average, 
rounded to exactly 3 decimal places.
"""
s = int(input())
average = 0.0
candidatesAbove = 0
scores = []
for i in range (s):
    temp = input()
    a = temp.split(' ')
    n = int(a[0])
    for k in range(1,n+1):
        scores.append(int(a[k]))
    average = sum(scores)/n
    candidatesAbove = 0
    for k in range(1,n+1):
        if(scores[k-1] > average):
            candidatesAbove +=1
    formatted_number = '{:.3f}'.format(round(candidatesAbove/float(a[0])*100,3))
    print(formatted_number+"%")
    scores.clear()