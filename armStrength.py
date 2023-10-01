"https://open.kattis.com/problems/armystrengtheasy"
cases = int(input())
godzilla = []
mecha = []
for i in range(cases):
    blank = input()
    blank2 = input()
    godzilla = input().split()
    mecha = input().split()
    for i in range(len(godzilla)):
        godzilla[i] = int(godzilla[i])
    for i in range(len(mecha)):
        mecha[i] = int(mecha[i])
    godzilla.sort()
    mecha.sort()
    while len(godzilla) != 0 and len(mecha) != 0:
        if godzilla[0] >= mecha[0]:
            mecha.pop(0)
        else:
            godzilla.pop(0)
    if(len(godzilla)==0):
        print("MechaGodzilla")
    elif(len(mecha)==0):
        print("Godzilla")
    else:
        print("uncertain")