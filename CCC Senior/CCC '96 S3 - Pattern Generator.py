import sys
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))
amount=readint()
N=0
A=[0]*31
def solve(n,k,o):
    #print(n,k,o)
    if n==0 and k==0:
        for i in range(o):
            print(A[i],end='')
        print()
    else:
        if k>0:
            A[o-n]=1
            solve(n-1,k-1,o)
        if n>k:
            A[o-n]=0
            solve(n-1,k,o)
               

for _ in range(amount):
    N,K=gi()
    print('The bit patterns are')
    solve(N,K,N)
    print()