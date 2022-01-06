import sys
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))
n,m=gi()
one=set(readline().split())
two=set(readline().split())
c=0
for x in one:
    if x in two:
        c+=1
print(c)