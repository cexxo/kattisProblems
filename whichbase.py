"https://open.kattis.com/problems/whichbase"
p = int(input())
out = ""
for i in range(p):
    temp = input().split()
    out = temp[0]
    out += " "
    try:
        out += str(int(temp[1],8))
    except:
        out+= str(0)
    out += " "
    out += str(int(temp[1],10))
    out += " "
    out += str(int(temp[1],16))
    print(out)