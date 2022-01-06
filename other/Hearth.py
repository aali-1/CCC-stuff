import sys
input = sys.stdin.readline
d={}
found=[]
N,T=[int(x) for x in input().split()]
for x in range(N):
    thing = input().split()
    thing[1]=int(thing[1])
    if thing[1]<T:
        d[thing[0]]=int(thing[1])
#print(d)
keyz=sorted(d.keys())
for x in keyz:
    for y in keyz:
        for z in keyz:
            if d[x]+d[y]+d[z]<=T and x!=y and x!=z and y!=z:
                thing=sorted([x,y,z])
                if not thing in found:
                    found.append(thing)
                    print(*thing)