import sys
from collections import deque
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gf = lambda: list(map(float, readline().split()))
N=readint()
K=gf()[0]
mean=0
for _ in range(N):
    thing=gf()[1:]
    temp=K
    for x in thing:
        temp+=x
    print(temp)
    mean+=temp
print(mean/N)
