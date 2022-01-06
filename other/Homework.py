import sys
from math import floor,sqrt
input = sys.stdin.readline
maximum=10000001
def isprime(N):
    if N==0 or N==1: return False
    for x in range(2,floor(sqrt(N))+1):
        if N%x==0 and N!=x:
            return False
    return True
count=0
precomp=[0]*(maximum+1)
for i in range(2,maximum):
    if precomp[i]>0:
        continue
    for f in range(i*2,maximum,i):
        precomp[f]+=1
    precomp[i]=1
    #print(i,precomp)
for h in range(int(input())):
    a,b,k=[int(x) for x in input().split()]
    print(f"Case #{h+1}: {precomp[a:b+1].count(k)}")