import sys
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))

def solve(N):
    c=0
    sieve = [False]*(N+1)
    sieve[0]=True
    sieve[1]=True
    for i in range(2,N+1):
        if sieve[i]:
            continue
        for h in range(i*2,N+1,i):
            sieve[h]=True
        '''for x in range(0,N+1,X):
            if x+i<N:
                c+=2
            elif x+i==N:
                c+=1'''
        c+=((N-i)//X)+1
        c+=((N-i-1)//X)+1
    return(c)

N,X=gi()
if N<=1:
    raise SystemExit(print(0))
print(solve(N))