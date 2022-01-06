import sys
input = sys.stdin.readline
def listofprimes(a,g):
    ls=[False for _ in range(g-1)]
    p=2
    ls[p-2]=True
    primes=[]
    while (True):
        for f in range(2,g//p+1):
    
            ls[f*p-2]=True
        primes.append(p)
        try:
            p=ls.index(False)+2
            ls[p-2]=True
        except(ValueError):
            break
    return([x for x in primes if x > a])
for _ in range(int(input())):
    one,two=[int(x) for x in input().split()]
    print(len(listofprimes(one-1,two-1)))
