"https://open.kattis.com/problems/aprizenoonecanwin"
a = input().split()
n = int(a[0])
x = int(a[1])
b = input().split()
items = []
for i in b:
    items.append(int(i))
items.sort()
counter = 1
total = 0
list = [items[0]]
items.remove(items[0])
noPush = False
for i in range(len(items)):
    for j in list:
        if i + j > x:
            counter += 1
    if counter != len(items):
        list.append(i)
        items.pop(0)
    counter = 0
print(len(list))