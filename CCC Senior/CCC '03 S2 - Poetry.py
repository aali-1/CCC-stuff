import sys
vowels = ['a','e','i','o','u']
input = sys.stdin.readline
for _ in range(int(input())):
    lastsyls=[]
    for _ in range(4):
        phrase = input().lower().split()[-1]
        if any(x in phrase for x in vowels):
            lastvo=[]
            for x in range(5):
                lastvo.append(phrase.rfind(vowels[x]))
            lastvo=max(lastvo)
            lastsyls.append(phrase[lastvo:])
        else:
            lastsyls.append(phrase)
    if lastsyls[0]==lastsyls[2] and lastsyls[1]==lastsyls[3]:
        if lastsyls[1]==lastsyls[2] and lastsyls[0]==lastsyls[3]:
            print('perfect')
        else:
            print('cross')
    elif lastsyls[0]==lastsyls[1] and lastsyls[2]==lastsyls[3]:
        print('even')
    elif lastsyls[0]==lastsyls[3] and lastsyls[1]==lastsyls[2]:
        print('shell')
    else:
        print('free')

'''
1
Helloh mjk
Helloh 
Helloh
Hello mjk
'''

