import sys
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))
n,k=gi()
ls=gi()
d={}
for x in range(n):
    d[ls[x]]=x
for x in range(n):
    if k==0:
        break
    if ls[x]==n-x:
        continue
    thing=d[n-x]
    if ls[thing]>ls[x]:
        d[n-x]=x
        thing2=ls[thing]
        ls[thing]=ls[x]
        ls[x]=thing2
        k-=1
print(*ls)
    