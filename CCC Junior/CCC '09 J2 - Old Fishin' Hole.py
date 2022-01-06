import sys
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))
btp=readint()
npp=readint()
ypp=readint()
total=readint()
ans=0
for b in range((total//btp)+2):
    for n in range((total//npp)+2):
        for y in range((total//ypp)+2):
            #print(b,n,y)
            if {b,n,y}=={0}:
                continue
            if b*btp+n*npp+y*ypp<=total:
                ans+=1
                print(f"{b} Brown Trout, {n} Northern Pike, {y} Yellow Pickerel")
print('Number of ways to catch fish:',ans)