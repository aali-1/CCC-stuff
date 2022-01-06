import sys
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))
N,M,K=gi()
if K==0:
    print(0)
    sys.exit()
A=[M]*N
D=[M]+[0 for _ in range(N)]
for _ in range(M):
    a,b=gi()
    D[a-1]-=1
    D[b]+=1
A[0]=D[0]
for i in range(1,N):
    A[i]=D[i]+A[i-1]
for i in range(1,N):
    A[i]+=A[i-1]
A=[0]+A
mini=float('inf')
one=0
two=0
while(two<=N):
    try:
        sm=A[two]-A[one]
    except(IndexError):
        if mini==float('inf'):
            print(-1)
        else:
            print(mini)
        sys.exit()
    if sm>=K:
        mini=min(mini,two-one)
        one+=1
    else:
        two+=1
print(mini if mini != float('inf') else -1)