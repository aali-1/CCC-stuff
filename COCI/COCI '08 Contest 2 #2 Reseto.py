import sys
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))
emp = lambda x, y: [x for _ in range(y)]

def modifiedsieve(N,K):
    sieve = [False]*(N+1)
    sieve[0]=True
    sieve[1]=True
    count=0
    for i in range(2,N+1):
        if sieve[i]==True:
            continue
        for h in range(i,N+1,i):
            #print(h)
            if not sieve[h]:
                count+=1
            if count==K:
                return h
            sieve[h]=True
    return h

line=gi()
print(modifiedsieve(line[0],line[1]))