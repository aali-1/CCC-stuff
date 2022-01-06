import sys
from bisect import bisect_left
class label(Exception): pass
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))
maxn= 10000001
primes=[]


sieve = [False]*(maxn+1)
sieve[0]=True
sieve[1]=True
for i in range(2,maxn):
    if not sieve[i]:
        primes.append(i)    
        for h in range(i<<1,maxn+1,i):
            sieve[h]=True
print(sieve[15])
for _ in range(5):
    N=readint()
    if not sieve[N]:
        print(f"{N} = {N}")
        continue
    try:
        if N%2==1:
            tempp=bisect_left(primes,(N//3))
            c=1
            a=0
            while(c>a):
                c=primes[tempp]
                #print(c)
                t=N-c
                what=bisect_left(primes,(t//2)+1)
                for i in range(what):
                    if not sieve[t-primes[i]]:
                        a=primes[i]
                        b=t-primes[i]
                tempp-=1
            f=sorted([c,a,b])
            print(f"{N} = {f[0]} + {f[1]} + {f[2]}")
        else:
            tempp=reversed([x for x in primes if x<=(N//2)+1])
            for x in tempp:
                if not sieve[N-x]:
                    f=sorted([x,N-x])
                    print(f"{N} = {f[0]} + {f[1]}")
                    raise label()
    except label:
        pass
                        
            
    