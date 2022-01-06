import sys
from math import ceil,sqrt
input=sys.stdin.readline


def listofprimes(g):
    ls=[False for _ in range(g-1)]
    p=2
    ls[p-2]=True
    primes=[]
    while (True):
        try:
            for f in range(2,g//p+1):
                ls[f*p-2]=True
            primes.append(p)
            try:
                p=ls.index(False)+2
                ls[p-2]=True
            except(ValueError):
                break
        except(IndexError):
            break
    return(primes)
thing=int(input())
if thing==1:
    raise SystemExit()
primes=listofprimes(ceil(sqrt(thing)))
proper=[]
for x in primes:
    while(True):
        if thing%x==0:
            proper.append(x)
            thing=thing//x
        else:break
if len(proper)==0:
    print(thing)
else:
    if thing>1:
        proper.append(thing)
    print(*proper,sep='\n')