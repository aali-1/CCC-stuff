import sys
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))
ring=readline()
N=len(ring)
d={chr(x):[0]*(N+1) for x in range(97,97+26)}
for i in range(N):
    for y in d:
        d[y][i+1]+=d[y][i]+int(ring[i]==y)
for _ in range(readint()):
    i,j,c=readline().split()
    i=int(i)
    j=int(j)
    #print(d[c])
    if i==j:
        if ring[i-1]==c:
            print(1)
        else:
            print(0)
    else:
        print(d[c][j]-d[c][i-1])