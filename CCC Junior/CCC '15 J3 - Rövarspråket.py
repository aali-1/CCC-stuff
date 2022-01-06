import sys
input = sys.stdin.readline
print=sys.stdout.write
vowels=[97,101,105,111,117]
thing = input()[:-1]
for x in range(len(thing)):
    print(thing[x])
    j=ord(thing[x])
    if not j in vowels:
        kee = lambda k : abs(k - j)
        vow=min(vowels,key=kee)
        print(chr(vow))
        if chr(j)=='z':
            print('z')
        else:
            for y in range(j+1,123):
                if not y in vowels:
                    print(chr(y))
                    break
        