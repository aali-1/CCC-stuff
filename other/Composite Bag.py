from math import sqrt,ceil
import sys
input=sys.stdin.readline

def isprime(N):
    if N==0 or N==1: return False
    for x in range(2,ceil(sqrt(N))+1):
        if N%x==0 and N!=x:
            return False
    return True
c=0
for _ in range(int(input())):
    num=int(input())
    if not isprime(num):
        c+=1
print(c) 