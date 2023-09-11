"Frogger (https://open.kattis.com/problems/1dfroggereasy?tab=metadata)"
a = input().split()
n = int(a[0])
s = int(a[1])
m = int(a[2])
b = input().split()
squares = []
for i in b:
    squares.append(int(i))
results = ['magic', 'left', 'right', 'cycle']
pointer = s-1
visited = []
counter = 0
while True:
    if pointer in visited:
        print(results[3])
        break
    if pointer <= -1:
        print(results[1])
        break
    elif pointer >= n:
        print(results[2])
        break
    if squares[pointer] == m:
        print(results[0])
        break
    else:
        visited.append(pointer)
        pointer += squares[pointer]
    counter += 1
print(counter)