"https://open.kattis.com/problems/wheresmyinternet"
"Slow solution"
class node:
    def __init__(self,value):
        self.value = value
        self.children = []
    def addChild(self,child):
        self.children.append(child)

a = input().split()
n = int(a[0])
m = int(a[1])
disconnected = [i for i in range(1,n+1)]
nodes = [node(i) for i in range(1,n+1)]
connected = [1]
for j in range(m):
    temp = input().split()
    nodes[int(temp[0])-1].addChild(int(temp[1]))
    nodes[int(temp[1])-1].addChild(int(temp[0]))
for k in range(2):
    for i in nodes:
        for j in i.children:
            if i.value in connected and j not in connected:
                connected.append(j)
            elif i.value not in connected and j in connected:
                connected.append(i.value)
for i in connected:
    disconnected.remove(i)
if len(disconnected)!=0:
    for i in disconnected:
        print(i)
else:
    print('Connected')
"Fast solution"
class Node:
    def __init__(self, value):
        self.value = value
        self.children = set()

    def add_child(self, child):
        self.children.add(child)

a = input().split()
n = int(a[0])
m = int(a[1])
disconnected = set(range(1, n + 1))
nodes = [Node(i) for i in range(1, n + 1)]
connected = {1}

for j in range(m):
    temp = input().split()
    nodes[int(temp[0]) - 1].add_child(int(temp[1]))
    nodes[int(temp[1]) - 1].add_child(int(temp[0]))

for _ in range(2):
    for i in nodes:
        for j in i.children:
            if i.value in connected and j not in connected:
                connected.add(j)
            elif i.value not in connected and j in connected:
                connected.add(i.value)

disconnected -= connected

if len(disconnected) != 0:
    for i in disconnected:
        print(i)
else:
    print('Connected')
