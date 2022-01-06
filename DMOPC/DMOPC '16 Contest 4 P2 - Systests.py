import sys
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))
idk=[0]
idk2={}
points=0
B=readint()
for x in range(1,B+1):
    f,c,p=gi()
    points+=p
    idk.append(p)
    for y in range(f,c+1):
        try:
            idk2[y].append(x)
        except:
            idk2[y]=[x]
#print(idk)
#print(idk2)
found=[False]*B
for _ in range(readint()):
    num=readint()
    try:
        for x in idk2[num]:
            try:
                if found[x]:
                    continue
                points-=idk[x]
                idk[x]=0

            except:
                pass
    except:
        pass
print(points)
    