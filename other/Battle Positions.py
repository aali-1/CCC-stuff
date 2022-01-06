import sys
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))
I=readint()
arr=[0]*(I+1)
N=readint()
J=readint()
ans=0
for _ in range(J):
    XI,XF,K=gi()
    arr[XI-1]+=K
    arr[XF]-=K
for i in range(1,I):
    arr[i]+=arr[i-1]
for i in range(I):
    ans+=int(arr[i]<N)
print(ans)