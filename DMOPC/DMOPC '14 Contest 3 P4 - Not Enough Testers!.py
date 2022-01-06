import sys
import bisect
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))
print=sys.stdout.write

maxi=100001
d={}
precomp=[1]*(maxi+1)
for x in range(2,maxi):
    for y in range(x,(maxi+1),x):
        precomp[y]+=1    
for x in range(maxi):
    try:
        d[precomp[x]].append(x)
    except:
        d[precomp[x]]=[x]
#print(d)
for _ in range(readint()):
    K,A,B=gi()
    try:
        cc=d[K].copy()
    except:
        print('0\n')
        continue
    two=bisect.bisect_right(cc,B)
    one=bisect.bisect_left(cc,A)
    print(str(two-one)+'\n')