"""
Bootstrapingnumber(https://open.kattis.com/problems/bootstrappingnumber)
"""
s = float(input())
i : float = 0.0
for k in range(1,10**6):
        if s >= 100000:
             i = 6.27
        elif float(k**k) > s:
            i = k-1
            #print (k)
            break
while True:
    if int(i**i) >= s:
        print(round(i,6))
        break
    else:
        i+= 5*10**-6