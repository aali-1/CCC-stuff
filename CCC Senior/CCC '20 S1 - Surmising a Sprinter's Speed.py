import sys
input = sys.stdin.readline
N = int(input())
T = {}
for _ in range(N):
    g,h = [int(x) for x in input().split()]
    T[g]=h
keyz = sorted(T.keys())
ab = 0
#print(keyz)
for x,y in enumerate(keyz):
    try:
        thing = abs(T[keyz[x+1]]-T[y])/(keyz[x+1]-y)
        if thing>ab:
            #print(abs(T[keyz[x+1]]-T[keyz[x]]),(keyz[x+1]-keyz[x]))
            ab=thing
    except(IndexError):
        pass
print(ab)
