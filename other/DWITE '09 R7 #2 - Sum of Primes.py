import sys
from math import sqrt,floor
input=sys.stdin.readline
def isprime(N):
    if N==0 or N==1: return False
    for x in range(2,floor(sqrt(N))+1):
        if N%x==0 and N!=x:
            return False
    return True
def sumofprimes(g):
    suma=0
    for d in range(2,g+1):
        if isprime(d):
            suma+=d
    return suma
for _ in range(5):
    print(sumofprimes(int(input())))