"https://open.kattis.com/problems/akcija"
s = input()
n = int(s)
numbers = []
temp  = ''
for i in range(n):
    temp = input()
    numbers.append(int(temp))
numbers.sort(reverse=True)
sum = numbers[0]
for i in range(len(numbers)):
    if (i+1)%3 != 0 and i > 0:
        sum += numbers[i]
print(sum)