import sys
from math import floor,sqrt
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))
emp = lambda x, y: [x for _ in range(y)]

maximum=100000
sieve = [False]*100001
sieve[0]=True
sieve[1]=True
for i in range(2,maximum):
    if sieve[i]==True:
        continue
    for h in range(i*2,maximum+1,i):
        sieve[h]=True
N=readint()
f=gi()
#print(sieve[:10])
count=0
for x in f:
    if not sieve[x]:
        count+=1
print(count)