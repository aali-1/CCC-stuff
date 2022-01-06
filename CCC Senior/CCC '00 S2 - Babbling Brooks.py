import sys
from itertools import chain
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))
flat = lambda y:[x for a in y for x in flat(a)] if type(y) is list else [y]
n=readint()
rivers=[readint() for _ in range(n)]
while(True):
    num=readint()
    if num==77:
        break
    if num==99: #split
        stream=readint()
        percent=readint()/100
        thing=rivers[stream-1]
        rivers[stream-1]=[(thing*percent),thing-(thing*percent)]
        rivers=flat(rivers)
        #print(rivers)
    if num==88:
        idex=readint()-1
        rivers[idex]=rivers[idex]+rivers.pop(idex+1)
        #print(rivers)
print(*[round(x) for x in rivers])