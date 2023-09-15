n = input()
numbers = []
k = int(n)
for i in n:
    numbers.append(int(i))
temp = numbers[::-1]
for i in range(len(temp)-1):
    if temp[i] > temp[i+1]:
        a = temp[i]
        temp[i] = temp[i+1]
        temp[i+1] = a
        break
numbers = temp[::-1]
stri = ""
for i in numbers:
    stri += str(i)
if k == int(stri):
    print(0)
else:
    print(int(stri))