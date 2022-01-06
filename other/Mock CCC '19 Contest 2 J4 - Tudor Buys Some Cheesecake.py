import sys
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))

from collections import defaultdict
thing=defaultdict(lambda: 0)
one=readline()
for x in one:
    thing[x]+=1
N=len(one)
two=readline()
ans=0
for x in two:
    if thing[x]>0:
        thing[x]-=1
for x in thing:
    ans+=thing[x]
print(ans)