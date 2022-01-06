import sys
from collections import deque
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))

bounds = gi()
loc=[0,0]
while(True):
    new=gi()
    if new==[0,0]:
        break
    loc[0]+=new[0]
    loc[1]+=new[1]
    loc = [0 if x<0 else x for x in loc]
    if loc[0]>bounds[0]:
        loc[0]=bounds[0]
    if loc[1]>bounds[1]:
        loc[1]=bounds[1]
    print(*loc)