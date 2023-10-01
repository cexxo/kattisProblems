"https://open.kattis.com/problems/astrologicalsign"
cases = int(input())
for i in range(cases):
    temp = input().split()
    temp[0] = int(temp [0])
    if temp[1] == 'Jan':
        if int(temp[0]>=21):
            print('Aquarius')
        else:
            print('Capricorn')
    if temp[1] == 'Feb':
        if int(temp[0]>=20):
            print('Pisces')
        else:
            print('Aquarius')
    if temp[1] == 'Mar':
        if int(temp[0]>=21):
            print('Aries')
        else:
            print('Pisces')
    if temp[1] == 'Apr':
        if int(temp[0]>=21):
            print('Taurus')
        else:
            print('Aries')
    if temp[1] == 'May':
        if int(temp[0]>=21):
            print('Gemini')
        else:
            print('Taurus')
    if temp[1] == 'Jun':
        if int(temp[0]>=22):
            print('Cancer')
        else:
            print('Gemini')
    if temp[1] == 'Jul':
        if int(temp[0]>=23):
            print('Leo')
        else:
            print('Cancer')
    if temp[1] == 'Aug':
        if int(temp[0]>=23):
            print('Virgo')
        else:
            print('Leo')
    if temp[1] == 'Sep':
        if int(temp[0]>=22):
            print('Libra')
        else:
            print('Virgo')
    if temp[1] == 'Oct':
        if int(temp[0]>=23):
            print('Scorpio')
        else:
            print('Libra')
    if temp[1] == 'Nov':
        if int(temp[0]>=23):
            print('Sagittarius')
        else:
            print('Scorpio')
    if temp[1] == 'Dec':
        if int(temp[0]>=22):
            print('Capricorn')
        else:
            print('Sagittarius')