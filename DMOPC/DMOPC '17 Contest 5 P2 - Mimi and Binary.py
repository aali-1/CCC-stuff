import sys
from bisect import bisect_left
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))
ring=[x for x in readline()]
w=len(ring)
zeros=[0]*(w+1)
ones=[0]*(w+1)
for i,x in enumerate(ring):
    if x=='1':
        ones[i+1]=ones[i]+1
        zeros[i+1]=zeros[i]
    else:
        ones[i+1]=ones[i]
        zeros[i+1]=zeros[i]+1
for x in range(readint()):
    x,y,z=gi()
    if z==1:
        i=bisect_left(ones,y+ones[x-1])
    else:
        i=bisect_left(zeros,y+zeros[x-1])
    if i>w:
        print(-1)
    else:
        print(i)    
            