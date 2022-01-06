import sys
from math import ceil,sqrt,floor
input=sys.stdin.readline
def isprime(N):
    if N==0 or N==1: return False
    for x in range(2,floor(sqrt(N))+1):
        if N%x==0 and N!=x:
            return False
    return True

for _ in range(5):
    num=int(input())
    ps={}
    for k in range(2,num+1):
        #print(k,ps)
        if isprime(k):
            ps[k]=1
            continue
        j = 2
        while j * j <= k:
            if k % j:
                j += 1
            else:
                k //= j
                ps[j]+=1
        if k > 1:
            ps[k]+=1
    stop=max(ps.keys())
    for x in ps:
        print(x,"^",ps[x],sep='',end=' ')
        if x!=stop:
            print('*',end=' ')
    print()