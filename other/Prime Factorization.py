import sys
from math import sqrt,ceil
input = sys.stdin.readline

def listofprimes(g):
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
    return(primes)

for _ in range(int(input())):
    things=[]
    number=int(input())
    possible=listofprimes(ceil(sqrt(number)))
    #print(possible)
    for x in range(len(possible)):
        while(True):
            if number%possible[x]==0:
                things.append(possible[x])
                number=number//possible[x]
            else:
                break
        
    if len(things)==0:
        print(number)
    else:
        if number==1:
            print(*things)
        else:
            things.append(number)
            print(*things)
        
    
'''
1
666
'''