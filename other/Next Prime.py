import sys
from math import sqrt,floor
N=int(sys.stdin.readline())
def isprime(N):
    if N==0 or N==1: return False
    for x in range(2,floor(sqrt(N))+1):
        if N%x==0 and N!=x:
            return False
    return True
for x in range(N,20000000001):
    if x<0:
        continue
    elif isprime(x):
        print(x)
        sys.exit()
