"https://open.kattis.com/problems/whatdoesthefoxsay?editsubmit=11683007"
t = int(input())
phrase = []
answer = ""
question = ['what','does','the','fox','say?']
for i in range(t):
    phrase = input().split()
    while True:
        k = input().split()
        if k == question:
            break
        while k[2] in phrase:
            phrase.remove(k[2])
    for i in range(len(phrase)-1):
        answer += phrase[i] + " "
    print(answer+phrase[-1])
    answer = ""